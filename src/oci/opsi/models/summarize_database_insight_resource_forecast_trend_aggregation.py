# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeDatabaseInsightResourceForecastTrendAggregation(object):
    """
    Forecast results from the selected time period.
    """

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "CPU"
    RESOURCE_METRIC_CPU = "CPU"

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "STORAGE"
    RESOURCE_METRIC_STORAGE = "STORAGE"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "CORES"
    USAGE_UNIT_CORES = "CORES"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "GB"
    USAGE_UNIT_GB = "GB"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "MBPS"
    USAGE_UNIT_MBPS = "MBPS"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "PERCENT"
    USAGE_UNIT_PERCENT = "PERCENT"

    #: A constant which can be used with the pattern property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "LINEAR"
    PATTERN_LINEAR = "LINEAR"

    #: A constant which can be used with the pattern property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "MONTHLY_SEASONS"
    PATTERN_MONTHLY_SEASONS = "MONTHLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "MONTHLY_AND_YEARLY_SEASONS"
    PATTERN_MONTHLY_AND_YEARLY_SEASONS = "MONTHLY_AND_YEARLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "WEEKLY_SEASONS"
    PATTERN_WEEKLY_SEASONS = "WEEKLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "WEEKLY_AND_MONTHLY_SEASONS"
    PATTERN_WEEKLY_AND_MONTHLY_SEASONS = "WEEKLY_AND_MONTHLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "WEEKLY_MONTHLY_AND_YEARLY_SEASONS"
    PATTERN_WEEKLY_MONTHLY_AND_YEARLY_SEASONS = "WEEKLY_MONTHLY_AND_YEARLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "WEEKLY_AND_YEARLY_SEASONS"
    PATTERN_WEEKLY_AND_YEARLY_SEASONS = "WEEKLY_AND_YEARLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeDatabaseInsightResourceForecastTrendAggregation.
    #: This constant has a value of "YEARLY_SEASONS"
    PATTERN_YEARLY_SEASONS = "YEARLY_SEASONS"

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeDatabaseInsightResourceForecastTrendAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type time_interval_end: datetime

        :param resource_metric:
            The value to assign to the resource_metric property of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
            Allowed values for this property are: "CPU", "STORAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_metric: str

        :param usage_unit:
            The value to assign to the usage_unit property of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
            Allowed values for this property are: "CORES", "GB", "MBPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type usage_unit: str

        :param pattern:
            The value to assign to the pattern property of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
            Allowed values for this property are: "LINEAR", "MONTHLY_SEASONS", "MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_SEASONS", "WEEKLY_AND_MONTHLY_SEASONS", "WEEKLY_MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_AND_YEARLY_SEASONS", "YEARLY_SEASONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type pattern: str

        :param historical_data:
            The value to assign to the historical_data property of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type historical_data: list[HistoricalDataItem]

        :param projected_data:
            The value to assign to the projected_data property of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type projected_data: list[ProjectedDataItem]

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'resource_metric': 'str',
            'usage_unit': 'str',
            'pattern': 'str',
            'historical_data': 'list[HistoricalDataItem]',
            'projected_data': 'list[ProjectedDataItem]'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'resource_metric': 'resourceMetric',
            'usage_unit': 'usageUnit',
            'pattern': 'pattern',
            'historical_data': 'historicalData',
            'projected_data': 'projectedData'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._resource_metric = None
        self._usage_unit = None
        self._pattern = None
        self._historical_data = None
        self._projected_data = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def resource_metric(self):
        """
        **[Required]** Gets the resource_metric of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Defines the type of resource metric (CPU, STORAGE)

        Allowed values for this property are: "CPU", "STORAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_metric of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :rtype: str
        """
        return self._resource_metric

    @resource_metric.setter
    def resource_metric(self, resource_metric):
        """
        Sets the resource_metric of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Defines the type of resource metric (CPU, STORAGE)


        :param resource_metric: The resource_metric of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type: str
        """
        allowed_values = ["CPU", "STORAGE"]
        if not value_allowed_none_or_none_sentinel(resource_metric, allowed_values):
            resource_metric = 'UNKNOWN_ENUM_VALUE'
        self._resource_metric = resource_metric

    @property
    def usage_unit(self):
        """
        **[Required]** Gets the usage_unit of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Displays usage unit ( CORES, GB)

        Allowed values for this property are: "CORES", "GB", "MBPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The usage_unit of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :rtype: str
        """
        return self._usage_unit

    @usage_unit.setter
    def usage_unit(self, usage_unit):
        """
        Sets the usage_unit of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Displays usage unit ( CORES, GB)


        :param usage_unit: The usage_unit of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type: str
        """
        allowed_values = ["CORES", "GB", "MBPS", "PERCENT"]
        if not value_allowed_none_or_none_sentinel(usage_unit, allowed_values):
            usage_unit = 'UNKNOWN_ENUM_VALUE'
        self._usage_unit = usage_unit

    @property
    def pattern(self):
        """
        **[Required]** Gets the pattern of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Time series patterns used in the forecasting.

        Allowed values for this property are: "LINEAR", "MONTHLY_SEASONS", "MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_SEASONS", "WEEKLY_AND_MONTHLY_SEASONS", "WEEKLY_MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_AND_YEARLY_SEASONS", "YEARLY_SEASONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The pattern of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Time series patterns used in the forecasting.


        :param pattern: The pattern of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type: str
        """
        allowed_values = ["LINEAR", "MONTHLY_SEASONS", "MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_SEASONS", "WEEKLY_AND_MONTHLY_SEASONS", "WEEKLY_MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_AND_YEARLY_SEASONS", "YEARLY_SEASONS"]
        if not value_allowed_none_or_none_sentinel(pattern, allowed_values):
            pattern = 'UNKNOWN_ENUM_VALUE'
        self._pattern = pattern

    @property
    def historical_data(self):
        """
        **[Required]** Gets the historical_data of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Time series data used for the forecast analysis.


        :return: The historical_data of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :rtype: list[HistoricalDataItem]
        """
        return self._historical_data

    @historical_data.setter
    def historical_data(self, historical_data):
        """
        Sets the historical_data of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Time series data used for the forecast analysis.


        :param historical_data: The historical_data of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type: list[HistoricalDataItem]
        """
        self._historical_data = historical_data

    @property
    def projected_data(self):
        """
        **[Required]** Gets the projected_data of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Time series data result of the forecasting analysis.


        :return: The projected_data of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :rtype: list[ProjectedDataItem]
        """
        return self._projected_data

    @projected_data.setter
    def projected_data(self, projected_data):
        """
        Sets the projected_data of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        Time series data result of the forecasting analysis.


        :param projected_data: The projected_data of this SummarizeDatabaseInsightResourceForecastTrendAggregation.
        :type: list[ProjectedDataItem]
        """
        self._projected_data = projected_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
