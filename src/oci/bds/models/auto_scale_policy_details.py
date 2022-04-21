# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalePolicyDetails(object):
    """
    Details of an autoscale policy.

    You can create following types of autoscaling policies:

    - **MetricBasedVerticalScalingPolicy:** Vertical autoscaling action is triggered when a performance metric exceeds a threshold
    - **MetricBasedHorizontalScalingPolicy:** Horizontal autoscaling action is triggered when a performance metric exceeds a threshold
    - **ScheduleBasedVerticalScalingPolicy:** Vertical autoscaling action is triggered at the specific times that you schedule.
    - **ScheduleBasedHorizontalScalingPolicy:** Horizontal autoscaling action is triggered at the specific times that you schedule.
    """

    #: A constant which can be used with the policy_type property of a AutoScalePolicyDetails.
    #: This constant has a value of "METRIC_BASED_VERTICAL_SCALING_POLICY"
    POLICY_TYPE_METRIC_BASED_VERTICAL_SCALING_POLICY = "METRIC_BASED_VERTICAL_SCALING_POLICY"

    #: A constant which can be used with the policy_type property of a AutoScalePolicyDetails.
    #: This constant has a value of "METRIC_BASED_HORIZONTAL_SCALING_POLICY"
    POLICY_TYPE_METRIC_BASED_HORIZONTAL_SCALING_POLICY = "METRIC_BASED_HORIZONTAL_SCALING_POLICY"

    #: A constant which can be used with the policy_type property of a AutoScalePolicyDetails.
    #: This constant has a value of "SCHEDULE_BASED_VERTICAL_SCALING_POLICY"
    POLICY_TYPE_SCHEDULE_BASED_VERTICAL_SCALING_POLICY = "SCHEDULE_BASED_VERTICAL_SCALING_POLICY"

    #: A constant which can be used with the policy_type property of a AutoScalePolicyDetails.
    #: This constant has a value of "SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY"
    POLICY_TYPE_SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY = "SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY"

    #: A constant which can be used with the trigger_type property of a AutoScalePolicyDetails.
    #: This constant has a value of "METRIC_BASED"
    TRIGGER_TYPE_METRIC_BASED = "METRIC_BASED"

    #: A constant which can be used with the trigger_type property of a AutoScalePolicyDetails.
    #: This constant has a value of "SCHEDULE_BASED"
    TRIGGER_TYPE_SCHEDULE_BASED = "SCHEDULE_BASED"

    #: A constant which can be used with the action_type property of a AutoScalePolicyDetails.
    #: This constant has a value of "VERTICAL_SCALING"
    ACTION_TYPE_VERTICAL_SCALING = "VERTICAL_SCALING"

    #: A constant which can be used with the action_type property of a AutoScalePolicyDetails.
    #: This constant has a value of "HORIZONTAL_SCALING"
    ACTION_TYPE_HORIZONTAL_SCALING = "HORIZONTAL_SCALING"

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalePolicyDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.bds.models.MetricBasedVerticalScalingPolicyDetails`
        * :class:`~oci.bds.models.ScheduleBasedVerticalScalingPolicyDetails`
        * :class:`~oci.bds.models.ScheduleBasedHorizontalScalingPolicyDetails`
        * :class:`~oci.bds.models.MetricBasedHorizontalScalingPolicyDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this AutoScalePolicyDetails.
            Allowed values for this property are: "METRIC_BASED_VERTICAL_SCALING_POLICY", "METRIC_BASED_HORIZONTAL_SCALING_POLICY", "SCHEDULE_BASED_VERTICAL_SCALING_POLICY", "SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type policy_type: str

        :param trigger_type:
            The value to assign to the trigger_type property of this AutoScalePolicyDetails.
            Allowed values for this property are: "METRIC_BASED", "SCHEDULE_BASED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type trigger_type: str

        :param action_type:
            The value to assign to the action_type property of this AutoScalePolicyDetails.
            Allowed values for this property are: "VERTICAL_SCALING", "HORIZONTAL_SCALING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action_type: str

        """
        self.swagger_types = {
            'policy_type': 'str',
            'trigger_type': 'str',
            'action_type': 'str'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'trigger_type': 'triggerType',
            'action_type': 'actionType'
        }

        self._policy_type = None
        self._trigger_type = None
        self._action_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['policyType']

        if type == 'METRIC_BASED_VERTICAL_SCALING_POLICY':
            return 'MetricBasedVerticalScalingPolicyDetails'

        if type == 'SCHEDULE_BASED_VERTICAL_SCALING_POLICY':
            return 'ScheduleBasedVerticalScalingPolicyDetails'

        if type == 'SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY':
            return 'ScheduleBasedHorizontalScalingPolicyDetails'

        if type == 'METRIC_BASED_HORIZONTAL_SCALING_POLICY':
            return 'MetricBasedHorizontalScalingPolicyDetails'
        else:
            return 'AutoScalePolicyDetails'

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this AutoScalePolicyDetails.
        Type of autoscaling policy.

        Allowed values for this property are: "METRIC_BASED_VERTICAL_SCALING_POLICY", "METRIC_BASED_HORIZONTAL_SCALING_POLICY", "SCHEDULE_BASED_VERTICAL_SCALING_POLICY", "SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The policy_type of this AutoScalePolicyDetails.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this AutoScalePolicyDetails.
        Type of autoscaling policy.


        :param policy_type: The policy_type of this AutoScalePolicyDetails.
        :type: str
        """
        allowed_values = ["METRIC_BASED_VERTICAL_SCALING_POLICY", "METRIC_BASED_HORIZONTAL_SCALING_POLICY", "SCHEDULE_BASED_VERTICAL_SCALING_POLICY", "SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY"]
        if not value_allowed_none_or_none_sentinel(policy_type, allowed_values):
            policy_type = 'UNKNOWN_ENUM_VALUE'
        self._policy_type = policy_type

    @property
    def trigger_type(self):
        """
        **[Required]** Gets the trigger_type of this AutoScalePolicyDetails.
        The type of autoscaling trigger.

        Allowed values for this property are: "METRIC_BASED", "SCHEDULE_BASED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The trigger_type of this AutoScalePolicyDetails.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """
        Sets the trigger_type of this AutoScalePolicyDetails.
        The type of autoscaling trigger.


        :param trigger_type: The trigger_type of this AutoScalePolicyDetails.
        :type: str
        """
        allowed_values = ["METRIC_BASED", "SCHEDULE_BASED"]
        if not value_allowed_none_or_none_sentinel(trigger_type, allowed_values):
            trigger_type = 'UNKNOWN_ENUM_VALUE'
        self._trigger_type = trigger_type

    @property
    def action_type(self):
        """
        **[Required]** Gets the action_type of this AutoScalePolicyDetails.
        The type of autoscaling action to take.

        Allowed values for this property are: "VERTICAL_SCALING", "HORIZONTAL_SCALING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action_type of this AutoScalePolicyDetails.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this AutoScalePolicyDetails.
        The type of autoscaling action to take.


        :param action_type: The action_type of this AutoScalePolicyDetails.
        :type: str
        """
        allowed_values = ["VERTICAL_SCALING", "HORIZONTAL_SCALING"]
        if not value_allowed_none_or_none_sentinel(action_type, allowed_values):
            action_type = 'UNKNOWN_ENUM_VALUE'
        self._action_type = action_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
