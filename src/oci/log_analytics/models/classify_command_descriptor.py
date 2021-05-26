# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClassifyCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage CLASSIFY command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClassifyCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.ClassifyCommandDescriptor.name` attribute
        of this class is ``CLASSIFY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ClassifyCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP", "COMPARE"
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this ClassifyCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this ClassifyCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this ClassifyCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this ClassifyCommandDescriptor.
        :type referenced_fields: list[oci.log_analytics.models.AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this ClassifyCommandDescriptor.
        :type declared_fields: list[oci.log_analytics.models.AbstractField]

        :param top_count:
            The value to assign to the top_count property of this ClassifyCommandDescriptor.
        :type top_count: int

        :param bottom_count:
            The value to assign to the bottom_count property of this ClassifyCommandDescriptor.
        :type bottom_count: int

        :param correlate:
            The value to assign to the correlate property of this ClassifyCommandDescriptor.
        :type correlate: list[oci.log_analytics.models.FieldsAddRemoveField]

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'top_count': 'int',
            'bottom_count': 'int',
            'correlate': 'list[FieldsAddRemoveField]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields',
            'top_count': 'topCount',
            'bottom_count': 'bottomCount',
            'correlate': 'correlate'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._top_count = None
        self._bottom_count = None
        self._correlate = None
        self._name = 'CLASSIFY'

    @property
    def top_count(self):
        """
        Gets the top_count of this ClassifyCommandDescriptor.
        Value specified in CLASSIFY command in queryString if set limits the results returned to top N.


        :return: The top_count of this ClassifyCommandDescriptor.
        :rtype: int
        """
        return self._top_count

    @top_count.setter
    def top_count(self, top_count):
        """
        Sets the top_count of this ClassifyCommandDescriptor.
        Value specified in CLASSIFY command in queryString if set limits the results returned to top N.


        :param top_count: The top_count of this ClassifyCommandDescriptor.
        :type: int
        """
        self._top_count = top_count

    @property
    def bottom_count(self):
        """
        Gets the bottom_count of this ClassifyCommandDescriptor.
        Value specified in CLASSIFY command in queryString if set limits the results returned to bottom N.


        :return: The bottom_count of this ClassifyCommandDescriptor.
        :rtype: int
        """
        return self._bottom_count

    @bottom_count.setter
    def bottom_count(self, bottom_count):
        """
        Sets the bottom_count of this ClassifyCommandDescriptor.
        Value specified in CLASSIFY command in queryString if set limits the results returned to bottom N.


        :param bottom_count: The bottom_count of this ClassifyCommandDescriptor.
        :type: int
        """
        self._bottom_count = bottom_count

    @property
    def correlate(self):
        """
        Gets the correlate of this ClassifyCommandDescriptor.
        Fields specified in CLASSIFY command in queryString if set include / exclude fields in correlate results.


        :return: The correlate of this ClassifyCommandDescriptor.
        :rtype: list[oci.log_analytics.models.FieldsAddRemoveField]
        """
        return self._correlate

    @correlate.setter
    def correlate(self, correlate):
        """
        Sets the correlate of this ClassifyCommandDescriptor.
        Fields specified in CLASSIFY command in queryString if set include / exclude fields in correlate results.


        :param correlate: The correlate of this ClassifyCommandDescriptor.
        :type: list[oci.log_analytics.models.FieldsAddRemoveField]
        """
        self._correlate = correlate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
