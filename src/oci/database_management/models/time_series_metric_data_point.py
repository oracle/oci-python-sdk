# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TimeSeriesMetricDataPoint(object):
    """
    The metric values with dimension details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TimeSeriesMetricDataPoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this TimeSeriesMetricDataPoint.
        :type timestamp: datetime

        :param value:
            The value to assign to the value property of this TimeSeriesMetricDataPoint.
        :type value: float

        :param unit:
            The value to assign to the unit property of this TimeSeriesMetricDataPoint.
        :type unit: str

        :param dimensions:
            The value to assign to the dimensions property of this TimeSeriesMetricDataPoint.
        :type dimensions: list[oci.database_management.models.MetricDimensionDefinition]

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'value': 'float',
            'unit': 'str',
            'dimensions': 'list[MetricDimensionDefinition]'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'value': 'value',
            'unit': 'unit',
            'dimensions': 'dimensions'
        }

        self._timestamp = None
        self._value = None
        self._unit = None
        self._dimensions = None

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this TimeSeriesMetricDataPoint.
        The date and time the metric was created.


        :return: The timestamp of this TimeSeriesMetricDataPoint.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this TimeSeriesMetricDataPoint.
        The date and time the metric was created.


        :param timestamp: The timestamp of this TimeSeriesMetricDataPoint.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def value(self):
        """
        **[Required]** Gets the value of this TimeSeriesMetricDataPoint.
        The value of the metric.


        :return: The value of this TimeSeriesMetricDataPoint.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this TimeSeriesMetricDataPoint.
        The value of the metric.


        :param value: The value of this TimeSeriesMetricDataPoint.
        :type: float
        """
        self._value = value

    @property
    def unit(self):
        """
        **[Required]** Gets the unit of this TimeSeriesMetricDataPoint.
        The unit of the metric value.


        :return: The unit of this TimeSeriesMetricDataPoint.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this TimeSeriesMetricDataPoint.
        The unit of the metric value.


        :param unit: The unit of this TimeSeriesMetricDataPoint.
        :type: str
        """
        self._unit = unit

    @property
    def dimensions(self):
        """
        Gets the dimensions of this TimeSeriesMetricDataPoint.
        The dimensions of the metric.


        :return: The dimensions of this TimeSeriesMetricDataPoint.
        :rtype: list[oci.database_management.models.MetricDimensionDefinition]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this TimeSeriesMetricDataPoint.
        The dimensions of the metric.


        :param dimensions: The dimensions of this TimeSeriesMetricDataPoint.
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
