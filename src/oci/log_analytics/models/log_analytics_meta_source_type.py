# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsMetaSourceType(object):
    """
    LogAnalyticsMetaSourceType
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsMetaSourceType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param built_in_parser_name:
            The value to assign to the built_in_parser_name property of this LogAnalyticsMetaSourceType.
        :type built_in_parser_name: str

        :param description:
            The value to assign to the description property of this LogAnalyticsMetaSourceType.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsMetaSourceType.
        :type display_name: str

        :param entity_display_name:
            The value to assign to the entity_display_name property of this LogAnalyticsMetaSourceType.
        :type entity_display_name: str

        :param entity_name:
            The value to assign to the entity_name property of this LogAnalyticsMetaSourceType.
        :type entity_name: str

        :param name:
            The value to assign to the name property of this LogAnalyticsMetaSourceType.
        :type name: str

        :param maximum_exclude_pattern:
            The value to assign to the maximum_exclude_pattern property of this LogAnalyticsMetaSourceType.
        :type maximum_exclude_pattern: int

        :param maximum_include_pattern:
            The value to assign to the maximum_include_pattern property of this LogAnalyticsMetaSourceType.
        :type maximum_include_pattern: int

        """
        self.swagger_types = {
            'built_in_parser_name': 'str',
            'description': 'str',
            'display_name': 'str',
            'entity_display_name': 'str',
            'entity_name': 'str',
            'name': 'str',
            'maximum_exclude_pattern': 'int',
            'maximum_include_pattern': 'int'
        }

        self.attribute_map = {
            'built_in_parser_name': 'builtInParserName',
            'description': 'description',
            'display_name': 'displayName',
            'entity_display_name': 'entityDisplayName',
            'entity_name': 'entityName',
            'name': 'name',
            'maximum_exclude_pattern': 'maximumExcludePattern',
            'maximum_include_pattern': 'maximumIncludePattern'
        }

        self._built_in_parser_name = None
        self._description = None
        self._display_name = None
        self._entity_display_name = None
        self._entity_name = None
        self._name = None
        self._maximum_exclude_pattern = None
        self._maximum_include_pattern = None

    @property
    def built_in_parser_name(self):
        """
        Gets the built_in_parser_name of this LogAnalyticsMetaSourceType.
        built in parser name


        :return: The built_in_parser_name of this LogAnalyticsMetaSourceType.
        :rtype: str
        """
        return self._built_in_parser_name

    @built_in_parser_name.setter
    def built_in_parser_name(self, built_in_parser_name):
        """
        Sets the built_in_parser_name of this LogAnalyticsMetaSourceType.
        built in parser name


        :param built_in_parser_name: The built_in_parser_name of this LogAnalyticsMetaSourceType.
        :type: str
        """
        self._built_in_parser_name = built_in_parser_name

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsMetaSourceType.
        type description


        :return: The description of this LogAnalyticsMetaSourceType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsMetaSourceType.
        type description


        :param description: The description of this LogAnalyticsMetaSourceType.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsMetaSourceType.
        display name


        :return: The display_name of this LogAnalyticsMetaSourceType.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsMetaSourceType.
        display name


        :param display_name: The display_name of this LogAnalyticsMetaSourceType.
        :type: str
        """
        self._display_name = display_name

    @property
    def entity_display_name(self):
        """
        Gets the entity_display_name of this LogAnalyticsMetaSourceType.
        entity display name


        :return: The entity_display_name of this LogAnalyticsMetaSourceType.
        :rtype: str
        """
        return self._entity_display_name

    @entity_display_name.setter
    def entity_display_name(self, entity_display_name):
        """
        Sets the entity_display_name of this LogAnalyticsMetaSourceType.
        entity display name


        :param entity_display_name: The entity_display_name of this LogAnalyticsMetaSourceType.
        :type: str
        """
        self._entity_display_name = entity_display_name

    @property
    def entity_name(self):
        """
        Gets the entity_name of this LogAnalyticsMetaSourceType.
        entity name


        :return: The entity_name of this LogAnalyticsMetaSourceType.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this LogAnalyticsMetaSourceType.
        entity name


        :param entity_name: The entity_name of this LogAnalyticsMetaSourceType.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsMetaSourceType.
        source type name


        :return: The name of this LogAnalyticsMetaSourceType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsMetaSourceType.
        source type name


        :param name: The name of this LogAnalyticsMetaSourceType.
        :type: str
        """
        self._name = name

    @property
    def maximum_exclude_pattern(self):
        """
        Gets the maximum_exclude_pattern of this LogAnalyticsMetaSourceType.
        maximum exclude pattern


        :return: The maximum_exclude_pattern of this LogAnalyticsMetaSourceType.
        :rtype: int
        """
        return self._maximum_exclude_pattern

    @maximum_exclude_pattern.setter
    def maximum_exclude_pattern(self, maximum_exclude_pattern):
        """
        Sets the maximum_exclude_pattern of this LogAnalyticsMetaSourceType.
        maximum exclude pattern


        :param maximum_exclude_pattern: The maximum_exclude_pattern of this LogAnalyticsMetaSourceType.
        :type: int
        """
        self._maximum_exclude_pattern = maximum_exclude_pattern

    @property
    def maximum_include_pattern(self):
        """
        Gets the maximum_include_pattern of this LogAnalyticsMetaSourceType.
        maximum include pattern


        :return: The maximum_include_pattern of this LogAnalyticsMetaSourceType.
        :rtype: int
        """
        return self._maximum_include_pattern

    @maximum_include_pattern.setter
    def maximum_include_pattern(self, maximum_include_pattern):
        """
        Sets the maximum_include_pattern of this LogAnalyticsMetaSourceType.
        maximum include pattern


        :param maximum_include_pattern: The maximum_include_pattern of this LogAnalyticsMetaSourceType.
        :type: int
        """
        self._maximum_include_pattern = maximum_include_pattern

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
