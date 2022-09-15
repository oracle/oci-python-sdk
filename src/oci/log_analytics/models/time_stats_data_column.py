# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_column import AbstractColumn
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TimeStatsDataColumn(AbstractColumn):
    """
    A data series specific to a particular TIMESTATS output field.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TimeStatsDataColumn object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.TimeStatsDataColumn.type` attribute
        of this class is ``TIME_STATS_DATA_COLUMN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TimeStatsDataColumn.
            Allowed values for this property are: "COLUMN", "CHART_COLUMN", "CHART_DATA_COLUMN", "TIME_STATS_COLUMN", "TIME_STATS_DATA_COLUMN", "TIME_CLUSTER_COLUMN", "TIME_CLUSTER_DATA_COLUMN", "TIME_COLUMN", "TREND_COLUMN", "CLASSIFY_COLUMN"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this TimeStatsDataColumn.
        :type display_name: str

        :param sub_system:
            The value to assign to the sub_system property of this TimeStatsDataColumn.
            Allowed values for this property are: "LOG"
        :type sub_system: str

        :param values:
            The value to assign to the values property of this TimeStatsDataColumn.
        :type values: list[oci.log_analytics.models.FieldValue]

        :param is_list_of_values:
            The value to assign to the is_list_of_values property of this TimeStatsDataColumn.
        :type is_list_of_values: bool

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this TimeStatsDataColumn.
        :type is_multi_valued: bool

        :param is_case_sensitive:
            The value to assign to the is_case_sensitive property of this TimeStatsDataColumn.
        :type is_case_sensitive: bool

        :param is_groupable:
            The value to assign to the is_groupable property of this TimeStatsDataColumn.
        :type is_groupable: bool

        :param is_evaluable:
            The value to assign to the is_evaluable property of this TimeStatsDataColumn.
        :type is_evaluable: bool

        :param value_type:
            The value to assign to the value_type property of this TimeStatsDataColumn.
            Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"
        :type value_type: str

        :param original_display_name:
            The value to assign to the original_display_name property of this TimeStatsDataColumn.
        :type original_display_name: str

        :param internal_name:
            The value to assign to the internal_name property of this TimeStatsDataColumn.
        :type internal_name: str

        :param columns:
            The value to assign to the columns property of this TimeStatsDataColumn.
        :type columns: list[oci.log_analytics.models.AbstractColumn]

        :param result:
            The value to assign to the result property of this TimeStatsDataColumn.
        :type result: list[dict(str, object)]

        :param result_count:
            The value to assign to the result_count property of this TimeStatsDataColumn.
        :type result_count: int

        :param total_count:
            The value to assign to the total_count property of this TimeStatsDataColumn.
        :type total_count: int

        :param partial_results:
            The value to assign to the partial_results property of this TimeStatsDataColumn.
        :type partial_results: bool

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'sub_system': 'str',
            'values': 'list[FieldValue]',
            'is_list_of_values': 'bool',
            'is_multi_valued': 'bool',
            'is_case_sensitive': 'bool',
            'is_groupable': 'bool',
            'is_evaluable': 'bool',
            'value_type': 'str',
            'original_display_name': 'str',
            'internal_name': 'str',
            'columns': 'list[AbstractColumn]',
            'result': 'list[dict(str, object)]',
            'result_count': 'int',
            'total_count': 'int',
            'partial_results': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'sub_system': 'subSystem',
            'values': 'values',
            'is_list_of_values': 'isListOfValues',
            'is_multi_valued': 'isMultiValued',
            'is_case_sensitive': 'isCaseSensitive',
            'is_groupable': 'isGroupable',
            'is_evaluable': 'isEvaluable',
            'value_type': 'valueType',
            'original_display_name': 'originalDisplayName',
            'internal_name': 'internalName',
            'columns': 'columns',
            'result': 'result',
            'result_count': 'resultCount',
            'total_count': 'totalCount',
            'partial_results': 'partialResults'
        }

        self._type = None
        self._display_name = None
        self._sub_system = None
        self._values = None
        self._is_list_of_values = None
        self._is_multi_valued = None
        self._is_case_sensitive = None
        self._is_groupable = None
        self._is_evaluable = None
        self._value_type = None
        self._original_display_name = None
        self._internal_name = None
        self._columns = None
        self._result = None
        self._result_count = None
        self._total_count = None
        self._partial_results = None
        self._type = 'TIME_STATS_DATA_COLUMN'

    @property
    def columns(self):
        """
        Gets the columns of this TimeStatsDataColumn.
        Column descriptors for the TIMESTATS result.


        :return: The columns of this TimeStatsDataColumn.
        :rtype: list[oci.log_analytics.models.AbstractColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this TimeStatsDataColumn.
        Column descriptors for the TIMESTATS result.


        :param columns: The columns of this TimeStatsDataColumn.
        :type: list[oci.log_analytics.models.AbstractColumn]
        """
        self._columns = columns

    @property
    def result(self):
        """
        Gets the result of this TimeStatsDataColumn.
        Results of the TIMESTATS command.


        :return: The result of this TimeStatsDataColumn.
        :rtype: list[dict(str, object)]
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this TimeStatsDataColumn.
        Results of the TIMESTATS command.


        :param result: The result of this TimeStatsDataColumn.
        :type: list[dict(str, object)]
        """
        self._result = result

    @property
    def result_count(self):
        """
        Gets the result_count of this TimeStatsDataColumn.
        Number of timeseries returned by the query.


        :return: The result_count of this TimeStatsDataColumn.
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """
        Sets the result_count of this TimeStatsDataColumn.
        Number of timeseries returned by the query.


        :param result_count: The result_count of this TimeStatsDataColumn.
        :type: int
        """
        self._result_count = result_count

    @property
    def total_count(self):
        """
        Gets the total_count of this TimeStatsDataColumn.
        Number of timeseries retrieved by the query.


        :return: The total_count of this TimeStatsDataColumn.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this TimeStatsDataColumn.
        Number of timeseries retrieved by the query.


        :param total_count: The total_count of this TimeStatsDataColumn.
        :type: int
        """
        self._total_count = total_count

    @property
    def partial_results(self):
        """
        Gets the partial_results of this TimeStatsDataColumn.
        True if query did not complete processing all data.


        :return: The partial_results of this TimeStatsDataColumn.
        :rtype: bool
        """
        return self._partial_results

    @partial_results.setter
    def partial_results(self, partial_results):
        """
        Sets the partial_results of this TimeStatsDataColumn.
        True if query did not complete processing all data.


        :param partial_results: The partial_results of this TimeStatsDataColumn.
        :type: bool
        """
        self._partial_results = partial_results

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
