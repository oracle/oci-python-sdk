# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementAgentPluginAggregationDimensions(object):
    """
    The Aggregation of Management Agent Plugin Dimensions
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementAgentPluginAggregationDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plugin_name:
            The value to assign to the plugin_name property of this ManagementAgentPluginAggregationDimensions.
        :type plugin_name: str

        :param plugin_display_name:
            The value to assign to the plugin_display_name property of this ManagementAgentPluginAggregationDimensions.
        :type plugin_display_name: str

        """
        self.swagger_types = {
            'plugin_name': 'str',
            'plugin_display_name': 'str'
        }

        self.attribute_map = {
            'plugin_name': 'pluginName',
            'plugin_display_name': 'pluginDisplayName'
        }

        self._plugin_name = None
        self._plugin_display_name = None

    @property
    def plugin_name(self):
        """
        Gets the plugin_name of this ManagementAgentPluginAggregationDimensions.
        Management Agent Plugin Name


        :return: The plugin_name of this ManagementAgentPluginAggregationDimensions.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """
        Sets the plugin_name of this ManagementAgentPluginAggregationDimensions.
        Management Agent Plugin Name


        :param plugin_name: The plugin_name of this ManagementAgentPluginAggregationDimensions.
        :type: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_display_name(self):
        """
        Gets the plugin_display_name of this ManagementAgentPluginAggregationDimensions.
        Management Agent Plugin Display Name


        :return: The plugin_display_name of this ManagementAgentPluginAggregationDimensions.
        :rtype: str
        """
        return self._plugin_display_name

    @plugin_display_name.setter
    def plugin_display_name(self, plugin_display_name):
        """
        Sets the plugin_display_name of this ManagementAgentPluginAggregationDimensions.
        Management Agent Plugin Display Name


        :param plugin_display_name: The plugin_display_name of this ManagementAgentPluginAggregationDimensions.
        :type: str
        """
        self._plugin_display_name = plugin_display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
