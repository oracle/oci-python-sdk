# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .detect_dominant_language_details import DetectDominantLanguageDetails
from .detect_dominant_language_result import DetectDominantLanguageResult
from .detect_language_entities_details import DetectLanguageEntitiesDetails
from .detect_language_entities_result import DetectLanguageEntitiesResult
from .detect_language_key_phrases_details import DetectLanguageKeyPhrasesDetails
from .detect_language_key_phrases_result import DetectLanguageKeyPhrasesResult
from .detect_language_sentiments_details import DetectLanguageSentimentsDetails
from .detect_language_sentiments_result import DetectLanguageSentimentsResult
from .detect_language_text_classification_details import DetectLanguageTextClassificationDetails
from .detect_language_text_classification_result import DetectLanguageTextClassificationResult
from .detected_language import DetectedLanguage
from .entity import Entity
from .key_phrase import KeyPhrase
from .sentiment_aspect import SentimentAspect
from .text_classification import TextClassification

# Maps type names to classes for ai_language services.
ai_language_type_mapping = {
    "DetectDominantLanguageDetails": DetectDominantLanguageDetails,
    "DetectDominantLanguageResult": DetectDominantLanguageResult,
    "DetectLanguageEntitiesDetails": DetectLanguageEntitiesDetails,
    "DetectLanguageEntitiesResult": DetectLanguageEntitiesResult,
    "DetectLanguageKeyPhrasesDetails": DetectLanguageKeyPhrasesDetails,
    "DetectLanguageKeyPhrasesResult": DetectLanguageKeyPhrasesResult,
    "DetectLanguageSentimentsDetails": DetectLanguageSentimentsDetails,
    "DetectLanguageSentimentsResult": DetectLanguageSentimentsResult,
    "DetectLanguageTextClassificationDetails": DetectLanguageTextClassificationDetails,
    "DetectLanguageTextClassificationResult": DetectLanguageTextClassificationResult,
    "DetectedLanguage": DetectedLanguage,
    "Entity": Entity,
    "KeyPhrase": KeyPhrase,
    "SentimentAspect": SentimentAspect,
    "TextClassification": TextClassification
}
