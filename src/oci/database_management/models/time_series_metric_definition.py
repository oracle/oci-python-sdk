# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TimeSeriesMetricDefinition(object):
    """
    The response object representing time series metric details
    for a specific database at a particular time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TimeSeriesMetricDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this TimeSeriesMetricDefinition.
        :type metric_name: str

        :param datapoints:
            The value to assign to the datapoints property of this TimeSeriesMetricDefinition.
        :type datapoints: list[oci.database_management.models.TimeSeriesMetricDataPoint]

        """
        self.swagger_types = {
            'metric_name': 'str',
            'datapoints': 'list[TimeSeriesMetricDataPoint]'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'datapoints': 'datapoints'
        }

        self._metric_name = None
        self._datapoints = None

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this TimeSeriesMetricDefinition.
        The name of the metric the time series data corresponds to.


        :return: The metric_name of this TimeSeriesMetricDefinition.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this TimeSeriesMetricDefinition.
        The name of the metric the time series data corresponds to.


        :param metric_name: The metric_name of this TimeSeriesMetricDefinition.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def datapoints(self):
        """
        **[Required]** Gets the datapoints of this TimeSeriesMetricDefinition.
        The time series metric data for the given metric.


        :return: The datapoints of this TimeSeriesMetricDefinition.
        :rtype: list[oci.database_management.models.TimeSeriesMetricDataPoint]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        """
        Sets the datapoints of this TimeSeriesMetricDefinition.
        The time series metric data for the given metric.


        :param datapoints: The datapoints of this TimeSeriesMetricDefinition.
        :type: list[oci.database_management.models.TimeSeriesMetricDataPoint]
        """
        self._datapoints = datapoints

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
