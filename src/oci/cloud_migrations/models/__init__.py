# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .as_is_resource_assessment_strategy import AsIsResourceAssessmentStrategy
from .asset_source import AssetSource
from .asset_source_collection import AssetSourceCollection
from .asset_source_connection import AssetSourceConnection
from .asset_source_connection_collection import AssetSourceConnectionCollection
from .asset_source_credentials import AssetSourceCredentials
from .asset_source_summary import AssetSourceSummary
from .available_shape_summary import AvailableShapeSummary
from .available_shapes_collection import AvailableShapesCollection
from .average_resource_assessment_strategy import AverageResourceAssessmentStrategy
from .change_asset_source_compartment_details import ChangeAssetSourceCompartmentDetails
from .change_discovery_schedule_compartment_details import ChangeDiscoveryScheduleCompartmentDetails
from .change_migration_compartment_details import ChangeMigrationCompartmentDetails
from .change_migration_plan_compartment_details import ChangeMigrationPlanCompartmentDetails
from .change_replication_schedule_compartment_details import ChangeReplicationScheduleCompartmentDetails
from .compatibility_message import CompatibilityMessage
from .compute_cost_estimation import ComputeCostEstimation
from .cost_estimation import CostEstimation
from .create_asset_source_details import CreateAssetSourceDetails
from .create_discovery_schedule_details import CreateDiscoveryScheduleDetails
from .create_migration_asset_details import CreateMigrationAssetDetails
from .create_migration_details import CreateMigrationDetails
from .create_migration_plan_details import CreateMigrationPlanDetails
from .create_replication_schedule_details import CreateReplicationScheduleDetails
from .create_target_asset_details import CreateTargetAssetDetails
from .create_vm_target_asset_details import CreateVmTargetAssetDetails
from .create_vm_ware_asset_source_details import CreateVmWareAssetSourceDetails
from .create_vnic_details import CreateVnicDetails
from .discovery_schedule import DiscoverySchedule
from .discovery_schedule_collection import DiscoveryScheduleCollection
from .discovery_schedule_summary import DiscoveryScheduleSummary
from .hydrated_volume import HydratedVolume
from .instance_agent_plugin_config_details import InstanceAgentPluginConfigDetails
from .instance_options import InstanceOptions
from .instance_source_details import InstanceSourceDetails
from .instance_source_via_boot_volume_details import InstanceSourceViaBootVolumeDetails
from .instance_source_via_image_details import InstanceSourceViaImageDetails
from .launch_instance_agent_config_details import LaunchInstanceAgentConfigDetails
from .launch_instance_details import LaunchInstanceDetails
from .launch_instance_shape_config_details import LaunchInstanceShapeConfigDetails
from .migration import Migration
from .migration_asset import MigrationAsset
from .migration_asset_collection import MigrationAssetCollection
from .migration_asset_summary import MigrationAssetSummary
from .migration_collection import MigrationCollection
from .migration_plan import MigrationPlan
from .migration_plan_collection import MigrationPlanCollection
from .migration_plan_stats import MigrationPlanStats
from .migration_plan_summary import MigrationPlanSummary
from .migration_summary import MigrationSummary
from .os_image_estimation import OsImageEstimation
from .peak_resource_assessment_strategy import PeakResourceAssessmentStrategy
from .percentile_resource_assessment_strategy import PercentileResourceAssessmentStrategy
from .preemptible_instance_config_details import PreemptibleInstanceConfigDetails
from .preemption_action import PreemptionAction
from .replication_progress import ReplicationProgress
from .replication_schedule import ReplicationSchedule
from .replication_schedule_collection import ReplicationScheduleCollection
from .replication_schedule_summary import ReplicationScheduleSummary
from .resource_assessment_strategy import ResourceAssessmentStrategy
from .storage_cost_estimation import StorageCostEstimation
from .target_asset import TargetAsset
from .target_asset_collection import TargetAssetCollection
from .target_asset_summary import TargetAssetSummary
from .target_environment import TargetEnvironment
from .terminate_preemption_action import TerminatePreemptionAction
from .update_asset_source_details import UpdateAssetSourceDetails
from .update_discovery_schedule_details import UpdateDiscoveryScheduleDetails
from .update_migration_asset_details import UpdateMigrationAssetDetails
from .update_migration_details import UpdateMigrationDetails
from .update_migration_plan_details import UpdateMigrationPlanDetails
from .update_replication_schedule_details import UpdateReplicationScheduleDetails
from .update_target_asset_details import UpdateTargetAssetDetails
from .update_vm_target_asset_details import UpdateVmTargetAssetDetails
from .update_vm_ware_asset_source_details import UpdateVmWareAssetSourceDetails
from .vm_target_asset import VmTargetAsset
from .vm_target_asset_summary import VmTargetAssetSummary
from .vm_target_environment import VmTargetEnvironment
from .vm_ware_asset_source import VmWareAssetSource
from .vm_ware_asset_source_summary import VmWareAssetSourceSummary
from .volume_cost_estimation import VolumeCostEstimation
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for cloud_migrations services.
cloud_migrations_type_mapping = {
    "AsIsResourceAssessmentStrategy": AsIsResourceAssessmentStrategy,
    "AssetSource": AssetSource,
    "AssetSourceCollection": AssetSourceCollection,
    "AssetSourceConnection": AssetSourceConnection,
    "AssetSourceConnectionCollection": AssetSourceConnectionCollection,
    "AssetSourceCredentials": AssetSourceCredentials,
    "AssetSourceSummary": AssetSourceSummary,
    "AvailableShapeSummary": AvailableShapeSummary,
    "AvailableShapesCollection": AvailableShapesCollection,
    "AverageResourceAssessmentStrategy": AverageResourceAssessmentStrategy,
    "ChangeAssetSourceCompartmentDetails": ChangeAssetSourceCompartmentDetails,
    "ChangeDiscoveryScheduleCompartmentDetails": ChangeDiscoveryScheduleCompartmentDetails,
    "ChangeMigrationCompartmentDetails": ChangeMigrationCompartmentDetails,
    "ChangeMigrationPlanCompartmentDetails": ChangeMigrationPlanCompartmentDetails,
    "ChangeReplicationScheduleCompartmentDetails": ChangeReplicationScheduleCompartmentDetails,
    "CompatibilityMessage": CompatibilityMessage,
    "ComputeCostEstimation": ComputeCostEstimation,
    "CostEstimation": CostEstimation,
    "CreateAssetSourceDetails": CreateAssetSourceDetails,
    "CreateDiscoveryScheduleDetails": CreateDiscoveryScheduleDetails,
    "CreateMigrationAssetDetails": CreateMigrationAssetDetails,
    "CreateMigrationDetails": CreateMigrationDetails,
    "CreateMigrationPlanDetails": CreateMigrationPlanDetails,
    "CreateReplicationScheduleDetails": CreateReplicationScheduleDetails,
    "CreateTargetAssetDetails": CreateTargetAssetDetails,
    "CreateVmTargetAssetDetails": CreateVmTargetAssetDetails,
    "CreateVmWareAssetSourceDetails": CreateVmWareAssetSourceDetails,
    "CreateVnicDetails": CreateVnicDetails,
    "DiscoverySchedule": DiscoverySchedule,
    "DiscoveryScheduleCollection": DiscoveryScheduleCollection,
    "DiscoveryScheduleSummary": DiscoveryScheduleSummary,
    "HydratedVolume": HydratedVolume,
    "InstanceAgentPluginConfigDetails": InstanceAgentPluginConfigDetails,
    "InstanceOptions": InstanceOptions,
    "InstanceSourceDetails": InstanceSourceDetails,
    "InstanceSourceViaBootVolumeDetails": InstanceSourceViaBootVolumeDetails,
    "InstanceSourceViaImageDetails": InstanceSourceViaImageDetails,
    "LaunchInstanceAgentConfigDetails": LaunchInstanceAgentConfigDetails,
    "LaunchInstanceDetails": LaunchInstanceDetails,
    "LaunchInstanceShapeConfigDetails": LaunchInstanceShapeConfigDetails,
    "Migration": Migration,
    "MigrationAsset": MigrationAsset,
    "MigrationAssetCollection": MigrationAssetCollection,
    "MigrationAssetSummary": MigrationAssetSummary,
    "MigrationCollection": MigrationCollection,
    "MigrationPlan": MigrationPlan,
    "MigrationPlanCollection": MigrationPlanCollection,
    "MigrationPlanStats": MigrationPlanStats,
    "MigrationPlanSummary": MigrationPlanSummary,
    "MigrationSummary": MigrationSummary,
    "OsImageEstimation": OsImageEstimation,
    "PeakResourceAssessmentStrategy": PeakResourceAssessmentStrategy,
    "PercentileResourceAssessmentStrategy": PercentileResourceAssessmentStrategy,
    "PreemptibleInstanceConfigDetails": PreemptibleInstanceConfigDetails,
    "PreemptionAction": PreemptionAction,
    "ReplicationProgress": ReplicationProgress,
    "ReplicationSchedule": ReplicationSchedule,
    "ReplicationScheduleCollection": ReplicationScheduleCollection,
    "ReplicationScheduleSummary": ReplicationScheduleSummary,
    "ResourceAssessmentStrategy": ResourceAssessmentStrategy,
    "StorageCostEstimation": StorageCostEstimation,
    "TargetAsset": TargetAsset,
    "TargetAssetCollection": TargetAssetCollection,
    "TargetAssetSummary": TargetAssetSummary,
    "TargetEnvironment": TargetEnvironment,
    "TerminatePreemptionAction": TerminatePreemptionAction,
    "UpdateAssetSourceDetails": UpdateAssetSourceDetails,
    "UpdateDiscoveryScheduleDetails": UpdateDiscoveryScheduleDetails,
    "UpdateMigrationAssetDetails": UpdateMigrationAssetDetails,
    "UpdateMigrationDetails": UpdateMigrationDetails,
    "UpdateMigrationPlanDetails": UpdateMigrationPlanDetails,
    "UpdateReplicationScheduleDetails": UpdateReplicationScheduleDetails,
    "UpdateTargetAssetDetails": UpdateTargetAssetDetails,
    "UpdateVmTargetAssetDetails": UpdateVmTargetAssetDetails,
    "UpdateVmWareAssetSourceDetails": UpdateVmWareAssetSourceDetails,
    "VmTargetAsset": VmTargetAsset,
    "VmTargetAssetSummary": VmTargetAssetSummary,
    "VmTargetEnvironment": VmTargetEnvironment,
    "VmWareAssetSource": VmWareAssetSource,
    "VmWareAssetSourceSummary": VmWareAssetSourceSummary,
    "VolumeCostEstimation": VolumeCostEstimation,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
