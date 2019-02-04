# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyRule(object):
    """
    Configuration for sorting and/or filtering the list of remaining candidate answers, subject to
    rule type and the values of type-specific parameters and/or data associated with answers.

    A rule may optionally include a sequence of cases, each with an optional `caseCondition`
    expression.  If it does, the first case with a matching `caseCondition` or with no
    `caseCondition` at all is used to set rule parameter values and/or answer-associated data,
    and the rule will be ignored during processing of any request that does not match any case.
    Rules without a sequence of cases are processed unconditionally, and rules with an _empty_
    sequence of cases are **ignored** unconditionally.

    Data is associated with answers one-by-one in a similar fashion\u2014for each answer, the first
    answerData item with a matching `answerCondition` or with no `answerCondition` at all is used
    to associate data with the answer, and the absence of any such item associates with the answer
    a default value.  Rule-level default answer data is always processed, but case-level answer
    data will override it on a per-answer basis.

    To prevent empty responses, any attempt to filter away all answers is suppressed at runtime.
    """

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "FILTER"
    RULE_TYPE_FILTER = "FILTER"

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "HEALTH"
    RULE_TYPE_HEALTH = "HEALTH"

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "WEIGHTED"
    RULE_TYPE_WEIGHTED = "WEIGHTED"

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "PRIORITY"
    RULE_TYPE_PRIORITY = "PRIORITY"

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "LIMIT"
    RULE_TYPE_LIMIT = "LIMIT"

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyRule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.dns.models.SteeringPolicyFilterRule`
        * :class:`~oci.dns.models.SteeringPolicyWeightedRule`
        * :class:`~oci.dns.models.SteeringPolicyLimitRule`
        * :class:`~oci.dns.models.SteeringPolicyHealthRule`
        * :class:`~oci.dns.models.SteeringPolicyPriorityRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this SteeringPolicyRule.
        :type description: str

        :param rule_type:
            The value to assign to the rule_type property of this SteeringPolicyRule.
            Allowed values for this property are: "FILTER", "HEALTH", "WEIGHTED", "PRIORITY", "LIMIT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rule_type: str

        """
        self.swagger_types = {
            'description': 'str',
            'rule_type': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'rule_type': 'ruleType'
        }

        self._description = None
        self._rule_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['ruleType']

        if type == 'FILTER':
            return 'SteeringPolicyFilterRule'

        if type == 'WEIGHTED':
            return 'SteeringPolicyWeightedRule'

        if type == 'LIMIT':
            return 'SteeringPolicyLimitRule'

        if type == 'HEALTH':
            return 'SteeringPolicyHealthRule'

        if type == 'PRIORITY':
            return 'SteeringPolicyPriorityRule'
        else:
            return 'SteeringPolicyRule'

    @property
    def description(self):
        """
        Gets the description of this SteeringPolicyRule.
        Your description of the rule's purpose and/or behavior.


        :return: The description of this SteeringPolicyRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SteeringPolicyRule.
        Your description of the rule's purpose and/or behavior.


        :param description: The description of this SteeringPolicyRule.
        :type: str
        """
        self._description = description

    @property
    def rule_type(self):
        """
        **[Required]** Gets the rule_type of this SteeringPolicyRule.
        The type of a rule determines its sorting/filtering behavior.
        - FILTER rules filter the list of answers (e.g., to remove those with hosts that are down
          for maintenance). Answers remain if and only if their associated data is `true`.
        - HEALTH rules remove answers from the list if their `rdata` matches a target in the
          health check monitor referenced by the steering policy and the target is reported down.
        - WEIGHTED rules probabilistically move answers with greater associated integer data to
          the beginning of the list.
        - PRIORITY rules sort answers by associated integer data, moving those with the lowest
          values to the beginning of the list without changing the relative order of those with
          the same value.
        - LIMIT rules filter away answers that are too far down the list. Parameter \"count\"
          specifies how many answers to keep.

        Allowed values for this property are: "FILTER", "HEALTH", "WEIGHTED", "PRIORITY", "LIMIT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rule_type of this SteeringPolicyRule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """
        Sets the rule_type of this SteeringPolicyRule.
        The type of a rule determines its sorting/filtering behavior.
        - FILTER rules filter the list of answers (e.g., to remove those with hosts that are down
          for maintenance). Answers remain if and only if their associated data is `true`.
        - HEALTH rules remove answers from the list if their `rdata` matches a target in the
          health check monitor referenced by the steering policy and the target is reported down.
        - WEIGHTED rules probabilistically move answers with greater associated integer data to
          the beginning of the list.
        - PRIORITY rules sort answers by associated integer data, moving those with the lowest
          values to the beginning of the list without changing the relative order of those with
          the same value.
        - LIMIT rules filter away answers that are too far down the list. Parameter \"count\"
          specifies how many answers to keep.


        :param rule_type: The rule_type of this SteeringPolicyRule.
        :type: str
        """
        allowed_values = ["FILTER", "HEALTH", "WEIGHTED", "PRIORITY", "LIMIT"]
        if not value_allowed_none_or_none_sentinel(rule_type, allowed_values):
            rule_type = 'UNKNOWN_ENUM_VALUE'
        self._rule_type = rule_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
