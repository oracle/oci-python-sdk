# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelDetails(object):
    """
    Possible model types
    """

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "NAMED_ENTITY_RECOGNITION"
    MODEL_TYPE_NAMED_ENTITY_RECOGNITION = "NAMED_ENTITY_RECOGNITION"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "TEXT_CLASSIFICATION"
    MODEL_TYPE_TEXT_CLASSIFICATION = "TEXT_CLASSIFICATION"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_NAMED_ENTITY_RECOGNITION"
    MODEL_TYPE_PRE_TRAINED_NAMED_ENTITY_RECOGNITION = "PRE_TRAINED_NAMED_ENTITY_RECOGNITION"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_TEXT_CLASSIFICATION"
    MODEL_TYPE_PRE_TRAINED_TEXT_CLASSIFICATION = "PRE_TRAINED_TEXT_CLASSIFICATION"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_SENTIMENT_ANALYSIS"
    MODEL_TYPE_PRE_TRAINED_SENTIMENT_ANALYSIS = "PRE_TRAINED_SENTIMENT_ANALYSIS"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_KEYPHRASE_EXTRACTION"
    MODEL_TYPE_PRE_TRAINED_KEYPHRASE_EXTRACTION = "PRE_TRAINED_KEYPHRASE_EXTRACTION"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_LANGUAGE_DETECTION"
    MODEL_TYPE_PRE_TRAINED_LANGUAGE_DETECTION = "PRE_TRAINED_LANGUAGE_DETECTION"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_PII"
    MODEL_TYPE_PRE_TRAINED_PII = "PRE_TRAINED_PII"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_HEALTH_NLU"
    MODEL_TYPE_PRE_TRAINED_HEALTH_NLU = "PRE_TRAINED_HEALTH_NLU"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_SUMMARIZATION"
    MODEL_TYPE_PRE_TRAINED_SUMMARIZATION = "PRE_TRAINED_SUMMARIZATION"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_UNIVERSAL"
    MODEL_TYPE_PRE_TRAINED_UNIVERSAL = "PRE_TRAINED_UNIVERSAL"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PII"
    MODEL_TYPE_PII = "PII"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "PRE_TRAINED_TRANSLATION"
    MODEL_TYPE_PRE_TRAINED_TRANSLATION = "PRE_TRAINED_TRANSLATION"

    #: A constant which can be used with the model_type property of a ModelDetails.
    #: This constant has a value of "HEALTH_NLU"
    MODEL_TYPE_HEALTH_NLU = "HEALTH_NLU"

    def __init__(self, **kwargs):
        """
        Initializes a new ModelDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_language.models.PreTrainedKeyPhraseExtractionModelDetails`
        * :class:`~oci.ai_language.models.PreTrainedTranslationModelDetails`
        * :class:`~oci.ai_language.models.PreTrainedHealthNluModelDetails`
        * :class:`~oci.ai_language.models.PreTrainedUniversalModel`
        * :class:`~oci.ai_language.models.PreTrainedLanguageDetectionModelDetails`
        * :class:`~oci.ai_language.models.PreTrainedSentimentAnalysisModelDetails`
        * :class:`~oci.ai_language.models.TextClassificationModelDetails`
        * :class:`~oci.ai_language.models.HealthNluModelDetails`
        * :class:`~oci.ai_language.models.PreTrainedSummarization`
        * :class:`~oci.ai_language.models.NamedEntityRecognitionModelDetails`
        * :class:`~oci.ai_language.models.PiiModelDetails`
        * :class:`~oci.ai_language.models.PreTrainedNamedEntityRecognitionModelDetails`
        * :class:`~oci.ai_language.models.PreTrainedTextClassificationModelDetails`
        * :class:`~oci.ai_language.models.PreTrainedPiiModelDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param language_code:
            The value to assign to the language_code property of this ModelDetails.
        :type language_code: str

        :param model_type:
            The value to assign to the model_type property of this ModelDetails.
            Allowed values for this property are: "NAMED_ENTITY_RECOGNITION", "TEXT_CLASSIFICATION", "PRE_TRAINED_NAMED_ENTITY_RECOGNITION", "PRE_TRAINED_TEXT_CLASSIFICATION", "PRE_TRAINED_SENTIMENT_ANALYSIS", "PRE_TRAINED_KEYPHRASE_EXTRACTION", "PRE_TRAINED_LANGUAGE_DETECTION", "PRE_TRAINED_PII", "PRE_TRAINED_HEALTH_NLU", "PRE_TRAINED_SUMMARIZATION", "PRE_TRAINED_UNIVERSAL", "PII", "PRE_TRAINED_TRANSLATION", "HEALTH_NLU", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        """
        self.swagger_types = {
            'language_code': 'str',
            'model_type': 'str'
        }
        self.attribute_map = {
            'language_code': 'languageCode',
            'model_type': 'modelType'
        }
        self._language_code = None
        self._model_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'PRE_TRAINED_KEYPHRASE_EXTRACTION':
            return 'PreTrainedKeyPhraseExtractionModelDetails'

        if type == 'PRE_TRAINED_TRANSLATION':
            return 'PreTrainedTranslationModelDetails'

        if type == 'PRE_TRAINED_HEALTH_NLU':
            return 'PreTrainedHealthNluModelDetails'

        if type == 'PRE_TRAINED_UNIVERSAL':
            return 'PreTrainedUniversalModel'

        if type == 'PRE_TRAINED_LANGUAGE_DETECTION':
            return 'PreTrainedLanguageDetectionModelDetails'

        if type == 'PRE_TRAINED_SENTIMENT_ANALYSIS':
            return 'PreTrainedSentimentAnalysisModelDetails'

        if type == 'TEXT_CLASSIFICATION':
            return 'TextClassificationModelDetails'

        if type == 'HEALTH_NLU':
            return 'HealthNluModelDetails'

        if type == 'PRE_TRAINED_SUMMARIZATION':
            return 'PreTrainedSummarization'

        if type == 'NAMED_ENTITY_RECOGNITION':
            return 'NamedEntityRecognitionModelDetails'

        if type == 'PII':
            return 'PiiModelDetails'

        if type == 'PRE_TRAINED_NAMED_ENTITY_RECOGNITION':
            return 'PreTrainedNamedEntityRecognitionModelDetails'

        if type == 'PRE_TRAINED_TEXT_CLASSIFICATION':
            return 'PreTrainedTextClassificationModelDetails'

        if type == 'PRE_TRAINED_PII':
            return 'PreTrainedPiiModelDetails'
        else:
            return 'ModelDetails'

    @property
    def language_code(self):
        """
        Gets the language_code of this ModelDetails.
        supported language default value is en


        :return: The language_code of this ModelDetails.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this ModelDetails.
        supported language default value is en


        :param language_code: The language_code of this ModelDetails.
        :type: str
        """
        self._language_code = language_code

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this ModelDetails.
        Model type

        Allowed values for this property are: "NAMED_ENTITY_RECOGNITION", "TEXT_CLASSIFICATION", "PRE_TRAINED_NAMED_ENTITY_RECOGNITION", "PRE_TRAINED_TEXT_CLASSIFICATION", "PRE_TRAINED_SENTIMENT_ANALYSIS", "PRE_TRAINED_KEYPHRASE_EXTRACTION", "PRE_TRAINED_LANGUAGE_DETECTION", "PRE_TRAINED_PII", "PRE_TRAINED_HEALTH_NLU", "PRE_TRAINED_SUMMARIZATION", "PRE_TRAINED_UNIVERSAL", "PII", "PRE_TRAINED_TRANSLATION", "HEALTH_NLU", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this ModelDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ModelDetails.
        Model type


        :param model_type: The model_type of this ModelDetails.
        :type: str
        """
        allowed_values = ["NAMED_ENTITY_RECOGNITION", "TEXT_CLASSIFICATION", "PRE_TRAINED_NAMED_ENTITY_RECOGNITION", "PRE_TRAINED_TEXT_CLASSIFICATION", "PRE_TRAINED_SENTIMENT_ANALYSIS", "PRE_TRAINED_KEYPHRASE_EXTRACTION", "PRE_TRAINED_LANGUAGE_DETECTION", "PRE_TRAINED_PII", "PRE_TRAINED_HEALTH_NLU", "PRE_TRAINED_SUMMARIZATION", "PRE_TRAINED_UNIVERSAL", "PII", "PRE_TRAINED_TRANSLATION", "HEALTH_NLU"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
