# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
Async base client for OCI services using aiohttp.

This module provides true async HTTP support for OCI services,
enabling non-blocking concurrent requests.
"""

from __future__ import absolute_import

import json
import logging
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Any, AsyncIterator, Dict, Optional, Type

import aiohttp
from ._vendor import requests

from .version import __version__

logger = logging.getLogger(__name__)

USER_INFO = "Oracle-PythonSDK-Async/{}".format(__version__)


class AsyncBaseClient:
    """
    Async HTTP client for OCI services.

    Uses aiohttp for true async/await support while reusing
    the existing OCI signer for request authentication.
    """

    def __init__(
        self,
        service: str,
        config: Dict[str, Any],
        signer: Any,
        type_mapping: Dict[str, Type],
        service_endpoint: Optional[str] = None,
        base_path: str = "",
        timeout: int = 300,
        **kwargs
    ):
        """
        Initialize the async client.

        Args:
            service: Service name (e.g., "generative_ai_inference")
            config: OCI config dictionary
            signer: OCI signer for request authentication
            type_mapping: Type mapping for response deserialization
            service_endpoint: Service endpoint URL
            base_path: Base path for API calls (e.g., "/20231130")
            timeout: Request timeout in seconds
        """
        self.service = service
        self.config = config
        self.signer = signer
        self.type_mapping = type_mapping
        self.service_endpoint = service_endpoint.rstrip("/") if service_endpoint else ""
        self.base_path = base_path
        self.timeout = timeout
        self._session: Optional[aiohttp.ClientSession] = None

    def _build_url(self, resource_path: str) -> str:
        """Build full URL from resource path."""
        return f"{self.service_endpoint}{self.base_path}{resource_path}"

    def _sign_request(
        self,
        method: str,
        url: str,
        headers: Dict[str, str],
        body_str: Optional[str] = None,
    ) -> Dict[str, str]:
        """
        Sign request headers using OCI signer.

        Args:
            method: HTTP method
            url: Request URL
            headers: Request headers
            body_str: Serialized request body (JSON string)

        Returns:
            Signed headers dictionary
        """
        # Create a requests.Request to sign (signer expects this format)
        req = requests.Request(
            method=method,
            url=url,
            headers=headers,
            data=body_str,
        )
        prepared = req.prepare()

        # Sign the request
        self.signer(prepared)

        return dict(prepared.headers)

    def _serialize_body(self, body: Any) -> Optional[str]:
        """Serialize request body to JSON using OCI's serialization."""
        if body is None:
            return None

        # Use OCI's sanitize_for_serialization which handles attribute_map
        serialized = self._sanitize_for_serialization(body)
        return json.dumps(serialized)

    def _sanitize_for_serialization(self, obj: Any) -> Any:
        """
        Recursively serialize OCI model objects to JSON-compatible dicts.

        Uses attribute_map to convert snake_case to camelCase as expected by the API.
        """
        from datetime import date, datetime
        import pytz

        if obj is None:
            return None

        if isinstance(obj, (str, int, float, bool)):
            return obj

        if isinstance(obj, datetime):
            if not obj.tzinfo:
                obj = pytz.utc.localize(obj)
            return obj.astimezone(pytz.utc).isoformat().replace('+00:00', 'Z')

        if isinstance(obj, date):
            return obj.isoformat()

        if isinstance(obj, list):
            return [self._sanitize_for_serialization(item) for item in obj]

        if isinstance(obj, dict):
            return {k: self._sanitize_for_serialization(v) for k, v in obj.items()}

        # Handle OCI model objects with swagger_types and attribute_map
        if hasattr(obj, 'swagger_types') and hasattr(obj, 'attribute_map'):
            result = {}
            for attr in obj.swagger_types:
                value = getattr(obj, attr, None)
                if value is not None:
                    # Use attribute_map to get camelCase key
                    key = obj.attribute_map.get(attr, attr)
                    result[key] = self._sanitize_for_serialization(value)
            return result

        # Fallback - try to convert to dict
        if hasattr(obj, '__dict__'):
            return {k: self._sanitize_for_serialization(v) for k, v in obj.__dict__.items()}

        return obj

    @asynccontextmanager
    async def _get_session(self) -> AsyncIterator[aiohttp.ClientSession]:
        """Get or create aiohttp session."""
        if self._session is None or self._session.closed:
            timeout = aiohttp.ClientTimeout(total=self.timeout)
            self._session = aiohttp.ClientSession(timeout=timeout)

        try:
            yield self._session
        except Exception:
            # Don't close on error - let caller handle
            raise

    async def close(self):
        """Close the aiohttp session."""
        if self._session and not self._session.closed:
            await self._session.close()
            self._session = None

    async def call_api_async(
        self,
        resource_path: str,
        method: str,
        header_params: Optional[Dict[str, str]] = None,
        body: Any = None,
        response_type: Optional[str] = None,
        stream: bool = False,
        **kwargs
    ) -> AsyncIterator[Dict[str, Any]]:
        """
        Make async API call to OCI service.

        Args:
            resource_path: API resource path
            method: HTTP method (GET, POST, etc.)
            header_params: Additional headers
            body: Request body
            response_type: Expected response type for deserialization
            stream: Whether to stream the response (SSE)

        Yields:
            Response data as dictionaries
        """
        url = self._build_url(resource_path)

        # Build headers
        headers = {
            "content-type": "application/json",
            "accept": "text/event-stream" if stream else "application/json",
            "user-agent": USER_INFO,
            "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT"),
        }
        if header_params:
            headers.update({k: v for k, v in header_params.items() if v is not None})

        # Serialize body
        body_str = self._serialize_body(body)

        # Sign the request (pass serialized body for content-length calculation)
        signed_headers = self._sign_request(method, url, headers, body_str)

        async with self._get_session() as session:
            async with session.request(
                method,
                url,
                headers=signed_headers,
                data=body_str,
            ) as response:
                if response.status >= 400:
                    error_text = await response.text()
                    raise RuntimeError(
                        f"OCI API request failed with status {response.status}: {error_text}"
                    )

                if stream:
                    async for line in response.content:
                        line = line.strip()
                        if not line:
                            continue

                        decoded = line.decode("utf-8")
                        if decoded.lower().startswith("data:"):
                            data = decoded[5:].strip()
                            if data and not data.startswith("[DONE]"):
                                try:
                                    yield json.loads(data)
                                except json.JSONDecodeError:
                                    continue
                else:
                    data = await response.json()
                    yield data

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
