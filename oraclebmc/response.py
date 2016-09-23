from .constants import HEADER_NEXT_PAGE, HEADER_REQUEST_ID


class Response(object):
    def __init__(self, status, headers, data, request):
        self._status = status
        self._headers = headers
        self._data = data
        self._request = request

        self._next_page = None
        self._request_id = None

        if self._headers is not None:
            self._next_page = self._headers.get(HEADER_NEXT_PAGE)
            self._request_id = self._headers.get(HEADER_REQUEST_ID)

    @property
    def status(self):
        return self._status

    @property
    def headers(self):
        return self._headers

    @property
    def data(self):
        return self._data

    @property
    def request(self):
        return self._request

    @property
    def next_page(self):
        return self._next_page

    @property
    def request_id(self):
        return self._request_id

    @property
    def has_next_page(self):
        return self._next_page is not None
