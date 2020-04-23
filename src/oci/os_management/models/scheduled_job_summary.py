# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledJobSummary(object):
    """
    Basic information about a Scheduled Job
    """

    #: A constant which can be used with the schedule_type property of a ScheduledJobSummary.
    #: This constant has a value of "ONETIME"
    SCHEDULE_TYPE_ONETIME = "ONETIME"

    #: A constant which can be used with the schedule_type property of a ScheduledJobSummary.
    #: This constant has a value of "RECURRING"
    SCHEDULE_TYPE_RECURRING = "RECURRING"

    #: A constant which can be used with the operation_type property of a ScheduledJobSummary.
    #: This constant has a value of "INSTALL"
    OPERATION_TYPE_INSTALL = "INSTALL"

    #: A constant which can be used with the operation_type property of a ScheduledJobSummary.
    #: This constant has a value of "UPDATE"
    OPERATION_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the operation_type property of a ScheduledJobSummary.
    #: This constant has a value of "REMOVE"
    OPERATION_TYPE_REMOVE = "REMOVE"

    #: A constant which can be used with the operation_type property of a ScheduledJobSummary.
    #: This constant has a value of "UPDATEALL"
    OPERATION_TYPE_UPDATEALL = "UPDATEALL"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJobSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJobSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJobSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJobSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJobSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJobSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the os_family property of a ScheduledJobSummary.
    #: This constant has a value of "LINUX"
    OS_FAMILY_LINUX = "LINUX"

    #: A constant which can be used with the os_family property of a ScheduledJobSummary.
    #: This constant has a value of "WINDOWS"
    OS_FAMILY_WINDOWS = "WINDOWS"

    #: A constant which can be used with the os_family property of a ScheduledJobSummary.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledJobSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScheduledJobSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ScheduledJobSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ScheduledJobSummary.
        :type compartment_id: str

        :param schedule_type:
            The value to assign to the schedule_type property of this ScheduledJobSummary.
            Allowed values for this property are: "ONETIME", "RECURRING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type schedule_type: str

        :param time_next_execution:
            The value to assign to the time_next_execution property of this ScheduledJobSummary.
        :type time_next_execution: datetime

        :param time_last_execution:
            The value to assign to the time_last_execution property of this ScheduledJobSummary.
        :type time_last_execution: datetime

        :param managed_instances:
            The value to assign to the managed_instances property of this ScheduledJobSummary.
        :type managed_instances: list[Id]

        :param managed_instance_groups:
            The value to assign to the managed_instance_groups property of this ScheduledJobSummary.
        :type managed_instance_groups: list[Id]

        :param operation_type:
            The value to assign to the operation_type property of this ScheduledJobSummary.
            Allowed values for this property are: "INSTALL", "UPDATE", "REMOVE", "UPDATEALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduledJobSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScheduledJobSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScheduledJobSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param os_family:
            The value to assign to the os_family property of this ScheduledJobSummary.
            Allowed values for this property are: "LINUX", "WINDOWS", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'schedule_type': 'str',
            'time_next_execution': 'datetime',
            'time_last_execution': 'datetime',
            'managed_instances': 'list[Id]',
            'managed_instance_groups': 'list[Id]',
            'operation_type': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'os_family': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'schedule_type': 'scheduleType',
            'time_next_execution': 'timeNextExecution',
            'time_last_execution': 'timeLastExecution',
            'managed_instances': 'managedInstances',
            'managed_instance_groups': 'managedInstanceGroups',
            'operation_type': 'operationType',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'os_family': 'osFamily'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._schedule_type = None
        self._time_next_execution = None
        self._time_last_execution = None
        self._managed_instances = None
        self._managed_instance_groups = None
        self._operation_type = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._os_family = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduledJobSummary.
        OCID for the Scheduled Job


        :return: The id of this ScheduledJobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledJobSummary.
        OCID for the Scheduled Job


        :param id: The id of this ScheduledJobSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScheduledJobSummary.
        Scheduled Job name


        :return: The display_name of this ScheduledJobSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScheduledJobSummary.
        Scheduled Job name


        :param display_name: The display_name of this ScheduledJobSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ScheduledJobSummary.
        OCID for the Compartment


        :return: The compartment_id of this ScheduledJobSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ScheduledJobSummary.
        OCID for the Compartment


        :param compartment_id: The compartment_id of this ScheduledJobSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def schedule_type(self):
        """
        Gets the schedule_type of this ScheduledJobSummary.
        the type of scheduling this Scheduled Job follows

        Allowed values for this property are: "ONETIME", "RECURRING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The schedule_type of this ScheduledJobSummary.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this ScheduledJobSummary.
        the type of scheduling this Scheduled Job follows


        :param schedule_type: The schedule_type of this ScheduledJobSummary.
        :type: str
        """
        allowed_values = ["ONETIME", "RECURRING"]
        if not value_allowed_none_or_none_sentinel(schedule_type, allowed_values):
            schedule_type = 'UNKNOWN_ENUM_VALUE'
        self._schedule_type = schedule_type

    @property
    def time_next_execution(self):
        """
        Gets the time_next_execution of this ScheduledJobSummary.
        the time/date of the next scheduled execution of this Scheduled Job


        :return: The time_next_execution of this ScheduledJobSummary.
        :rtype: datetime
        """
        return self._time_next_execution

    @time_next_execution.setter
    def time_next_execution(self, time_next_execution):
        """
        Sets the time_next_execution of this ScheduledJobSummary.
        the time/date of the next scheduled execution of this Scheduled Job


        :param time_next_execution: The time_next_execution of this ScheduledJobSummary.
        :type: datetime
        """
        self._time_next_execution = time_next_execution

    @property
    def time_last_execution(self):
        """
        Gets the time_last_execution of this ScheduledJobSummary.
        the time/date of the last execution of this Scheduled Job


        :return: The time_last_execution of this ScheduledJobSummary.
        :rtype: datetime
        """
        return self._time_last_execution

    @time_last_execution.setter
    def time_last_execution(self, time_last_execution):
        """
        Sets the time_last_execution of this ScheduledJobSummary.
        the time/date of the last execution of this Scheduled Job


        :param time_last_execution: The time_last_execution of this ScheduledJobSummary.
        :type: datetime
        """
        self._time_last_execution = time_last_execution

    @property
    def managed_instances(self):
        """
        Gets the managed_instances of this ScheduledJobSummary.
        the list of managed instances this scheduled job operates on (mutually exclusive with managedInstanceGroups)


        :return: The managed_instances of this ScheduledJobSummary.
        :rtype: list[Id]
        """
        return self._managed_instances

    @managed_instances.setter
    def managed_instances(self, managed_instances):
        """
        Sets the managed_instances of this ScheduledJobSummary.
        the list of managed instances this scheduled job operates on (mutually exclusive with managedInstanceGroups)


        :param managed_instances: The managed_instances of this ScheduledJobSummary.
        :type: list[Id]
        """
        self._managed_instances = managed_instances

    @property
    def managed_instance_groups(self):
        """
        Gets the managed_instance_groups of this ScheduledJobSummary.
        the list of managed instance groups this scheduled job operates on (mutually exclusive with managedInstances)


        :return: The managed_instance_groups of this ScheduledJobSummary.
        :rtype: list[Id]
        """
        return self._managed_instance_groups

    @managed_instance_groups.setter
    def managed_instance_groups(self, managed_instance_groups):
        """
        Sets the managed_instance_groups of this ScheduledJobSummary.
        the list of managed instance groups this scheduled job operates on (mutually exclusive with managedInstances)


        :param managed_instance_groups: The managed_instance_groups of this ScheduledJobSummary.
        :type: list[Id]
        """
        self._managed_instance_groups = managed_instance_groups

    @property
    def operation_type(self):
        """
        Gets the operation_type of this ScheduledJobSummary.
        the type of operation this Scheduled Job performs

        Allowed values for this property are: "INSTALL", "UPDATE", "REMOVE", "UPDATEALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this ScheduledJobSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this ScheduledJobSummary.
        the type of operation this Scheduled Job performs


        :param operation_type: The operation_type of this ScheduledJobSummary.
        :type: str
        """
        allowed_values = ["INSTALL", "UPDATE", "REMOVE", "UPDATEALL"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ScheduledJobSummary.
        The current state of the Scheduled Job.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ScheduledJobSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduledJobSummary.
        The current state of the Scheduled Job.


        :param lifecycle_state: The lifecycle_state of this ScheduledJobSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ScheduledJobSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ScheduledJobSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScheduledJobSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ScheduledJobSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ScheduledJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ScheduledJobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScheduledJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ScheduledJobSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def os_family(self):
        """
        Gets the os_family of this ScheduledJobSummary.
        The Operating System type of the managed instance.

        Allowed values for this property are: "LINUX", "WINDOWS", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this ScheduledJobSummary.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this ScheduledJobSummary.
        The Operating System type of the managed instance.


        :param os_family: The os_family of this ScheduledJobSummary.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
