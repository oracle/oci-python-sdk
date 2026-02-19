# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""Unit tests for AsyncBaseClient."""

import json
import pytest
from datetime import datetime, date
from unittest.mock import MagicMock, AsyncMock, patch

from oci.async_base_client import AsyncBaseClient


class TestAsyncBaseClient:
    """Tests for AsyncBaseClient."""

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
        async with client._get_session():
            pass
        # Close should work
        await client.close()
        assert client._session is None or client._session.closed


class TestAsyncBaseClientAPICall:
    """Tests for AsyncBaseClient API calls."""

    @pytest.fixture
    def mock_signer(self):
        signer = MagicMock()
        signer.side_effect = lambda req: req
        return signer

    @pytest.mark.asyncio
    async def test_call_api_async_success(self, mock_signer):
        """Test successful API call."""
        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
            base_path="/v1",
        )

        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value={"result": "success"})

        with patch("aiohttp.ClientSession.request") as mock_request:
            mock_request.return_value.__aenter__ = AsyncMock(return_value=mock_response)
            mock_request.return_value.__aexit__ = AsyncMock(return_value=None)

            results = []
            async for data in client.call_api_async(
                resource_path="/test",
                method="GET",
                stream=False,
            ):
                results.append(data)

            assert len(results) == 1
            assert results[0] == {"result": "success"}

        await client.close()

    @pytest.mark.asyncio
    async def test_call_api_async_error(self, mock_signer):
        """Test API call error handling."""
        client = AsyncBaseClient(
            service="test",
            config={},
            signer=mock_signer,
            type_mapping={},
            service_endpoint="https://test.com",
        )

        mock_response = AsyncMock()
        mock_response.status = 400
        mock_response.text = AsyncMock(return_value="Bad Request")

        with patch("aiohttp.ClientSession.request") as mock_request:
            mock_request.return_value.__aenter__ = AsyncMock(return_value=mock_response)
            mock_request.return_value.__aexit__ = AsyncMock(return_value=None)

            with pytest.raises(RuntimeError, match="OCI API request failed"):
                async for _ in client.call_api_async(
                    resource_path="/test",
                    method="GET",
                ):
                    pass

        await client.close()
