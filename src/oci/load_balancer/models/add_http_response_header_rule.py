# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20170115

from .rule import Rule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddHttpResponseHeaderRule(Rule):
    """
    An object that represents the action of adding a header to a response.
    This rule applies only to HTTP listeners.

    **NOTES:**

    *  If a matching header already exists in the response, the system removes all of its occurrences, and then adds the
    new header.

    *  The system does not distinquish between underscore and dash characters in headers. That is, it treats
    `example_header_name` and `example-header-name` as identical. Oracle recommends that you do not rely on underscore
    or dash characters to uniquely distinguish header names.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddHttpResponseHeaderRule object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.AddHttpResponseHeaderRule.action` attribute
        of this class is ``ADD_HTTP_RESPONSE_HEADER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this AddHttpResponseHeaderRule.
            Allowed values for this property are: "ADD_HTTP_REQUEST_HEADER", "EXTEND_HTTP_REQUEST_HEADER_VALUE", "REMOVE_HTTP_REQUEST_HEADER", "ADD_HTTP_RESPONSE_HEADER", "EXTEND_HTTP_RESPONSE_HEADER_VALUE", "REMOVE_HTTP_RESPONSE_HEADER", "ALLOW", "CONTROL_ACCESS_USING_HTTP_METHODS", "REDIRECT", "HTTP_HEADER", "IP_BASED_MAX_CONNECTIONS"
        :type action: str

        :param header:
            The value to assign to the header property of this AddHttpResponseHeaderRule.
        :type header: str

        :param value:
            The value to assign to the value property of this AddHttpResponseHeaderRule.
        :type value: str

        """
        self.swagger_types = {
            'action': 'str',
            'header': 'str',
            'value': 'str'
        }
        self.attribute_map = {
            'action': 'action',
            'header': 'header',
            'value': 'value'
        }
        self._action = None
        self._header = None
        self._value = None
        self._action = 'ADD_HTTP_RESPONSE_HEADER'

    @property
    def header(self):
        """
        **[Required]** Gets the header of this AddHttpResponseHeaderRule.
        A header name that conforms to RFC 7230.

        Example: `example_header_name`


        :return: The header of this AddHttpResponseHeaderRule.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Sets the header of this AddHttpResponseHeaderRule.
        A header name that conforms to RFC 7230.

        Example: `example_header_name`


        :param header: The header of this AddHttpResponseHeaderRule.
        :type: str
        """
        self._header = header

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AddHttpResponseHeaderRule.
        A header value that conforms to RFC 7230.
        With the following exceptions:
        *  value cannot contain `$`
        *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.

        Example: `example_value`


        :return: The value of this AddHttpResponseHeaderRule.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AddHttpResponseHeaderRule.
        A header value that conforms to RFC 7230.
        With the following exceptions:
        *  value cannot contain `$`
        *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.

        Example: `example_value`


        :param value: The value of this AddHttpResponseHeaderRule.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
