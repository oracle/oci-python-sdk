# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryAggregation(object):
    """
    Query results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_count:
            The value to assign to the total_count property of this QueryAggregation.
        :type total_count: int

        :param total_matched_count:
            The value to assign to the total_matched_count property of this QueryAggregation.
        :type total_matched_count: int

        :param are_partial_results:
            The value to assign to the are_partial_results property of this QueryAggregation.
        :type are_partial_results: bool

        :param partial_result_reason:
            The value to assign to the partial_result_reason property of this QueryAggregation.
        :type partial_result_reason: str

        :param columns:
            The value to assign to the columns property of this QueryAggregation.
        :type columns: list[oci.log_analytics.models.AbstractColumn]

        :param fields:
            The value to assign to the fields property of this QueryAggregation.
        :type fields: list[oci.log_analytics.models.AbstractColumn]

        :param items:
            The value to assign to the items property of this QueryAggregation.
        :type items: list[dict(str, object)]

        :param query_execution_time_in_ms:
            The value to assign to the query_execution_time_in_ms property of this QueryAggregation.
        :type query_execution_time_in_ms: int

        :param percent_complete:
            The value to assign to the percent_complete property of this QueryAggregation.
        :type percent_complete: int

        """
        self.swagger_types = {
            'total_count': 'int',
            'total_matched_count': 'int',
            'are_partial_results': 'bool',
            'partial_result_reason': 'str',
            'columns': 'list[AbstractColumn]',
            'fields': 'list[AbstractColumn]',
            'items': 'list[dict(str, object)]',
            'query_execution_time_in_ms': 'int',
            'percent_complete': 'int'
        }

        self.attribute_map = {
            'total_count': 'totalCount',
            'total_matched_count': 'totalMatchedCount',
            'are_partial_results': 'arePartialResults',
            'partial_result_reason': 'partialResultReason',
            'columns': 'columns',
            'fields': 'fields',
            'items': 'items',
            'query_execution_time_in_ms': 'queryExecutionTimeInMs',
            'percent_complete': 'percentComplete'
        }

        self._total_count = None
        self._total_matched_count = None
        self._are_partial_results = None
        self._partial_result_reason = None
        self._columns = None
        self._fields = None
        self._items = None
        self._query_execution_time_in_ms = None
        self._percent_complete = None

    @property
    def total_count(self):
        """
        Gets the total_count of this QueryAggregation.
        Number of rows query retrieved. Up to maxTotalCount limit.


        :return: The total_count of this QueryAggregation.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this QueryAggregation.
        Number of rows query retrieved. Up to maxTotalCount limit.


        :param total_count: The total_count of this QueryAggregation.
        :type: int
        """
        self._total_count = total_count

    @property
    def total_matched_count(self):
        """
        Gets the total_matched_count of this QueryAggregation.
        Number of rows matched by query.


        :return: The total_matched_count of this QueryAggregation.
        :rtype: int
        """
        return self._total_matched_count

    @total_matched_count.setter
    def total_matched_count(self, total_matched_count):
        """
        Sets the total_matched_count of this QueryAggregation.
        Number of rows matched by query.


        :param total_matched_count: The total_matched_count of this QueryAggregation.
        :type: int
        """
        self._total_matched_count = total_matched_count

    @property
    def are_partial_results(self):
        """
        Gets the are_partial_results of this QueryAggregation.
        True if query did not complete processing all data.


        :return: The are_partial_results of this QueryAggregation.
        :rtype: bool
        """
        return self._are_partial_results

    @are_partial_results.setter
    def are_partial_results(self, are_partial_results):
        """
        Sets the are_partial_results of this QueryAggregation.
        True if query did not complete processing all data.


        :param are_partial_results: The are_partial_results of this QueryAggregation.
        :type: bool
        """
        self._are_partial_results = are_partial_results

    @property
    def partial_result_reason(self):
        """
        Gets the partial_result_reason of this QueryAggregation.
        Explanation of why results may be partial. Only set if arePartialResults is true.


        :return: The partial_result_reason of this QueryAggregation.
        :rtype: str
        """
        return self._partial_result_reason

    @partial_result_reason.setter
    def partial_result_reason(self, partial_result_reason):
        """
        Sets the partial_result_reason of this QueryAggregation.
        Explanation of why results may be partial. Only set if arePartialResults is true.


        :param partial_result_reason: The partial_result_reason of this QueryAggregation.
        :type: str
        """
        self._partial_result_reason = partial_result_reason

    @property
    def columns(self):
        """
        Gets the columns of this QueryAggregation.
        Query result columns


        :return: The columns of this QueryAggregation.
        :rtype: list[oci.log_analytics.models.AbstractColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this QueryAggregation.
        Query result columns


        :param columns: The columns of this QueryAggregation.
        :type: list[oci.log_analytics.models.AbstractColumn]
        """
        self._columns = columns

    @property
    def fields(self):
        """
        Gets the fields of this QueryAggregation.
        Query result fields


        :return: The fields of this QueryAggregation.
        :rtype: list[oci.log_analytics.models.AbstractColumn]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this QueryAggregation.
        Query result fields


        :param fields: The fields of this QueryAggregation.
        :type: list[oci.log_analytics.models.AbstractColumn]
        """
        self._fields = fields

    @property
    def items(self):
        """
        Gets the items of this QueryAggregation.
        Query result data


        :return: The items of this QueryAggregation.
        :rtype: list[dict(str, object)]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this QueryAggregation.
        Query result data


        :param items: The items of this QueryAggregation.
        :type: list[dict(str, object)]
        """
        self._items = items

    @property
    def query_execution_time_in_ms(self):
        """
        Gets the query_execution_time_in_ms of this QueryAggregation.
        Time ellapsed executing query in milli-seconds.


        :return: The query_execution_time_in_ms of this QueryAggregation.
        :rtype: int
        """
        return self._query_execution_time_in_ms

    @query_execution_time_in_ms.setter
    def query_execution_time_in_ms(self, query_execution_time_in_ms):
        """
        Sets the query_execution_time_in_ms of this QueryAggregation.
        Time ellapsed executing query in milli-seconds.


        :param query_execution_time_in_ms: The query_execution_time_in_ms of this QueryAggregation.
        :type: int
        """
        self._query_execution_time_in_ms = query_execution_time_in_ms

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this QueryAggregation.
        Percentage progress completion of the query.


        :return: The percent_complete of this QueryAggregation.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this QueryAggregation.
        Percentage progress completion of the query.


        :param percent_complete: The percent_complete of this QueryAggregation.
        :type: int
        """
        self._percent_complete = percent_complete

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
