# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupFailurePolicy(object):
    """
    Specifies a failure policy for a compute instance group rolling deployment stage.
    """

    #: A constant which can be used with the policy_type property of a ComputeInstanceGroupFailurePolicy.
    #: This constant has a value of "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT"
    POLICY_TYPE_COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT = "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT"

    #: A constant which can be used with the policy_type property of a ComputeInstanceGroupFailurePolicy.
    #: This constant has a value of "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE"
    POLICY_TYPE_COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE = "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupFailurePolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.ComputeInstanceGroupFailurePolicyByPercentage`
        * :class:`~oci.devops.models.ComputeInstanceGroupFailurePolicyByCount`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this ComputeInstanceGroupFailurePolicy.
            Allowed values for this property are: "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT", "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
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

        if type == 'COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE':
            return 'ComputeInstanceGroupFailurePolicyByPercentage'

        if type == 'COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT':
            return 'ComputeInstanceGroupFailurePolicyByCount'
        else:
            return 'ComputeInstanceGroupFailurePolicy'

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this ComputeInstanceGroupFailurePolicy.
        Specifies if the failure instance size is given by absolute number or by percentage.

        Allowed values for this property are: "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT", "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The policy_type of this ComputeInstanceGroupFailurePolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this ComputeInstanceGroupFailurePolicy.
        Specifies if the failure instance size is given by absolute number or by percentage.


        :param policy_type: The policy_type of this ComputeInstanceGroupFailurePolicy.
        :type: str
        """
        allowed_values = ["COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT", "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE"]
        if not value_allowed_none_or_none_sentinel(policy_type, allowed_values):
            policy_type = 'UNKNOWN_ENUM_VALUE'
        self._policy_type = policy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
