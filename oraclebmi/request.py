
class Request(object):

    def __init__(self,
                 method,
                 url,
                 query_params,
                 header_params,
                 body,
                 response_type,
                 enforce_content_headers=True):

        self._method = method
        self._url = url
        self._query_params = query_params
        self._header_params = header_params
        self._body = body
        self._response_type = response_type
        self._enforce_content_headers = enforce_content_headers

    @property
    def method(self):
        return self._method

    @property
    def url(self):
        return self._url

    @property
    def query_params(self):
        return self._query_params

    @property
    def header_params(self):
        return self._header_params

    @property
    def body(self):
        return self._body

    @property
    def response_type(self):
        return self._response_type

    @property
    def enforce_content_headers(self):
        """True if content headers should be automatically added if not present when
        signing put and post requests."""
        return self._enforce_content_headers

