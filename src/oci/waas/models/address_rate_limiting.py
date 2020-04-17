# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddressRateLimiting(object):
    """
    The IP rate limiting configuration. Defines the amount of allowed requests from a unique IP address and the resulting block response code when that threshold is exceeded.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddressRateLimiting object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this AddressRateLimiting.
        :type is_enabled: bool

        :param allowed_rate_per_address:
            The value to assign to the allowed_rate_per_address property of this AddressRateLimiting.
        :type allowed_rate_per_address: int

        :param max_delayed_count_per_address:
            The value to assign to the max_delayed_count_per_address property of this AddressRateLimiting.
        :type max_delayed_count_per_address: int

        :param block_response_code:
            The value to assign to the block_response_code property of this AddressRateLimiting.
        :type block_response_code: int

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'allowed_rate_per_address': 'int',
            'max_delayed_count_per_address': 'int',
            'block_response_code': 'int'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'allowed_rate_per_address': 'allowedRatePerAddress',
            'max_delayed_count_per_address': 'maxDelayedCountPerAddress',
            'block_response_code': 'blockResponseCode'
        }

        self._is_enabled = None
        self._allowed_rate_per_address = None
        self._max_delayed_count_per_address = None
        self._block_response_code = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this AddressRateLimiting.
        Enables or disables the address rate limiting Web Application Firewall feature.


        :return: The is_enabled of this AddressRateLimiting.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AddressRateLimiting.
        Enables or disables the address rate limiting Web Application Firewall feature.


        :param is_enabled: The is_enabled of this AddressRateLimiting.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def allowed_rate_per_address(self):
        """
        Gets the allowed_rate_per_address of this AddressRateLimiting.
        The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.


        :return: The allowed_rate_per_address of this AddressRateLimiting.
        :rtype: int
        """
        return self._allowed_rate_per_address

    @allowed_rate_per_address.setter
    def allowed_rate_per_address(self, allowed_rate_per_address):
        """
        Sets the allowed_rate_per_address of this AddressRateLimiting.
        The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.


        :param allowed_rate_per_address: The allowed_rate_per_address of this AddressRateLimiting.
        :type: int
        """
        self._allowed_rate_per_address = allowed_rate_per_address

    @property
    def max_delayed_count_per_address(self):
        """
        Gets the max_delayed_count_per_address of this AddressRateLimiting.
        The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.


        :return: The max_delayed_count_per_address of this AddressRateLimiting.
        :rtype: int
        """
        return self._max_delayed_count_per_address

    @max_delayed_count_per_address.setter
    def max_delayed_count_per_address(self, max_delayed_count_per_address):
        """
        Sets the max_delayed_count_per_address of this AddressRateLimiting.
        The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.


        :param max_delayed_count_per_address: The max_delayed_count_per_address of this AddressRateLimiting.
        :type: int
        """
        self._max_delayed_count_per_address = max_delayed_count_per_address

    @property
    def block_response_code(self):
        """
        Gets the block_response_code of this AddressRateLimiting.
        The response status code returned when a request is blocked. If unspecified, defaults to `503`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.


        :return: The block_response_code of this AddressRateLimiting.
        :rtype: int
        """
        return self._block_response_code

    @block_response_code.setter
    def block_response_code(self, block_response_code):
        """
        Sets the block_response_code of this AddressRateLimiting.
        The response status code returned when a request is blocked. If unspecified, defaults to `503`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.


        :param block_response_code: The block_response_code of this AddressRateLimiting.
        :type: int
        """
        self._block_response_code = block_response_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
