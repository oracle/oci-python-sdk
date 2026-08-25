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
import functools
import json
import logging
import random
import re
import string
import sys
import time
from datetime import date, datetime, timezone
from typing import Any, AsyncIterator, Callable, Dict, Optional, Type, TypeVar, Union
from urllib.parse import quote, urlencode

import aiohttp
import pytz
from circuitbreaker import CircuitBreakerError, CircuitBreakerMonitor
from dateutil.parser import parse
from dateutil import tz as dateutil_tz
from ._vendor import requests, six

from . import retry
from .base_client import BaseClient, VALID_COLLECTION_FORMAT_TYPES, build_user_agent, merge_type_mappings
from .circuit_breaker import CircuitBreakerStrategy, NoCircuitBreakerStrategy
from .config import get_config_value_or_default
from .exceptions import RequestException, ServiceError, TransientServiceError
from .response import Response
from .util import NONE_SENTINEL, Sentinel
from .version import __version__

logger = logging.getLogger(__name__)

USER_INFO = "Oracle-PythonSDK/{}".format(__version__)
missing = Sentinel("Missing")

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
        base_path: Service API base path
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
        'user_agent',
        'skip_deserialization',
        'retry_strategy',
        'client_level_dualstack_endpoints_enabled',
        'service_uses_dualstack_endpoints_by_default',
        'circuit_breaker_strategy',
        'circuit_breaker_callback',
        '_circuit_breaker',
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
            service: OCI service name
            config: OCI config dictionary from oci.config.from_file()
            signer: OCI signer for request authentication
            type_mapping: Type mapping for response deserialization
            service_endpoint: Service endpoint URL (required)
            base_path: Base path for API calls
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
        self.type_mapping = merge_type_mappings(BaseClient.primitive_type_map, type_mapping)
        self.service_endpoint = service_endpoint.rstrip("/") if service_endpoint else ""
        self.base_path = base_path
        self.timeout = timeout
        self.user_agent = build_user_agent(
            get_config_value_or_default(config, "additional_user_agent")
        )
        self.skip_deserialization = skip_deserialization
        self.retry_strategy = retry_strategy
        self.client_level_dualstack_endpoints_enabled = kwargs.get(
            'client_level_dualstack_endpoints_enabled'
        )
        self.service_uses_dualstack_endpoints_by_default = kwargs.get(
            'service_uses_dualstack_endpoints_by_default', False
        )
        self.circuit_breaker_strategy = kwargs.get('circuit_breaker_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')
        self._circuit_breaker = None
        if self.circuit_breaker_strategy is not None and not isinstance(
            self.circuit_breaker_strategy, NoCircuitBreakerStrategy
        ):
            if not isinstance(self.circuit_breaker_strategy, CircuitBreakerStrategy):
                raise TypeError('Invalid Circuit Breaker Strategy!')
            self._circuit_breaker = CircuitBreakerMonitor.get(
                self.circuit_breaker_strategy.name
            )
            if self._circuit_breaker is None:
                self._circuit_breaker = (
                    self.circuit_breaker_strategy.get_circuit_breaker()
                )
                CircuitBreakerMonitor.register(self._circuit_breaker)
        self._session: Optional[aiohttp.ClientSession] = None
        # asyncio primitives created outside a running loop bind eagerly on older
        # Python versions. Create this on first async use instead.
        self._session_lock = None

    @property
    def endpoint(self) -> str:
        """Expose the endpoint name expected by BaseClient's template logic."""
        return self.service_endpoint

    def is_dual_stack_enabled(self) -> bool:
        """Use the synchronous client's dual-stack precedence rules unchanged."""
        return BaseClient.is_dual_stack_enabled(self)

    def update_endpoint_template_for_options(self) -> str:
        """Expand endpoint option blocks with the synchronous client implementation."""
        return BaseClient.update_endpoint_template_for_options(self)

    def map_service_params_to_values(
        self, service_params_url, path_params, query_params, required_arguments
    ):
        """Map endpoint service parameters using the synchronous client implementation."""
        return BaseClient.map_service_params_to_values(
            self, service_params_url, path_params, query_params, required_arguments
        )

    def handle_service_params_in_endpoint(
        self, path_params, query_params, required_arguments
    ) -> str:
        """Resolve endpoint service parameters using the synchronous client implementation."""
        return BaseClient.handle_service_params_in_endpoint(
            self, path_params, query_params, required_arguments
        )

    def _build_url(
        self,
        resource_path: str,
        path_params: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        enable_strict_url_encoding: bool = False,
        required_arguments: Optional[Any] = None,
    ) -> str:
        """Build full URL from resource path."""
        if path_params:
            for key, value in path_params.items():
                if value is missing or value is None:
                    continue
                safe = "" if enable_strict_url_encoding else "/"
                replacement = quote(str(self.to_path_value(value)), safe=safe)
                resource_path = resource_path.replace(
                    "{{{}}}".format(key),
                    replacement,
                )
        endpoint = self.handle_service_params_in_endpoint(
            path_params, query_params, required_arguments
        )
        self._validate_endpoint_host_components(endpoint)
        if self.base_path and not endpoint.endswith(self.base_path):
            endpoint = "{}{}".format(endpoint, self.base_path)
        url = f"{endpoint}{resource_path}"
        if query_params:
            query_params = {
                key: value
                for key, value in query_params.items()
                if value is not missing and value is not None
            }
            if query_params:
                query_params = self.process_query_params(query_params)
                url = "{}?{}".format(url, urlencode(query_params, doseq=True))
        return url

    @staticmethod
    def to_path_value(obj: Any) -> str:
        """Convert a path parameter to the representation used by BaseClient."""
        if isinstance(obj, list):
            return ",".join(obj)
        return str(obj)

    def generate_collection_format_param(self, param_value, collection_format_type):
        if param_value is missing:
            return missing

        if collection_format_type not in VALID_COLLECTION_FORMAT_TYPES:
            raise ValueError('Invalid collection format type {}. Valid types are: {}'.format(collection_format_type, list(VALID_COLLECTION_FORMAT_TYPES.keys())))

        if collection_format_type == 'multi':
            return param_value
        else:
            return VALID_COLLECTION_FORMAT_TYPES[collection_format_type].join(param_value)

    def process_query_params(self, query_params):
        query_params = self._sanitize_for_serialization(query_params)

        processed_query_params = {}
        for k, v in query_params.items():
            if isinstance(v, bool):
                processed_query_params[k] = 'true' if v else 'false'
            elif not isinstance(v, dict) and not isinstance(v, list):
                processed_query_params[k] = self.to_path_value(v)
            elif isinstance(v, list):
                processed_query_params[k] = v
            else:
                for inner_key, inner_val in v.items():
                    processed_query_params['{}.{}'.format(k, inner_key)] = inner_val

        return processed_query_params

    async def _sign_request(
        self,
        method: str,
        url: str,
        headers: Dict[str, str],
        body_str: Any = None,
        enforce_content_headers: bool = True,
    ) -> Dict[str, str]:
        """
        Sign request headers using OCI signer.

        Args:
            method: HTTP method
            url: Request URL
            headers: Request headers
            body_str: Serialized request body

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

        # Token-based signers can refresh expired tokens and acquire locks while
        # signing. Keep that blocking work off the event-loop thread.
        loop = asyncio.get_event_loop()
        signer_call = functools.partial(self.signer, prepared)
        if not enforce_content_headers:
            signer_call = functools.partial(
                self.signer, prepared, enforce_content_headers=False
            )
        await loop.run_in_executor(None, signer_call)

        return dict(prepared.headers)

    def is_instance_principal_or_resource_principal_signer(self) -> bool:
        """Return whether this signer requires a refresh after an HTTP 401."""
        return BaseClient.is_instance_principal_or_resource_principal_signer(self)

    async def _refresh_security_token(self) -> None:
        """Refresh a token signer without blocking the event loop."""
        refresh_security_token = getattr(self.signer, "refresh_security_token", None)
        if callable(refresh_security_token):
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, refresh_security_token)

    def _validate_endpoint_host_components(self, endpoint: str) -> None:
        """Validate a resolved service-parameter endpoint before sending it."""
        parsed_endpoint = six.moves.urllib.parse.urlparse(endpoint)

        if parsed_endpoint.scheme not in ("http", "https"):
            raise ValueError("Invalid endpoint host: endpoint scheme must be http or https.")

        try:
            parsed_endpoint.port
        except ValueError:
            raise ValueError("Invalid endpoint host: endpoint host must contain only letters, digits, underscores, hyphens, and periods.")

        if parsed_endpoint.username is not None or parsed_endpoint.password is not None:
            raise ValueError("Invalid endpoint host: endpoint must not contain user info.")

        if not BaseClient._is_valid_endpoint_hostname(parsed_endpoint.hostname):
            raise ValueError("Invalid endpoint host: endpoint host must contain only letters, digits, underscores, hyphens, and periods.")

        if not self._is_valid_endpoint_path(parsed_endpoint.path) or parsed_endpoint.query or parsed_endpoint.fragment:
            raise ValueError("Invalid endpoint host: endpoint must not contain path, query, or fragment.")

    def _is_valid_endpoint_path(self, endpoint_path: str) -> bool:
        """Allow only the path explicitly configured on the async endpoint."""
        endpoint_without_scheme = self.service_endpoint.rstrip("/").split("://", 1)[-1]
        path_start = endpoint_without_scheme.find("/")
        configured_path = "" if path_start == -1 else endpoint_without_scheme[path_start:]
        configured_path = configured_path.rstrip("/")

        if not configured_path:
            return endpoint_path in ("", "/")
        return endpoint_path in (configured_path, "{}/".format(configured_path))

    def _serialize_body(
        self,
        body: Any,
        content_type: Optional[str] = None,
    ) -> Any:
        """Serialize a body using the same content-type rules as BaseClient."""
        if body is None or body is missing:
            return None

        if isinstance(body, (str, bytes)):
            return body

        serialized = self._sanitize_for_serialization(body)
        if content_type and "json" not in content_type.lower():
            return serialized
        return json.dumps(serialized)

    @staticmethod
    def _get_header(headers: Dict[str, Any], name: str) -> Optional[Any]:
        """Return a header value without assuming key casing."""
        name = name.lower()
        for key, value in headers.items():
            if key.lower() == name:
                return value
        return None

    def _prepare_headers(
        self,
        method: str,
        header_params: Optional[Dict[str, Any]],
        body: Any,
        default_accept: str,
        enforce_content_headers: bool = True,
    ) -> Dict[str, Any]:
        """Add common SDK headers while preserving operation-specific headers."""
        headers = {
            "accept": default_accept,
            "user-agent": USER_INFO,
            "date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT"),
        }
        if enforce_content_headers and body is not None and method.upper() in ("POST", "PUT", "PATCH"):
            headers["content-type"] = "application/json"
        if header_params:
            for key, value in header_params.items():
                if value is missing or value is None:
                    continue
                existing_key = next(
                    (
                        candidate
                        for candidate in headers
                        if candidate.lower() == key.lower()
                    ),
                    None,
                )
                if existing_key is not None:
                    headers.pop(existing_key)
                headers[key] = value

        # Match BaseClient telemetry and do not allow differently-cased operation
        # headers to leave duplicates behind.
        for header_name in ("user-agent", "opc-client-info"):
            for existing_key in list(headers):
                if existing_key.lower() == header_name:
                    headers.pop(existing_key)
        headers["opc-client-info"] = USER_INFO
        headers["user-agent"] = self.user_agent
        return headers

    def _sanitize_for_serialization(self, obj: Any) -> Any:
        """
        Recursively serialize OCI model objects to JSON-compatible dicts.

        Uses attribute_map to convert snake_case to camelCase as expected by the API.
        """
        if obj is None or obj is NONE_SENTINEL:
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
            return {
                k: self._sanitize_for_serialization(v)
                for k, v in obj.items()
                if v is not missing
            }

        # Handle OCI model objects with swagger_types and attribute_map
        if hasattr(obj, 'swagger_types') and hasattr(obj, 'attribute_map'):
            result = {}
            for attr in obj.swagger_types:
                value = getattr(obj, attr, None)
                if value is not None and value is not missing:
                    # Use attribute_map to get camelCase key
                    key = obj.attribute_map.get(attr, attr)
                    result[key] = self._sanitize_for_serialization(value)
            return result

        # Fallback - try to convert to dict
        if hasattr(obj, '__dict__'):
            return {k: self._sanitize_for_serialization(v) for k, v in obj.__dict__.items()}

        return obj

    @staticmethod
    def is_none_or_none_sentinel(obj: Any) -> bool:
        """Return whether a value represents an explicitly serialized null."""
        return obj is None or obj is NONE_SENTINEL

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

    @staticmethod
    def get_preferred_retry_strategy(operation_retry_strategy, client_retry_strategy):
        """Return the operation, client, or global retry strategy, in that order."""
        retry_strategy = None
        if operation_retry_strategy:
            retry_strategy = operation_retry_strategy
        elif client_retry_strategy:
            retry_strategy = client_retry_strategy
        elif retry.GLOBAL_RETRY_STRATEGY:
            retry_strategy = retry.GLOBAL_RETRY_STRATEGY
        return retry_strategy

    @staticmethod
    def add_opc_retry_token_if_needed(header_params, retry_token_length=30):
        """Add an idempotency token when a retryable operation has none."""
        if "opc-retry-token" not in header_params:
            characters = string.ascii_letters + string.digits
            header_params["opc-retry-token"] = "".join(
                random.SystemRandom().choice(characters)
                for _ in range(retry_token_length)
            )

    @staticmethod
    def add_opc_client_retries_header(header_params):
        """Mark requests for which the SDK performs client-side retries."""
        if "opc-client-retries" not in header_params:
            header_params["opc-client-retries"] = "true"

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

    async def _call_with_circuit_breaker(self, func: Callable, *args, **kwargs) -> Any:
        """Execute one attempt through OCI's existing circuit breaker."""
        if self._circuit_breaker is None:
            return await func(*args, **kwargs)
        if self._circuit_breaker.opened:
            raise CircuitBreakerError(self._circuit_breaker)
        with self._circuit_breaker:
            return await func(*args, **kwargs)

    @staticmethod
    def _retry_checker_exception(exception: Exception) -> Exception:
        """Adapt aiohttp transport failures to the existing retry checkers."""
        if isinstance(
            exception,
            (aiohttp.ClientConnectionError, aiohttp.ClientPayloadError, asyncio.TimeoutError),
        ):
            request_exception = RequestException(exception)
            request_exception.__cause__ = exception
            return request_exception
        return exception

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
        # Circuit breaking applies whether retries are enabled or not.
        if retry_strategy is None or isinstance(retry_strategy, retry.NoneRetryStrategy):
            return await self._call_with_circuit_breaker(func, *args, **kwargs)

        checkers = getattr(retry_strategy, 'checkers', None)
        do_sleep = getattr(retry_strategy, 'do_sleep', None)
        if checkers is None or not callable(getattr(checkers, 'should_retry', None)) or not callable(do_sleep):
            raise TypeError(
                "AsyncBaseClient requires an async-compatible retry strategy "
                "with checkers.should_retry() and do_sleep()."
            )

        attempt = 0
        start_time = time.time()

        while True:
            try:
                return await self._call_with_circuit_breaker(func, *args, **kwargs)
            except asyncio.CancelledError:
                raise
            except Exception as exception:
                attempt += 1
                elapsed = time.time() - start_time
                checker_exception = self._retry_checker_exception(exception)
                checker_kwargs = {
                    'exception': checker_exception,
                    'current_attempt': attempt,
                    'total_time_elapsed': elapsed,
                }
                if callable(self.circuit_breaker_callback):
                    checker_kwargs['circuit_breaker_callback'] = (
                        self.circuit_breaker_callback
                    )
                if not checkers.should_retry(
                    **checker_kwargs
                ):
                    raise

                logger.debug(
                    "Retry attempt %s (status=%s, code=%s)",
                    attempt,
                    getattr(exception, 'status', None),
                    getattr(exception, 'code', None),
                )

                # Reuse the exact existing strategy (including custom jitter) on
                # a worker thread so its time.sleep does not block the event loop.
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(
                    None, do_sleep, attempt, exception
                )

    # -------------------------------------------------------------------------
    # Session management with thread-safe lock
    # -------------------------------------------------------------------------

    def _get_session_lock(self) -> asyncio.Lock:
        """Create the session lock in the running event loop."""
        if self._session_lock is None:
            self._session_lock = asyncio.Lock()
        return self._session_lock

    def _get_client_timeout(self, streaming: bool = False) -> aiohttp.ClientTimeout:
        """Translate SDK timeout values into aiohttp timeout phases."""
        if self.timeout is None:
            return aiohttp.ClientTimeout(total=None)
        if isinstance(self.timeout, tuple):
            connect_timeout, read_timeout = self.timeout
            return aiohttp.ClientTimeout(
                total=None,
                connect=connect_timeout,
                sock_connect=connect_timeout,
                sock_read=read_timeout,
            )
        if streaming:
            return aiohttp.ClientTimeout(
                total=None,
                connect=self.timeout,
                sock_connect=self.timeout,
                sock_read=self.timeout,
            )
        return aiohttp.ClientTimeout(total=self.timeout)

    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create aiohttp session (thread-safe)."""
        async with self._get_session_lock():
            if self._session is None or self._session.closed:
                timeout = self._get_client_timeout()
                self._session = aiohttp.ClientSession(timeout=timeout)
            return self._session

    async def close(self) -> None:
        """Close the aiohttp session."""
        async with self._get_session_lock():
            if self._session and not self._session.closed:
                await self._session.close()
                self._session = None

    # -------------------------------------------------------------------------
    # API call methods
    # -------------------------------------------------------------------------

    async def _read_response_data(
        self,
        response: aiohttp.ClientResponse,
        response_type: Optional[str],
        allow_control_chars: Optional[bool],
    ) -> Any:
        """Read common OCI response formats without assuming a service."""
        if response.status in (204, 205):
            return None
        if response_type == "bytes":
            return await response.read()
        if response_type in ("str", "text"):
            return await response.text()

        try:
            if allow_control_chars:
                return json.loads(await response.text(), strict=False)
            return await response.json()
        except (aiohttp.ContentTypeError, json.JSONDecodeError, ValueError):
            response_text = await response.text()
            return response_text if response_text else None

    async def _do_call_api(
        self,
        resource_path: str,
        method: str,
        header_params: Optional[Dict[str, str]] = None,
        body: Any = None,
        response_type: Optional[str] = None,
        operation_name: Optional[str] = None,
        api_reference_link: Optional[str] = None,
        path_params: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        allow_control_chars: Optional[bool] = None,
        enable_strict_url_encoding: Optional[bool] = None,
        required_arguments: Optional[Any] = None,
        enforce_content_headers: bool = True,
    ) -> Response:
        """Internal method to make the actual API call."""
        url = self._build_url(
            resource_path,
            path_params=path_params,
            query_params=query_params,
            enable_strict_url_encoding=bool(enable_strict_url_encoding),
            required_arguments=required_arguments,
        )

        headers = self._prepare_headers(
            method,
            header_params,
            body,
            default_accept="application/json",
            enforce_content_headers=enforce_content_headers,
        )

        serialized_body = self._serialize_body(
            body,
            content_type=self._get_header(headers, "content-type"),
        )

        # Sign the request
        signed_headers = await self._sign_request(
            method,
            url,
            headers,
            serialized_body,
            enforce_content_headers=enforce_content_headers,
        )

        session = await self._get_session()
        async with session.request(
            method,
            url,
            headers=signed_headers,
            data=serialized_body,
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

            response_data = await self._read_response_data(
                response,
                response_type,
                allow_control_chars,
            )

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
        path_params: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        allow_control_chars: Optional[bool] = None,
        enable_strict_url_encoding: Optional[bool] = None,
        required_arguments: Optional[Any] = None,
        enforce_content_headers: bool = True,
        **kwargs
    ) -> Response:
        """
        Make async API call to OCI service (non-streaming).

        Args:
            resource_path: API resource path
            method: HTTP method (GET, POST, etc.)
            path_params: Values used to replace placeholders in the resource path
            query_params: Query parameters encoded into the request URL
            header_params: Additional headers to include
            body: Request body (OCI model object or dict)
            response_type: Expected response type for deserialization
            operation_name: Name of the operation (for error messages)
            api_reference_link: Link to API docs (for error messages)
            retry_strategy: Operation-specific retry strategy. Overrides
                client and global retry strategies.
            allow_control_chars: Allow JSON strings containing control characters
            enable_strict_url_encoding: Encode all reserved path characters

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
            ...     resource_path="/resources",
            ...     method="POST",
            ...     body={"displayName": "example"},
            ...     response_type="Resource",
            ... )
            >>> print(response.data)
        """
        effective_retry = self._get_retry_strategy(retry_strategy)

        call_kwargs = {
            "resource_path": resource_path,
            "method": method,
            "header_params": header_params,
            "body": body,
            "response_type": response_type,
            "operation_name": operation_name,
            "api_reference_link": api_reference_link,
            "path_params": path_params,
            "query_params": query_params,
            "allow_control_chars": allow_control_chars,
            "enable_strict_url_encoding": enable_strict_url_encoding,
            "required_arguments": required_arguments,
            "enforce_content_headers": enforce_content_headers,
        }
        try:
            return await self._make_retrying_call(
                self._do_call_api, effective_retry, **call_kwargs
            )
        except ServiceError as error:
            if error.status != 401 or not self.is_instance_principal_or_resource_principal_signer():
                raise
            await self._refresh_security_token()
            return await self._make_retrying_call(
                self._do_call_api, effective_retry, **call_kwargs
            )

    async def _open_stream(
        self,
        resource_path: str,
        method: str,
        header_params: Optional[Dict[str, str]] = None,
        body: Any = None,
        operation_name: Optional[str] = None,
        api_reference_link: Optional[str] = None,
        path_params: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        enable_strict_url_encoding: Optional[bool] = None,
        required_arguments: Optional[Any] = None,
    ) -> Any:
        """Open and validate an SSE response without consuming its event body."""
        url = self._build_url(
            resource_path,
            path_params=path_params,
            query_params=query_params,
            enable_strict_url_encoding=bool(enable_strict_url_encoding),
            required_arguments=required_arguments,
        )
        headers = self._prepare_headers(
            method,
            header_params,
            body,
            default_accept="text/event-stream",
        )
        serialized_body = self._serialize_body(
            body,
            content_type=self._get_header(headers, "content-type"),
        )
        signed_headers = await self._sign_request(method, url, headers, serialized_body)
        session = await self._get_session()
        response_context = session.request(
            method,
            url,
            headers=signed_headers,
            data=serialized_body,
            timeout=self._get_client_timeout(streaming=True),
        )
        response = await response_context.__aenter__()
        if response.status >= 400:
            try:
                await self._handle_error_response(
                    response,
                    dict(response.headers),
                    operation_name,
                    api_reference_link,
                    url,
                )
            except Exception:
                await response_context.__aexit__(*sys.exc_info())
                raise
        return response_context, response

    async def call_api_stream(
        self,
        resource_path: str,
        method: str,
        header_params: Optional[Dict[str, str]] = None,
        body: Any = None,
        response_type: Optional[str] = None,
        path_params: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        allow_control_chars: Optional[bool] = None,
        enable_strict_url_encoding: Optional[bool] = None,
        retry_strategy: Optional[Any] = None,
        operation_name: Optional[str] = None,
        api_reference_link: Optional[str] = None,
        required_arguments: Optional[Any] = None,
        **kwargs
    ) -> AsyncIterator[Dict[str, Any]]:
        """
        Make async streaming API call to OCI service (SSE).

        This method is used by OCI operations that return Server-Sent Events.

        Args:
            resource_path: API resource path
            method: HTTP method (GET, POST, etc.)
            header_params: Additional headers
            body: Request body
            response_type: Not used for streaming (events are raw dicts)
            path_params: Values used to replace placeholders in the resource path
            query_params: Query parameters encoded into the request URL
            allow_control_chars: Allow JSON strings containing control characters
            enable_strict_url_encoding: Encode all reserved path characters
            retry_strategy: Strategy used while establishing the stream. An
                interrupted stream is not resumed after events have been yielded.

        Yields:
            Server-sent events as dictionaries. Each event contains
            the incremental response data.

        Raises:
            ServiceError: If the API returns an error response

        Example:
            >>> async for event in client.call_api_stream(
            ...     resource_path="/events",
            ...     method="GET",
            ... ):
            ...     print(event)
        """
        effective_retry = self._get_retry_strategy(retry_strategy)
        call_kwargs = {
            "resource_path": resource_path,
            "method": method,
            "header_params": header_params,
            "body": body,
            "operation_name": operation_name,
            "api_reference_link": api_reference_link,
            "path_params": path_params,
            "query_params": query_params,
            "enable_strict_url_encoding": enable_strict_url_encoding,
            "required_arguments": required_arguments,
        }
        try:
            response_context, response = await self._make_retrying_call(
                self._open_stream, effective_retry, **call_kwargs
            )
        except ServiceError as error:
            if error.status != 401 or not self.is_instance_principal_or_resource_principal_signer():
                raise
            await self._refresh_security_token()
            response_context, response = await self._make_retrying_call(
                self._open_stream, effective_retry, **call_kwargs
            )
        try:
            async for line in response.content:
                line = line.strip()
                if not line:
                    continue

                decoded = line.decode("utf-8")
                if decoded.lower().startswith("data:"):
                    data = decoded[5:].strip()
                    if data and not data.startswith("[DONE]"):
                        try:
                            yield json.loads(data, strict=not bool(allow_control_chars))
                        except json.JSONDecodeError as exc:
                            logger.debug("Dropping malformed SSE data line: %s (%s)", data[:200], exc)
                            continue
        finally:
            await response_context.__aexit__(None, None, None)

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

        error_class = ServiceError
        if isinstance(
            self.circuit_breaker_strategy, CircuitBreakerStrategy
        ) and self.circuit_breaker_strategy.is_transient_error(response.status, code):
            error_class = TransientServiceError

        raise error_class(
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
