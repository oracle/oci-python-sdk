# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlertPolicyRuleSummary(object):
    """
    A rule associated with an alert policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AlertPolicyRuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this AlertPolicyRuleSummary.
        :type key: str

        :param description:
            The value to assign to the description property of this AlertPolicyRuleSummary.
        :type description: str

        :param expression:
            The value to assign to the expression property of this AlertPolicyRuleSummary.
        :type expression: str

        """
        self.swagger_types = {
            'key': 'str',
            'description': 'str',
            'expression': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'description': 'description',
            'expression': 'expression'
        }

        self._key = None
        self._description = None
        self._expression = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this AlertPolicyRuleSummary.
        The unique key of the alert policy rule.


        :return: The key of this AlertPolicyRuleSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this AlertPolicyRuleSummary.
        The unique key of the alert policy rule.


        :param key: The key of this AlertPolicyRuleSummary.
        :type: str
        """
        self._key = key

    @property
    def description(self):
        """
        Gets the description of this AlertPolicyRuleSummary.
        Describes the alert policy rule.


        :return: The description of this AlertPolicyRuleSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AlertPolicyRuleSummary.
        Describes the alert policy rule.


        :param description: The description of this AlertPolicyRuleSummary.
        :type: str
        """
        self._description = description

    @property
    def expression(self):
        """
        **[Required]** Gets the expression of this AlertPolicyRuleSummary.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :return: The expression of this AlertPolicyRuleSummary.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this AlertPolicyRuleSummary.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :param expression: The expression of this AlertPolicyRuleSummary.
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
