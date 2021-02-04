# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentPluginConfigDetails(object):
    """
    The configuration of plugins associated with this instance.
    """

    #: A constant which can be used with the desired_state property of a InstanceAgentPluginConfigDetails.
    #: This constant has a value of "ENABLED"
    DESIRED_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the desired_state property of a InstanceAgentPluginConfigDetails.
    #: This constant has a value of "DISABLED"
    DESIRED_STATE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentPluginConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this InstanceAgentPluginConfigDetails.
        :type name: str

        :param desired_state:
            The value to assign to the desired_state property of this InstanceAgentPluginConfigDetails.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type desired_state: str

        """
        self.swagger_types = {
            'name': 'str',
            'desired_state': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'desired_state': 'desiredState'
        }

        self._name = None
        self._desired_state = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this InstanceAgentPluginConfigDetails.
        The plugin name. To get a list of available plugins, use the
        :func:`list_instanceagent_available_plugins`
        operation in the Oracle Cloud Agent API. For more information about the available plugins, see
        `Managing Plugins with Oracle Cloud Agent`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm


        :return: The name of this InstanceAgentPluginConfigDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InstanceAgentPluginConfigDetails.
        The plugin name. To get a list of available plugins, use the
        :func:`list_instanceagent_available_plugins`
        operation in the Oracle Cloud Agent API. For more information about the available plugins, see
        `Managing Plugins with Oracle Cloud Agent`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm


        :param name: The name of this InstanceAgentPluginConfigDetails.
        :type: str
        """
        self._name = name

    @property
    def desired_state(self):
        """
        **[Required]** Gets the desired_state of this InstanceAgentPluginConfigDetails.
        Whether the plugin should be enabled or disabled.

        To enable the monitoring and management plugins, the `isMonitoringDisabled` and
        `isManagementDisabled` attributes must also be set to false.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The desired_state of this InstanceAgentPluginConfigDetails.
        :rtype: str
        """
        return self._desired_state

    @desired_state.setter
    def desired_state(self, desired_state):
        """
        Sets the desired_state of this InstanceAgentPluginConfigDetails.
        Whether the plugin should be enabled or disabled.

        To enable the monitoring and management plugins, the `isMonitoringDisabled` and
        `isManagementDisabled` attributes must also be set to false.


        :param desired_state: The desired_state of this InstanceAgentPluginConfigDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(desired_state, allowed_values):
            desired_state = 'UNKNOWN_ENUM_VALUE'
        self._desired_state = desired_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
