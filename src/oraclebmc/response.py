# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .constants import HEADER_NEXT_PAGE, HEADER_REQUEST_ID


class Response(object):
    def __init__(self, status, headers, data, request):
        self.status = status
        self.headers = headers
        self.data = data
        self.request = request

        self.next_page = None
        self.request_id = None

        if self.headers is not None:
            self.next_page = self.headers.get(HEADER_NEXT_PAGE)
            self.request_id = self.headers.get(HEADER_REQUEST_ID)

    @property
    def has_next_page(self):
        return self.next_page is not None
