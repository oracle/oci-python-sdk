# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LinkCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage LINK command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LinkCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.LinkCommandDescriptor.name` attribute
        of this class is ``LINK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this LinkCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "GEO_STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "JSON_EXTRACT", "XML_EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP", "COMPARE"
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this LinkCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this LinkCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this LinkCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this LinkCommandDescriptor.
        :type referenced_fields: list[oci.log_analytics.models.AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this LinkCommandDescriptor.
        :type declared_fields: list[oci.log_analytics.models.AbstractField]

        :param should_include_nulls:
            The value to assign to the should_include_nulls property of this LinkCommandDescriptor.
        :type should_include_nulls: bool

        :param should_include_trends:
            The value to assign to the should_include_trends property of this LinkCommandDescriptor.
        :type should_include_trends: bool

        :param span:
            The value to assign to the span property of this LinkCommandDescriptor.
        :type span: str

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'should_include_nulls': 'bool',
            'should_include_trends': 'bool',
            'span': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields',
            'should_include_nulls': 'shouldIncludeNulls',
            'should_include_trends': 'shouldIncludeTrends',
            'span': 'span'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._should_include_nulls = None
        self._should_include_trends = None
        self._span = None
        self._name = 'LINK'

    @property
    def should_include_nulls(self):
        """
        Gets the should_include_nulls of this LinkCommandDescriptor.
        Option to return groups with a null value if specified.


        :return: The should_include_nulls of this LinkCommandDescriptor.
        :rtype: bool
        """
        return self._should_include_nulls

    @should_include_nulls.setter
    def should_include_nulls(self, should_include_nulls):
        """
        Sets the should_include_nulls of this LinkCommandDescriptor.
        Option to return groups with a null value if specified.


        :param should_include_nulls: The should_include_nulls of this LinkCommandDescriptor.
        :type: bool
        """
        self._should_include_nulls = should_include_nulls

    @property
    def should_include_trends(self):
        """
        Gets the should_include_trends of this LinkCommandDescriptor.
        Option to calculate trends of each group if specified.


        :return: The should_include_trends of this LinkCommandDescriptor.
        :rtype: bool
        """
        return self._should_include_trends

    @should_include_trends.setter
    def should_include_trends(self, should_include_trends):
        """
        Sets the should_include_trends of this LinkCommandDescriptor.
        Option to calculate trends of each group if specified.


        :param should_include_trends: The should_include_trends of this LinkCommandDescriptor.
        :type: bool
        """
        self._should_include_trends = should_include_trends

    @property
    def span(self):
        """
        Gets the span of this LinkCommandDescriptor.
        Option to control the size of buckets in the histogram e.g 8hrs  - each bar other than first and last should represent 8hr time span. Will be adjusted to a larger span if time range is very large.


        :return: The span of this LinkCommandDescriptor.
        :rtype: str
        """
        return self._span

    @span.setter
    def span(self, span):
        """
        Sets the span of this LinkCommandDescriptor.
        Option to control the size of buckets in the histogram e.g 8hrs  - each bar other than first and last should represent 8hr time span. Will be adjusted to a larger span if time range is very large.


        :param span: The span of this LinkCommandDescriptor.
        :type: str
        """
        self._span = span

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
