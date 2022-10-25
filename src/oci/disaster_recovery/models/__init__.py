# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .associate_dr_protection_group_details import AssociateDrProtectionGroupDetails
from .cancel_dr_plan_execution_details import CancelDrPlanExecutionDetails
from .change_dr_protection_group_compartment_details import ChangeDrProtectionGroupCompartmentDetails
from .compute_instance_vnic_mapping import ComputeInstanceVnicMapping
from .compute_instance_vnic_mapping_details import ComputeInstanceVnicMappingDetails
from .create_dr_plan_details import CreateDrPlanDetails
from .create_dr_plan_execution_details import CreateDrPlanExecutionDetails
from .create_dr_protection_group_details import CreateDrProtectionGroupDetails
from .create_dr_protection_group_member_autonomous_database_details import CreateDrProtectionGroupMemberAutonomousDatabaseDetails
from .create_dr_protection_group_member_compute_instance_details import CreateDrProtectionGroupMemberComputeInstanceDetails
from .create_dr_protection_group_member_database_details import CreateDrProtectionGroupMemberDatabaseDetails
from .create_dr_protection_group_member_details import CreateDrProtectionGroupMemberDetails
from .create_dr_protection_group_member_volume_group_details import CreateDrProtectionGroupMemberVolumeGroupDetails
from .create_object_storage_log_location_details import CreateObjectStorageLogLocationDetails
from .disassociate_dr_protection_group_default_details import DisassociateDrProtectionGroupDefaultDetails
from .disassociate_dr_protection_group_details import DisassociateDrProtectionGroupDetails
from .dr_plan import DrPlan
from .dr_plan_collection import DrPlanCollection
from .dr_plan_execution import DrPlanExecution
from .dr_plan_execution_collection import DrPlanExecutionCollection
from .dr_plan_execution_control_details import DrPlanExecutionControlDetails
from .dr_plan_execution_option_details import DrPlanExecutionOptionDetails
from .dr_plan_execution_options import DrPlanExecutionOptions
from .dr_plan_execution_summary import DrPlanExecutionSummary
from .dr_plan_group import DrPlanGroup
from .dr_plan_group_execution import DrPlanGroupExecution
from .dr_plan_step import DrPlanStep
from .dr_plan_step_execution import DrPlanStepExecution
from .dr_plan_summary import DrPlanSummary
from .dr_plan_user_defined_step import DrPlanUserDefinedStep
from .dr_protection_group import DrProtectionGroup
from .dr_protection_group_collection import DrProtectionGroupCollection
from .dr_protection_group_member import DrProtectionGroupMember
from .dr_protection_group_member_autonomous_database import DrProtectionGroupMemberAutonomousDatabase
from .dr_protection_group_member_compute_instance import DrProtectionGroupMemberComputeInstance
from .dr_protection_group_member_database import DrProtectionGroupMemberDatabase
from .dr_protection_group_member_volume_group import DrProtectionGroupMemberVolumeGroup
from .dr_protection_group_summary import DrProtectionGroupSummary
from .failover_execution_option_details import FailoverExecutionOptionDetails
from .failover_execution_options import FailoverExecutionOptions
from .failover_precheck_execution_option_details import FailoverPrecheckExecutionOptionDetails
from .failover_precheck_execution_options import FailoverPrecheckExecutionOptions
from .ignore_dr_plan_execution_details import IgnoreDrPlanExecutionDetails
from .invoke_function_precheck_step import InvokeFunctionPrecheckStep
from .invoke_function_step import InvokeFunctionStep
from .local_script_precheck_step import LocalScriptPrecheckStep
from .object_storage_log_location import ObjectStorageLogLocation
from .object_storage_script_location import ObjectStorageScriptLocation
from .object_store_script_precheck_step import ObjectStoreScriptPrecheckStep
from .pause_dr_plan_execution_details import PauseDrPlanExecutionDetails
from .resume_dr_plan_execution_details import ResumeDrPlanExecutionDetails
from .retry_dr_plan_execution_details import RetryDrPlanExecutionDetails
from .run_local_script_user_defined_step import RunLocalScriptUserDefinedStep
from .run_object_store_script_user_defined_step import RunObjectStoreScriptUserDefinedStep
from .switchover_execution_option_details import SwitchoverExecutionOptionDetails
from .switchover_execution_options import SwitchoverExecutionOptions
from .switchover_precheck_execution_option_details import SwitchoverPrecheckExecutionOptionDetails
from .switchover_precheck_execution_options import SwitchoverPrecheckExecutionOptions
from .update_dr_plan_details import UpdateDrPlanDetails
from .update_dr_plan_execution_details import UpdateDrPlanExecutionDetails
from .update_dr_plan_group_details import UpdateDrPlanGroupDetails
from .update_dr_plan_step_details import UpdateDrPlanStepDetails
from .update_dr_plan_user_defined_step_details import UpdateDrPlanUserDefinedStepDetails
from .update_dr_protection_group_details import UpdateDrProtectionGroupDetails
from .update_dr_protection_group_member_autonomous_database_details import UpdateDrProtectionGroupMemberAutonomousDatabaseDetails
from .update_dr_protection_group_member_compute_instance_details import UpdateDrProtectionGroupMemberComputeInstanceDetails
from .update_dr_protection_group_member_database_details import UpdateDrProtectionGroupMemberDatabaseDetails
from .update_dr_protection_group_member_details import UpdateDrProtectionGroupMemberDetails
from .update_dr_protection_group_member_volume_group_details import UpdateDrProtectionGroupMemberVolumeGroupDetails
from .update_dr_protection_group_role_details import UpdateDrProtectionGroupRoleDetails
from .update_invoke_function_precheck_step_details import UpdateInvokeFunctionPrecheckStepDetails
from .update_invoke_function_user_defined_step_details import UpdateInvokeFunctionUserDefinedStepDetails
from .update_local_script_precheck_step_details import UpdateLocalScriptPrecheckStepDetails
from .update_object_storage_log_location_details import UpdateObjectStorageLogLocationDetails
from .update_object_storage_script_location_details import UpdateObjectStorageScriptLocationDetails
from .update_object_store_script_precheck_step_details import UpdateObjectStoreScriptPrecheckStepDetails
from .update_run_local_script_user_defined_step_details import UpdateRunLocalScriptUserDefinedStepDetails
from .update_run_object_store_script_user_defined_step_details import UpdateRunObjectStoreScriptUserDefinedStepDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for disaster_recovery services.
disaster_recovery_type_mapping = {
    "AssociateDrProtectionGroupDetails": AssociateDrProtectionGroupDetails,
    "CancelDrPlanExecutionDetails": CancelDrPlanExecutionDetails,
    "ChangeDrProtectionGroupCompartmentDetails": ChangeDrProtectionGroupCompartmentDetails,
    "ComputeInstanceVnicMapping": ComputeInstanceVnicMapping,
    "ComputeInstanceVnicMappingDetails": ComputeInstanceVnicMappingDetails,
    "CreateDrPlanDetails": CreateDrPlanDetails,
    "CreateDrPlanExecutionDetails": CreateDrPlanExecutionDetails,
    "CreateDrProtectionGroupDetails": CreateDrProtectionGroupDetails,
    "CreateDrProtectionGroupMemberAutonomousDatabaseDetails": CreateDrProtectionGroupMemberAutonomousDatabaseDetails,
    "CreateDrProtectionGroupMemberComputeInstanceDetails": CreateDrProtectionGroupMemberComputeInstanceDetails,
    "CreateDrProtectionGroupMemberDatabaseDetails": CreateDrProtectionGroupMemberDatabaseDetails,
    "CreateDrProtectionGroupMemberDetails": CreateDrProtectionGroupMemberDetails,
    "CreateDrProtectionGroupMemberVolumeGroupDetails": CreateDrProtectionGroupMemberVolumeGroupDetails,
    "CreateObjectStorageLogLocationDetails": CreateObjectStorageLogLocationDetails,
    "DisassociateDrProtectionGroupDefaultDetails": DisassociateDrProtectionGroupDefaultDetails,
    "DisassociateDrProtectionGroupDetails": DisassociateDrProtectionGroupDetails,
    "DrPlan": DrPlan,
    "DrPlanCollection": DrPlanCollection,
    "DrPlanExecution": DrPlanExecution,
    "DrPlanExecutionCollection": DrPlanExecutionCollection,
    "DrPlanExecutionControlDetails": DrPlanExecutionControlDetails,
    "DrPlanExecutionOptionDetails": DrPlanExecutionOptionDetails,
    "DrPlanExecutionOptions": DrPlanExecutionOptions,
    "DrPlanExecutionSummary": DrPlanExecutionSummary,
    "DrPlanGroup": DrPlanGroup,
    "DrPlanGroupExecution": DrPlanGroupExecution,
    "DrPlanStep": DrPlanStep,
    "DrPlanStepExecution": DrPlanStepExecution,
    "DrPlanSummary": DrPlanSummary,
    "DrPlanUserDefinedStep": DrPlanUserDefinedStep,
    "DrProtectionGroup": DrProtectionGroup,
    "DrProtectionGroupCollection": DrProtectionGroupCollection,
    "DrProtectionGroupMember": DrProtectionGroupMember,
    "DrProtectionGroupMemberAutonomousDatabase": DrProtectionGroupMemberAutonomousDatabase,
    "DrProtectionGroupMemberComputeInstance": DrProtectionGroupMemberComputeInstance,
    "DrProtectionGroupMemberDatabase": DrProtectionGroupMemberDatabase,
    "DrProtectionGroupMemberVolumeGroup": DrProtectionGroupMemberVolumeGroup,
    "DrProtectionGroupSummary": DrProtectionGroupSummary,
    "FailoverExecutionOptionDetails": FailoverExecutionOptionDetails,
    "FailoverExecutionOptions": FailoverExecutionOptions,
    "FailoverPrecheckExecutionOptionDetails": FailoverPrecheckExecutionOptionDetails,
    "FailoverPrecheckExecutionOptions": FailoverPrecheckExecutionOptions,
    "IgnoreDrPlanExecutionDetails": IgnoreDrPlanExecutionDetails,
    "InvokeFunctionPrecheckStep": InvokeFunctionPrecheckStep,
    "InvokeFunctionStep": InvokeFunctionStep,
    "LocalScriptPrecheckStep": LocalScriptPrecheckStep,
    "ObjectStorageLogLocation": ObjectStorageLogLocation,
    "ObjectStorageScriptLocation": ObjectStorageScriptLocation,
    "ObjectStoreScriptPrecheckStep": ObjectStoreScriptPrecheckStep,
    "PauseDrPlanExecutionDetails": PauseDrPlanExecutionDetails,
    "ResumeDrPlanExecutionDetails": ResumeDrPlanExecutionDetails,
    "RetryDrPlanExecutionDetails": RetryDrPlanExecutionDetails,
    "RunLocalScriptUserDefinedStep": RunLocalScriptUserDefinedStep,
    "RunObjectStoreScriptUserDefinedStep": RunObjectStoreScriptUserDefinedStep,
    "SwitchoverExecutionOptionDetails": SwitchoverExecutionOptionDetails,
    "SwitchoverExecutionOptions": SwitchoverExecutionOptions,
    "SwitchoverPrecheckExecutionOptionDetails": SwitchoverPrecheckExecutionOptionDetails,
    "SwitchoverPrecheckExecutionOptions": SwitchoverPrecheckExecutionOptions,
    "UpdateDrPlanDetails": UpdateDrPlanDetails,
    "UpdateDrPlanExecutionDetails": UpdateDrPlanExecutionDetails,
    "UpdateDrPlanGroupDetails": UpdateDrPlanGroupDetails,
    "UpdateDrPlanStepDetails": UpdateDrPlanStepDetails,
    "UpdateDrPlanUserDefinedStepDetails": UpdateDrPlanUserDefinedStepDetails,
    "UpdateDrProtectionGroupDetails": UpdateDrProtectionGroupDetails,
    "UpdateDrProtectionGroupMemberAutonomousDatabaseDetails": UpdateDrProtectionGroupMemberAutonomousDatabaseDetails,
    "UpdateDrProtectionGroupMemberComputeInstanceDetails": UpdateDrProtectionGroupMemberComputeInstanceDetails,
    "UpdateDrProtectionGroupMemberDatabaseDetails": UpdateDrProtectionGroupMemberDatabaseDetails,
    "UpdateDrProtectionGroupMemberDetails": UpdateDrProtectionGroupMemberDetails,
    "UpdateDrProtectionGroupMemberVolumeGroupDetails": UpdateDrProtectionGroupMemberVolumeGroupDetails,
    "UpdateDrProtectionGroupRoleDetails": UpdateDrProtectionGroupRoleDetails,
    "UpdateInvokeFunctionPrecheckStepDetails": UpdateInvokeFunctionPrecheckStepDetails,
    "UpdateInvokeFunctionUserDefinedStepDetails": UpdateInvokeFunctionUserDefinedStepDetails,
    "UpdateLocalScriptPrecheckStepDetails": UpdateLocalScriptPrecheckStepDetails,
    "UpdateObjectStorageLogLocationDetails": UpdateObjectStorageLogLocationDetails,
    "UpdateObjectStorageScriptLocationDetails": UpdateObjectStorageScriptLocationDetails,
    "UpdateObjectStoreScriptPrecheckStepDetails": UpdateObjectStoreScriptPrecheckStepDetails,
    "UpdateRunLocalScriptUserDefinedStepDetails": UpdateRunLocalScriptUserDefinedStepDetails,
    "UpdateRunObjectStoreScriptUserDefinedStepDetails": UpdateRunObjectStoreScriptUserDefinedStepDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
