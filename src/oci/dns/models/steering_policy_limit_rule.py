# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .steering_policy_rule import SteeringPolicyRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyLimitRule(SteeringPolicyRule):
    """
    SteeringPolicyLimitRule model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyLimitRule object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.SteeringPolicyLimitRule.rule_type` attribute
        of this class is ``LIMIT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this SteeringPolicyLimitRule.
        :type description: str

        :param rule_type:
            The value to assign to the rule_type property of this SteeringPolicyLimitRule.
            Allowed values for this property are: "FILTER", "HEALTH", "WEIGHTED", "PRIORITY", "LIMIT"
        :type rule_type: str

        :param cases:
            The value to assign to the cases property of this SteeringPolicyLimitRule.
        :type cases: list[SteeringPolicyLimitRuleCase]

        :param default_count:
            The value to assign to the default_count property of this SteeringPolicyLimitRule.
        :type default_count: int

        """
        self.swagger_types = {
            'description': 'str',
            'rule_type': 'str',
            'cases': 'list[SteeringPolicyLimitRuleCase]',
            'default_count': 'int'
        }

        self.attribute_map = {
            'description': 'description',
            'rule_type': 'ruleType',
            'cases': 'cases',
            'default_count': 'defaultCount'
        }

        self._description = None
        self._rule_type = None
        self._cases = None
        self._default_count = None
        self._rule_type = 'LIMIT'

    @property
    def cases(self):
        """
        Gets the cases of this SteeringPolicyLimitRule.

        :return: The cases of this SteeringPolicyLimitRule.
        :rtype: list[SteeringPolicyLimitRuleCase]
        """
        return self._cases

    @cases.setter
    def cases(self, cases):
        """
        Sets the cases of this SteeringPolicyLimitRule.

        :param cases: The cases of this SteeringPolicyLimitRule.
        :type: list[SteeringPolicyLimitRuleCase]
        """
        self._cases = cases

    @property
    def default_count(self):
        """
        Gets the default_count of this SteeringPolicyLimitRule.
        Defines a default count if `cases` is not defined for the rule or a matching case does
        not define `count`. `defaultCount` is **not** applied if `cases` is defined and there
        are no matching cases.


        :return: The default_count of this SteeringPolicyLimitRule.
        :rtype: int
        """
        return self._default_count

    @default_count.setter
    def default_count(self, default_count):
        """
        Sets the default_count of this SteeringPolicyLimitRule.
        Defines a default count if `cases` is not defined for the rule or a matching case does
        not define `count`. `defaultCount` is **not** applied if `cases` is defined and there
        are no matching cases.


        :param default_count: The default_count of this SteeringPolicyLimitRule.
        :type: int
        """
        self._default_count = default_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
