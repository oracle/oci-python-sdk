# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAlertPolicyRuleDetails(object):
    """
    The details used to update a alert policy rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAlertPolicyRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateAlertPolicyRuleDetails.
        :type description: str

        :param expression:
            The value to assign to the expression property of this UpdateAlertPolicyRuleDetails.
        :type expression: str

        """
        self.swagger_types = {
            'description': 'str',
            'expression': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'expression': 'expression'
        }

        self._description = None
        self._expression = None

    @property
    def description(self):
        """
        Gets the description of this UpdateAlertPolicyRuleDetails.
        Describes the alert policy rule.


        :return: The description of this UpdateAlertPolicyRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateAlertPolicyRuleDetails.
        Describes the alert policy rule.


        :param description: The description of this UpdateAlertPolicyRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def expression(self):
        """
        Gets the expression of this UpdateAlertPolicyRuleDetails.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :return: The expression of this UpdateAlertPolicyRuleDetails.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this UpdateAlertPolicyRuleDetails.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :param expression: The expression of this UpdateAlertPolicyRuleDetails.
        :type: str
        """
        self._expression = expression

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
