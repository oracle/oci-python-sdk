# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .batch_detect_dominant_language_details import BatchDetectDominantLanguageDetails
from .batch_detect_dominant_language_result import BatchDetectDominantLanguageResult
from .batch_detect_language_entities_details import BatchDetectLanguageEntitiesDetails
from .batch_detect_language_entities_result import BatchDetectLanguageEntitiesResult
from .batch_detect_language_key_phrases_details import BatchDetectLanguageKeyPhrasesDetails
from .batch_detect_language_key_phrases_result import BatchDetectLanguageKeyPhrasesResult
from .batch_detect_language_sentiments_details import BatchDetectLanguageSentimentsDetails
from .batch_detect_language_sentiments_result import BatchDetectLanguageSentimentsResult
from .batch_detect_language_text_classification_details import BatchDetectLanguageTextClassificationDetails
from .batch_detect_language_text_classification_result import BatchDetectLanguageTextClassificationResult
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
from .document_error import DocumentError
from .dominant_language_document import DominantLanguageDocument
from .dominant_language_document_result import DominantLanguageDocumentResult
from .entity import Entity
from .entity_document import EntityDocument
from .entity_document_result import EntityDocumentResult
from .error_details import ErrorDetails
from .hierarchical_entity import HierarchicalEntity
from .key_phrase import KeyPhrase
from .key_phrase_document import KeyPhraseDocument
from .key_phrase_document_result import KeyPhraseDocumentResult
from .sentiment_aspect import SentimentAspect
from .sentiment_document_result import SentimentDocumentResult
from .sentiment_sentence import SentimentSentence
from .sentiments_document import SentimentsDocument
from .text_classification import TextClassification
from .text_classification_document import TextClassificationDocument
from .text_classification_document_result import TextClassificationDocumentResult

# Maps type names to classes for ai_language services.
ai_language_type_mapping = {
    "BatchDetectDominantLanguageDetails": BatchDetectDominantLanguageDetails,
    "BatchDetectDominantLanguageResult": BatchDetectDominantLanguageResult,
    "BatchDetectLanguageEntitiesDetails": BatchDetectLanguageEntitiesDetails,
    "BatchDetectLanguageEntitiesResult": BatchDetectLanguageEntitiesResult,
    "BatchDetectLanguageKeyPhrasesDetails": BatchDetectLanguageKeyPhrasesDetails,
    "BatchDetectLanguageKeyPhrasesResult": BatchDetectLanguageKeyPhrasesResult,
    "BatchDetectLanguageSentimentsDetails": BatchDetectLanguageSentimentsDetails,
    "BatchDetectLanguageSentimentsResult": BatchDetectLanguageSentimentsResult,
    "BatchDetectLanguageTextClassificationDetails": BatchDetectLanguageTextClassificationDetails,
    "BatchDetectLanguageTextClassificationResult": BatchDetectLanguageTextClassificationResult,
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
    "DocumentError": DocumentError,
    "DominantLanguageDocument": DominantLanguageDocument,
    "DominantLanguageDocumentResult": DominantLanguageDocumentResult,
    "Entity": Entity,
    "EntityDocument": EntityDocument,
    "EntityDocumentResult": EntityDocumentResult,
    "ErrorDetails": ErrorDetails,
    "HierarchicalEntity": HierarchicalEntity,
    "KeyPhrase": KeyPhrase,
    "KeyPhraseDocument": KeyPhraseDocument,
    "KeyPhraseDocumentResult": KeyPhraseDocumentResult,
    "SentimentAspect": SentimentAspect,
    "SentimentDocumentResult": SentimentDocumentResult,
    "SentimentSentence": SentimentSentence,
    "SentimentsDocument": SentimentsDocument,
    "TextClassification": TextClassification,
    "TextClassificationDocument": TextClassificationDocument,
    "TextClassificationDocumentResult": TextClassificationDocumentResult
}
