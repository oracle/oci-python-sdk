# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeDatabaseInsightResourceStatisticsAggregationCollection(object):
    """
    Returns list of the Databases with resource statistics like usage,capacity,utilization and usage change percent.
    """

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "CPU"
    RESOURCE_METRIC_CPU = "CPU"

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "STORAGE"
    RESOURCE_METRIC_STORAGE = "STORAGE"

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "IO"
    RESOURCE_METRIC_IO = "IO"

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "MEMORY"
    RESOURCE_METRIC_MEMORY = "MEMORY"

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "MEMORY_PGA"
    RESOURCE_METRIC_MEMORY_PGA = "MEMORY_PGA"

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "MEMORY_SGA"
    RESOURCE_METRIC_MEMORY_SGA = "MEMORY_SGA"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "CORES"
    USAGE_UNIT_CORES = "CORES"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "GB"
    USAGE_UNIT_GB = "GB"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "MBPS"
    USAGE_UNIT_MBPS = "MBPS"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
    #: This constant has a value of "PERCENT"
    USAGE_UNIT_PERCENT = "PERCENT"

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeDatabaseInsightResourceStatisticsAggregationCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :type time_interval_end: datetime

        :param resource_metric:
            The value to assign to the resource_metric property of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
            Allowed values for this property are: "CPU", "STORAGE", "IO", "MEMORY", "MEMORY_PGA", "MEMORY_SGA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_metric: str

        :param usage_unit:
            The value to assign to the usage_unit property of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
            Allowed values for this property are: "CORES", "GB", "MBPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type usage_unit: str

        :param items:
            The value to assign to the items property of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :type items: list[oci.opsi.models.ResourceStatisticsAggregation]

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'resource_metric': 'str',
            'usage_unit': 'str',
            'items': 'list[ResourceStatisticsAggregation]'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'resource_metric': 'resourceMetric',
            'usage_unit': 'usageUnit',
            'items': 'items'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._resource_metric = None
        self._usage_unit = None
        self._items = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def resource_metric(self):
        """
        **[Required]** Gets the resource_metric of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        Defines the type of resource metric (example: CPU, STORAGE)

        Allowed values for this property are: "CPU", "STORAGE", "IO", "MEMORY", "MEMORY_PGA", "MEMORY_SGA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_metric of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :rtype: str
        """
        return self._resource_metric

    @resource_metric.setter
    def resource_metric(self, resource_metric):
        """
        Sets the resource_metric of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        Defines the type of resource metric (example: CPU, STORAGE)


        :param resource_metric: The resource_metric of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :type: str
        """
        allowed_values = ["CPU", "STORAGE", "IO", "MEMORY", "MEMORY_PGA", "MEMORY_SGA"]
        if not value_allowed_none_or_none_sentinel(resource_metric, allowed_values):
            resource_metric = 'UNKNOWN_ENUM_VALUE'
        self._resource_metric = resource_metric

    @property
    def usage_unit(self):
        """
        **[Required]** Gets the usage_unit of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        Displays usage unit ( CORES, GB)

        Allowed values for this property are: "CORES", "GB", "MBPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The usage_unit of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :rtype: str
        """
        return self._usage_unit

    @usage_unit.setter
    def usage_unit(self, usage_unit):
        """
        Sets the usage_unit of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        Displays usage unit ( CORES, GB)


        :param usage_unit: The usage_unit of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :type: str
        """
        allowed_values = ["CORES", "GB", "MBPS", "PERCENT"]
        if not value_allowed_none_or_none_sentinel(usage_unit, allowed_values):
            usage_unit = 'UNKNOWN_ENUM_VALUE'
        self._usage_unit = usage_unit

    @property
    def items(self):
        """
        **[Required]** Gets the items of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        Collection of Resource Statistics items


        :return: The items of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :rtype: list[oci.opsi.models.ResourceStatisticsAggregation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        Collection of Resource Statistics items


        :param items: The items of this SummarizeDatabaseInsightResourceStatisticsAggregationCollection.
        :type: list[oci.opsi.models.ResourceStatisticsAggregation]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
