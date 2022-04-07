# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageFeature(object):
    """
    The type of image analysis.
    """

    #: A constant which can be used with the feature_type property of a ImageFeature.
    #: This constant has a value of "IMAGE_CLASSIFICATION"
    FEATURE_TYPE_IMAGE_CLASSIFICATION = "IMAGE_CLASSIFICATION"

    #: A constant which can be used with the feature_type property of a ImageFeature.
    #: This constant has a value of "OBJECT_DETECTION"
    FEATURE_TYPE_OBJECT_DETECTION = "OBJECT_DETECTION"

    #: A constant which can be used with the feature_type property of a ImageFeature.
    #: This constant has a value of "TEXT_DETECTION"
    FEATURE_TYPE_TEXT_DETECTION = "TEXT_DETECTION"

    def __init__(self, **kwargs):
        """
        Initializes a new ImageFeature object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_vision.models.ImageTextDetectionFeature`
        * :class:`~oci.ai_vision.models.ImageObjectDetectionFeature`
        * :class:`~oci.ai_vision.models.ImageClassificationFeature`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_type:
            The value to assign to the feature_type property of this ImageFeature.
            Allowed values for this property are: "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_DETECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type feature_type: str

        """
        self.swagger_types = {
            'feature_type': 'str'
        }

        self.attribute_map = {
            'feature_type': 'featureType'
        }

        self._feature_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['featureType']

        if type == 'TEXT_DETECTION':
            return 'ImageTextDetectionFeature'

        if type == 'OBJECT_DETECTION':
            return 'ImageObjectDetectionFeature'

        if type == 'IMAGE_CLASSIFICATION':
            return 'ImageClassificationFeature'
        else:
            return 'ImageFeature'

    @property
    def feature_type(self):
        """
        **[Required]** Gets the feature_type of this ImageFeature.
        The type of image analysis requested.
        The allowed values are:
        - `IMAGE_CLASSIFICATION`: Label the image.
        - `OBJECT_DETECTION`: Identify objects in the image with bounding boxes.
        - `TEXT_DETECTION`: Recognize text in the image.

        Allowed values for this property are: "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_DETECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The feature_type of this ImageFeature.
        :rtype: str
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """
        Sets the feature_type of this ImageFeature.
        The type of image analysis requested.
        The allowed values are:
        - `IMAGE_CLASSIFICATION`: Label the image.
        - `OBJECT_DETECTION`: Identify objects in the image with bounding boxes.
        - `TEXT_DETECTION`: Recognize text in the image.


        :param feature_type: The feature_type of this ImageFeature.
        :type: str
        """
        allowed_values = ["IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_DETECTION"]
        if not value_allowed_none_or_none_sentinel(feature_type, allowed_values):
            feature_type = 'UNKNOWN_ENUM_VALUE'
        self._feature_type = feature_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
