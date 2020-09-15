# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

        :param detector_rules:
            The value to assign to the detector_rules property of this UpdateTargetDetectorRecipeDetails.
        :type detector_rules: list[UpdateTargetRecipeDetectorRuleDetails]

        """
        self.swagger_types = {
            'detector_rules': 'list[UpdateTargetRecipeDetectorRuleDetails]'
        }

        self.attribute_map = {
            'detector_rules': 'detectorRules'
        }

        self._detector_rules = None

    @property
    def detector_rules(self):
        """
        **[Required]** Gets the detector_rules of this UpdateTargetDetectorRecipeDetails.
        Update detector rules associated with detector recipe in a target.


        :return: The detector_rules of this UpdateTargetDetectorRecipeDetails.
        :rtype: list[UpdateTargetRecipeDetectorRuleDetails]
        """
        return self._detector_rules

    @detector_rules.setter
    def detector_rules(self, detector_rules):
        """
        Sets the detector_rules of this UpdateTargetDetectorRecipeDetails.
        Update detector rules associated with detector recipe in a target.


        :param detector_rules: The detector_rules of this UpdateTargetDetectorRecipeDetails.
        :type: list[UpdateTargetRecipeDetectorRuleDetails]
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
