# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .analyze_document_details import AnalyzeDocumentDetails
from .analyze_document_result import AnalyzeDocumentResult
from .analyze_image_details import AnalyzeImageDetails
from .analyze_image_result import AnalyzeImageResult
from .bounding_polygon import BoundingPolygon
from .cell import Cell
from .change_model_compartment_details import ChangeModelCompartmentDetails
from .change_project_compartment_details import ChangeProjectCompartmentDetails
from .create_document_job_details import CreateDocumentJobDetails
from .create_image_job_details import CreateImageJobDetails
from .create_model_details import CreateModelDetails
from .create_project_details import CreateProjectDetails
from .data_science_labeling_dataset import DataScienceLabelingDataset
from .dataset import Dataset
from .detected_document_type import DetectedDocumentType
from .detected_language import DetectedLanguage
from .dimensions import Dimensions
from .document_classification_feature import DocumentClassificationFeature
from .document_details import DocumentDetails
from .document_feature import DocumentFeature
from .document_field import DocumentField
from .document_job import DocumentJob
from .document_key_value_detection_feature import DocumentKeyValueDetectionFeature
from .document_language_classification_feature import DocumentLanguageClassificationFeature
from .document_metadata import DocumentMetadata
from .document_table_detection_feature import DocumentTableDetectionFeature
from .document_text_detection_feature import DocumentTextDetectionFeature
from .field_label import FieldLabel
from .field_name import FieldName
from .field_value import FieldValue
from .image_classification_feature import ImageClassificationFeature
from .image_details import ImageDetails
from .image_feature import ImageFeature
from .image_job import ImageJob
from .image_object import ImageObject
from .image_object_detection_feature import ImageObjectDetectionFeature
from .image_text import ImageText
from .image_text_detection_feature import ImageTextDetectionFeature
from .inline_document_details import InlineDocumentDetails
from .inline_image_details import InlineImageDetails
from .input_location import InputLocation
from .label import Label
from .line import Line
from .model import Model
from .model_collection import ModelCollection
from .model_summary import ModelSummary
from .normalized_vertex import NormalizedVertex
from .object_list_inline_input_location import ObjectListInlineInputLocation
from .object_location import ObjectLocation
from .object_storage_dataset import ObjectStorageDataset
from .object_storage_document_details import ObjectStorageDocumentDetails
from .object_storage_image_details import ObjectStorageImageDetails
from .ontology_class import OntologyClass
from .output_location import OutputLocation
from .page import Page
from .processing_error import ProcessingError
from .project import Project
from .project_collection import ProjectCollection
from .project_summary import ProjectSummary
from .table import Table
from .table_row import TableRow
from .update_model_details import UpdateModelDetails
from .update_project_details import UpdateProjectDetails
from .value_array import ValueArray
from .value_date import ValueDate
from .value_integer import ValueInteger
from .value_number import ValueNumber
from .value_phone_number import ValuePhoneNumber
from .value_string import ValueString
from .value_time import ValueTime
from .word import Word
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for ai_vision services.
ai_vision_type_mapping = {
    "AnalyzeDocumentDetails": AnalyzeDocumentDetails,
    "AnalyzeDocumentResult": AnalyzeDocumentResult,
    "AnalyzeImageDetails": AnalyzeImageDetails,
    "AnalyzeImageResult": AnalyzeImageResult,
    "BoundingPolygon": BoundingPolygon,
    "Cell": Cell,
    "ChangeModelCompartmentDetails": ChangeModelCompartmentDetails,
    "ChangeProjectCompartmentDetails": ChangeProjectCompartmentDetails,
    "CreateDocumentJobDetails": CreateDocumentJobDetails,
    "CreateImageJobDetails": CreateImageJobDetails,
    "CreateModelDetails": CreateModelDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "DataScienceLabelingDataset": DataScienceLabelingDataset,
    "Dataset": Dataset,
    "DetectedDocumentType": DetectedDocumentType,
    "DetectedLanguage": DetectedLanguage,
    "Dimensions": Dimensions,
    "DocumentClassificationFeature": DocumentClassificationFeature,
    "DocumentDetails": DocumentDetails,
    "DocumentFeature": DocumentFeature,
    "DocumentField": DocumentField,
    "DocumentJob": DocumentJob,
    "DocumentKeyValueDetectionFeature": DocumentKeyValueDetectionFeature,
    "DocumentLanguageClassificationFeature": DocumentLanguageClassificationFeature,
    "DocumentMetadata": DocumentMetadata,
    "DocumentTableDetectionFeature": DocumentTableDetectionFeature,
    "DocumentTextDetectionFeature": DocumentTextDetectionFeature,
    "FieldLabel": FieldLabel,
    "FieldName": FieldName,
    "FieldValue": FieldValue,
    "ImageClassificationFeature": ImageClassificationFeature,
    "ImageDetails": ImageDetails,
    "ImageFeature": ImageFeature,
    "ImageJob": ImageJob,
    "ImageObject": ImageObject,
    "ImageObjectDetectionFeature": ImageObjectDetectionFeature,
    "ImageText": ImageText,
    "ImageTextDetectionFeature": ImageTextDetectionFeature,
    "InlineDocumentDetails": InlineDocumentDetails,
    "InlineImageDetails": InlineImageDetails,
    "InputLocation": InputLocation,
    "Label": Label,
    "Line": Line,
    "Model": Model,
    "ModelCollection": ModelCollection,
    "ModelSummary": ModelSummary,
    "NormalizedVertex": NormalizedVertex,
    "ObjectListInlineInputLocation": ObjectListInlineInputLocation,
    "ObjectLocation": ObjectLocation,
    "ObjectStorageDataset": ObjectStorageDataset,
    "ObjectStorageDocumentDetails": ObjectStorageDocumentDetails,
    "ObjectStorageImageDetails": ObjectStorageImageDetails,
    "OntologyClass": OntologyClass,
    "OutputLocation": OutputLocation,
    "Page": Page,
    "ProcessingError": ProcessingError,
    "Project": Project,
    "ProjectCollection": ProjectCollection,
    "ProjectSummary": ProjectSummary,
    "Table": Table,
    "TableRow": TableRow,
    "UpdateModelDetails": UpdateModelDetails,
    "UpdateProjectDetails": UpdateProjectDetails,
    "ValueArray": ValueArray,
    "ValueDate": ValueDate,
    "ValueInteger": ValueInteger,
    "ValueNumber": ValueNumber,
    "ValuePhoneNumber": ValuePhoneNumber,
    "ValueString": ValueString,
    "ValueTime": ValueTime,
    "Word": Word,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
