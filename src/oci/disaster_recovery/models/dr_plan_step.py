# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrPlanStep(object):
    """
    Details of a step in a DR Plan.
    """

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "COMPUTE_INSTANCE_STOP_PRECHECK"
    TYPE_COMPUTE_INSTANCE_STOP_PRECHECK = "COMPUTE_INSTANCE_STOP_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "COMPUTE_INSTANCE_LAUNCH_PRECHECK"
    TYPE_COMPUTE_INSTANCE_LAUNCH_PRECHECK = "COMPUTE_INSTANCE_LAUNCH_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "COMPUTE_INSTANCE_TERMINATE_PRECHECK"
    TYPE_COMPUTE_INSTANCE_TERMINATE_PRECHECK = "COMPUTE_INSTANCE_TERMINATE_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "COMPUTE_INSTANCE_REMOVE_PRECHECK"
    TYPE_COMPUTE_INSTANCE_REMOVE_PRECHECK = "COMPUTE_INSTANCE_REMOVE_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK"
    TYPE_VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK = "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK"
    TYPE_VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK = "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "DATABASE_SWITCHOVER_PRECHECK"
    TYPE_DATABASE_SWITCHOVER_PRECHECK = "DATABASE_SWITCHOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "DATABASE_FAILOVER_PRECHECK"
    TYPE_DATABASE_FAILOVER_PRECHECK = "DATABASE_FAILOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK"
    TYPE_AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK = "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK"
    TYPE_AUTONOMOUS_DATABASE_FAILOVER_PRECHECK = "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "USER_DEFINED_PRECHECK"
    TYPE_USER_DEFINED_PRECHECK = "USER_DEFINED_PRECHECK"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "COMPUTE_INSTANCE_LAUNCH"
    TYPE_COMPUTE_INSTANCE_LAUNCH = "COMPUTE_INSTANCE_LAUNCH"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "COMPUTE_INSTANCE_STOP"
    TYPE_COMPUTE_INSTANCE_STOP = "COMPUTE_INSTANCE_STOP"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "COMPUTE_INSTANCE_TERMINATE"
    TYPE_COMPUTE_INSTANCE_TERMINATE = "COMPUTE_INSTANCE_TERMINATE"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "COMPUTE_INSTANCE_REMOVE"
    TYPE_COMPUTE_INSTANCE_REMOVE = "COMPUTE_INSTANCE_REMOVE"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "DATABASE_SWITCHOVER"
    TYPE_DATABASE_SWITCHOVER = "DATABASE_SWITCHOVER"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "DATABASE_FAILOVER"
    TYPE_DATABASE_FAILOVER = "DATABASE_FAILOVER"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "AUTONOMOUS_DATABASE_SWITCHOVER"
    TYPE_AUTONOMOUS_DATABASE_SWITCHOVER = "AUTONOMOUS_DATABASE_SWITCHOVER"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "AUTONOMOUS_DATABASE_FAILOVER"
    TYPE_AUTONOMOUS_DATABASE_FAILOVER = "AUTONOMOUS_DATABASE_FAILOVER"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "VOLUME_GROUP_RESTORE_SWITCHOVER"
    TYPE_VOLUME_GROUP_RESTORE_SWITCHOVER = "VOLUME_GROUP_RESTORE_SWITCHOVER"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "VOLUME_GROUP_RESTORE_FAILOVER"
    TYPE_VOLUME_GROUP_RESTORE_FAILOVER = "VOLUME_GROUP_RESTORE_FAILOVER"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "VOLUME_GROUP_REVERSE"
    TYPE_VOLUME_GROUP_REVERSE = "VOLUME_GROUP_REVERSE"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "VOLUME_GROUP_DELETE"
    TYPE_VOLUME_GROUP_DELETE = "VOLUME_GROUP_DELETE"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "VOLUME_GROUP_REMOVE"
    TYPE_VOLUME_GROUP_REMOVE = "VOLUME_GROUP_REMOVE"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "VOLUME_GROUP_TERMINATE"
    TYPE_VOLUME_GROUP_TERMINATE = "VOLUME_GROUP_TERMINATE"

    #: A constant which can be used with the type property of a DrPlanStep.
    #: This constant has a value of "USER_DEFINED"
    TYPE_USER_DEFINED = "USER_DEFINED"

    #: A constant which can be used with the error_mode property of a DrPlanStep.
    #: This constant has a value of "STOP_ON_ERROR"
    ERROR_MODE_STOP_ON_ERROR = "STOP_ON_ERROR"

    #: A constant which can be used with the error_mode property of a DrPlanStep.
    #: This constant has a value of "CONTINUE_ON_ERROR"
    ERROR_MODE_CONTINUE_ON_ERROR = "CONTINUE_ON_ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new DrPlanStep object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DrPlanStep.
        :type id: str

        :param group_id:
            The value to assign to the group_id property of this DrPlanStep.
        :type group_id: str

        :param member_id:
            The value to assign to the member_id property of this DrPlanStep.
        :type member_id: str

        :param type:
            The value to assign to the type property of this DrPlanStep.
            Allowed values for this property are: "COMPUTE_INSTANCE_STOP_PRECHECK", "COMPUTE_INSTANCE_LAUNCH_PRECHECK", "COMPUTE_INSTANCE_TERMINATE_PRECHECK", "COMPUTE_INSTANCE_REMOVE_PRECHECK", "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK", "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK", "DATABASE_SWITCHOVER_PRECHECK", "DATABASE_FAILOVER_PRECHECK", "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK", "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK", "USER_DEFINED_PRECHECK", "COMPUTE_INSTANCE_LAUNCH", "COMPUTE_INSTANCE_STOP", "COMPUTE_INSTANCE_TERMINATE", "COMPUTE_INSTANCE_REMOVE", "DATABASE_SWITCHOVER", "DATABASE_FAILOVER", "AUTONOMOUS_DATABASE_SWITCHOVER", "AUTONOMOUS_DATABASE_FAILOVER", "VOLUME_GROUP_RESTORE_SWITCHOVER", "VOLUME_GROUP_RESTORE_FAILOVER", "VOLUME_GROUP_REVERSE", "VOLUME_GROUP_DELETE", "VOLUME_GROUP_REMOVE", "VOLUME_GROUP_TERMINATE", "USER_DEFINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this DrPlanStep.
        :type display_name: str

        :param error_mode:
            The value to assign to the error_mode property of this DrPlanStep.
            Allowed values for this property are: "STOP_ON_ERROR", "CONTINUE_ON_ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type error_mode: str

        :param timeout:
            The value to assign to the timeout property of this DrPlanStep.
        :type timeout: int

        :param is_enabled:
            The value to assign to the is_enabled property of this DrPlanStep.
        :type is_enabled: bool

        :param user_defined_step:
            The value to assign to the user_defined_step property of this DrPlanStep.
        :type user_defined_step: oci.disaster_recovery.models.DrPlanUserDefinedStep

        """
        self.swagger_types = {
            'id': 'str',
            'group_id': 'str',
            'member_id': 'str',
            'type': 'str',
            'display_name': 'str',
            'error_mode': 'str',
            'timeout': 'int',
            'is_enabled': 'bool',
            'user_defined_step': 'DrPlanUserDefinedStep'
        }

        self.attribute_map = {
            'id': 'id',
            'group_id': 'groupId',
            'member_id': 'memberId',
            'type': 'type',
            'display_name': 'displayName',
            'error_mode': 'errorMode',
            'timeout': 'timeout',
            'is_enabled': 'isEnabled',
            'user_defined_step': 'userDefinedStep'
        }

        self._id = None
        self._group_id = None
        self._member_id = None
        self._type = None
        self._display_name = None
        self._error_mode = None
        self._timeout = None
        self._is_enabled = None
        self._user_defined_step = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrPlanStep.
        The unique id of this step. Must not be modified by the user.

        Example: `sgid1.step..examplestepsgid`


        :return: The id of this DrPlanStep.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrPlanStep.
        The unique id of this step. Must not be modified by the user.

        Example: `sgid1.step..examplestepsgid`


        :param id: The id of this DrPlanStep.
        :type: str
        """
        self._id = id

    @property
    def group_id(self):
        """
        **[Required]** Gets the group_id of this DrPlanStep.
        The unique id of the group to which this step belongs. Must not be modified by user.

        Example: `sgid1.group..examplegroupsgid`


        :return: The group_id of this DrPlanStep.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this DrPlanStep.
        The unique id of the group to which this step belongs. Must not be modified by user.

        Example: `sgid1.group..examplegroupsgid`


        :param group_id: The group_id of this DrPlanStep.
        :type: str
        """
        self._group_id = group_id

    @property
    def member_id(self):
        """
        Gets the member_id of this DrPlanStep.
        The OCID of the member associated with this step.

        Example: `ocid1.database.oc1.phx.exampleocid1`


        :return: The member_id of this DrPlanStep.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this DrPlanStep.
        The OCID of the member associated with this step.

        Example: `ocid1.database.oc1.phx.exampleocid1`


        :param member_id: The member_id of this DrPlanStep.
        :type: str
        """
        self._member_id = member_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DrPlanStep.
        The plan step type.

        Allowed values for this property are: "COMPUTE_INSTANCE_STOP_PRECHECK", "COMPUTE_INSTANCE_LAUNCH_PRECHECK", "COMPUTE_INSTANCE_TERMINATE_PRECHECK", "COMPUTE_INSTANCE_REMOVE_PRECHECK", "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK", "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK", "DATABASE_SWITCHOVER_PRECHECK", "DATABASE_FAILOVER_PRECHECK", "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK", "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK", "USER_DEFINED_PRECHECK", "COMPUTE_INSTANCE_LAUNCH", "COMPUTE_INSTANCE_STOP", "COMPUTE_INSTANCE_TERMINATE", "COMPUTE_INSTANCE_REMOVE", "DATABASE_SWITCHOVER", "DATABASE_FAILOVER", "AUTONOMOUS_DATABASE_SWITCHOVER", "AUTONOMOUS_DATABASE_FAILOVER", "VOLUME_GROUP_RESTORE_SWITCHOVER", "VOLUME_GROUP_RESTORE_FAILOVER", "VOLUME_GROUP_REVERSE", "VOLUME_GROUP_DELETE", "VOLUME_GROUP_REMOVE", "VOLUME_GROUP_TERMINATE", "USER_DEFINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DrPlanStep.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DrPlanStep.
        The plan step type.


        :param type: The type of this DrPlanStep.
        :type: str
        """
        allowed_values = ["COMPUTE_INSTANCE_STOP_PRECHECK", "COMPUTE_INSTANCE_LAUNCH_PRECHECK", "COMPUTE_INSTANCE_TERMINATE_PRECHECK", "COMPUTE_INSTANCE_REMOVE_PRECHECK", "VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK", "VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK", "DATABASE_SWITCHOVER_PRECHECK", "DATABASE_FAILOVER_PRECHECK", "AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK", "AUTONOMOUS_DATABASE_FAILOVER_PRECHECK", "USER_DEFINED_PRECHECK", "COMPUTE_INSTANCE_LAUNCH", "COMPUTE_INSTANCE_STOP", "COMPUTE_INSTANCE_TERMINATE", "COMPUTE_INSTANCE_REMOVE", "DATABASE_SWITCHOVER", "DATABASE_FAILOVER", "AUTONOMOUS_DATABASE_SWITCHOVER", "AUTONOMOUS_DATABASE_FAILOVER", "VOLUME_GROUP_RESTORE_SWITCHOVER", "VOLUME_GROUP_RESTORE_FAILOVER", "VOLUME_GROUP_REVERSE", "VOLUME_GROUP_DELETE", "VOLUME_GROUP_REMOVE", "VOLUME_GROUP_TERMINATE", "USER_DEFINED"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DrPlanStep.
        The display name of this DR Plan Group.

        Example: `DATABASE_SWITCHOVER`


        :return: The display_name of this DrPlanStep.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrPlanStep.
        The display name of this DR Plan Group.

        Example: `DATABASE_SWITCHOVER`


        :param display_name: The display_name of this DrPlanStep.
        :type: str
        """
        self._display_name = display_name

    @property
    def error_mode(self):
        """
        **[Required]** Gets the error_mode of this DrPlanStep.
        The error mode for this step.

        Allowed values for this property are: "STOP_ON_ERROR", "CONTINUE_ON_ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The error_mode of this DrPlanStep.
        :rtype: str
        """
        return self._error_mode

    @error_mode.setter
    def error_mode(self, error_mode):
        """
        Sets the error_mode of this DrPlanStep.
        The error mode for this step.


        :param error_mode: The error_mode of this DrPlanStep.
        :type: str
        """
        allowed_values = ["STOP_ON_ERROR", "CONTINUE_ON_ERROR"]
        if not value_allowed_none_or_none_sentinel(error_mode, allowed_values):
            error_mode = 'UNKNOWN_ENUM_VALUE'
        self._error_mode = error_mode

    @property
    def timeout(self):
        """
        **[Required]** Gets the timeout of this DrPlanStep.
        The timeout in seconds for executing this step.

        Example: `600`


        :return: The timeout of this DrPlanStep.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this DrPlanStep.
        The timeout in seconds for executing this step.

        Example: `600`


        :param timeout: The timeout of this DrPlanStep.
        :type: int
        """
        self._timeout = timeout

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this DrPlanStep.
        A flag indicating whether this step should be enabled for execution.

        Example: `true`


        :return: The is_enabled of this DrPlanStep.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this DrPlanStep.
        A flag indicating whether this step should be enabled for execution.

        Example: `true`


        :param is_enabled: The is_enabled of this DrPlanStep.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def user_defined_step(self):
        """
        Gets the user_defined_step of this DrPlanStep.

        :return: The user_defined_step of this DrPlanStep.
        :rtype: oci.disaster_recovery.models.DrPlanUserDefinedStep
        """
        return self._user_defined_step

    @user_defined_step.setter
    def user_defined_step(self, user_defined_step):
        """
        Sets the user_defined_step of this DrPlanStep.

        :param user_defined_step: The user_defined_step of this DrPlanStep.
        :type: oci.disaster_recovery.models.DrPlanUserDefinedStep
        """
        self._user_defined_step = user_defined_step

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
