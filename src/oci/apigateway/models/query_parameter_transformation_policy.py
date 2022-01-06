# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryParameterTransformationPolicy(object):
    """
    A set of transformations to apply to query parameters that pass through the gateway.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryParameterTransformationPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param set_query_parameters:
            The value to assign to the set_query_parameters property of this QueryParameterTransformationPolicy.
        :type set_query_parameters: oci.apigateway.models.SetQueryParameterPolicy

        :param rename_query_parameters:
            The value to assign to the rename_query_parameters property of this QueryParameterTransformationPolicy.
        :type rename_query_parameters: oci.apigateway.models.RenameQueryParameterPolicy

        :param filter_query_parameters:
            The value to assign to the filter_query_parameters property of this QueryParameterTransformationPolicy.
        :type filter_query_parameters: oci.apigateway.models.FilterQueryParameterPolicy

        """
        self.swagger_types = {
            'set_query_parameters': 'SetQueryParameterPolicy',
            'rename_query_parameters': 'RenameQueryParameterPolicy',
            'filter_query_parameters': 'FilterQueryParameterPolicy'
        }

        self.attribute_map = {
            'set_query_parameters': 'setQueryParameters',
            'rename_query_parameters': 'renameQueryParameters',
            'filter_query_parameters': 'filterQueryParameters'
        }

        self._set_query_parameters = None
        self._rename_query_parameters = None
        self._filter_query_parameters = None

    @property
    def set_query_parameters(self):
        """
        Gets the set_query_parameters of this QueryParameterTransformationPolicy.

        :return: The set_query_parameters of this QueryParameterTransformationPolicy.
        :rtype: oci.apigateway.models.SetQueryParameterPolicy
        """
        return self._set_query_parameters

    @set_query_parameters.setter
    def set_query_parameters(self, set_query_parameters):
        """
        Sets the set_query_parameters of this QueryParameterTransformationPolicy.

        :param set_query_parameters: The set_query_parameters of this QueryParameterTransformationPolicy.
        :type: oci.apigateway.models.SetQueryParameterPolicy
        """
        self._set_query_parameters = set_query_parameters

    @property
    def rename_query_parameters(self):
        """
        Gets the rename_query_parameters of this QueryParameterTransformationPolicy.

        :return: The rename_query_parameters of this QueryParameterTransformationPolicy.
        :rtype: oci.apigateway.models.RenameQueryParameterPolicy
        """
        return self._rename_query_parameters

    @rename_query_parameters.setter
    def rename_query_parameters(self, rename_query_parameters):
        """
        Sets the rename_query_parameters of this QueryParameterTransformationPolicy.

        :param rename_query_parameters: The rename_query_parameters of this QueryParameterTransformationPolicy.
        :type: oci.apigateway.models.RenameQueryParameterPolicy
        """
        self._rename_query_parameters = rename_query_parameters

    @property
    def filter_query_parameters(self):
        """
        Gets the filter_query_parameters of this QueryParameterTransformationPolicy.

        :return: The filter_query_parameters of this QueryParameterTransformationPolicy.
        :rtype: oci.apigateway.models.FilterQueryParameterPolicy
        """
        return self._filter_query_parameters

    @filter_query_parameters.setter
    def filter_query_parameters(self, filter_query_parameters):
        """
        Sets the filter_query_parameters of this QueryParameterTransformationPolicy.

        :param filter_query_parameters: The filter_query_parameters of this QueryParameterTransformationPolicy.
        :type: oci.apigateway.models.FilterQueryParameterPolicy
        """
        self._filter_query_parameters = filter_query_parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
