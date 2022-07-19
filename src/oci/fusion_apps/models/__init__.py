# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .action import Action
from .admin_user_collection import AdminUserCollection
from .admin_user_summary import AdminUserSummary
from .allow_rule import AllowRule
from .attach_existing_instance_details import AttachExistingInstanceDetails
from .capabilities import Capabilities
from .change_fusion_environment_compartment_details import ChangeFusionEnvironmentCompartmentDetails
from .change_fusion_environment_family_compartment_details import ChangeFusionEnvironmentFamilyCompartmentDetails
from .create_data_masking_activity_details import CreateDataMaskingActivityDetails
from .create_fusion_environment_admin_user_details import CreateFusionEnvironmentAdminUserDetails
from .create_fusion_environment_details import CreateFusionEnvironmentDetails
from .create_fusion_environment_family_details import CreateFusionEnvironmentFamilyDetails
from .create_new_instance_details import CreateNewInstanceDetails
from .create_oax_service_instance_details import CreateOaxServiceInstanceDetails
from .create_oic_service_instance_details import CreateOicServiceInstanceDetails
from .create_refresh_activity_details import CreateRefreshActivityDetails
from .create_service_attachment_details import CreateServiceAttachmentDetails
from .create_service_instance_details import CreateServiceInstanceDetails
from .data_masking_activity import DataMaskingActivity
from .data_masking_activity_collection import DataMaskingActivityCollection
from .data_masking_activity_summary import DataMaskingActivitySummary
from .family_maintenance_policy import FamilyMaintenancePolicy
from .faw_admin_info_details import FawAdminInfoDetails
from .fusion_environment import FusionEnvironment
from .fusion_environment_collection import FusionEnvironmentCollection
from .fusion_environment_family import FusionEnvironmentFamily
from .fusion_environment_family_collection import FusionEnvironmentFamilyCollection
from .fusion_environment_family_limits_and_usage import FusionEnvironmentFamilyLimitsAndUsage
from .fusion_environment_family_summary import FusionEnvironmentFamilySummary
from .fusion_environment_status import FusionEnvironmentStatus
from .fusion_environment_summary import FusionEnvironmentSummary
from .get_maintenance_policy_details import GetMaintenancePolicyDetails
from .kms_key_info import KmsKeyInfo
from .limit_and_usage import LimitAndUsage
from .maintenance_policy import MaintenancePolicy
from .patch_action import PatchAction
from .quarterly_upgrade_begin_times import QuarterlyUpgradeBeginTimes
from .refresh_activity import RefreshActivity
from .refresh_activity_collection import RefreshActivityCollection
from .refresh_activity_summary import RefreshActivitySummary
from .refresh_details import RefreshDetails
from .reset_fusion_environment_password_details import ResetFusionEnvironmentPasswordDetails
from .rule import Rule
from .rule_condition import RuleCondition
from .scheduled_activity import ScheduledActivity
from .scheduled_activity_collection import ScheduledActivityCollection
from .scheduled_activity_summary import ScheduledActivitySummary
from .service_attachment import ServiceAttachment
from .service_attachment_collection import ServiceAttachmentCollection
from .service_attachment_summary import ServiceAttachmentSummary
from .source_ip_address_condition import SourceIpAddressCondition
from .source_vcn_id_condition import SourceVcnIdCondition
from .source_vcn_ip_address_condition import SourceVcnIpAddressCondition
from .subscription import Subscription
from .subscription_detail import SubscriptionDetail
from .subscription_sku import SubscriptionSku
from .time_available_for_refresh import TimeAvailableForRefresh
from .time_available_for_refresh_collection import TimeAvailableForRefreshCollection
from .time_available_for_refresh_summary import TimeAvailableForRefreshSummary
from .update_family_maintenance_policy_details import UpdateFamilyMaintenancePolicyDetails
from .update_fusion_environment_details import UpdateFusionEnvironmentDetails
from .update_fusion_environment_family_details import UpdateFusionEnvironmentFamilyDetails
from .upgrade_action import UpgradeAction
from .vertex_action import VertexAction
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for fusion_apps services.
fusion_apps_type_mapping = {
    "Action": Action,
    "AdminUserCollection": AdminUserCollection,
    "AdminUserSummary": AdminUserSummary,
    "AllowRule": AllowRule,
    "AttachExistingInstanceDetails": AttachExistingInstanceDetails,
    "Capabilities": Capabilities,
    "ChangeFusionEnvironmentCompartmentDetails": ChangeFusionEnvironmentCompartmentDetails,
    "ChangeFusionEnvironmentFamilyCompartmentDetails": ChangeFusionEnvironmentFamilyCompartmentDetails,
    "CreateDataMaskingActivityDetails": CreateDataMaskingActivityDetails,
    "CreateFusionEnvironmentAdminUserDetails": CreateFusionEnvironmentAdminUserDetails,
    "CreateFusionEnvironmentDetails": CreateFusionEnvironmentDetails,
    "CreateFusionEnvironmentFamilyDetails": CreateFusionEnvironmentFamilyDetails,
    "CreateNewInstanceDetails": CreateNewInstanceDetails,
    "CreateOaxServiceInstanceDetails": CreateOaxServiceInstanceDetails,
    "CreateOicServiceInstanceDetails": CreateOicServiceInstanceDetails,
    "CreateRefreshActivityDetails": CreateRefreshActivityDetails,
    "CreateServiceAttachmentDetails": CreateServiceAttachmentDetails,
    "CreateServiceInstanceDetails": CreateServiceInstanceDetails,
    "DataMaskingActivity": DataMaskingActivity,
    "DataMaskingActivityCollection": DataMaskingActivityCollection,
    "DataMaskingActivitySummary": DataMaskingActivitySummary,
    "FamilyMaintenancePolicy": FamilyMaintenancePolicy,
    "FawAdminInfoDetails": FawAdminInfoDetails,
    "FusionEnvironment": FusionEnvironment,
    "FusionEnvironmentCollection": FusionEnvironmentCollection,
    "FusionEnvironmentFamily": FusionEnvironmentFamily,
    "FusionEnvironmentFamilyCollection": FusionEnvironmentFamilyCollection,
    "FusionEnvironmentFamilyLimitsAndUsage": FusionEnvironmentFamilyLimitsAndUsage,
    "FusionEnvironmentFamilySummary": FusionEnvironmentFamilySummary,
    "FusionEnvironmentStatus": FusionEnvironmentStatus,
    "FusionEnvironmentSummary": FusionEnvironmentSummary,
    "GetMaintenancePolicyDetails": GetMaintenancePolicyDetails,
    "KmsKeyInfo": KmsKeyInfo,
    "LimitAndUsage": LimitAndUsage,
    "MaintenancePolicy": MaintenancePolicy,
    "PatchAction": PatchAction,
    "QuarterlyUpgradeBeginTimes": QuarterlyUpgradeBeginTimes,
    "RefreshActivity": RefreshActivity,
    "RefreshActivityCollection": RefreshActivityCollection,
    "RefreshActivitySummary": RefreshActivitySummary,
    "RefreshDetails": RefreshDetails,
    "ResetFusionEnvironmentPasswordDetails": ResetFusionEnvironmentPasswordDetails,
    "Rule": Rule,
    "RuleCondition": RuleCondition,
    "ScheduledActivity": ScheduledActivity,
    "ScheduledActivityCollection": ScheduledActivityCollection,
    "ScheduledActivitySummary": ScheduledActivitySummary,
    "ServiceAttachment": ServiceAttachment,
    "ServiceAttachmentCollection": ServiceAttachmentCollection,
    "ServiceAttachmentSummary": ServiceAttachmentSummary,
    "SourceIpAddressCondition": SourceIpAddressCondition,
    "SourceVcnIdCondition": SourceVcnIdCondition,
    "SourceVcnIpAddressCondition": SourceVcnIpAddressCondition,
    "Subscription": Subscription,
    "SubscriptionDetail": SubscriptionDetail,
    "SubscriptionSku": SubscriptionSku,
    "TimeAvailableForRefresh": TimeAvailableForRefresh,
    "TimeAvailableForRefreshCollection": TimeAvailableForRefreshCollection,
    "TimeAvailableForRefreshSummary": TimeAvailableForRefreshSummary,
    "UpdateFamilyMaintenancePolicyDetails": UpdateFamilyMaintenancePolicyDetails,
    "UpdateFusionEnvironmentDetails": UpdateFusionEnvironmentDetails,
    "UpdateFusionEnvironmentFamilyDetails": UpdateFusionEnvironmentFamilyDetails,
    "UpgradeAction": UpgradeAction,
    "VertexAction": VertexAction,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
