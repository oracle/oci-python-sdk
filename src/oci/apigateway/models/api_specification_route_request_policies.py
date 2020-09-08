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

        :param header_transformations:
            The value to assign to the header_transformations property of this ApiSpecificationRouteRequestPolicies.
        :type header_transformations: HeaderTransformationPolicy

        :param query_parameter_transformations:
            The value to assign to the query_parameter_transformations property of this ApiSpecificationRouteRequestPolicies.
        :type query_parameter_transformations: QueryParameterTransformationPolicy

        """
        self.swagger_types = {
            'authorization': 'RouteAuthorizationPolicy',
            'cors': 'CorsPolicy',
            'header_transformations': 'HeaderTransformationPolicy',
            'query_parameter_transformations': 'QueryParameterTransformationPolicy'
        }

        self.attribute_map = {
            'authorization': 'authorization',
            'cors': 'cors',
            'header_transformations': 'headerTransformations',
            'query_parameter_transformations': 'queryParameterTransformations'
        }

        self._authorization = None
        self._cors = None
        self._header_transformations = None
        self._query_parameter_transformations = None

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

    @property
    def header_transformations(self):
        """
        Gets the header_transformations of this ApiSpecificationRouteRequestPolicies.

        :return: The header_transformations of this ApiSpecificationRouteRequestPolicies.
        :rtype: HeaderTransformationPolicy
        """
        return self._header_transformations

    @header_transformations.setter
    def header_transformations(self, header_transformations):
        """
        Sets the header_transformations of this ApiSpecificationRouteRequestPolicies.

        :param header_transformations: The header_transformations of this ApiSpecificationRouteRequestPolicies.
        :type: HeaderTransformationPolicy
        """
        self._header_transformations = header_transformations

    @property
    def query_parameter_transformations(self):
        """
        Gets the query_parameter_transformations of this ApiSpecificationRouteRequestPolicies.

        :return: The query_parameter_transformations of this ApiSpecificationRouteRequestPolicies.
        :rtype: QueryParameterTransformationPolicy
        """
        return self._query_parameter_transformations

    @query_parameter_transformations.setter
    def query_parameter_transformations(self, query_parameter_transformations):
        """
        Sets the query_parameter_transformations of this ApiSpecificationRouteRequestPolicies.

        :param query_parameter_transformations: The query_parameter_transformations of this ApiSpecificationRouteRequestPolicies.
        :type: QueryParameterTransformationPolicy
        """
        self._query_parameter_transformations = query_parameter_transformations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
