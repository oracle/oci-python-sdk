# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterCompareCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage CLUSTERCOMPARE command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterCompareCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.ClusterCompareCommandDescriptor.name` attribute
        of this class is ``CLUSTER_COMPARE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ClusterCompareCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "GEO_STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "JSON_EXTRACT", "XML_EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP", "COMPARE"
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this ClusterCompareCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this ClusterCompareCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this ClusterCompareCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this ClusterCompareCommandDescriptor.
        :type referenced_fields: list[oci.log_analytics.models.AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this ClusterCompareCommandDescriptor.
        :type declared_fields: list[oci.log_analytics.models.AbstractField]

        :param time_shift:
            The value to assign to the time_shift property of this ClusterCompareCommandDescriptor.
        :type time_shift: str

        :param time_start:
            The value to assign to the time_start property of this ClusterCompareCommandDescriptor.
        :type time_start: int

        :param time_end:
            The value to assign to the time_end property of this ClusterCompareCommandDescriptor.
        :type time_end: int

        :param should_include_trends:
            The value to assign to the should_include_trends property of this ClusterCompareCommandDescriptor.
        :type should_include_trends: bool

        :param span:
            The value to assign to the span property of this ClusterCompareCommandDescriptor.
        :type span: str

        :param baseline_query:
            The value to assign to the baseline_query property of this ClusterCompareCommandDescriptor.
        :type baseline_query: str

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'time_shift': 'str',
            'time_start': 'int',
            'time_end': 'int',
            'should_include_trends': 'bool',
            'span': 'str',
            'baseline_query': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields',
            'time_shift': 'timeShift',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'should_include_trends': 'shouldIncludeTrends',
            'span': 'span',
            'baseline_query': 'baselineQuery'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._time_shift = None
        self._time_start = None
        self._time_end = None
        self._should_include_trends = None
        self._span = None
        self._baseline_query = None
        self._name = 'CLUSTER_COMPARE'

    @property
    def time_shift(self):
        """
        Gets the time_shift of this ClusterCompareCommandDescriptor.
        To shift time range of main query backwards using a relative time expression e.g -24hrs. E.g compare against the previous 24 hrs.


        :return: The time_shift of this ClusterCompareCommandDescriptor.
        :rtype: str
        """
        return self._time_shift

    @time_shift.setter
    def time_shift(self, time_shift):
        """
        Sets the time_shift of this ClusterCompareCommandDescriptor.
        To shift time range of main query backwards using a relative time expression e.g -24hrs. E.g compare against the previous 24 hrs.


        :param time_shift: The time_shift of this ClusterCompareCommandDescriptor.
        :type: str
        """
        self._time_shift = time_shift

    @property
    def time_start(self):
        """
        Gets the time_start of this ClusterCompareCommandDescriptor.
        Start time to apply to base line query if specified.


        :return: The time_start of this ClusterCompareCommandDescriptor.
        :rtype: int
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this ClusterCompareCommandDescriptor.
        Start time to apply to base line query if specified.


        :param time_start: The time_start of this ClusterCompareCommandDescriptor.
        :type: int
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this ClusterCompareCommandDescriptor.
        End time to apply to base line query if specified.


        :return: The time_end of this ClusterCompareCommandDescriptor.
        :rtype: int
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this ClusterCompareCommandDescriptor.
        End time to apply to base line query if specified.


        :param time_end: The time_end of this ClusterCompareCommandDescriptor.
        :type: int
        """
        self._time_end = time_end

    @property
    def should_include_trends(self):
        """
        Gets the should_include_trends of this ClusterCompareCommandDescriptor.
        Option to calculate trends of each cluster if specified.


        :return: The should_include_trends of this ClusterCompareCommandDescriptor.
        :rtype: bool
        """
        return self._should_include_trends

    @should_include_trends.setter
    def should_include_trends(self, should_include_trends):
        """
        Sets the should_include_trends of this ClusterCompareCommandDescriptor.
        Option to calculate trends of each cluster if specified.


        :param should_include_trends: The should_include_trends of this ClusterCompareCommandDescriptor.
        :type: bool
        """
        self._should_include_trends = should_include_trends

    @property
    def span(self):
        """
        Gets the span of this ClusterCompareCommandDescriptor.
        Option to control the size of buckets in the histogram e.g 8hrs  - each bar other than first and last should represent 8hr time span. Will be adjusted to a larger span if time range is very large.


        :return: The span of this ClusterCompareCommandDescriptor.
        :rtype: str
        """
        return self._span

    @span.setter
    def span(self, span):
        """
        Sets the span of this ClusterCompareCommandDescriptor.
        Option to control the size of buckets in the histogram e.g 8hrs  - each bar other than first and last should represent 8hr time span. Will be adjusted to a larger span if time range is very large.


        :param span: The span of this ClusterCompareCommandDescriptor.
        :type: str
        """
        self._span = span

    @property
    def baseline_query(self):
        """
        Gets the baseline_query of this ClusterCompareCommandDescriptor.
        Query to use to compute base line to compare top level query results against to identify differences if specified.


        :return: The baseline_query of this ClusterCompareCommandDescriptor.
        :rtype: str
        """
        return self._baseline_query

    @baseline_query.setter
    def baseline_query(self, baseline_query):
        """
        Sets the baseline_query of this ClusterCompareCommandDescriptor.
        Query to use to compute base line to compare top level query results against to identify differences if specified.


        :param baseline_query: The baseline_query of this ClusterCompareCommandDescriptor.
        :type: str
        """
        self._baseline_query = baseline_query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
