# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnalyzeImageDetails(object):
    """
    The details of how to analyze an image.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnalyzeImageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param features:
            The value to assign to the features property of this AnalyzeImageDetails.
        :type features: list[oci.ai_vision.models.ImageFeature]

        :param image:
            The value to assign to the image property of this AnalyzeImageDetails.
        :type image: oci.ai_vision.models.ImageDetails

        :param compartment_id:
            The value to assign to the compartment_id property of this AnalyzeImageDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'features': 'list[ImageFeature]',
            'image': 'ImageDetails',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'features': 'features',
            'image': 'image',
            'compartment_id': 'compartmentId'
        }

        self._features = None
        self._image = None
        self._compartment_id = None

    @property
    def features(self):
        """
        **[Required]** Gets the features of this AnalyzeImageDetails.
        The types of image analysis.


        :return: The features of this AnalyzeImageDetails.
        :rtype: list[oci.ai_vision.models.ImageFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this AnalyzeImageDetails.
        The types of image analysis.


        :param features: The features of this AnalyzeImageDetails.
        :type: list[oci.ai_vision.models.ImageFeature]
        """
        self._features = features

    @property
    def image(self):
        """
        **[Required]** Gets the image of this AnalyzeImageDetails.

        :return: The image of this AnalyzeImageDetails.
        :rtype: oci.ai_vision.models.ImageDetails
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this AnalyzeImageDetails.

        :param image: The image of this AnalyzeImageDetails.
        :type: oci.ai_vision.models.ImageDetails
        """
        self._image = image

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this AnalyzeImageDetails.
        The OCID of the compartment that calls the API.


        :return: The compartment_id of this AnalyzeImageDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AnalyzeImageDetails.
        The OCID of the compartment that calls the API.


        :param compartment_id: The compartment_id of this AnalyzeImageDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
