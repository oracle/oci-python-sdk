# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .rule import Rule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AllowRule(Rule):
    """
    Configuration of an access control rule that permits access to the application
    resources exposed by a listener based on user specified match conditions.

    This rule applies to only HTTP listeners.

    Atleast one match condition should be specified in the rule.

    **NOTE:** When user does not specify any access control rules, the implicit default rule is to allow all traffic.
    **NOTE:** When user adds any access control rules, all the traffic not matching with any rules will be implicitly denied.
    **NOTE:** User can specify this rule only with the following combinations of RuleCondition types:
    - [\"SOURCE_IP_ADDRESS\"]
    - [\"SOURCE_VCN_ID\"]
    - [\"SOURCE_VCN_ID\", \"SOURCE_VCN_IP_ADDRESS\"]
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AllowRule object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.AllowRule.action` attribute
        of this class is ``ALLOW`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this AllowRule.
            Allowed values for this property are: "ADD_HTTP_REQUEST_HEADER", "EXTEND_HTTP_REQUEST_HEADER_VALUE", "REMOVE_HTTP_REQUEST_HEADER", "ADD_HTTP_RESPONSE_HEADER", "EXTEND_HTTP_RESPONSE_HEADER_VALUE", "REMOVE_HTTP_RESPONSE_HEADER", "ALLOW", "CONTROL_ACCESS_USING_HTTP_METHODS"
        :type action: str

        :param conditions:
            The value to assign to the conditions property of this AllowRule.
        :type conditions: list[RuleCondition]

        :param description:
            The value to assign to the description property of this AllowRule.
        :type description: str

        """
        self.swagger_types = {
            'action': 'str',
            'conditions': 'list[RuleCondition]',
            'description': 'str'
        }

        self.attribute_map = {
            'action': 'action',
            'conditions': 'conditions',
            'description': 'description'
        }

        self._action = None
        self._conditions = None
        self._description = None
        self._action = 'ALLOW'

    @property
    def conditions(self):
        """
        **[Required]** Gets the conditions of this AllowRule.

        :return: The conditions of this AllowRule.
        :rtype: list[RuleCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this AllowRule.

        :param conditions: The conditions of this AllowRule.
        :type: list[RuleCondition]
        """
        self._conditions = conditions

    @property
    def description(self):
        """
        Gets the description of this AllowRule.
        Brief description of the access control rule.


        :return: The description of this AllowRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AllowRule.
        Brief description of the access control rule.


        :param description: The description of this AllowRule.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
