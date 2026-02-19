# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""Unit tests for AsyncBaseClient."""

import json
import pytest
from datetime import datetime, date
from unittest.mock import MagicMock, AsyncMock, patch

from oci.async_base_client import AsyncBaseClient
from oci.exceptions import ServiceError
from oci.response import Response
from oci import retry


class TestAsyncBaseClient:
    """Tests for AsyncBaseClient initialization and basic methods."""

    @pytest.fixture
    def mock_signer(self):
        """Create a mock OCI signer."""
        signer = MagicMock()

        def sign_request(prepared_request):
            prepared_request.headers["Authorization"] = "Signature signed"
            return prepared_request

        signer.side_effect = sign_request
        return signer

    @pytest.fixture
    def client(self, mock_signer):
        """Create an AsyncBaseClient instance."""
        return AsyncBaseClient(
            service="test_service",
            config={"region": "us-test-1"},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.endpoint.com",
            base_path="/20231130",
        )

    def test_init(self, client):
        """Test client initialization."""
        assert client.service == "test_service"
        assert client.service_endpoint == "https://test.endpoint.com"
        assert client.base_path == "/20231130"
        assert client.timeout == 300

    def test_init_with_retry_strategy(self, mock_signer):
        """Test client initialization with retry strategy."""
        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
            retry_strategy=retry.DEFAULT_RETRY_STRATEGY,
        )
        assert client.retry_strategy == retry.DEFAULT_RETRY_STRATEGY

    def test_init_with_slots(self, client):
        """Test that __slots__ is properly defined."""
        assert hasattr(AsyncBaseClient, '__slots__')
        # Should not be able to add arbitrary attributes
        with pytest.raises(AttributeError):
            client.arbitrary_attribute = "test"

    def test_build_url(self, client):
        """Test URL building."""
        url = client._build_url("/actions/chat")
        assert url == "https://test.endpoint.com/20231130/actions/chat"

    def test_sanitize_primitive_types(self, client):
        """Test serialization of primitive types."""
        assert client._sanitize_for_serialization(None) is None
        assert client._sanitize_for_serialization("hello") == "hello"
        assert client._sanitize_for_serialization(42) == 42
        assert client._sanitize_for_serialization(3.14) == 3.14
        assert client._sanitize_for_serialization(True) is True

    def test_sanitize_list(self, client):
        """Test serialization of lists."""
        result = client._sanitize_for_serialization([1, "two", 3.0])
        assert result == [1, "two", 3.0]

    def test_sanitize_dict(self, client):
        """Test serialization of dicts."""
        result = client._sanitize_for_serialization({"key": "value", "num": 42})
        assert result == {"key": "value", "num": 42}

    def test_sanitize_datetime(self, client):
        """Test serialization of datetime."""
        dt = datetime(2024, 1, 15, 12, 30, 45)
        result = client._sanitize_for_serialization(dt)
        assert "2024-01-15" in result
        assert result.endswith("Z")

    def test_sanitize_date(self, client):
        """Test serialization of date."""
        d = date(2024, 1, 15)
        result = client._sanitize_for_serialization(d)
        assert result == "2024-01-15"

    def test_sanitize_oci_model(self, client):
        """Test serialization of OCI model objects."""
        # Create mock OCI model
        mock_model = MagicMock()
        mock_model.swagger_types = {"model_id": "str", "compartment_id": "str"}
        mock_model.attribute_map = {
            "model_id": "modelId",
            "compartment_id": "compartmentId",
        }
        mock_model.model_id = "test-model"
        mock_model.compartment_id = "test-compartment"

        result = client._sanitize_for_serialization(mock_model)

        assert result == {
            "modelId": "test-model",
            "compartmentId": "test-compartment",
        }

    def test_serialize_body_none(self, client):
        """Test body serialization with None."""
        assert client._serialize_body(None) is None

    def test_serialize_body_dict(self, client):
        """Test body serialization with dict."""
        result = client._serialize_body({"key": "value"})
        assert json.loads(result) == {"key": "value"}

    def test_sign_request(self, client, mock_signer):
        """Test request signing."""
        headers = client._sign_request(
            method="POST",
            url="https://test.endpoint.com/actions/chat",
            headers={"content-type": "application/json"},
            body_str='{"test": "data"}',
        )
        assert "Authorization" in headers
        mock_signer.assert_called_once()


class TestAsyncBaseClientDeserialization:
    """Tests for AsyncBaseClient deserialization."""

    @pytest.fixture
    def mock_signer(self):
        signer = MagicMock()
        signer.side_effect = lambda req: req
        return signer

    @pytest.fixture
    def client_with_types(self, mock_signer):
        """Create client with type mappings."""
        # Mock type mapping
        class MockChatResult:
            swagger_types = {"chat_response": "dict(str, object)"}
            attribute_map = {"chat_response": "chatResponse"}

            def __init__(self):
                self.chat_response = None

        return AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={"ChatResult": MockChatResult},
            service_endpoint="https://test.com",
        )

    def test_deserialize_primitive_str(self, client_with_types):
        """Test deserializing string."""
        result = client_with_types._deserialize("hello", "str")
        assert result == "hello"

    def test_deserialize_primitive_int(self, client_with_types):
        """Test deserializing int."""
        result = client_with_types._deserialize(42, "int")
        assert result == 42

    def test_deserialize_list(self, client_with_types):
        """Test deserializing list."""
        result = client_with_types._deserialize([1, 2, 3], "list[int]")
        assert result == [1, 2, 3]

    def test_deserialize_dict(self, client_with_types):
        """Test deserializing dict."""
        result = client_with_types._deserialize({"a": "b"}, "dict(str, str)")
        assert result == {"a": "b"}

    def test_deserialize_date(self, client_with_types):
        """Test deserializing date."""
        result = client_with_types._deserialize_date("2024-01-15")
        assert result == date(2024, 1, 15)

    def test_deserialize_datetime(self, client_with_types):
        """Test deserializing datetime."""
        result = client_with_types._deserialize_datetime("2024-01-15T12:30:45.000Z")
        assert result.year == 2024
        assert result.month == 1
        assert result.day == 15


class TestAsyncBaseClientRetry:
    """Tests for AsyncBaseClient retry functionality."""

    @pytest.fixture
    def mock_signer(self):
        signer = MagicMock()
        signer.side_effect = lambda req: req
        return signer

    def test_get_retry_strategy_operation_level(self, mock_signer):
        """Test operation-level retry takes precedence."""
        client_strategy = retry.NoneRetryStrategy()
        op_strategy = retry.DEFAULT_RETRY_STRATEGY

        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
            retry_strategy=client_strategy,
        )

        result = client._get_retry_strategy(op_strategy)
        assert result == op_strategy

    def test_get_retry_strategy_client_level(self, mock_signer):
        """Test client-level retry is used when no operation strategy."""
        client_strategy = retry.DEFAULT_RETRY_STRATEGY

        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
            retry_strategy=client_strategy,
        )

        result = client._get_retry_strategy(None)
        assert result == client_strategy

    def test_get_retry_strategy_none(self, mock_signer):
        """Test None strategy when no retry configured."""
        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
        )

        # Mock global strategy as None
        with patch.object(retry, 'GLOBAL_RETRY_STRATEGY', None):
            result = client._get_retry_strategy(None)
            assert result is None


class TestAsyncBaseClientContextManager:
    """Tests for AsyncBaseClient context manager."""

    @pytest.fixture
    def mock_signer(self):
        signer = MagicMock()
        signer.side_effect = lambda req: req
        return signer

    @pytest.mark.asyncio
    async def test_context_manager(self, mock_signer):
        """Test async context manager."""
        async with AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
        ) as client:
            assert client is not None

    @pytest.mark.asyncio
    async def test_close(self, mock_signer):
        """Test client close."""
        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
        )
        # Create a session
        await client._get_session()
        # Close should work
        await client.close()
        assert client._session is None or client._session.closed

    @pytest.mark.asyncio
    async def test_session_lock_prevents_race(self, mock_signer):
        """Test that session creation is thread-safe."""
        import asyncio

        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
        )

        # Get session multiple times concurrently
        sessions = await asyncio.gather(
            client._get_session(),
            client._get_session(),
            client._get_session(),
        )

        # All should return the same session
        assert sessions[0] is sessions[1] is sessions[2]
        await client.close()


class TestAsyncBaseClientAPICall:
    """Tests for AsyncBaseClient API calls."""

    @pytest.fixture
    def mock_signer(self):
        signer = MagicMock()
        signer.side_effect = lambda req: req
        return signer

    @pytest.mark.asyncio
    async def test_call_api_success(self, mock_signer):
        """Test successful API call returns Response object."""
        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
            base_path="/v1",
            skip_deserialization=True,
        )

        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.headers = {"opc-request-id": "test-id"}
        mock_response.json = AsyncMock(return_value={"result": "success"})

        with patch("aiohttp.ClientSession.request") as mock_request:
            mock_request.return_value.__aenter__ = AsyncMock(return_value=mock_response)
            mock_request.return_value.__aexit__ = AsyncMock(return_value=None)

            response = await client.call_api(
                resource_path="/test",
                method="GET",
            )

            assert isinstance(response, Response)
            assert response.status == 200
            assert response.data == {"result": "success"}
            assert response.request_id == "test-id"

        await client.close()

    @pytest.mark.asyncio
    async def test_call_api_error_raises_service_error(self, mock_signer):
        """Test API call error raises ServiceError."""
        client = AsyncBaseClient(
            service="test_service",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
        )

        mock_response = AsyncMock()
        mock_response.status = 400
        mock_response.headers = {"opc-request-id": "error-id"}
        mock_response.text = AsyncMock(
            return_value='{"code": "InvalidParameter", "message": "Bad Request"}'
        )

        with patch("aiohttp.ClientSession.request") as mock_request:
            mock_request.return_value.__aenter__ = AsyncMock(return_value=mock_response)
            mock_request.return_value.__aexit__ = AsyncMock(return_value=None)

            with pytest.raises(ServiceError) as exc_info:
                await client.call_api(
                    resource_path="/test",
                    method="GET",
                )

            error = exc_info.value
            assert error.status == 400
            assert error.code == "InvalidParameter"
            assert "Bad Request" in error.message
            assert error.target_service == "test_service"

        await client.close()

    @pytest.mark.asyncio
    async def test_call_api_stream_success(self, mock_signer):
        """Test streaming API call."""
        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
        )

        # Create async iterator for response content
        async def mock_content():
            yield b"data: {\"chunk\": 1}\n"
            yield b"\n"
            yield b"data: {\"chunk\": 2}\n"
            yield b"data: [DONE]\n"

        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.headers = {}
        mock_response.content = mock_content()

        with patch("aiohttp.ClientSession.request") as mock_request:
            mock_request.return_value.__aenter__ = AsyncMock(return_value=mock_response)
            mock_request.return_value.__aexit__ = AsyncMock(return_value=None)

            chunks = []
            async for chunk in client.call_api_stream(
                resource_path="/test",
                method="POST",
            ):
                chunks.append(chunk)

            assert len(chunks) == 2
            assert chunks[0] == {"chunk": 1}
            assert chunks[1] == {"chunk": 2}

        await client.close()

    @pytest.mark.asyncio
    async def test_call_api_with_deserialization(self, mock_signer):
        """Test API call with response deserialization."""

        class MockResult:
            swagger_types = {"name": "str", "count": "int"}
            attribute_map = {"name": "name", "count": "count"}

            def __init__(self):
                self.name = None
                self.count = None

        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={"MockResult": MockResult},
            service_endpoint="https://test.com",
        )

        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.headers = {}
        mock_response.json = AsyncMock(return_value={"name": "test", "count": 42})

        with patch("aiohttp.ClientSession.request") as mock_request:
            mock_request.return_value.__aenter__ = AsyncMock(return_value=mock_response)
            mock_request.return_value.__aexit__ = AsyncMock(return_value=None)

            response = await client.call_api(
                resource_path="/test",
                method="GET",
                response_type="MockResult",
            )

            assert isinstance(response.data, MockResult)
            assert response.data.name == "test"
            assert response.data.count == 42

        await client.close()

    @pytest.mark.asyncio
    async def test_call_api_with_retry_on_throttle(self, mock_signer):
        """Test that 429 errors trigger retry."""
        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
            skip_deserialization=True,
        )

        call_count = 0

        async def mock_request_side_effect(*args, **kwargs):
            nonlocal call_count
            call_count += 1

            mock_response = AsyncMock()
            if call_count < 3:
                mock_response.status = 429
                mock_response.headers = {}
                mock_response.text = AsyncMock(
                    return_value='{"code": "TooManyRequests", "message": "Rate limited"}'
                )
            else:
                mock_response.status = 200
                mock_response.headers = {}
                mock_response.json = AsyncMock(return_value={"success": True})

            context = AsyncMock()
            context.__aenter__ = AsyncMock(return_value=mock_response)
            context.__aexit__ = AsyncMock(return_value=None)
            return context

        with patch("aiohttp.ClientSession.request", side_effect=mock_request_side_effect):
            # Use a simple retry strategy that retries on 429
            response = await client.call_api(
                resource_path="/test",
                method="GET",
                retry_strategy=retry.DEFAULT_RETRY_STRATEGY,
            )

            assert response.status == 200
            assert response.data == {"success": True}
            assert call_count == 3  # 2 failures + 1 success

        await client.close()
