# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetDetectorRecipeDetails(object):
    """
    The information to be updated in DetectorRecipe
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetDetectorRecipeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param detector_recipe_id:
            The value to assign to the detector_recipe_id property of this UpdateTargetDetectorRecipeDetails.
        :type detector_recipe_id: str

        :param is_validation_only_query:
            The value to assign to the is_validation_only_query property of this UpdateTargetDetectorRecipeDetails.
        :type is_validation_only_query: bool

        :param detector_rules:
            The value to assign to the detector_rules property of this UpdateTargetDetectorRecipeDetails.
        :type detector_rules: list[oci.cloud_guard.models.UpdateTargetRecipeDetectorRuleDetails]

        """
        self.swagger_types = {
            'detector_recipe_id': 'str',
            'is_validation_only_query': 'bool',
            'detector_rules': 'list[UpdateTargetRecipeDetectorRuleDetails]'
        }

        self.attribute_map = {
            'detector_recipe_id': 'detectorRecipeId',
            'is_validation_only_query': 'isValidationOnlyQuery',
            'detector_rules': 'detectorRules'
        }

        self._detector_recipe_id = None
        self._is_validation_only_query = None
        self._detector_rules = None

    @property
    def detector_recipe_id(self):
        """
        Gets the detector_recipe_id of this UpdateTargetDetectorRecipeDetails.
        Detector recipe identifier associated with the target


        :return: The detector_recipe_id of this UpdateTargetDetectorRecipeDetails.
        :rtype: str
        """
        return self._detector_recipe_id

    @detector_recipe_id.setter
    def detector_recipe_id(self, detector_recipe_id):
        """
        Sets the detector_recipe_id of this UpdateTargetDetectorRecipeDetails.
        Detector recipe identifier associated with the target


        :param detector_recipe_id: The detector_recipe_id of this UpdateTargetDetectorRecipeDetails.
        :type: str
        """
        self._detector_recipe_id = detector_recipe_id

    @property
    def is_validation_only_query(self):
        """
        Gets the is_validation_only_query of this UpdateTargetDetectorRecipeDetails.
        When enabled, validation is performed for attaching the detector recipe.


        :return: The is_validation_only_query of this UpdateTargetDetectorRecipeDetails.
        :rtype: bool
        """
        return self._is_validation_only_query

    @is_validation_only_query.setter
    def is_validation_only_query(self, is_validation_only_query):
        """
        Sets the is_validation_only_query of this UpdateTargetDetectorRecipeDetails.
        When enabled, validation is performed for attaching the detector recipe.


        :param is_validation_only_query: The is_validation_only_query of this UpdateTargetDetectorRecipeDetails.
        :type: bool
        """
        self._is_validation_only_query = is_validation_only_query

    @property
    def detector_rules(self):
        """
        Gets the detector_rules of this UpdateTargetDetectorRecipeDetails.
        Update detector rules associated with detector recipe in a target.


        :return: The detector_rules of this UpdateTargetDetectorRecipeDetails.
        :rtype: list[oci.cloud_guard.models.UpdateTargetRecipeDetectorRuleDetails]
        """
        return self._detector_rules

    @detector_rules.setter
    def detector_rules(self, detector_rules):
        """
        Sets the detector_rules of this UpdateTargetDetectorRecipeDetails.
        Update detector rules associated with detector recipe in a target.


        :param detector_rules: The detector_rules of this UpdateTargetDetectorRecipeDetails.
        :type: list[oci.cloud_guard.models.UpdateTargetRecipeDetectorRuleDetails]
        """
        self._detector_rules = detector_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
