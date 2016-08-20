from .exceptions import (NetworkError, StreamAlreadyConsumed)
from requests.exceptions import (ConnectionError, StreamConsumedError)

DEFAULT_CHUNK_SIZE = 512

class DataStream(object):
    """Represents the data for a streamed response."""

    def __init__(self, response):
        self._response = response

    def iter_content(self, chunk_size=DEFAULT_CHUNK_SIZE):
        """Iterates over the response data.

        :param chunk_size: The number of bytes in each chunk.
        """
        try:
            for chunk in self._response.iter_content(chunk_size=chunk_size):
                yield chunk
        except ConnectionError as e:
            raise NetworkError() from e
        except StreamConsumedError as e:
            raise StreamAlreadyConsumed() from e

    @property
    def content(self):
        """Gets the full content of the data stream.
        Calling this after the data stream has been consumed will result
        in a StreamAlreadyConsumed exception."""

        try:
            return self._response.content
        except RuntimeError as e:
            # requests throws a RuntimeError in this case
            # instead of a StreamConsumedError.
            raise StreamAlreadyConsumed() from e

    @property
    def raw(self):
        """Returns the raw urllib3.response.HTTPResponse"""
        return self._response.raw

