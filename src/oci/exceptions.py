# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


class ServiceError(Exception):
    """The service returned an error response."""

    def __init__(self, status, code, headers, message):
        self.status = status
        self.code = code
        self.headers = headers
        self.message = message

        if not message:
            message = "The service returned error code %s" % self.status

        super(ServiceError, self).__init__({
            "opc-request-id": headers.get("opc-request-id"),
            "code": code,
            "message": message,
            "status": status
        })


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
