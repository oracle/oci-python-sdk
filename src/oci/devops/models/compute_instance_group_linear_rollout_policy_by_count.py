# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .compute_instance_group_rollout_policy import ComputeInstanceGroupRolloutPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupLinearRolloutPolicyByCount(ComputeInstanceGroupRolloutPolicy):
    """
    Specifies a linear rollout strategy for a compute instance group rolling deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupLinearRolloutPolicyByCount object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ComputeInstanceGroupLinearRolloutPolicyByCount.policy_type` attribute
        of this class is ``COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this ComputeInstanceGroupLinearRolloutPolicyByCount.
            Allowed values for this property are: "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT", "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE"
        :type policy_type: str

        :param batch_delay_in_seconds:
            The value to assign to the batch_delay_in_seconds property of this ComputeInstanceGroupLinearRolloutPolicyByCount.
        :type batch_delay_in_seconds: int

        :param batch_count:
            The value to assign to the batch_count property of this ComputeInstanceGroupLinearRolloutPolicyByCount.
        :type batch_count: int

        """
        self.swagger_types = {
            'policy_type': 'str',
            'batch_delay_in_seconds': 'int',
            'batch_count': 'int'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'batch_delay_in_seconds': 'batchDelayInSeconds',
            'batch_count': 'batchCount'
        }

        self._policy_type = None
        self._batch_delay_in_seconds = None
        self._batch_count = None
        self._policy_type = 'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT'

    @property
    def batch_count(self):
        """
        **[Required]** Gets the batch_count of this ComputeInstanceGroupLinearRolloutPolicyByCount.
        The number that will be used to determine how many instances will be deployed concurrently.


        :return: The batch_count of this ComputeInstanceGroupLinearRolloutPolicyByCount.
        :rtype: int
        """
        return self._batch_count

    @batch_count.setter
    def batch_count(self, batch_count):
        """
        Sets the batch_count of this ComputeInstanceGroupLinearRolloutPolicyByCount.
        The number that will be used to determine how many instances will be deployed concurrently.


        :param batch_count: The batch_count of this ComputeInstanceGroupLinearRolloutPolicyByCount.
        :type: int
        """
        self._batch_count = batch_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
