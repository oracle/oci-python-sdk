# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetResponderRecipe(object):
    """
    The information to be updated in attached Target ResponderRecipe
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetResponderRecipe object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_responder_recipe_id:
            The value to assign to the target_responder_recipe_id property of this UpdateTargetResponderRecipe.
        :type target_responder_recipe_id: str

        :param responder_rules:
            The value to assign to the responder_rules property of this UpdateTargetResponderRecipe.
        :type responder_rules: list[oci.cloud_guard.models.UpdateTargetRecipeResponderRuleDetails]

        """
        self.swagger_types = {
            'target_responder_recipe_id': 'str',
            'responder_rules': 'list[UpdateTargetRecipeResponderRuleDetails]'
        }

        self.attribute_map = {
            'target_responder_recipe_id': 'targetResponderRecipeId',
            'responder_rules': 'responderRules'
        }

        self._target_responder_recipe_id = None
        self._responder_rules = None

    @property
    def target_responder_recipe_id(self):
        """
        **[Required]** Gets the target_responder_recipe_id of this UpdateTargetResponderRecipe.
        Identifier for ResponderRecipe.


        :return: The target_responder_recipe_id of this UpdateTargetResponderRecipe.
        :rtype: str
        """
        return self._target_responder_recipe_id

    @target_responder_recipe_id.setter
    def target_responder_recipe_id(self, target_responder_recipe_id):
        """
        Sets the target_responder_recipe_id of this UpdateTargetResponderRecipe.
        Identifier for ResponderRecipe.


        :param target_responder_recipe_id: The target_responder_recipe_id of this UpdateTargetResponderRecipe.
        :type: str
        """
        self._target_responder_recipe_id = target_responder_recipe_id

    @property
    def responder_rules(self):
        """
        **[Required]** Gets the responder_rules of this UpdateTargetResponderRecipe.
        Update responder rules associated with reponder recipe in a target.


        :return: The responder_rules of this UpdateTargetResponderRecipe.
        :rtype: list[oci.cloud_guard.models.UpdateTargetRecipeResponderRuleDetails]
        """
        return self._responder_rules

    @responder_rules.setter
    def responder_rules(self, responder_rules):
        """
        Sets the responder_rules of this UpdateTargetResponderRecipe.
        Update responder rules associated with reponder recipe in a target.


        :param responder_rules: The responder_rules of this UpdateTargetResponderRecipe.
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
