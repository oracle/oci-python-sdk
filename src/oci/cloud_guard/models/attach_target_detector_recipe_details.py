# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachTargetDetectorRecipeDetails(object):
    """
    The information required to create TargetDetectorRecipe
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachTargetDetectorRecipeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param detector_recipe_id:
            The value to assign to the detector_recipe_id property of this AttachTargetDetectorRecipeDetails.
        :type detector_recipe_id: str

        """
        self.swagger_types = {
            'detector_recipe_id': 'str'
        }

        self.attribute_map = {
            'detector_recipe_id': 'detectorRecipeId'
        }

        self._detector_recipe_id = None

    @property
    def detector_recipe_id(self):
        """
        **[Required]** Gets the detector_recipe_id of this AttachTargetDetectorRecipeDetails.
        DetectorRecipe Identifier


        :return: The detector_recipe_id of this AttachTargetDetectorRecipeDetails.
        :rtype: str
        """
        return self._detector_recipe_id

    @detector_recipe_id.setter
    def detector_recipe_id(self, detector_recipe_id):
        """
        Sets the detector_recipe_id of this AttachTargetDetectorRecipeDetails.
        DetectorRecipe Identifier


        :param detector_recipe_id: The detector_recipe_id of this AttachTargetDetectorRecipeDetails.
        :type: str
        """
        self._detector_recipe_id = detector_recipe_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
