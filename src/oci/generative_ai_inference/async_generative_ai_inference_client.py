# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
Async client for OCI Generative AI Inference service.

This module provides true async support for GenAI operations,
enabling non-blocking concurrent requests for high-throughput applications.

Example usage:
    ```python
    import asyncio
    from oci.generative_ai_inference import AsyncGenerativeAiInferenceClient
    from oci.generative_ai_inference.models import (
        ChatDetails, OnDemandServingMode, GenericChatRequest, UserMessage, TextContent
    )

    async def main():
        async with AsyncGenerativeAiInferenceClient(config) as client:
            # Single request
            response = await client.chat(chat_details)

            # Concurrent requests
            responses = await asyncio.gather(
                client.chat(chat_details_1),
                client.chat(chat_details_2),
                client.chat(chat_details_3),
            )

            # Streaming
            async for event in client.chat_stream(chat_details):
                print(event)

    asyncio.run(main())
    ```
"""

from __future__ import absolute_import

from typing import Any, AsyncIterator, Dict

from oci.async_base_client import AsyncBaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from oci.exceptions import InvalidAlloyConfig
from oci.alloy import OCI_SDK_ENABLED_SERVICES_SET
from .models import generative_ai_inference_type_mapping

missing = Sentinel("Missing")


class AsyncGenerativeAiInferenceClient:
    """
    Async client for OCI Generative AI Inference service.

    Provides true async/await support for chat, text generation,
    summarization, and embeddings operations.
    """

    def __init__(self, config: Dict[str, Any], **kwargs):
        """
        Create async client for OCI Generative AI Inference.

        Args:
            config: OCI config dictionary (from oci.config.from_file())

        Keyword Args:
            service_endpoint: Override service endpoint URL
            signer: Custom signer (default: create from config)
            timeout: Request timeout in seconds (default: 300)
        """
        if not OCI_SDK_ENABLED_SERVICES_SET.is_service_enabled("generative_ai_inference"):
            raise InvalidAlloyConfig(
                "The Alloy configuration has disabled this service"
            )

        validate_config(config, signer=kwargs.get("signer"))

        # Get or create signer
        if "signer" in kwargs:
            signer = kwargs["signer"]
        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)
        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content"),
            )

        # Build service endpoint
        service_endpoint = kwargs.get("service_endpoint")
        if not service_endpoint:
            region = config.get("region", "us-chicago-1")
            service_endpoint = f"https://inference.generativeai.{region}.oci.oraclecloud.com"

        self._client = AsyncBaseClient(
            service="generative_ai_inference",
            config=config,
            signer=signer,
            type_mapping=generative_ai_inference_type_mapping,
            service_endpoint=service_endpoint,
            base_path="/20231130",
            timeout=kwargs.get("timeout", 300),
        )

    async def chat(
        self,
        chat_details: Any,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create chat response (non-streaming).

        Args:
            chat_details: ChatDetails object with request parameters

        Returns:
            Chat response as dictionary

        Example:
            ```python
            from oci.generative_ai_inference.models import (
                ChatDetails, OnDemandServingMode, GenericChatRequest,
                UserMessage, TextContent
            )

            chat_details = ChatDetails(
                compartment_id="ocid1.compartment...",
                serving_mode=OnDemandServingMode(model_id="meta.llama-3.3-70b-instruct"),
                chat_request=GenericChatRequest(
                    messages=[
                        UserMessage(content=[TextContent(text="Hello!")])
                    ]
                )
            )
            response = await client.chat(chat_details)
            ```
        """
        header_params = {
            "opc-retry-token": kwargs.get("opc_retry_token"),
            "opc-request-id": kwargs.get("opc_request_id"),
        }

        async for response in self._client.call_api_async(
            resource_path="/actions/chat",
            method="POST",
            header_params=header_params,
            body=chat_details,
            response_type="ChatResult",
            stream=False,
        ):
            return response

        raise RuntimeError("No response received from OCI GenAI")

    async def chat_stream(
        self,
        chat_details: Any,
        **kwargs
    ) -> AsyncIterator[Dict[str, Any]]:
        """
        Create streaming chat response.

        Args:
            chat_details: ChatDetails object with request parameters
                (ensure chat_request.is_stream = True)

        Yields:
            Server-sent events as dictionaries

        Example:
            ```python
            chat_details = ChatDetails(
                compartment_id="ocid1.compartment...",
                serving_mode=OnDemandServingMode(model_id="meta.llama-3.3-70b-instruct"),
                chat_request=GenericChatRequest(
                    messages=[UserMessage(content=[TextContent(text="Tell me a story")])],
                    is_stream=True,
                )
            )
            async for event in client.chat_stream(chat_details):
                print(event)
            ```
        """
        header_params = {
            "opc-retry-token": kwargs.get("opc_retry_token"),
            "opc-request-id": kwargs.get("opc_request_id"),
        }

        async for event in self._client.call_api_async(
            resource_path="/actions/chat",
            method="POST",
            header_params=header_params,
            body=chat_details,
            response_type="ChatResult",
            stream=True,
        ):
            yield event

    async def generate_text(
        self,
        generate_text_details: Any,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generate text completion.

        Args:
            generate_text_details: GenerateTextDetails object

        Returns:
            Generated text response as dictionary
        """
        header_params = {
            "opc-retry-token": kwargs.get("opc_retry_token"),
            "opc-request-id": kwargs.get("opc_request_id"),
        }

        async for response in self._client.call_api_async(
            resource_path="/actions/generateText",
            method="POST",
            header_params=header_params,
            body=generate_text_details,
            response_type="GenerateTextResult",
            stream=False,
        ):
            return response

        raise RuntimeError("No response received from OCI GenAI")

    async def embed_text(
        self,
        embed_text_details: Any,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generate text embeddings.

        Args:
            embed_text_details: EmbedTextDetails object

        Returns:
            Embeddings response as dictionary
        """
        header_params = {
            "opc-retry-token": kwargs.get("opc_retry_token"),
            "opc-request-id": kwargs.get("opc_request_id"),
        }

        async for response in self._client.call_api_async(
            resource_path="/actions/embedText",
            method="POST",
            header_params=header_params,
            body=embed_text_details,
            response_type="EmbedTextResult",
            stream=False,
        ):
            return response

        raise RuntimeError("No response received from OCI GenAI")

    async def summarize_text(
        self,
        summarize_text_details: Any,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Summarize text.

        Args:
            summarize_text_details: SummarizeTextDetails object

        Returns:
            Summary response as dictionary
        """
        header_params = {
            "opc-retry-token": kwargs.get("opc_retry_token"),
            "opc-request-id": kwargs.get("opc_request_id"),
        }

        async for response in self._client.call_api_async(
            resource_path="/actions/summarizeText",
            method="POST",
            header_params=header_params,
            body=summarize_text_details,
            response_type="SummarizeTextResult",
            stream=False,
        ):
            return response

        raise RuntimeError("No response received from OCI GenAI")

    async def close(self):
        """Close the async client."""
        await self._client.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
