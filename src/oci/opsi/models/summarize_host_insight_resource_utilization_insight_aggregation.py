# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeHostInsightResourceUtilizationInsightAggregation(object):
    """
    Insights response containing current/projected groups for CPU or memory.
    """

    #: A constant which can be used with the resource_metric property of a SummarizeHostInsightResourceUtilizationInsightAggregation.
    #: This constant has a value of "CPU"
    RESOURCE_METRIC_CPU = "CPU"

    #: A constant which can be used with the resource_metric property of a SummarizeHostInsightResourceUtilizationInsightAggregation.
    #: This constant has a value of "MEMORY"
    RESOURCE_METRIC_MEMORY = "MEMORY"

    #: A constant which can be used with the resource_metric property of a SummarizeHostInsightResourceUtilizationInsightAggregation.
    #: This constant has a value of "LOGICAL_MEMORY"
    RESOURCE_METRIC_LOGICAL_MEMORY = "LOGICAL_MEMORY"

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeHostInsightResourceUtilizationInsightAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :type time_interval_end: datetime

        :param resource_metric:
            The value to assign to the resource_metric property of this SummarizeHostInsightResourceUtilizationInsightAggregation.
            Allowed values for this property are: "CPU", "MEMORY", "LOGICAL_MEMORY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_metric: str

        :param projected_utilization:
            The value to assign to the projected_utilization property of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :type projected_utilization: oci.opsi.models.ResourceInsightProjectedUtilization

        :param current_utilization:
            The value to assign to the current_utilization property of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :type current_utilization: oci.opsi.models.ResourceInsightCurrentUtilization

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'resource_metric': 'str',
            'projected_utilization': 'ResourceInsightProjectedUtilization',
            'current_utilization': 'ResourceInsightCurrentUtilization'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'resource_metric': 'resourceMetric',
            'projected_utilization': 'projectedUtilization',
            'current_utilization': 'currentUtilization'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._resource_metric = None
        self._projected_utilization = None
        self._current_utilization = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def resource_metric(self):
        """
        **[Required]** Gets the resource_metric of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        Defines the type of resource metric (CPU, Physical Memory, Logical Memory)

        Allowed values for this property are: "CPU", "MEMORY", "LOGICAL_MEMORY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_metric of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :rtype: str
        """
        return self._resource_metric

    @resource_metric.setter
    def resource_metric(self, resource_metric):
        """
        Sets the resource_metric of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        Defines the type of resource metric (CPU, Physical Memory, Logical Memory)


        :param resource_metric: The resource_metric of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :type: str
        """
        allowed_values = ["CPU", "MEMORY", "LOGICAL_MEMORY"]
        if not value_allowed_none_or_none_sentinel(resource_metric, allowed_values):
            resource_metric = 'UNKNOWN_ENUM_VALUE'
        self._resource_metric = resource_metric

    @property
    def projected_utilization(self):
        """
        **[Required]** Gets the projected_utilization of this SummarizeHostInsightResourceUtilizationInsightAggregation.

        :return: The projected_utilization of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :rtype: oci.opsi.models.ResourceInsightProjectedUtilization
        """
        return self._projected_utilization

    @projected_utilization.setter
    def projected_utilization(self, projected_utilization):
        """
        Sets the projected_utilization of this SummarizeHostInsightResourceUtilizationInsightAggregation.

        :param projected_utilization: The projected_utilization of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :type: oci.opsi.models.ResourceInsightProjectedUtilization
        """
        self._projected_utilization = projected_utilization

    @property
    def current_utilization(self):
        """
        **[Required]** Gets the current_utilization of this SummarizeHostInsightResourceUtilizationInsightAggregation.

        :return: The current_utilization of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :rtype: oci.opsi.models.ResourceInsightCurrentUtilization
        """
        return self._current_utilization

    @current_utilization.setter
    def current_utilization(self, current_utilization):
        """
        Sets the current_utilization of this SummarizeHostInsightResourceUtilizationInsightAggregation.

        :param current_utilization: The current_utilization of this SummarizeHostInsightResourceUtilizationInsightAggregation.
        :type: oci.opsi.models.ResourceInsightCurrentUtilization
        """
        self._current_utilization = current_utilization

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
