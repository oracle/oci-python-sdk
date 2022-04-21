# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_auto_scale_policy_details import UpdateAutoScalePolicyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateScheduleBasedVerticalScalingPolicyDetails(UpdateAutoScalePolicyDetails):
    """
    Update details of a schedule based vertical autoscaling policy.

    In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateScheduleBasedVerticalScalingPolicyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.UpdateScheduleBasedVerticalScalingPolicyDetails.policy_type` attribute
        of this class is ``SCHEDULE_BASED_VERTICAL_SCALING_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this UpdateScheduleBasedVerticalScalingPolicyDetails.
        :type policy_type: str

        :param timezone:
            The value to assign to the timezone property of this UpdateScheduleBasedVerticalScalingPolicyDetails.
        :type timezone: str

        :param schedule_details:
            The value to assign to the schedule_details property of this UpdateScheduleBasedVerticalScalingPolicyDetails.
        :type schedule_details: list[oci.bds.models.VerticalScalingScheduleDetails]

        """
        self.swagger_types = {
            'policy_type': 'str',
            'timezone': 'str',
            'schedule_details': 'list[VerticalScalingScheduleDetails]'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'timezone': 'timezone',
            'schedule_details': 'scheduleDetails'
        }

        self._policy_type = None
        self._timezone = None
        self._schedule_details = None
        self._policy_type = 'SCHEDULE_BASED_VERTICAL_SCALING_POLICY'

    @property
    def timezone(self):
        """
        Gets the timezone of this UpdateScheduleBasedVerticalScalingPolicyDetails.
        The time zone of the execution schedule, in IANA time zone database name format


        :return: The timezone of this UpdateScheduleBasedVerticalScalingPolicyDetails.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this UpdateScheduleBasedVerticalScalingPolicyDetails.
        The time zone of the execution schedule, in IANA time zone database name format


        :param timezone: The timezone of this UpdateScheduleBasedVerticalScalingPolicyDetails.
        :type: str
        """
        self._timezone = timezone

    @property
    def schedule_details(self):
        """
        Gets the schedule_details of this UpdateScheduleBasedVerticalScalingPolicyDetails.

        :return: The schedule_details of this UpdateScheduleBasedVerticalScalingPolicyDetails.
        :rtype: list[oci.bds.models.VerticalScalingScheduleDetails]
        """
        return self._schedule_details

    @schedule_details.setter
    def schedule_details(self, schedule_details):
        """
        Sets the schedule_details of this UpdateScheduleBasedVerticalScalingPolicyDetails.

        :param schedule_details: The schedule_details of this UpdateScheduleBasedVerticalScalingPolicyDetails.
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
