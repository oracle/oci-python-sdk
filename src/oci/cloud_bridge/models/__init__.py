# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_agent_dependency_details import AddAgentDependencyDetails
from .agent import Agent
from .agent_collection import AgentCollection
from .agent_dependency import AgentDependency
from .agent_dependency_collection import AgentDependencyCollection
from .agent_dependency_summary import AgentDependencySummary
from .agent_summary import AgentSummary
from .appliance_image_collection import ApplianceImageCollection
from .appliance_image_summary import ApplianceImageSummary
from .asset import Asset
from .asset_aggregation import AssetAggregation
from .asset_aggregation_collection import AssetAggregationCollection
from .asset_collection import AssetCollection
from .asset_source import AssetSource
from .asset_source_collection import AssetSourceCollection
from .asset_source_connection import AssetSourceConnection
from .asset_source_connection_collection import AssetSourceConnectionCollection
from .asset_source_credentials import AssetSourceCredentials
from .asset_source_summary import AssetSourceSummary
from .asset_summary import AssetSummary
from .change_agent_compartment_details import ChangeAgentCompartmentDetails
from .change_agent_dependency_compartment_details import ChangeAgentDependencyCompartmentDetails
from .change_asset_compartment_details import ChangeAssetCompartmentDetails
from .change_asset_source_compartment_details import ChangeAssetSourceCompartmentDetails
from .change_asset_tags_details import ChangeAssetTagsDetails
from .change_discovery_schedule_compartment_details import ChangeDiscoveryScheduleCompartmentDetails
from .change_environment_compartment_details import ChangeEnvironmentCompartmentDetails
from .compute_properties import ComputeProperties
from .create_agent_dependency_details import CreateAgentDependencyDetails
from .create_agent_details import CreateAgentDetails
from .create_asset_details import CreateAssetDetails
from .create_asset_source_details import CreateAssetSourceDetails
from .create_discovery_schedule_details import CreateDiscoveryScheduleDetails
from .create_environment_details import CreateEnvironmentDetails
from .create_inventory_details import CreateInventoryDetails
from .create_vm_ware_asset_source_details import CreateVmWareAssetSourceDetails
from .create_vmware_vm_asset_details import CreateVmwareVmAssetDetails
from .customer_tag import CustomerTag
from .discovery_schedule import DiscoverySchedule
from .discovery_schedule_collection import DiscoveryScheduleCollection
from .discovery_schedule_summary import DiscoveryScheduleSummary
from .disk import Disk
from .environment import Environment
from .environment_collection import EnvironmentCollection
from .environment_summary import EnvironmentSummary
from .gpu_device import GpuDevice
from .historical_metric import HistoricalMetric
from .historical_metric_collection import HistoricalMetricCollection
from .historical_metric_summary import HistoricalMetricSummary
from .import_inventory_details import ImportInventoryDetails
from .import_inventory_via_assets_details import ImportInventoryViaAssetsDetails
from .inventory import Inventory
from .inventory_collection import InventoryCollection
from .inventory_summary import InventorySummary
from .nic import Nic
from .nvdimm import Nvdimm
from .nvdimm_controller import NvdimmController
from .plugin import Plugin
from .plugin_summary import PluginSummary
from .remove_agent_dependency_details import RemoveAgentDependencyDetails
from .scsi_controller import ScsiController
from .submit_historical_metrics_details import SubmitHistoricalMetricsDetails
from .update_agent_dependency_details import UpdateAgentDependencyDetails
from .update_agent_details import UpdateAgentDetails
from .update_asset_details import UpdateAssetDetails
from .update_asset_source_details import UpdateAssetSourceDetails
from .update_discovery_schedule_details import UpdateDiscoveryScheduleDetails
from .update_environment_details import UpdateEnvironmentDetails
from .update_inventory_details import UpdateInventoryDetails
from .update_plugin_details import UpdatePluginDetails
from .update_vm_asset_details import UpdateVmAssetDetails
from .update_vm_ware_asset_source_details import UpdateVmWareAssetSourceDetails
from .update_vmware_vm_asset_details import UpdateVmwareVmAssetDetails
from .vm_asset import VmAsset
from .vm_properties import VmProperties
from .vm_ware_asset_source import VmWareAssetSource
from .vm_ware_asset_source_summary import VmWareAssetSourceSummary
from .vmware_v_center_properties import VmwareVCenterProperties
from .vmware_vm_asset import VmwareVmAsset
from .vmware_vm_properties import VmwareVmProperties
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for cloud_bridge services.
cloud_bridge_type_mapping = {
    "AddAgentDependencyDetails": AddAgentDependencyDetails,
    "Agent": Agent,
    "AgentCollection": AgentCollection,
    "AgentDependency": AgentDependency,
    "AgentDependencyCollection": AgentDependencyCollection,
    "AgentDependencySummary": AgentDependencySummary,
    "AgentSummary": AgentSummary,
    "ApplianceImageCollection": ApplianceImageCollection,
    "ApplianceImageSummary": ApplianceImageSummary,
    "Asset": Asset,
    "AssetAggregation": AssetAggregation,
    "AssetAggregationCollection": AssetAggregationCollection,
    "AssetCollection": AssetCollection,
    "AssetSource": AssetSource,
    "AssetSourceCollection": AssetSourceCollection,
    "AssetSourceConnection": AssetSourceConnection,
    "AssetSourceConnectionCollection": AssetSourceConnectionCollection,
    "AssetSourceCredentials": AssetSourceCredentials,
    "AssetSourceSummary": AssetSourceSummary,
    "AssetSummary": AssetSummary,
    "ChangeAgentCompartmentDetails": ChangeAgentCompartmentDetails,
    "ChangeAgentDependencyCompartmentDetails": ChangeAgentDependencyCompartmentDetails,
    "ChangeAssetCompartmentDetails": ChangeAssetCompartmentDetails,
    "ChangeAssetSourceCompartmentDetails": ChangeAssetSourceCompartmentDetails,
    "ChangeAssetTagsDetails": ChangeAssetTagsDetails,
    "ChangeDiscoveryScheduleCompartmentDetails": ChangeDiscoveryScheduleCompartmentDetails,
    "ChangeEnvironmentCompartmentDetails": ChangeEnvironmentCompartmentDetails,
    "ComputeProperties": ComputeProperties,
    "CreateAgentDependencyDetails": CreateAgentDependencyDetails,
    "CreateAgentDetails": CreateAgentDetails,
    "CreateAssetDetails": CreateAssetDetails,
    "CreateAssetSourceDetails": CreateAssetSourceDetails,
    "CreateDiscoveryScheduleDetails": CreateDiscoveryScheduleDetails,
    "CreateEnvironmentDetails": CreateEnvironmentDetails,
    "CreateInventoryDetails": CreateInventoryDetails,
    "CreateVmWareAssetSourceDetails": CreateVmWareAssetSourceDetails,
    "CreateVmwareVmAssetDetails": CreateVmwareVmAssetDetails,
    "CustomerTag": CustomerTag,
    "DiscoverySchedule": DiscoverySchedule,
    "DiscoveryScheduleCollection": DiscoveryScheduleCollection,
    "DiscoveryScheduleSummary": DiscoveryScheduleSummary,
    "Disk": Disk,
    "Environment": Environment,
    "EnvironmentCollection": EnvironmentCollection,
    "EnvironmentSummary": EnvironmentSummary,
    "GpuDevice": GpuDevice,
    "HistoricalMetric": HistoricalMetric,
    "HistoricalMetricCollection": HistoricalMetricCollection,
    "HistoricalMetricSummary": HistoricalMetricSummary,
    "ImportInventoryDetails": ImportInventoryDetails,
    "ImportInventoryViaAssetsDetails": ImportInventoryViaAssetsDetails,
    "Inventory": Inventory,
    "InventoryCollection": InventoryCollection,
    "InventorySummary": InventorySummary,
    "Nic": Nic,
    "Nvdimm": Nvdimm,
    "NvdimmController": NvdimmController,
    "Plugin": Plugin,
    "PluginSummary": PluginSummary,
    "RemoveAgentDependencyDetails": RemoveAgentDependencyDetails,
    "ScsiController": ScsiController,
    "SubmitHistoricalMetricsDetails": SubmitHistoricalMetricsDetails,
    "UpdateAgentDependencyDetails": UpdateAgentDependencyDetails,
    "UpdateAgentDetails": UpdateAgentDetails,
    "UpdateAssetDetails": UpdateAssetDetails,
    "UpdateAssetSourceDetails": UpdateAssetSourceDetails,
    "UpdateDiscoveryScheduleDetails": UpdateDiscoveryScheduleDetails,
    "UpdateEnvironmentDetails": UpdateEnvironmentDetails,
    "UpdateInventoryDetails": UpdateInventoryDetails,
    "UpdatePluginDetails": UpdatePluginDetails,
    "UpdateVmAssetDetails": UpdateVmAssetDetails,
    "UpdateVmWareAssetSourceDetails": UpdateVmWareAssetSourceDetails,
    "UpdateVmwareVmAssetDetails": UpdateVmwareVmAssetDetails,
    "VmAsset": VmAsset,
    "VmProperties": VmProperties,
    "VmWareAssetSource": VmWareAssetSource,
    "VmWareAssetSourceSummary": VmWareAssetSourceSummary,
    "VmwareVCenterProperties": VmwareVCenterProperties,
    "VmwareVmAsset": VmwareVmAsset,
    "VmwareVmProperties": VmwareVmProperties,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
