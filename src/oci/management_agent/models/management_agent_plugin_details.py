# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementAgentPluginDetails(object):
    """
    The information about the current management agent plugins that agent is having.
    """

    #: A constant which can be used with the plugin_status property of a ManagementAgentPluginDetails.
    #: This constant has a value of "RUNNING"
    PLUGIN_STATUS_RUNNING = "RUNNING"

    #: A constant which can be used with the plugin_status property of a ManagementAgentPluginDetails.
    #: This constant has a value of "STOPPED"
    PLUGIN_STATUS_STOPPED = "STOPPED"

    #: A constant which can be used with the plugin_status property of a ManagementAgentPluginDetails.
    #: This constant has a value of "INVALID"
    PLUGIN_STATUS_INVALID = "INVALID"

    #: A constant which can be used with the plugin_status property of a ManagementAgentPluginDetails.
    #: This constant has a value of "FAILED"
    PLUGIN_STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementAgentPluginDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plugin_id:
            The value to assign to the plugin_id property of this ManagementAgentPluginDetails.
        :type plugin_id: str

        :param plugin_name:
            The value to assign to the plugin_name property of this ManagementAgentPluginDetails.
        :type plugin_name: str

        :param plugin_display_name:
            The value to assign to the plugin_display_name property of this ManagementAgentPluginDetails.
        :type plugin_display_name: str

        :param plugin_version:
            The value to assign to the plugin_version property of this ManagementAgentPluginDetails.
        :type plugin_version: str

        :param plugin_status:
            The value to assign to the plugin_status property of this ManagementAgentPluginDetails.
            Allowed values for this property are: "RUNNING", "STOPPED", "INVALID", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type plugin_status: str

        :param plugin_status_message:
            The value to assign to the plugin_status_message property of this ManagementAgentPluginDetails.
        :type plugin_status_message: str

        :param is_enabled:
            The value to assign to the is_enabled property of this ManagementAgentPluginDetails.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'plugin_id': 'str',
            'plugin_name': 'str',
            'plugin_display_name': 'str',
            'plugin_version': 'str',
            'plugin_status': 'str',
            'plugin_status_message': 'str',
            'is_enabled': 'bool'
        }

        self.attribute_map = {
            'plugin_id': 'pluginId',
            'plugin_name': 'pluginName',
            'plugin_display_name': 'pluginDisplayName',
            'plugin_version': 'pluginVersion',
            'plugin_status': 'pluginStatus',
            'plugin_status_message': 'pluginStatusMessage',
            'is_enabled': 'isEnabled'
        }

        self._plugin_id = None
        self._plugin_name = None
        self._plugin_display_name = None
        self._plugin_version = None
        self._plugin_status = None
        self._plugin_status_message = None
        self._is_enabled = None

    @property
    def plugin_id(self):
        """
        Gets the plugin_id of this ManagementAgentPluginDetails.
        Plugin Id


        :return: The plugin_id of this ManagementAgentPluginDetails.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """
        Sets the plugin_id of this ManagementAgentPluginDetails.
        Plugin Id


        :param plugin_id: The plugin_id of this ManagementAgentPluginDetails.
        :type: str
        """
        self._plugin_id = plugin_id

    @property
    def plugin_name(self):
        """
        **[Required]** Gets the plugin_name of this ManagementAgentPluginDetails.
        Management Agent Plugin Name


        :return: The plugin_name of this ManagementAgentPluginDetails.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """
        Sets the plugin_name of this ManagementAgentPluginDetails.
        Management Agent Plugin Name


        :param plugin_name: The plugin_name of this ManagementAgentPluginDetails.
        :type: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_display_name(self):
        """
        Gets the plugin_display_name of this ManagementAgentPluginDetails.
        Management Agent Plugin Identifier, can be renamed


        :return: The plugin_display_name of this ManagementAgentPluginDetails.
        :rtype: str
        """
        return self._plugin_display_name

    @plugin_display_name.setter
    def plugin_display_name(self, plugin_display_name):
        """
        Sets the plugin_display_name of this ManagementAgentPluginDetails.
        Management Agent Plugin Identifier, can be renamed


        :param plugin_display_name: The plugin_display_name of this ManagementAgentPluginDetails.
        :type: str
        """
        self._plugin_display_name = plugin_display_name

    @property
    def plugin_version(self):
        """
        Gets the plugin_version of this ManagementAgentPluginDetails.
        Plugin Version


        :return: The plugin_version of this ManagementAgentPluginDetails.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """
        Sets the plugin_version of this ManagementAgentPluginDetails.
        Plugin Version


        :param plugin_version: The plugin_version of this ManagementAgentPluginDetails.
        :type: str
        """
        self._plugin_version = plugin_version

    @property
    def plugin_status(self):
        """
        Gets the plugin_status of this ManagementAgentPluginDetails.
        Plugin Status

        Allowed values for this property are: "RUNNING", "STOPPED", "INVALID", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The plugin_status of this ManagementAgentPluginDetails.
        :rtype: str
        """
        return self._plugin_status

    @plugin_status.setter
    def plugin_status(self, plugin_status):
        """
        Sets the plugin_status of this ManagementAgentPluginDetails.
        Plugin Status


        :param plugin_status: The plugin_status of this ManagementAgentPluginDetails.
        :type: str
        """
        allowed_values = ["RUNNING", "STOPPED", "INVALID", "FAILED"]
        if not value_allowed_none_or_none_sentinel(plugin_status, allowed_values):
            plugin_status = 'UNKNOWN_ENUM_VALUE'
        self._plugin_status = plugin_status

    @property
    def plugin_status_message(self):
        """
        Gets the plugin_status_message of this ManagementAgentPluginDetails.
        Status message of the Plugin


        :return: The plugin_status_message of this ManagementAgentPluginDetails.
        :rtype: str
        """
        return self._plugin_status_message

    @plugin_status_message.setter
    def plugin_status_message(self, plugin_status_message):
        """
        Sets the plugin_status_message of this ManagementAgentPluginDetails.
        Status message of the Plugin


        :param plugin_status_message: The plugin_status_message of this ManagementAgentPluginDetails.
        :type: str
        """
        self._plugin_status_message = plugin_status_message

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this ManagementAgentPluginDetails.
        flag indicating whether the plugin is in enabled mode or disabled mode.


        :return: The is_enabled of this ManagementAgentPluginDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ManagementAgentPluginDetails.
        flag indicating whether the plugin is in enabled mode or disabled mode.


        :param is_enabled: The is_enabled of this ManagementAgentPluginDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
