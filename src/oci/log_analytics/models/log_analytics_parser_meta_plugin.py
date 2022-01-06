# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsParserMetaPlugin(object):
    """
    LogAnalyticsParserMetaPlugin
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsParserMetaPlugin object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param meta_plugin_parameters:
            The value to assign to the meta_plugin_parameters property of this LogAnalyticsParserMetaPlugin.
        :type meta_plugin_parameters: list[oci.log_analytics.models.LogAnalyticsParserMetaPluginParameter]

        :param description:
            The value to assign to the description property of this LogAnalyticsParserMetaPlugin.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsParserMetaPlugin.
        :type display_name: str

        :param name:
            The value to assign to the name property of this LogAnalyticsParserMetaPlugin.
        :type name: str

        """
        self.swagger_types = {
            'meta_plugin_parameters': 'list[LogAnalyticsParserMetaPluginParameter]',
            'description': 'str',
            'display_name': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'meta_plugin_parameters': 'metaPluginParameters',
            'description': 'description',
            'display_name': 'displayName',
            'name': 'name'
        }

        self._meta_plugin_parameters = None
        self._description = None
        self._display_name = None
        self._name = None

    @property
    def meta_plugin_parameters(self):
        """
        Gets the meta_plugin_parameters of this LogAnalyticsParserMetaPlugin.
        An array of plugin parameters.


        :return: The meta_plugin_parameters of this LogAnalyticsParserMetaPlugin.
        :rtype: list[oci.log_analytics.models.LogAnalyticsParserMetaPluginParameter]
        """
        return self._meta_plugin_parameters

    @meta_plugin_parameters.setter
    def meta_plugin_parameters(self, meta_plugin_parameters):
        """
        Sets the meta_plugin_parameters of this LogAnalyticsParserMetaPlugin.
        An array of plugin parameters.


        :param meta_plugin_parameters: The meta_plugin_parameters of this LogAnalyticsParserMetaPlugin.
        :type: list[oci.log_analytics.models.LogAnalyticsParserMetaPluginParameter]
        """
        self._meta_plugin_parameters = meta_plugin_parameters

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsParserMetaPlugin.
        The plugin description.


        :return: The description of this LogAnalyticsParserMetaPlugin.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsParserMetaPlugin.
        The plugin description.


        :param description: The description of this LogAnalyticsParserMetaPlugin.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsParserMetaPlugin.
        The plugin display name.


        :return: The display_name of this LogAnalyticsParserMetaPlugin.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsParserMetaPlugin.
        The plugin display name.


        :param display_name: The display_name of this LogAnalyticsParserMetaPlugin.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsParserMetaPlugin.
        The plugin internal name.


        :return: The name of this LogAnalyticsParserMetaPlugin.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsParserMetaPlugin.
        The plugin internal name.


        :param name: The name of this LogAnalyticsParserMetaPlugin.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
