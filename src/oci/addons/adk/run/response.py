# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
ADK run response
"""

import json
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, computed_field

from oci.addons.adk.logger import default_logger as logger
from oci.addons.adk.run.types import RawResponse, RequiredAction, GuardrailResult, GuardrailFinding


class RunResponse(BaseModel):
    """Response from the agent run containing the final output."""
    raw_responses: List[RawResponse] = Field(..., description="Accumulated list of raw response from agent.")
    data: Dict[str, Any] | None = Field(default=None, description="Last response from the agent")
    session_id: str = Field(..., description="Session ID used for the response")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def final_output(self) -> str | None:
        """Direct access to the agent message text as output"""
        return self._get_nested_text()

    @computed_field(deprecated="Use 'final_output' instead")  # type: ignore[prop-decorator]
    @property
    def output(self) -> str | None:
        """Direct access to the agent message text as output"""
        return self.final_output

    @computed_field
    def last_guardrail_result(self) -> GuardrailResult | None:
        """Direct access to the last agent guardrail result"""
        return self.raw_responses[-1].get_guardrail_result() if len(self.raw_responses) > 0 else None

    @computed_field
    def first_guardrail_result(self) -> GuardrailResult | None:
        """Direct access to the first agent guardrail result"""
        return self.raw_responses[0].get_guardrail_result() if len(self.raw_responses) > 0 else None

    @computed_field
    def messages(self) -> List[str | None]:
        """Get all chat message content text."""
        return [raw_response.get_nested_text() for raw_response in self.raw_responses]

    @computed_field
    def required_actions(self) -> List[List[RequiredAction] | None]:
        """Get all required actions results."""
        return [raw_response.get_required_action() for raw_response in self.raw_responses]

    @computed_field
    def guardrail_results(self) -> List[GuardrailResult | None]:
        """Get all guardrail results."""
        return [raw_response.get_guardrail_result() for raw_response in self.raw_responses]

    def _format_guardrail_result(self) -> str:
        """Format the guardrail result into human-readable form."""
        messages = []

        # Parse and validate the guardrail result from JSON
        guardrail_result = None
        if self.data and "guardrail_result" in self.data:
            guardrail_result = GuardrailResult.model_validate(
                json.loads(self.data["guardrail_result"])
            )

        if not guardrail_result:
            return "No guardrail issues detected."

        for location in ["input", "output"]:
            content: Optional[GuardrailFinding] = getattr(guardrail_result, location, None)
            if not content:
                continue

            # Content Moderation
            if content.content_moderation:
                for category, score in content.content_moderation.model_dump().items():
                    messages.append(
                        f"Content moderation detected - {category.upper()} with score {score} in {location.lower()}"
                    )

            # Prompt Injection
            if content.prompt_injection:
                score = content.prompt_injection.score
                messages.append(
                    f"Prompt injection risk detected with score {score} in {location.lower()}"
                )

            # Personally Identifiable Information
            personally_identifiable_information = content.personally_identifiable_information
            if personally_identifiable_information:
                for pii in personally_identifiable_information:
                    messages.append(
                        f"Personally identifiable information detected with ({pii.label}): '{pii.text}' in {location.lower()}"
                    )
        return "\n".join(messages) if messages else "No guardrail issues detected."

    def _get_nested_text(self) -> str | None:
        """Safely extract text from nested data structure."""
        try:
            return self.raw_responses[-1].get_nested_text()
        except (KeyError, TypeError):
            return None

    def pretty_print(self, print_data: bool = False) -> None:
        """Pretty print this run response."""
        if self.final_output is None:
            logger.warning("NO TEXT AVAILABLE IN RESPONSE")

        message_text = f"agent text message:\n[bold green]{self.final_output}[/bold green]"

        if print_data:
            message_text += f"\n\ndata:\n[bold magenta]{json.dumps(self.data, indent=4)}[/bold magenta]"  # noqa: E501
        if self.data is not None and "guardrail_result" in self.data and self.data["guardrail_result"] is not None:
            guardrail_result = self._format_guardrail_result()
            logger.print(
                guardrail_result,
                title="Guardrail Result",
                border_style="blue",
            )
        logger.print(
            message_text,
            title="Agent run response",
            border_style="blue",
        )
