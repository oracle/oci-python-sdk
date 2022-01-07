# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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
        :type authorization: oci.apigateway.models.RouteAuthorizationPolicy

        :param cors:
            The value to assign to the cors property of this ApiSpecificationRouteRequestPolicies.
        :type cors: oci.apigateway.models.CorsPolicy

        :param query_parameter_validations:
            The value to assign to the query_parameter_validations property of this ApiSpecificationRouteRequestPolicies.
        :type query_parameter_validations: oci.apigateway.models.QueryParameterValidationRequestPolicy

        :param header_validations:
            The value to assign to the header_validations property of this ApiSpecificationRouteRequestPolicies.
        :type header_validations: oci.apigateway.models.HeaderValidationRequestPolicy

        :param body_validation:
            The value to assign to the body_validation property of this ApiSpecificationRouteRequestPolicies.
        :type body_validation: oci.apigateway.models.BodyValidationRequestPolicy

        :param header_transformations:
            The value to assign to the header_transformations property of this ApiSpecificationRouteRequestPolicies.
        :type header_transformations: oci.apigateway.models.HeaderTransformationPolicy

        :param query_parameter_transformations:
            The value to assign to the query_parameter_transformations property of this ApiSpecificationRouteRequestPolicies.
        :type query_parameter_transformations: oci.apigateway.models.QueryParameterTransformationPolicy

        :param response_cache_lookup:
            The value to assign to the response_cache_lookup property of this ApiSpecificationRouteRequestPolicies.
        :type response_cache_lookup: oci.apigateway.models.ResponseCacheLookupPolicy

        """
        self.swagger_types = {
            'authorization': 'RouteAuthorizationPolicy',
            'cors': 'CorsPolicy',
            'query_parameter_validations': 'QueryParameterValidationRequestPolicy',
            'header_validations': 'HeaderValidationRequestPolicy',
            'body_validation': 'BodyValidationRequestPolicy',
            'header_transformations': 'HeaderTransformationPolicy',
            'query_parameter_transformations': 'QueryParameterTransformationPolicy',
            'response_cache_lookup': 'ResponseCacheLookupPolicy'
        }

        self.attribute_map = {
            'authorization': 'authorization',
            'cors': 'cors',
            'query_parameter_validations': 'queryParameterValidations',
            'header_validations': 'headerValidations',
            'body_validation': 'bodyValidation',
            'header_transformations': 'headerTransformations',
            'query_parameter_transformations': 'queryParameterTransformations',
            'response_cache_lookup': 'responseCacheLookup'
        }

        self._authorization = None
        self._cors = None
        self._query_parameter_validations = None
        self._header_validations = None
        self._body_validation = None
        self._header_transformations = None
        self._query_parameter_transformations = None
        self._response_cache_lookup = None

    @property
    def authorization(self):
        """
        Gets the authorization of this ApiSpecificationRouteRequestPolicies.

        :return: The authorization of this ApiSpecificationRouteRequestPolicies.
        :rtype: oci.apigateway.models.RouteAuthorizationPolicy
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """
        Sets the authorization of this ApiSpecificationRouteRequestPolicies.

        :param authorization: The authorization of this ApiSpecificationRouteRequestPolicies.
        :type: oci.apigateway.models.RouteAuthorizationPolicy
        """
        self._authorization = authorization

    @property
    def cors(self):
        """
        Gets the cors of this ApiSpecificationRouteRequestPolicies.

        :return: The cors of this ApiSpecificationRouteRequestPolicies.
        :rtype: oci.apigateway.models.CorsPolicy
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """
        Sets the cors of this ApiSpecificationRouteRequestPolicies.

        :param cors: The cors of this ApiSpecificationRouteRequestPolicies.
        :type: oci.apigateway.models.CorsPolicy
        """
        self._cors = cors

    @property
    def query_parameter_validations(self):
        """
        Gets the query_parameter_validations of this ApiSpecificationRouteRequestPolicies.

        :return: The query_parameter_validations of this ApiSpecificationRouteRequestPolicies.
        :rtype: oci.apigateway.models.QueryParameterValidationRequestPolicy
        """
        return self._query_parameter_validations

    @query_parameter_validations.setter
    def query_parameter_validations(self, query_parameter_validations):
        """
        Sets the query_parameter_validations of this ApiSpecificationRouteRequestPolicies.

        :param query_parameter_validations: The query_parameter_validations of this ApiSpecificationRouteRequestPolicies.
        :type: oci.apigateway.models.QueryParameterValidationRequestPolicy
        """
        self._query_parameter_validations = query_parameter_validations

    @property
    def header_validations(self):
        """
        Gets the header_validations of this ApiSpecificationRouteRequestPolicies.

        :return: The header_validations of this ApiSpecificationRouteRequestPolicies.
        :rtype: oci.apigateway.models.HeaderValidationRequestPolicy
        """
        return self._header_validations

    @header_validations.setter
    def header_validations(self, header_validations):
        """
        Sets the header_validations of this ApiSpecificationRouteRequestPolicies.

        :param header_validations: The header_validations of this ApiSpecificationRouteRequestPolicies.
        :type: oci.apigateway.models.HeaderValidationRequestPolicy
        """
        self._header_validations = header_validations

    @property
    def body_validation(self):
        """
        Gets the body_validation of this ApiSpecificationRouteRequestPolicies.

        :return: The body_validation of this ApiSpecificationRouteRequestPolicies.
        :rtype: oci.apigateway.models.BodyValidationRequestPolicy
        """
        return self._body_validation

    @body_validation.setter
    def body_validation(self, body_validation):
        """
        Sets the body_validation of this ApiSpecificationRouteRequestPolicies.

        :param body_validation: The body_validation of this ApiSpecificationRouteRequestPolicies.
        :type: oci.apigateway.models.BodyValidationRequestPolicy
        """
        self._body_validation = body_validation

    @property
    def header_transformations(self):
        """
        Gets the header_transformations of this ApiSpecificationRouteRequestPolicies.

        :return: The header_transformations of this ApiSpecificationRouteRequestPolicies.
        :rtype: oci.apigateway.models.HeaderTransformationPolicy
        """
        return self._header_transformations

    @header_transformations.setter
    def header_transformations(self, header_transformations):
        """
        Sets the header_transformations of this ApiSpecificationRouteRequestPolicies.

        :param header_transformations: The header_transformations of this ApiSpecificationRouteRequestPolicies.
        :type: oci.apigateway.models.HeaderTransformationPolicy
        """
        self._header_transformations = header_transformations

    @property
    def query_parameter_transformations(self):
        """
        Gets the query_parameter_transformations of this ApiSpecificationRouteRequestPolicies.

        :return: The query_parameter_transformations of this ApiSpecificationRouteRequestPolicies.
        :rtype: oci.apigateway.models.QueryParameterTransformationPolicy
        """
        return self._query_parameter_transformations

    @query_parameter_transformations.setter
    def query_parameter_transformations(self, query_parameter_transformations):
        """
        Sets the query_parameter_transformations of this ApiSpecificationRouteRequestPolicies.

        :param query_parameter_transformations: The query_parameter_transformations of this ApiSpecificationRouteRequestPolicies.
        :type: oci.apigateway.models.QueryParameterTransformationPolicy
        """
        self._query_parameter_transformations = query_parameter_transformations

    @property
    def response_cache_lookup(self):
        """
        Gets the response_cache_lookup of this ApiSpecificationRouteRequestPolicies.

        :return: The response_cache_lookup of this ApiSpecificationRouteRequestPolicies.
        :rtype: oci.apigateway.models.ResponseCacheLookupPolicy
        """
        return self._response_cache_lookup

    @response_cache_lookup.setter
    def response_cache_lookup(self, response_cache_lookup):
        """
        Sets the response_cache_lookup of this ApiSpecificationRouteRequestPolicies.

        :param response_cache_lookup: The response_cache_lookup of this ApiSpecificationRouteRequestPolicies.
        :type: oci.apigateway.models.ResponseCacheLookupPolicy
        """
        self._response_cache_lookup = response_cache_lookup

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
