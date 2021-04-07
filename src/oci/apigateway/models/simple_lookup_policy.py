# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .response_cache_lookup_policy import ResponseCacheLookupPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SimpleLookupPolicy(ResponseCacheLookupPolicy):
    """
    Provides ability to vary the cache key using context expressions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SimpleLookupPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.SimpleLookupPolicy.type` attribute
        of this class is ``SIMPLE_LOOKUP_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SimpleLookupPolicy.
            Allowed values for this property are: "SIMPLE_LOOKUP_POLICY"
        :type type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this SimpleLookupPolicy.
        :type is_enabled: bool

        :param is_private_caching_enabled:
            The value to assign to the is_private_caching_enabled property of this SimpleLookupPolicy.
        :type is_private_caching_enabled: bool

        :param cache_key_additions:
            The value to assign to the cache_key_additions property of this SimpleLookupPolicy.
        :type cache_key_additions: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'is_enabled': 'bool',
            'is_private_caching_enabled': 'bool',
            'cache_key_additions': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'is_enabled': 'isEnabled',
            'is_private_caching_enabled': 'isPrivateCachingEnabled',
            'cache_key_additions': 'cacheKeyAdditions'
        }

        self._type = None
        self._is_enabled = None
        self._is_private_caching_enabled = None
        self._cache_key_additions = None
        self._type = 'SIMPLE_LOOKUP_POLICY'

    @property
    def cache_key_additions(self):
        """
        Gets the cache_key_additions of this SimpleLookupPolicy.
        A list of context expressions whose values will be added to the base cache key. Values should contain an expression enclosed within
        ${} delimiters. Only the request context is available.


        :return: The cache_key_additions of this SimpleLookupPolicy.
        :rtype: list[str]
        """
        return self._cache_key_additions

    @cache_key_additions.setter
    def cache_key_additions(self, cache_key_additions):
        """
        Sets the cache_key_additions of this SimpleLookupPolicy.
        A list of context expressions whose values will be added to the base cache key. Values should contain an expression enclosed within
        ${} delimiters. Only the request context is available.


        :param cache_key_additions: The cache_key_additions of this SimpleLookupPolicy.
        :type: list[str]
        """
        self._cache_key_additions = cache_key_additions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
