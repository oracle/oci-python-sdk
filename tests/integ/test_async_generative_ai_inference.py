# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
Integration tests for AsyncGenerativeAiInferenceClient.

These tests require OCI credentials and access to OCI Generative AI service.
Uses the standard OCI SDK test configuration patterns.

Environment variables:
    OCI_PYSDK_COMPARTMENT_ID: Compartment OCID for testing (required)
    OCI_GENAI_MODEL_ID: Model to use (default: meta.llama-3.3-70b-instruct)
    OCI_GENAI_REGION: Region for GenAI (default: us-chicago-1)
"""

import asyncio
import time
import pytest

from oci.generative_ai_inference import AsyncGenerativeAiInferenceClient
from oci.generative_ai_inference.models import (
    ChatDetails,
    OnDemandServingMode,
    GenericChatRequest,
    UserMessage,
    TextContent,
)
from oci.response import Response

from . import util


# Get test configuration from util (which reads from environment)
COMPARTMENT_ID = util.COMPARTMENT_ID
MODEL_ID = util.GENAI_MODEL_ID
GENAI_REGION = util.GENAI_REGION


def get_service_endpoint():
    """Get the GenAI service endpoint for the configured region."""
    return f"https://inference.generativeai.{GENAI_REGION}.oci.oraclecloud.com"


def make_chat_details(prompt: str, stream: bool = False) -> ChatDetails:
    """Create ChatDetails for testing."""
    return ChatDetails(
        compartment_id=COMPARTMENT_ID,
        serving_mode=OnDemandServingMode(model_id=MODEL_ID),
        chat_request=GenericChatRequest(
            messages=[UserMessage(content=[TextContent(text=prompt)])],
            max_tokens=50,
            temperature=0.1,
            is_stream=stream,
        ),
    )


@pytest.fixture(scope="module")
def async_genai_client(config):
    """Create async GenAI client fixture."""
    client = AsyncGenerativeAiInferenceClient(
        config,
        service_endpoint=get_service_endpoint(),
    )
    yield client
    # Note: Can't use async cleanup in sync fixture, client will be GC'd


@pytest.mark.skipif(
    not COMPARTMENT_ID,
    reason="OCI_PYSDK_COMPARTMENT_ID environment variable not set",
)
class TestAsyncGenerativeAiInference:
    """Integration tests for AsyncGenerativeAiInferenceClient."""

    @pytest.mark.asyncio
    async def test_single_chat_request(self, config):
        """Test single async chat request returns valid Response with ChatResult."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            response = await client.chat(
                make_chat_details("Say 'hello' and nothing else")
            )

            # Response should be an OCI Response object
            assert isinstance(response, Response)
            assert response.status == 200

            # data should be a ChatResult model object
            chat_result = response.data
            assert chat_result is not None
            assert hasattr(chat_result, 'chat_response')

            # Verify chat response content
            chat_response = chat_result.chat_response
            assert hasattr(chat_response, 'choices')
            assert len(chat_response.choices) > 0

            choice = chat_response.choices[0]
            assert hasattr(choice, 'message')
            assert hasattr(choice.message, 'content')
            assert len(choice.message.content) > 0

            text = choice.message.content[0].text.lower()
            assert "hello" in text

    @pytest.mark.asyncio
    async def test_response_has_request_id(self, config):
        """Test that response includes opc-request-id."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            response = await client.chat(make_chat_details("Say hello"))

            assert response.request_id is not None
            assert len(response.request_id) > 0

    @pytest.mark.asyncio
    async def test_concurrent_requests(self, config):
        """Test multiple concurrent async requests complete successfully."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            prompts = [
                "What is 2+2? Answer with just the number.",
                "What is 3+3? Answer with just the number.",
                "What is 4+4? Answer with just the number.",
            ]

            results = await asyncio.gather(
                *[client.chat(make_chat_details(p)) for p in prompts]
            )

            assert len(results) == 3
            for result in results:
                assert isinstance(result, Response)
                assert result.status == 200
                assert result.data is not None
                assert hasattr(result.data, 'chat_response')
                assert len(result.data.chat_response.choices) > 0

    @pytest.mark.asyncio
    async def test_streaming_response(self, config):
        """Test streaming chat response yields chunks."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            chat_details = make_chat_details("Count to 3", stream=True)
            chunks = []

            async for event in client.chat_stream(chat_details):
                chunks.append(event)

            # Streaming still returns raw dicts
            assert len(chunks) > 0
            assert isinstance(chunks[0], dict)

    @pytest.mark.asyncio
    async def test_concurrent_faster_than_sequential(self, config):
        """Verify concurrent requests are faster than sequential."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            prompts = [
                "What is 1+1?",
                "What is 2+2?",
                "What is 3+3?",
            ]

            # Sequential timing
            start = time.perf_counter()
            for p in prompts:
                await client.chat(make_chat_details(p))
            sequential_time = time.perf_counter() - start

            # Concurrent timing
            start = time.perf_counter()
            await asyncio.gather(
                *[client.chat(make_chat_details(p)) for p in prompts]
            )
            concurrent_time = time.perf_counter() - start

            # Concurrent should be faster (allow margin for variance)
            assert concurrent_time <= sequential_time * 1.5, (
                f"Concurrent ({concurrent_time:.2f}s) should be faster than "
                f"sequential ({sequential_time:.2f}s)"
            )

    @pytest.mark.asyncio
    async def test_context_manager(self, config):
        """Test client works as async context manager."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            response = await client.chat(make_chat_details("Say hello"))
            assert response is not None
            assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_explicit_close(self, config):
        """Test explicit client close."""
        client = AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        )
        try:
            response = await client.chat(make_chat_details("Say hello"))
            assert response is not None
            assert isinstance(response, Response)
        finally:
            await client.close()

    @pytest.mark.asyncio
    async def test_multiple_requests_same_client(self, config):
        """Test multiple sequential requests with same client instance."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            for i in range(3):
                response = await client.chat(make_chat_details(f"Say {i}"))
                assert response is not None
                assert isinstance(response, Response)
                assert response.data is not None
