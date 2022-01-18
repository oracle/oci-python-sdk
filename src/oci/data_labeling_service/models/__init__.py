# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_dataset_labels_details import AddDatasetLabelsDetails
from .annotation_format import AnnotationFormat
from .annotation_format_collection import AnnotationFormatCollection
from .annotation_format_summary import AnnotationFormatSummary
from .change_dataset_compartment_details import ChangeDatasetCompartmentDetails
from .create_dataset_details import CreateDatasetDetails
from .dataset import Dataset
from .dataset_collection import DatasetCollection
from .dataset_format_details import DatasetFormatDetails
from .dataset_source_details import DatasetSourceDetails
from .dataset_summary import DatasetSummary
from .document_dataset_format_details import DocumentDatasetFormatDetails
from .export_format import ExportFormat
from .generate_dataset_records_details import GenerateDatasetRecordsDetails
from .image_dataset_format_details import ImageDatasetFormatDetails
from .initial_record_generation_configuration import InitialRecordGenerationConfiguration
from .label import Label
from .label_set import LabelSet
from .object_storage_snapshot_export_details import ObjectStorageSnapshotExportDetails
from .object_storage_source_details import ObjectStorageSourceDetails
from .remove_dataset_labels_details import RemoveDatasetLabelsDetails
from .rename_dataset_labels_details import RenameDatasetLabelsDetails
from .snapshot_dataset_details import SnapshotDatasetDetails
from .snapshot_export_details import SnapshotExportDetails
from .text_dataset_format_details import TextDatasetFormatDetails
from .update_dataset_details import UpdateDatasetDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for data_labeling_service services.
data_labeling_service_type_mapping = {
    "AddDatasetLabelsDetails": AddDatasetLabelsDetails,
    "AnnotationFormat": AnnotationFormat,
    "AnnotationFormatCollection": AnnotationFormatCollection,
    "AnnotationFormatSummary": AnnotationFormatSummary,
    "ChangeDatasetCompartmentDetails": ChangeDatasetCompartmentDetails,
    "CreateDatasetDetails": CreateDatasetDetails,
    "Dataset": Dataset,
    "DatasetCollection": DatasetCollection,
    "DatasetFormatDetails": DatasetFormatDetails,
    "DatasetSourceDetails": DatasetSourceDetails,
    "DatasetSummary": DatasetSummary,
    "DocumentDatasetFormatDetails": DocumentDatasetFormatDetails,
    "ExportFormat": ExportFormat,
    "GenerateDatasetRecordsDetails": GenerateDatasetRecordsDetails,
    "ImageDatasetFormatDetails": ImageDatasetFormatDetails,
    "InitialRecordGenerationConfiguration": InitialRecordGenerationConfiguration,
    "Label": Label,
    "LabelSet": LabelSet,
    "ObjectStorageSnapshotExportDetails": ObjectStorageSnapshotExportDetails,
    "ObjectStorageSourceDetails": ObjectStorageSourceDetails,
    "RemoveDatasetLabelsDetails": RemoveDatasetLabelsDetails,
    "RenameDatasetLabelsDetails": RenameDatasetLabelsDetails,
    "SnapshotDatasetDetails": SnapshotDatasetDetails,
    "SnapshotExportDetails": SnapshotExportDetails,
    "TextDatasetFormatDetails": TextDatasetFormatDetails,
    "UpdateDatasetDetails": UpdateDatasetDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
