# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateResponderRecipeResponderRule(object):
    """
    The details to be updated in ResponderRule
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateResponderRecipeResponderRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param responder_rule_id:
            The value to assign to the responder_rule_id property of this UpdateResponderRecipeResponderRule.
        :type responder_rule_id: str

        :param details:
            The value to assign to the details property of this UpdateResponderRecipeResponderRule.
        :type details: oci.cloud_guard.models.UpdateResponderRuleDetails

        """
        self.swagger_types = {
            'responder_rule_id': 'str',
            'details': 'UpdateResponderRuleDetails'
        }

        self.attribute_map = {
            'responder_rule_id': 'responderRuleId',
            'details': 'details'
        }

        self._responder_rule_id = None
        self._details = None

    @property
    def responder_rule_id(self):
        """
        **[Required]** Gets the responder_rule_id of this UpdateResponderRecipeResponderRule.
        ResponderRecipeRule Identifier


        :return: The responder_rule_id of this UpdateResponderRecipeResponderRule.
        :rtype: str
        """
        return self._responder_rule_id

    @responder_rule_id.setter
    def responder_rule_id(self, responder_rule_id):
        """
        Sets the responder_rule_id of this UpdateResponderRecipeResponderRule.
        ResponderRecipeRule Identifier


        :param responder_rule_id: The responder_rule_id of this UpdateResponderRecipeResponderRule.
        :type: str
        """
        self._responder_rule_id = responder_rule_id

    @property
    def details(self):
        """
        **[Required]** Gets the details of this UpdateResponderRecipeResponderRule.

        :return: The details of this UpdateResponderRecipeResponderRule.
        :rtype: oci.cloud_guard.models.UpdateResponderRuleDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this UpdateResponderRecipeResponderRule.

        :param details: The details of this UpdateResponderRecipeResponderRule.
        :type: oci.cloud_guard.models.UpdateResponderRuleDetails
        """
        self._details = details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
