# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .rule import Rule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpHeaderRule(Rule):
    """
    An object that represents the advance http header options that allow the setting of http header size and allow/disallow
    invalid characters in the http headers.
    For example httpLargeHeaderSizeInKB=32, the http header could have 4 buffers of 32KBs each
    This rule applies only to HTTP listeners. No more than one `HttpHeaderRule` object can be present in
    a given listener.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HttpHeaderRule object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.HttpHeaderRule.action` attribute
        of this class is ``HTTP_HEADER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this HttpHeaderRule.
            Allowed values for this property are: "ADD_HTTP_REQUEST_HEADER", "EXTEND_HTTP_REQUEST_HEADER_VALUE", "REMOVE_HTTP_REQUEST_HEADER", "ADD_HTTP_RESPONSE_HEADER", "EXTEND_HTTP_RESPONSE_HEADER_VALUE", "REMOVE_HTTP_RESPONSE_HEADER", "ALLOW", "CONTROL_ACCESS_USING_HTTP_METHODS", "REDIRECT", "HTTP_HEADER"
        :type action: str

        :param are_invalid_characters_allowed:
            The value to assign to the are_invalid_characters_allowed property of this HttpHeaderRule.
        :type are_invalid_characters_allowed: bool

        :param http_large_header_size_in_kb:
            The value to assign to the http_large_header_size_in_kb property of this HttpHeaderRule.
        :type http_large_header_size_in_kb: int

        """
        self.swagger_types = {
            'action': 'str',
            'are_invalid_characters_allowed': 'bool',
            'http_large_header_size_in_kb': 'int'
        }

        self.attribute_map = {
            'action': 'action',
            'are_invalid_characters_allowed': 'areInvalidCharactersAllowed',
            'http_large_header_size_in_kb': 'httpLargeHeaderSizeInKB'
        }

        self._action = None
        self._are_invalid_characters_allowed = None
        self._http_large_header_size_in_kb = None
        self._action = 'HTTP_HEADER'

    @property
    def are_invalid_characters_allowed(self):
        """
        Gets the are_invalid_characters_allowed of this HttpHeaderRule.
        Indicates whether or not invalid characters in client header fields will be allowed.
        Valid names are composed of English letters, digits, hyphens and underscores.
        If \"true\", invalid characters are allowed in the HTTP header.
        If \"false\", invalid characters are not allowed in the HTTP header


        :return: The are_invalid_characters_allowed of this HttpHeaderRule.
        :rtype: bool
        """
        return self._are_invalid_characters_allowed

    @are_invalid_characters_allowed.setter
    def are_invalid_characters_allowed(self, are_invalid_characters_allowed):
        """
        Sets the are_invalid_characters_allowed of this HttpHeaderRule.
        Indicates whether or not invalid characters in client header fields will be allowed.
        Valid names are composed of English letters, digits, hyphens and underscores.
        If \"true\", invalid characters are allowed in the HTTP header.
        If \"false\", invalid characters are not allowed in the HTTP header


        :param are_invalid_characters_allowed: The are_invalid_characters_allowed of this HttpHeaderRule.
        :type: bool
        """
        self._are_invalid_characters_allowed = are_invalid_characters_allowed

    @property
    def http_large_header_size_in_kb(self):
        """
        Gets the http_large_header_size_in_kb of this HttpHeaderRule.
        The maximum size of each buffer used for reading http client request header.
        This value indicates the maximum size allowed for each buffer.
        The allowed values for buffer size are 8, 16, 32 and 64.


        :return: The http_large_header_size_in_kb of this HttpHeaderRule.
        :rtype: int
        """
        return self._http_large_header_size_in_kb

    @http_large_header_size_in_kb.setter
    def http_large_header_size_in_kb(self, http_large_header_size_in_kb):
        """
        Sets the http_large_header_size_in_kb of this HttpHeaderRule.
        The maximum size of each buffer used for reading http client request header.
        This value indicates the maximum size allowed for each buffer.
        The allowed values for buffer size are 8, 16, 32 and 64.


        :param http_large_header_size_in_kb: The http_large_header_size_in_kb of this HttpHeaderRule.
        :type: int
        """
        self._http_large_header_size_in_kb = http_large_header_size_in_kb

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
