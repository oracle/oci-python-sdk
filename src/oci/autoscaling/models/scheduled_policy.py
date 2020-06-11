# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .auto_scaling_policy import AutoScalingPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledPolicy(AutoScalingPolicy):
    """
    An autoscaling policy that defines execution schedules for an autoscaling configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.autoscaling.models.ScheduledPolicy.policy_type` attribute
        of this class is ``scheduled`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity:
            The value to assign to the capacity property of this ScheduledPolicy.
        :type capacity: Capacity

        :param id:
            The value to assign to the id property of this ScheduledPolicy.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ScheduledPolicy.
        :type display_name: str

        :param policy_type:
            The value to assign to the policy_type property of this ScheduledPolicy.
        :type policy_type: str

        :param time_created:
            The value to assign to the time_created property of this ScheduledPolicy.
        :type time_created: datetime

        :param is_enabled:
            The value to assign to the is_enabled property of this ScheduledPolicy.
        :type is_enabled: bool

        :param execution_schedule:
            The value to assign to the execution_schedule property of this ScheduledPolicy.
        :type execution_schedule: ExecutionSchedule

        """
        self.swagger_types = {
            'capacity': 'Capacity',
            'id': 'str',
            'display_name': 'str',
            'policy_type': 'str',
            'time_created': 'datetime',
            'is_enabled': 'bool',
            'execution_schedule': 'ExecutionSchedule'
        }

        self.attribute_map = {
            'capacity': 'capacity',
            'id': 'id',
            'display_name': 'displayName',
            'policy_type': 'policyType',
            'time_created': 'timeCreated',
            'is_enabled': 'isEnabled',
            'execution_schedule': 'executionSchedule'
        }

        self._capacity = None
        self._id = None
        self._display_name = None
        self._policy_type = None
        self._time_created = None
        self._is_enabled = None
        self._execution_schedule = None
        self._policy_type = 'scheduled'

    @property
    def execution_schedule(self):
        """
        **[Required]** Gets the execution_schedule of this ScheduledPolicy.

        :return: The execution_schedule of this ScheduledPolicy.
        :rtype: ExecutionSchedule
        """
        return self._execution_schedule

    @execution_schedule.setter
    def execution_schedule(self, execution_schedule):
        """
        Sets the execution_schedule of this ScheduledPolicy.

        :param execution_schedule: The execution_schedule of this ScheduledPolicy.
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
