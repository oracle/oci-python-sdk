# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddAutoScalePolicyDetails(object):
    """
    Policy definition for the autoscale configuration.

    An autoscaling policy is part of an autoscaling configuration. For more information, see
    `Autoscaling`__

    You can create following type of autoscaling policies:

    - **MetricBasedVerticalScalingPolicy:** Vertical autoscaling action is triggered when a performance metric exceeds a threshold
    - **MetricBasedHorizontalScalingPolicy:** Horizontal autoscaling action is triggered when a performance metric exceeds a threshold
    - **ScheduleBasedVerticalScalingPolicy:** Vertical autoscaling action is triggered at the specific times that you schedule.
    - **ScheduleBasedHorizontalScalingPolicy:** Horizontal autoscaling action is triggered at the specific times that you schedule.

    An autoscaling configuration can have one of above supported policies.

    __ https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-autoscale
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddAutoScalePolicyDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.bds.models.AddMetricBasedHorizontalScalingPolicyDetails`
        * :class:`~oci.bds.models.AddScheduleBasedVerticalScalingPolicyDetails`
        * :class:`~oci.bds.models.AddScheduleBasedHorizontalScalingPolicyDetails`
        * :class:`~oci.bds.models.AddMetricBasedVerticalScalingPolicyDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this AddAutoScalePolicyDetails.
        :type policy_type: str

        """
        self.swagger_types = {
            'policy_type': 'str'
        }
        self.attribute_map = {
            'policy_type': 'policyType'
        }
        self._policy_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['policyType']

        if type == 'METRIC_BASED_HORIZONTAL_SCALING_POLICY':
            return 'AddMetricBasedHorizontalScalingPolicyDetails'

        if type == 'SCHEDULE_BASED_VERTICAL_SCALING_POLICY':
            return 'AddScheduleBasedVerticalScalingPolicyDetails'

        if type == 'SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY':
            return 'AddScheduleBasedHorizontalScalingPolicyDetails'

        if type == 'METRIC_BASED_VERTICAL_SCALING_POLICY':
            return 'AddMetricBasedVerticalScalingPolicyDetails'
        else:
            return 'AddAutoScalePolicyDetails'

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this AddAutoScalePolicyDetails.
        Type of autoscaling policy.


        :return: The policy_type of this AddAutoScalePolicyDetails.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this AddAutoScalePolicyDetails.
        Type of autoscaling policy.


        :param policy_type: The policy_type of this AddAutoScalePolicyDetails.
        :type: str
        """
        self._policy_type = policy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
