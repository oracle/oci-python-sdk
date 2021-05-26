# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HighlightGroupsCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage HIGHLIGHTGROUPS command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HighlightGroupsCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.HighlightGroupsCommandDescriptor.name` attribute
        of this class is ``HIGHLIGHT_GROUPS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this HighlightGroupsCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP", "COMPARE"
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this HighlightGroupsCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this HighlightGroupsCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this HighlightGroupsCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this HighlightGroupsCommandDescriptor.
        :type referenced_fields: list[oci.log_analytics.models.AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this HighlightGroupsCommandDescriptor.
        :type declared_fields: list[oci.log_analytics.models.AbstractField]

        :param color:
            The value to assign to the color property of this HighlightGroupsCommandDescriptor.
        :type color: str

        :param priority:
            The value to assign to the priority property of this HighlightGroupsCommandDescriptor.
        :type priority: str

        :param fields:
            The value to assign to the fields property of this HighlightGroupsCommandDescriptor.
        :type fields: list[str]

        :param keywords:
            The value to assign to the keywords property of this HighlightGroupsCommandDescriptor.
        :type keywords: list[str]

        :param sub_queries:
            The value to assign to the sub_queries property of this HighlightGroupsCommandDescriptor.
        :type sub_queries: list[oci.log_analytics.models.ParseQueryOutput]

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'color': 'str',
            'priority': 'str',
            'fields': 'list[str]',
            'keywords': 'list[str]',
            'sub_queries': 'list[ParseQueryOutput]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields',
            'color': 'color',
            'priority': 'priority',
            'fields': 'fields',
            'keywords': 'keywords',
            'sub_queries': 'subQueries'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._color = None
        self._priority = None
        self._fields = None
        self._keywords = None
        self._sub_queries = None
        self._name = 'HIGHLIGHT_GROUPS'

    @property
    def color(self):
        """
        Gets the color of this HighlightGroupsCommandDescriptor.
        User specified color to highlight matches with if found.


        :return: The color of this HighlightGroupsCommandDescriptor.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this HighlightGroupsCommandDescriptor.
        User specified color to highlight matches with if found.


        :param color: The color of this HighlightGroupsCommandDescriptor.
        :type: str
        """
        self._color = color

    @property
    def priority(self):
        """
        Gets the priority of this HighlightGroupsCommandDescriptor.
        User specified priority assigned to highlighted matches if found.


        :return: The priority of this HighlightGroupsCommandDescriptor.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this HighlightGroupsCommandDescriptor.
        User specified priority assigned to highlighted matches if found.


        :param priority: The priority of this HighlightGroupsCommandDescriptor.
        :type: str
        """
        self._priority = priority

    @property
    def fields(self):
        """
        Gets the fields of this HighlightGroupsCommandDescriptor.
        List of fields to search for terms or phrases to highlight.


        :return: The fields of this HighlightGroupsCommandDescriptor.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this HighlightGroupsCommandDescriptor.
        List of fields to search for terms or phrases to highlight.


        :param fields: The fields of this HighlightGroupsCommandDescriptor.
        :type: list[str]
        """
        self._fields = fields

    @property
    def keywords(self):
        """
        Gets the keywords of this HighlightGroupsCommandDescriptor.
        List of terms or phrases to highlight if found.


        :return: The keywords of this HighlightGroupsCommandDescriptor.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this HighlightGroupsCommandDescriptor.
        List of terms or phrases to highlight if found.


        :param keywords: The keywords of this HighlightGroupsCommandDescriptor.
        :type: list[str]
        """
        self._keywords = keywords

    @property
    def sub_queries(self):
        """
        Gets the sub_queries of this HighlightGroupsCommandDescriptor.
        List of subQueries specified as highlightgroups command arguments


        :return: The sub_queries of this HighlightGroupsCommandDescriptor.
        :rtype: list[oci.log_analytics.models.ParseQueryOutput]
        """
        return self._sub_queries

    @sub_queries.setter
    def sub_queries(self, sub_queries):
        """
        Sets the sub_queries of this HighlightGroupsCommandDescriptor.
        List of subQueries specified as highlightgroups command arguments


        :param sub_queries: The sub_queries of this HighlightGroupsCommandDescriptor.
        :type: list[oci.log_analytics.models.ParseQueryOutput]
        """
        self._sub_queries = sub_queries

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
