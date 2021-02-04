# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricDataPoint(object):
    """
    The metric values with dimension details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetricDataPoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this MetricDataPoint.
        :type value: float

        :param unit:
            The value to assign to the unit property of this MetricDataPoint.
        :type unit: str

        :param dimensions:
            The value to assign to the dimensions property of this MetricDataPoint.
        :type dimensions: list[oci.database_management.models.MetricDimensionDefinition]

        """
        self.swagger_types = {
            'value': 'float',
            'unit': 'str',
            'dimensions': 'list[MetricDimensionDefinition]'
        }

        self.attribute_map = {
            'value': 'value',
            'unit': 'unit',
            'dimensions': 'dimensions'
        }

        self._value = None
        self._unit = None
        self._dimensions = None

    @property
    def value(self):
        """
        Gets the value of this MetricDataPoint.
        The value of the metric.


        :return: The value of this MetricDataPoint.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MetricDataPoint.
        The value of the metric.


        :param value: The value of this MetricDataPoint.
        :type: float
        """
        self._value = value

    @property
    def unit(self):
        """
        Gets the unit of this MetricDataPoint.
        The unit of the metric value.


        :return: The unit of this MetricDataPoint.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this MetricDataPoint.
        The unit of the metric value.


        :param unit: The unit of this MetricDataPoint.
        :type: str
        """
        self._unit = unit

    @property
    def dimensions(self):
        """
        Gets the dimensions of this MetricDataPoint.
        The dimensions of the metric.


        :return: The dimensions of this MetricDataPoint.
        :rtype: list[oci.database_management.models.MetricDimensionDefinition]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this MetricDataPoint.
        The dimensions of the metric.


        :param dimensions: The dimensions of this MetricDataPoint.
        :type: list[oci.database_management.models.MetricDimensionDefinition]
        """
        self._dimensions = dimensions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
