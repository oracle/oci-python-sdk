
class ServiceError(Exception):
    '''The service returned an error response.'''

    def __init__(self, status, headers, data):
        self.status = status
        self.headers = headers
        self.data = data

        message = None
        if data:
            message = data.message

        if message == None:
            message = "The service returned error code %s" % self.status

        super(ServiceError, self).__init__(message)

class ClientError(Exception):
    """A client-side error occurred.."""

class ConfigFileNotFound(ClientError):
    """Config file not be found."""

class ProfileNotFound(ClientError):
    """The specified profile was not found in the config file."""

class WaitUntilNotSupported(ClientError):
    """wait_until is not supported by this response."""

class MaximumWaitTimeExceeded(ClientError):
    """Maximum wait time has been exceeded."""
