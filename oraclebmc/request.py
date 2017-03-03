# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


class Request(object):

    def __init__(self,
                 method,
                 url,
                 query_params=None,
                 header_params=None,
                 body=None,
                 response_type=None,
                 enforce_content_headers=True):
        """
        :param method: HTTP method
        :param url: URL that will serve the request
        :param query_params: (optional) Query parameters in the url.
        :param header_params: (optional) Request header params.
        :param body: (optional) Request body.
        :param response_type: (optional) Response data type.
        :param enforce_content_headers: (optional) Whether content headers should be added for
            PUT and POST requests when not present.  Defaults to True.
        """

        self.method = method
        self.url = url
        self.query_params = query_params
        self.header_params = header_params or {}
        self.body = body
        self.response_type = response_type
        self.enforce_content_headers = enforce_content_headers
