
class ServiceError(StandardError):

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