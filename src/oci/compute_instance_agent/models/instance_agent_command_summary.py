# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandSummary(object):
    """
    command summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_agent_command_id:
            The value to assign to the instance_agent_command_id property of this InstanceAgentCommandSummary.
        :type instance_agent_command_id: str

        :param display_name:
            The value to assign to the display_name property of this InstanceAgentCommandSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceAgentCommandSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this InstanceAgentCommandSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this InstanceAgentCommandSummary.
        :type time_updated: datetime

        :param is_canceled:
            The value to assign to the is_canceled property of this InstanceAgentCommandSummary.
        :type is_canceled: bool

        """
        self.swagger_types = {
            'instance_agent_command_id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'is_canceled': 'bool'
        }

        self.attribute_map = {
            'instance_agent_command_id': 'instanceAgentCommandId',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'is_canceled': 'isCanceled'
        }

        self._instance_agent_command_id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._is_canceled = None

    @property
    def instance_agent_command_id(self):
        """
        **[Required]** Gets the instance_agent_command_id of this InstanceAgentCommandSummary.
        The command OCID


        :return: The instance_agent_command_id of this InstanceAgentCommandSummary.
        :rtype: str
        """
        return self._instance_agent_command_id

    @instance_agent_command_id.setter
    def instance_agent_command_id(self, instance_agent_command_id):
        """
        Sets the instance_agent_command_id of this InstanceAgentCommandSummary.
        The command OCID


        :param instance_agent_command_id: The instance_agent_command_id of this InstanceAgentCommandSummary.
        :type: str
        """
        self._instance_agent_command_id = instance_agent_command_id

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceAgentCommandSummary.
        The user friendly display name of the command.


        :return: The display_name of this InstanceAgentCommandSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceAgentCommandSummary.
        The user friendly display name of the command.


        :param display_name: The display_name of this InstanceAgentCommandSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InstanceAgentCommandSummary.
        The OCID of the compartment the command is created in.


        :return: The compartment_id of this InstanceAgentCommandSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstanceAgentCommandSummary.
        The OCID of the compartment the command is created in.


        :param compartment_id: The compartment_id of this InstanceAgentCommandSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this InstanceAgentCommandSummary.
        The command creation date


        :return: The time_created of this InstanceAgentCommandSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstanceAgentCommandSummary.
        The command creation date


        :param time_created: The time_created of this InstanceAgentCommandSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this InstanceAgentCommandSummary.
        The command last updated at date.


        :return: The time_updated of this InstanceAgentCommandSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this InstanceAgentCommandSummary.
        The command last updated at date.


        :param time_updated: The time_updated of this InstanceAgentCommandSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def is_canceled(self):
        """
        Gets the is_canceled of this InstanceAgentCommandSummary.
        Set to true, if the command has been canceled.


        :return: The is_canceled of this InstanceAgentCommandSummary.
        :rtype: bool
        """
        return self._is_canceled

    @is_canceled.setter
    def is_canceled(self, is_canceled):
        """
        Sets the is_canceled of this InstanceAgentCommandSummary.
        Set to true, if the command has been canceled.


        :param is_canceled: The is_canceled of this InstanceAgentCommandSummary.
        :type: bool
        """
        self._is_canceled = is_canceled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
