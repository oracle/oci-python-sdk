# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection(object):
    """
    Top level response object.
    """

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
    #: This constant has a value of "CORES"
    USAGE_UNIT_CORES = "CORES"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
    #: This constant has a value of "GB"
    USAGE_UNIT_GB = "GB"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
    #: This constant has a value of "MBPS"
    USAGE_UNIT_MBPS = "MBPS"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
    #: This constant has a value of "IOPS"
    USAGE_UNIT_IOPS = "IOPS"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
    #: This constant has a value of "PERCENT"
    USAGE_UNIT_PERCENT = "PERCENT"

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :type time_interval_end: datetime

        :param usage_unit:
            The value to assign to the usage_unit property of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
            Allowed values for this property are: "CORES", "GB", "MBPS", "IOPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type usage_unit: str

        :param item_duration_in_ms:
            The value to assign to the item_duration_in_ms property of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :type item_duration_in_ms: int

        :param items:
            The value to assign to the items property of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :type items: list[oci.opsi.models.TablespaceUsageTrendAggregation]

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'usage_unit': 'str',
            'item_duration_in_ms': 'int',
            'items': 'list[TablespaceUsageTrendAggregation]'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'usage_unit': 'usageUnit',
            'item_duration_in_ms': 'itemDurationInMs',
            'items': 'items'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._usage_unit = None
        self._item_duration_in_ms = None
        self._items = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def usage_unit(self):
        """
        **[Required]** Gets the usage_unit of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        Displays usage unit ( CORES, GB , PERCENT, MBPS)

        Allowed values for this property are: "CORES", "GB", "MBPS", "IOPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The usage_unit of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :rtype: str
        """
        return self._usage_unit

    @usage_unit.setter
    def usage_unit(self, usage_unit):
        """
        Sets the usage_unit of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        Displays usage unit ( CORES, GB , PERCENT, MBPS)


        :param usage_unit: The usage_unit of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :type: str
        """
        allowed_values = ["CORES", "GB", "MBPS", "IOPS", "PERCENT"]
        if not value_allowed_none_or_none_sentinel(usage_unit, allowed_values):
            usage_unit = 'UNKNOWN_ENUM_VALUE'
        self._usage_unit = usage_unit

    @property
    def item_duration_in_ms(self):
        """
        **[Required]** Gets the item_duration_in_ms of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        Time duration in milliseconds between data points (one hour or one day).


        :return: The item_duration_in_ms of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :rtype: int
        """
        return self._item_duration_in_ms

    @item_duration_in_ms.setter
    def item_duration_in_ms(self, item_duration_in_ms):
        """
        Sets the item_duration_in_ms of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        Time duration in milliseconds between data points (one hour or one day).


        :param item_duration_in_ms: The item_duration_in_ms of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :type: int
        """
        self._item_duration_in_ms = item_duration_in_ms

    @property
    def items(self):
        """
        **[Required]** Gets the items of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        Collection of Usage Data with time stamps for top five tablespace


        :return: The items of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :rtype: list[oci.opsi.models.TablespaceUsageTrendAggregation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        Collection of Usage Data with time stamps for top five tablespace


        :param items: The items of this SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection.
        :type: list[oci.opsi.models.TablespaceUsageTrendAggregation]
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
