# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .add_auto_scale_policy_details import AddAutoScalePolicyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddScheduleBasedHorizontalScalingPolicyDetails(AddAutoScalePolicyDetails):
    """
    Details of a schedule based horizontal autoscaling policy.

    In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddScheduleBasedHorizontalScalingPolicyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.AddScheduleBasedHorizontalScalingPolicyDetails.policy_type` attribute
        of this class is ``SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this AddScheduleBasedHorizontalScalingPolicyDetails.
        :type policy_type: str

        :param timezone:
            The value to assign to the timezone property of this AddScheduleBasedHorizontalScalingPolicyDetails.
        :type timezone: str

        :param schedule_details:
            The value to assign to the schedule_details property of this AddScheduleBasedHorizontalScalingPolicyDetails.
        :type schedule_details: list[oci.bds.models.HorizontalScalingScheduleDetails]

        """
        self.swagger_types = {
            'policy_type': 'str',
            'timezone': 'str',
            'schedule_details': 'list[HorizontalScalingScheduleDetails]'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'timezone': 'timezone',
            'schedule_details': 'scheduleDetails'
        }

        self._policy_type = None
        self._timezone = None
        self._schedule_details = None
        self._policy_type = 'SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY'

    @property
    def timezone(self):
        """
        Gets the timezone of this AddScheduleBasedHorizontalScalingPolicyDetails.
        The time zone of the execution schedule, in IANA time zone database name format


        :return: The timezone of this AddScheduleBasedHorizontalScalingPolicyDetails.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this AddScheduleBasedHorizontalScalingPolicyDetails.
        The time zone of the execution schedule, in IANA time zone database name format


        :param timezone: The timezone of this AddScheduleBasedHorizontalScalingPolicyDetails.
        :type: str
        """
        self._timezone = timezone

    @property
    def schedule_details(self):
        """
        Gets the schedule_details of this AddScheduleBasedHorizontalScalingPolicyDetails.

        :return: The schedule_details of this AddScheduleBasedHorizontalScalingPolicyDetails.
        :rtype: list[oci.bds.models.HorizontalScalingScheduleDetails]
        """
        return self._schedule_details

    @schedule_details.setter
    def schedule_details(self, schedule_details):
        """
        Sets the schedule_details of this AddScheduleBasedHorizontalScalingPolicyDetails.

        :param schedule_details: The schedule_details of this AddScheduleBasedHorizontalScalingPolicyDetails.
        :type: list[oci.bds.models.HorizontalScalingScheduleDetails]
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
