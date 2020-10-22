# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommand(object):
    """
    The command payload.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommand object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InstanceAgentCommand.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceAgentCommand.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this InstanceAgentCommand.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this InstanceAgentCommand.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this InstanceAgentCommand.
        :type time_updated: datetime

        :param is_canceled:
            The value to assign to the is_canceled property of this InstanceAgentCommand.
        :type is_canceled: bool

        :param execution_time_out_in_seconds:
            The value to assign to the execution_time_out_in_seconds property of this InstanceAgentCommand.
        :type execution_time_out_in_seconds: int

        :param target:
            The value to assign to the target property of this InstanceAgentCommand.
        :type target: InstanceAgentCommandTarget

        :param content:
            The value to assign to the content property of this InstanceAgentCommand.
        :type content: InstanceAgentCommandContent

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'is_canceled': 'bool',
            'execution_time_out_in_seconds': 'int',
            'target': 'InstanceAgentCommandTarget',
            'content': 'InstanceAgentCommandContent'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'is_canceled': 'isCanceled',
            'execution_time_out_in_seconds': 'executionTimeOutInSeconds',
            'target': 'target',
            'content': 'content'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._is_canceled = None
        self._execution_time_out_in_seconds = None
        self._target = None
        self._content = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InstanceAgentCommand.
        The command OCID


        :return: The id of this InstanceAgentCommand.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceAgentCommand.
        The command OCID


        :param id: The id of this InstanceAgentCommand.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InstanceAgentCommand.
        The OCID of the compartment the command is created in.


        :return: The compartment_id of this InstanceAgentCommand.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstanceAgentCommand.
        The OCID of the compartment the command is created in.


        :param compartment_id: The compartment_id of this InstanceAgentCommand.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceAgentCommand.
        The user friendly display name of the command.


        :return: The display_name of this InstanceAgentCommand.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceAgentCommand.
        The user friendly display name of the command.


        :param display_name: The display_name of this InstanceAgentCommand.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this InstanceAgentCommand.
        the time command was created at.


        :return: The time_created of this InstanceAgentCommand.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstanceAgentCommand.
        the time command was created at.


        :param time_created: The time_created of this InstanceAgentCommand.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this InstanceAgentCommand.
        the time command was updated at.


        :return: The time_updated of this InstanceAgentCommand.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this InstanceAgentCommand.
        the time command was updated at.


        :param time_updated: The time_updated of this InstanceAgentCommand.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def is_canceled(self):
        """
        Gets the is_canceled of this InstanceAgentCommand.
        Whether the command has been requested to be canceled.


        :return: The is_canceled of this InstanceAgentCommand.
        :rtype: bool
        """
        return self._is_canceled

    @is_canceled.setter
    def is_canceled(self, is_canceled):
        """
        Sets the is_canceled of this InstanceAgentCommand.
        Whether the command has been requested to be canceled.


        :param is_canceled: The is_canceled of this InstanceAgentCommand.
        :type: bool
        """
        self._is_canceled = is_canceled

    @property
    def execution_time_out_in_seconds(self):
        """
        Gets the execution_time_out_in_seconds of this InstanceAgentCommand.
        Command execution time limit that the instance agent will honor when executing the command inside the instance. This timer starts when the instance agent starts the commond. Zero means no timeout.


        :return: The execution_time_out_in_seconds of this InstanceAgentCommand.
        :rtype: int
        """
        return self._execution_time_out_in_seconds

    @execution_time_out_in_seconds.setter
    def execution_time_out_in_seconds(self, execution_time_out_in_seconds):
        """
        Sets the execution_time_out_in_seconds of this InstanceAgentCommand.
        Command execution time limit that the instance agent will honor when executing the command inside the instance. This timer starts when the instance agent starts the commond. Zero means no timeout.


        :param execution_time_out_in_seconds: The execution_time_out_in_seconds of this InstanceAgentCommand.
        :type: int
        """
        self._execution_time_out_in_seconds = execution_time_out_in_seconds

    @property
    def target(self):
        """
        **[Required]** Gets the target of this InstanceAgentCommand.

        :return: The target of this InstanceAgentCommand.
        :rtype: InstanceAgentCommandTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this InstanceAgentCommand.

        :param target: The target of this InstanceAgentCommand.
        :type: InstanceAgentCommandTarget
        """
        self._target = target

    @property
    def content(self):
        """
        **[Required]** Gets the content of this InstanceAgentCommand.

        :return: The content of this InstanceAgentCommand.
        :rtype: InstanceAgentCommandContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this InstanceAgentCommand.

        :param content: The content of this InstanceAgentCommand.
        :type: InstanceAgentCommandContent
        """
        self._content = content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
