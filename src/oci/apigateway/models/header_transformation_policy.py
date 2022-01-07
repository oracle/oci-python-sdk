# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HeaderTransformationPolicy(object):
    """
    A set of transformations to apply to HTTP headers that pass through the gateway.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HeaderTransformationPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param set_headers:
            The value to assign to the set_headers property of this HeaderTransformationPolicy.
        :type set_headers: oci.apigateway.models.SetHeaderPolicy

        :param rename_headers:
            The value to assign to the rename_headers property of this HeaderTransformationPolicy.
        :type rename_headers: oci.apigateway.models.RenameHeaderPolicy

        :param filter_headers:
            The value to assign to the filter_headers property of this HeaderTransformationPolicy.
        :type filter_headers: oci.apigateway.models.FilterHeaderPolicy

        """
        self.swagger_types = {
            'set_headers': 'SetHeaderPolicy',
            'rename_headers': 'RenameHeaderPolicy',
            'filter_headers': 'FilterHeaderPolicy'
        }

        self.attribute_map = {
            'set_headers': 'setHeaders',
            'rename_headers': 'renameHeaders',
            'filter_headers': 'filterHeaders'
        }

        self._set_headers = None
        self._rename_headers = None
        self._filter_headers = None

    @property
    def set_headers(self):
        """
        Gets the set_headers of this HeaderTransformationPolicy.

        :return: The set_headers of this HeaderTransformationPolicy.
        :rtype: oci.apigateway.models.SetHeaderPolicy
        """
        return self._set_headers

    @set_headers.setter
    def set_headers(self, set_headers):
        """
        Sets the set_headers of this HeaderTransformationPolicy.

        :param set_headers: The set_headers of this HeaderTransformationPolicy.
        :type: oci.apigateway.models.SetHeaderPolicy
        """
        self._set_headers = set_headers

    @property
    def rename_headers(self):
        """
        Gets the rename_headers of this HeaderTransformationPolicy.

        :return: The rename_headers of this HeaderTransformationPolicy.
        :rtype: oci.apigateway.models.RenameHeaderPolicy
        """
        return self._rename_headers

    @rename_headers.setter
    def rename_headers(self, rename_headers):
        """
        Sets the rename_headers of this HeaderTransformationPolicy.

        :param rename_headers: The rename_headers of this HeaderTransformationPolicy.
        :type: oci.apigateway.models.RenameHeaderPolicy
        """
        self._rename_headers = rename_headers

    @property
    def filter_headers(self):
        """
        Gets the filter_headers of this HeaderTransformationPolicy.

        :return: The filter_headers of this HeaderTransformationPolicy.
        :rtype: oci.apigateway.models.FilterHeaderPolicy
        """
        return self._filter_headers

    @filter_headers.setter
    def filter_headers(self, filter_headers):
        """
        Sets the filter_headers of this HeaderTransformationPolicy.

        :param filter_headers: The filter_headers of this HeaderTransformationPolicy.
        :type: oci.apigateway.models.FilterHeaderPolicy
        """
        self._filter_headers = filter_headers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
