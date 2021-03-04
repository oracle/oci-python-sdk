# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryResultsGroupedBySummary(object):
    """
    Summary of the attribute based on which the query results are grouped by.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryResultsGroupedBySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query_results_grouped_by_column:
            The value to assign to the query_results_grouped_by_column property of this QueryResultsGroupedBySummary.
        :type query_results_grouped_by_column: str

        """
        self.swagger_types = {
            'query_results_grouped_by_column': 'str'
        }

        self.attribute_map = {
            'query_results_grouped_by_column': 'queryResultsGroupedByColumn'
        }

        self._query_results_grouped_by_column = None

    @property
    def query_results_grouped_by_column(self):
        """
        Gets the query_results_grouped_by_column of this QueryResultsGroupedBySummary.
        Column or attribute in the query result which is a group by value.


        :return: The query_results_grouped_by_column of this QueryResultsGroupedBySummary.
        :rtype: str
        """
        return self._query_results_grouped_by_column

    @query_results_grouped_by_column.setter
    def query_results_grouped_by_column(self, query_results_grouped_by_column):
        """
        Sets the query_results_grouped_by_column of this QueryResultsGroupedBySummary.
        Column or attribute in the query result which is a group by value.


        :param query_results_grouped_by_column: The query_results_grouped_by_column of this QueryResultsGroupedBySummary.
        :type: str
        """
        self._query_results_grouped_by_column = query_results_grouped_by_column

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
