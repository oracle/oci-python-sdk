# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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
        :type header_transformations: HeaderTransformationPolicy

        """
        self.swagger_types = {
            'header_transformations': 'HeaderTransformationPolicy'
        }

        self.attribute_map = {
            'header_transformations': 'headerTransformations'
        }

        self._header_transformations = None

    @property
    def header_transformations(self):
        """
        Gets the header_transformations of this ApiSpecificationRouteResponsePolicies.

        :return: The header_transformations of this ApiSpecificationRouteResponsePolicies.
        :rtype: HeaderTransformationPolicy
        """
        return self._header_transformations

    @header_transformations.setter
    def header_transformations(self, header_transformations):
        """
        Sets the header_transformations of this ApiSpecificationRouteResponsePolicies.

        :param header_transformations: The header_transformations of this ApiSpecificationRouteResponsePolicies.
        :type: HeaderTransformationPolicy
        """
        self._header_transformations = header_transformations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
