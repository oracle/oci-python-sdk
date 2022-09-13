# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .artifact_export_details import ArtifactExportDetails
from .artifact_export_details_object_storage import ArtifactExportDetailsObjectStorage
from .artifact_import_details import ArtifactImportDetails
from .artifact_import_details_object_storage import ArtifactImportDetailsObjectStorage
from .category_log_details import CategoryLogDetails
from .change_job_compartment_details import ChangeJobCompartmentDetails
from .change_job_run_compartment_details import ChangeJobRunCompartmentDetails
from .change_model_compartment_details import ChangeModelCompartmentDetails
from .change_model_deployment_compartment_details import ChangeModelDeploymentCompartmentDetails
from .change_notebook_session_compartment_details import ChangeNotebookSessionCompartmentDetails
from .change_project_compartment_details import ChangeProjectCompartmentDetails
from .create_job_details import CreateJobDetails
from .create_job_run_details import CreateJobRunDetails
from .create_model_deployment_details import CreateModelDeploymentDetails
from .create_model_details import CreateModelDetails
from .create_model_provenance_details import CreateModelProvenanceDetails
from .create_notebook_session_details import CreateNotebookSessionDetails
from .create_project_details import CreateProjectDetails
from .default_job_configuration_details import DefaultJobConfigurationDetails
from .export_model_artifact_details import ExportModelArtifactDetails
from .fast_launch_job_config_summary import FastLaunchJobConfigSummary
from .fixed_size_scaling_policy import FixedSizeScalingPolicy
from .import_model_artifact_details import ImportModelArtifactDetails
from .instance_configuration import InstanceConfiguration
from .job import Job
from .job_configuration_details import JobConfigurationDetails
from .job_infrastructure_configuration_details import JobInfrastructureConfigurationDetails
from .job_log_configuration_details import JobLogConfigurationDetails
from .job_run import JobRun
from .job_run_log_details import JobRunLogDetails
from .job_run_summary import JobRunSummary
from .job_shape_config_details import JobShapeConfigDetails
from .job_shape_summary import JobShapeSummary
from .job_summary import JobSummary
from .log_details import LogDetails
from .managed_egress_standalone_job_infrastructure_configuration_details import ManagedEgressStandaloneJobInfrastructureConfigurationDetails
from .metadata import Metadata
from .model import Model
from .model_configuration_details import ModelConfigurationDetails
from .model_deployment import ModelDeployment
from .model_deployment_configuration_details import ModelDeploymentConfigurationDetails
from .model_deployment_instance_shape_config_details import ModelDeploymentInstanceShapeConfigDetails
from .model_deployment_shape_summary import ModelDeploymentShapeSummary
from .model_deployment_summary import ModelDeploymentSummary
from .model_provenance import ModelProvenance
from .model_summary import ModelSummary
from .notebook_session import NotebookSession
from .notebook_session_config_details import NotebookSessionConfigDetails
from .notebook_session_configuration_details import NotebookSessionConfigurationDetails
from .notebook_session_git_config_details import NotebookSessionGitConfigDetails
from .notebook_session_git_repo_config_details import NotebookSessionGitRepoConfigDetails
from .notebook_session_runtime_config_details import NotebookSessionRuntimeConfigDetails
from .notebook_session_shape_config_details import NotebookSessionShapeConfigDetails
from .notebook_session_shape_summary import NotebookSessionShapeSummary
from .notebook_session_summary import NotebookSessionSummary
from .project import Project
from .project_summary import ProjectSummary
from .scaling_policy import ScalingPolicy
from .single_model_deployment_configuration_details import SingleModelDeploymentConfigurationDetails
from .standalone_job_infrastructure_configuration_details import StandaloneJobInfrastructureConfigurationDetails
from .update_category_log_details import UpdateCategoryLogDetails
from .update_job_details import UpdateJobDetails
from .update_job_run_details import UpdateJobRunDetails
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
    "ArtifactExportDetails": ArtifactExportDetails,
    "ArtifactExportDetailsObjectStorage": ArtifactExportDetailsObjectStorage,
    "ArtifactImportDetails": ArtifactImportDetails,
    "ArtifactImportDetailsObjectStorage": ArtifactImportDetailsObjectStorage,
    "CategoryLogDetails": CategoryLogDetails,
    "ChangeJobCompartmentDetails": ChangeJobCompartmentDetails,
    "ChangeJobRunCompartmentDetails": ChangeJobRunCompartmentDetails,
    "ChangeModelCompartmentDetails": ChangeModelCompartmentDetails,
    "ChangeModelDeploymentCompartmentDetails": ChangeModelDeploymentCompartmentDetails,
    "ChangeNotebookSessionCompartmentDetails": ChangeNotebookSessionCompartmentDetails,
    "ChangeProjectCompartmentDetails": ChangeProjectCompartmentDetails,
    "CreateJobDetails": CreateJobDetails,
    "CreateJobRunDetails": CreateJobRunDetails,
    "CreateModelDeploymentDetails": CreateModelDeploymentDetails,
    "CreateModelDetails": CreateModelDetails,
    "CreateModelProvenanceDetails": CreateModelProvenanceDetails,
    "CreateNotebookSessionDetails": CreateNotebookSessionDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "DefaultJobConfigurationDetails": DefaultJobConfigurationDetails,
    "ExportModelArtifactDetails": ExportModelArtifactDetails,
    "FastLaunchJobConfigSummary": FastLaunchJobConfigSummary,
    "FixedSizeScalingPolicy": FixedSizeScalingPolicy,
    "ImportModelArtifactDetails": ImportModelArtifactDetails,
    "InstanceConfiguration": InstanceConfiguration,
    "Job": Job,
    "JobConfigurationDetails": JobConfigurationDetails,
    "JobInfrastructureConfigurationDetails": JobInfrastructureConfigurationDetails,
    "JobLogConfigurationDetails": JobLogConfigurationDetails,
    "JobRun": JobRun,
    "JobRunLogDetails": JobRunLogDetails,
    "JobRunSummary": JobRunSummary,
    "JobShapeConfigDetails": JobShapeConfigDetails,
    "JobShapeSummary": JobShapeSummary,
    "JobSummary": JobSummary,
    "LogDetails": LogDetails,
    "ManagedEgressStandaloneJobInfrastructureConfigurationDetails": ManagedEgressStandaloneJobInfrastructureConfigurationDetails,
    "Metadata": Metadata,
    "Model": Model,
    "ModelConfigurationDetails": ModelConfigurationDetails,
    "ModelDeployment": ModelDeployment,
    "ModelDeploymentConfigurationDetails": ModelDeploymentConfigurationDetails,
    "ModelDeploymentInstanceShapeConfigDetails": ModelDeploymentInstanceShapeConfigDetails,
    "ModelDeploymentShapeSummary": ModelDeploymentShapeSummary,
    "ModelDeploymentSummary": ModelDeploymentSummary,
    "ModelProvenance": ModelProvenance,
    "ModelSummary": ModelSummary,
    "NotebookSession": NotebookSession,
    "NotebookSessionConfigDetails": NotebookSessionConfigDetails,
    "NotebookSessionConfigurationDetails": NotebookSessionConfigurationDetails,
    "NotebookSessionGitConfigDetails": NotebookSessionGitConfigDetails,
    "NotebookSessionGitRepoConfigDetails": NotebookSessionGitRepoConfigDetails,
    "NotebookSessionRuntimeConfigDetails": NotebookSessionRuntimeConfigDetails,
    "NotebookSessionShapeConfigDetails": NotebookSessionShapeConfigDetails,
    "NotebookSessionShapeSummary": NotebookSessionShapeSummary,
    "NotebookSessionSummary": NotebookSessionSummary,
    "Project": Project,
    "ProjectSummary": ProjectSummary,
    "ScalingPolicy": ScalingPolicy,
    "SingleModelDeploymentConfigurationDetails": SingleModelDeploymentConfigurationDetails,
    "StandaloneJobInfrastructureConfigurationDetails": StandaloneJobInfrastructureConfigurationDetails,
    "UpdateCategoryLogDetails": UpdateCategoryLogDetails,
    "UpdateJobDetails": UpdateJobDetails,
    "UpdateJobRunDetails": UpdateJobRunDetails,
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
