# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryResultResponse(object):
    """
    A response containing a collection of query rows (selected attributes and aggregations) filtered, grouped and
    sorted by the specified criteria from the query that is run, and the associated summary describing the corresponding
    query result metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryResultResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query_result_metadata_summary:
            The value to assign to the query_result_metadata_summary property of this QueryResultResponse.
        :type query_result_metadata_summary: oci.apm_traces.models.QueryResultMetadataSummary

        :param query_result_rows:
            The value to assign to the query_result_rows property of this QueryResultResponse.
        :type query_result_rows: list[oci.apm_traces.models.QueryResultRow]

        """
        self.swagger_types = {
            'query_result_metadata_summary': 'QueryResultMetadataSummary',
            'query_result_rows': 'list[QueryResultRow]'
        }

        self.attribute_map = {
            'query_result_metadata_summary': 'queryResultMetadataSummary',
            'query_result_rows': 'queryResultRows'
        }

        self._query_result_metadata_summary = None
        self._query_result_rows = None

    @property
    def query_result_metadata_summary(self):
        """
        **[Required]** Gets the query_result_metadata_summary of this QueryResultResponse.

        :return: The query_result_metadata_summary of this QueryResultResponse.
        :rtype: oci.apm_traces.models.QueryResultMetadataSummary
        """
        return self._query_result_metadata_summary

    @query_result_metadata_summary.setter
    def query_result_metadata_summary(self, query_result_metadata_summary):
        """
        Sets the query_result_metadata_summary of this QueryResultResponse.

        :param query_result_metadata_summary: The query_result_metadata_summary of this QueryResultResponse.
        :type: oci.apm_traces.models.QueryResultMetadataSummary
        """
        self._query_result_metadata_summary = query_result_metadata_summary

    @property
    def query_result_rows(self):
        """
        **[Required]** Gets the query_result_rows of this QueryResultResponse.
        A collection of objects with each object representing an individual row of the query result set.  The total number of objects
        returned in this collection correspond to the total number of rows returned by the actual query that is run against
        the queried entity.


        :return: The query_result_rows of this QueryResultResponse.
        :rtype: list[oci.apm_traces.models.QueryResultRow]
        """
        return self._query_result_rows

    @query_result_rows.setter
    def query_result_rows(self, query_result_rows):
        """
        Sets the query_result_rows of this QueryResultResponse.
        A collection of objects with each object representing an individual row of the query result set.  The total number of objects
        returned in this collection correspond to the total number of rows returned by the actual query that is run against
        the queried entity.


        :param query_result_rows: The query_result_rows of this QueryResultResponse.
        :type: list[oci.apm_traces.models.QueryResultRow]
        """
        self._query_result_rows = query_result_rows

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
