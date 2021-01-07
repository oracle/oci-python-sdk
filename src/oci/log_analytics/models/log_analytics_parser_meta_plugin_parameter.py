# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsParserMetaPluginParameter(object):
    """
    LogAnalyticsParserMetaPluginParameter
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsParserMetaPluginParameter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this LogAnalyticsParserMetaPluginParameter.
        :type description: str

        :param name:
            The value to assign to the name property of this LogAnalyticsParserMetaPluginParameter.
        :type name: str

        :param is_mandatory:
            The value to assign to the is_mandatory property of this LogAnalyticsParserMetaPluginParameter.
        :type is_mandatory: bool

        :param is_repeatable:
            The value to assign to the is_repeatable property of this LogAnalyticsParserMetaPluginParameter.
        :type is_repeatable: bool

        :param plugin_name:
            The value to assign to the plugin_name property of this LogAnalyticsParserMetaPluginParameter.
        :type plugin_name: str

        :param type:
            The value to assign to the type property of this LogAnalyticsParserMetaPluginParameter.
        :type type: str

        """
        self.swagger_types = {
            'description': 'str',
            'name': 'str',
            'is_mandatory': 'bool',
            'is_repeatable': 'bool',
            'plugin_name': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'name': 'name',
            'is_mandatory': 'isMandatory',
            'is_repeatable': 'isRepeatable',
            'plugin_name': 'pluginName',
            'type': 'type'
        }

        self._description = None
        self._name = None
        self._is_mandatory = None
        self._is_repeatable = None
        self._plugin_name = None
        self._type = None

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsParserMetaPluginParameter.
        parameter description


        :return: The description of this LogAnalyticsParserMetaPluginParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsParserMetaPluginParameter.
        parameter description


        :param description: The description of this LogAnalyticsParserMetaPluginParameter.
        :type: str
        """
        self._description = description

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsParserMetaPluginParameter.
        parameter internal name


        :return: The name of this LogAnalyticsParserMetaPluginParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsParserMetaPluginParameter.
        parameter internal name


        :param name: The name of this LogAnalyticsParserMetaPluginParameter.
        :type: str
        """
        self._name = name

    @property
    def is_mandatory(self):
        """
        Gets the is_mandatory of this LogAnalyticsParserMetaPluginParameter.
        is mandatory flag


        :return: The is_mandatory of this LogAnalyticsParserMetaPluginParameter.
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """
        Sets the is_mandatory of this LogAnalyticsParserMetaPluginParameter.
        is mandatory flag


        :param is_mandatory: The is_mandatory of this LogAnalyticsParserMetaPluginParameter.
        :type: bool
        """
        self._is_mandatory = is_mandatory

    @property
    def is_repeatable(self):
        """
        Gets the is_repeatable of this LogAnalyticsParserMetaPluginParameter.
        is repeatable flag


        :return: The is_repeatable of this LogAnalyticsParserMetaPluginParameter.
        :rtype: bool
        """
        return self._is_repeatable

    @is_repeatable.setter
    def is_repeatable(self, is_repeatable):
        """
        Sets the is_repeatable of this LogAnalyticsParserMetaPluginParameter.
        is repeatable flag


        :param is_repeatable: The is_repeatable of this LogAnalyticsParserMetaPluginParameter.
        :type: bool
        """
        self._is_repeatable = is_repeatable

    @property
    def plugin_name(self):
        """
        Gets the plugin_name of this LogAnalyticsParserMetaPluginParameter.
        plugin internal name


        :return: The plugin_name of this LogAnalyticsParserMetaPluginParameter.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """
        Sets the plugin_name of this LogAnalyticsParserMetaPluginParameter.
        plugin internal name


        :param plugin_name: The plugin_name of this LogAnalyticsParserMetaPluginParameter.
        :type: str
        """
        self._plugin_name = plugin_name

    @property
    def type(self):
        """
        Gets the type of this LogAnalyticsParserMetaPluginParameter.
        parameter type


        :return: The type of this LogAnalyticsParserMetaPluginParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LogAnalyticsParserMetaPluginParameter.
        parameter type


        :param type: The type of this LogAnalyticsParserMetaPluginParameter.
        :type: str
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
