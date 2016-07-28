
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

class ConfigFileNotFoundError(Exception):
    """Config file not be found."""

class ProfileNotFoundError(Exception):
    """The specified profile was not found in the config file."""

class WaitUntilNotSupportedError(Exception):
    """wait_until is not supported by this response."""

class MaximumWaitTimeExceededError(Exception):
    """Maximum wait time has been exceeded."""
