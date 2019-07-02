# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListenerRuleSummary(object):
    """
    Information about a Rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ListenerRuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rule:
            The value to assign to the rule property of this ListenerRuleSummary.
        :type rule: Rule

        :param rule_set_name:
            The value to assign to the rule_set_name property of this ListenerRuleSummary.
        :type rule_set_name: str

        """
        self.swagger_types = {
            'rule': 'Rule',
            'rule_set_name': 'str'
        }

        self.attribute_map = {
            'rule': 'rule',
            'rule_set_name': 'ruleSetName'
        }

        self._rule = None
        self._rule_set_name = None

    @property
    def rule(self):
        """
        Gets the rule of this ListenerRuleSummary.
        Rule object that was applied to a listener.


        :return: The rule of this ListenerRuleSummary.
        :rtype: Rule
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """
        Sets the rule of this ListenerRuleSummary.
        Rule object that was applied to a listener.


        :param rule: The rule of this ListenerRuleSummary.
        :type: Rule
        """
        self._rule = rule

    @property
    def rule_set_name(self):
        """
        Gets the rule_set_name of this ListenerRuleSummary.
        Name of the ruleset to which rule belongs to


        :return: The rule_set_name of this ListenerRuleSummary.
        :rtype: str
        """
        return self._rule_set_name

    @rule_set_name.setter
    def rule_set_name(self, rule_set_name):
        """
        Sets the rule_set_name of this ListenerRuleSummary.
        Name of the ruleset to which rule belongs to


        :param rule_set_name: The rule_set_name of this ListenerRuleSummary.
        :type: str
        """
        self._rule_set_name = rule_set_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
