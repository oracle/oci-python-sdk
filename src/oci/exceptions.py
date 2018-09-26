# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from oci._vendor.requests.exceptions import RequestException as BaseRequestException
from oci._vendor.requests.exceptions import ConnectTimeout as BaseConnectTimeout


class ServiceError(Exception):
    """The service returned an error response."""

    def __init__(self, status, code, headers, message, **kwargs):
        self.status = status
        self.code = code
        self.headers = headers
        self.message = message
        self.original_request = kwargs.get('original_request')
        self.request_id = self._get_opc_request_id()

        if not message:
            message = "The service returned error code %s" % self.status

        super(ServiceError, self).__init__({
            "opc-request-id": self.request_id,
            "code": code,
            "message": message,
            "status": status
        })

    def _get_opc_request_id(self):
        if self.headers.get("opc-request-id"):
            return self.headers.get("opc-request-id")
        elif self.original_request and self.original_request.header_params:
            return self.original_request.header_params.get("opc-request-id")
        else:
            return None


class ClientError(Exception):
    """A client-side error occurred.."""


class ConfigFileNotFound(ClientError):
    """Config file not be found."""


class InvalidConfig(ClientError):
    """The config object is missing required keys or contains malformed values.

    For example:

    .. code-block:: python

        raise InvalidConfig({
            "region": "missing",
            "key_id": "malformed'
        })
    """
    def __init__(self, errors):
        """:param errors: {config key: error code}"""
        self.errors = errors

    def __str__(self):
        return str(self.errors)


class InvalidPrivateKey(ClientError):
    """The provided key is not a private key, or the provided passphrase is incorrect."""


class MissingPrivateKeyPassphrase(InvalidPrivateKey):
    """The provided key requires a passphrase."""


class ProfileNotFound(ClientError):
    """The specified profile was not found in the config file."""


class WaitUntilNotSupported(ClientError):
    """wait_until is not supported by this response."""


class MaximumWaitTimeExceeded(ClientError):
    """Maximum wait time has been exceeded."""


class MultipartUploadError(Exception):
    """
    Exception thrown when an error with a multipart upload occurs. As multipart uploads can be
    parallelised, this error contains a collection of errors which caused individual part uploads
    to fail
    """
    def __init__(self, **kwargs):
        """
        :param queue error_causes_queue:
            A queue containing errors which occured during the multipart upload
        """
        self.error_causes = []
        if 'error_causes_queue' in kwargs:
            while not kwargs['error_causes_queue'].empty():
                self.error_causes.append(kwargs['error_causes_queue'].get())


class CompositeOperationError(Exception):
    """
    An exception occurred during a composite operation (e.g. launching an instance and waiting for state)
    but part of the composite operation succeeded. This exception has the following attributes:

    :var list partial_results: Any partial results which are available (e.g. if the :py:meth:`~oci.core.ComputeClient.launch_instance` succeeded and the waiting for state failed then this will contain the :py:meth:`~oci.core.ComputeClient.launch_instance` result)
    :var Exception cause: The exception which caused the composite operation to fail
    """

    def __init__(self, partial_results=[], cause=None):
        self.partial_results = partial_results
        self.cause = cause


class RequestException(BaseRequestException):
    """An exception occurred when making the request"""


class ConnectTimeout(BaseConnectTimeout):
    """The request timed out while trying to connect to the remote server.

    Requests that produced this error are safe to retry.
    """


class MissingEndpointForNonRegionalServiceClientError(ValueError):
    """No endpoint value was provided when trying to create a non-regional service client.
    """
