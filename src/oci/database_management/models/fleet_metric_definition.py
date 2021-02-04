# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetMetricDefinition(object):
    """
    The database metric details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FleetMetricDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this FleetMetricDefinition.
        :type metric_name: str

        :param baseline_value:
            The value to assign to the baseline_value property of this FleetMetricDefinition.
        :type baseline_value: float

        :param target_value:
            The value to assign to the target_value property of this FleetMetricDefinition.
        :type target_value: float

        :param unit:
            The value to assign to the unit property of this FleetMetricDefinition.
        :type unit: str

        :param timestamp:
            The value to assign to the timestamp property of this FleetMetricDefinition.
        :type timestamp: datetime

        :param percentage_change:
            The value to assign to the percentage_change property of this FleetMetricDefinition.
        :type percentage_change: float

        :param dimensions:
            The value to assign to the dimensions property of this FleetMetricDefinition.
        :type dimensions: list[oci.database_management.models.MetricDimensionDefinition]

        """
        self.swagger_types = {
            'metric_name': 'str',
            'baseline_value': 'float',
            'target_value': 'float',
            'unit': 'str',
            'timestamp': 'datetime',
            'percentage_change': 'float',
            'dimensions': 'list[MetricDimensionDefinition]'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'baseline_value': 'baselineValue',
            'target_value': 'targetValue',
            'unit': 'unit',
            'timestamp': 'timestamp',
            'percentage_change': 'percentageChange',
            'dimensions': 'dimensions'
        }

        self._metric_name = None
        self._baseline_value = None
        self._target_value = None
        self._unit = None
        self._timestamp = None
        self._percentage_change = None
        self._dimensions = None

    @property
    def metric_name(self):
        """
        Gets the metric_name of this FleetMetricDefinition.
        The name of the metric.


        :return: The metric_name of this FleetMetricDefinition.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this FleetMetricDefinition.
        The name of the metric.


        :param metric_name: The metric_name of this FleetMetricDefinition.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def baseline_value(self):
        """
        Gets the baseline_value of this FleetMetricDefinition.
        The baseline value of the metric.


        :return: The baseline_value of this FleetMetricDefinition.
        :rtype: float
        """
        return self._baseline_value

    @baseline_value.setter
    def baseline_value(self, baseline_value):
        """
        Sets the baseline_value of this FleetMetricDefinition.
        The baseline value of the metric.


        :param baseline_value: The baseline_value of this FleetMetricDefinition.
        :type: float
        """
        self._baseline_value = baseline_value

    @property
    def target_value(self):
        """
        Gets the target_value of this FleetMetricDefinition.
        The target value of the metric.


        :return: The target_value of this FleetMetricDefinition.
        :rtype: float
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """
        Sets the target_value of this FleetMetricDefinition.
        The target value of the metric.


        :param target_value: The target_value of this FleetMetricDefinition.
        :type: float
        """
        self._target_value = target_value

    @property
    def unit(self):
        """
        Gets the unit of this FleetMetricDefinition.
        The unit of the value.


        :return: The unit of this FleetMetricDefinition.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this FleetMetricDefinition.
        The unit of the value.


        :param unit: The unit of this FleetMetricDefinition.
        :type: str
        """
        self._unit = unit

    @property
    def timestamp(self):
        """
        Gets the timestamp of this FleetMetricDefinition.
        The data point date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :return: The timestamp of this FleetMetricDefinition.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this FleetMetricDefinition.
        The data point date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :param timestamp: The timestamp of this FleetMetricDefinition.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def percentage_change(self):
        """
        Gets the percentage_change of this FleetMetricDefinition.
        The percentage change in the metric aggregated value compared to the baseline value.


        :return: The percentage_change of this FleetMetricDefinition.
        :rtype: float
        """
        return self._percentage_change

    @percentage_change.setter
    def percentage_change(self, percentage_change):
        """
        Sets the percentage_change of this FleetMetricDefinition.
        The percentage change in the metric aggregated value compared to the baseline value.


        :param percentage_change: The percentage_change of this FleetMetricDefinition.
        :type: float
        """
        self._percentage_change = percentage_change

    @property
    def dimensions(self):
        """
        Gets the dimensions of this FleetMetricDefinition.
        The dimensions of the metric.


        :return: The dimensions of this FleetMetricDefinition.
        :rtype: list[oci.database_management.models.MetricDimensionDefinition]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this FleetMetricDefinition.
        The dimensions of the metric.


        :param dimensions: The dimensions of this FleetMetricDefinition.
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
