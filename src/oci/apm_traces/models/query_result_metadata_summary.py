# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryResultMetadataSummary(object):
    """
    Summary containing the metadata about the query result set.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryResultMetadataSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query_result_row_type_summaries:
            The value to assign to the query_result_row_type_summaries property of this QueryResultMetadataSummary.
        :type query_result_row_type_summaries: list[oci.apm_traces.models.QueryResultRowTypeSummary]

        :param source_name:
            The value to assign to the source_name property of this QueryResultMetadataSummary.
        :type source_name: str

        :param query_results_grouped_by:
            The value to assign to the query_results_grouped_by property of this QueryResultMetadataSummary.
        :type query_results_grouped_by: list[oci.apm_traces.models.QueryResultsGroupedBySummary]

        :param query_results_ordered_by:
            The value to assign to the query_results_ordered_by property of this QueryResultMetadataSummary.
        :type query_results_ordered_by: list[oci.apm_traces.models.QueryResultsOrderedBySummary]

        :param time_series_interval_in_mins:
            The value to assign to the time_series_interval_in_mins property of this QueryResultMetadataSummary.
        :type time_series_interval_in_mins: int

        """
        self.swagger_types = {
            'query_result_row_type_summaries': 'list[QueryResultRowTypeSummary]',
            'source_name': 'str',
            'query_results_grouped_by': 'list[QueryResultsGroupedBySummary]',
            'query_results_ordered_by': 'list[QueryResultsOrderedBySummary]',
            'time_series_interval_in_mins': 'int'
        }

        self.attribute_map = {
            'query_result_row_type_summaries': 'queryResultRowTypeSummaries',
            'source_name': 'sourceName',
            'query_results_grouped_by': 'queryResultsGroupedBy',
            'query_results_ordered_by': 'queryResultsOrderedBy',
            'time_series_interval_in_mins': 'timeSeriesIntervalInMins'
        }

        self._query_result_row_type_summaries = None
        self._source_name = None
        self._query_results_grouped_by = None
        self._query_results_ordered_by = None
        self._time_series_interval_in_mins = None

    @property
    def query_result_row_type_summaries(self):
        """
        Gets the query_result_row_type_summaries of this QueryResultMetadataSummary.
        A collection of QueryResultRowTypeSummary objects that describe the type and properties of the individual row elements of the query rows
        being returned.  The ith element in this list contains the QueryResultRowTypeSummary of the ith key value pair in the QueryResultRowData map.


        :return: The query_result_row_type_summaries of this QueryResultMetadataSummary.
        :rtype: list[oci.apm_traces.models.QueryResultRowTypeSummary]
        """
        return self._query_result_row_type_summaries

    @query_result_row_type_summaries.setter
    def query_result_row_type_summaries(self, query_result_row_type_summaries):
        """
        Sets the query_result_row_type_summaries of this QueryResultMetadataSummary.
        A collection of QueryResultRowTypeSummary objects that describe the type and properties of the individual row elements of the query rows
        being returned.  The ith element in this list contains the QueryResultRowTypeSummary of the ith key value pair in the QueryResultRowData map.


        :param query_result_row_type_summaries: The query_result_row_type_summaries of this QueryResultMetadataSummary.
        :type: list[oci.apm_traces.models.QueryResultRowTypeSummary]
        """
        self._query_result_row_type_summaries = query_result_row_type_summaries

    @property
    def source_name(self):
        """
        Gets the source_name of this QueryResultMetadataSummary.
        Source of the query result set (traces, spans, etc).


        :return: The source_name of this QueryResultMetadataSummary.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this QueryResultMetadataSummary.
        Source of the query result set (traces, spans, etc).


        :param source_name: The source_name of this QueryResultMetadataSummary.
        :type: str
        """
        self._source_name = source_name

    @property
    def query_results_grouped_by(self):
        """
        Gets the query_results_grouped_by of this QueryResultMetadataSummary.
        Columns or attributes of the query rows  which are group by values.  This is a list of ResultsGroupedBy summary objects,
        and the list will contain as many elements as the attributes and aggregate functions in the group by clause in the select query.


        :return: The query_results_grouped_by of this QueryResultMetadataSummary.
        :rtype: list[oci.apm_traces.models.QueryResultsGroupedBySummary]
        """
        return self._query_results_grouped_by

    @query_results_grouped_by.setter
    def query_results_grouped_by(self, query_results_grouped_by):
        """
        Sets the query_results_grouped_by of this QueryResultMetadataSummary.
        Columns or attributes of the query rows  which are group by values.  This is a list of ResultsGroupedBy summary objects,
        and the list will contain as many elements as the attributes and aggregate functions in the group by clause in the select query.


        :param query_results_grouped_by: The query_results_grouped_by of this QueryResultMetadataSummary.
        :type: list[oci.apm_traces.models.QueryResultsGroupedBySummary]
        """
        self._query_results_grouped_by = query_results_grouped_by

    @property
    def query_results_ordered_by(self):
        """
        Gets the query_results_ordered_by of this QueryResultMetadataSummary.
        Order by which the query results are organized.  This is a list of queryResultsOrderedBy summary objects, and the list
        will contain more than one OrderedBy summary object, if the sort was multidimensional.


        :return: The query_results_ordered_by of this QueryResultMetadataSummary.
        :rtype: list[oci.apm_traces.models.QueryResultsOrderedBySummary]
        """
        return self._query_results_ordered_by

    @query_results_ordered_by.setter
    def query_results_ordered_by(self, query_results_ordered_by):
        """
        Sets the query_results_ordered_by of this QueryResultMetadataSummary.
        Order by which the query results are organized.  This is a list of queryResultsOrderedBy summary objects, and the list
        will contain more than one OrderedBy summary object, if the sort was multidimensional.


        :param query_results_ordered_by: The query_results_ordered_by of this QueryResultMetadataSummary.
        :type: list[oci.apm_traces.models.QueryResultsOrderedBySummary]
        """
        self._query_results_ordered_by = query_results_ordered_by

    @property
    def time_series_interval_in_mins(self):
        """
        Gets the time_series_interval_in_mins of this QueryResultMetadataSummary.
        Interval for the time series function in minutes.


        :return: The time_series_interval_in_mins of this QueryResultMetadataSummary.
        :rtype: int
        """
        return self._time_series_interval_in_mins

    @time_series_interval_in_mins.setter
    def time_series_interval_in_mins(self, time_series_interval_in_mins):
        """
        Sets the time_series_interval_in_mins of this QueryResultMetadataSummary.
        Interval for the time series function in minutes.


        :param time_series_interval_in_mins: The time_series_interval_in_mins of this QueryResultMetadataSummary.
        :type: int
        """
        self._time_series_interval_in_mins = time_series_interval_in_mins

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
