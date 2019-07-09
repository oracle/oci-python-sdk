# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .apply_job_plan_resolution import ApplyJobPlanResolution
from .change_stack_compartment_details import ChangeStackCompartmentDetails
from .config_source import ConfigSource
from .create_config_source_details import CreateConfigSourceDetails
from .create_job_details import CreateJobDetails
from .create_stack_details import CreateStackDetails
from .create_zip_upload_config_source_details import CreateZipUploadConfigSourceDetails
from .failure_details import FailureDetails
from .job import Job
from .job_summary import JobSummary
from .log_entry import LogEntry
from .stack import Stack
from .stack_summary import StackSummary
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
    "ApplyJobPlanResolution": ApplyJobPlanResolution,
    "ChangeStackCompartmentDetails": ChangeStackCompartmentDetails,
    "ConfigSource": ConfigSource,
    "CreateConfigSourceDetails": CreateConfigSourceDetails,
    "CreateJobDetails": CreateJobDetails,
    "CreateStackDetails": CreateStackDetails,
    "CreateZipUploadConfigSourceDetails": CreateZipUploadConfigSourceDetails,
    "FailureDetails": FailureDetails,
    "Job": Job,
    "JobSummary": JobSummary,
    "LogEntry": LogEntry,
    "Stack": Stack,
    "StackSummary": StackSummary,
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
