# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .model_details import ModelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextClassificationModelDetails(ModelDetails):
    """
    Possible TextClassificationModelDetails
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextClassificationModelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.TextClassificationModelDetails.model_type` attribute
        of this class is ``TEXT_CLASSIFICATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param language_code:
            The value to assign to the language_code property of this TextClassificationModelDetails.
        :type language_code: str

        :param model_type:
            The value to assign to the model_type property of this TextClassificationModelDetails.
            Allowed values for this property are: "NAMED_ENTITY_RECOGNITION", "TEXT_CLASSIFICATION"
        :type model_type: str

        :param classification_mode:
            The value to assign to the classification_mode property of this TextClassificationModelDetails.
        :type classification_mode: oci.ai_language.models.ClassificationType

        """
        self.swagger_types = {
            'language_code': 'str',
            'model_type': 'str',
            'classification_mode': 'ClassificationType'
        }

        self.attribute_map = {
            'language_code': 'languageCode',
            'model_type': 'modelType',
            'classification_mode': 'classificationMode'
        }

        self._language_code = None
        self._model_type = None
        self._classification_mode = None
        self._model_type = 'TEXT_CLASSIFICATION'

    @property
    def classification_mode(self):
        """
        Gets the classification_mode of this TextClassificationModelDetails.

        :return: The classification_mode of this TextClassificationModelDetails.
        :rtype: oci.ai_language.models.ClassificationType
        """
        return self._classification_mode

    @classification_mode.setter
    def classification_mode(self, classification_mode):
        """
        Sets the classification_mode of this TextClassificationModelDetails.

        :param classification_mode: The classification_mode of this TextClassificationModelDetails.
        :type: oci.ai_language.models.ClassificationType
        """
        self._classification_mode = classification_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
