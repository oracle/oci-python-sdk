# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .image_feature import ImageFeature
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageTextDetectionFeature(ImageFeature):
    """
    Text detection parameters.
    """

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "ENG"
    LANGUAGE_ENG = "ENG"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "CES"
    LANGUAGE_CES = "CES"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "DAN"
    LANGUAGE_DAN = "DAN"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "NLD"
    LANGUAGE_NLD = "NLD"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "FIN"
    LANGUAGE_FIN = "FIN"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "FRA"
    LANGUAGE_FRA = "FRA"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "DEU"
    LANGUAGE_DEU = "DEU"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "ELL"
    LANGUAGE_ELL = "ELL"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "HUN"
    LANGUAGE_HUN = "HUN"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "ITA"
    LANGUAGE_ITA = "ITA"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "NOR"
    LANGUAGE_NOR = "NOR"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "POL"
    LANGUAGE_POL = "POL"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "POR"
    LANGUAGE_POR = "POR"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "RON"
    LANGUAGE_RON = "RON"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "RUS"
    LANGUAGE_RUS = "RUS"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "SLK"
    LANGUAGE_SLK = "SLK"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "SPA"
    LANGUAGE_SPA = "SPA"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "SWE"
    LANGUAGE_SWE = "SWE"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "TUR"
    LANGUAGE_TUR = "TUR"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "ARA"
    LANGUAGE_ARA = "ARA"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "CHI_SIM"
    LANGUAGE_CHI_SIM = "CHI_SIM"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "HIN"
    LANGUAGE_HIN = "HIN"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "JPN"
    LANGUAGE_JPN = "JPN"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "KOR"
    LANGUAGE_KOR = "KOR"

    #: A constant which can be used with the language property of a ImageTextDetectionFeature.
    #: This constant has a value of "OTHERS"
    LANGUAGE_OTHERS = "OTHERS"

    def __init__(self, **kwargs):
        """
        Initializes a new ImageTextDetectionFeature object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.ImageTextDetectionFeature.feature_type` attribute
        of this class is ``TEXT_DETECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_type:
            The value to assign to the feature_type property of this ImageTextDetectionFeature.
            Allowed values for this property are: "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_DETECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type feature_type: str

        :param language:
            The value to assign to the language property of this ImageTextDetectionFeature.
            Allowed values for this property are: "ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type language: str

        """
        self.swagger_types = {
            'feature_type': 'str',
            'language': 'str'
        }

        self.attribute_map = {
            'feature_type': 'featureType',
            'language': 'language'
        }

        self._feature_type = None
        self._language = None
        self._feature_type = 'TEXT_DETECTION'

    @property
    def language(self):
        """
        Gets the language of this ImageTextDetectionFeature.
        Language of the document image, abbreviated according to ISO 639-2.

        Allowed values for this property are: "ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The language of this ImageTextDetectionFeature.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this ImageTextDetectionFeature.
        Language of the document image, abbreviated according to ISO 639-2.


        :param language: The language of this ImageTextDetectionFeature.
        :type: str
        """
        allowed_values = ["ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"]
        if not value_allowed_none_or_none_sentinel(language, allowed_values):
            language = 'UNKNOWN_ENUM_VALUE'
        self._language = language

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
