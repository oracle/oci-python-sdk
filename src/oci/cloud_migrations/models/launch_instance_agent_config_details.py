# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchInstanceAgentConfigDetails(object):
    """
    Configuration options for the Oracle Cloud Agent software running on the instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchInstanceAgentConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_monitoring_disabled:
            The value to assign to the is_monitoring_disabled property of this LaunchInstanceAgentConfigDetails.
        :type is_monitoring_disabled: bool

        :param is_management_disabled:
            The value to assign to the is_management_disabled property of this LaunchInstanceAgentConfigDetails.
        :type is_management_disabled: bool

        :param are_all_plugins_disabled:
            The value to assign to the are_all_plugins_disabled property of this LaunchInstanceAgentConfigDetails.
        :type are_all_plugins_disabled: bool

        :param plugins_config:
            The value to assign to the plugins_config property of this LaunchInstanceAgentConfigDetails.
        :type plugins_config: list[oci.cloud_migrations.models.InstanceAgentPluginConfigDetails]

        """
        self.swagger_types = {
            'is_monitoring_disabled': 'bool',
            'is_management_disabled': 'bool',
            'are_all_plugins_disabled': 'bool',
            'plugins_config': 'list[InstanceAgentPluginConfigDetails]'
        }

        self.attribute_map = {
            'is_monitoring_disabled': 'isMonitoringDisabled',
            'is_management_disabled': 'isManagementDisabled',
            'are_all_plugins_disabled': 'areAllPluginsDisabled',
            'plugins_config': 'pluginsConfig'
        }

        self._is_monitoring_disabled = None
        self._is_management_disabled = None
        self._are_all_plugins_disabled = None
        self._plugins_config = None

    @property
    def is_monitoring_disabled(self):
        """
        Gets the is_monitoring_disabled of this LaunchInstanceAgentConfigDetails.
        Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
        monitoring plugins. By default, the value is false (monitoring plugins are enabled).

        These are the monitoring plugins: Compute instance monitoring
        and Custom logs monitoring.

        The monitoring plugins are controlled by this parameter and by the per-plugin
        configuration in the `pluginsConfig` object.

        - If `isMonitoringDisabled` is true, all the monitoring plugins are disabled, regardless of
        the per-plugin configuration.
        - If `isMonitoringDisabled` is false, all the monitoring plugins are enabled. You
        can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
        object.


        :return: The is_monitoring_disabled of this LaunchInstanceAgentConfigDetails.
        :rtype: bool
        """
        return self._is_monitoring_disabled

    @is_monitoring_disabled.setter
    def is_monitoring_disabled(self, is_monitoring_disabled):
        """
        Sets the is_monitoring_disabled of this LaunchInstanceAgentConfigDetails.
        Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
        monitoring plugins. By default, the value is false (monitoring plugins are enabled).

        These are the monitoring plugins: Compute instance monitoring
        and Custom logs monitoring.

        The monitoring plugins are controlled by this parameter and by the per-plugin
        configuration in the `pluginsConfig` object.

        - If `isMonitoringDisabled` is true, all the monitoring plugins are disabled, regardless of
        the per-plugin configuration.
        - If `isMonitoringDisabled` is false, all the monitoring plugins are enabled. You
        can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
        object.


        :param is_monitoring_disabled: The is_monitoring_disabled of this LaunchInstanceAgentConfigDetails.
        :type: bool
        """
        self._is_monitoring_disabled = is_monitoring_disabled

    @property
    def is_management_disabled(self):
        """
        Gets the is_management_disabled of this LaunchInstanceAgentConfigDetails.
        Whether Oracle Cloud Agent can run all the available management plugins.
        By default, the value is false (management plugins are enabled).

        These are the management plugins: OS Management Service Agent and Compute instance
        run command.

        The management plugins are controlled by this parameter and the per-plugin
        configuration in the `pluginsConfig` object.

        - If `isManagementDisabled` is true, all the management plugins are disabled, regardless of
        the per-plugin configuration.
        - If `isManagementDisabled` is false, all the management plugins are enabled. You
        can optionally disable individual management plugins by providing a value in the `pluginsConfig`
        object.


        :return: The is_management_disabled of this LaunchInstanceAgentConfigDetails.
        :rtype: bool
        """
        return self._is_management_disabled

    @is_management_disabled.setter
    def is_management_disabled(self, is_management_disabled):
        """
        Sets the is_management_disabled of this LaunchInstanceAgentConfigDetails.
        Whether Oracle Cloud Agent can run all the available management plugins.
        By default, the value is false (management plugins are enabled).

        These are the management plugins: OS Management Service Agent and Compute instance
        run command.

        The management plugins are controlled by this parameter and the per-plugin
        configuration in the `pluginsConfig` object.

        - If `isManagementDisabled` is true, all the management plugins are disabled, regardless of
        the per-plugin configuration.
        - If `isManagementDisabled` is false, all the management plugins are enabled. You
        can optionally disable individual management plugins by providing a value in the `pluginsConfig`
        object.


        :param is_management_disabled: The is_management_disabled of this LaunchInstanceAgentConfigDetails.
        :type: bool
        """
        self._is_management_disabled = is_management_disabled

    @property
    def are_all_plugins_disabled(self):
        """
        Gets the are_all_plugins_disabled of this LaunchInstanceAgentConfigDetails.
        Whether Oracle Cloud Agent can run all the available plugins.
        This includes the management and monitoring plugins.

        To get a list of available plugins, use the
        :func:`list_instanceagent_available_plugins`
        operation in the Oracle Cloud Agent API. For more information about the available plugins, see
        `Managing Plugins with Oracle Cloud Agent`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm


        :return: The are_all_plugins_disabled of this LaunchInstanceAgentConfigDetails.
        :rtype: bool
        """
        return self._are_all_plugins_disabled

    @are_all_plugins_disabled.setter
    def are_all_plugins_disabled(self, are_all_plugins_disabled):
        """
        Sets the are_all_plugins_disabled of this LaunchInstanceAgentConfigDetails.
        Whether Oracle Cloud Agent can run all the available plugins.
        This includes the management and monitoring plugins.

        To get a list of available plugins, use the
        :func:`list_instanceagent_available_plugins`
        operation in the Oracle Cloud Agent API. For more information about the available plugins, see
        `Managing Plugins with Oracle Cloud Agent`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm


        :param are_all_plugins_disabled: The are_all_plugins_disabled of this LaunchInstanceAgentConfigDetails.
        :type: bool
        """
        self._are_all_plugins_disabled = are_all_plugins_disabled

    @property
    def plugins_config(self):
        """
        Gets the plugins_config of this LaunchInstanceAgentConfigDetails.
        The configuration of plugins associated with this instance.


        :return: The plugins_config of this LaunchInstanceAgentConfigDetails.
        :rtype: list[oci.cloud_migrations.models.InstanceAgentPluginConfigDetails]
        """
        return self._plugins_config

    @plugins_config.setter
    def plugins_config(self, plugins_config):
        """
        Sets the plugins_config of this LaunchInstanceAgentConfigDetails.
        The configuration of plugins associated with this instance.


        :param plugins_config: The plugins_config of this LaunchInstanceAgentConfigDetails.
        :type: list[oci.cloud_migrations.models.InstanceAgentPluginConfigDetails]
        """
        self._plugins_config = plugins_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
