# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetResponderRecipeDetails(object):
    """
    The information to be updated in ResponderRecipe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetResponderRecipeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param responder_rules:
            The value to assign to the responder_rules property of this UpdateTargetResponderRecipeDetails.
        :type responder_rules: list[oci.cloud_guard.models.UpdateTargetRecipeResponderRuleDetails]

        """
        self.swagger_types = {
            'responder_rules': 'list[UpdateTargetRecipeResponderRuleDetails]'
        }

        self.attribute_map = {
            'responder_rules': 'responderRules'
        }

        self._responder_rules = None

    @property
    def responder_rules(self):
        """
        **[Required]** Gets the responder_rules of this UpdateTargetResponderRecipeDetails.
        Update responder rules associated with responder recipe in a target.


        :return: The responder_rules of this UpdateTargetResponderRecipeDetails.
        :rtype: list[oci.cloud_guard.models.UpdateTargetRecipeResponderRuleDetails]
        """
        return self._responder_rules

    @responder_rules.setter
    def responder_rules(self, responder_rules):
        """
        Sets the responder_rules of this UpdateTargetResponderRecipeDetails.
        Update responder rules associated with responder recipe in a target.


        :param responder_rules: The responder_rules of this UpdateTargetResponderRecipeDetails.
        :type: list[oci.cloud_guard.models.UpdateTargetRecipeResponderRuleDetails]
        """
        self._responder_rules = responder_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
