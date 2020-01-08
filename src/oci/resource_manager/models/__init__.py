# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .apply_job_operation_details import ApplyJobOperationDetails
from .apply_job_operation_details_summary import ApplyJobOperationDetailsSummary
from .apply_job_plan_resolution import ApplyJobPlanResolution
from .change_stack_compartment_details import ChangeStackCompartmentDetails
from .config_source import ConfigSource
from .create_apply_job_operation_details import CreateApplyJobOperationDetails
from .create_config_source_details import CreateConfigSourceDetails
from .create_destroy_job_operation_details import CreateDestroyJobOperationDetails
from .create_import_tf_state_job_operation_details import CreateImportTfStateJobOperationDetails
from .create_job_details import CreateJobDetails
from .create_job_operation_details import CreateJobOperationDetails
from .create_plan_job_operation_details import CreatePlanJobOperationDetails
from .create_stack_details import CreateStackDetails
from .create_zip_upload_config_source_details import CreateZipUploadConfigSourceDetails
from .destroy_job_operation_details import DestroyJobOperationDetails
from .destroy_job_operation_details_summary import DestroyJobOperationDetailsSummary
from .failure_details import FailureDetails
from .import_tf_state_job_operation_details import ImportTfStateJobOperationDetails
from .import_tf_state_job_operation_details_summary import ImportTfStateJobOperationDetailsSummary
from .job import Job
from .job_operation_details import JobOperationDetails
from .job_operation_details_summary import JobOperationDetailsSummary
from .job_summary import JobSummary
from .log_entry import LogEntry
from .plan_job_operation_details import PlanJobOperationDetails
from .plan_job_operation_details_summary import PlanJobOperationDetailsSummary
from .stack import Stack
from .stack_summary import StackSummary
from .terraform_version_collection import TerraformVersionCollection
from .terraform_version_summary import TerraformVersionSummary
from .update_config_source_details import UpdateConfigSourceDetails
from .update_job_details import UpdateJobDetails
from .update_stack_details import UpdateStackDetails
from .update_zip_upload_config_source_details import UpdateZipUploadConfigSourceDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .zip_upload_config_source import ZipUploadConfigSource

# Maps type names to classes for resource_manager services.
resource_manager_type_mapping = {
    "ApplyJobOperationDetails": ApplyJobOperationDetails,
    "ApplyJobOperationDetailsSummary": ApplyJobOperationDetailsSummary,
    "ApplyJobPlanResolution": ApplyJobPlanResolution,
    "ChangeStackCompartmentDetails": ChangeStackCompartmentDetails,
    "ConfigSource": ConfigSource,
    "CreateApplyJobOperationDetails": CreateApplyJobOperationDetails,
    "CreateConfigSourceDetails": CreateConfigSourceDetails,
    "CreateDestroyJobOperationDetails": CreateDestroyJobOperationDetails,
    "CreateImportTfStateJobOperationDetails": CreateImportTfStateJobOperationDetails,
    "CreateJobDetails": CreateJobDetails,
    "CreateJobOperationDetails": CreateJobOperationDetails,
    "CreatePlanJobOperationDetails": CreatePlanJobOperationDetails,
    "CreateStackDetails": CreateStackDetails,
    "CreateZipUploadConfigSourceDetails": CreateZipUploadConfigSourceDetails,
    "DestroyJobOperationDetails": DestroyJobOperationDetails,
    "DestroyJobOperationDetailsSummary": DestroyJobOperationDetailsSummary,
    "FailureDetails": FailureDetails,
    "ImportTfStateJobOperationDetails": ImportTfStateJobOperationDetails,
    "ImportTfStateJobOperationDetailsSummary": ImportTfStateJobOperationDetailsSummary,
    "Job": Job,
    "JobOperationDetails": JobOperationDetails,
    "JobOperationDetailsSummary": JobOperationDetailsSummary,
    "JobSummary": JobSummary,
    "LogEntry": LogEntry,
    "PlanJobOperationDetails": PlanJobOperationDetails,
    "PlanJobOperationDetailsSummary": PlanJobOperationDetailsSummary,
    "Stack": Stack,
    "StackSummary": StackSummary,
    "TerraformVersionCollection": TerraformVersionCollection,
    "TerraformVersionSummary": TerraformVersionSummary,
    "UpdateConfigSourceDetails": UpdateConfigSourceDetails,
    "UpdateJobDetails": UpdateJobDetails,
    "UpdateStackDetails": UpdateStackDetails,
    "UpdateZipUploadConfigSourceDetails": UpdateZipUploadConfigSourceDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "ZipUploadConfigSource": ZipUploadConfigSource
}
