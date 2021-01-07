# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchResponse(object):
    """
    Search response object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param results:
            The value to assign to the results property of this SearchResponse.
        :type results: list[oci.loggingsearch.models.SearchResult]

        :param fields:
            The value to assign to the fields property of this SearchResponse.
        :type fields: list[oci.loggingsearch.models.FieldInfo]

        :param summary:
            The value to assign to the summary property of this SearchResponse.
        :type summary: oci.loggingsearch.models.SearchResultSummary

        """
        self.swagger_types = {
            'results': 'list[SearchResult]',
            'fields': 'list[FieldInfo]',
            'summary': 'SearchResultSummary'
        }

        self.attribute_map = {
            'results': 'results',
            'fields': 'fields',
            'summary': 'summary'
        }

        self._results = None
        self._fields = None
        self._summary = None

    @property
    def results(self):
        """
        Gets the results of this SearchResponse.
        List of search results


        :return: The results of this SearchResponse.
        :rtype: list[oci.loggingsearch.models.SearchResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this SearchResponse.
        List of search results


        :param results: The results of this SearchResponse.
        :type: list[oci.loggingsearch.models.SearchResult]
        """
        self._results = results

    @property
    def fields(self):
        """
        Gets the fields of this SearchResponse.
        List of log field schema information.


        :return: The fields of this SearchResponse.
        :rtype: list[oci.loggingsearch.models.FieldInfo]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this SearchResponse.
        List of log field schema information.


        :param fields: The fields of this SearchResponse.
        :type: list[oci.loggingsearch.models.FieldInfo]
        """
        self._fields = fields

    @property
    def summary(self):
        """
        **[Required]** Gets the summary of this SearchResponse.

        :return: The summary of this SearchResponse.
        :rtype: oci.loggingsearch.models.SearchResultSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this SearchResponse.

        :param summary: The summary of this SearchResponse.
        :type: oci.loggingsearch.models.SearchResultSummary
        """
        self._summary = summary

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
