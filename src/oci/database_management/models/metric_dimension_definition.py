# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricDimensionDefinition(object):
    """
    The metric dimension details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetricDimensionDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimension_name:
            The value to assign to the dimension_name property of this MetricDimensionDefinition.
        :type dimension_name: str

        :param dimension_value:
            The value to assign to the dimension_value property of this MetricDimensionDefinition.
        :type dimension_value: str

        """
        self.swagger_types = {
            'dimension_name': 'str',
            'dimension_value': 'str'
        }

        self.attribute_map = {
            'dimension_name': 'dimensionName',
            'dimension_value': 'dimensionValue'
        }

        self._dimension_name = None
        self._dimension_value = None

    @property
    def dimension_name(self):
        """
        Gets the dimension_name of this MetricDimensionDefinition.
        The name of the dimension.


        :return: The dimension_name of this MetricDimensionDefinition.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        """
        Sets the dimension_name of this MetricDimensionDefinition.
        The name of the dimension.


        :param dimension_name: The dimension_name of this MetricDimensionDefinition.
        :type: str
        """
        self._dimension_name = dimension_name

    @property
    def dimension_value(self):
        """
        Gets the dimension_value of this MetricDimensionDefinition.
        The value of the dimension.


        :return: The dimension_value of this MetricDimensionDefinition.
        :rtype: str
        """
        return self._dimension_value

    @dimension_value.setter
    def dimension_value(self, dimension_value):
        """
        Sets the dimension_value of this MetricDimensionDefinition.
        The value of the dimension.


        :param dimension_value: The dimension_value of this MetricDimensionDefinition.
        :type: str
        """
        self._dimension_value = dimension_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
