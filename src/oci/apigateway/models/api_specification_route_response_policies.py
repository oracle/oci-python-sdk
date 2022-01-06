# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSpecificationRouteResponsePolicies(object):
    """
    Behavior applied to any responses sent by the API for requests on this route.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSpecificationRouteResponsePolicies object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param header_transformations:
            The value to assign to the header_transformations property of this ApiSpecificationRouteResponsePolicies.
        :type header_transformations: oci.apigateway.models.HeaderTransformationPolicy

        :param response_cache_store:
            The value to assign to the response_cache_store property of this ApiSpecificationRouteResponsePolicies.
        :type response_cache_store: oci.apigateway.models.ResponseCacheStorePolicy

        """
        self.swagger_types = {
            'header_transformations': 'HeaderTransformationPolicy',
            'response_cache_store': 'ResponseCacheStorePolicy'
        }

        self.attribute_map = {
            'header_transformations': 'headerTransformations',
            'response_cache_store': 'responseCacheStore'
        }

        self._header_transformations = None
        self._response_cache_store = None

    @property
    def header_transformations(self):
        """
        Gets the header_transformations of this ApiSpecificationRouteResponsePolicies.

        :return: The header_transformations of this ApiSpecificationRouteResponsePolicies.
        :rtype: oci.apigateway.models.HeaderTransformationPolicy
        """
        return self._header_transformations

    @header_transformations.setter
    def header_transformations(self, header_transformations):
        """
        Sets the header_transformations of this ApiSpecificationRouteResponsePolicies.

        :param header_transformations: The header_transformations of this ApiSpecificationRouteResponsePolicies.
        :type: oci.apigateway.models.HeaderTransformationPolicy
        """
        self._header_transformations = header_transformations

    @property
    def response_cache_store(self):
        """
        Gets the response_cache_store of this ApiSpecificationRouteResponsePolicies.

        :return: The response_cache_store of this ApiSpecificationRouteResponsePolicies.
        :rtype: oci.apigateway.models.ResponseCacheStorePolicy
        """
        return self._response_cache_store

    @response_cache_store.setter
    def response_cache_store(self, response_cache_store):
        """
        Sets the response_cache_store of this ApiSpecificationRouteResponsePolicies.

        :param response_cache_store: The response_cache_store of this ApiSpecificationRouteResponsePolicies.
        :type: oci.apigateway.models.ResponseCacheStorePolicy
        """
        self._response_cache_store = response_cache_store

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
