# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .category_log_details import CategoryLogDetails
from .change_model_compartment_details import ChangeModelCompartmentDetails
from .change_model_deployment_compartment_details import ChangeModelDeploymentCompartmentDetails
from .change_notebook_session_compartment_details import ChangeNotebookSessionCompartmentDetails
from .change_project_compartment_details import ChangeProjectCompartmentDetails
from .create_model_deployment_details import CreateModelDeploymentDetails
from .create_model_details import CreateModelDetails
from .create_model_provenance_details import CreateModelProvenanceDetails
from .create_notebook_session_details import CreateNotebookSessionDetails
from .create_project_details import CreateProjectDetails
from .fixed_size_scaling_policy import FixedSizeScalingPolicy
from .instance_configuration import InstanceConfiguration
from .log_details import LogDetails
from .model import Model
from .model_configuration_details import ModelConfigurationDetails
from .model_deployment import ModelDeployment
from .model_deployment_configuration_details import ModelDeploymentConfigurationDetails
from .model_deployment_shape_summary import ModelDeploymentShapeSummary
from .model_deployment_summary import ModelDeploymentSummary
from .model_provenance import ModelProvenance
from .model_summary import ModelSummary
from .notebook_session import NotebookSession
from .notebook_session_configuration_details import NotebookSessionConfigurationDetails
from .notebook_session_shape_config_details import NotebookSessionShapeConfigDetails
from .notebook_session_shape_summary import NotebookSessionShapeSummary
from .notebook_session_summary import NotebookSessionSummary
from .project import Project
from .project_summary import ProjectSummary
from .scaling_policy import ScalingPolicy
from .single_model_deployment_configuration_details import SingleModelDeploymentConfigurationDetails
from .update_category_log_details import UpdateCategoryLogDetails
from .update_model_configuration_details import UpdateModelConfigurationDetails
from .update_model_deployment_configuration_details import UpdateModelDeploymentConfigurationDetails
from .update_model_deployment_details import UpdateModelDeploymentDetails
from .update_model_details import UpdateModelDetails
from .update_model_provenance_details import UpdateModelProvenanceDetails
from .update_notebook_session_details import UpdateNotebookSessionDetails
from .update_project_details import UpdateProjectDetails
from .update_single_model_deployment_configuration_details import UpdateSingleModelDeploymentConfigurationDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for data_science services.
data_science_type_mapping = {
    "CategoryLogDetails": CategoryLogDetails,
    "ChangeModelCompartmentDetails": ChangeModelCompartmentDetails,
    "ChangeModelDeploymentCompartmentDetails": ChangeModelDeploymentCompartmentDetails,
    "ChangeNotebookSessionCompartmentDetails": ChangeNotebookSessionCompartmentDetails,
    "ChangeProjectCompartmentDetails": ChangeProjectCompartmentDetails,
    "CreateModelDeploymentDetails": CreateModelDeploymentDetails,
    "CreateModelDetails": CreateModelDetails,
    "CreateModelProvenanceDetails": CreateModelProvenanceDetails,
    "CreateNotebookSessionDetails": CreateNotebookSessionDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "FixedSizeScalingPolicy": FixedSizeScalingPolicy,
    "InstanceConfiguration": InstanceConfiguration,
    "LogDetails": LogDetails,
    "Model": Model,
    "ModelConfigurationDetails": ModelConfigurationDetails,
    "ModelDeployment": ModelDeployment,
    "ModelDeploymentConfigurationDetails": ModelDeploymentConfigurationDetails,
    "ModelDeploymentShapeSummary": ModelDeploymentShapeSummary,
    "ModelDeploymentSummary": ModelDeploymentSummary,
    "ModelProvenance": ModelProvenance,
    "ModelSummary": ModelSummary,
    "NotebookSession": NotebookSession,
    "NotebookSessionConfigurationDetails": NotebookSessionConfigurationDetails,
    "NotebookSessionShapeConfigDetails": NotebookSessionShapeConfigDetails,
    "NotebookSessionShapeSummary": NotebookSessionShapeSummary,
    "NotebookSessionSummary": NotebookSessionSummary,
    "Project": Project,
    "ProjectSummary": ProjectSummary,
    "ScalingPolicy": ScalingPolicy,
    "SingleModelDeploymentConfigurationDetails": SingleModelDeploymentConfigurationDetails,
    "UpdateCategoryLogDetails": UpdateCategoryLogDetails,
    "UpdateModelConfigurationDetails": UpdateModelConfigurationDetails,
    "UpdateModelDeploymentConfigurationDetails": UpdateModelDeploymentConfigurationDetails,
    "UpdateModelDeploymentDetails": UpdateModelDeploymentDetails,
    "UpdateModelDetails": UpdateModelDetails,
    "UpdateModelProvenanceDetails": UpdateModelProvenanceDetails,
    "UpdateNotebookSessionDetails": UpdateNotebookSessionDetails,
    "UpdateProjectDetails": UpdateProjectDetails,
    "UpdateSingleModelDeploymentConfigurationDetails": UpdateSingleModelDeploymentConfigurationDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
