# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .analyze_document_result import AnalyzeDocumentResult
from .bounding_polygon import BoundingPolygon
from .cell import Cell
from .create_processor_job_details import CreateProcessorJobDetails
from .detected_document_type import DetectedDocumentType
from .detected_language import DetectedLanguage
from .dimensions import Dimensions
from .document_classification_feature import DocumentClassificationFeature
from .document_feature import DocumentFeature
from .document_field import DocumentField
from .document_key_value_extraction_feature import DocumentKeyValueExtractionFeature
from .document_language_classification_feature import DocumentLanguageClassificationFeature
from .document_metadata import DocumentMetadata
from .document_table_extraction_feature import DocumentTableExtractionFeature
from .document_text_extraction_feature import DocumentTextExtractionFeature
from .field_label import FieldLabel
from .field_name import FieldName
from .field_value import FieldValue
from .general_processor_config import GeneralProcessorConfig
from .inline_document_content import InlineDocumentContent
from .input_location import InputLocation
from .line import Line
from .normalized_vertex import NormalizedVertex
from .object_location import ObjectLocation
from .object_storage_locations import ObjectStorageLocations
from .output_location import OutputLocation
from .page import Page
from .processing_error import ProcessingError
from .processor_config import ProcessorConfig
from .processor_job import ProcessorJob
from .table import Table
from .table_row import TableRow
from .value_array import ValueArray
from .value_date import ValueDate
from .value_integer import ValueInteger
from .value_number import ValueNumber
from .value_phone_number import ValuePhoneNumber
from .value_string import ValueString
from .value_time import ValueTime
from .word import Word

# Maps type names to classes for ai_document services.
ai_document_type_mapping = {
    "AnalyzeDocumentResult": AnalyzeDocumentResult,
    "BoundingPolygon": BoundingPolygon,
    "Cell": Cell,
    "CreateProcessorJobDetails": CreateProcessorJobDetails,
    "DetectedDocumentType": DetectedDocumentType,
    "DetectedLanguage": DetectedLanguage,
    "Dimensions": Dimensions,
    "DocumentClassificationFeature": DocumentClassificationFeature,
    "DocumentFeature": DocumentFeature,
    "DocumentField": DocumentField,
    "DocumentKeyValueExtractionFeature": DocumentKeyValueExtractionFeature,
    "DocumentLanguageClassificationFeature": DocumentLanguageClassificationFeature,
    "DocumentMetadata": DocumentMetadata,
    "DocumentTableExtractionFeature": DocumentTableExtractionFeature,
    "DocumentTextExtractionFeature": DocumentTextExtractionFeature,
    "FieldLabel": FieldLabel,
    "FieldName": FieldName,
    "FieldValue": FieldValue,
    "GeneralProcessorConfig": GeneralProcessorConfig,
    "InlineDocumentContent": InlineDocumentContent,
    "InputLocation": InputLocation,
    "Line": Line,
    "NormalizedVertex": NormalizedVertex,
    "ObjectLocation": ObjectLocation,
    "ObjectStorageLocations": ObjectStorageLocations,
    "OutputLocation": OutputLocation,
    "Page": Page,
    "ProcessingError": ProcessingError,
    "ProcessorConfig": ProcessorConfig,
    "ProcessorJob": ProcessorJob,
    "Table": Table,
    "TableRow": TableRow,
    "ValueArray": ValueArray,
    "ValueDate": ValueDate,
    "ValueInteger": ValueInteger,
    "ValueNumber": ValueNumber,
    "ValuePhoneNumber": ValuePhoneNumber,
    "ValueString": ValueString,
    "ValueTime": ValueTime,
    "Word": Word
}
