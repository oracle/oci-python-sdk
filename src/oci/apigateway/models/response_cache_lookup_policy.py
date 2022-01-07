# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponseCacheLookupPolicy(object):
    """
    Base policy for Response Cache lookup.
    """

    #: A constant which can be used with the type property of a ResponseCacheLookupPolicy.
    #: This constant has a value of "SIMPLE_LOOKUP_POLICY"
    TYPE_SIMPLE_LOOKUP_POLICY = "SIMPLE_LOOKUP_POLICY"

    def __init__(self, **kwargs):
        """
        Initializes a new ResponseCacheLookupPolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apigateway.models.SimpleLookupPolicy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ResponseCacheLookupPolicy.
            Allowed values for this property are: "SIMPLE_LOOKUP_POLICY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this ResponseCacheLookupPolicy.
        :type is_enabled: bool

        :param is_private_caching_enabled:
            The value to assign to the is_private_caching_enabled property of this ResponseCacheLookupPolicy.
        :type is_private_caching_enabled: bool

        """
        self.swagger_types = {
            'type': 'str',
            'is_enabled': 'bool',
            'is_private_caching_enabled': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'is_enabled': 'isEnabled',
            'is_private_caching_enabled': 'isPrivateCachingEnabled'
        }

        self._type = None
        self._is_enabled = None
        self._is_private_caching_enabled = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'SIMPLE_LOOKUP_POLICY':
            return 'SimpleLookupPolicy'
        else:
            return 'ResponseCacheLookupPolicy'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ResponseCacheLookupPolicy.
        Type of the Response Cache Store Policy.

        Allowed values for this property are: "SIMPLE_LOOKUP_POLICY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ResponseCacheLookupPolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ResponseCacheLookupPolicy.
        Type of the Response Cache Store Policy.


        :param type: The type of this ResponseCacheLookupPolicy.
        :type: str
        """
        allowed_values = ["SIMPLE_LOOKUP_POLICY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this ResponseCacheLookupPolicy.
        Whether this policy is currently enabled.


        :return: The is_enabled of this ResponseCacheLookupPolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ResponseCacheLookupPolicy.
        Whether this policy is currently enabled.


        :param is_enabled: The is_enabled of this ResponseCacheLookupPolicy.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_private_caching_enabled(self):
        """
        Gets the is_private_caching_enabled of this ResponseCacheLookupPolicy.
        Set true to allow caching responses where the request has an Authorization header. Ensure you have configured your
        cache key additions to get the level of isolation across authenticated requests that you require.

        When false, any request with an Authorization header will not be stored in the Response Cache.

        If using the CustomAuthenticationPolicy then the tokenHeader/tokenQueryParam are also subject to this check.


        :return: The is_private_caching_enabled of this ResponseCacheLookupPolicy.
        :rtype: bool
        """
        return self._is_private_caching_enabled

    @is_private_caching_enabled.setter
    def is_private_caching_enabled(self, is_private_caching_enabled):
        """
        Sets the is_private_caching_enabled of this ResponseCacheLookupPolicy.
        Set true to allow caching responses where the request has an Authorization header. Ensure you have configured your
        cache key additions to get the level of isolation across authenticated requests that you require.

        When false, any request with an Authorization header will not be stored in the Response Cache.

        If using the CustomAuthenticationPolicy then the tokenHeader/tokenQueryParam are also subject to this check.


        :param is_private_caching_enabled: The is_private_caching_enabled of this ResponseCacheLookupPolicy.
        :type: bool
        """
        self._is_private_caching_enabled = is_private_caching_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
