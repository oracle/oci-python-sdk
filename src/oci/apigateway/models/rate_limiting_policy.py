# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RateLimitingPolicy(object):
    """
    Limit the number of requests that should be handled for the specified window using a specfic key.
    """

    #: A constant which can be used with the rate_key property of a RateLimitingPolicy.
    #: This constant has a value of "CLIENT_IP"
    RATE_KEY_CLIENT_IP = "CLIENT_IP"

    #: A constant which can be used with the rate_key property of a RateLimitingPolicy.
    #: This constant has a value of "TOTAL"
    RATE_KEY_TOTAL = "TOTAL"

    def __init__(self, **kwargs):
        """
        Initializes a new RateLimitingPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rate_in_requests_per_second:
            The value to assign to the rate_in_requests_per_second property of this RateLimitingPolicy.
        :type rate_in_requests_per_second: int

        :param rate_key:
            The value to assign to the rate_key property of this RateLimitingPolicy.
            Allowed values for this property are: "CLIENT_IP", "TOTAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rate_key: str

        """
        self.swagger_types = {
            'rate_in_requests_per_second': 'int',
            'rate_key': 'str'
        }

        self.attribute_map = {
            'rate_in_requests_per_second': 'rateInRequestsPerSecond',
            'rate_key': 'rateKey'
        }

        self._rate_in_requests_per_second = None
        self._rate_key = None

    @property
    def rate_in_requests_per_second(self):
        """
        **[Required]** Gets the rate_in_requests_per_second of this RateLimitingPolicy.
        The maximum number of requests per second to allow.


        :return: The rate_in_requests_per_second of this RateLimitingPolicy.
        :rtype: int
        """
        return self._rate_in_requests_per_second

    @rate_in_requests_per_second.setter
    def rate_in_requests_per_second(self, rate_in_requests_per_second):
        """
        Sets the rate_in_requests_per_second of this RateLimitingPolicy.
        The maximum number of requests per second to allow.


        :param rate_in_requests_per_second: The rate_in_requests_per_second of this RateLimitingPolicy.
        :type: int
        """
        self._rate_in_requests_per_second = rate_in_requests_per_second

    @property
    def rate_key(self):
        """
        **[Required]** Gets the rate_key of this RateLimitingPolicy.
        The key used to group requests together.

        Allowed values for this property are: "CLIENT_IP", "TOTAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rate_key of this RateLimitingPolicy.
        :rtype: str
        """
        return self._rate_key

    @rate_key.setter
    def rate_key(self, rate_key):
        """
        Sets the rate_key of this RateLimitingPolicy.
        The key used to group requests together.


        :param rate_key: The rate_key of this RateLimitingPolicy.
        :type: str
        """
        allowed_values = ["CLIENT_IP", "TOTAL"]
        if not value_allowed_none_or_none_sentinel(rate_key, allowed_values):
            rate_key = 'UNKNOWN_ENUM_VALUE'
        self._rate_key = rate_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
