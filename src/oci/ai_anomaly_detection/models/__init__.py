# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .ai_private_endpoint import AiPrivateEndpoint
from .ai_private_endpoint_collection import AiPrivateEndpointCollection
from .ai_private_endpoint_summary import AiPrivateEndpointSummary
from .anomaly import Anomaly
from .anomaly_detect_result import AnomalyDetectResult
from .change_ai_private_endpoint_compartment_details import ChangeAiPrivateEndpointCompartmentDetails
from .change_data_asset_compartment_details import ChangeDataAssetCompartmentDetails
from .change_model_compartment_details import ChangeModelCompartmentDetails
from .change_project_compartment_details import ChangeProjectCompartmentDetails
from .create_ai_private_endpoint_details import CreateAiPrivateEndpointDetails
from .create_data_asset_details import CreateDataAssetDetails
from .create_model_details import CreateModelDetails
from .create_project_details import CreateProjectDetails
from .data_asset import DataAsset
from .data_asset_collection import DataAssetCollection
from .data_asset_summary import DataAssetSummary
from .data_item import DataItem
from .data_source_details import DataSourceDetails
from .data_source_details_atp import DataSourceDetailsATP
from .data_source_details_influx import DataSourceDetailsInflux
from .data_source_details_object_storage import DataSourceDetailsObjectStorage
from .detect_anomalies_details import DetectAnomaliesDetails
from .detection_result_item import DetectionResultItem
from .embedded_detect_anomalies_request import EmbeddedDetectAnomaliesRequest
from .influx_details import InfluxDetails
from .influx_details_v1v8 import InfluxDetailsV1v8
from .influx_details_v2v0 import InfluxDetailsV2v0
from .inline_detect_anomalies_request import InlineDetectAnomaliesRequest
from .model import Model
from .model_collection import ModelCollection
from .model_summary import ModelSummary
from .model_training_details import ModelTrainingDetails
from .model_training_results import ModelTrainingResults
from .per_signal_details import PerSignalDetails
from .project import Project
from .project_collection import ProjectCollection
from .project_summary import ProjectSummary
from .row_reduction_details import RowReductionDetails
from .update_ai_private_endpoint_details import UpdateAiPrivateEndpointDetails
from .update_data_asset_details import UpdateDataAssetDetails
from .update_model_details import UpdateModelDetails
from .update_project_details import UpdateProjectDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for ai_anomaly_detection services.
ai_anomaly_detection_type_mapping = {
    "AiPrivateEndpoint": AiPrivateEndpoint,
    "AiPrivateEndpointCollection": AiPrivateEndpointCollection,
    "AiPrivateEndpointSummary": AiPrivateEndpointSummary,
    "Anomaly": Anomaly,
    "AnomalyDetectResult": AnomalyDetectResult,
    "ChangeAiPrivateEndpointCompartmentDetails": ChangeAiPrivateEndpointCompartmentDetails,
    "ChangeDataAssetCompartmentDetails": ChangeDataAssetCompartmentDetails,
    "ChangeModelCompartmentDetails": ChangeModelCompartmentDetails,
    "ChangeProjectCompartmentDetails": ChangeProjectCompartmentDetails,
    "CreateAiPrivateEndpointDetails": CreateAiPrivateEndpointDetails,
    "CreateDataAssetDetails": CreateDataAssetDetails,
    "CreateModelDetails": CreateModelDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "DataAsset": DataAsset,
    "DataAssetCollection": DataAssetCollection,
    "DataAssetSummary": DataAssetSummary,
    "DataItem": DataItem,
    "DataSourceDetails": DataSourceDetails,
    "DataSourceDetailsATP": DataSourceDetailsATP,
    "DataSourceDetailsInflux": DataSourceDetailsInflux,
    "DataSourceDetailsObjectStorage": DataSourceDetailsObjectStorage,
    "DetectAnomaliesDetails": DetectAnomaliesDetails,
    "DetectionResultItem": DetectionResultItem,
    "EmbeddedDetectAnomaliesRequest": EmbeddedDetectAnomaliesRequest,
    "InfluxDetails": InfluxDetails,
    "InfluxDetailsV1v8": InfluxDetailsV1v8,
    "InfluxDetailsV2v0": InfluxDetailsV2v0,
    "InlineDetectAnomaliesRequest": InlineDetectAnomaliesRequest,
    "Model": Model,
    "ModelCollection": ModelCollection,
    "ModelSummary": ModelSummary,
    "ModelTrainingDetails": ModelTrainingDetails,
    "ModelTrainingResults": ModelTrainingResults,
    "PerSignalDetails": PerSignalDetails,
    "Project": Project,
    "ProjectCollection": ProjectCollection,
    "ProjectSummary": ProjectSummary,
    "RowReductionDetails": RowReductionDetails,
    "UpdateAiPrivateEndpointDetails": UpdateAiPrivateEndpointDetails,
    "UpdateDataAssetDetails": UpdateDataAssetDetails,
    "UpdateModelDetails": UpdateModelDetails,
    "UpdateProjectDetails": UpdateProjectDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
