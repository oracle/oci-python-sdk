# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .rule import Rule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtendHttpRequestHeaderValueRule(Rule):
    """
    An object that represents the action of modifying a request header value. This rule applies only to HTTP listeners.

    This rule adds a prefix, a suffix, or both to the header value.

    **NOTES:**

    *  This rule requires a value for a prefix, suffix, or both.

    *  The system does not support this rule for headers with multiple values.

    *  The system does not distinquish between underscore and dash characters in headers. That is, it treats
    `example_header_name` and `example-header-name` as identical.  If two such headers appear in a request, the system
    applies the action to the first header it finds. The affected header cannot be determined in advance. Oracle
    recommends that you do not rely on underscore or dash characters to uniquely distinguish header names.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtendHttpRequestHeaderValueRule object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.ExtendHttpRequestHeaderValueRule.action` attribute
        of this class is ``EXTEND_HTTP_REQUEST_HEADER_VALUE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this ExtendHttpRequestHeaderValueRule.
            Allowed values for this property are: "ADD_HTTP_REQUEST_HEADER", "EXTEND_HTTP_REQUEST_HEADER_VALUE", "REMOVE_HTTP_REQUEST_HEADER", "ADD_HTTP_RESPONSE_HEADER", "EXTEND_HTTP_RESPONSE_HEADER_VALUE", "REMOVE_HTTP_RESPONSE_HEADER", "ALLOW", "CONTROL_ACCESS_USING_HTTP_METHODS", "REDIRECT", "HTTP_HEADER"
        :type action: str

        :param header:
            The value to assign to the header property of this ExtendHttpRequestHeaderValueRule.
        :type header: str

        :param prefix:
            The value to assign to the prefix property of this ExtendHttpRequestHeaderValueRule.
        :type prefix: str

        :param suffix:
            The value to assign to the suffix property of this ExtendHttpRequestHeaderValueRule.
        :type suffix: str

        """
        self.swagger_types = {
            'action': 'str',
            'header': 'str',
            'prefix': 'str',
            'suffix': 'str'
        }

        self.attribute_map = {
            'action': 'action',
            'header': 'header',
            'prefix': 'prefix',
            'suffix': 'suffix'
        }

        self._action = None
        self._header = None
        self._prefix = None
        self._suffix = None
        self._action = 'EXTEND_HTTP_REQUEST_HEADER_VALUE'

    @property
    def header(self):
        """
        **[Required]** Gets the header of this ExtendHttpRequestHeaderValueRule.
        A header name that conforms to RFC 7230.

        Example: `example_header_name`


        :return: The header of this ExtendHttpRequestHeaderValueRule.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Sets the header of this ExtendHttpRequestHeaderValueRule.
        A header name that conforms to RFC 7230.

        Example: `example_header_name`


        :param header: The header of this ExtendHttpRequestHeaderValueRule.
        :type: str
        """
        self._header = header

    @property
    def prefix(self):
        """
        Gets the prefix of this ExtendHttpRequestHeaderValueRule.
        A string to prepend to the header value. The resulting header value must conform to RFC 7230.
        With the following exceptions:
        *  value cannot contain `$`
        *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.

        Example: `example_prefix_value`


        :return: The prefix of this ExtendHttpRequestHeaderValueRule.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this ExtendHttpRequestHeaderValueRule.
        A string to prepend to the header value. The resulting header value must conform to RFC 7230.
        With the following exceptions:
        *  value cannot contain `$`
        *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.

        Example: `example_prefix_value`


        :param prefix: The prefix of this ExtendHttpRequestHeaderValueRule.
        :type: str
        """
        self._prefix = prefix

    @property
    def suffix(self):
        """
        Gets the suffix of this ExtendHttpRequestHeaderValueRule.
        A string to append to the header value. The resulting header value must conform to RFC 7230.
        With the following exceptions:
        *  value cannot contain `$`
        *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.

        Example: `example_suffix_value`


        :return: The suffix of this ExtendHttpRequestHeaderValueRule.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this ExtendHttpRequestHeaderValueRule.
        A string to append to the header value. The resulting header value must conform to RFC 7230.
        With the following exceptions:
        *  value cannot contain `$`
        *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.

        Example: `example_suffix_value`


        :param suffix: The suffix of this ExtendHttpRequestHeaderValueRule.
        :type: str
        """
        self._suffix = suffix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
