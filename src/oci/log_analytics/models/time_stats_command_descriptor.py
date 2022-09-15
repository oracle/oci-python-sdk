# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TimeStatsCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage TIMESTATS command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TimeStatsCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.TimeStatsCommandDescriptor.name` attribute
        of this class is ``TIME_STATS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this TimeStatsCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "GEO_STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "JSON_EXTRACT", "XML_EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MODULE", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP", "COMPARE", "ADD_INSIGHTS", "ANOMALY", "DEDUP", "TIME_CLUSTER"
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this TimeStatsCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this TimeStatsCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this TimeStatsCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this TimeStatsCommandDescriptor.
        :type referenced_fields: list[oci.log_analytics.models.AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this TimeStatsCommandDescriptor.
        :type declared_fields: list[oci.log_analytics.models.AbstractField]

        :param is_hidden:
            The value to assign to the is_hidden property of this TimeStatsCommandDescriptor.
        :type is_hidden: bool

        :param time:
            The value to assign to the time property of this TimeStatsCommandDescriptor.
        :type time: oci.log_analytics.models.AbstractField

        :param span:
            The value to assign to the span property of this TimeStatsCommandDescriptor.
        :type span: str

        :param group_by_fields:
            The value to assign to the group_by_fields property of this TimeStatsCommandDescriptor.
        :type group_by_fields: list[oci.log_analytics.models.AbstractField]

        :param functions:
            The value to assign to the functions property of this TimeStatsCommandDescriptor.
        :type functions: list[oci.log_analytics.models.FunctionField]

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'is_hidden': 'bool',
            'time': 'AbstractField',
            'span': 'str',
            'group_by_fields': 'list[AbstractField]',
            'functions': 'list[FunctionField]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields',
            'is_hidden': 'isHidden',
            'time': 'time',
            'span': 'span',
            'group_by_fields': 'groupByFields',
            'functions': 'functions'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._is_hidden = None
        self._time = None
        self._span = None
        self._group_by_fields = None
        self._functions = None
        self._name = 'TIME_STATS'

    @property
    def time(self):
        """
        Gets the time of this TimeStatsCommandDescriptor.
        Optional timestamp datatype field if specified. Default field is time.


        :return: The time of this TimeStatsCommandDescriptor.
        :rtype: oci.log_analytics.models.AbstractField
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this TimeStatsCommandDescriptor.
        Optional timestamp datatype field if specified. Default field is time.


        :param time: The time of this TimeStatsCommandDescriptor.
        :type: oci.log_analytics.models.AbstractField
        """
        self._time = time

    @property
    def span(self):
        """
        Gets the span of this TimeStatsCommandDescriptor.
        Option to control the size of buckets in the histogram e.g 8hrs  - each bar other than first and last should represent 8hr time span. Will be adjusted to a larger span if time range is very large.


        :return: The span of this TimeStatsCommandDescriptor.
        :rtype: str
        """
        return self._span

    @span.setter
    def span(self, span):
        """
        Sets the span of this TimeStatsCommandDescriptor.
        Option to control the size of buckets in the histogram e.g 8hrs  - each bar other than first and last should represent 8hr time span. Will be adjusted to a larger span if time range is very large.


        :param span: The span of this TimeStatsCommandDescriptor.
        :type: str
        """
        self._span = span

    @property
    def group_by_fields(self):
        """
        Gets the group_by_fields of this TimeStatsCommandDescriptor.
        Group by fields if specified in the query string.


        :return: The group_by_fields of this TimeStatsCommandDescriptor.
        :rtype: list[oci.log_analytics.models.AbstractField]
        """
        return self._group_by_fields

    @group_by_fields.setter
    def group_by_fields(self, group_by_fields):
        """
        Sets the group_by_fields of this TimeStatsCommandDescriptor.
        Group by fields if specified in the query string.


        :param group_by_fields: The group_by_fields of this TimeStatsCommandDescriptor.
        :type: list[oci.log_analytics.models.AbstractField]
        """
        self._group_by_fields = group_by_fields

    @property
    def functions(self):
        """
        Gets the functions of this TimeStatsCommandDescriptor.
        Statistical functions specified in the query string. Atleast 1 is required for a TIMESTATS command.


        :return: The functions of this TimeStatsCommandDescriptor.
        :rtype: list[oci.log_analytics.models.FunctionField]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """
        Sets the functions of this TimeStatsCommandDescriptor.
        Statistical functions specified in the query string. Atleast 1 is required for a TIMESTATS command.


        :param functions: The functions of this TimeStatsCommandDescriptor.
        :type: list[oci.log_analytics.models.FunctionField]
        """
        self._functions = functions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
