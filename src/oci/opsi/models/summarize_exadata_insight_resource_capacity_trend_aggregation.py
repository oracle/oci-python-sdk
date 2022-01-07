# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeExadataInsightResourceCapacityTrendAggregation(object):
    """
    Collection of resource capacity trend.
    """

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "CPU"
    EXADATA_RESOURCE_METRIC_CPU = "CPU"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "STORAGE"
    EXADATA_RESOURCE_METRIC_STORAGE = "STORAGE"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "IO"
    EXADATA_RESOURCE_METRIC_IO = "IO"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "MEMORY"
    EXADATA_RESOURCE_METRIC_MEMORY = "MEMORY"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "IOPS"
    EXADATA_RESOURCE_METRIC_IOPS = "IOPS"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "THROUGHPUT"
    EXADATA_RESOURCE_METRIC_THROUGHPUT = "THROUGHPUT"

    #: A constant which can be used with the exadata_resource_type property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "DATABASE"
    EXADATA_RESOURCE_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the exadata_resource_type property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "HOST"
    EXADATA_RESOURCE_TYPE_HOST = "HOST"

    #: A constant which can be used with the exadata_resource_type property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "STORAGE_SERVER"
    EXADATA_RESOURCE_TYPE_STORAGE_SERVER = "STORAGE_SERVER"

    #: A constant which can be used with the exadata_resource_type property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "DISKGROUP"
    EXADATA_RESOURCE_TYPE_DISKGROUP = "DISKGROUP"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "CORES"
    USAGE_UNIT_CORES = "CORES"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "GB"
    USAGE_UNIT_GB = "GB"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "MBPS"
    USAGE_UNIT_MBPS = "MBPS"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "IOPS"
    USAGE_UNIT_IOPS = "IOPS"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceCapacityTrendAggregation.
    #: This constant has a value of "PERCENT"
    USAGE_UNIT_PERCENT = "PERCENT"

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeExadataInsightResourceCapacityTrendAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type time_interval_end: datetime

        :param exadata_resource_metric:
            The value to assign to the exadata_resource_metric property of this SummarizeExadataInsightResourceCapacityTrendAggregation.
            Allowed values for this property are: "CPU", "STORAGE", "IO", "MEMORY", "IOPS", "THROUGHPUT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_resource_metric: str

        :param exadata_resource_type:
            The value to assign to the exadata_resource_type property of this SummarizeExadataInsightResourceCapacityTrendAggregation.
            Allowed values for this property are: "DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_resource_type: str

        :param usage_unit:
            The value to assign to the usage_unit property of this SummarizeExadataInsightResourceCapacityTrendAggregation.
            Allowed values for this property are: "CORES", "GB", "MBPS", "IOPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type usage_unit: str

        :param item_duration_in_ms:
            The value to assign to the item_duration_in_ms property of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type item_duration_in_ms: int

        :param capacity_data:
            The value to assign to the capacity_data property of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type capacity_data: list[oci.opsi.models.ExadataInsightResourceCapacityTrendAggregation]

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'exadata_resource_metric': 'str',
            'exadata_resource_type': 'str',
            'usage_unit': 'str',
            'item_duration_in_ms': 'int',
            'capacity_data': 'list[ExadataInsightResourceCapacityTrendAggregation]'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'exadata_resource_metric': 'exadataResourceMetric',
            'exadata_resource_type': 'exadataResourceType',
            'usage_unit': 'usageUnit',
            'item_duration_in_ms': 'itemDurationInMs',
            'capacity_data': 'capacityData'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._exadata_resource_metric = None
        self._exadata_resource_type = None
        self._usage_unit = None
        self._item_duration_in_ms = None
        self._capacity_data = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def exadata_resource_metric(self):
        """
        **[Required]** Gets the exadata_resource_metric of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Defines the type of exadata resource metric (example: CPU, STORAGE)

        Allowed values for this property are: "CPU", "STORAGE", "IO", "MEMORY", "IOPS", "THROUGHPUT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_resource_metric of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :rtype: str
        """
        return self._exadata_resource_metric

    @exadata_resource_metric.setter
    def exadata_resource_metric(self, exadata_resource_metric):
        """
        Sets the exadata_resource_metric of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Defines the type of exadata resource metric (example: CPU, STORAGE)


        :param exadata_resource_metric: The exadata_resource_metric of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type: str
        """
        allowed_values = ["CPU", "STORAGE", "IO", "MEMORY", "IOPS", "THROUGHPUT"]
        if not value_allowed_none_or_none_sentinel(exadata_resource_metric, allowed_values):
            exadata_resource_metric = 'UNKNOWN_ENUM_VALUE'
        self._exadata_resource_metric = exadata_resource_metric

    @property
    def exadata_resource_type(self):
        """
        **[Required]** Gets the exadata_resource_type of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Defines the resource type for an exadata  (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

        Allowed values for this property are: "DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_resource_type of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :rtype: str
        """
        return self._exadata_resource_type

    @exadata_resource_type.setter
    def exadata_resource_type(self, exadata_resource_type):
        """
        Sets the exadata_resource_type of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Defines the resource type for an exadata  (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)


        :param exadata_resource_type: The exadata_resource_type of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type: str
        """
        allowed_values = ["DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP"]
        if not value_allowed_none_or_none_sentinel(exadata_resource_type, allowed_values):
            exadata_resource_type = 'UNKNOWN_ENUM_VALUE'
        self._exadata_resource_type = exadata_resource_type

    @property
    def usage_unit(self):
        """
        **[Required]** Gets the usage_unit of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Identifies the units of the current resource metric (CORES, GB).

        Allowed values for this property are: "CORES", "GB", "MBPS", "IOPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The usage_unit of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :rtype: str
        """
        return self._usage_unit

    @usage_unit.setter
    def usage_unit(self, usage_unit):
        """
        Sets the usage_unit of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Identifies the units of the current resource metric (CORES, GB).


        :param usage_unit: The usage_unit of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type: str
        """
        allowed_values = ["CORES", "GB", "MBPS", "IOPS", "PERCENT"]
        if not value_allowed_none_or_none_sentinel(usage_unit, allowed_values):
            usage_unit = 'UNKNOWN_ENUM_VALUE'
        self._usage_unit = usage_unit

    @property
    def item_duration_in_ms(self):
        """
        **[Required]** Gets the item_duration_in_ms of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Time duration in milliseconds between data points (one hour or one day).


        :return: The item_duration_in_ms of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :rtype: int
        """
        return self._item_duration_in_ms

    @item_duration_in_ms.setter
    def item_duration_in_ms(self, item_duration_in_ms):
        """
        Sets the item_duration_in_ms of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Time duration in milliseconds between data points (one hour or one day).


        :param item_duration_in_ms: The item_duration_in_ms of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type: int
        """
        self._item_duration_in_ms = item_duration_in_ms

    @property
    def capacity_data(self):
        """
        **[Required]** Gets the capacity_data of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Capacity Data with time interval


        :return: The capacity_data of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :rtype: list[oci.opsi.models.ExadataInsightResourceCapacityTrendAggregation]
        """
        return self._capacity_data

    @capacity_data.setter
    def capacity_data(self, capacity_data):
        """
        Sets the capacity_data of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        Capacity Data with time interval


        :param capacity_data: The capacity_data of this SummarizeExadataInsightResourceCapacityTrendAggregation.
        :type: list[oci.opsi.models.ExadataInsightResourceCapacityTrendAggregation]
        """
        self._capacity_data = capacity_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
