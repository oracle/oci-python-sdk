# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .steering_policy_rule import SteeringPolicyRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyHealthRule(SteeringPolicyRule):
    """
    SteeringPolicyHealthRule model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyHealthRule object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.SteeringPolicyHealthRule.rule_type` attribute
        of this class is ``HEALTH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this SteeringPolicyHealthRule.
        :type description: str

        :param rule_type:
            The value to assign to the rule_type property of this SteeringPolicyHealthRule.
            Allowed values for this property are: "FILTER", "HEALTH", "WEIGHTED", "PRIORITY", "LIMIT"
        :type rule_type: str

        :param cases:
            The value to assign to the cases property of this SteeringPolicyHealthRule.
        :type cases: list[SteeringPolicyHealthRuleCase]

        """
        self.swagger_types = {
            'description': 'str',
            'rule_type': 'str',
            'cases': 'list[SteeringPolicyHealthRuleCase]'
        }

        self.attribute_map = {
            'description': 'description',
            'rule_type': 'ruleType',
            'cases': 'cases'
        }

        self._description = None
        self._rule_type = None
        self._cases = None
        self._rule_type = 'HEALTH'

    @property
    def cases(self):
        """
        Gets the cases of this SteeringPolicyHealthRule.

        :return: The cases of this SteeringPolicyHealthRule.
        :rtype: list[SteeringPolicyHealthRuleCase]
        """
        return self._cases

    @cases.setter
    def cases(self, cases):
        """
        Sets the cases of this SteeringPolicyHealthRule.

        :param cases: The cases of this SteeringPolicyHealthRule.
        :type: list[SteeringPolicyHealthRuleCase]
        """
        self._cases = cases

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
