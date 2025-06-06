# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrPlanUserDefinedStepDetails(object):
    """
    The details for updating a user-defined step in a DR plan.
    """

    #: A constant which can be used with the step_type property of a UpdateDrPlanUserDefinedStepDetails.
    #: This constant has a value of "RUN_OBJECTSTORE_SCRIPT_PRECHECK"
    STEP_TYPE_RUN_OBJECTSTORE_SCRIPT_PRECHECK = "RUN_OBJECTSTORE_SCRIPT_PRECHECK"

    #: A constant which can be used with the step_type property of a UpdateDrPlanUserDefinedStepDetails.
    #: This constant has a value of "RUN_LOCAL_SCRIPT_PRECHECK"
    STEP_TYPE_RUN_LOCAL_SCRIPT_PRECHECK = "RUN_LOCAL_SCRIPT_PRECHECK"

    #: A constant which can be used with the step_type property of a UpdateDrPlanUserDefinedStepDetails.
    #: This constant has a value of "INVOKE_FUNCTION_PRECHECK"
    STEP_TYPE_INVOKE_FUNCTION_PRECHECK = "INVOKE_FUNCTION_PRECHECK"

    #: A constant which can be used with the step_type property of a UpdateDrPlanUserDefinedStepDetails.
    #: This constant has a value of "RUN_OBJECTSTORE_SCRIPT"
    STEP_TYPE_RUN_OBJECTSTORE_SCRIPT = "RUN_OBJECTSTORE_SCRIPT"

    #: A constant which can be used with the step_type property of a UpdateDrPlanUserDefinedStepDetails.
    #: This constant has a value of "RUN_LOCAL_SCRIPT"
    STEP_TYPE_RUN_LOCAL_SCRIPT = "RUN_LOCAL_SCRIPT"

    #: A constant which can be used with the step_type property of a UpdateDrPlanUserDefinedStepDetails.
    #: This constant has a value of "INVOKE_FUNCTION"
    STEP_TYPE_INVOKE_FUNCTION = "INVOKE_FUNCTION"

    #: A constant which can be used with the step_type property of a UpdateDrPlanUserDefinedStepDetails.
    #: This constant has a value of "RUN_OBJECTSTORE_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK"
    STEP_TYPE_RUN_OBJECTSTORE_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK = "RUN_OBJECTSTORE_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK"

    #: A constant which can be used with the step_type property of a UpdateDrPlanUserDefinedStepDetails.
    #: This constant has a value of "RUN_LOCAL_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK"
    STEP_TYPE_RUN_LOCAL_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK = "RUN_LOCAL_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK"

    #: A constant which can be used with the step_type property of a UpdateDrPlanUserDefinedStepDetails.
    #: This constant has a value of "INVOKE_FUNCTION_USER_DEFINED_CUSTOM_PRECHECK"
    STEP_TYPE_INVOKE_FUNCTION_USER_DEFINED_CUSTOM_PRECHECK = "INVOKE_FUNCTION_USER_DEFINED_CUSTOM_PRECHECK"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrPlanUserDefinedStepDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.disaster_recovery.models.UpdateRunLocalScriptUserDefinedCustomPrecheckStepDetails`
        * :class:`~oci.disaster_recovery.models.UpdateLocalScriptPrecheckStepDetails`
        * :class:`~oci.disaster_recovery.models.UpdateInvokeFunctionPrecheckStepDetails`
        * :class:`~oci.disaster_recovery.models.UpdateInvokeFunctionUserDefinedStepDetails`
        * :class:`~oci.disaster_recovery.models.UpdateRunObjectStoreScriptUserDefinedCustomPrecheckStepDetails`
        * :class:`~oci.disaster_recovery.models.UpdateInvokeFunctionUserDefinedCustomPrecheckStepDetails`
        * :class:`~oci.disaster_recovery.models.UpdateRunObjectStoreScriptUserDefinedStepDetails`
        * :class:`~oci.disaster_recovery.models.UpdateObjectStoreScriptPrecheckStepDetails`
        * :class:`~oci.disaster_recovery.models.UpdateRunLocalScriptUserDefinedStepDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_type:
            The value to assign to the step_type property of this UpdateDrPlanUserDefinedStepDetails.
            Allowed values for this property are: "RUN_OBJECTSTORE_SCRIPT_PRECHECK", "RUN_LOCAL_SCRIPT_PRECHECK", "INVOKE_FUNCTION_PRECHECK", "RUN_OBJECTSTORE_SCRIPT", "RUN_LOCAL_SCRIPT", "INVOKE_FUNCTION", "RUN_OBJECTSTORE_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK", "RUN_LOCAL_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK", "INVOKE_FUNCTION_USER_DEFINED_CUSTOM_PRECHECK"
        :type step_type: str

        """
        self.swagger_types = {
            'step_type': 'str'
        }
        self.attribute_map = {
            'step_type': 'stepType'
        }
        self._step_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['stepType']

        if type == 'RUN_LOCAL_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK':
            return 'UpdateRunLocalScriptUserDefinedCustomPrecheckStepDetails'

        if type == 'RUN_LOCAL_SCRIPT_PRECHECK':
            return 'UpdateLocalScriptPrecheckStepDetails'

        if type == 'INVOKE_FUNCTION_PRECHECK':
            return 'UpdateInvokeFunctionPrecheckStepDetails'

        if type == 'INVOKE_FUNCTION':
            return 'UpdateInvokeFunctionUserDefinedStepDetails'

        if type == 'RUN_OBJECTSTORE_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK':
            return 'UpdateRunObjectStoreScriptUserDefinedCustomPrecheckStepDetails'

        if type == 'INVOKE_FUNCTION_USER_DEFINED_CUSTOM_PRECHECK':
            return 'UpdateInvokeFunctionUserDefinedCustomPrecheckStepDetails'

        if type == 'RUN_OBJECTSTORE_SCRIPT':
            return 'UpdateRunObjectStoreScriptUserDefinedStepDetails'

        if type == 'RUN_OBJECTSTORE_SCRIPT_PRECHECK':
            return 'UpdateObjectStoreScriptPrecheckStepDetails'

        if type == 'RUN_LOCAL_SCRIPT':
            return 'UpdateRunLocalScriptUserDefinedStepDetails'
        else:
            return 'UpdateDrPlanUserDefinedStepDetails'

    @property
    def step_type(self):
        """
        **[Required]** Gets the step_type of this UpdateDrPlanUserDefinedStepDetails.
        The type of the user-defined step.

          **RUN_OBJECTSTORE_SCRIPT_PRECHECK** - A built-in step which performs a precheck on a script stored
            in OCI object storage.  This step cannot be added, deleted, or customized by the user.

          **RUN_LOCAL_SCRIPT_PRECHECK** - A built-in step which performs a precheck on a script which resides
            locally on a compute instance.  This step cannot be added, deleted, or customized by the user.

          **INVOKE_FUNCTION_PRECHECK** - A built-in step which performs a precheck on an OCI function.  This
            step cannot be added, deleted, or customized by the user.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

          **RUN_OBJECTSTORE_SCRIPT** - A step which runs a script stored in OCI object storage.

          **RUN_LOCAL_SCRIPT** - A step which runs a script that resides locally on a compute instance.

          **INVOKE_FUNCTION** - A step which invokes an OCI function.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

          **RUN_OBJECTSTORE_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK** - A user-defined step which performs a precheck by executing a user-provided script stored
            in OCI object storage.

          **RUN_LOCAL_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK** - A user-defined step which performs a precheck by executing a user-provided script which resides
            locally on a compute instance.

          **INVOKE_FUNCTION_USER_DEFINED_CUSTOM_PRECHECK** - A user-defined step which performs a precheck by executing a user-provided OCI function.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

        Allowed values for this property are: "RUN_OBJECTSTORE_SCRIPT_PRECHECK", "RUN_LOCAL_SCRIPT_PRECHECK", "INVOKE_FUNCTION_PRECHECK", "RUN_OBJECTSTORE_SCRIPT", "RUN_LOCAL_SCRIPT", "INVOKE_FUNCTION", "RUN_OBJECTSTORE_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK", "RUN_LOCAL_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK", "INVOKE_FUNCTION_USER_DEFINED_CUSTOM_PRECHECK"


        :return: The step_type of this UpdateDrPlanUserDefinedStepDetails.
        :rtype: str
        """
        return self._step_type

    @step_type.setter
    def step_type(self, step_type):
        """
        Sets the step_type of this UpdateDrPlanUserDefinedStepDetails.
        The type of the user-defined step.

          **RUN_OBJECTSTORE_SCRIPT_PRECHECK** - A built-in step which performs a precheck on a script stored
            in OCI object storage.  This step cannot be added, deleted, or customized by the user.

          **RUN_LOCAL_SCRIPT_PRECHECK** - A built-in step which performs a precheck on a script which resides
            locally on a compute instance.  This step cannot be added, deleted, or customized by the user.

          **INVOKE_FUNCTION_PRECHECK** - A built-in step which performs a precheck on an OCI function.  This
            step cannot be added, deleted, or customized by the user.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

          **RUN_OBJECTSTORE_SCRIPT** - A step which runs a script stored in OCI object storage.

          **RUN_LOCAL_SCRIPT** - A step which runs a script that resides locally on a compute instance.

          **INVOKE_FUNCTION** - A step which invokes an OCI function.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

          **RUN_OBJECTSTORE_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK** - A user-defined step which performs a precheck by executing a user-provided script stored
            in OCI object storage.

          **RUN_LOCAL_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK** - A user-defined step which performs a precheck by executing a user-provided script which resides
            locally on a compute instance.

          **INVOKE_FUNCTION_USER_DEFINED_CUSTOM_PRECHECK** - A user-defined step which performs a precheck by executing a user-provided OCI function.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.


        :param step_type: The step_type of this UpdateDrPlanUserDefinedStepDetails.
        :type: str
        """
        allowed_values = ["RUN_OBJECTSTORE_SCRIPT_PRECHECK", "RUN_LOCAL_SCRIPT_PRECHECK", "INVOKE_FUNCTION_PRECHECK", "RUN_OBJECTSTORE_SCRIPT", "RUN_LOCAL_SCRIPT", "INVOKE_FUNCTION", "RUN_OBJECTSTORE_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK", "RUN_LOCAL_SCRIPT_USER_DEFINED_CUSTOM_PRECHECK", "INVOKE_FUNCTION_USER_DEFINED_CUSTOM_PRECHECK"]
        if not value_allowed_none_or_none_sentinel(step_type, allowed_values):
            raise ValueError(
                f"Invalid value for `step_type`, must be None or one of {allowed_values}"
            )
        self._step_type = step_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
