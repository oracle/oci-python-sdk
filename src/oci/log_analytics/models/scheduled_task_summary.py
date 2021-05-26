# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledTaskSummary(object):
    """
    Summary information about a scheduled task.
    """

    #: A constant which can be used with the task_type property of a ScheduledTaskSummary.
    #: This constant has a value of "SAVED_SEARCH"
    TASK_TYPE_SAVED_SEARCH = "SAVED_SEARCH"

    #: A constant which can be used with the task_type property of a ScheduledTaskSummary.
    #: This constant has a value of "ACCELERATION"
    TASK_TYPE_ACCELERATION = "ACCELERATION"

    #: A constant which can be used with the task_type property of a ScheduledTaskSummary.
    #: This constant has a value of "PURGE"
    TASK_TYPE_PURGE = "PURGE"

    #: A constant which can be used with the task_type property of a ScheduledTaskSummary.
    #: This constant has a value of "ACCELERATION_MAINTENANCE"
    TASK_TYPE_ACCELERATION_MAINTENANCE = "ACCELERATION_MAINTENANCE"

    #: A constant which can be used with the task_status property of a ScheduledTaskSummary.
    #: This constant has a value of "READY"
    TASK_STATUS_READY = "READY"

    #: A constant which can be used with the task_status property of a ScheduledTaskSummary.
    #: This constant has a value of "PAUSED"
    TASK_STATUS_PAUSED = "PAUSED"

    #: A constant which can be used with the task_status property of a ScheduledTaskSummary.
    #: This constant has a value of "COMPLETED"
    TASK_STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the task_status property of a ScheduledTaskSummary.
    #: This constant has a value of "BLOCKED"
    TASK_STATUS_BLOCKED = "BLOCKED"

    #: A constant which can be used with the last_execution_status property of a ScheduledTaskSummary.
    #: This constant has a value of "FAILED"
    LAST_EXECUTION_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the last_execution_status property of a ScheduledTaskSummary.
    #: This constant has a value of "SUCCEEDED"
    LAST_EXECUTION_STATUS_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledTaskSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScheduledTaskSummary.
        :type id: str

        :param task_type:
            The value to assign to the task_type property of this ScheduledTaskSummary.
            Allowed values for this property are: "SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ScheduledTaskSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ScheduledTaskSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ScheduledTaskSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduledTaskSummary.
        :type lifecycle_state: str

        :param task_status:
            The value to assign to the task_status property of this ScheduledTaskSummary.
            Allowed values for this property are: "READY", "PAUSED", "COMPLETED", "BLOCKED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_status: str

        :param pause_reason:
            The value to assign to the pause_reason property of this ScheduledTaskSummary.
        :type pause_reason: str

        :param work_request_id:
            The value to assign to the work_request_id property of this ScheduledTaskSummary.
        :type work_request_id: str

        :param display_name:
            The value to assign to the display_name property of this ScheduledTaskSummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScheduledTaskSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScheduledTaskSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param last_execution_status:
            The value to assign to the last_execution_status property of this ScheduledTaskSummary.
            Allowed values for this property are: "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type last_execution_status: str

        :param time_last_executed:
            The value to assign to the time_last_executed property of this ScheduledTaskSummary.
        :type time_last_executed: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'task_type': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'task_status': 'str',
            'pause_reason': 'str',
            'work_request_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'last_execution_status': 'str',
            'time_last_executed': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'task_type': 'taskType',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'task_status': 'taskStatus',
            'pause_reason': 'pauseReason',
            'work_request_id': 'workRequestId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'last_execution_status': 'lastExecutionStatus',
            'time_last_executed': 'timeLastExecuted'
        }

        self._id = None
        self._task_type = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._task_status = None
        self._pause_reason = None
        self._work_request_id = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._last_execution_status = None
        self._time_last_executed = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduledTaskSummary.
        The `OCID`__ of the data plane resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ScheduledTaskSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledTaskSummary.
        The `OCID`__ of the data plane resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ScheduledTaskSummary.
        :type: str
        """
        self._id = id

    @property
    def task_type(self):
        """
        **[Required]** Gets the task_type of this ScheduledTaskSummary.
        Task type.

        Allowed values for this property are: "SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The task_type of this ScheduledTaskSummary.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """
        Sets the task_type of this ScheduledTaskSummary.
        Task type.


        :param task_type: The task_type of this ScheduledTaskSummary.
        :type: str
        """
        allowed_values = ["SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE"]
        if not value_allowed_none_or_none_sentinel(task_type, allowed_values):
            task_type = 'UNKNOWN_ENUM_VALUE'
        self._task_type = task_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ScheduledTaskSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ScheduledTaskSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ScheduledTaskSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ScheduledTaskSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ScheduledTaskSummary.
        The date and time the schedule task was created, in the format defined by RFC3339.


        :return: The time_created of this ScheduledTaskSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ScheduledTaskSummary.
        The date and time the schedule task was created, in the format defined by RFC3339.


        :param time_created: The time_created of this ScheduledTaskSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ScheduledTaskSummary.
        The date and time the scheduled task was last updated, in the format defined by RFC3339.


        :return: The time_updated of this ScheduledTaskSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ScheduledTaskSummary.
        The date and time the scheduled task was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this ScheduledTaskSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ScheduledTaskSummary.
        The current state of the scheduled task.


        :return: The lifecycle_state of this ScheduledTaskSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduledTaskSummary.
        The current state of the scheduled task.


        :param lifecycle_state: The lifecycle_state of this ScheduledTaskSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def task_status(self):
        """
        Gets the task_status of this ScheduledTaskSummary.
        Status of the scheduled task.

        Allowed values for this property are: "READY", "PAUSED", "COMPLETED", "BLOCKED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The task_status of this ScheduledTaskSummary.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """
        Sets the task_status of this ScheduledTaskSummary.
        Status of the scheduled task.


        :param task_status: The task_status of this ScheduledTaskSummary.
        :type: str
        """
        allowed_values = ["READY", "PAUSED", "COMPLETED", "BLOCKED"]
        if not value_allowed_none_or_none_sentinel(task_status, allowed_values):
            task_status = 'UNKNOWN_ENUM_VALUE'
        self._task_status = task_status

    @property
    def pause_reason(self):
        """
        Gets the pause_reason of this ScheduledTaskSummary.
        reason for taskStatus PAUSED.


        :return: The pause_reason of this ScheduledTaskSummary.
        :rtype: str
        """
        return self._pause_reason

    @pause_reason.setter
    def pause_reason(self, pause_reason):
        """
        Sets the pause_reason of this ScheduledTaskSummary.
        reason for taskStatus PAUSED.


        :param pause_reason: The pause_reason of this ScheduledTaskSummary.
        :type: str
        """
        self._pause_reason = pause_reason

    @property
    def work_request_id(self):
        """
        Gets the work_request_id of this ScheduledTaskSummary.
        most recent Work Request Identifier `OCID]`__ for the asynchronous request.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The work_request_id of this ScheduledTaskSummary.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this ScheduledTaskSummary.
        most recent Work Request Identifier `OCID]`__ for the asynchronous request.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param work_request_id: The work_request_id of this ScheduledTaskSummary.
        :type: str
        """
        self._work_request_id = work_request_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScheduledTaskSummary.
        A user-friendly name that is changeable and that does not have to be unique.
        Format: a leading alphanumeric, followed by zero or more
        alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
        No trailing spaces allowed.


        :return: The display_name of this ScheduledTaskSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScheduledTaskSummary.
        A user-friendly name that is changeable and that does not have to be unique.
        Format: a leading alphanumeric, followed by zero or more
        alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
        No trailing spaces allowed.


        :param display_name: The display_name of this ScheduledTaskSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ScheduledTaskSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ScheduledTaskSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScheduledTaskSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ScheduledTaskSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ScheduledTaskSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ScheduledTaskSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScheduledTaskSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ScheduledTaskSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def last_execution_status(self):
        """
        Gets the last_execution_status of this ScheduledTaskSummary.
        The most recent task execution status.

        Allowed values for this property are: "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_execution_status of this ScheduledTaskSummary.
        :rtype: str
        """
        return self._last_execution_status

    @last_execution_status.setter
    def last_execution_status(self, last_execution_status):
        """
        Sets the last_execution_status of this ScheduledTaskSummary.
        The most recent task execution status.


        :param last_execution_status: The last_execution_status of this ScheduledTaskSummary.
        :type: str
        """
        allowed_values = ["FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(last_execution_status, allowed_values):
            last_execution_status = 'UNKNOWN_ENUM_VALUE'
        self._last_execution_status = last_execution_status

    @property
    def time_last_executed(self):
        """
        Gets the time_last_executed of this ScheduledTaskSummary.
        The date and time the scheduled task last executed, in the format defined by RFC3339.


        :return: The time_last_executed of this ScheduledTaskSummary.
        :rtype: datetime
        """
        return self._time_last_executed

    @time_last_executed.setter
    def time_last_executed(self, time_last_executed):
        """
        Sets the time_last_executed of this ScheduledTaskSummary.
        The date and time the scheduled task last executed, in the format defined by RFC3339.


        :param time_last_executed: The time_last_executed of this ScheduledTaskSummary.
        :type: datetime
        """
        self._time_last_executed = time_last_executed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
