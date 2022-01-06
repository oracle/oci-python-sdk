# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GeoStatsCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage GEOSTATS command.  This is similiar to STATS with some built in functions for City, State and Country by Coordinates.
    """

    #: A constant which can be used with the include property of a GeoStatsCommandDescriptor.
    #: This constant has a value of "CLIENT"
    INCLUDE_CLIENT = "CLIENT"

    #: A constant which can be used with the include property of a GeoStatsCommandDescriptor.
    #: This constant has a value of "SERVER"
    INCLUDE_SERVER = "SERVER"

    #: A constant which can be used with the include property of a GeoStatsCommandDescriptor.
    #: This constant has a value of "CLIENT_AND_SERVER"
    INCLUDE_CLIENT_AND_SERVER = "CLIENT_AND_SERVER"

    def __init__(self, **kwargs):
        """
        Initializes a new GeoStatsCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.GeoStatsCommandDescriptor.name` attribute
        of this class is ``GEO_STATS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this GeoStatsCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "GEO_STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "JSON_EXTRACT", "XML_EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP", "COMPARE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this GeoStatsCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this GeoStatsCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this GeoStatsCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this GeoStatsCommandDescriptor.
        :type referenced_fields: list[oci.log_analytics.models.AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this GeoStatsCommandDescriptor.
        :type declared_fields: list[oci.log_analytics.models.AbstractField]

        :param include:
            The value to assign to the include property of this GeoStatsCommandDescriptor.
            Allowed values for this property are: "CLIENT", "SERVER", "CLIENT_AND_SERVER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type include: str

        :param group_by_fields:
            The value to assign to the group_by_fields property of this GeoStatsCommandDescriptor.
        :type group_by_fields: list[oci.log_analytics.models.AbstractField]

        :param functions:
            The value to assign to the functions property of this GeoStatsCommandDescriptor.
        :type functions: list[oci.log_analytics.models.FunctionField]

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'include': 'str',
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
            'include': 'include',
            'group_by_fields': 'groupByFields',
            'functions': 'functions'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._include = None
        self._group_by_fields = None
        self._functions = None
        self._name = 'GEO_STATS'

    @property
    def include(self):
        """
        Gets the include of this GeoStatsCommandDescriptor.
        Indicates which coordinates to show.  Either client, server or both.  Defaults to client.

        Allowed values for this property are: "CLIENT", "SERVER", "CLIENT_AND_SERVER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The include of this GeoStatsCommandDescriptor.
        :rtype: str
        """
        return self._include

    @include.setter
    def include(self, include):
        """
        Sets the include of this GeoStatsCommandDescriptor.
        Indicates which coordinates to show.  Either client, server or both.  Defaults to client.


        :param include: The include of this GeoStatsCommandDescriptor.
        :type: str
        """
        allowed_values = ["CLIENT", "SERVER", "CLIENT_AND_SERVER"]
        if not value_allowed_none_or_none_sentinel(include, allowed_values):
            include = 'UNKNOWN_ENUM_VALUE'
        self._include = include

    @property
    def group_by_fields(self):
        """
        Gets the group_by_fields of this GeoStatsCommandDescriptor.
        Group by fields if specified in the query string.


        :return: The group_by_fields of this GeoStatsCommandDescriptor.
        :rtype: list[oci.log_analytics.models.AbstractField]
        """
        return self._group_by_fields

    @group_by_fields.setter
    def group_by_fields(self, group_by_fields):
        """
        Sets the group_by_fields of this GeoStatsCommandDescriptor.
        Group by fields if specified in the query string.


        :param group_by_fields: The group_by_fields of this GeoStatsCommandDescriptor.
        :type: list[oci.log_analytics.models.AbstractField]
        """
        self._group_by_fields = group_by_fields

    @property
    def functions(self):
        """
        Gets the functions of this GeoStatsCommandDescriptor.
        Statistical functions specified in the query string. Atleast 1 is required for a GEOSTATS command.


        :return: The functions of this GeoStatsCommandDescriptor.
        :rtype: list[oci.log_analytics.models.FunctionField]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """
        Sets the functions of this GeoStatsCommandDescriptor.
        Statistical functions specified in the query string. Atleast 1 is required for a GEOSTATS command.


        :param functions: The functions of this GeoStatsCommandDescriptor.
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
