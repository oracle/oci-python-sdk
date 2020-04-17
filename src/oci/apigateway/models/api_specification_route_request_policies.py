# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSpecificationRouteRequestPolicies(object):
    """
    Behavior applied to any requests received by the API on this route.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSpecificationRouteRequestPolicies object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param authorization:
            The value to assign to the authorization property of this ApiSpecificationRouteRequestPolicies.
        :type authorization: RouteAuthorizationPolicy

        :param cors:
            The value to assign to the cors property of this ApiSpecificationRouteRequestPolicies.
        :type cors: CorsPolicy

        """
        self.swagger_types = {
            'authorization': 'RouteAuthorizationPolicy',
            'cors': 'CorsPolicy'
        }

        self.attribute_map = {
            'authorization': 'authorization',
            'cors': 'cors'
        }

        self._authorization = None
        self._cors = None

    @property
    def authorization(self):
        """
        Gets the authorization of this ApiSpecificationRouteRequestPolicies.

        :return: The authorization of this ApiSpecificationRouteRequestPolicies.
        :rtype: RouteAuthorizationPolicy
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """
        Sets the authorization of this ApiSpecificationRouteRequestPolicies.

        :param authorization: The authorization of this ApiSpecificationRouteRequestPolicies.
        :type: RouteAuthorizationPolicy
        """
        self._authorization = authorization

    @property
    def cors(self):
        """
        Gets the cors of this ApiSpecificationRouteRequestPolicies.

        :return: The cors of this ApiSpecificationRouteRequestPolicies.
        :rtype: CorsPolicy
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """
        Sets the cors of this ApiSpecificationRouteRequestPolicies.

        :param cors: The cors of this ApiSpecificationRouteRequestPolicies.
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
