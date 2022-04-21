# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .auto_scale_policy_details import AutoScalePolicyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleBasedVerticalScalingPolicyDetails(AutoScalePolicyDetails):
    """
    Details of a schedule based vertical autoscaling policy.

    In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleBasedVerticalScalingPolicyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.ScheduleBasedVerticalScalingPolicyDetails.policy_type` attribute
        of this class is ``SCHEDULE_BASED_VERTICAL_SCALING_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this ScheduleBasedVerticalScalingPolicyDetails.
            Allowed values for this property are: "METRIC_BASED_VERTICAL_SCALING_POLICY", "METRIC_BASED_HORIZONTAL_SCALING_POLICY", "SCHEDULE_BASED_VERTICAL_SCALING_POLICY", "SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY"
        :type policy_type: str

        :param trigger_type:
            The value to assign to the trigger_type property of this ScheduleBasedVerticalScalingPolicyDetails.
            Allowed values for this property are: "METRIC_BASED", "SCHEDULE_BASED"
        :type trigger_type: str

        :param action_type:
            The value to assign to the action_type property of this ScheduleBasedVerticalScalingPolicyDetails.
            Allowed values for this property are: "VERTICAL_SCALING", "HORIZONTAL_SCALING"
        :type action_type: str

        :param timezone:
            The value to assign to the timezone property of this ScheduleBasedVerticalScalingPolicyDetails.
        :type timezone: str

        :param schedule_details:
            The value to assign to the schedule_details property of this ScheduleBasedVerticalScalingPolicyDetails.
        :type schedule_details: list[oci.bds.models.VerticalScalingScheduleDetails]

        """
        self.swagger_types = {
            'policy_type': 'str',
            'trigger_type': 'str',
            'action_type': 'str',
            'timezone': 'str',
            'schedule_details': 'list[VerticalScalingScheduleDetails]'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'trigger_type': 'triggerType',
            'action_type': 'actionType',
            'timezone': 'timezone',
            'schedule_details': 'scheduleDetails'
        }

        self._policy_type = None
        self._trigger_type = None
        self._action_type = None
        self._timezone = None
        self._schedule_details = None
        self._policy_type = 'SCHEDULE_BASED_VERTICAL_SCALING_POLICY'

    @property
    def timezone(self):
        """
        Gets the timezone of this ScheduleBasedVerticalScalingPolicyDetails.
        The time zone of the execution schedule, in IANA time zone database name format


        :return: The timezone of this ScheduleBasedVerticalScalingPolicyDetails.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ScheduleBasedVerticalScalingPolicyDetails.
        The time zone of the execution schedule, in IANA time zone database name format


        :param timezone: The timezone of this ScheduleBasedVerticalScalingPolicyDetails.
        :type: str
        """
        self._timezone = timezone

    @property
    def schedule_details(self):
        """
        Gets the schedule_details of this ScheduleBasedVerticalScalingPolicyDetails.

        :return: The schedule_details of this ScheduleBasedVerticalScalingPolicyDetails.
        :rtype: list[oci.bds.models.VerticalScalingScheduleDetails]
        """
        return self._schedule_details

    @schedule_details.setter
    def schedule_details(self, schedule_details):
        """
        Sets the schedule_details of this ScheduleBasedVerticalScalingPolicyDetails.

        :param schedule_details: The schedule_details of this ScheduleBasedVerticalScalingPolicyDetails.
        :type: list[oci.bds.models.VerticalScalingScheduleDetails]
        """
        self._schedule_details = schedule_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
