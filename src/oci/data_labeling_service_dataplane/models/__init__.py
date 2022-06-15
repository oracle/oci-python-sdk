# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .annotation import Annotation
from .annotation_aggregation_dimensions import AnnotationAggregationDimensions
from .annotation_analytics_aggregation import AnnotationAnalyticsAggregation
from .annotation_analytics_aggregation_collection import AnnotationAnalyticsAggregationCollection
from .annotation_collection import AnnotationCollection
from .annotation_summary import AnnotationSummary
from .bounding_polygon import BoundingPolygon
from .create_annotation_details import CreateAnnotationDetails
from .create_object_storage_source_details import CreateObjectStorageSourceDetails
from .create_record_details import CreateRecordDetails
from .create_source_details import CreateSourceDetails
from .dataset import Dataset
from .dataset_format_details import DatasetFormatDetails
from .dataset_source_details import DatasetSourceDetails
from .delimited_file_type_metadata import DelimitedFileTypeMetadata
from .document_dataset_format_details import DocumentDatasetFormatDetails
from .document_metadata import DocumentMetadata
from .entity import Entity
from .generic_entity import GenericEntity
from .image_dataset_format_details import ImageDatasetFormatDetails
from .image_metadata import ImageMetadata
from .image_object_selection_entity import ImageObjectSelectionEntity
from .initial_record_generation_configuration import InitialRecordGenerationConfiguration
from .label import Label
from .label_name import LabelName
from .label_set import LabelSet
from .normalized_vertex import NormalizedVertex
from .object_storage_dataset_source_details import ObjectStorageDatasetSourceDetails
from .object_storage_source_details import ObjectStorageSourceDetails
from .record import Record
from .record_aggregation_dimensions import RecordAggregationDimensions
from .record_analytics_aggregation import RecordAnalyticsAggregation
from .record_analytics_aggregation_collection import RecordAnalyticsAggregationCollection
from .record_collection import RecordCollection
from .record_metadata import RecordMetadata
from .record_summary import RecordSummary
from .source_details import SourceDetails
from .text_dataset_format_details import TextDatasetFormatDetails
from .text_file_type_metadata import TextFileTypeMetadata
from .text_metadata import TextMetadata
from .text_selection_entity import TextSelectionEntity
from .text_span import TextSpan
from .update_annotation_details import UpdateAnnotationDetails
from .update_record_details import UpdateRecordDetails

# Maps type names to classes for data_labeling_service_dataplane services.
data_labeling_service_dataplane_type_mapping = {
    "Annotation": Annotation,
    "AnnotationAggregationDimensions": AnnotationAggregationDimensions,
    "AnnotationAnalyticsAggregation": AnnotationAnalyticsAggregation,
    "AnnotationAnalyticsAggregationCollection": AnnotationAnalyticsAggregationCollection,
    "AnnotationCollection": AnnotationCollection,
    "AnnotationSummary": AnnotationSummary,
    "BoundingPolygon": BoundingPolygon,
    "CreateAnnotationDetails": CreateAnnotationDetails,
    "CreateObjectStorageSourceDetails": CreateObjectStorageSourceDetails,
    "CreateRecordDetails": CreateRecordDetails,
    "CreateSourceDetails": CreateSourceDetails,
    "Dataset": Dataset,
    "DatasetFormatDetails": DatasetFormatDetails,
    "DatasetSourceDetails": DatasetSourceDetails,
    "DelimitedFileTypeMetadata": DelimitedFileTypeMetadata,
    "DocumentDatasetFormatDetails": DocumentDatasetFormatDetails,
    "DocumentMetadata": DocumentMetadata,
    "Entity": Entity,
    "GenericEntity": GenericEntity,
    "ImageDatasetFormatDetails": ImageDatasetFormatDetails,
    "ImageMetadata": ImageMetadata,
    "ImageObjectSelectionEntity": ImageObjectSelectionEntity,
    "InitialRecordGenerationConfiguration": InitialRecordGenerationConfiguration,
    "Label": Label,
    "LabelName": LabelName,
    "LabelSet": LabelSet,
    "NormalizedVertex": NormalizedVertex,
    "ObjectStorageDatasetSourceDetails": ObjectStorageDatasetSourceDetails,
    "ObjectStorageSourceDetails": ObjectStorageSourceDetails,
    "Record": Record,
    "RecordAggregationDimensions": RecordAggregationDimensions,
    "RecordAnalyticsAggregation": RecordAnalyticsAggregation,
    "RecordAnalyticsAggregationCollection": RecordAnalyticsAggregationCollection,
    "RecordCollection": RecordCollection,
    "RecordMetadata": RecordMetadata,
    "RecordSummary": RecordSummary,
    "SourceDetails": SourceDetails,
    "TextDatasetFormatDetails": TextDatasetFormatDetails,
    "TextFileTypeMetadata": TextFileTypeMetadata,
    "TextMetadata": TextMetadata,
    "TextSelectionEntity": TextSelectionEntity,
    "TextSpan": TextSpan,
    "UpdateAnnotationDetails": UpdateAnnotationDetails,
    "UpdateRecordDetails": UpdateRecordDetails
}
