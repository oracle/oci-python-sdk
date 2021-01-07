# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FilterOutput(object):
    """
    Query builder api response object containing updated querystring's
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FilterOutput object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_query_string:
            The value to assign to the display_query_string property of this FilterOutput.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this FilterOutput.
        :type internal_query_string: str

        :param response_time_in_ms:
            The value to assign to the response_time_in_ms property of this FilterOutput.
        :type response_time_in_ms: int

        """
        self.swagger_types = {
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'response_time_in_ms': 'int'
        }

        self.attribute_map = {
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'response_time_in_ms': 'responseTimeInMs'
        }

        self._display_query_string = None
        self._internal_query_string = None
        self._response_time_in_ms = None

    @property
    def display_query_string(self):
        """
        **[Required]** Gets the display_query_string of this FilterOutput.
        Modified user visible query string.


        :return: The display_query_string of this FilterOutput.
        :rtype: str
        """
        return self._display_query_string

    @display_query_string.setter
    def display_query_string(self, display_query_string):
        """
        Sets the display_query_string of this FilterOutput.
        Modified user visible query string.


        :param display_query_string: The display_query_string of this FilterOutput.
        :type: str
        """
        self._display_query_string = display_query_string

    @property
    def internal_query_string(self):
        """
        **[Required]** Gets the internal_query_string of this FilterOutput.
        Modified localization agnostic query string.


        :return: The internal_query_string of this FilterOutput.
        :rtype: str
        """
        return self._internal_query_string

    @internal_query_string.setter
    def internal_query_string(self, internal_query_string):
        """
        Sets the internal_query_string of this FilterOutput.
        Modified localization agnostic query string.


        :param internal_query_string: The internal_query_string of this FilterOutput.
        :type: str
        """
        self._internal_query_string = internal_query_string

    @property
    def response_time_in_ms(self):
        """
        Gets the response_time_in_ms of this FilterOutput.
        Operation response time.


        :return: The response_time_in_ms of this FilterOutput.
        :rtype: int
        """
        return self._response_time_in_ms

    @response_time_in_ms.setter
    def response_time_in_ms(self, response_time_in_ms):
        """
        Sets the response_time_in_ms of this FilterOutput.
        Operation response time.


        :param response_time_in_ms: The response_time_in_ms of this FilterOutput.
        :type: int
        """
        self._response_time_in_ms = response_time_in_ms

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
