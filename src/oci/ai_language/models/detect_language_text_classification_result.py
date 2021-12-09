# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectLanguageTextClassificationResult(object):
    """
    Result of text classification detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetectLanguageTextClassificationResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text_classification:
            The value to assign to the text_classification property of this DetectLanguageTextClassificationResult.
        :type text_classification: list[oci.ai_language.models.TextClassification]

        """
        self.swagger_types = {
            'text_classification': 'list[TextClassification]'
        }

        self.attribute_map = {
            'text_classification': 'textClassification'
        }

        self._text_classification = None

    @property
    def text_classification(self):
        """
        **[Required]** Gets the text_classification of this DetectLanguageTextClassificationResult.
        List of detected text classes.


        :return: The text_classification of this DetectLanguageTextClassificationResult.
        :rtype: list[oci.ai_language.models.TextClassification]
        """
        return self._text_classification

    @text_classification.setter
    def text_classification(self, text_classification):
        """
        Sets the text_classification of this DetectLanguageTextClassificationResult.
        List of detected text classes.


        :param text_classification: The text_classification of this DetectLanguageTextClassificationResult.
        :type: list[oci.ai_language.models.TextClassification]
        """
        self._text_classification = text_classification

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
