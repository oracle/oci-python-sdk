# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
        :type cases: list[oci.dns.models.SteeringPolicyHealthRuleCase]

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
        An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate
        configurations for how it should behave during processing for any given DNS query. When a rule has
        no sequence of `cases`, it is always evaluated with the same configuration during processing. When
        a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a
        non-empty sequence of `cases`, its behavior during processing is configured by the first matching
        `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no
        `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression
        evaluates to true for the given query.


        :return: The cases of this SteeringPolicyHealthRule.
        :rtype: list[oci.dns.models.SteeringPolicyHealthRuleCase]
        """
        return self._cases

    @cases.setter
    def cases(self, cases):
        """
        Sets the cases of this SteeringPolicyHealthRule.
        An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate
        configurations for how it should behave during processing for any given DNS query. When a rule has
        no sequence of `cases`, it is always evaluated with the same configuration during processing. When
        a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a
        non-empty sequence of `cases`, its behavior during processing is configured by the first matching
        `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no
        `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression
        evaluates to true for the given query.


        :param cases: The cases of this SteeringPolicyHealthRule.
        :type: list[oci.dns.models.SteeringPolicyHealthRuleCase]
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
