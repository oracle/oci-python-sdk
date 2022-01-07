# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .apply_job_operation_details import ApplyJobOperationDetails
from .apply_job_operation_details_summary import ApplyJobOperationDetailsSummary
from .apply_job_plan_resolution import ApplyJobPlanResolution
from .cancellation_details import CancellationDetails
from .change_configuration_source_provider_compartment_details import ChangeConfigurationSourceProviderCompartmentDetails
from .change_stack_compartment_details import ChangeStackCompartmentDetails
from .change_template_compartment_details import ChangeTemplateCompartmentDetails
from .compartment_config_source import CompartmentConfigSource
from .config_source import ConfigSource
from .config_source_record import ConfigSourceRecord
from .configuration_source_provider import ConfigurationSourceProvider
from .configuration_source_provider_collection import ConfigurationSourceProviderCollection
from .configuration_source_provider_summary import ConfigurationSourceProviderSummary
from .create_apply_job_operation_details import CreateApplyJobOperationDetails
from .create_compartment_config_source_details import CreateCompartmentConfigSourceDetails
from .create_config_source_details import CreateConfigSourceDetails
from .create_configuration_source_provider_details import CreateConfigurationSourceProviderDetails
from .create_destroy_job_operation_details import CreateDestroyJobOperationDetails
from .create_git_config_source_details import CreateGitConfigSourceDetails
from .create_github_access_token_configuration_source_provider_details import CreateGithubAccessTokenConfigurationSourceProviderDetails
from .create_gitlab_access_token_configuration_source_provider_details import CreateGitlabAccessTokenConfigurationSourceProviderDetails
from .create_import_tf_state_job_operation_details import CreateImportTfStateJobOperationDetails
from .create_job_details import CreateJobDetails
from .create_job_operation_details import CreateJobOperationDetails
from .create_object_storage_config_source_details import CreateObjectStorageConfigSourceDetails
from .create_plan_job_operation_details import CreatePlanJobOperationDetails
from .create_stack_details import CreateStackDetails
from .create_stack_template_config_source_details import CreateStackTemplateConfigSourceDetails
from .create_template_config_source_details import CreateTemplateConfigSourceDetails
from .create_template_details import CreateTemplateDetails
from .create_template_zip_upload_config_source_details import CreateTemplateZipUploadConfigSourceDetails
from .create_zip_upload_config_source_details import CreateZipUploadConfigSourceDetails
from .destroy_job_operation_details import DestroyJobOperationDetails
from .destroy_job_operation_details_summary import DestroyJobOperationDetailsSummary
from .detect_stack_drift_details import DetectStackDriftDetails
from .failure_details import FailureDetails
from .git_config_source import GitConfigSource
from .git_config_source_record import GitConfigSourceRecord
from .github_access_token_configuration_source_provider import GithubAccessTokenConfigurationSourceProvider
from .github_access_token_configuration_source_provider_summary import GithubAccessTokenConfigurationSourceProviderSummary
from .gitlab_access_token_configuration_source_provider import GitlabAccessTokenConfigurationSourceProvider
from .gitlab_access_token_configuration_source_provider_summary import GitlabAccessTokenConfigurationSourceProviderSummary
from .import_tf_state_job_operation_details import ImportTfStateJobOperationDetails
from .import_tf_state_job_operation_details_summary import ImportTfStateJobOperationDetailsSummary
from .job import Job
from .job_operation_details import JobOperationDetails
from .job_operation_details_summary import JobOperationDetailsSummary
from .job_summary import JobSummary
from .log_entry import LogEntry
from .object_storage_config_source import ObjectStorageConfigSource
from .object_storage_config_source_record import ObjectStorageConfigSourceRecord
from .plan_job_operation_details import PlanJobOperationDetails
from .plan_job_operation_details_summary import PlanJobOperationDetailsSummary
from .resource_discovery_service_collection import ResourceDiscoveryServiceCollection
from .resource_discovery_service_summary import ResourceDiscoveryServiceSummary
from .stack import Stack
from .stack_resource_drift_collection import StackResourceDriftCollection
from .stack_resource_drift_summary import StackResourceDriftSummary
from .stack_summary import StackSummary
from .template import Template
from .template_category_summary import TemplateCategorySummary
from .template_category_summary_collection import TemplateCategorySummaryCollection
from .template_config_source import TemplateConfigSource
from .template_summary import TemplateSummary
from .template_summary_collection import TemplateSummaryCollection
from .template_zip_upload_config_source import TemplateZipUploadConfigSource
from .terraform_advanced_options import TerraformAdvancedOptions
from .terraform_version_collection import TerraformVersionCollection
from .terraform_version_summary import TerraformVersionSummary
from .update_config_source_details import UpdateConfigSourceDetails
from .update_configuration_source_provider_details import UpdateConfigurationSourceProviderDetails
from .update_git_config_source_details import UpdateGitConfigSourceDetails
from .update_github_access_token_configuration_source_provider_details import UpdateGithubAccessTokenConfigurationSourceProviderDetails
from .update_gitlab_access_token_configuration_source_provider_details import UpdateGitlabAccessTokenConfigurationSourceProviderDetails
from .update_job_details import UpdateJobDetails
from .update_object_storage_config_source_details import UpdateObjectStorageConfigSourceDetails
from .update_stack_details import UpdateStackDetails
from .update_template_config_source_details import UpdateTemplateConfigSourceDetails
from .update_template_details import UpdateTemplateDetails
from .update_template_zip_upload_config_source_details import UpdateTemplateZipUploadConfigSourceDetails
from .update_zip_upload_config_source_details import UpdateZipUploadConfigSourceDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .zip_upload_config_source import ZipUploadConfigSource
from .zip_upload_config_source_record import ZipUploadConfigSourceRecord

# Maps type names to classes for resource_manager services.
resource_manager_type_mapping = {
    "ApplyJobOperationDetails": ApplyJobOperationDetails,
    "ApplyJobOperationDetailsSummary": ApplyJobOperationDetailsSummary,
    "ApplyJobPlanResolution": ApplyJobPlanResolution,
    "CancellationDetails": CancellationDetails,
    "ChangeConfigurationSourceProviderCompartmentDetails": ChangeConfigurationSourceProviderCompartmentDetails,
    "ChangeStackCompartmentDetails": ChangeStackCompartmentDetails,
    "ChangeTemplateCompartmentDetails": ChangeTemplateCompartmentDetails,
    "CompartmentConfigSource": CompartmentConfigSource,
    "ConfigSource": ConfigSource,
    "ConfigSourceRecord": ConfigSourceRecord,
    "ConfigurationSourceProvider": ConfigurationSourceProvider,
    "ConfigurationSourceProviderCollection": ConfigurationSourceProviderCollection,
    "ConfigurationSourceProviderSummary": ConfigurationSourceProviderSummary,
    "CreateApplyJobOperationDetails": CreateApplyJobOperationDetails,
    "CreateCompartmentConfigSourceDetails": CreateCompartmentConfigSourceDetails,
    "CreateConfigSourceDetails": CreateConfigSourceDetails,
    "CreateConfigurationSourceProviderDetails": CreateConfigurationSourceProviderDetails,
    "CreateDestroyJobOperationDetails": CreateDestroyJobOperationDetails,
    "CreateGitConfigSourceDetails": CreateGitConfigSourceDetails,
    "CreateGithubAccessTokenConfigurationSourceProviderDetails": CreateGithubAccessTokenConfigurationSourceProviderDetails,
    "CreateGitlabAccessTokenConfigurationSourceProviderDetails": CreateGitlabAccessTokenConfigurationSourceProviderDetails,
    "CreateImportTfStateJobOperationDetails": CreateImportTfStateJobOperationDetails,
    "CreateJobDetails": CreateJobDetails,
    "CreateJobOperationDetails": CreateJobOperationDetails,
    "CreateObjectStorageConfigSourceDetails": CreateObjectStorageConfigSourceDetails,
    "CreatePlanJobOperationDetails": CreatePlanJobOperationDetails,
    "CreateStackDetails": CreateStackDetails,
    "CreateStackTemplateConfigSourceDetails": CreateStackTemplateConfigSourceDetails,
    "CreateTemplateConfigSourceDetails": CreateTemplateConfigSourceDetails,
    "CreateTemplateDetails": CreateTemplateDetails,
    "CreateTemplateZipUploadConfigSourceDetails": CreateTemplateZipUploadConfigSourceDetails,
    "CreateZipUploadConfigSourceDetails": CreateZipUploadConfigSourceDetails,
    "DestroyJobOperationDetails": DestroyJobOperationDetails,
    "DestroyJobOperationDetailsSummary": DestroyJobOperationDetailsSummary,
    "DetectStackDriftDetails": DetectStackDriftDetails,
    "FailureDetails": FailureDetails,
    "GitConfigSource": GitConfigSource,
    "GitConfigSourceRecord": GitConfigSourceRecord,
    "GithubAccessTokenConfigurationSourceProvider": GithubAccessTokenConfigurationSourceProvider,
    "GithubAccessTokenConfigurationSourceProviderSummary": GithubAccessTokenConfigurationSourceProviderSummary,
    "GitlabAccessTokenConfigurationSourceProvider": GitlabAccessTokenConfigurationSourceProvider,
    "GitlabAccessTokenConfigurationSourceProviderSummary": GitlabAccessTokenConfigurationSourceProviderSummary,
    "ImportTfStateJobOperationDetails": ImportTfStateJobOperationDetails,
    "ImportTfStateJobOperationDetailsSummary": ImportTfStateJobOperationDetailsSummary,
    "Job": Job,
    "JobOperationDetails": JobOperationDetails,
    "JobOperationDetailsSummary": JobOperationDetailsSummary,
    "JobSummary": JobSummary,
    "LogEntry": LogEntry,
    "ObjectStorageConfigSource": ObjectStorageConfigSource,
    "ObjectStorageConfigSourceRecord": ObjectStorageConfigSourceRecord,
    "PlanJobOperationDetails": PlanJobOperationDetails,
    "PlanJobOperationDetailsSummary": PlanJobOperationDetailsSummary,
    "ResourceDiscoveryServiceCollection": ResourceDiscoveryServiceCollection,
    "ResourceDiscoveryServiceSummary": ResourceDiscoveryServiceSummary,
    "Stack": Stack,
    "StackResourceDriftCollection": StackResourceDriftCollection,
    "StackResourceDriftSummary": StackResourceDriftSummary,
    "StackSummary": StackSummary,
    "Template": Template,
    "TemplateCategorySummary": TemplateCategorySummary,
    "TemplateCategorySummaryCollection": TemplateCategorySummaryCollection,
    "TemplateConfigSource": TemplateConfigSource,
    "TemplateSummary": TemplateSummary,
    "TemplateSummaryCollection": TemplateSummaryCollection,
    "TemplateZipUploadConfigSource": TemplateZipUploadConfigSource,
    "TerraformAdvancedOptions": TerraformAdvancedOptions,
    "TerraformVersionCollection": TerraformVersionCollection,
    "TerraformVersionSummary": TerraformVersionSummary,
    "UpdateConfigSourceDetails": UpdateConfigSourceDetails,
    "UpdateConfigurationSourceProviderDetails": UpdateConfigurationSourceProviderDetails,
    "UpdateGitConfigSourceDetails": UpdateGitConfigSourceDetails,
    "UpdateGithubAccessTokenConfigurationSourceProviderDetails": UpdateGithubAccessTokenConfigurationSourceProviderDetails,
    "UpdateGitlabAccessTokenConfigurationSourceProviderDetails": UpdateGitlabAccessTokenConfigurationSourceProviderDetails,
    "UpdateJobDetails": UpdateJobDetails,
    "UpdateObjectStorageConfigSourceDetails": UpdateObjectStorageConfigSourceDetails,
    "UpdateStackDetails": UpdateStackDetails,
    "UpdateTemplateConfigSourceDetails": UpdateTemplateConfigSourceDetails,
    "UpdateTemplateDetails": UpdateTemplateDetails,
    "UpdateTemplateZipUploadConfigSourceDetails": UpdateTemplateZipUploadConfigSourceDetails,
    "UpdateZipUploadConfigSourceDetails": UpdateZipUploadConfigSourceDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "ZipUploadConfigSource": ZipUploadConfigSource,
    "ZipUploadConfigSourceRecord": ZipUploadConfigSourceRecord
}
