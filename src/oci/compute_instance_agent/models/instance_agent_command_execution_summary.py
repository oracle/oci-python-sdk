# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandExecutionSummary(object):
    """
    Execution details for a command.
    """

    #: A constant which can be used with the delivery_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "VISIBLE"
    DELIVERY_STATE_VISIBLE = "VISIBLE"

    #: A constant which can be used with the delivery_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "PENDING"
    DELIVERY_STATE_PENDING = "PENDING"

    #: A constant which can be used with the delivery_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "ACKED"
    DELIVERY_STATE_ACKED = "ACKED"

    #: A constant which can be used with the delivery_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "ACKED_CANCELED"
    DELIVERY_STATE_ACKED_CANCELED = "ACKED_CANCELED"

    #: A constant which can be used with the delivery_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "EXPIRED"
    DELIVERY_STATE_EXPIRED = "EXPIRED"

    #: A constant which can be used with the lifecycle_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "TIMED_OUT"
    LIFECYCLE_STATE_TIMED_OUT = "TIMED_OUT"

    #: A constant which can be used with the lifecycle_state property of a InstanceAgentCommandExecutionSummary.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandExecutionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_agent_command_id:
            The value to assign to the instance_agent_command_id property of this InstanceAgentCommandExecutionSummary.
        :type instance_agent_command_id: str

        :param instance_id:
            The value to assign to the instance_id property of this InstanceAgentCommandExecutionSummary.
        :type instance_id: str

        :param delivery_state:
            The value to assign to the delivery_state property of this InstanceAgentCommandExecutionSummary.
            Allowed values for this property are: "VISIBLE", "PENDING", "ACKED", "ACKED_CANCELED", "EXPIRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type delivery_state: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InstanceAgentCommandExecutionSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "TIMED_OUT", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this InstanceAgentCommandExecutionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this InstanceAgentCommandExecutionSummary.
        :type time_updated: datetime

        :param sequence_number:
            The value to assign to the sequence_number property of this InstanceAgentCommandExecutionSummary.
        :type sequence_number: int

        :param display_name:
            The value to assign to the display_name property of this InstanceAgentCommandExecutionSummary.
        :type display_name: str

        :param content:
            The value to assign to the content property of this InstanceAgentCommandExecutionSummary.
        :type content: oci.compute_instance_agent.models.InstanceAgentCommandExecutionOutputContent

        """
        self.swagger_types = {
            'instance_agent_command_id': 'str',
            'instance_id': 'str',
            'delivery_state': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'sequence_number': 'int',
            'display_name': 'str',
            'content': 'InstanceAgentCommandExecutionOutputContent'
        }

        self.attribute_map = {
            'instance_agent_command_id': 'instanceAgentCommandId',
            'instance_id': 'instanceId',
            'delivery_state': 'deliveryState',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'sequence_number': 'sequenceNumber',
            'display_name': 'displayName',
            'content': 'content'
        }

        self._instance_agent_command_id = None
        self._instance_id = None
        self._delivery_state = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._sequence_number = None
        self._display_name = None
        self._content = None

    @property
    def instance_agent_command_id(self):
        """
        **[Required]** Gets the instance_agent_command_id of this InstanceAgentCommandExecutionSummary.
        The `OCID`__ of the command.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The instance_agent_command_id of this InstanceAgentCommandExecutionSummary.
        :rtype: str
        """
        return self._instance_agent_command_id

    @instance_agent_command_id.setter
    def instance_agent_command_id(self, instance_agent_command_id):
        """
        Sets the instance_agent_command_id of this InstanceAgentCommandExecutionSummary.
        The `OCID`__ of the command.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param instance_agent_command_id: The instance_agent_command_id of this InstanceAgentCommandExecutionSummary.
        :type: str
        """
        self._instance_agent_command_id = instance_agent_command_id

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this InstanceAgentCommandExecutionSummary.
        The `OCID`__ of the instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The instance_id of this InstanceAgentCommandExecutionSummary.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this InstanceAgentCommandExecutionSummary.
        The `OCID`__ of the instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param instance_id: The instance_id of this InstanceAgentCommandExecutionSummary.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def delivery_state(self):
        """
        **[Required]** Gets the delivery_state of this InstanceAgentCommandExecutionSummary.
        The command delivery state.
         * `VISIBLE` - The command is visible to the instance.
         * `PENDING` - The command is pending acknowledgment from the instance.
         * `ACKED` - The command has been received and acknowledged by the instance.
         * `ACKED_CANCELED` - The canceled command has been received and acknowledged by the instance.
         * `EXPIRED` - The instance has not requested for commands and the command's delivery has expired.

        Allowed values for this property are: "VISIBLE", "PENDING", "ACKED", "ACKED_CANCELED", "EXPIRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The delivery_state of this InstanceAgentCommandExecutionSummary.
        :rtype: str
        """
        return self._delivery_state

    @delivery_state.setter
    def delivery_state(self, delivery_state):
        """
        Sets the delivery_state of this InstanceAgentCommandExecutionSummary.
        The command delivery state.
         * `VISIBLE` - The command is visible to the instance.
         * `PENDING` - The command is pending acknowledgment from the instance.
         * `ACKED` - The command has been received and acknowledged by the instance.
         * `ACKED_CANCELED` - The canceled command has been received and acknowledged by the instance.
         * `EXPIRED` - The instance has not requested for commands and the command's delivery has expired.


        :param delivery_state: The delivery_state of this InstanceAgentCommandExecutionSummary.
        :type: str
        """
        allowed_values = ["VISIBLE", "PENDING", "ACKED", "ACKED_CANCELED", "EXPIRED"]
        if not value_allowed_none_or_none_sentinel(delivery_state, allowed_values):
            delivery_state = 'UNKNOWN_ENUM_VALUE'
        self._delivery_state = delivery_state

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this InstanceAgentCommandExecutionSummary.
        The command execution lifecycle state.
        * `ACCEPTED` - The command has been accepted to run.
        * `IN_PROGRESS` - The command is in progress.
        * `SUCCEEDED` - The command was successfully executed.
        * `FAILED` - The command failed to execute.
        * `TIMED_OUT` - The command execution timed out.
        * `CANCELED` - The command execution was canceled.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "TIMED_OUT", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InstanceAgentCommandExecutionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InstanceAgentCommandExecutionSummary.
        The command execution lifecycle state.
        * `ACCEPTED` - The command has been accepted to run.
        * `IN_PROGRESS` - The command is in progress.
        * `SUCCEEDED` - The command was successfully executed.
        * `FAILED` - The command failed to execute.
        * `TIMED_OUT` - The command execution timed out.
        * `CANCELED` - The command execution was canceled.


        :param lifecycle_state: The lifecycle_state of this InstanceAgentCommandExecutionSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "TIMED_OUT", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this InstanceAgentCommandExecutionSummary.
        The date and time the command was created, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this InstanceAgentCommandExecutionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstanceAgentCommandExecutionSummary.
        The date and time the command was created, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this InstanceAgentCommandExecutionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this InstanceAgentCommandExecutionSummary.
        The date and time the command was last updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this InstanceAgentCommandExecutionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this InstanceAgentCommandExecutionSummary.
        The date and time the command was last updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this InstanceAgentCommandExecutionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def sequence_number(self):
        """
        **[Required]** Gets the sequence_number of this InstanceAgentCommandExecutionSummary.
        A large, non-consecutive number that Oracle Cloud Agent assigns to each created command.


        :return: The sequence_number of this InstanceAgentCommandExecutionSummary.
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """
        Sets the sequence_number of this InstanceAgentCommandExecutionSummary.
        A large, non-consecutive number that Oracle Cloud Agent assigns to each created command.


        :param sequence_number: The sequence_number of this InstanceAgentCommandExecutionSummary.
        :type: int
        """
        self._sequence_number = sequence_number

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceAgentCommandExecutionSummary.
        A user-friendly name. Does not have to be unique.


        :return: The display_name of this InstanceAgentCommandExecutionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceAgentCommandExecutionSummary.
        A user-friendly name. Does not have to be unique.


        :param display_name: The display_name of this InstanceAgentCommandExecutionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def content(self):
        """
        **[Required]** Gets the content of this InstanceAgentCommandExecutionSummary.
        The execution output from a command.


        :return: The content of this InstanceAgentCommandExecutionSummary.
        :rtype: oci.compute_instance_agent.models.InstanceAgentCommandExecutionOutputContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this InstanceAgentCommandExecutionSummary.
        The execution output from a command.


        :param content: The content of this InstanceAgentCommandExecutionSummary.
        :type: oci.compute_instance_agent.models.InstanceAgentCommandExecutionOutputContent
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
