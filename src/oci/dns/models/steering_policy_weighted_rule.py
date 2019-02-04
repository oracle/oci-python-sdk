# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .steering_policy_rule import SteeringPolicyRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyWeightedRule(SteeringPolicyRule):
    """
    SteeringPolicyWeightedRule model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyWeightedRule object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.SteeringPolicyWeightedRule.rule_type` attribute
        of this class is ``WEIGHTED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this SteeringPolicyWeightedRule.
        :type description: str

        :param rule_type:
            The value to assign to the rule_type property of this SteeringPolicyWeightedRule.
            Allowed values for this property are: "FILTER", "HEALTH", "WEIGHTED", "PRIORITY", "LIMIT"
        :type rule_type: str

        :param cases:
            The value to assign to the cases property of this SteeringPolicyWeightedRule.
        :type cases: list[SteeringPolicyWeightedRuleCase]

        :param default_answer_data:
            The value to assign to the default_answer_data property of this SteeringPolicyWeightedRule.
        :type default_answer_data: list[SteeringPolicyWeightedAnswerData]

        """
        self.swagger_types = {
            'description': 'str',
            'rule_type': 'str',
            'cases': 'list[SteeringPolicyWeightedRuleCase]',
            'default_answer_data': 'list[SteeringPolicyWeightedAnswerData]'
        }

        self.attribute_map = {
            'description': 'description',
            'rule_type': 'ruleType',
            'cases': 'cases',
            'default_answer_data': 'defaultAnswerData'
        }

        self._description = None
        self._rule_type = None
        self._cases = None
        self._default_answer_data = None
        self._rule_type = 'WEIGHTED'

    @property
    def cases(self):
        """
        Gets the cases of this SteeringPolicyWeightedRule.

        :return: The cases of this SteeringPolicyWeightedRule.
        :rtype: list[SteeringPolicyWeightedRuleCase]
        """
        return self._cases

    @cases.setter
    def cases(self, cases):
        """
        Sets the cases of this SteeringPolicyWeightedRule.

        :param cases: The cases of this SteeringPolicyWeightedRule.
        :type: list[SteeringPolicyWeightedRuleCase]
        """
        self._cases = cases

    @property
    def default_answer_data(self):
        """
        Gets the default_answer_data of this SteeringPolicyWeightedRule.
        Defines a default set of answer conditions and values that are applied to an answer when
        `cases` is not defined for the rule or a matching case does not have any matching
        `answerCondition`s in its `answerData`. `defaultAnswerData` is **not** applied if `cases` is
        defined and there are no matching cases.


        :return: The default_answer_data of this SteeringPolicyWeightedRule.
        :rtype: list[SteeringPolicyWeightedAnswerData]
        """
        return self._default_answer_data

    @default_answer_data.setter
    def default_answer_data(self, default_answer_data):
        """
        Sets the default_answer_data of this SteeringPolicyWeightedRule.
        Defines a default set of answer conditions and values that are applied to an answer when
        `cases` is not defined for the rule or a matching case does not have any matching
        `answerCondition`s in its `answerData`. `defaultAnswerData` is **not** applied if `cases` is
        defined and there are no matching cases.


        :param default_answer_data: The default_answer_data of this SteeringPolicyWeightedRule.
        :type: list[SteeringPolicyWeightedAnswerData]
        """
        self._default_answer_data = default_answer_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
