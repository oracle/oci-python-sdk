# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HighlightRowsCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage HIGHLIGHTROWS command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HighlightRowsCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.HighlightRowsCommandDescriptor.name` attribute
        of this class is ``HIGHLIGHT_ROWS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this HighlightRowsCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP"
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this HighlightRowsCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this HighlightRowsCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this HighlightRowsCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this HighlightRowsCommandDescriptor.
        :type referenced_fields: list[oci.log_analytics.models.AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this HighlightRowsCommandDescriptor.
        :type declared_fields: list[oci.log_analytics.models.AbstractField]

        :param color:
            The value to assign to the color property of this HighlightRowsCommandDescriptor.
        :type color: str

        :param keywords:
            The value to assign to the keywords property of this HighlightRowsCommandDescriptor.
        :type keywords: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'color': 'str',
            'keywords': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields',
            'color': 'color',
            'keywords': 'keywords'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._color = None
        self._keywords = None
        self._name = 'HIGHLIGHT_ROWS'

    @property
    def color(self):
        """
        Gets the color of this HighlightRowsCommandDescriptor.
        User specified color to highlight matches with if found.


        :return: The color of this HighlightRowsCommandDescriptor.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this HighlightRowsCommandDescriptor.
        User specified color to highlight matches with if found.


        :param color: The color of this HighlightRowsCommandDescriptor.
        :type: str
        """
        self._color = color

    @property
    def keywords(self):
        """
        Gets the keywords of this HighlightRowsCommandDescriptor.
        List of terms or phrases to find to mark the result row as highlighted.


        :return: The keywords of this HighlightRowsCommandDescriptor.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this HighlightRowsCommandDescriptor.
        List of terms or phrases to find to mark the result row as highlighted.


        :param keywords: The keywords of this HighlightRowsCommandDescriptor.
        :type: list[str]
        """
        self._keywords = keywords

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
