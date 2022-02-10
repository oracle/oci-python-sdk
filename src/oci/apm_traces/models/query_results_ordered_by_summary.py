# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryResultsOrderedBySummary(object):
    """
    Summary of the sort and order by attribute based on which the query results are organized.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryResultsOrderedBySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query_results_ordered_by:
            The value to assign to the query_results_ordered_by property of this QueryResultsOrderedBySummary.
        :type query_results_ordered_by: str

        :param query_results_sort_order:
            The value to assign to the query_results_sort_order property of this QueryResultsOrderedBySummary.
        :type query_results_sort_order: str

        """
        self.swagger_types = {
            'query_results_ordered_by': 'str',
            'query_results_sort_order': 'str'
        }

        self.attribute_map = {
            'query_results_ordered_by': 'queryResultsOrderedBy',
            'query_results_sort_order': 'queryResultsSortOrder'
        }

        self._query_results_ordered_by = None
        self._query_results_sort_order = None

    @property
    def query_results_ordered_by(self):
        """
        Gets the query_results_ordered_by of this QueryResultsOrderedBySummary.
        Attribute by which the query results are sorted.


        :return: The query_results_ordered_by of this QueryResultsOrderedBySummary.
        :rtype: str
        """
        return self._query_results_ordered_by

    @query_results_ordered_by.setter
    def query_results_ordered_by(self, query_results_ordered_by):
        """
        Sets the query_results_ordered_by of this QueryResultsOrderedBySummary.
        Attribute by which the query results are sorted.


        :param query_results_ordered_by: The query_results_ordered_by of this QueryResultsOrderedBySummary.
        :type: str
        """
        self._query_results_ordered_by = query_results_ordered_by

    @property
    def query_results_sort_order(self):
        """
        Gets the query_results_sort_order of this QueryResultsOrderedBySummary.
        The sort order for the attribute, either 'ASC' or 'DESC'.


        :return: The query_results_sort_order of this QueryResultsOrderedBySummary.
        :rtype: str
        """
        return self._query_results_sort_order

    @query_results_sort_order.setter
    def query_results_sort_order(self, query_results_sort_order):
        """
        Sets the query_results_sort_order of this QueryResultsOrderedBySummary.
        The sort order for the attribute, either 'ASC' or 'DESC'.


        :param query_results_sort_order: The query_results_sort_order of this QueryResultsOrderedBySummary.
        :type: str
        """
        self._query_results_sort_order = query_results_sort_order

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
