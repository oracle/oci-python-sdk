# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .compute_instance_group_failure_policy import ComputeInstanceGroupFailurePolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupFailurePolicyByCount(ComputeInstanceGroupFailurePolicy):
    """
    Specifies a failure policy by count for a compute instance group rolling deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupFailurePolicyByCount object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ComputeInstanceGroupFailurePolicyByCount.policy_type` attribute
        of this class is ``COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this ComputeInstanceGroupFailurePolicyByCount.
            Allowed values for this property are: "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT", "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE"
        :type policy_type: str

        :param failure_count:
            The value to assign to the failure_count property of this ComputeInstanceGroupFailurePolicyByCount.
        :type failure_count: int

        """
        self.swagger_types = {
            'policy_type': 'str',
            'failure_count': 'int'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'failure_count': 'failureCount'
        }

        self._policy_type = None
        self._failure_count = None
        self._policy_type = 'COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT'

    @property
    def failure_count(self):
        """
        **[Required]** Gets the failure_count of this ComputeInstanceGroupFailurePolicyByCount.
        The threshold count of failed instances in the group, which when reached or exceeded sets the stage as FAILED.


        :return: The failure_count of this ComputeInstanceGroupFailurePolicyByCount.
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        """
        Sets the failure_count of this ComputeInstanceGroupFailurePolicyByCount.
        The threshold count of failed instances in the group, which when reached or exceeded sets the stage as FAILED.


        :param failure_count: The failure_count of this ComputeInstanceGroupFailurePolicyByCount.
        :type: int
        """
        self._failure_count = failure_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
