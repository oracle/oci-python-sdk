# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_auto_scaling_policy_details import CreateAutoScalingPolicyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateScheduledPolicyDetails(CreateAutoScalingPolicyDetails):
    """
    Creation details for a schedule-based autoscaling policy.

    In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateScheduledPolicyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.autoscaling.models.CreateScheduledPolicyDetails.policy_type` attribute
        of this class is ``scheduled`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity:
            The value to assign to the capacity property of this CreateScheduledPolicyDetails.
        :type capacity: oci.autoscaling.models.Capacity

        :param display_name:
            The value to assign to the display_name property of this CreateScheduledPolicyDetails.
        :type display_name: str

        :param policy_type:
            The value to assign to the policy_type property of this CreateScheduledPolicyDetails.
        :type policy_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateScheduledPolicyDetails.
        :type is_enabled: bool

        :param execution_schedule:
            The value to assign to the execution_schedule property of this CreateScheduledPolicyDetails.
        :type execution_schedule: oci.autoscaling.models.ExecutionSchedule

        :param resource_action:
            The value to assign to the resource_action property of this CreateScheduledPolicyDetails.
        :type resource_action: oci.autoscaling.models.ResourceAction

        """
        self.swagger_types = {
            'capacity': 'Capacity',
            'display_name': 'str',
            'policy_type': 'str',
            'is_enabled': 'bool',
            'execution_schedule': 'ExecutionSchedule',
            'resource_action': 'ResourceAction'
        }

        self.attribute_map = {
            'capacity': 'capacity',
            'display_name': 'displayName',
            'policy_type': 'policyType',
            'is_enabled': 'isEnabled',
            'execution_schedule': 'executionSchedule',
            'resource_action': 'resourceAction'
        }

        self._capacity = None
        self._display_name = None
        self._policy_type = None
        self._is_enabled = None
        self._execution_schedule = None
        self._resource_action = None
        self._policy_type = 'scheduled'

    @property
    def execution_schedule(self):
        """
        **[Required]** Gets the execution_schedule of this CreateScheduledPolicyDetails.

        :return: The execution_schedule of this CreateScheduledPolicyDetails.
        :rtype: oci.autoscaling.models.ExecutionSchedule
        """
        return self._execution_schedule

    @execution_schedule.setter
    def execution_schedule(self, execution_schedule):
        """
        Sets the execution_schedule of this CreateScheduledPolicyDetails.

        :param execution_schedule: The execution_schedule of this CreateScheduledPolicyDetails.
        :type: oci.autoscaling.models.ExecutionSchedule
        """
        self._execution_schedule = execution_schedule

    @property
    def resource_action(self):
        """
        Gets the resource_action of this CreateScheduledPolicyDetails.

        :return: The resource_action of this CreateScheduledPolicyDetails.
        :rtype: oci.autoscaling.models.ResourceAction
        """
        return self._resource_action

    @resource_action.setter
    def resource_action(self, resource_action):
        """
        Sets the resource_action of this CreateScheduledPolicyDetails.

        :param resource_action: The resource_action of this CreateScheduledPolicyDetails.
        :type: oci.autoscaling.models.ResourceAction
        """
        self._resource_action = resource_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
