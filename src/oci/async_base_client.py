# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
Async base client for OCI services using aiohttp.

This module provides true async HTTP support for OCI services,
enabling non-blocking concurrent requests.

Features:
    - True async/await support using aiohttp
    - Thread-safe session management with asyncio.Lock
    - Full response deserialization to OCI model types
    - ServiceError exceptions matching sync client behavior
    - Retry policy support (operation-level, client-level, and global)
    - Streaming (SSE) support for real-time responses

Example:
    >>> import asyncio
    >>> from oci.async_base_client import AsyncBaseClient
    >>>
    >>> async def main():
    ...     async with AsyncBaseClient(...) as client:
    ...         response = await client.call_api("/resource", "GET")
    ...         print(response.data)
    >>>
    >>> asyncio.run(main())
"""

from __future__ import absolute_import

import asyncio
import json
import logging
import re
import time
from datetime import date, datetime, timezone
from typing import Any, AsyncIterator, Callable, Dict, Optional, Type, TypeVar, Union

import aiohttp
import pytz
from dateutil.parser import parse
from dateutil import tz as dateutil_tz
from ._vendor import requests, six

from . import retry
from .exceptions import ServiceError
from .response import Response
from .version import __version__

logger = logging.getLogger(__name__)

USER_INFO = "Oracle-PythonSDK-Async/{}".format(__version__)

# Type variable for generic response types
T = TypeVar('T')

# Regex patterns for deserialization (same as base_client)
DICT_VALUE_TYPE_REGEX = re.compile(r'dict\(str, (.+?)\)$')
LIST_ITEM_TYPE_REGEX = re.compile(r'list\[(.+?)\]$')


class AsyncBaseClient:
    """
    Async HTTP client for OCI services.

    Uses aiohttp for true async/await support while reusing
    the existing OCI signer for request authentication.

    This client provides:
        - Async context manager support (async with)
        - Thread-safe session management
        - Full OCI model deserialization
        - Retry policy integration
        - Proper ServiceError exceptions

    Attributes:
        service: The OCI service name
        config: OCI configuration dictionary
        signer: OCI request signer
        type_mapping: Mapping of type names to classes for deserialization
        service_endpoint: Base URL for the service
        base_path: API version path (e.g., "/20231130")
        timeout: Request timeout in seconds
        retry_strategy: Optional retry strategy for failed requests
    """

    __slots__ = (
        'service',
        'config',
        'signer',
        'type_mapping',
        'service_endpoint',
        'base_path',
        'timeout',
        'skip_deserialization',
        'retry_strategy',
        '_session',
        '_session_lock',
    )

    def __init__(
        self,
        service: str,
        config: Dict[str, Any],
        signer: Any,
        type_mapping: Dict[str, Type],
        service_endpoint: Optional[str] = None,
        base_path: str = "",
        timeout: int = 300,
        skip_deserialization: bool = False,
        retry_strategy: Optional[Any] = None,
        **kwargs
    ):
        """
        Initialize the async client.

        Args:
            service: Service name (e.g., "generative_ai_inference")
            config: OCI config dictionary from oci.config.from_file()
            signer: OCI signer for request authentication
            type_mapping: Type mapping for response deserialization
            service_endpoint: Service endpoint URL (required)
            base_path: Base path for API calls (e.g., "/20231130")
            timeout: Request timeout in seconds (default: 300)
            skip_deserialization: If True, return raw dicts instead of OCI models
            retry_strategy: Retry strategy for failed requests. Can be:
                - None: Use global retry strategy if set
                - oci.retry.NoneRetryStrategy(): Disable retries
                - oci.retry.DEFAULT_RETRY_STRATEGY: Use default retry
                - Custom retry strategy built with RetryStrategyBuilder
        """
        self.service = service
        self.config = config
        self.signer = signer
        self.type_mapping = type_mapping
        self.service_endpoint = service_endpoint.rstrip("/") if service_endpoint else ""
        self.base_path = base_path
        self.timeout = timeout
        self.skip_deserialization = skip_deserialization
        self.retry_strategy = retry_strategy
        self._session: Optional[aiohttp.ClientSession] = None
        self._session_lock = asyncio.Lock()

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

    # -------------------------------------------------------------------------
    # Deserialization (mirrors base_client.py logic)
    # -------------------------------------------------------------------------

    def _deserialize(self, data: Any, cls: str) -> Any:
        """
        Deserialize a dict, list, or str into an object.

        Args:
            data: dict, list or str
            cls: string of class name

        Returns:
            Deserialized object
        """
        if data is None:
            return None

        if cls.startswith('list['):
            sub_kls = re.match(r'list\[(.*)\]', cls).group(1)
            return [self._deserialize(sub_data, sub_kls) for sub_data in data]

        if cls.startswith('dict('):
            sub_kls = re.match(r'dict\(([^,]*), (.*)\)', cls).group(2)
            return {k: self._deserialize(v, sub_kls) for k, v in data.items()}

        # Enums are not present in type mappings, and they are strings
        if cls in self.type_mapping:
            cls_type = self.type_mapping[cls]
        else:
            return self._deserialize_primitive(data, cls)

        if hasattr(cls_type, 'get_subtype'):
            # Use the discriminator value to get the correct subtype
            subtype_name = cls_type.get_subtype(data)
            cls_type = self.type_mapping[subtype_name]

        if cls_type in [int, float, six.u, bool]:
            return self._deserialize_primitive(data, cls_type)
        elif cls_type == object:
            return data
        elif cls_type == date:
            return self._deserialize_date(data)
        elif cls_type == datetime:
            return self._deserialize_datetime(data)
        else:
            return self._deserialize_model(data, cls_type)

    def _deserialize_primitive(self, data: Any, cls: Union[str, type]) -> Any:
        """Deserialize string to primitive type."""
        try:
            if isinstance(cls, str):
                if cls == 'str':
                    return str(data)
                elif cls == 'int':
                    return int(data)
                elif cls == 'float':
                    return float(data)
                elif cls == 'bool':
                    return bool(data)
                return data
            value = cls(data)
        except UnicodeEncodeError:
            value = six.u(data)
        except TypeError:
            value = data
        return value

    def _deserialize_date(self, string: str) -> date:
        """Deserialize string to date."""
        try:
            return parse(string).date()
        except (ImportError, ValueError):
            return string

    def _deserialize_datetime(self, string: str) -> datetime:
        """Deserialize string to datetime."""
        try:
            # If this parser creates a date without raising an exception
            # then the time zone is utc and needs to be set.
            naivedatetime = datetime.strptime(string, "%Y-%m-%dT%H:%M:%S.%fZ")
            awaredatetime = naivedatetime.replace(tzinfo=dateutil_tz.tzutc())
            return awaredatetime
        except ValueError:
            try:
                return parse(string)
            except (ImportError, ValueError):
                return string
        except ImportError:
            return string

    def _deserialize_model(self, data: Dict, cls: type) -> Any:
        """Deserialize dict to model instance."""
        instance = cls()

        for attr, attr_type in instance.swagger_types.items():
            prop = instance.attribute_map[attr]
            if prop in data:
                value = data[prop]
                setattr(instance, attr, self._deserialize(value, attr_type))

        return instance

    # -------------------------------------------------------------------------
    # Retry support
    # -------------------------------------------------------------------------

    def _get_retry_strategy(self, operation_retry_strategy: Optional[Any] = None) -> Optional[Any]:
        """
        Get the effective retry strategy for an operation.

        Priority order:
            1. Operation-level retry strategy (if provided)
            2. Client-level retry strategy (self.retry_strategy)
            3. Global retry strategy (oci.retry.GLOBAL_RETRY_STRATEGY)

        Args:
            operation_retry_strategy: Optional operation-specific retry strategy

        Returns:
            The retry strategy to use, or None if no retries
        """
        if operation_retry_strategy is not None:
            return operation_retry_strategy
        if self.retry_strategy is not None:
            return self.retry_strategy
        return retry.GLOBAL_RETRY_STRATEGY

    async def _make_retrying_call(
        self,
        func: Callable,
        retry_strategy: Optional[Any],
        *args,
        **kwargs
    ) -> Response:
        """
        Execute an async function with retry logic.

        Args:
            func: Async function to call
            retry_strategy: Retry strategy to use
            *args: Positional arguments for func
            **kwargs: Keyword arguments for func

        Returns:
            Response from the function

        Raises:
            ServiceError: If all retries are exhausted
        """
        # If no retry strategy or it's NoneRetryStrategy, just call directly
        if retry_strategy is None or isinstance(retry_strategy, retry.NoneRetryStrategy):
            return await func(*args, **kwargs)

        # Get retry parameters from the strategy
        max_attempts = 8  # default
        total_elapsed_time_seconds = 600  # default
        base_sleep_time = getattr(retry_strategy, 'base_sleep_time_seconds', 1)
        exponent = getattr(retry_strategy, 'exponent_growth_factor', 2)
        max_wait = getattr(retry_strategy, 'max_wait_between_calls_seconds', 30)

        # Extract max_attempts from checker if available
        if hasattr(retry_strategy, 'checkers') and hasattr(retry_strategy.checkers, 'checkers'):
            for checker in retry_strategy.checkers.checkers:
                if hasattr(checker, 'max_attempts'):
                    max_attempts = checker.max_attempts
                if hasattr(checker, 'total_elapsed_time_seconds'):
                    total_elapsed_time_seconds = checker.total_elapsed_time_seconds

        attempt = 0
        start_time = time.time()

        while True:
            try:
                return await func(*args, **kwargs)
            except ServiceError as e:
                attempt += 1
                elapsed = time.time() - start_time

                # Check if we should retry
                should_retry = False
                if hasattr(retry_strategy, 'checkers'):
                    should_retry = retry_strategy.checkers.should_retry(
                        exception=e,
                        current_attempt=attempt,
                        total_time_elapsed=elapsed,
                    )
                else:
                    # Simple retry logic for transient errors
                    should_retry = (
                        attempt < max_attempts and
                        elapsed < total_elapsed_time_seconds and
                        (e.status == 429 or e.status >= 500 and e.status != 501)
                    )

                if not should_retry:
                    raise

                # Calculate sleep time with exponential backoff
                sleep_time = min(
                    base_sleep_time * (exponent ** attempt),
                    max_wait
                )

                logger.debug(
                    f"Retry attempt {attempt} after {sleep_time:.2f}s "
                    f"(status={e.status}, code={e.code})"
                )

                await asyncio.sleep(sleep_time)

    # -------------------------------------------------------------------------
    # Session management with thread-safe lock
    # -------------------------------------------------------------------------

    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create aiohttp session (thread-safe)."""
        async with self._session_lock:
            if self._session is None or self._session.closed:
                timeout = aiohttp.ClientTimeout(total=self.timeout)
                self._session = aiohttp.ClientSession(timeout=timeout)
            return self._session

    async def close(self) -> None:
        """Close the aiohttp session."""
        async with self._session_lock:
            if self._session and not self._session.closed:
                await self._session.close()
                self._session = None

    # -------------------------------------------------------------------------
    # API call methods
    # -------------------------------------------------------------------------

    async def _do_call_api(
        self,
        resource_path: str,
        method: str,
        header_params: Optional[Dict[str, str]] = None,
        body: Any = None,
        response_type: Optional[str] = None,
        operation_name: Optional[str] = None,
        api_reference_link: Optional[str] = None,
    ) -> Response:
        """Internal method to make the actual API call."""
        url = self._build_url(resource_path)

        # Build headers
        headers = {
            "content-type": "application/json",
            "accept": "application/json",
            "user-agent": USER_INFO,
            "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT"),
        }
        if header_params:
            headers.update({k: v for k, v in header_params.items() if v is not None})

        # Serialize body
        body_str = self._serialize_body(body)

        # Sign the request
        signed_headers = self._sign_request(method, url, headers, body_str)

        session = await self._get_session()
        async with session.request(
            method,
            url,
            headers=signed_headers,
            data=body_str,
        ) as response:
            response_headers = dict(response.headers)

            if response.status >= 400:
                await self._handle_error_response(
                    response,
                    response_headers,
                    operation_name,
                    api_reference_link,
                    url,
                )

            # Parse response
            response_data = await response.json()

            # Deserialize if response_type provided and not skipping
            if response_type and not self.skip_deserialization:
                data = self._deserialize(response_data, response_type)
            else:
                data = response_data

            return Response(
                status=response.status,
                headers=response_headers,
                data=data,
                request=None,
            )

    async def call_api(
        self,
        resource_path: str,
        method: str,
        header_params: Optional[Dict[str, str]] = None,
        body: Any = None,
        response_type: Optional[str] = None,
        operation_name: Optional[str] = None,
        api_reference_link: Optional[str] = None,
        retry_strategy: Optional[Any] = None,
        **kwargs
    ) -> Response:
        """
        Make async API call to OCI service (non-streaming).

        Args:
            resource_path: API resource path (e.g., "/actions/chat")
            method: HTTP method (GET, POST, etc.)
            header_params: Additional headers to include
            body: Request body (OCI model object or dict)
            response_type: Expected response type for deserialization
            operation_name: Name of the operation (for error messages)
            api_reference_link: Link to API docs (for error messages)
            retry_strategy: Operation-specific retry strategy. Overrides
                client and global retry strategies.

        Returns:
            Response object with:
                - status: HTTP status code
                - headers: Response headers dict
                - data: Deserialized response (OCI model or dict)
                - request_id: OCI request ID for debugging

        Raises:
            ServiceError: If the API returns an error response

        Example:
            >>> response = await client.call_api(
            ...     resource_path="/actions/chat",
            ...     method="POST",
            ...     body=chat_details,
            ...     response_type="ChatResult",
            ... )
            >>> print(response.data.chat_response)
        """
        effective_retry = self._get_retry_strategy(retry_strategy)

        return await self._make_retrying_call(
            self._do_call_api,
            effective_retry,
            resource_path,
            method,
            header_params,
            body,
            response_type,
            operation_name,
            api_reference_link,
        )

    async def call_api_stream(
        self,
        resource_path: str,
        method: str,
        header_params: Optional[Dict[str, str]] = None,
        body: Any = None,
        response_type: Optional[str] = None,
        **kwargs
    ) -> AsyncIterator[Dict[str, Any]]:
        """
        Make async streaming API call to OCI service (SSE).

        This method is used for streaming responses like chat completions
        where the server sends data incrementally using Server-Sent Events.

        Args:
            resource_path: API resource path
            method: HTTP method (GET, POST, etc.)
            header_params: Additional headers
            body: Request body
            response_type: Not used for streaming (events are raw dicts)

        Yields:
            Server-sent events as dictionaries. Each event contains
            the incremental response data.

        Raises:
            ServiceError: If the API returns an error response

        Example:
            >>> async for event in client.call_api_stream(
            ...     resource_path="/actions/chat",
            ...     method="POST",
            ...     body=chat_details,
            ... ):
            ...     print(event)
        """
        url = self._build_url(resource_path)

        # Build headers
        headers = {
            "content-type": "application/json",
            "accept": "text/event-stream",
            "user-agent": USER_INFO,
            "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT"),
        }
        if header_params:
            headers.update({k: v for k, v in header_params.items() if v is not None})

        # Serialize body
        body_str = self._serialize_body(body)

        # Sign the request
        signed_headers = self._sign_request(method, url, headers, body_str)

        session = await self._get_session()
        async with session.request(
            method,
            url,
            headers=signed_headers,
            data=body_str,
        ) as response:
            response_headers = dict(response.headers)

            if response.status >= 400:
                await self._handle_error_response(
                    response,
                    response_headers,
                    None,
                    None,
                    url,
                )

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

    async def _handle_error_response(
        self,
        response: aiohttp.ClientResponse,
        headers: Dict[str, str],
        operation_name: Optional[str],
        api_reference_link: Optional[str],
        url: str,
    ) -> None:
        """Handle error response by raising ServiceError."""
        error_text = await response.text()

        # Try to parse error as JSON
        code = "Unknown"
        message = error_text
        deserialized_data = None

        try:
            error_json = json.loads(error_text)
            code = error_json.get("code", "Unknown")
            message = error_json.get("message", error_text)
            deserialized_data = error_json
        except json.JSONDecodeError:
            pass

        raise ServiceError(
            status=response.status,
            code=code,
            headers=headers,
            message=message,
            operation_name=operation_name,
            api_reference_link=api_reference_link,
            target_service=self.service,
            request_endpoint=url,
            client_version=USER_INFO,
            timestamp=datetime.now(timezone.utc).isoformat(),
            deserialized_data=deserialized_data,
        )

    async def __aenter__(self) -> 'AsyncBaseClient':
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        await self.close()
