# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSpecificationRequestPolicies(object):
    """
    Global behavior applied to all requests received by the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSpecificationRequestPolicies object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param authentication:
            The value to assign to the authentication property of this ApiSpecificationRequestPolicies.
        :type authentication: AuthenticationPolicy

        :param rate_limiting:
            The value to assign to the rate_limiting property of this ApiSpecificationRequestPolicies.
        :type rate_limiting: RateLimitingPolicy

        :param cors:
            The value to assign to the cors property of this ApiSpecificationRequestPolicies.
        :type cors: CorsPolicy

        """
        self.swagger_types = {
            'authentication': 'AuthenticationPolicy',
            'rate_limiting': 'RateLimitingPolicy',
            'cors': 'CorsPolicy'
        }

        self.attribute_map = {
            'authentication': 'authentication',
            'rate_limiting': 'rateLimiting',
            'cors': 'cors'
        }

        self._authentication = None
        self._rate_limiting = None
        self._cors = None

    @property
    def authentication(self):
        """
        Gets the authentication of this ApiSpecificationRequestPolicies.

        :return: The authentication of this ApiSpecificationRequestPolicies.
        :rtype: AuthenticationPolicy
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """
        Sets the authentication of this ApiSpecificationRequestPolicies.

        :param authentication: The authentication of this ApiSpecificationRequestPolicies.
        :type: AuthenticationPolicy
        """
        self._authentication = authentication

    @property
    def rate_limiting(self):
        """
        Gets the rate_limiting of this ApiSpecificationRequestPolicies.

        :return: The rate_limiting of this ApiSpecificationRequestPolicies.
        :rtype: RateLimitingPolicy
        """
        return self._rate_limiting

    @rate_limiting.setter
    def rate_limiting(self, rate_limiting):
        """
        Sets the rate_limiting of this ApiSpecificationRequestPolicies.

        :param rate_limiting: The rate_limiting of this ApiSpecificationRequestPolicies.
        :type: RateLimitingPolicy
        """
        self._rate_limiting = rate_limiting

    @property
    def cors(self):
        """
        Gets the cors of this ApiSpecificationRequestPolicies.

        :return: The cors of this ApiSpecificationRequestPolicies.
        :rtype: CorsPolicy
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """
        Sets the cors of this ApiSpecificationRequestPolicies.

        :param cors: The cors of this ApiSpecificationRequestPolicies.
        :type: CorsPolicy
        """
        self._cors = cors

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
