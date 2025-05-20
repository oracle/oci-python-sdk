# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
ADK run response
"""

import json
from typing import Any, Dict

from pydantic import BaseModel, Field, computed_field

from oci.addons.adk.logger import default_logger as logger


class RunResponse(BaseModel):
    """Response from the agent run containing the final output."""

    data: Dict[str, Any] = Field(..., description="Raw response from the agent")
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

    def _get_nested_text(self) -> str | None:
        """Safely extract text from nested data structure."""
        try:
            return self.data["message"]["content"]["text"]
        except (KeyError, TypeError):
            return None

    def pretty_print(self, print_data: bool = False) -> None:
        """Pretty print this run response."""
        if self.final_output is None:
            logger.warning("NO TEXT AVAILABLE IN RESPONSE")

        message_text = f"agent text message:\n[bold green]{self.final_output}[/bold green]"

        if print_data:
            message_text += f"\n\ndata:\n[bold magenta]{json.dumps(self.data, indent=4)}[/bold magenta]"  # noqa: E501

        logger.print(
            message_text,
            title="Agent run response",
            border_style="blue",
        )
