# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .apply_job_operation_details import ApplyJobOperationDetails
from .apply_job_operation_details_summary import ApplyJobOperationDetailsSummary
from .apply_job_plan_resolution import ApplyJobPlanResolution
from .apply_rollback_job_operation_details import ApplyRollbackJobOperationDetails
from .apply_rollback_job_operation_details_summary import ApplyRollbackJobOperationDetailsSummary
from .associated_resource_summary import AssociatedResourceSummary
from .associated_resources_collection import AssociatedResourcesCollection
from .bitbucket_cloud_config_source import BitbucketCloudConfigSource
from .bitbucket_cloud_config_source_record import BitbucketCloudConfigSourceRecord
from .bitbucket_cloud_username_app_password_configuration_source_provider import BitbucketCloudUsernameAppPasswordConfigurationSourceProvider
from .bitbucket_cloud_username_app_password_configuration_source_provider_summary import BitbucketCloudUsernameAppPasswordConfigurationSourceProviderSummary
from .bitbucket_server_access_token_configuration_source_provider import BitbucketServerAccessTokenConfigurationSourceProvider
from .bitbucket_server_access_token_configuration_source_provider_summary import BitbucketServerAccessTokenConfigurationSourceProviderSummary
from .bitbucket_server_config_source import BitbucketServerConfigSource
from .bitbucket_server_config_source_record import BitbucketServerConfigSourceRecord
from .cancellation_details import CancellationDetails
from .change_configuration_source_provider_compartment_details import ChangeConfigurationSourceProviderCompartmentDetails
from .change_private_endpoint_compartment_details import ChangePrivateEndpointCompartmentDetails
from .change_stack_compartment_details import ChangeStackCompartmentDetails
from .change_template_compartment_details import ChangeTemplateCompartmentDetails
from .compartment_config_source import CompartmentConfigSource
from .config_source import ConfigSource
from .config_source_record import ConfigSourceRecord
from .configuration_source_provider import ConfigurationSourceProvider
from .configuration_source_provider_collection import ConfigurationSourceProviderCollection
from .configuration_source_provider_summary import ConfigurationSourceProviderSummary
from .create_apply_job_operation_details import CreateApplyJobOperationDetails
from .create_apply_rollback_job_operation_details import CreateApplyRollbackJobOperationDetails
from .create_bitbucket_cloud_config_source_details import CreateBitbucketCloudConfigSourceDetails
from .create_bitbucket_cloud_username_app_password_configuration_source_provider_details import CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails
from .create_bitbucket_server_access_token_configuration_source_provider_details import CreateBitbucketServerAccessTokenConfigurationSourceProviderDetails
from .create_bitbucket_server_config_source_details import CreateBitbucketServerConfigSourceDetails
from .create_compartment_config_source_details import CreateCompartmentConfigSourceDetails
from .create_config_source_details import CreateConfigSourceDetails
from .create_configuration_source_provider_details import CreateConfigurationSourceProviderDetails
from .create_destroy_job_operation_details import CreateDestroyJobOperationDetails
from .create_dev_ops_config_source_details import CreateDevOpsConfigSourceDetails
from .create_git_config_source_details import CreateGitConfigSourceDetails
from .create_github_access_token_configuration_source_provider_details import CreateGithubAccessTokenConfigurationSourceProviderDetails
from .create_gitlab_access_token_configuration_source_provider_details import CreateGitlabAccessTokenConfigurationSourceProviderDetails
from .create_import_tf_state_job_operation_details import CreateImportTfStateJobOperationDetails
from .create_job_details import CreateJobDetails
from .create_job_operation_details import CreateJobOperationDetails
from .create_object_storage_config_source_details import CreateObjectStorageConfigSourceDetails
from .create_plan_job_operation_details import CreatePlanJobOperationDetails
from .create_plan_rollback_job_operation_details import CreatePlanRollbackJobOperationDetails
from .create_private_endpoint_details import CreatePrivateEndpointDetails
from .create_stack_details import CreateStackDetails
from .create_stack_template_config_source_details import CreateStackTemplateConfigSourceDetails
from .create_template_config_source_details import CreateTemplateConfigSourceDetails
from .create_template_details import CreateTemplateDetails
from .create_template_zip_upload_config_source_details import CreateTemplateZipUploadConfigSourceDetails
from .create_zip_upload_config_source_details import CreateZipUploadConfigSourceDetails
from .custom_terraform_provider import CustomTerraformProvider
from .destroy_job_operation_details import DestroyJobOperationDetails
from .destroy_job_operation_details_summary import DestroyJobOperationDetailsSummary
from .detect_stack_drift_details import DetectStackDriftDetails
from .dev_ops_config_source import DevOpsConfigSource
from .dev_ops_config_source_record import DevOpsConfigSourceRecord
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
from .job_output_summary import JobOutputSummary
from .job_outputs_collection import JobOutputsCollection
from .job_summary import JobSummary
from .log_entry import LogEntry
from .object_storage_config_source import ObjectStorageConfigSource
from .object_storage_config_source_record import ObjectStorageConfigSourceRecord
from .plan_job_operation_details import PlanJobOperationDetails
from .plan_job_operation_details_summary import PlanJobOperationDetailsSummary
from .plan_rollback_job_operation_details import PlanRollbackJobOperationDetails
from .plan_rollback_job_operation_details_summary import PlanRollbackJobOperationDetailsSummary
from .private_endpoint import PrivateEndpoint
from .private_endpoint_collection import PrivateEndpointCollection
from .private_endpoint_summary import PrivateEndpointSummary
from .private_server_config_details import PrivateServerConfigDetails
from .reachable_ip import ReachableIp
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
from .update_bitbucket_cloud_config_source_details import UpdateBitbucketCloudConfigSourceDetails
from .update_bitbucket_cloud_username_app_password_configuration_source_provider_details import UpdateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails
from .update_bitbucket_server_access_token_configuration_source_provider_details import UpdateBitbucketServerAccessTokenConfigurationSourceProviderDetails
from .update_bitbucket_server_config_source_details import UpdateBitbucketServerConfigSourceDetails
from .update_config_source_details import UpdateConfigSourceDetails
from .update_configuration_source_provider_details import UpdateConfigurationSourceProviderDetails
from .update_dev_ops_config_source_details import UpdateDevOpsConfigSourceDetails
from .update_git_config_source_details import UpdateGitConfigSourceDetails
from .update_github_access_token_configuration_source_provider_details import UpdateGithubAccessTokenConfigurationSourceProviderDetails
from .update_gitlab_access_token_configuration_source_provider_details import UpdateGitlabAccessTokenConfigurationSourceProviderDetails
from .update_job_details import UpdateJobDetails
from .update_object_storage_config_source_details import UpdateObjectStorageConfigSourceDetails
from .update_private_endpoint_details import UpdatePrivateEndpointDetails
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
    "ApplyRollbackJobOperationDetails": ApplyRollbackJobOperationDetails,
    "ApplyRollbackJobOperationDetailsSummary": ApplyRollbackJobOperationDetailsSummary,
    "AssociatedResourceSummary": AssociatedResourceSummary,
    "AssociatedResourcesCollection": AssociatedResourcesCollection,
    "BitbucketCloudConfigSource": BitbucketCloudConfigSource,
    "BitbucketCloudConfigSourceRecord": BitbucketCloudConfigSourceRecord,
    "BitbucketCloudUsernameAppPasswordConfigurationSourceProvider": BitbucketCloudUsernameAppPasswordConfigurationSourceProvider,
    "BitbucketCloudUsernameAppPasswordConfigurationSourceProviderSummary": BitbucketCloudUsernameAppPasswordConfigurationSourceProviderSummary,
    "BitbucketServerAccessTokenConfigurationSourceProvider": BitbucketServerAccessTokenConfigurationSourceProvider,
    "BitbucketServerAccessTokenConfigurationSourceProviderSummary": BitbucketServerAccessTokenConfigurationSourceProviderSummary,
    "BitbucketServerConfigSource": BitbucketServerConfigSource,
    "BitbucketServerConfigSourceRecord": BitbucketServerConfigSourceRecord,
    "CancellationDetails": CancellationDetails,
    "ChangeConfigurationSourceProviderCompartmentDetails": ChangeConfigurationSourceProviderCompartmentDetails,
    "ChangePrivateEndpointCompartmentDetails": ChangePrivateEndpointCompartmentDetails,
    "ChangeStackCompartmentDetails": ChangeStackCompartmentDetails,
    "ChangeTemplateCompartmentDetails": ChangeTemplateCompartmentDetails,
    "CompartmentConfigSource": CompartmentConfigSource,
    "ConfigSource": ConfigSource,
    "ConfigSourceRecord": ConfigSourceRecord,
    "ConfigurationSourceProvider": ConfigurationSourceProvider,
    "ConfigurationSourceProviderCollection": ConfigurationSourceProviderCollection,
    "ConfigurationSourceProviderSummary": ConfigurationSourceProviderSummary,
    "CreateApplyJobOperationDetails": CreateApplyJobOperationDetails,
    "CreateApplyRollbackJobOperationDetails": CreateApplyRollbackJobOperationDetails,
    "CreateBitbucketCloudConfigSourceDetails": CreateBitbucketCloudConfigSourceDetails,
    "CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails": CreateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails,
    "CreateBitbucketServerAccessTokenConfigurationSourceProviderDetails": CreateBitbucketServerAccessTokenConfigurationSourceProviderDetails,
    "CreateBitbucketServerConfigSourceDetails": CreateBitbucketServerConfigSourceDetails,
    "CreateCompartmentConfigSourceDetails": CreateCompartmentConfigSourceDetails,
    "CreateConfigSourceDetails": CreateConfigSourceDetails,
    "CreateConfigurationSourceProviderDetails": CreateConfigurationSourceProviderDetails,
    "CreateDestroyJobOperationDetails": CreateDestroyJobOperationDetails,
    "CreateDevOpsConfigSourceDetails": CreateDevOpsConfigSourceDetails,
    "CreateGitConfigSourceDetails": CreateGitConfigSourceDetails,
    "CreateGithubAccessTokenConfigurationSourceProviderDetails": CreateGithubAccessTokenConfigurationSourceProviderDetails,
    "CreateGitlabAccessTokenConfigurationSourceProviderDetails": CreateGitlabAccessTokenConfigurationSourceProviderDetails,
    "CreateImportTfStateJobOperationDetails": CreateImportTfStateJobOperationDetails,
    "CreateJobDetails": CreateJobDetails,
    "CreateJobOperationDetails": CreateJobOperationDetails,
    "CreateObjectStorageConfigSourceDetails": CreateObjectStorageConfigSourceDetails,
    "CreatePlanJobOperationDetails": CreatePlanJobOperationDetails,
    "CreatePlanRollbackJobOperationDetails": CreatePlanRollbackJobOperationDetails,
    "CreatePrivateEndpointDetails": CreatePrivateEndpointDetails,
    "CreateStackDetails": CreateStackDetails,
    "CreateStackTemplateConfigSourceDetails": CreateStackTemplateConfigSourceDetails,
    "CreateTemplateConfigSourceDetails": CreateTemplateConfigSourceDetails,
    "CreateTemplateDetails": CreateTemplateDetails,
    "CreateTemplateZipUploadConfigSourceDetails": CreateTemplateZipUploadConfigSourceDetails,
    "CreateZipUploadConfigSourceDetails": CreateZipUploadConfigSourceDetails,
    "CustomTerraformProvider": CustomTerraformProvider,
    "DestroyJobOperationDetails": DestroyJobOperationDetails,
    "DestroyJobOperationDetailsSummary": DestroyJobOperationDetailsSummary,
    "DetectStackDriftDetails": DetectStackDriftDetails,
    "DevOpsConfigSource": DevOpsConfigSource,
    "DevOpsConfigSourceRecord": DevOpsConfigSourceRecord,
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
    "JobOutputSummary": JobOutputSummary,
    "JobOutputsCollection": JobOutputsCollection,
    "JobSummary": JobSummary,
    "LogEntry": LogEntry,
    "ObjectStorageConfigSource": ObjectStorageConfigSource,
    "ObjectStorageConfigSourceRecord": ObjectStorageConfigSourceRecord,
    "PlanJobOperationDetails": PlanJobOperationDetails,
    "PlanJobOperationDetailsSummary": PlanJobOperationDetailsSummary,
    "PlanRollbackJobOperationDetails": PlanRollbackJobOperationDetails,
    "PlanRollbackJobOperationDetailsSummary": PlanRollbackJobOperationDetailsSummary,
    "PrivateEndpoint": PrivateEndpoint,
    "PrivateEndpointCollection": PrivateEndpointCollection,
    "PrivateEndpointSummary": PrivateEndpointSummary,
    "PrivateServerConfigDetails": PrivateServerConfigDetails,
    "ReachableIp": ReachableIp,
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
    "UpdateBitbucketCloudConfigSourceDetails": UpdateBitbucketCloudConfigSourceDetails,
    "UpdateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails": UpdateBitbucketCloudUsernameAppPasswordConfigurationSourceProviderDetails,
    "UpdateBitbucketServerAccessTokenConfigurationSourceProviderDetails": UpdateBitbucketServerAccessTokenConfigurationSourceProviderDetails,
    "UpdateBitbucketServerConfigSourceDetails": UpdateBitbucketServerConfigSourceDetails,
    "UpdateConfigSourceDetails": UpdateConfigSourceDetails,
    "UpdateConfigurationSourceProviderDetails": UpdateConfigurationSourceProviderDetails,
    "UpdateDevOpsConfigSourceDetails": UpdateDevOpsConfigSourceDetails,
    "UpdateGitConfigSourceDetails": UpdateGitConfigSourceDetails,
    "UpdateGithubAccessTokenConfigurationSourceProviderDetails": UpdateGithubAccessTokenConfigurationSourceProviderDetails,
    "UpdateGitlabAccessTokenConfigurationSourceProviderDetails": UpdateGitlabAccessTokenConfigurationSourceProviderDetails,
    "UpdateJobDetails": UpdateJobDetails,
    "UpdateObjectStorageConfigSourceDetails": UpdateObjectStorageConfigSourceDetails,
    "UpdatePrivateEndpointDetails": UpdatePrivateEndpointDetails,
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
