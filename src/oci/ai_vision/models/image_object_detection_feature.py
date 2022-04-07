# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .image_feature import ImageFeature
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageObjectDetectionFeature(ImageFeature):
    """
    The object detection parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageObjectDetectionFeature object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.ImageObjectDetectionFeature.feature_type` attribute
        of this class is ``OBJECT_DETECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_type:
            The value to assign to the feature_type property of this ImageObjectDetectionFeature.
            Allowed values for this property are: "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_DETECTION"
        :type feature_type: str

        :param max_results:
            The value to assign to the max_results property of this ImageObjectDetectionFeature.
        :type max_results: int

        :param model_id:
            The value to assign to the model_id property of this ImageObjectDetectionFeature.
        :type model_id: str

        """
        self.swagger_types = {
            'feature_type': 'str',
            'max_results': 'int',
            'model_id': 'str'
        }

        self.attribute_map = {
            'feature_type': 'featureType',
            'max_results': 'maxResults',
            'model_id': 'modelId'
        }

        self._feature_type = None
        self._max_results = None
        self._model_id = None
        self._feature_type = 'OBJECT_DETECTION'

    @property
    def max_results(self):
        """
        Gets the max_results of this ImageObjectDetectionFeature.
        The maximum number of results to return.


        :return: The max_results of this ImageObjectDetectionFeature.
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """
        Sets the max_results of this ImageObjectDetectionFeature.
        The maximum number of results to return.


        :param max_results: The max_results of this ImageObjectDetectionFeature.
        :type: int
        """
        self._max_results = max_results

    @property
    def model_id(self):
        """
        Gets the model_id of this ImageObjectDetectionFeature.
        The custom model ID.


        :return: The model_id of this ImageObjectDetectionFeature.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this ImageObjectDetectionFeature.
        The custom model ID.


        :param model_id: The model_id of this ImageObjectDetectionFeature.
        :type: str
        """
        self._model_id = model_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
