# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .scheduled_task import ScheduledTask
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StandardTask(ScheduledTask):
    """
    Log analytics scheduled task resource.
    """

    #: A constant which can be used with the last_execution_status property of a StandardTask.
    #: This constant has a value of "FAILED"
    LAST_EXECUTION_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the last_execution_status property of a StandardTask.
    #: This constant has a value of "SUCCEEDED"
    LAST_EXECUTION_STATUS_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new StandardTask object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.StandardTask.kind` attribute
        of this class is ``STANDARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this StandardTask.
            Allowed values for this property are: "ACCELERATION", "STANDARD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param id:
            The value to assign to the id property of this StandardTask.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this StandardTask.
        :type display_name: str

        :param task_type:
            The value to assign to the task_type property of this StandardTask.
            Allowed values for this property are: "SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_type: str

        :param schedules:
            The value to assign to the schedules property of this StandardTask.
        :type schedules: list[oci.log_analytics.models.Schedule]

        :param action:
            The value to assign to the action property of this StandardTask.
        :type action: oci.log_analytics.models.Action

        :param task_status:
            The value to assign to the task_status property of this StandardTask.
            Allowed values for this property are: "READY", "PAUSED", "COMPLETED", "BLOCKED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_status: str

        :param work_request_id:
            The value to assign to the work_request_id property of this StandardTask.
        :type work_request_id: str

        :param num_occurrences:
            The value to assign to the num_occurrences property of this StandardTask.
        :type num_occurrences: int

        :param compartment_id:
            The value to assign to the compartment_id property of this StandardTask.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this StandardTask.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this StandardTask.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this StandardTask.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this StandardTask.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this StandardTask.
        :type defined_tags: dict(str, dict(str, object))

        :param last_execution_status:
            The value to assign to the last_execution_status property of this StandardTask.
            Allowed values for this property are: "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type last_execution_status: str

        :param time_last_executed:
            The value to assign to the time_last_executed property of this StandardTask.
        :type time_last_executed: datetime

        """
        self.swagger_types = {
            'kind': 'str',
            'id': 'str',
            'display_name': 'str',
            'task_type': 'str',
            'schedules': 'list[Schedule]',
            'action': 'Action',
            'task_status': 'str',
            'work_request_id': 'str',
            'num_occurrences': 'int',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'last_execution_status': 'str',
            'time_last_executed': 'datetime'
        }

        self.attribute_map = {
            'kind': 'kind',
            'id': 'id',
            'display_name': 'displayName',
            'task_type': 'taskType',
            'schedules': 'schedules',
            'action': 'action',
            'task_status': 'taskStatus',
            'work_request_id': 'workRequestId',
            'num_occurrences': 'numOccurrences',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'last_execution_status': 'lastExecutionStatus',
            'time_last_executed': 'timeLastExecuted'
        }

        self._kind = None
        self._id = None
        self._display_name = None
        self._task_type = None
        self._schedules = None
        self._action = None
        self._task_status = None
        self._work_request_id = None
        self._num_occurrences = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._last_execution_status = None
        self._time_last_executed = None
        self._kind = 'STANDARD'

    @property
    def last_execution_status(self):
        """
        Gets the last_execution_status of this StandardTask.
        The most recent task execution status.

        Allowed values for this property are: "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_execution_status of this StandardTask.
        :rtype: str
        """
        return self._last_execution_status

    @last_execution_status.setter
    def last_execution_status(self, last_execution_status):
        """
        Sets the last_execution_status of this StandardTask.
        The most recent task execution status.


        :param last_execution_status: The last_execution_status of this StandardTask.
        :type: str
        """
        allowed_values = ["FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(last_execution_status, allowed_values):
            last_execution_status = 'UNKNOWN_ENUM_VALUE'
        self._last_execution_status = last_execution_status

    @property
    def time_last_executed(self):
        """
        Gets the time_last_executed of this StandardTask.
        The date and time the scheduled task last executed, in the format defined by RFC3339.


        :return: The time_last_executed of this StandardTask.
        :rtype: datetime
        """
        return self._time_last_executed

    @time_last_executed.setter
    def time_last_executed(self, time_last_executed):
        """
        Sets the time_last_executed of this StandardTask.
        The date and time the scheduled task last executed, in the format defined by RFC3339.


        :param time_last_executed: The time_last_executed of this StandardTask.
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
