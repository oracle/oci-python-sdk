# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrPlanGroupExecution(object):
    """
    Summary information about a group execution in a DR Plan Execution.
    """

    #: A constant which can be used with the type property of a DrPlanGroupExecution.
    #: This constant has a value of "USER_DEFINED"
    TYPE_USER_DEFINED = "USER_DEFINED"

    #: A constant which can be used with the type property of a DrPlanGroupExecution.
    #: This constant has a value of "BUILT_IN"
    TYPE_BUILT_IN = "BUILT_IN"

    #: A constant which can be used with the type property of a DrPlanGroupExecution.
    #: This constant has a value of "BUILT_IN_PRECHECK"
    TYPE_BUILT_IN_PRECHECK = "BUILT_IN_PRECHECK"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "QUEUED"
    STATUS_QUEUED = "QUEUED"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "SUCCEEDED_WITH_WARNING"
    STATUS_SUCCEEDED_WITH_WARNING = "SUCCEEDED_WITH_WARNING"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "FAILED_IGNORED"
    STATUS_FAILED_IGNORED = "FAILED_IGNORED"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "TIMED_OUT"
    STATUS_TIMED_OUT = "TIMED_OUT"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "TIMED_OUT_IGNORED"
    STATUS_TIMED_OUT_IGNORED = "TIMED_OUT_IGNORED"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "PAUSED"
    STATUS_PAUSED = "PAUSED"

    #: A constant which can be used with the status property of a DrPlanGroupExecution.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new DrPlanGroupExecution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param group_id:
            The value to assign to the group_id property of this DrPlanGroupExecution.
        :type group_id: str

        :param type:
            The value to assign to the type property of this DrPlanGroupExecution.
            Allowed values for this property are: "USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this DrPlanGroupExecution.
        :type display_name: str

        :param status:
            The value to assign to the status property of this DrPlanGroupExecution.
            Allowed values for this property are: "QUEUED", "DISABLED", "IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_WARNING", "FAILED", "FAILED_IGNORED", "TIMED_OUT", "TIMED_OUT_IGNORED", "PAUSED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_details:
            The value to assign to the status_details property of this DrPlanGroupExecution.
        :type status_details: str

        :param time_started:
            The value to assign to the time_started property of this DrPlanGroupExecution.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this DrPlanGroupExecution.
        :type time_ended: datetime

        :param execution_duration_in_sec:
            The value to assign to the execution_duration_in_sec property of this DrPlanGroupExecution.
        :type execution_duration_in_sec: int

        :param step_executions:
            The value to assign to the step_executions property of this DrPlanGroupExecution.
        :type step_executions: list[oci.disaster_recovery.models.DrPlanStepExecution]

        """
        self.swagger_types = {
            'group_id': 'str',
            'type': 'str',
            'display_name': 'str',
            'status': 'str',
            'status_details': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'execution_duration_in_sec': 'int',
            'step_executions': 'list[DrPlanStepExecution]'
        }

        self.attribute_map = {
            'group_id': 'groupId',
            'type': 'type',
            'display_name': 'displayName',
            'status': 'status',
            'status_details': 'statusDetails',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'execution_duration_in_sec': 'executionDurationInSec',
            'step_executions': 'stepExecutions'
        }

        self._group_id = None
        self._type = None
        self._display_name = None
        self._status = None
        self._status_details = None
        self._time_started = None
        self._time_ended = None
        self._execution_duration_in_sec = None
        self._step_executions = None

    @property
    def group_id(self):
        """
        **[Required]** Gets the group_id of this DrPlanGroupExecution.
        The unique id of the group. Must not be modified by user.

        Example: `sgid1.group..examplegroupsgid`


        :return: The group_id of this DrPlanGroupExecution.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this DrPlanGroupExecution.
        The unique id of the group. Must not be modified by user.

        Example: `sgid1.group..examplegroupsgid`


        :param group_id: The group_id of this DrPlanGroupExecution.
        :type: str
        """
        self._group_id = group_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DrPlanGroupExecution.
        The plan group type.

        Allowed values for this property are: "USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DrPlanGroupExecution.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DrPlanGroupExecution.
        The plan group type.


        :param type: The type of this DrPlanGroupExecution.
        :type: str
        """
        allowed_values = ["USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DrPlanGroupExecution.
        The display name of group that was executed.

        Example: `DATABASE_SWITCHOVER`


        :return: The display_name of this DrPlanGroupExecution.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrPlanGroupExecution.
        The display name of group that was executed.

        Example: `DATABASE_SWITCHOVER`


        :param display_name: The display_name of this DrPlanGroupExecution.
        :type: str
        """
        self._display_name = display_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this DrPlanGroupExecution.
        The status of the group execution.

        Allowed values for this property are: "QUEUED", "DISABLED", "IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_WARNING", "FAILED", "FAILED_IGNORED", "TIMED_OUT", "TIMED_OUT_IGNORED", "PAUSED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DrPlanGroupExecution.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DrPlanGroupExecution.
        The status of the group execution.


        :param status: The status of this DrPlanGroupExecution.
        :type: str
        """
        allowed_values = ["QUEUED", "DISABLED", "IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_WARNING", "FAILED", "FAILED_IGNORED", "TIMED_OUT", "TIMED_OUT_IGNORED", "PAUSED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_details(self):
        """
        Gets the status_details of this DrPlanGroupExecution.
        Additional details about the group execution status.

        Example: `A total of three steps failed in the group`


        :return: The status_details of this DrPlanGroupExecution.
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """
        Sets the status_details of this DrPlanGroupExecution.
        Additional details about the group execution status.

        Example: `A total of three steps failed in the group`


        :param status_details: The status_details of this DrPlanGroupExecution.
        :type: str
        """
        self._status_details = status_details

    @property
    def time_started(self):
        """
        Gets the time_started of this DrPlanGroupExecution.
        The time at which group execution began. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_started of this DrPlanGroupExecution.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DrPlanGroupExecution.
        The time at which group execution began. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_started: The time_started of this DrPlanGroupExecution.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this DrPlanGroupExecution.
        The time at which group execution ended. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_ended of this DrPlanGroupExecution.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this DrPlanGroupExecution.
        The time at which group execution ended. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_ended: The time_ended of this DrPlanGroupExecution.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def execution_duration_in_sec(self):
        """
        Gets the execution_duration_in_sec of this DrPlanGroupExecution.
        The total duration in seconds taken to complete group execution.

        Example: `120`


        :return: The execution_duration_in_sec of this DrPlanGroupExecution.
        :rtype: int
        """
        return self._execution_duration_in_sec

    @execution_duration_in_sec.setter
    def execution_duration_in_sec(self, execution_duration_in_sec):
        """
        Sets the execution_duration_in_sec of this DrPlanGroupExecution.
        The total duration in seconds taken to complete group execution.

        Example: `120`


        :param execution_duration_in_sec: The execution_duration_in_sec of this DrPlanGroupExecution.
        :type: int
        """
        self._execution_duration_in_sec = execution_duration_in_sec

    @property
    def step_executions(self):
        """
        **[Required]** Gets the step_executions of this DrPlanGroupExecution.
        A list of details of each step executed in this group.


        :return: The step_executions of this DrPlanGroupExecution.
        :rtype: list[oci.disaster_recovery.models.DrPlanStepExecution]
        """
        return self._step_executions

    @step_executions.setter
    def step_executions(self, step_executions):
        """
        Sets the step_executions of this DrPlanGroupExecution.
        A list of details of each step executed in this group.


        :param step_executions: The step_executions of this DrPlanGroupExecution.
        :type: list[oci.disaster_recovery.models.DrPlanStepExecution]
        """
        self._step_executions = step_executions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
