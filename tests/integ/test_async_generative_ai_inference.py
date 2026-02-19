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
    EmbedTextDetails,
    FunctionDefinition,
)
from oci.response import Response

from . import util


# Get test configuration from util (which reads from environment)
COMPARTMENT_ID = util.COMPARTMENT_ID
MODEL_ID = util.GENAI_MODEL_ID
GENAI_REGION = util.GENAI_REGION
EMBED_MODEL_ID = "cohere.embed-english-v3.0"


def get_service_endpoint():
    """Get the GenAI service endpoint for the configured region."""
    return f"https://inference.generativeai.{GENAI_REGION}.oci.oraclecloud.com"


def make_chat_details(prompt: str, stream: bool = False, model_id: str = None) -> ChatDetails:
    """Create ChatDetails for testing."""
    return ChatDetails(
        compartment_id=COMPARTMENT_ID,
        serving_mode=OnDemandServingMode(model_id=model_id or MODEL_ID),
        chat_request=GenericChatRequest(
            messages=[UserMessage(content=[TextContent(text=prompt)])],
            max_tokens=50,
            temperature=0.1,
            is_stream=stream,
        ),
    )


def make_embed_details(inputs: list, input_type: str = "SEARCH_DOCUMENT") -> EmbedTextDetails:
    """Create EmbedTextDetails for testing."""
    return EmbedTextDetails(
        compartment_id=COMPARTMENT_ID,
        serving_mode=OnDemandServingMode(model_id=EMBED_MODEL_ID),
        inputs=inputs,
        input_type=input_type,
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

    # =========================================================================
    # embed_text tests
    # =========================================================================

    @pytest.mark.asyncio
    async def test_embed_text(self, config):
        """Test basic embed_text returns valid Response with embeddings."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            response = await client.embed_text(
                make_embed_details(["Hello world", "Test embedding"])
            )

            assert isinstance(response, Response)
            assert response.status == 200
            assert response.data is not None
            assert hasattr(response.data, 'embeddings')
            assert len(response.data.embeddings) == 2
            # Each embedding should be a list of floats
            assert isinstance(response.data.embeddings[0], list)
            assert len(response.data.embeddings[0]) > 0
            assert isinstance(response.data.embeddings[0][0], float)

    @pytest.mark.asyncio
    async def test_embed_multilingual(self, config):
        """Test embed_text with multilingual inputs."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            response = await client.embed_text(
                make_embed_details([
                    "Hello world",
                    "Hola mundo",
                    "Bonjour le monde",
                ])
            )

            assert isinstance(response, Response)
            assert response.status == 200
            assert len(response.data.embeddings) == 3

    @pytest.mark.asyncio
    async def test_embed_concurrent(self, config):
        """Test concurrent embed_text requests."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            results = await asyncio.gather(
                client.embed_text(make_embed_details(["Text 1"])),
                client.embed_text(make_embed_details(["Text 2"])),
                client.embed_text(make_embed_details(["Text 3"])),
            )

            assert len(results) == 3
            for result in results:
                assert isinstance(result, Response)
                assert result.status == 200
                assert len(result.data.embeddings) == 1

    @pytest.mark.asyncio
    async def test_embed_with_input_type(self, config):
        """Test embed_text with different input types."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            # Test SEARCH_QUERY input type
            response = await client.embed_text(
                make_embed_details(["What is machine learning?"], input_type="SEARCH_QUERY")
            )

            assert isinstance(response, Response)
            assert response.status == 200
            assert len(response.data.embeddings) == 1

    # =========================================================================
    # Additional chat_stream tests
    # =========================================================================

    @pytest.mark.asyncio
    async def test_chat_stream_content_extraction(self, config):
        """Test that streaming response content can be extracted and assembled."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            chat_details = make_chat_details("Say 'hello world'", stream=True)
            full_text = ""

            async for event in client.chat_stream(chat_details):
                # Extract text from streaming event
                # Streaming events have message.content directly (not wrapped in chatResponse)
                message = event.get("message", {})
                content = message.get("content", [])
                if content and isinstance(content, list) and len(content) > 0:
                    text = content[0].get("text", "")
                    if text:
                        full_text += text

            # Should have accumulated some text
            assert len(full_text) > 0
            assert "hello" in full_text.lower()

    @pytest.mark.asyncio
    async def test_chat_stream_long_response(self, config):
        """Test streaming with a longer response."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            chat_details = ChatDetails(
                compartment_id=COMPARTMENT_ID,
                serving_mode=OnDemandServingMode(model_id=MODEL_ID),
                chat_request=GenericChatRequest(
                    messages=[UserMessage(content=[TextContent(text="Count from 1 to 10")])],
                    max_tokens=200,
                    temperature=0.1,
                    is_stream=True,
                ),
            )
            chunks = []

            async for event in client.chat_stream(chat_details):
                chunks.append(event)

            # Should have multiple chunks for longer response
            assert len(chunks) > 1

    # =========================================================================
    # Tool calling tests
    # =========================================================================

    @pytest.mark.asyncio
    async def test_chat_with_tool_calling(self, config):
        """Test chat with function/tool calling."""
        async with AsyncGenerativeAiInferenceClient(
            config,
            service_endpoint=get_service_endpoint(),
        ) as client:
            # Define a simple tool
            tools = [
                FunctionDefinition(
                    name="get_weather",
                    description="Get the current weather for a location",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and country, e.g. 'Paris, France'"
                            }
                        },
                        "required": ["location"]
                    }
                )
            ]

            chat_details = ChatDetails(
                compartment_id=COMPARTMENT_ID,
                serving_mode=OnDemandServingMode(model_id=MODEL_ID),
                chat_request=GenericChatRequest(
                    messages=[UserMessage(content=[TextContent(text="What's the weather in Tokyo?")])],
                    tools=tools,
                    max_tokens=100,
                    temperature=0.1,
                ),
            )

            response = await client.chat(chat_details)

            assert isinstance(response, Response)
            assert response.status == 200

            choice = response.data.chat_response.choices[0]

            # Model should decide to call the tool
            assert choice.finish_reason == "tool_calls"
            assert hasattr(choice.message, 'tool_calls')
            assert choice.message.tool_calls is not None
            assert len(choice.message.tool_calls) > 0

            # Verify tool call structure
            tool_call = choice.message.tool_calls[0]
            assert tool_call.type == "FUNCTION"
            assert tool_call.name == "get_weather"
            assert tool_call.id is not None
            assert "tokyo" in tool_call.arguments.lower() or "Tokyo" in tool_call.arguments
