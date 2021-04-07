# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .response_cache_store_policy import ResponseCacheStorePolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FixedTTLResponseCacheStorePolicy(ResponseCacheStorePolicy):
    """
    How a response from a backend is cached in the Response Cache.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FixedTTLResponseCacheStorePolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.FixedTTLResponseCacheStorePolicy.type` attribute
        of this class is ``FIXED_TTL_STORE_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FixedTTLResponseCacheStorePolicy.
            Allowed values for this property are: "FIXED_TTL_STORE_POLICY"
        :type type: str

        :param time_to_live_in_seconds:
            The value to assign to the time_to_live_in_seconds property of this FixedTTLResponseCacheStorePolicy.
        :type time_to_live_in_seconds: int

        """
        self.swagger_types = {
            'type': 'str',
            'time_to_live_in_seconds': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'time_to_live_in_seconds': 'timeToLiveInSeconds'
        }

        self._type = None
        self._time_to_live_in_seconds = None
        self._type = 'FIXED_TTL_STORE_POLICY'

    @property
    def time_to_live_in_seconds(self):
        """
        **[Required]** Gets the time_to_live_in_seconds of this FixedTTLResponseCacheStorePolicy.
        Sets the number of seconds for a response from a backend being stored in the Response Cache before it expires.


        :return: The time_to_live_in_seconds of this FixedTTLResponseCacheStorePolicy.
        :rtype: int
        """
        return self._time_to_live_in_seconds

    @time_to_live_in_seconds.setter
    def time_to_live_in_seconds(self, time_to_live_in_seconds):
        """
        Sets the time_to_live_in_seconds of this FixedTTLResponseCacheStorePolicy.
        Sets the number of seconds for a response from a backend being stored in the Response Cache before it expires.


        :param time_to_live_in_seconds: The time_to_live_in_seconds of this FixedTTLResponseCacheStorePolicy.
        :type: int
        """
        self._time_to_live_in_seconds = time_to_live_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
