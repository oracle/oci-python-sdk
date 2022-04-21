# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalePolicy(object):
    """
    This model for autoscaling policy is deprecated and not supported for ODH clusters. Use the `AutoScalePolicyDetails` model to manage autoscale policy details for ODH clusters.
    """

    #: A constant which can be used with the policy_type property of a AutoScalePolicy.
    #: This constant has a value of "THRESHOLD_BASED"
    POLICY_TYPE_THRESHOLD_BASED = "THRESHOLD_BASED"

    #: A constant which can be used with the policy_type property of a AutoScalePolicy.
    #: This constant has a value of "SCHEDULE_BASED"
    POLICY_TYPE_SCHEDULE_BASED = "SCHEDULE_BASED"

    #: A constant which can be used with the policy_type property of a AutoScalePolicy.
    #: This constant has a value of "NONE"
    POLICY_TYPE_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalePolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this AutoScalePolicy.
            Allowed values for this property are: "THRESHOLD_BASED", "SCHEDULE_BASED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type policy_type: str

        :param rules:
            The value to assign to the rules property of this AutoScalePolicy.
        :type rules: list[oci.bds.models.AutoScalePolicyRule]

        """
        self.swagger_types = {
            'policy_type': 'str',
            'rules': 'list[AutoScalePolicyRule]'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'rules': 'rules'
        }

        self._policy_type = None
        self._rules = None

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this AutoScalePolicy.
        Types of autoscale policies. Options are SCHEDULE-BASED or THRESHOLD-BASED. (Only THRESHOLD-BASED is supported in this release.)

        Allowed values for this property are: "THRESHOLD_BASED", "SCHEDULE_BASED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The policy_type of this AutoScalePolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this AutoScalePolicy.
        Types of autoscale policies. Options are SCHEDULE-BASED or THRESHOLD-BASED. (Only THRESHOLD-BASED is supported in this release.)


        :param policy_type: The policy_type of this AutoScalePolicy.
        :type: str
        """
        allowed_values = ["THRESHOLD_BASED", "SCHEDULE_BASED", "NONE"]
        if not value_allowed_none_or_none_sentinel(policy_type, allowed_values):
            policy_type = 'UNKNOWN_ENUM_VALUE'
        self._policy_type = policy_type

    @property
    def rules(self):
        """
        **[Required]** Gets the rules of this AutoScalePolicy.
        The list of rules for autoscaling. If an action has multiple rules, the last rule in the array will be applied.


        :return: The rules of this AutoScalePolicy.
        :rtype: list[oci.bds.models.AutoScalePolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this AutoScalePolicy.
        The list of rules for autoscaling. If an action has multiple rules, the last rule in the array will be applied.


        :param rules: The rules of this AutoScalePolicy.
        :type: list[oci.bds.models.AutoScalePolicyRule]
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
