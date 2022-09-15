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

    #: A constant which can be used with the include property of a GeoStatsCommandDescriptor.
    #: This constant has a value of "CUSTOM"
    INCLUDE_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new GeoStatsCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.GeoStatsCommandDescriptor.name` attribute
        of this class is ``GEO_STATS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this GeoStatsCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "GEO_STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "JSON_EXTRACT", "XML_EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MODULE", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP", "COMPARE", "ADD_INSIGHTS", "ANOMALY", "DEDUP", "TIME_CLUSTER", 'UNKNOWN_ENUM_VALUE'.
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

        :param is_hidden:
            The value to assign to the is_hidden property of this GeoStatsCommandDescriptor.
        :type is_hidden: bool

        :param include:
            The value to assign to the include property of this GeoStatsCommandDescriptor.
            Allowed values for this property are: "CLIENT", "SERVER", "CLIENT_AND_SERVER", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type include: str

        :param city_field:
            The value to assign to the city_field property of this GeoStatsCommandDescriptor.
        :type city_field: oci.log_analytics.models.AbstractField

        :param region_field:
            The value to assign to the region_field property of this GeoStatsCommandDescriptor.
        :type region_field: oci.log_analytics.models.AbstractField

        :param country_field:
            The value to assign to the country_field property of this GeoStatsCommandDescriptor.
        :type country_field: oci.log_analytics.models.AbstractField

        :param continent_field:
            The value to assign to the continent_field property of this GeoStatsCommandDescriptor.
        :type continent_field: oci.log_analytics.models.AbstractField

        :param coordinates_field:
            The value to assign to the coordinates_field property of this GeoStatsCommandDescriptor.
        :type coordinates_field: oci.log_analytics.models.AbstractField

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
            'is_hidden': 'bool',
            'include': 'str',
            'city_field': 'AbstractField',
            'region_field': 'AbstractField',
            'country_field': 'AbstractField',
            'continent_field': 'AbstractField',
            'coordinates_field': 'AbstractField',
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
            'include': 'include',
            'city_field': 'cityField',
            'region_field': 'regionField',
            'country_field': 'countryField',
            'continent_field': 'continentField',
            'coordinates_field': 'coordinatesField',
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
        self._include = None
        self._city_field = None
        self._region_field = None
        self._country_field = None
        self._continent_field = None
        self._coordinates_field = None
        self._group_by_fields = None
        self._functions = None
        self._name = 'GEO_STATS'

    @property
    def include(self):
        """
        Gets the include of this GeoStatsCommandDescriptor.
        Indicates which coordinates to show.  Either client, server, client and server or custom. If custom is specified at least one of  coordinatesField, regionField or countryField is required. Defaults to client.

        Allowed values for this property are: "CLIENT", "SERVER", "CLIENT_AND_SERVER", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The include of this GeoStatsCommandDescriptor.
        :rtype: str
        """
        return self._include

    @include.setter
    def include(self, include):
        """
        Sets the include of this GeoStatsCommandDescriptor.
        Indicates which coordinates to show.  Either client, server, client and server or custom. If custom is specified at least one of  coordinatesField, regionField or countryField is required. Defaults to client.


        :param include: The include of this GeoStatsCommandDescriptor.
        :type: str
        """
        allowed_values = ["CLIENT", "SERVER", "CLIENT_AND_SERVER", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(include, allowed_values):
            include = 'UNKNOWN_ENUM_VALUE'
        self._include = include

    @property
    def city_field(self):
        """
        Gets the city_field of this GeoStatsCommandDescriptor.
        The city field to use. Only applicable when include = CUSTOM.


        :return: The city_field of this GeoStatsCommandDescriptor.
        :rtype: oci.log_analytics.models.AbstractField
        """
        return self._city_field

    @city_field.setter
    def city_field(self, city_field):
        """
        Sets the city_field of this GeoStatsCommandDescriptor.
        The city field to use. Only applicable when include = CUSTOM.


        :param city_field: The city_field of this GeoStatsCommandDescriptor.
        :type: oci.log_analytics.models.AbstractField
        """
        self._city_field = city_field

    @property
    def region_field(self):
        """
        Gets the region_field of this GeoStatsCommandDescriptor.
        The region field to use. Only applicable when include = CUSTOM.


        :return: The region_field of this GeoStatsCommandDescriptor.
        :rtype: oci.log_analytics.models.AbstractField
        """
        return self._region_field

    @region_field.setter
    def region_field(self, region_field):
        """
        Sets the region_field of this GeoStatsCommandDescriptor.
        The region field to use. Only applicable when include = CUSTOM.


        :param region_field: The region_field of this GeoStatsCommandDescriptor.
        :type: oci.log_analytics.models.AbstractField
        """
        self._region_field = region_field

    @property
    def country_field(self):
        """
        Gets the country_field of this GeoStatsCommandDescriptor.
        The country field to use. Only applicable when include = CUSTOM.


        :return: The country_field of this GeoStatsCommandDescriptor.
        :rtype: oci.log_analytics.models.AbstractField
        """
        return self._country_field

    @country_field.setter
    def country_field(self, country_field):
        """
        Sets the country_field of this GeoStatsCommandDescriptor.
        The country field to use. Only applicable when include = CUSTOM.


        :param country_field: The country_field of this GeoStatsCommandDescriptor.
        :type: oci.log_analytics.models.AbstractField
        """
        self._country_field = country_field

    @property
    def continent_field(self):
        """
        Gets the continent_field of this GeoStatsCommandDescriptor.
        The continent field to use. Only applicable when include = CUSTOM.


        :return: The continent_field of this GeoStatsCommandDescriptor.
        :rtype: oci.log_analytics.models.AbstractField
        """
        return self._continent_field

    @continent_field.setter
    def continent_field(self, continent_field):
        """
        Sets the continent_field of this GeoStatsCommandDescriptor.
        The continent field to use. Only applicable when include = CUSTOM.


        :param continent_field: The continent_field of this GeoStatsCommandDescriptor.
        :type: oci.log_analytics.models.AbstractField
        """
        self._continent_field = continent_field

    @property
    def coordinates_field(self):
        """
        Gets the coordinates_field of this GeoStatsCommandDescriptor.
        The coordinates field to use. Only applicable when include = CUSTOM.


        :return: The coordinates_field of this GeoStatsCommandDescriptor.
        :rtype: oci.log_analytics.models.AbstractField
        """
        return self._coordinates_field

    @coordinates_field.setter
    def coordinates_field(self, coordinates_field):
        """
        Sets the coordinates_field of this GeoStatsCommandDescriptor.
        The coordinates field to use. Only applicable when include = CUSTOM.


        :param coordinates_field: The coordinates_field of this GeoStatsCommandDescriptor.
        :type: oci.log_analytics.models.AbstractField
        """
        self._coordinates_field = coordinates_field

    @property
    def group_by_fields(self):
        """
        Gets the group_by_fields of this GeoStatsCommandDescriptor.
        Group by fields if specified in the query string.  Required if include = CUSTOM.


        :return: The group_by_fields of this GeoStatsCommandDescriptor.
        :rtype: list[oci.log_analytics.models.AbstractField]
        """
        return self._group_by_fields

    @group_by_fields.setter
    def group_by_fields(self, group_by_fields):
        """
        Sets the group_by_fields of this GeoStatsCommandDescriptor.
        Group by fields if specified in the query string.  Required if include = CUSTOM.


        :param group_by_fields: The group_by_fields of this GeoStatsCommandDescriptor.
        :type: list[oci.log_analytics.models.AbstractField]
        """
        self._group_by_fields = group_by_fields

    @property
    def functions(self):
        """
        Gets the functions of this GeoStatsCommandDescriptor.
        Statistical functions specified in the query string. At least 1 is required for a GEOSTATS command.


        :return: The functions of this GeoStatsCommandDescriptor.
        :rtype: list[oci.log_analytics.models.FunctionField]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """
        Sets the functions of this GeoStatsCommandDescriptor.
        Statistical functions specified in the query string. At least 1 is required for a GEOSTATS command.


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
