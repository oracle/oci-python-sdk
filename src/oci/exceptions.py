# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import platform
import oci.util
from .version import __version__
from oci._vendor.requests.exceptions import RequestException as BaseRequestException
from oci._vendor.requests.exceptions import ConnectTimeout as BaseConnectTimeout
CLIENT_VERSION = f"Oracle-PythonSDK/{__version__}"
OS_VERSION = platform.platform()
UPLOAD_MANAGER_DEBUG_INFORMATION_LOG = f"Client Version: {CLIENT_VERSION}, OS Version: {OS_VERSION}, See https://docs.oracle.com/iaas/Content/API/Concepts/sdk_troubleshooting.htm for common issues and steps to resolve them. If you need to contact support, or file a GitHub issue, please include this full error message."


class ServiceError(Exception):
    """The service returned an error response."""

    def __init__(self, status, code, headers, message, **kwargs):
        self.status = status
        self.code = code
        self.headers = headers
        self.message = message
        self.original_request = kwargs.get('original_request')
        self.request_id = self._get_opc_request_id()
        self.operation_name = kwargs.get('operation_name')
        self.api_reference_link = kwargs.get('api_reference_link')
        self.target_service = kwargs.get('target_service')
        self.request_endpoint = kwargs.get('request_endpoint')
        self.client_version = kwargs.get('client_version')
        self.timestamp = kwargs.get('timestamp')

        api_errors_info = f"See https://docs.oracle.com/iaas/Content/API/References/apierrors.htm#apierrors_{str(self.status)}__{str(self.status)}_{str(code).lower()} for more information about resolving this error."
        contact_info = f"If you are unable to resolve this {self.target_service} issue, please contact Oracle support and provide them this full error message."

        if not message:
            message = "The service returned error code %s" % self.status

        error_details = {
            "target_service": self.target_service,
            "status": status,
            "code": code,
            "opc-request-id": self.request_id,
            "message": message,
            "operation_name": self.operation_name,
            "timestamp": self.timestamp,
            "client_version": self.client_version,
            "request_endpoint": self.request_endpoint,
            "logging_tips": "To get more info on the failing request, refer to https://docs.oracle.com/en-us/iaas/tools/python/latest/logging.html for ways to log the request/response details."
        }

        if self.api_reference_link:
            error_details['troubleshooting_tips'] = f"{api_errors_info} Also see {self.api_reference_link} for details on this operation's requirements. {contact_info}"
        else:
            error_details['troubleshooting_tips'] = f"{api_errors_info} {contact_info}"

        if isinstance(kwargs.get('deserialized_data'), dict):
            # convert the Keys of the dictionary to snake case
            deserialized_data = oci.util.camel_to_snake_keys(kwargs.get('deserialized_data'))
            for key, value in deserialized_data.items():
                # Skip adding duplicate keys in error_details
                if key not in (error_details):
                    error_details[key] = value

        super(ServiceError, self).__init__(error_details)

    def _get_opc_request_id(self):
        if self.headers.get("opc-request-id"):
            return self.headers.get("opc-request-id")
        elif self.original_request and self.original_request.header_params:
            return self.original_request.header_params.get("opc-request-id")
        else:
            return None


class TransientServiceError(ServiceError):
    """A transient service error occurred"""


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


class InvalidAlloyConfig(ClientError):
    """Alloy config is invalid, or is blocking a service"""


class InvalidResourcePrincipalArguments(ClientError):
    """The ResourceId is missing."""


class InvalidPrivateKey(ClientError):
    """The provided key is not a private key, or the provided passphrase is incorrect."""


class MissingPrivateKeyPassphrase(InvalidPrivateKey):
    """The provided key requires a passphrase."""


class InvalidKeyFilePath(ClientError):
    """The value is expected to be a file name but it's not a valid key_file path."""


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

        self.message = f"MultipartUploadError exception has occurred. {UPLOAD_MANAGER_DEBUG_INFORMATION_LOG}"
        super(Exception, self).__init__(self.message)


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


class DownloadTerminated(Exception):
    """
    This exception is raised by DownloadManager.get_object_to_path and DownloadManager.get_object_to_stream when a
    download is terminated in between. This is generally raised when the download manager's state is changed to -1,
    indicating that the download is to be terminated.
    """
    pass


class ResumableDownloadException(Exception):
    """
    This exception is raised when in a multipart download some parts failed.
    """
    def __init__(self,
                 namespace_name,
                 bucket_name,
                 object_name,
                 failed_parts):
        self.namespace_name = namespace_name
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.failed_parts = failed_parts


class DownloadFailedIncorrectDownloadSize(Exception):
    """
    This exception is raised when the final integrity check (comparing the actual bytes downloaded with the object size
    in bytes) fails.
    """

    def __init__(self,
                 actual_bytes_downloaded,
                 object_size):
        self.actual_bytes_downloaded = actual_bytes_downloaded
        self.object_size = object_size
        self.message = (f"The downloaded file didn't match the object size in bytes: expected {object_size}, "
                        f"got {actual_bytes_downloaded}")
