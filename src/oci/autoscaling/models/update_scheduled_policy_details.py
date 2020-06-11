# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_auto_scaling_policy_details import UpdateAutoScalingPolicyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateScheduledPolicyDetails(UpdateAutoScalingPolicyDetails):
    """
    UpdateScheduledPolicyDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateScheduledPolicyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.autoscaling.models.UpdateScheduledPolicyDetails.policy_type` attribute
        of this class is ``scheduled`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateScheduledPolicyDetails.
        :type display_name: str

        :param capacity:
            The value to assign to the capacity property of this UpdateScheduledPolicyDetails.
        :type capacity: Capacity

        :param policy_type:
            The value to assign to the policy_type property of this UpdateScheduledPolicyDetails.
        :type policy_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateScheduledPolicyDetails.
        :type is_enabled: bool

        :param execution_schedule:
            The value to assign to the execution_schedule property of this UpdateScheduledPolicyDetails.
        :type execution_schedule: ExecutionSchedule

        """
        self.swagger_types = {
            'display_name': 'str',
            'capacity': 'Capacity',
            'policy_type': 'str',
            'is_enabled': 'bool',
            'execution_schedule': 'ExecutionSchedule'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'capacity': 'capacity',
            'policy_type': 'policyType',
            'is_enabled': 'isEnabled',
            'execution_schedule': 'executionSchedule'
        }

        self._display_name = None
        self._capacity = None
        self._policy_type = None
        self._is_enabled = None
        self._execution_schedule = None
        self._policy_type = 'scheduled'

    @property
    def execution_schedule(self):
        """
        Gets the execution_schedule of this UpdateScheduledPolicyDetails.

        :return: The execution_schedule of this UpdateScheduledPolicyDetails.
        :rtype: ExecutionSchedule
        """
        return self._execution_schedule

    @execution_schedule.setter
    def execution_schedule(self, execution_schedule):
        """
        Sets the execution_schedule of this UpdateScheduledPolicyDetails.

        :param execution_schedule: The execution_schedule of this UpdateScheduledPolicyDetails.
        :type: ExecutionSchedule
        """
        self._execution_schedule = execution_schedule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
