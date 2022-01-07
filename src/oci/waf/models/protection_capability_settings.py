# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtectionCapabilitySettings(object):
    """
    Settings for protection capabilities
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProtectionCapabilitySettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param max_number_of_arguments:
            The value to assign to the max_number_of_arguments property of this ProtectionCapabilitySettings.
        :type max_number_of_arguments: int

        :param max_single_argument_length:
            The value to assign to the max_single_argument_length property of this ProtectionCapabilitySettings.
        :type max_single_argument_length: int

        :param max_total_argument_length:
            The value to assign to the max_total_argument_length property of this ProtectionCapabilitySettings.
        :type max_total_argument_length: int

        :param max_http_request_headers:
            The value to assign to the max_http_request_headers property of this ProtectionCapabilitySettings.
        :type max_http_request_headers: int

        :param max_http_request_header_length:
            The value to assign to the max_http_request_header_length property of this ProtectionCapabilitySettings.
        :type max_http_request_header_length: int

        :param allowed_http_methods:
            The value to assign to the allowed_http_methods property of this ProtectionCapabilitySettings.
        :type allowed_http_methods: list[str]

        """
        self.swagger_types = {
            'max_number_of_arguments': 'int',
            'max_single_argument_length': 'int',
            'max_total_argument_length': 'int',
            'max_http_request_headers': 'int',
            'max_http_request_header_length': 'int',
            'allowed_http_methods': 'list[str]'
        }

        self.attribute_map = {
            'max_number_of_arguments': 'maxNumberOfArguments',
            'max_single_argument_length': 'maxSingleArgumentLength',
            'max_total_argument_length': 'maxTotalArgumentLength',
            'max_http_request_headers': 'maxHttpRequestHeaders',
            'max_http_request_header_length': 'maxHttpRequestHeaderLength',
            'allowed_http_methods': 'allowedHttpMethods'
        }

        self._max_number_of_arguments = None
        self._max_single_argument_length = None
        self._max_total_argument_length = None
        self._max_http_request_headers = None
        self._max_http_request_header_length = None
        self._allowed_http_methods = None

    @property
    def max_number_of_arguments(self):
        """
        Gets the max_number_of_arguments of this ProtectionCapabilitySettings.
        Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits.


        :return: The max_number_of_arguments of this ProtectionCapabilitySettings.
        :rtype: int
        """
        return self._max_number_of_arguments

    @max_number_of_arguments.setter
    def max_number_of_arguments(self, max_number_of_arguments):
        """
        Sets the max_number_of_arguments of this ProtectionCapabilitySettings.
        Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits.


        :param max_number_of_arguments: The max_number_of_arguments of this ProtectionCapabilitySettings.
        :type: int
        """
        self._max_number_of_arguments = max_number_of_arguments

    @property
    def max_single_argument_length(self):
        """
        Gets the max_single_argument_length of this ProtectionCapabilitySettings.
        Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length.


        :return: The max_single_argument_length of this ProtectionCapabilitySettings.
        :rtype: int
        """
        return self._max_single_argument_length

    @max_single_argument_length.setter
    def max_single_argument_length(self, max_single_argument_length):
        """
        Sets the max_single_argument_length of this ProtectionCapabilitySettings.
        Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length.


        :param max_single_argument_length: The max_single_argument_length of this ProtectionCapabilitySettings.
        :type: int
        """
        self._max_single_argument_length = max_single_argument_length

    @property
    def max_total_argument_length(self):
        """
        Gets the max_total_argument_length of this ProtectionCapabilitySettings.
        Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length.


        :return: The max_total_argument_length of this ProtectionCapabilitySettings.
        :rtype: int
        """
        return self._max_total_argument_length

    @max_total_argument_length.setter
    def max_total_argument_length(self, max_total_argument_length):
        """
        Sets the max_total_argument_length of this ProtectionCapabilitySettings.
        Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length.


        :param max_total_argument_length: The max_total_argument_length of this ProtectionCapabilitySettings.
        :type: int
        """
        self._max_total_argument_length = max_total_argument_length

    @property
    def max_http_request_headers(self):
        """
        Gets the max_http_request_headers of this ProtectionCapabilitySettings.
        Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request Headers.


        :return: The max_http_request_headers of this ProtectionCapabilitySettings.
        :rtype: int
        """
        return self._max_http_request_headers

    @max_http_request_headers.setter
    def max_http_request_headers(self, max_http_request_headers):
        """
        Sets the max_http_request_headers of this ProtectionCapabilitySettings.
        Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request Headers.


        :param max_http_request_headers: The max_http_request_headers of this ProtectionCapabilitySettings.
        :type: int
        """
        self._max_http_request_headers = max_http_request_headers

    @property
    def max_http_request_header_length(self):
        """
        Gets the max_http_request_header_length of this ProtectionCapabilitySettings.
        Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request header size.


        :return: The max_http_request_header_length of this ProtectionCapabilitySettings.
        :rtype: int
        """
        return self._max_http_request_header_length

    @max_http_request_header_length.setter
    def max_http_request_header_length(self, max_http_request_header_length):
        """
        Sets the max_http_request_header_length of this ProtectionCapabilitySettings.
        Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request header size.


        :param max_http_request_header_length: The max_http_request_header_length of this ProtectionCapabilitySettings.
        :type: int
        """
        self._max_http_request_header_length = max_http_request_header_length

    @property
    def allowed_http_methods(self):
        """
        Gets the allowed_http_methods of this ProtectionCapabilitySettings.
        List of allowed HTTP methods. Each value as a RFC7230 formated token string.
        Used in protection capability 911100: Restrict HTTP Request Methods.


        :return: The allowed_http_methods of this ProtectionCapabilitySettings.
        :rtype: list[str]
        """
        return self._allowed_http_methods

    @allowed_http_methods.setter
    def allowed_http_methods(self, allowed_http_methods):
        """
        Sets the allowed_http_methods of this ProtectionCapabilitySettings.
        List of allowed HTTP methods. Each value as a RFC7230 formated token string.
        Used in protection capability 911100: Restrict HTTP Request Methods.


        :param allowed_http_methods: The allowed_http_methods of this ProtectionCapabilitySettings.
        :type: list[str]
        """
        self._allowed_http_methods = allowed_http_methods

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
