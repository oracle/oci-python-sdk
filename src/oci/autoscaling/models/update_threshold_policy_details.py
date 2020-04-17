# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_auto_scaling_policy_details import UpdateAutoScalingPolicyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateThresholdPolicyDetails(UpdateAutoScalingPolicyDetails):
    """
    UpdateThresholdPolicyDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateThresholdPolicyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.autoscaling.models.UpdateThresholdPolicyDetails.policy_type` attribute
        of this class is ``threshold`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateThresholdPolicyDetails.
        :type display_name: str

        :param capacity:
            The value to assign to the capacity property of this UpdateThresholdPolicyDetails.
        :type capacity: Capacity

        :param policy_type:
            The value to assign to the policy_type property of this UpdateThresholdPolicyDetails.
        :type policy_type: str

        :param rules:
            The value to assign to the rules property of this UpdateThresholdPolicyDetails.
        :type rules: list[UpdateConditionDetails]

        """
        self.swagger_types = {
            'display_name': 'str',
            'capacity': 'Capacity',
            'policy_type': 'str',
            'rules': 'list[UpdateConditionDetails]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'capacity': 'capacity',
            'policy_type': 'policyType',
            'rules': 'rules'
        }

        self._display_name = None
        self._capacity = None
        self._policy_type = None
        self._rules = None
        self._policy_type = 'threshold'

    @property
    def rules(self):
        """
        Gets the rules of this UpdateThresholdPolicyDetails.

        :return: The rules of this UpdateThresholdPolicyDetails.
        :rtype: list[UpdateConditionDetails]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this UpdateThresholdPolicyDetails.

        :param rules: The rules of this UpdateThresholdPolicyDetails.
        :type: list[UpdateConditionDetails]
        """
        self._rules = rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
