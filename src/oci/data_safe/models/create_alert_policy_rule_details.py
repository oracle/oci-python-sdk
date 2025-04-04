# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAlertPolicyRuleDetails(object):
    """
    The details used to create a new alert policy rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAlertPolicyRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param expression:
            The value to assign to the expression property of this CreateAlertPolicyRuleDetails.
        :type expression: str

        :param description:
            The value to assign to the description property of this CreateAlertPolicyRuleDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateAlertPolicyRuleDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'expression': 'str',
            'description': 'str',
            'display_name': 'str'
        }
        self.attribute_map = {
            'expression': 'expression',
            'description': 'description',
            'display_name': 'displayName'
        }
        self._expression = None
        self._description = None
        self._display_name = None

    @property
    def expression(self):
        """
        **[Required]** Gets the expression of this CreateAlertPolicyRuleDetails.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :return: The expression of this CreateAlertPolicyRuleDetails.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this CreateAlertPolicyRuleDetails.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :param expression: The expression of this CreateAlertPolicyRuleDetails.
        :type: str
        """
        self._expression = expression

    @property
    def description(self):
        """
        Gets the description of this CreateAlertPolicyRuleDetails.
        Describes the alert policy rule.


        :return: The description of this CreateAlertPolicyRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAlertPolicyRuleDetails.
        Describes the alert policy rule.


        :param description: The description of this CreateAlertPolicyRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAlertPolicyRuleDetails.
        The display name of the alert policy rule.


        :return: The display_name of this CreateAlertPolicyRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAlertPolicyRuleDetails.
        The display name of the alert policy rule.


        :param display_name: The display_name of this CreateAlertPolicyRuleDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
