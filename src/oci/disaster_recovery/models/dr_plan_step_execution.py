# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrPlanStepExecution(object):
    """
    Summary information about a step execution.
    """

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "COMPUTE_INSTANCE_STOP_PRECHECK"
    TYPE_COMPUTE_INSTANCE_STOP_PRECHECK = "COMPUTE_INSTANCE_STOP_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "COMPUTE_INSTANCE_LAUNCH_PRECHECK"
    TYPE_COMPUTE_INSTANCE_LAUNCH_PRECHECK = "COMPUTE_INSTANCE_LAUNCH_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "COMPUTE_INSTANCE_TERMINATE_PRECHECK"
    TYPE_COMPUTE_INSTANCE_TERMINATE_PRECHECK = "COMPUTE_INSTANCE_TERMINATE_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "COMPUTE_INSTANCE_REMOVE_PRECHECK"
    TYPE_COMPUTE_INSTANCE_REMOVE_PRECHECK = "COMPUTE_INSTANCE_REMOVE_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK"
    TYPE_VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK = "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK"
    TYPE_VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK = "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "DATABASE_SWITCHOVER_PRECHECK"
    TYPE_DATABASE_SWITCHOVER_PRECHECK = "DATABASE_SWITCHOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "DATABASE_FAILOVER_PRECHECK"
    TYPE_DATABASE_FAILOVER_PRECHECK = "DATABASE_FAILOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK"
    TYPE_AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK = "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK"
    TYPE_AUTONOMOUS_DATABASE_FAILOVER_PRECHECK = "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "USER_DEFINED_PRECHECK"
    TYPE_USER_DEFINED_PRECHECK = "USER_DEFINED_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "COMPUTE_INSTANCE_LAUNCH"
    TYPE_COMPUTE_INSTANCE_LAUNCH = "COMPUTE_INSTANCE_LAUNCH"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "COMPUTE_INSTANCE_STOP"
    TYPE_COMPUTE_INSTANCE_STOP = "COMPUTE_INSTANCE_STOP"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "COMPUTE_INSTANCE_TERMINATE"
    TYPE_COMPUTE_INSTANCE_TERMINATE = "COMPUTE_INSTANCE_TERMINATE"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "COMPUTE_INSTANCE_REMOVE"
    TYPE_COMPUTE_INSTANCE_REMOVE = "COMPUTE_INSTANCE_REMOVE"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "DATABASE_SWITCHOVER"
    TYPE_DATABASE_SWITCHOVER = "DATABASE_SWITCHOVER"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "DATABASE_FAILOVER"
    TYPE_DATABASE_FAILOVER = "DATABASE_FAILOVER"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "AUTONOMOUS_DATABASE_SWITCHOVER"
    TYPE_AUTONOMOUS_DATABASE_SWITCHOVER = "AUTONOMOUS_DATABASE_SWITCHOVER"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "AUTONOMOUS_DATABASE_FAILOVER"
    TYPE_AUTONOMOUS_DATABASE_FAILOVER = "AUTONOMOUS_DATABASE_FAILOVER"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "VOLUME_GROUP_RESTORE_SWITCHOVER"
    TYPE_VOLUME_GROUP_RESTORE_SWITCHOVER = "VOLUME_GROUP_RESTORE_SWITCHOVER"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "VOLUME_GROUP_RESTORE_FAILOVER"
    TYPE_VOLUME_GROUP_RESTORE_FAILOVER = "VOLUME_GROUP_RESTORE_FAILOVER"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "VOLUME_GROUP_REVERSE"
    TYPE_VOLUME_GROUP_REVERSE = "VOLUME_GROUP_REVERSE"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "VOLUME_GROUP_DELETE"
    TYPE_VOLUME_GROUP_DELETE = "VOLUME_GROUP_DELETE"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "VOLUME_GROUP_REMOVE"
    TYPE_VOLUME_GROUP_REMOVE = "VOLUME_GROUP_REMOVE"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "VOLUME_GROUP_TERMINATE"
    TYPE_VOLUME_GROUP_TERMINATE = "VOLUME_GROUP_TERMINATE"

    #: A constant which can be used with the type property of a DrPlanStepExecution.
    #: This constant has a value of "USER_DEFINED"
    TYPE_USER_DEFINED = "USER_DEFINED"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "QUEUED"
    STATUS_QUEUED = "QUEUED"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "FAILED_IGNORED"
    STATUS_FAILED_IGNORED = "FAILED_IGNORED"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "TIMED_OUT"
    STATUS_TIMED_OUT = "TIMED_OUT"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "TIMED_OUT_IGNORED"
    STATUS_TIMED_OUT_IGNORED = "TIMED_OUT_IGNORED"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "PAUSED"
    STATUS_PAUSED = "PAUSED"

    #: A constant which can be used with the status property of a DrPlanStepExecution.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new DrPlanStepExecution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_id:
            The value to assign to the step_id property of this DrPlanStepExecution.
        :type step_id: str

        :param type:
            The value to assign to the type property of this DrPlanStepExecution.
            Allowed values for this property are: "COMPUTE_INSTANCE_STOP_PRECHECK", "COMPUTE_INSTANCE_LAUNCH_PRECHECK", "COMPUTE_INSTANCE_TERMINATE_PRECHECK", "COMPUTE_INSTANCE_REMOVE_PRECHECK", "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK", "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK", "DATABASE_SWITCHOVER_PRECHECK", "DATABASE_FAILOVER_PRECHECK", "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK", "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK", "USER_DEFINED_PRECHECK", "COMPUTE_INSTANCE_LAUNCH", "COMPUTE_INSTANCE_STOP", "COMPUTE_INSTANCE_TERMINATE", "COMPUTE_INSTANCE_REMOVE", "DATABASE_SWITCHOVER", "DATABASE_FAILOVER", "AUTONOMOUS_DATABASE_SWITCHOVER", "AUTONOMOUS_DATABASE_FAILOVER", "VOLUME_GROUP_RESTORE_SWITCHOVER", "VOLUME_GROUP_RESTORE_FAILOVER", "VOLUME_GROUP_REVERSE", "VOLUME_GROUP_DELETE", "VOLUME_GROUP_REMOVE", "VOLUME_GROUP_TERMINATE", "USER_DEFINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param group_id:
            The value to assign to the group_id property of this DrPlanStepExecution.
        :type group_id: str

        :param display_name:
            The value to assign to the display_name property of this DrPlanStepExecution.
        :type display_name: str

        :param log_location:
            The value to assign to the log_location property of this DrPlanStepExecution.
        :type log_location: oci.disaster_recovery.models.ObjectStorageLogLocation

        :param status:
            The value to assign to the status property of this DrPlanStepExecution.
            Allowed values for this property are: "QUEUED", "DISABLED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "FAILED_IGNORED", "TIMED_OUT", "TIMED_OUT_IGNORED", "PAUSED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_details:
            The value to assign to the status_details property of this DrPlanStepExecution.
        :type status_details: str

        :param time_started:
            The value to assign to the time_started property of this DrPlanStepExecution.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this DrPlanStepExecution.
        :type time_ended: datetime

        :param execution_duration_in_sec:
            The value to assign to the execution_duration_in_sec property of this DrPlanStepExecution.
        :type execution_duration_in_sec: int

        """
        self.swagger_types = {
            'step_id': 'str',
            'type': 'str',
            'group_id': 'str',
            'display_name': 'str',
            'log_location': 'ObjectStorageLogLocation',
            'status': 'str',
            'status_details': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'execution_duration_in_sec': 'int'
        }

        self.attribute_map = {
            'step_id': 'stepId',
            'type': 'type',
            'group_id': 'groupId',
            'display_name': 'displayName',
            'log_location': 'logLocation',
            'status': 'status',
            'status_details': 'statusDetails',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'execution_duration_in_sec': 'executionDurationInSec'
        }

        self._step_id = None
        self._type = None
        self._group_id = None
        self._display_name = None
        self._log_location = None
        self._status = None
        self._status_details = None
        self._time_started = None
        self._time_ended = None
        self._execution_duration_in_sec = None

    @property
    def step_id(self):
        """
        **[Required]** Gets the step_id of this DrPlanStepExecution.
        The unique id of this step. Must not be modified by user.

        Example: `sgid1.step..examplestepsgid`


        :return: The step_id of this DrPlanStepExecution.
        :rtype: str
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        """
        Sets the step_id of this DrPlanStepExecution.
        The unique id of this step. Must not be modified by user.

        Example: `sgid1.step..examplestepsgid`


        :param step_id: The step_id of this DrPlanStepExecution.
        :type: str
        """
        self._step_id = step_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DrPlanStepExecution.
        The plan step type.

        Allowed values for this property are: "COMPUTE_INSTANCE_STOP_PRECHECK", "COMPUTE_INSTANCE_LAUNCH_PRECHECK", "COMPUTE_INSTANCE_TERMINATE_PRECHECK", "COMPUTE_INSTANCE_REMOVE_PRECHECK", "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK", "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK", "DATABASE_SWITCHOVER_PRECHECK", "DATABASE_FAILOVER_PRECHECK", "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK", "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK", "USER_DEFINED_PRECHECK", "COMPUTE_INSTANCE_LAUNCH", "COMPUTE_INSTANCE_STOP", "COMPUTE_INSTANCE_TERMINATE", "COMPUTE_INSTANCE_REMOVE", "DATABASE_SWITCHOVER", "DATABASE_FAILOVER", "AUTONOMOUS_DATABASE_SWITCHOVER", "AUTONOMOUS_DATABASE_FAILOVER", "VOLUME_GROUP_RESTORE_SWITCHOVER", "VOLUME_GROUP_RESTORE_FAILOVER", "VOLUME_GROUP_REVERSE", "VOLUME_GROUP_DELETE", "VOLUME_GROUP_REMOVE", "VOLUME_GROUP_TERMINATE", "USER_DEFINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DrPlanStepExecution.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DrPlanStepExecution.
        The plan step type.


        :param type: The type of this DrPlanStepExecution.
        :type: str
        """
        allowed_values = ["COMPUTE_INSTANCE_STOP_PRECHECK", "COMPUTE_INSTANCE_LAUNCH_PRECHECK", "COMPUTE_INSTANCE_TERMINATE_PRECHECK", "COMPUTE_INSTANCE_REMOVE_PRECHECK", "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK", "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK", "DATABASE_SWITCHOVER_PRECHECK", "DATABASE_FAILOVER_PRECHECK", "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK", "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK", "USER_DEFINED_PRECHECK", "COMPUTE_INSTANCE_LAUNCH", "COMPUTE_INSTANCE_STOP", "COMPUTE_INSTANCE_TERMINATE", "COMPUTE_INSTANCE_REMOVE", "DATABASE_SWITCHOVER", "DATABASE_FAILOVER", "AUTONOMOUS_DATABASE_SWITCHOVER", "AUTONOMOUS_DATABASE_FAILOVER", "VOLUME_GROUP_RESTORE_SWITCHOVER", "VOLUME_GROUP_RESTORE_FAILOVER", "VOLUME_GROUP_REVERSE", "VOLUME_GROUP_DELETE", "VOLUME_GROUP_REMOVE", "VOLUME_GROUP_TERMINATE", "USER_DEFINED"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def group_id(self):
        """
        **[Required]** Gets the group_id of this DrPlanStepExecution.
        The unique id of the group to which this step belongs. Must not be modified by user.

        Example: `sgid1.group..examplegroupsgid`


        :return: The group_id of this DrPlanStepExecution.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this DrPlanStepExecution.
        The unique id of the group to which this step belongs. Must not be modified by user.

        Example: `sgid1.group..examplegroupsgid`


        :param group_id: The group_id of this DrPlanStepExecution.
        :type: str
        """
        self._group_id = group_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DrPlanStepExecution.
        The display name of the step.

        Example: `DATABASE_SWITCHOVER`


        :return: The display_name of this DrPlanStepExecution.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrPlanStepExecution.
        The display name of the step.

        Example: `DATABASE_SWITCHOVER`


        :param display_name: The display_name of this DrPlanStepExecution.
        :type: str
        """
        self._display_name = display_name

    @property
    def log_location(self):
        """
        **[Required]** Gets the log_location of this DrPlanStepExecution.

        :return: The log_location of this DrPlanStepExecution.
        :rtype: oci.disaster_recovery.models.ObjectStorageLogLocation
        """
        return self._log_location

    @log_location.setter
    def log_location(self, log_location):
        """
        Sets the log_location of this DrPlanStepExecution.

        :param log_location: The log_location of this DrPlanStepExecution.
        :type: oci.disaster_recovery.models.ObjectStorageLogLocation
        """
        self._log_location = log_location

    @property
    def status(self):
        """
        **[Required]** Gets the status of this DrPlanStepExecution.
        The status of the step execution.

        Allowed values for this property are: "QUEUED", "DISABLED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "FAILED_IGNORED", "TIMED_OUT", "TIMED_OUT_IGNORED", "PAUSED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DrPlanStepExecution.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DrPlanStepExecution.
        The status of the step execution.


        :param status: The status of this DrPlanStepExecution.
        :type: str
        """
        allowed_values = ["QUEUED", "DISABLED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "FAILED_IGNORED", "TIMED_OUT", "TIMED_OUT_IGNORED", "PAUSED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_details(self):
        """
        Gets the status_details of this DrPlanStepExecution.
        Additional details about the step execution status.

        Example: `This step failed to complete due to a timeout`


        :return: The status_details of this DrPlanStepExecution.
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """
        Sets the status_details of this DrPlanStepExecution.
        Additional details about the step execution status.

        Example: `This step failed to complete due to a timeout`


        :param status_details: The status_details of this DrPlanStepExecution.
        :type: str
        """
        self._status_details = status_details

    @property
    def time_started(self):
        """
        Gets the time_started of this DrPlanStepExecution.
        The time at which step execution began. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_started of this DrPlanStepExecution.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DrPlanStepExecution.
        The time at which step execution began. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_started: The time_started of this DrPlanStepExecution.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this DrPlanStepExecution.
        The time at which step execution ended. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_ended of this DrPlanStepExecution.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this DrPlanStepExecution.
        The time at which step execution ended. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_ended: The time_ended of this DrPlanStepExecution.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def execution_duration_in_sec(self):
        """
        Gets the execution_duration_in_sec of this DrPlanStepExecution.
        The total duration in seconds taken to complete step execution.

        Example: `35`


        :return: The execution_duration_in_sec of this DrPlanStepExecution.
        :rtype: int
        """
        return self._execution_duration_in_sec

    @execution_duration_in_sec.setter
    def execution_duration_in_sec(self, execution_duration_in_sec):
        """
        Sets the execution_duration_in_sec of this DrPlanStepExecution.
        The total duration in seconds taken to complete step execution.

        Example: `35`


        :param execution_duration_in_sec: The execution_duration_in_sec of this DrPlanStepExecution.
        :type: int
        """
        self._execution_duration_in_sec = execution_duration_in_sec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
