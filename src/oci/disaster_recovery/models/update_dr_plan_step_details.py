# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrPlanStepDetails(object):
    """
    The details for updating a DR Plan step.
    """

    #: A constant which can be used with the error_mode property of a UpdateDrPlanStepDetails.
    #: This constant has a value of "STOP_ON_ERROR"
    ERROR_MODE_STOP_ON_ERROR = "STOP_ON_ERROR"

    #: A constant which can be used with the error_mode property of a UpdateDrPlanStepDetails.
    #: This constant has a value of "CONTINUE_ON_ERROR"
    ERROR_MODE_CONTINUE_ON_ERROR = "CONTINUE_ON_ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrPlanStepDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this UpdateDrPlanStepDetails.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this UpdateDrPlanStepDetails.
        :type display_name: str

        :param error_mode:
            The value to assign to the error_mode property of this UpdateDrPlanStepDetails.
            Allowed values for this property are: "STOP_ON_ERROR", "CONTINUE_ON_ERROR"
        :type error_mode: str

        :param timeout:
            The value to assign to the timeout property of this UpdateDrPlanStepDetails.
        :type timeout: int

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateDrPlanStepDetails.
        :type is_enabled: bool

        :param user_defined_step:
            The value to assign to the user_defined_step property of this UpdateDrPlanStepDetails.
        :type user_defined_step: oci.disaster_recovery.models.UpdateDrPlanUserDefinedStepDetails

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'error_mode': 'str',
            'timeout': 'int',
            'is_enabled': 'bool',
            'user_defined_step': 'UpdateDrPlanUserDefinedStepDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'error_mode': 'errorMode',
            'timeout': 'timeout',
            'is_enabled': 'isEnabled',
            'user_defined_step': 'userDefinedStep'
        }

        self._id = None
        self._display_name = None
        self._error_mode = None
        self._timeout = None
        self._is_enabled = None
        self._user_defined_step = None

    @property
    def id(self):
        """
        Gets the id of this UpdateDrPlanStepDetails.
        The unique id of this step.

        Example: `sgid1.step..examplestepsgid`


        :return: The id of this UpdateDrPlanStepDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateDrPlanStepDetails.
        The unique id of this step.

        Example: `sgid1.step..examplestepsgid`


        :param id: The id of this UpdateDrPlanStepDetails.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDrPlanStepDetails.
        The display name of this step in a group.

        Example: `My_STEP_3A - EBS Start - STAGE A`


        :return: The display_name of this UpdateDrPlanStepDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDrPlanStepDetails.
        The display name of this step in a group.

        Example: `My_STEP_3A - EBS Start - STAGE A`


        :param display_name: The display_name of this UpdateDrPlanStepDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def error_mode(self):
        """
        Gets the error_mode of this UpdateDrPlanStepDetails.
        The error mode for this step.

        Allowed values for this property are: "STOP_ON_ERROR", "CONTINUE_ON_ERROR"


        :return: The error_mode of this UpdateDrPlanStepDetails.
        :rtype: str
        """
        return self._error_mode

    @error_mode.setter
    def error_mode(self, error_mode):
        """
        Sets the error_mode of this UpdateDrPlanStepDetails.
        The error mode for this step.


        :param error_mode: The error_mode of this UpdateDrPlanStepDetails.
        :type: str
        """
        allowed_values = ["STOP_ON_ERROR", "CONTINUE_ON_ERROR"]
        if not value_allowed_none_or_none_sentinel(error_mode, allowed_values):
            raise ValueError(
                "Invalid value for `error_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._error_mode = error_mode

    @property
    def timeout(self):
        """
        Gets the timeout of this UpdateDrPlanStepDetails.
        The timeout in seconds for executing this step.

        Example: `600`


        :return: The timeout of this UpdateDrPlanStepDetails.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this UpdateDrPlanStepDetails.
        The timeout in seconds for executing this step.

        Example: `600`


        :param timeout: The timeout of this UpdateDrPlanStepDetails.
        :type: int
        """
        self._timeout = timeout

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateDrPlanStepDetails.
        A flag indicating whether this step should be enabled for execution.

        Example: `true`


        :return: The is_enabled of this UpdateDrPlanStepDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateDrPlanStepDetails.
        A flag indicating whether this step should be enabled for execution.

        Example: `true`


        :param is_enabled: The is_enabled of this UpdateDrPlanStepDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def user_defined_step(self):
        """
        Gets the user_defined_step of this UpdateDrPlanStepDetails.

        :return: The user_defined_step of this UpdateDrPlanStepDetails.
        :rtype: oci.disaster_recovery.models.UpdateDrPlanUserDefinedStepDetails
        """
        return self._user_defined_step

    @user_defined_step.setter
    def user_defined_step(self, user_defined_step):
        """
        Sets the user_defined_step of this UpdateDrPlanStepDetails.

        :param user_defined_step: The user_defined_step of this UpdateDrPlanStepDetails.
        :type: oci.disaster_recovery.models.UpdateDrPlanUserDefinedStepDetails
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
