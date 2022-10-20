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
from .batch_language_translation_details import BatchLanguageTranslationDetails
from .batch_language_translation_result import BatchLanguageTranslationResult
from .change_endpoint_compartment_details import ChangeEndpointCompartmentDetails
from .change_model_compartment_details import ChangeModelCompartmentDetails
from .change_project_compartment_details import ChangeProjectCompartmentDetails
from .class_metrics import ClassMetrics
from .classification_multi_class_mode_details import ClassificationMultiClassModeDetails
from .classification_multi_label_mode_details import ClassificationMultiLabelModeDetails
from .classification_type import ClassificationType
from .confusion_matrix_details import ConfusionMatrixDetails
from .create_endpoint_details import CreateEndpointDetails
from .create_model_details import CreateModelDetails
from .create_project_details import CreateProjectDetails
from .data_science_labeling_dataset import DataScienceLabelingDataset
from .dataset_details import DatasetDetails
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
from .endpoint import Endpoint
from .endpoint_collection import EndpointCollection
from .endpoint_summary import EndpointSummary
from .entity import Entity
from .entity_document_result import EntityDocumentResult
from .entity_label_error_analysis import EntityLabelErrorAnalysis
from .entity_metrics import EntityMetrics
from .error_details import ErrorDetails
from .evaluation_result_collection import EvaluationResultCollection
from .evaluation_result_summary import EvaluationResultSummary
from .evaluation_results import EvaluationResults
from .hierarchical_entity import HierarchicalEntity
from .key_phrase import KeyPhrase
from .key_phrase_document_result import KeyPhraseDocumentResult
from .location_details import LocationDetails
from .model import Model
from .model_collection import ModelCollection
from .model_details import ModelDetails
from .model_summary import ModelSummary
from .named_entity_recognition_evaluation_result import NamedEntityRecognitionEvaluationResult
from .named_entity_recognition_evaluation_results import NamedEntityRecognitionEvaluationResults
from .named_entity_recognition_model_details import NamedEntityRecognitionModelDetails
from .named_entity_recognition_model_metrics import NamedEntityRecognitionModelMetrics
from .object_list_dataset import ObjectListDataset
from .object_storage_dataset import ObjectStorageDataset
from .pre_deployed_language_models import PreDeployedLanguageModels
from .project import Project
from .project_collection import ProjectCollection
from .project_summary import ProjectSummary
from .sentiment_aspect import SentimentAspect
from .sentiment_document_result import SentimentDocumentResult
from .sentiment_sentence import SentimentSentence
from .test_and_validation_dataset_strategy import TestAndValidationDatasetStrategy
from .test_strategy import TestStrategy
from .text_classification import TextClassification
from .text_classification_document_result import TextClassificationDocumentResult
from .text_classification_evaluation_results import TextClassificationEvaluationResults
from .text_classification_model_details import TextClassificationModelDetails
from .text_classification_model_evaluation_result import TextClassificationModelEvaluationResult
from .text_classification_model_metrics import TextClassificationModelMetrics
from .text_document import TextDocument
from .translation_document_result import TranslationDocumentResult
from .update_endpoint_details import UpdateEndpointDetails
from .update_model_details import UpdateModelDetails
from .update_project_details import UpdateProjectDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log import WorkRequestLog
from .work_request_log_collection import WorkRequestLogCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

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
    "BatchLanguageTranslationDetails": BatchLanguageTranslationDetails,
    "BatchLanguageTranslationResult": BatchLanguageTranslationResult,
    "ChangeEndpointCompartmentDetails": ChangeEndpointCompartmentDetails,
    "ChangeModelCompartmentDetails": ChangeModelCompartmentDetails,
    "ChangeProjectCompartmentDetails": ChangeProjectCompartmentDetails,
    "ClassMetrics": ClassMetrics,
    "ClassificationMultiClassModeDetails": ClassificationMultiClassModeDetails,
    "ClassificationMultiLabelModeDetails": ClassificationMultiLabelModeDetails,
    "ClassificationType": ClassificationType,
    "ConfusionMatrixDetails": ConfusionMatrixDetails,
    "CreateEndpointDetails": CreateEndpointDetails,
    "CreateModelDetails": CreateModelDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "DataScienceLabelingDataset": DataScienceLabelingDataset,
    "DatasetDetails": DatasetDetails,
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
    "Endpoint": Endpoint,
    "EndpointCollection": EndpointCollection,
    "EndpointSummary": EndpointSummary,
    "Entity": Entity,
    "EntityDocumentResult": EntityDocumentResult,
    "EntityLabelErrorAnalysis": EntityLabelErrorAnalysis,
    "EntityMetrics": EntityMetrics,
    "ErrorDetails": ErrorDetails,
    "EvaluationResultCollection": EvaluationResultCollection,
    "EvaluationResultSummary": EvaluationResultSummary,
    "EvaluationResults": EvaluationResults,
    "HierarchicalEntity": HierarchicalEntity,
    "KeyPhrase": KeyPhrase,
    "KeyPhraseDocumentResult": KeyPhraseDocumentResult,
    "LocationDetails": LocationDetails,
    "Model": Model,
    "ModelCollection": ModelCollection,
    "ModelDetails": ModelDetails,
    "ModelSummary": ModelSummary,
    "NamedEntityRecognitionEvaluationResult": NamedEntityRecognitionEvaluationResult,
    "NamedEntityRecognitionEvaluationResults": NamedEntityRecognitionEvaluationResults,
    "NamedEntityRecognitionModelDetails": NamedEntityRecognitionModelDetails,
    "NamedEntityRecognitionModelMetrics": NamedEntityRecognitionModelMetrics,
    "ObjectListDataset": ObjectListDataset,
    "ObjectStorageDataset": ObjectStorageDataset,
    "PreDeployedLanguageModels": PreDeployedLanguageModels,
    "Project": Project,
    "ProjectCollection": ProjectCollection,
    "ProjectSummary": ProjectSummary,
    "SentimentAspect": SentimentAspect,
    "SentimentDocumentResult": SentimentDocumentResult,
    "SentimentSentence": SentimentSentence,
    "TestAndValidationDatasetStrategy": TestAndValidationDatasetStrategy,
    "TestStrategy": TestStrategy,
    "TextClassification": TextClassification,
    "TextClassificationDocumentResult": TextClassificationDocumentResult,
    "TextClassificationEvaluationResults": TextClassificationEvaluationResults,
    "TextClassificationModelDetails": TextClassificationModelDetails,
    "TextClassificationModelEvaluationResult": TextClassificationModelEvaluationResult,
    "TextClassificationModelMetrics": TextClassificationModelMetrics,
    "TextDocument": TextDocument,
    "TranslationDocumentResult": TranslationDocumentResult,
    "UpdateEndpointDetails": UpdateEndpointDetails,
    "UpdateModelDetails": UpdateModelDetails,
    "UpdateProjectDetails": UpdateProjectDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestLogCollection": WorkRequestLogCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
