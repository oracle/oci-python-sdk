# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_column import AbstractColumn
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrendColumn(AbstractColumn):
    """
    Result column, that contains time series data points in each row. The column includes the time stamps as additional field in column header.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TrendColumn object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.TrendColumn.type` attribute
        of this class is ``TREND_COLUMN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TrendColumn.
            Allowed values for this property are: "COLUMN", "CHART_COLUMN", "CHART_DATA_COLUMN", "TIME_COLUMN", "TREND_COLUMN", "CLASSIFY_COLUMN"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this TrendColumn.
        :type display_name: str

        :param sub_system:
            The value to assign to the sub_system property of this TrendColumn.
            Allowed values for this property are: "LOG"
        :type sub_system: str

        :param values:
            The value to assign to the values property of this TrendColumn.
        :type values: list[oci.log_analytics.models.FieldValue]

        :param is_list_of_values:
            The value to assign to the is_list_of_values property of this TrendColumn.
        :type is_list_of_values: bool

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this TrendColumn.
        :type is_multi_valued: bool

        :param is_groupable:
            The value to assign to the is_groupable property of this TrendColumn.
        :type is_groupable: bool

        :param is_evaluable:
            The value to assign to the is_evaluable property of this TrendColumn.
        :type is_evaluable: bool

        :param value_type:
            The value to assign to the value_type property of this TrendColumn.
            Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"
        :type value_type: str

        :param original_display_name:
            The value to assign to the original_display_name property of this TrendColumn.
        :type original_display_name: str

        :param internal_name:
            The value to assign to the internal_name property of this TrendColumn.
        :type internal_name: str

        :param interval_gap:
            The value to assign to the interval_gap property of this TrendColumn.
        :type interval_gap: str

        :param intervals:
            The value to assign to the intervals property of this TrendColumn.
        :type intervals: list[int]

        :param total_interval_counts:
            The value to assign to the total_interval_counts property of this TrendColumn.
        :type total_interval_counts: list[int]

        :param total_interval_counts_after_filter:
            The value to assign to the total_interval_counts_after_filter property of this TrendColumn.
        :type total_interval_counts_after_filter: list[int]

        :param interval_group_counts:
            The value to assign to the interval_group_counts property of this TrendColumn.
        :type interval_group_counts: list[int]

        :param interval_group_counts_after_filter:
            The value to assign to the interval_group_counts_after_filter property of this TrendColumn.
        :type interval_group_counts_after_filter: list[int]

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'sub_system': 'str',
            'values': 'list[FieldValue]',
            'is_list_of_values': 'bool',
            'is_multi_valued': 'bool',
            'is_groupable': 'bool',
            'is_evaluable': 'bool',
            'value_type': 'str',
            'original_display_name': 'str',
            'internal_name': 'str',
            'interval_gap': 'str',
            'intervals': 'list[int]',
            'total_interval_counts': 'list[int]',
            'total_interval_counts_after_filter': 'list[int]',
            'interval_group_counts': 'list[int]',
            'interval_group_counts_after_filter': 'list[int]'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'sub_system': 'subSystem',
            'values': 'values',
            'is_list_of_values': 'isListOfValues',
            'is_multi_valued': 'isMultiValued',
            'is_groupable': 'isGroupable',
            'is_evaluable': 'isEvaluable',
            'value_type': 'valueType',
            'original_display_name': 'originalDisplayName',
            'internal_name': 'internalName',
            'interval_gap': 'intervalGap',
            'intervals': 'intervals',
            'total_interval_counts': 'totalIntervalCounts',
            'total_interval_counts_after_filter': 'totalIntervalCountsAfterFilter',
            'interval_group_counts': 'intervalGroupCounts',
            'interval_group_counts_after_filter': 'intervalGroupCountsAfterFilter'
        }

        self._type = None
        self._display_name = None
        self._sub_system = None
        self._values = None
        self._is_list_of_values = None
        self._is_multi_valued = None
        self._is_groupable = None
        self._is_evaluable = None
        self._value_type = None
        self._original_display_name = None
        self._internal_name = None
        self._interval_gap = None
        self._intervals = None
        self._total_interval_counts = None
        self._total_interval_counts_after_filter = None
        self._interval_group_counts = None
        self._interval_group_counts_after_filter = None
        self._type = 'TREND_COLUMN'

    @property
    def interval_gap(self):
        """
        Gets the interval_gap of this TrendColumn.
        Time gap between each data pont in the series.


        :return: The interval_gap of this TrendColumn.
        :rtype: str
        """
        return self._interval_gap

    @interval_gap.setter
    def interval_gap(self, interval_gap):
        """
        Sets the interval_gap of this TrendColumn.
        Time gap between each data pont in the series.


        :param interval_gap: The interval_gap of this TrendColumn.
        :type: str
        """
        self._interval_gap = interval_gap

    @property
    def intervals(self):
        """
        Gets the intervals of this TrendColumn.
        Timestamps for each series data point


        :return: The intervals of this TrendColumn.
        :rtype: list[int]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """
        Sets the intervals of this TrendColumn.
        Timestamps for each series data point


        :param intervals: The intervals of this TrendColumn.
        :type: list[int]
        """
        self._intervals = intervals

    @property
    def total_interval_counts(self):
        """
        Gets the total_interval_counts of this TrendColumn.
        Sum across all column values for a given timestamp.


        :return: The total_interval_counts of this TrendColumn.
        :rtype: list[int]
        """
        return self._total_interval_counts

    @total_interval_counts.setter
    def total_interval_counts(self, total_interval_counts):
        """
        Sets the total_interval_counts of this TrendColumn.
        Sum across all column values for a given timestamp.


        :param total_interval_counts: The total_interval_counts of this TrendColumn.
        :type: list[int]
        """
        self._total_interval_counts = total_interval_counts

    @property
    def total_interval_counts_after_filter(self):
        """
        Gets the total_interval_counts_after_filter of this TrendColumn.

        :return: The total_interval_counts_after_filter of this TrendColumn.
        :rtype: list[int]
        """
        return self._total_interval_counts_after_filter

    @total_interval_counts_after_filter.setter
    def total_interval_counts_after_filter(self, total_interval_counts_after_filter):
        """
        Sets the total_interval_counts_after_filter of this TrendColumn.

        :param total_interval_counts_after_filter: The total_interval_counts_after_filter of this TrendColumn.
        :type: list[int]
        """
        self._total_interval_counts_after_filter = total_interval_counts_after_filter

    @property
    def interval_group_counts(self):
        """
        Gets the interval_group_counts of this TrendColumn.

        :return: The interval_group_counts of this TrendColumn.
        :rtype: list[int]
        """
        return self._interval_group_counts

    @interval_group_counts.setter
    def interval_group_counts(self, interval_group_counts):
        """
        Sets the interval_group_counts of this TrendColumn.

        :param interval_group_counts: The interval_group_counts of this TrendColumn.
        :type: list[int]
        """
        self._interval_group_counts = interval_group_counts

    @property
    def interval_group_counts_after_filter(self):
        """
        Gets the interval_group_counts_after_filter of this TrendColumn.

        :return: The interval_group_counts_after_filter of this TrendColumn.
        :rtype: list[int]
        """
        return self._interval_group_counts_after_filter

    @interval_group_counts_after_filter.setter
    def interval_group_counts_after_filter(self, interval_group_counts_after_filter):
        """
        Sets the interval_group_counts_after_filter of this TrendColumn.

        :param interval_group_counts_after_filter: The interval_group_counts_after_filter of this TrendColumn.
        :type: list[int]
        """
        self._interval_group_counts_after_filter = interval_group_counts_after_filter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
