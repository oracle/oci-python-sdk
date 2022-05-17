# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activate_exadata_infrastructure_details import ActivateExadataInfrastructureDetails
from .add_virtual_machine_to_vm_cluster_details import AddVirtualMachineToVmClusterDetails
from .associated_database_details import AssociatedDatabaseDetails
from .automated_mount_details import AutomatedMountDetails
from .autonomous_container_database import AutonomousContainerDatabase
from .autonomous_container_database_backup_config import AutonomousContainerDatabaseBackupConfig
from .autonomous_container_database_dataguard_association import AutonomousContainerDatabaseDataguardAssociation
from .autonomous_container_database_summary import AutonomousContainerDatabaseSummary
from .autonomous_data_warehouse import AutonomousDataWarehouse
from .autonomous_data_warehouse_connection_strings import AutonomousDataWarehouseConnectionStrings
from .autonomous_data_warehouse_summary import AutonomousDataWarehouseSummary
from .autonomous_database import AutonomousDatabase
from .autonomous_database_apex import AutonomousDatabaseApex
from .autonomous_database_backup import AutonomousDatabaseBackup
from .autonomous_database_backup_config import AutonomousDatabaseBackupConfig
from .autonomous_database_backup_summary import AutonomousDatabaseBackupSummary
from .autonomous_database_character_sets import AutonomousDatabaseCharacterSets
from .autonomous_database_connection_strings import AutonomousDatabaseConnectionStrings
from .autonomous_database_connection_urls import AutonomousDatabaseConnectionUrls
from .autonomous_database_console_token_details import AutonomousDatabaseConsoleTokenDetails
from .autonomous_database_dataguard_association import AutonomousDatabaseDataguardAssociation
from .autonomous_database_key_history_entry import AutonomousDatabaseKeyHistoryEntry
from .autonomous_database_manual_refresh_details import AutonomousDatabaseManualRefreshDetails
from .autonomous_database_standby_summary import AutonomousDatabaseStandbySummary
from .autonomous_database_summary import AutonomousDatabaseSummary
from .autonomous_database_wallet import AutonomousDatabaseWallet
from .autonomous_db_preview_version_summary import AutonomousDbPreviewVersionSummary
from .autonomous_db_version_summary import AutonomousDbVersionSummary
from .autonomous_exadata_infrastructure import AutonomousExadataInfrastructure
from .autonomous_exadata_infrastructure_shape_summary import AutonomousExadataInfrastructureShapeSummary
from .autonomous_exadata_infrastructure_summary import AutonomousExadataInfrastructureSummary
from .autonomous_patch import AutonomousPatch
from .autonomous_patch_summary import AutonomousPatchSummary
from .autonomous_vm_cluster import AutonomousVmCluster
from .autonomous_vm_cluster_summary import AutonomousVmClusterSummary
from .backup import Backup
from .backup_destination import BackupDestination
from .backup_destination_details import BackupDestinationDetails
from .backup_destination_summary import BackupDestinationSummary
from .backup_summary import BackupSummary
from .change_autonomous_vm_cluster_compartment_details import ChangeAutonomousVmClusterCompartmentDetails
from .change_cloud_autonomous_vm_cluster_compartment_details import ChangeCloudAutonomousVmClusterCompartmentDetails
from .change_cloud_exadata_infrastructure_compartment_details import ChangeCloudExadataInfrastructureCompartmentDetails
from .change_cloud_vm_cluster_compartment_details import ChangeCloudVmClusterCompartmentDetails
from .change_compartment_details import ChangeCompartmentDetails
from .change_exadata_infrastructure_compartment_details import ChangeExadataInfrastructureCompartmentDetails
from .change_key_store_compartment_details import ChangeKeyStoreCompartmentDetails
from .change_vm_cluster_compartment_details import ChangeVmClusterCompartmentDetails
from .cloud_autonomous_vm_cluster import CloudAutonomousVmCluster
from .cloud_autonomous_vm_cluster_summary import CloudAutonomousVmClusterSummary
from .cloud_database_management_config import CloudDatabaseManagementConfig
from .cloud_exadata_infrastructure import CloudExadataInfrastructure
from .cloud_exadata_infrastructure_summary import CloudExadataInfrastructureSummary
from .cloud_vm_cluster import CloudVmCluster
from .cloud_vm_cluster_summary import CloudVmClusterSummary
from .complete_external_backup_job_details import CompleteExternalBackupJobDetails
from .compute_performance_summary import ComputePerformanceSummary
from .configure_autonomous_database_vault_key_details import ConfigureAutonomousDatabaseVaultKeyDetails
from .console_connection import ConsoleConnection
from .console_connection_summary import ConsoleConnectionSummary
from .convert_to_pdb_details import ConvertToPdbDetails
from .convert_to_pdb_target_base import ConvertToPdbTargetBase
from .create_autonomous_container_database_details import CreateAutonomousContainerDatabaseDetails
from .create_autonomous_database_backup_details import CreateAutonomousDatabaseBackupDetails
from .create_autonomous_database_base import CreateAutonomousDatabaseBase
from .create_autonomous_database_clone_details import CreateAutonomousDatabaseCloneDetails
from .create_autonomous_database_details import CreateAutonomousDatabaseDetails
from .create_autonomous_database_from_backup_details import CreateAutonomousDatabaseFromBackupDetails
from .create_autonomous_database_from_backup_timestamp_details import CreateAutonomousDatabaseFromBackupTimestampDetails
from .create_autonomous_vm_cluster_details import CreateAutonomousVmClusterDetails
from .create_backup_destination_details import CreateBackupDestinationDetails
from .create_backup_details import CreateBackupDetails
from .create_cloud_autonomous_vm_cluster_details import CreateCloudAutonomousVmClusterDetails
from .create_cloud_exadata_infrastructure_details import CreateCloudExadataInfrastructureDetails
from .create_cloud_vm_cluster_details import CreateCloudVmClusterDetails
from .create_console_connection_details import CreateConsoleConnectionDetails
from .create_cross_region_autonomous_database_data_guard_details import CreateCrossRegionAutonomousDatabaseDataGuardDetails
from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from .create_data_guard_association_to_existing_db_system_details import CreateDataGuardAssociationToExistingDbSystemDetails
from .create_data_guard_association_to_existing_vm_cluster_details import CreateDataGuardAssociationToExistingVmClusterDetails
from .create_data_guard_association_with_new_db_system_details import CreateDataGuardAssociationWithNewDbSystemDetails
from .create_database_base import CreateDatabaseBase
from .create_database_details import CreateDatabaseDetails
from .create_database_from_another_database_details import CreateDatabaseFromAnotherDatabaseDetails
from .create_database_from_backup import CreateDatabaseFromBackup
from .create_database_from_backup_details import CreateDatabaseFromBackupDetails
from .create_database_from_db_system_details import CreateDatabaseFromDbSystemDetails
from .create_database_software_image_details import CreateDatabaseSoftwareImageDetails
from .create_db_home_base import CreateDbHomeBase
from .create_db_home_details import CreateDbHomeDetails
from .create_db_home_from_backup_details import CreateDbHomeFromBackupDetails
from .create_db_home_from_database_details import CreateDbHomeFromDatabaseDetails
from .create_db_home_from_db_system_details import CreateDbHomeFromDbSystemDetails
from .create_db_home_with_db_system_id_details import CreateDbHomeWithDbSystemIdDetails
from .create_db_home_with_db_system_id_from_backup_details import CreateDbHomeWithDbSystemIdFromBackupDetails
from .create_db_home_with_db_system_id_from_database_details import CreateDbHomeWithDbSystemIdFromDatabaseDetails
from .create_db_home_with_vm_cluster_id_details import CreateDbHomeWithVmClusterIdDetails
from .create_db_home_with_vm_cluster_id_from_backup_details import CreateDbHomeWithVmClusterIdFromBackupDetails
from .create_exadata_infrastructure_details import CreateExadataInfrastructureDetails
from .create_external_backup_job_details import CreateExternalBackupJobDetails
from .create_external_container_database_details import CreateExternalContainerDatabaseDetails
from .create_external_database_connector_details import CreateExternalDatabaseConnectorDetails
from .create_external_database_details_base import CreateExternalDatabaseDetailsBase
from .create_external_macs_connector_details import CreateExternalMacsConnectorDetails
from .create_external_non_container_database_details import CreateExternalNonContainerDatabaseDetails
from .create_external_pluggable_database_details import CreateExternalPluggableDatabaseDetails
from .create_key_store_details import CreateKeyStoreDetails
from .create_nfs_backup_destination_details import CreateNFSBackupDestinationDetails
from .create_new_database_details import CreateNewDatabaseDetails
from .create_pluggable_database_details import CreatePluggableDatabaseDetails
from .create_recovery_appliance_backup_destination_details import CreateRecoveryApplianceBackupDestinationDetails
from .create_refreshable_autonomous_database_clone_details import CreateRefreshableAutonomousDatabaseCloneDetails
from .create_vm_cluster_details import CreateVmClusterDetails
from .customer_contact import CustomerContact
from .data_collection_options import DataCollectionOptions
from .data_guard_association import DataGuardAssociation
from .data_guard_association_summary import DataGuardAssociationSummary
from .database import Database
from .database_connection_credentails_by_name import DatabaseConnectionCredentailsByName
from .database_connection_credentials import DatabaseConnectionCredentials
from .database_connection_credentials_by_details import DatabaseConnectionCredentialsByDetails
from .database_connection_string import DatabaseConnectionString
from .database_connection_string_profile import DatabaseConnectionStringProfile
from .database_connection_strings import DatabaseConnectionStrings
from .database_credential_details import DatabaseCredentialDetails
from .database_management_config import DatabaseManagementConfig
from .database_software_image import DatabaseSoftwareImage
from .database_software_image_summary import DatabaseSoftwareImageSummary
from .database_ssl_connection_credentials import DatabaseSslConnectionCredentials
from .database_summary import DatabaseSummary
from .database_upgrade_history_entry import DatabaseUpgradeHistoryEntry
from .database_upgrade_history_entry_summary import DatabaseUpgradeHistoryEntrySummary
from .database_upgrade_source_base import DatabaseUpgradeSourceBase
from .database_upgrade_with_database_software_image_details import DatabaseUpgradeWithDatabaseSoftwareImageDetails
from .database_upgrade_with_db_home_details import DatabaseUpgradeWithDbHomeDetails
from .database_upgrade_with_db_version_details import DatabaseUpgradeWithDbVersionDetails
from .day_of_week import DayOfWeek
from .db_backup_config import DbBackupConfig
from .db_home import DbHome
from .db_home_from_agent_resource_id import DbHomeFromAgentResourceId
from .db_home_summary import DbHomeSummary
from .db_iorm_config import DbIormConfig
from .db_iorm_config_update_detail import DbIormConfigUpdateDetail
from .db_node import DbNode
from .db_node_summary import DbNodeSummary
from .db_server import DbServer
from .db_server_details import DbServerDetails
from .db_server_patching_details import DbServerPatchingDetails
from .db_server_summary import DbServerSummary
from .db_system import DbSystem
from .db_system_compute_performance_summary import DbSystemComputePerformanceSummary
from .db_system_options import DbSystemOptions
from .db_system_shape_summary import DbSystemShapeSummary
from .db_system_storage_performance_summary import DbSystemStoragePerformanceSummary
from .db_system_summary import DbSystemSummary
from .db_system_upgrade_history_entry import DbSystemUpgradeHistoryEntry
from .db_system_upgrade_history_entry_summary import DbSystemUpgradeHistoryEntrySummary
from .db_version_summary import DbVersionSummary
from .deregister_autonomous_database_data_safe_details import DeregisterAutonomousDatabaseDataSafeDetails
from .disk_performance_details import DiskPerformanceDetails
from .enable_database_management_details import EnableDatabaseManagementDetails
from .enable_external_container_database_database_management_details import EnableExternalContainerDatabaseDatabaseManagementDetails
from .enable_external_container_database_stack_monitoring_details import EnableExternalContainerDatabaseStackMonitoringDetails
from .enable_external_database_management_details_base import EnableExternalDatabaseManagementDetailsBase
from .enable_external_database_operations_insights_details_base import EnableExternalDatabaseOperationsInsightsDetailsBase
from .enable_external_database_stack_monitoring_details_base import EnableExternalDatabaseStackMonitoringDetailsBase
from .enable_external_non_container_database_database_management_details import EnableExternalNonContainerDatabaseDatabaseManagementDetails
from .enable_external_non_container_database_operations_insights_details import EnableExternalNonContainerDatabaseOperationsInsightsDetails
from .enable_external_non_container_database_stack_monitoring_details import EnableExternalNonContainerDatabaseStackMonitoringDetails
from .enable_external_pluggable_database_database_management_details import EnableExternalPluggableDatabaseDatabaseManagementDetails
from .enable_external_pluggable_database_operations_insights_details import EnableExternalPluggableDatabaseOperationsInsightsDetails
from .enable_external_pluggable_database_stack_monitoring_details import EnableExternalPluggableDatabaseStackMonitoringDetails
from .estimated_patching_time import EstimatedPatchingTime
from .exadata_db_system_migration import ExadataDbSystemMigration
from .exadata_db_system_migration_summary import ExadataDbSystemMigrationSummary
from .exadata_infrastructure import ExadataInfrastructure
from .exadata_infrastructure_contact import ExadataInfrastructureContact
from .exadata_infrastructure_summary import ExadataInfrastructureSummary
from .exadata_iorm_config import ExadataIormConfig
from .exadata_iorm_config_update_details import ExadataIormConfigUpdateDetails
from .external_backup_job import ExternalBackupJob
from .external_container_database import ExternalContainerDatabase
from .external_container_database_summary import ExternalContainerDatabaseSummary
from .external_database_base import ExternalDatabaseBase
from .external_database_connector import ExternalDatabaseConnector
from .external_database_connector_summary import ExternalDatabaseConnectorSummary
from .external_macs_connector import ExternalMacsConnector
from .external_macs_connector_summary import ExternalMacsConnectorSummary
from .external_non_container_database import ExternalNonContainerDatabase
from .external_non_container_database_summary import ExternalNonContainerDatabaseSummary
from .external_pluggable_database import ExternalPluggableDatabase
from .external_pluggable_database_summary import ExternalPluggableDatabaseSummary
from .failover_data_guard_association_details import FailoverDataGuardAssociationDetails
from .flex_component_collection import FlexComponentCollection
from .flex_component_summary import FlexComponentSummary
from .generate_autonomous_database_wallet_details import GenerateAutonomousDatabaseWalletDetails
from .generate_recommended_network_details import GenerateRecommendedNetworkDetails
from .gi_version_summary import GiVersionSummary
from .info_for_network_gen_details import InfoForNetworkGenDetails
from .key_store import KeyStore
from .key_store_associated_database_details import KeyStoreAssociatedDatabaseDetails
from .key_store_summary import KeyStoreSummary
from .key_store_type_details import KeyStoreTypeDetails
from .key_store_type_from_oracle_key_vault_details import KeyStoreTypeFromOracleKeyVaultDetails
from .launch_autonomous_exadata_infrastructure_details import LaunchAutonomousExadataInfrastructureDetails
from .launch_db_system_base import LaunchDbSystemBase
from .launch_db_system_details import LaunchDbSystemDetails
from .launch_db_system_from_backup_details import LaunchDbSystemFromBackupDetails
from .launch_db_system_from_database_details import LaunchDbSystemFromDatabaseDetails
from .launch_db_system_from_db_system_details import LaunchDbSystemFromDbSystemDetails
from .local_clone_pluggable_database_details import LocalClonePluggableDatabaseDetails
from .maintenance_run import MaintenanceRun
from .maintenance_run_summary import MaintenanceRunSummary
from .maintenance_window import MaintenanceWindow
from .migrate_vault_key_details import MigrateVaultKeyDetails
from .modify_database_management_details import ModifyDatabaseManagementDetails
from .month import Month
from .mount_type_details import MountTypeDetails
from .node_details import NodeDetails
from .ocp_us import OCPUs
from .operations_insights_config import OperationsInsightsConfig
from .patch import Patch
from .patch_details import PatchDetails
from .patch_history_entry import PatchHistoryEntry
from .patch_history_entry_summary import PatchHistoryEntrySummary
from .patch_summary import PatchSummary
from .pdb_conversion_history_entry import PdbConversionHistoryEntry
from .pdb_conversion_history_entry_summary import PdbConversionHistoryEntrySummary
from .pdb_conversion_to_new_database_details import PdbConversionToNewDatabaseDetails
from .peer_autonomous_container_database_backup_config import PeerAutonomousContainerDatabaseBackupConfig
from .pluggable_database import PluggableDatabase
from .pluggable_database_connection_strings import PluggableDatabaseConnectionStrings
from .pluggable_database_summary import PluggableDatabaseSummary
from .register_autonomous_database_data_safe_details import RegisterAutonomousDatabaseDataSafeDetails
from .reinstate_data_guard_association_details import ReinstateDataGuardAssociationDetails
from .remote_clone_pluggable_database_details import RemoteClonePluggableDatabaseDetails
from .remove_virtual_machine_from_vm_cluster_details import RemoveVirtualMachineFromVmClusterDetails
from .restore_autonomous_database_details import RestoreAutonomousDatabaseDetails
from .restore_database_details import RestoreDatabaseDetails
from .scan_details import ScanDetails
from .scheduled_operation_details import ScheduledOperationDetails
from .self_mount_details import SelfMountDetails
from .stack_monitoring_config import StackMonitoringConfig
from .storage_performance_details import StoragePerformanceDetails
from .switchover_data_guard_association_details import SwitchoverDataGuardAssociationDetails
from .update import Update
from .update_autonomous_container_database_data_guard_association_details import UpdateAutonomousContainerDatabaseDataGuardAssociationDetails
from .update_autonomous_container_database_details import UpdateAutonomousContainerDatabaseDetails
from .update_autonomous_database_details import UpdateAutonomousDatabaseDetails
from .update_autonomous_database_wallet_details import UpdateAutonomousDatabaseWalletDetails
from .update_autonomous_exadata_infrastructure_details import UpdateAutonomousExadataInfrastructureDetails
from .update_autonomous_vm_cluster_details import UpdateAutonomousVmClusterDetails
from .update_backup_destination_details import UpdateBackupDestinationDetails
from .update_cloud_autonomous_vm_cluster_details import UpdateCloudAutonomousVmClusterDetails
from .update_cloud_exadata_infrastructure_details import UpdateCloudExadataInfrastructureDetails
from .update_cloud_vm_cluster_details import UpdateCloudVmClusterDetails
from .update_data_guard_association_details import UpdateDataGuardAssociationDetails
from .update_database_details import UpdateDatabaseDetails
from .update_database_software_image_details import UpdateDatabaseSoftwareImageDetails
from .update_db_home_details import UpdateDbHomeDetails
from .update_db_system_details import UpdateDbSystemDetails
from .update_details import UpdateDetails
from .update_exadata_infrastructure_details import UpdateExadataInfrastructureDetails
from .update_external_container_database_details import UpdateExternalContainerDatabaseDetails
from .update_external_database_connector_details import UpdateExternalDatabaseConnectorDetails
from .update_external_database_details_base import UpdateExternalDatabaseDetailsBase
from .update_external_macs_connector_details import UpdateExternalMacsConnectorDetails
from .update_external_non_container_database_details import UpdateExternalNonContainerDatabaseDetails
from .update_external_pluggable_database_details import UpdateExternalPluggableDatabaseDetails
from .update_history_entry import UpdateHistoryEntry
from .update_history_entry_summary import UpdateHistoryEntrySummary
from .update_key_store_details import UpdateKeyStoreDetails
from .update_maintenance_run_details import UpdateMaintenanceRunDetails
from .update_pluggable_database_details import UpdatePluggableDatabaseDetails
from .update_summary import UpdateSummary
from .update_vm_cluster_details import UpdateVmClusterDetails
from .update_vm_cluster_network_details import UpdateVmClusterNetworkDetails
from .upgrade_database_details import UpgradeDatabaseDetails
from .upgrade_db_system_details import UpgradeDbSystemDetails
from .vm_cluster import VmCluster
from .vm_cluster_network import VmClusterNetwork
from .vm_cluster_network_details import VmClusterNetworkDetails
from .vm_cluster_network_summary import VmClusterNetworkSummary
from .vm_cluster_summary import VmClusterSummary
from .vm_cluster_update import VmClusterUpdate
from .vm_cluster_update_details import VmClusterUpdateDetails
from .vm_cluster_update_history_entry import VmClusterUpdateHistoryEntry
from .vm_cluster_update_history_entry_summary import VmClusterUpdateHistoryEntrySummary
from .vm_cluster_update_summary import VmClusterUpdateSummary
from .vm_network_details import VmNetworkDetails
from .workload_type import WorkloadType

# Maps type names to classes for database services.
database_type_mapping = {
    "ActivateExadataInfrastructureDetails": ActivateExadataInfrastructureDetails,
    "AddVirtualMachineToVmClusterDetails": AddVirtualMachineToVmClusterDetails,
    "AssociatedDatabaseDetails": AssociatedDatabaseDetails,
    "AutomatedMountDetails": AutomatedMountDetails,
    "AutonomousContainerDatabase": AutonomousContainerDatabase,
    "AutonomousContainerDatabaseBackupConfig": AutonomousContainerDatabaseBackupConfig,
    "AutonomousContainerDatabaseDataguardAssociation": AutonomousContainerDatabaseDataguardAssociation,
    "AutonomousContainerDatabaseSummary": AutonomousContainerDatabaseSummary,
    "AutonomousDataWarehouse": AutonomousDataWarehouse,
    "AutonomousDataWarehouseConnectionStrings": AutonomousDataWarehouseConnectionStrings,
    "AutonomousDataWarehouseSummary": AutonomousDataWarehouseSummary,
    "AutonomousDatabase": AutonomousDatabase,
    "AutonomousDatabaseApex": AutonomousDatabaseApex,
    "AutonomousDatabaseBackup": AutonomousDatabaseBackup,
    "AutonomousDatabaseBackupConfig": AutonomousDatabaseBackupConfig,
    "AutonomousDatabaseBackupSummary": AutonomousDatabaseBackupSummary,
    "AutonomousDatabaseCharacterSets": AutonomousDatabaseCharacterSets,
    "AutonomousDatabaseConnectionStrings": AutonomousDatabaseConnectionStrings,
    "AutonomousDatabaseConnectionUrls": AutonomousDatabaseConnectionUrls,
    "AutonomousDatabaseConsoleTokenDetails": AutonomousDatabaseConsoleTokenDetails,
    "AutonomousDatabaseDataguardAssociation": AutonomousDatabaseDataguardAssociation,
    "AutonomousDatabaseKeyHistoryEntry": AutonomousDatabaseKeyHistoryEntry,
    "AutonomousDatabaseManualRefreshDetails": AutonomousDatabaseManualRefreshDetails,
    "AutonomousDatabaseStandbySummary": AutonomousDatabaseStandbySummary,
    "AutonomousDatabaseSummary": AutonomousDatabaseSummary,
    "AutonomousDatabaseWallet": AutonomousDatabaseWallet,
    "AutonomousDbPreviewVersionSummary": AutonomousDbPreviewVersionSummary,
    "AutonomousDbVersionSummary": AutonomousDbVersionSummary,
    "AutonomousExadataInfrastructure": AutonomousExadataInfrastructure,
    "AutonomousExadataInfrastructureShapeSummary": AutonomousExadataInfrastructureShapeSummary,
    "AutonomousExadataInfrastructureSummary": AutonomousExadataInfrastructureSummary,
    "AutonomousPatch": AutonomousPatch,
    "AutonomousPatchSummary": AutonomousPatchSummary,
    "AutonomousVmCluster": AutonomousVmCluster,
    "AutonomousVmClusterSummary": AutonomousVmClusterSummary,
    "Backup": Backup,
    "BackupDestination": BackupDestination,
    "BackupDestinationDetails": BackupDestinationDetails,
    "BackupDestinationSummary": BackupDestinationSummary,
    "BackupSummary": BackupSummary,
    "ChangeAutonomousVmClusterCompartmentDetails": ChangeAutonomousVmClusterCompartmentDetails,
    "ChangeCloudAutonomousVmClusterCompartmentDetails": ChangeCloudAutonomousVmClusterCompartmentDetails,
    "ChangeCloudExadataInfrastructureCompartmentDetails": ChangeCloudExadataInfrastructureCompartmentDetails,
    "ChangeCloudVmClusterCompartmentDetails": ChangeCloudVmClusterCompartmentDetails,
    "ChangeCompartmentDetails": ChangeCompartmentDetails,
    "ChangeExadataInfrastructureCompartmentDetails": ChangeExadataInfrastructureCompartmentDetails,
    "ChangeKeyStoreCompartmentDetails": ChangeKeyStoreCompartmentDetails,
    "ChangeVmClusterCompartmentDetails": ChangeVmClusterCompartmentDetails,
    "CloudAutonomousVmCluster": CloudAutonomousVmCluster,
    "CloudAutonomousVmClusterSummary": CloudAutonomousVmClusterSummary,
    "CloudDatabaseManagementConfig": CloudDatabaseManagementConfig,
    "CloudExadataInfrastructure": CloudExadataInfrastructure,
    "CloudExadataInfrastructureSummary": CloudExadataInfrastructureSummary,
    "CloudVmCluster": CloudVmCluster,
    "CloudVmClusterSummary": CloudVmClusterSummary,
    "CompleteExternalBackupJobDetails": CompleteExternalBackupJobDetails,
    "ComputePerformanceSummary": ComputePerformanceSummary,
    "ConfigureAutonomousDatabaseVaultKeyDetails": ConfigureAutonomousDatabaseVaultKeyDetails,
    "ConsoleConnection": ConsoleConnection,
    "ConsoleConnectionSummary": ConsoleConnectionSummary,
    "ConvertToPdbDetails": ConvertToPdbDetails,
    "ConvertToPdbTargetBase": ConvertToPdbTargetBase,
    "CreateAutonomousContainerDatabaseDetails": CreateAutonomousContainerDatabaseDetails,
    "CreateAutonomousDatabaseBackupDetails": CreateAutonomousDatabaseBackupDetails,
    "CreateAutonomousDatabaseBase": CreateAutonomousDatabaseBase,
    "CreateAutonomousDatabaseCloneDetails": CreateAutonomousDatabaseCloneDetails,
    "CreateAutonomousDatabaseDetails": CreateAutonomousDatabaseDetails,
    "CreateAutonomousDatabaseFromBackupDetails": CreateAutonomousDatabaseFromBackupDetails,
    "CreateAutonomousDatabaseFromBackupTimestampDetails": CreateAutonomousDatabaseFromBackupTimestampDetails,
    "CreateAutonomousVmClusterDetails": CreateAutonomousVmClusterDetails,
    "CreateBackupDestinationDetails": CreateBackupDestinationDetails,
    "CreateBackupDetails": CreateBackupDetails,
    "CreateCloudAutonomousVmClusterDetails": CreateCloudAutonomousVmClusterDetails,
    "CreateCloudExadataInfrastructureDetails": CreateCloudExadataInfrastructureDetails,
    "CreateCloudVmClusterDetails": CreateCloudVmClusterDetails,
    "CreateConsoleConnectionDetails": CreateConsoleConnectionDetails,
    "CreateCrossRegionAutonomousDatabaseDataGuardDetails": CreateCrossRegionAutonomousDatabaseDataGuardDetails,
    "CreateDataGuardAssociationDetails": CreateDataGuardAssociationDetails,
    "CreateDataGuardAssociationToExistingDbSystemDetails": CreateDataGuardAssociationToExistingDbSystemDetails,
    "CreateDataGuardAssociationToExistingVmClusterDetails": CreateDataGuardAssociationToExistingVmClusterDetails,
    "CreateDataGuardAssociationWithNewDbSystemDetails": CreateDataGuardAssociationWithNewDbSystemDetails,
    "CreateDatabaseBase": CreateDatabaseBase,
    "CreateDatabaseDetails": CreateDatabaseDetails,
    "CreateDatabaseFromAnotherDatabaseDetails": CreateDatabaseFromAnotherDatabaseDetails,
    "CreateDatabaseFromBackup": CreateDatabaseFromBackup,
    "CreateDatabaseFromBackupDetails": CreateDatabaseFromBackupDetails,
    "CreateDatabaseFromDbSystemDetails": CreateDatabaseFromDbSystemDetails,
    "CreateDatabaseSoftwareImageDetails": CreateDatabaseSoftwareImageDetails,
    "CreateDbHomeBase": CreateDbHomeBase,
    "CreateDbHomeDetails": CreateDbHomeDetails,
    "CreateDbHomeFromBackupDetails": CreateDbHomeFromBackupDetails,
    "CreateDbHomeFromDatabaseDetails": CreateDbHomeFromDatabaseDetails,
    "CreateDbHomeFromDbSystemDetails": CreateDbHomeFromDbSystemDetails,
    "CreateDbHomeWithDbSystemIdDetails": CreateDbHomeWithDbSystemIdDetails,
    "CreateDbHomeWithDbSystemIdFromBackupDetails": CreateDbHomeWithDbSystemIdFromBackupDetails,
    "CreateDbHomeWithDbSystemIdFromDatabaseDetails": CreateDbHomeWithDbSystemIdFromDatabaseDetails,
    "CreateDbHomeWithVmClusterIdDetails": CreateDbHomeWithVmClusterIdDetails,
    "CreateDbHomeWithVmClusterIdFromBackupDetails": CreateDbHomeWithVmClusterIdFromBackupDetails,
    "CreateExadataInfrastructureDetails": CreateExadataInfrastructureDetails,
    "CreateExternalBackupJobDetails": CreateExternalBackupJobDetails,
    "CreateExternalContainerDatabaseDetails": CreateExternalContainerDatabaseDetails,
    "CreateExternalDatabaseConnectorDetails": CreateExternalDatabaseConnectorDetails,
    "CreateExternalDatabaseDetailsBase": CreateExternalDatabaseDetailsBase,
    "CreateExternalMacsConnectorDetails": CreateExternalMacsConnectorDetails,
    "CreateExternalNonContainerDatabaseDetails": CreateExternalNonContainerDatabaseDetails,
    "CreateExternalPluggableDatabaseDetails": CreateExternalPluggableDatabaseDetails,
    "CreateKeyStoreDetails": CreateKeyStoreDetails,
    "CreateNFSBackupDestinationDetails": CreateNFSBackupDestinationDetails,
    "CreateNewDatabaseDetails": CreateNewDatabaseDetails,
    "CreatePluggableDatabaseDetails": CreatePluggableDatabaseDetails,
    "CreateRecoveryApplianceBackupDestinationDetails": CreateRecoveryApplianceBackupDestinationDetails,
    "CreateRefreshableAutonomousDatabaseCloneDetails": CreateRefreshableAutonomousDatabaseCloneDetails,
    "CreateVmClusterDetails": CreateVmClusterDetails,
    "CustomerContact": CustomerContact,
    "DataCollectionOptions": DataCollectionOptions,
    "DataGuardAssociation": DataGuardAssociation,
    "DataGuardAssociationSummary": DataGuardAssociationSummary,
    "Database": Database,
    "DatabaseConnectionCredentailsByName": DatabaseConnectionCredentailsByName,
    "DatabaseConnectionCredentials": DatabaseConnectionCredentials,
    "DatabaseConnectionCredentialsByDetails": DatabaseConnectionCredentialsByDetails,
    "DatabaseConnectionString": DatabaseConnectionString,
    "DatabaseConnectionStringProfile": DatabaseConnectionStringProfile,
    "DatabaseConnectionStrings": DatabaseConnectionStrings,
    "DatabaseCredentialDetails": DatabaseCredentialDetails,
    "DatabaseManagementConfig": DatabaseManagementConfig,
    "DatabaseSoftwareImage": DatabaseSoftwareImage,
    "DatabaseSoftwareImageSummary": DatabaseSoftwareImageSummary,
    "DatabaseSslConnectionCredentials": DatabaseSslConnectionCredentials,
    "DatabaseSummary": DatabaseSummary,
    "DatabaseUpgradeHistoryEntry": DatabaseUpgradeHistoryEntry,
    "DatabaseUpgradeHistoryEntrySummary": DatabaseUpgradeHistoryEntrySummary,
    "DatabaseUpgradeSourceBase": DatabaseUpgradeSourceBase,
    "DatabaseUpgradeWithDatabaseSoftwareImageDetails": DatabaseUpgradeWithDatabaseSoftwareImageDetails,
    "DatabaseUpgradeWithDbHomeDetails": DatabaseUpgradeWithDbHomeDetails,
    "DatabaseUpgradeWithDbVersionDetails": DatabaseUpgradeWithDbVersionDetails,
    "DayOfWeek": DayOfWeek,
    "DbBackupConfig": DbBackupConfig,
    "DbHome": DbHome,
    "DbHomeFromAgentResourceId": DbHomeFromAgentResourceId,
    "DbHomeSummary": DbHomeSummary,
    "DbIormConfig": DbIormConfig,
    "DbIormConfigUpdateDetail": DbIormConfigUpdateDetail,
    "DbNode": DbNode,
    "DbNodeSummary": DbNodeSummary,
    "DbServer": DbServer,
    "DbServerDetails": DbServerDetails,
    "DbServerPatchingDetails": DbServerPatchingDetails,
    "DbServerSummary": DbServerSummary,
    "DbSystem": DbSystem,
    "DbSystemComputePerformanceSummary": DbSystemComputePerformanceSummary,
    "DbSystemOptions": DbSystemOptions,
    "DbSystemShapeSummary": DbSystemShapeSummary,
    "DbSystemStoragePerformanceSummary": DbSystemStoragePerformanceSummary,
    "DbSystemSummary": DbSystemSummary,
    "DbSystemUpgradeHistoryEntry": DbSystemUpgradeHistoryEntry,
    "DbSystemUpgradeHistoryEntrySummary": DbSystemUpgradeHistoryEntrySummary,
    "DbVersionSummary": DbVersionSummary,
    "DeregisterAutonomousDatabaseDataSafeDetails": DeregisterAutonomousDatabaseDataSafeDetails,
    "DiskPerformanceDetails": DiskPerformanceDetails,
    "EnableDatabaseManagementDetails": EnableDatabaseManagementDetails,
    "EnableExternalContainerDatabaseDatabaseManagementDetails": EnableExternalContainerDatabaseDatabaseManagementDetails,
    "EnableExternalContainerDatabaseStackMonitoringDetails": EnableExternalContainerDatabaseStackMonitoringDetails,
    "EnableExternalDatabaseManagementDetailsBase": EnableExternalDatabaseManagementDetailsBase,
    "EnableExternalDatabaseOperationsInsightsDetailsBase": EnableExternalDatabaseOperationsInsightsDetailsBase,
    "EnableExternalDatabaseStackMonitoringDetailsBase": EnableExternalDatabaseStackMonitoringDetailsBase,
    "EnableExternalNonContainerDatabaseDatabaseManagementDetails": EnableExternalNonContainerDatabaseDatabaseManagementDetails,
    "EnableExternalNonContainerDatabaseOperationsInsightsDetails": EnableExternalNonContainerDatabaseOperationsInsightsDetails,
    "EnableExternalNonContainerDatabaseStackMonitoringDetails": EnableExternalNonContainerDatabaseStackMonitoringDetails,
    "EnableExternalPluggableDatabaseDatabaseManagementDetails": EnableExternalPluggableDatabaseDatabaseManagementDetails,
    "EnableExternalPluggableDatabaseOperationsInsightsDetails": EnableExternalPluggableDatabaseOperationsInsightsDetails,
    "EnableExternalPluggableDatabaseStackMonitoringDetails": EnableExternalPluggableDatabaseStackMonitoringDetails,
    "EstimatedPatchingTime": EstimatedPatchingTime,
    "ExadataDbSystemMigration": ExadataDbSystemMigration,
    "ExadataDbSystemMigrationSummary": ExadataDbSystemMigrationSummary,
    "ExadataInfrastructure": ExadataInfrastructure,
    "ExadataInfrastructureContact": ExadataInfrastructureContact,
    "ExadataInfrastructureSummary": ExadataInfrastructureSummary,
    "ExadataIormConfig": ExadataIormConfig,
    "ExadataIormConfigUpdateDetails": ExadataIormConfigUpdateDetails,
    "ExternalBackupJob": ExternalBackupJob,
    "ExternalContainerDatabase": ExternalContainerDatabase,
    "ExternalContainerDatabaseSummary": ExternalContainerDatabaseSummary,
    "ExternalDatabaseBase": ExternalDatabaseBase,
    "ExternalDatabaseConnector": ExternalDatabaseConnector,
    "ExternalDatabaseConnectorSummary": ExternalDatabaseConnectorSummary,
    "ExternalMacsConnector": ExternalMacsConnector,
    "ExternalMacsConnectorSummary": ExternalMacsConnectorSummary,
    "ExternalNonContainerDatabase": ExternalNonContainerDatabase,
    "ExternalNonContainerDatabaseSummary": ExternalNonContainerDatabaseSummary,
    "ExternalPluggableDatabase": ExternalPluggableDatabase,
    "ExternalPluggableDatabaseSummary": ExternalPluggableDatabaseSummary,
    "FailoverDataGuardAssociationDetails": FailoverDataGuardAssociationDetails,
    "FlexComponentCollection": FlexComponentCollection,
    "FlexComponentSummary": FlexComponentSummary,
    "GenerateAutonomousDatabaseWalletDetails": GenerateAutonomousDatabaseWalletDetails,
    "GenerateRecommendedNetworkDetails": GenerateRecommendedNetworkDetails,
    "GiVersionSummary": GiVersionSummary,
    "InfoForNetworkGenDetails": InfoForNetworkGenDetails,
    "KeyStore": KeyStore,
    "KeyStoreAssociatedDatabaseDetails": KeyStoreAssociatedDatabaseDetails,
    "KeyStoreSummary": KeyStoreSummary,
    "KeyStoreTypeDetails": KeyStoreTypeDetails,
    "KeyStoreTypeFromOracleKeyVaultDetails": KeyStoreTypeFromOracleKeyVaultDetails,
    "LaunchAutonomousExadataInfrastructureDetails": LaunchAutonomousExadataInfrastructureDetails,
    "LaunchDbSystemBase": LaunchDbSystemBase,
    "LaunchDbSystemDetails": LaunchDbSystemDetails,
    "LaunchDbSystemFromBackupDetails": LaunchDbSystemFromBackupDetails,
    "LaunchDbSystemFromDatabaseDetails": LaunchDbSystemFromDatabaseDetails,
    "LaunchDbSystemFromDbSystemDetails": LaunchDbSystemFromDbSystemDetails,
    "LocalClonePluggableDatabaseDetails": LocalClonePluggableDatabaseDetails,
    "MaintenanceRun": MaintenanceRun,
    "MaintenanceRunSummary": MaintenanceRunSummary,
    "MaintenanceWindow": MaintenanceWindow,
    "MigrateVaultKeyDetails": MigrateVaultKeyDetails,
    "ModifyDatabaseManagementDetails": ModifyDatabaseManagementDetails,
    "Month": Month,
    "MountTypeDetails": MountTypeDetails,
    "NodeDetails": NodeDetails,
    "OCPUs": OCPUs,
    "OperationsInsightsConfig": OperationsInsightsConfig,
    "Patch": Patch,
    "PatchDetails": PatchDetails,
    "PatchHistoryEntry": PatchHistoryEntry,
    "PatchHistoryEntrySummary": PatchHistoryEntrySummary,
    "PatchSummary": PatchSummary,
    "PdbConversionHistoryEntry": PdbConversionHistoryEntry,
    "PdbConversionHistoryEntrySummary": PdbConversionHistoryEntrySummary,
    "PdbConversionToNewDatabaseDetails": PdbConversionToNewDatabaseDetails,
    "PeerAutonomousContainerDatabaseBackupConfig": PeerAutonomousContainerDatabaseBackupConfig,
    "PluggableDatabase": PluggableDatabase,
    "PluggableDatabaseConnectionStrings": PluggableDatabaseConnectionStrings,
    "PluggableDatabaseSummary": PluggableDatabaseSummary,
    "RegisterAutonomousDatabaseDataSafeDetails": RegisterAutonomousDatabaseDataSafeDetails,
    "ReinstateDataGuardAssociationDetails": ReinstateDataGuardAssociationDetails,
    "RemoteClonePluggableDatabaseDetails": RemoteClonePluggableDatabaseDetails,
    "RemoveVirtualMachineFromVmClusterDetails": RemoveVirtualMachineFromVmClusterDetails,
    "RestoreAutonomousDatabaseDetails": RestoreAutonomousDatabaseDetails,
    "RestoreDatabaseDetails": RestoreDatabaseDetails,
    "ScanDetails": ScanDetails,
    "ScheduledOperationDetails": ScheduledOperationDetails,
    "SelfMountDetails": SelfMountDetails,
    "StackMonitoringConfig": StackMonitoringConfig,
    "StoragePerformanceDetails": StoragePerformanceDetails,
    "SwitchoverDataGuardAssociationDetails": SwitchoverDataGuardAssociationDetails,
    "Update": Update,
    "UpdateAutonomousContainerDatabaseDataGuardAssociationDetails": UpdateAutonomousContainerDatabaseDataGuardAssociationDetails,
    "UpdateAutonomousContainerDatabaseDetails": UpdateAutonomousContainerDatabaseDetails,
    "UpdateAutonomousDatabaseDetails": UpdateAutonomousDatabaseDetails,
    "UpdateAutonomousDatabaseWalletDetails": UpdateAutonomousDatabaseWalletDetails,
    "UpdateAutonomousExadataInfrastructureDetails": UpdateAutonomousExadataInfrastructureDetails,
    "UpdateAutonomousVmClusterDetails": UpdateAutonomousVmClusterDetails,
    "UpdateBackupDestinationDetails": UpdateBackupDestinationDetails,
    "UpdateCloudAutonomousVmClusterDetails": UpdateCloudAutonomousVmClusterDetails,
    "UpdateCloudExadataInfrastructureDetails": UpdateCloudExadataInfrastructureDetails,
    "UpdateCloudVmClusterDetails": UpdateCloudVmClusterDetails,
    "UpdateDataGuardAssociationDetails": UpdateDataGuardAssociationDetails,
    "UpdateDatabaseDetails": UpdateDatabaseDetails,
    "UpdateDatabaseSoftwareImageDetails": UpdateDatabaseSoftwareImageDetails,
    "UpdateDbHomeDetails": UpdateDbHomeDetails,
    "UpdateDbSystemDetails": UpdateDbSystemDetails,
    "UpdateDetails": UpdateDetails,
    "UpdateExadataInfrastructureDetails": UpdateExadataInfrastructureDetails,
    "UpdateExternalContainerDatabaseDetails": UpdateExternalContainerDatabaseDetails,
    "UpdateExternalDatabaseConnectorDetails": UpdateExternalDatabaseConnectorDetails,
    "UpdateExternalDatabaseDetailsBase": UpdateExternalDatabaseDetailsBase,
    "UpdateExternalMacsConnectorDetails": UpdateExternalMacsConnectorDetails,
    "UpdateExternalNonContainerDatabaseDetails": UpdateExternalNonContainerDatabaseDetails,
    "UpdateExternalPluggableDatabaseDetails": UpdateExternalPluggableDatabaseDetails,
    "UpdateHistoryEntry": UpdateHistoryEntry,
    "UpdateHistoryEntrySummary": UpdateHistoryEntrySummary,
    "UpdateKeyStoreDetails": UpdateKeyStoreDetails,
    "UpdateMaintenanceRunDetails": UpdateMaintenanceRunDetails,
    "UpdatePluggableDatabaseDetails": UpdatePluggableDatabaseDetails,
    "UpdateSummary": UpdateSummary,
    "UpdateVmClusterDetails": UpdateVmClusterDetails,
    "UpdateVmClusterNetworkDetails": UpdateVmClusterNetworkDetails,
    "UpgradeDatabaseDetails": UpgradeDatabaseDetails,
    "UpgradeDbSystemDetails": UpgradeDbSystemDetails,
    "VmCluster": VmCluster,
    "VmClusterNetwork": VmClusterNetwork,
    "VmClusterNetworkDetails": VmClusterNetworkDetails,
    "VmClusterNetworkSummary": VmClusterNetworkSummary,
    "VmClusterSummary": VmClusterSummary,
    "VmClusterUpdate": VmClusterUpdate,
    "VmClusterUpdateDetails": VmClusterUpdateDetails,
    "VmClusterUpdateHistoryEntry": VmClusterUpdateHistoryEntry,
    "VmClusterUpdateHistoryEntrySummary": VmClusterUpdateHistoryEntrySummary,
    "VmClusterUpdateSummary": VmClusterUpdateSummary,
    "VmNetworkDetails": VmNetworkDetails,
    "WorkloadType": WorkloadType
}
