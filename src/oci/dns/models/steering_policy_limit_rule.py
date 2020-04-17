# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
        An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate
        configurations for how it should behave during processing for any given DNS query. When a rule has
        no sequence of `cases`, it is always evaluated with the same configuration during processing. When
        a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a
        non-empty sequence of `cases`, its behavior during processing is configured by the first matching
        `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no
        `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression
        evaluates to true for the given query.


        :return: The cases of this SteeringPolicyLimitRule.
        :rtype: list[SteeringPolicyLimitRuleCase]
        """
        return self._cases

    @cases.setter
    def cases(self, cases):
        """
        Sets the cases of this SteeringPolicyLimitRule.
        An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate
        configurations for how it should behave during processing for any given DNS query. When a rule has
        no sequence of `cases`, it is always evaluated with the same configuration during processing. When
        a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a
        non-empty sequence of `cases`, its behavior during processing is configured by the first matching
        `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no
        `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression
        evaluates to true for the given query.


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
        are no matching cases. In this scenario, the next rule will be processed. If no rules
        remain to be processed, the answer will be chosen from the remaining list of answers.


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
        are no matching cases. In this scenario, the next rule will be processed. If no rules
        remain to be processed, the answer will be chosen from the remaining list of answers.


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
