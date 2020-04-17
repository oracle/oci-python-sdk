# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activate_exadata_infrastructure_details import ActivateExadataInfrastructureDetails
from .associated_database_details import AssociatedDatabaseDetails
from .autonomous_container_database import AutonomousContainerDatabase
from .autonomous_container_database_backup_config import AutonomousContainerDatabaseBackupConfig
from .autonomous_container_database_summary import AutonomousContainerDatabaseSummary
from .autonomous_data_warehouse import AutonomousDataWarehouse
from .autonomous_data_warehouse_backup import AutonomousDataWarehouseBackup
from .autonomous_data_warehouse_backup_summary import AutonomousDataWarehouseBackupSummary
from .autonomous_data_warehouse_connection_strings import AutonomousDataWarehouseConnectionStrings
from .autonomous_data_warehouse_console_token_details import AutonomousDataWarehouseConsoleTokenDetails
from .autonomous_data_warehouse_summary import AutonomousDataWarehouseSummary
from .autonomous_database import AutonomousDatabase
from .autonomous_database_backup import AutonomousDatabaseBackup
from .autonomous_database_backup_summary import AutonomousDatabaseBackupSummary
from .autonomous_database_connection_strings import AutonomousDatabaseConnectionStrings
from .autonomous_database_connection_urls import AutonomousDatabaseConnectionUrls
from .autonomous_database_console_token_details import AutonomousDatabaseConsoleTokenDetails
from .autonomous_database_summary import AutonomousDatabaseSummary
from .autonomous_database_wallet import AutonomousDatabaseWallet
from .autonomous_db_preview_version_summary import AutonomousDbPreviewVersionSummary
from .autonomous_db_version_summary import AutonomousDbVersionSummary
from .autonomous_exadata_infrastructure import AutonomousExadataInfrastructure
from .autonomous_exadata_infrastructure_shape_summary import AutonomousExadataInfrastructureShapeSummary
from .autonomous_exadata_infrastructure_summary import AutonomousExadataInfrastructureSummary
from .backup import Backup
from .backup_destination import BackupDestination
from .backup_destination_details import BackupDestinationDetails
from .backup_destination_summary import BackupDestinationSummary
from .backup_summary import BackupSummary
from .change_compartment_details import ChangeCompartmentDetails
from .change_exadata_infrastructure_compartment_details import ChangeExadataInfrastructureCompartmentDetails
from .change_vm_cluster_compartment_details import ChangeVmClusterCompartmentDetails
from .complete_external_backup_job_details import CompleteExternalBackupJobDetails
from .console_connection import ConsoleConnection
from .console_connection_summary import ConsoleConnectionSummary
from .create_autonomous_container_database_details import CreateAutonomousContainerDatabaseDetails
from .create_autonomous_data_warehouse_backup_details import CreateAutonomousDataWarehouseBackupDetails
from .create_autonomous_data_warehouse_details import CreateAutonomousDataWarehouseDetails
from .create_autonomous_database_backup_details import CreateAutonomousDatabaseBackupDetails
from .create_autonomous_database_base import CreateAutonomousDatabaseBase
from .create_autonomous_database_clone_details import CreateAutonomousDatabaseCloneDetails
from .create_autonomous_database_details import CreateAutonomousDatabaseDetails
from .create_autonomous_database_from_backup_details import CreateAutonomousDatabaseFromBackupDetails
from .create_autonomous_database_from_backup_timestamp_details import CreateAutonomousDatabaseFromBackupTimestampDetails
from .create_backup_destination_details import CreateBackupDestinationDetails
from .create_backup_details import CreateBackupDetails
from .create_console_connection_details import CreateConsoleConnectionDetails
from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from .create_data_guard_association_to_existing_db_system_details import CreateDataGuardAssociationToExistingDbSystemDetails
from .create_data_guard_association_with_new_db_system_details import CreateDataGuardAssociationWithNewDbSystemDetails
from .create_database_base import CreateDatabaseBase
from .create_database_details import CreateDatabaseDetails
from .create_database_from_backup import CreateDatabaseFromBackup
from .create_database_from_backup_details import CreateDatabaseFromBackupDetails
from .create_db_home_base import CreateDbHomeBase
from .create_db_home_details import CreateDbHomeDetails
from .create_db_home_from_backup_details import CreateDbHomeFromBackupDetails
from .create_db_home_with_db_system_id_details import CreateDbHomeWithDbSystemIdDetails
from .create_db_home_with_db_system_id_from_backup_details import CreateDbHomeWithDbSystemIdFromBackupDetails
from .create_db_home_with_vm_cluster_id_details import CreateDbHomeWithVmClusterIdDetails
from .create_exadata_infrastructure_details import CreateExadataInfrastructureDetails
from .create_external_backup_job_details import CreateExternalBackupJobDetails
from .create_nfs_backup_destination_details import CreateNFSBackupDestinationDetails
from .create_new_database_details import CreateNewDatabaseDetails
from .create_recovery_appliance_backup_destination_details import CreateRecoveryApplianceBackupDestinationDetails
from .create_vm_cluster_details import CreateVmClusterDetails
from .data_guard_association import DataGuardAssociation
from .data_guard_association_summary import DataGuardAssociationSummary
from .database import Database
from .database_connection_strings import DatabaseConnectionStrings
from .database_summary import DatabaseSummary
from .day_of_week import DayOfWeek
from .db_backup_config import DbBackupConfig
from .db_home import DbHome
from .db_home_summary import DbHomeSummary
from .db_iorm_config import DbIormConfig
from .db_iorm_config_update_detail import DbIormConfigUpdateDetail
from .db_node import DbNode
from .db_node_summary import DbNodeSummary
from .db_system import DbSystem
from .db_system_options import DbSystemOptions
from .db_system_shape_summary import DbSystemShapeSummary
from .db_system_summary import DbSystemSummary
from .db_version_summary import DbVersionSummary
from .exadata_infrastructure import ExadataInfrastructure
from .exadata_infrastructure_summary import ExadataInfrastructureSummary
from .exadata_iorm_config import ExadataIormConfig
from .exadata_iorm_config_update_details import ExadataIormConfigUpdateDetails
from .external_backup_job import ExternalBackupJob
from .failover_data_guard_association_details import FailoverDataGuardAssociationDetails
from .generate_autonomous_data_warehouse_wallet_details import GenerateAutonomousDataWarehouseWalletDetails
from .generate_autonomous_database_wallet_details import GenerateAutonomousDatabaseWalletDetails
from .generate_recommended_network_details import GenerateRecommendedNetworkDetails
from .gi_version_summary import GiVersionSummary
from .info_for_network_gen_details import InfoForNetworkGenDetails
from .launch_autonomous_exadata_infrastructure_details import LaunchAutonomousExadataInfrastructureDetails
from .launch_db_system_base import LaunchDbSystemBase
from .launch_db_system_details import LaunchDbSystemDetails
from .launch_db_system_from_backup_details import LaunchDbSystemFromBackupDetails
from .maintenance_run import MaintenanceRun
from .maintenance_run_summary import MaintenanceRunSummary
from .maintenance_window import MaintenanceWindow
from .month import Month
from .node_details import NodeDetails
from .ocp_us import OCPUs
from .patch import Patch
from .patch_details import PatchDetails
from .patch_history_entry import PatchHistoryEntry
from .patch_history_entry_summary import PatchHistoryEntrySummary
from .patch_summary import PatchSummary
from .reinstate_data_guard_association_details import ReinstateDataGuardAssociationDetails
from .restore_autonomous_data_warehouse_details import RestoreAutonomousDataWarehouseDetails
from .restore_autonomous_database_details import RestoreAutonomousDatabaseDetails
from .restore_database_details import RestoreDatabaseDetails
from .scan_details import ScanDetails
from .switchover_data_guard_association_details import SwitchoverDataGuardAssociationDetails
from .update_autonomous_container_database_details import UpdateAutonomousContainerDatabaseDetails
from .update_autonomous_data_warehouse_details import UpdateAutonomousDataWarehouseDetails
from .update_autonomous_database_details import UpdateAutonomousDatabaseDetails
from .update_autonomous_database_wallet_details import UpdateAutonomousDatabaseWalletDetails
from .update_autonomous_exadata_infrastructure_details import UpdateAutonomousExadataInfrastructureDetails
from .update_backup_destination_details import UpdateBackupDestinationDetails
from .update_database_details import UpdateDatabaseDetails
from .update_db_home_details import UpdateDbHomeDetails
from .update_db_system_details import UpdateDbSystemDetails
from .update_exadata_infrastructure_details import UpdateExadataInfrastructureDetails
from .update_maintenance_run_details import UpdateMaintenanceRunDetails
from .update_vm_cluster_details import UpdateVmClusterDetails
from .update_vm_cluster_network_details import UpdateVmClusterNetworkDetails
from .vm_cluster import VmCluster
from .vm_cluster_network import VmClusterNetwork
from .vm_cluster_network_details import VmClusterNetworkDetails
from .vm_cluster_network_summary import VmClusterNetworkSummary
from .vm_cluster_summary import VmClusterSummary
from .vm_network_details import VmNetworkDetails
from .workload_type import WorkloadType

# Maps type names to classes for database services.
database_type_mapping = {
    "ActivateExadataInfrastructureDetails": ActivateExadataInfrastructureDetails,
    "AssociatedDatabaseDetails": AssociatedDatabaseDetails,
    "AutonomousContainerDatabase": AutonomousContainerDatabase,
    "AutonomousContainerDatabaseBackupConfig": AutonomousContainerDatabaseBackupConfig,
    "AutonomousContainerDatabaseSummary": AutonomousContainerDatabaseSummary,
    "AutonomousDataWarehouse": AutonomousDataWarehouse,
    "AutonomousDataWarehouseBackup": AutonomousDataWarehouseBackup,
    "AutonomousDataWarehouseBackupSummary": AutonomousDataWarehouseBackupSummary,
    "AutonomousDataWarehouseConnectionStrings": AutonomousDataWarehouseConnectionStrings,
    "AutonomousDataWarehouseConsoleTokenDetails": AutonomousDataWarehouseConsoleTokenDetails,
    "AutonomousDataWarehouseSummary": AutonomousDataWarehouseSummary,
    "AutonomousDatabase": AutonomousDatabase,
    "AutonomousDatabaseBackup": AutonomousDatabaseBackup,
    "AutonomousDatabaseBackupSummary": AutonomousDatabaseBackupSummary,
    "AutonomousDatabaseConnectionStrings": AutonomousDatabaseConnectionStrings,
    "AutonomousDatabaseConnectionUrls": AutonomousDatabaseConnectionUrls,
    "AutonomousDatabaseConsoleTokenDetails": AutonomousDatabaseConsoleTokenDetails,
    "AutonomousDatabaseSummary": AutonomousDatabaseSummary,
    "AutonomousDatabaseWallet": AutonomousDatabaseWallet,
    "AutonomousDbPreviewVersionSummary": AutonomousDbPreviewVersionSummary,
    "AutonomousDbVersionSummary": AutonomousDbVersionSummary,
    "AutonomousExadataInfrastructure": AutonomousExadataInfrastructure,
    "AutonomousExadataInfrastructureShapeSummary": AutonomousExadataInfrastructureShapeSummary,
    "AutonomousExadataInfrastructureSummary": AutonomousExadataInfrastructureSummary,
    "Backup": Backup,
    "BackupDestination": BackupDestination,
    "BackupDestinationDetails": BackupDestinationDetails,
    "BackupDestinationSummary": BackupDestinationSummary,
    "BackupSummary": BackupSummary,
    "ChangeCompartmentDetails": ChangeCompartmentDetails,
    "ChangeExadataInfrastructureCompartmentDetails": ChangeExadataInfrastructureCompartmentDetails,
    "ChangeVmClusterCompartmentDetails": ChangeVmClusterCompartmentDetails,
    "CompleteExternalBackupJobDetails": CompleteExternalBackupJobDetails,
    "ConsoleConnection": ConsoleConnection,
    "ConsoleConnectionSummary": ConsoleConnectionSummary,
    "CreateAutonomousContainerDatabaseDetails": CreateAutonomousContainerDatabaseDetails,
    "CreateAutonomousDataWarehouseBackupDetails": CreateAutonomousDataWarehouseBackupDetails,
    "CreateAutonomousDataWarehouseDetails": CreateAutonomousDataWarehouseDetails,
    "CreateAutonomousDatabaseBackupDetails": CreateAutonomousDatabaseBackupDetails,
    "CreateAutonomousDatabaseBase": CreateAutonomousDatabaseBase,
    "CreateAutonomousDatabaseCloneDetails": CreateAutonomousDatabaseCloneDetails,
    "CreateAutonomousDatabaseDetails": CreateAutonomousDatabaseDetails,
    "CreateAutonomousDatabaseFromBackupDetails": CreateAutonomousDatabaseFromBackupDetails,
    "CreateAutonomousDatabaseFromBackupTimestampDetails": CreateAutonomousDatabaseFromBackupTimestampDetails,
    "CreateBackupDestinationDetails": CreateBackupDestinationDetails,
    "CreateBackupDetails": CreateBackupDetails,
    "CreateConsoleConnectionDetails": CreateConsoleConnectionDetails,
    "CreateDataGuardAssociationDetails": CreateDataGuardAssociationDetails,
    "CreateDataGuardAssociationToExistingDbSystemDetails": CreateDataGuardAssociationToExistingDbSystemDetails,
    "CreateDataGuardAssociationWithNewDbSystemDetails": CreateDataGuardAssociationWithNewDbSystemDetails,
    "CreateDatabaseBase": CreateDatabaseBase,
    "CreateDatabaseDetails": CreateDatabaseDetails,
    "CreateDatabaseFromBackup": CreateDatabaseFromBackup,
    "CreateDatabaseFromBackupDetails": CreateDatabaseFromBackupDetails,
    "CreateDbHomeBase": CreateDbHomeBase,
    "CreateDbHomeDetails": CreateDbHomeDetails,
    "CreateDbHomeFromBackupDetails": CreateDbHomeFromBackupDetails,
    "CreateDbHomeWithDbSystemIdDetails": CreateDbHomeWithDbSystemIdDetails,
    "CreateDbHomeWithDbSystemIdFromBackupDetails": CreateDbHomeWithDbSystemIdFromBackupDetails,
    "CreateDbHomeWithVmClusterIdDetails": CreateDbHomeWithVmClusterIdDetails,
    "CreateExadataInfrastructureDetails": CreateExadataInfrastructureDetails,
    "CreateExternalBackupJobDetails": CreateExternalBackupJobDetails,
    "CreateNFSBackupDestinationDetails": CreateNFSBackupDestinationDetails,
    "CreateNewDatabaseDetails": CreateNewDatabaseDetails,
    "CreateRecoveryApplianceBackupDestinationDetails": CreateRecoveryApplianceBackupDestinationDetails,
    "CreateVmClusterDetails": CreateVmClusterDetails,
    "DataGuardAssociation": DataGuardAssociation,
    "DataGuardAssociationSummary": DataGuardAssociationSummary,
    "Database": Database,
    "DatabaseConnectionStrings": DatabaseConnectionStrings,
    "DatabaseSummary": DatabaseSummary,
    "DayOfWeek": DayOfWeek,
    "DbBackupConfig": DbBackupConfig,
    "DbHome": DbHome,
    "DbHomeSummary": DbHomeSummary,
    "DbIormConfig": DbIormConfig,
    "DbIormConfigUpdateDetail": DbIormConfigUpdateDetail,
    "DbNode": DbNode,
    "DbNodeSummary": DbNodeSummary,
    "DbSystem": DbSystem,
    "DbSystemOptions": DbSystemOptions,
    "DbSystemShapeSummary": DbSystemShapeSummary,
    "DbSystemSummary": DbSystemSummary,
    "DbVersionSummary": DbVersionSummary,
    "ExadataInfrastructure": ExadataInfrastructure,
    "ExadataInfrastructureSummary": ExadataInfrastructureSummary,
    "ExadataIormConfig": ExadataIormConfig,
    "ExadataIormConfigUpdateDetails": ExadataIormConfigUpdateDetails,
    "ExternalBackupJob": ExternalBackupJob,
    "FailoverDataGuardAssociationDetails": FailoverDataGuardAssociationDetails,
    "GenerateAutonomousDataWarehouseWalletDetails": GenerateAutonomousDataWarehouseWalletDetails,
    "GenerateAutonomousDatabaseWalletDetails": GenerateAutonomousDatabaseWalletDetails,
    "GenerateRecommendedNetworkDetails": GenerateRecommendedNetworkDetails,
    "GiVersionSummary": GiVersionSummary,
    "InfoForNetworkGenDetails": InfoForNetworkGenDetails,
    "LaunchAutonomousExadataInfrastructureDetails": LaunchAutonomousExadataInfrastructureDetails,
    "LaunchDbSystemBase": LaunchDbSystemBase,
    "LaunchDbSystemDetails": LaunchDbSystemDetails,
    "LaunchDbSystemFromBackupDetails": LaunchDbSystemFromBackupDetails,
    "MaintenanceRun": MaintenanceRun,
    "MaintenanceRunSummary": MaintenanceRunSummary,
    "MaintenanceWindow": MaintenanceWindow,
    "Month": Month,
    "NodeDetails": NodeDetails,
    "OCPUs": OCPUs,
    "Patch": Patch,
    "PatchDetails": PatchDetails,
    "PatchHistoryEntry": PatchHistoryEntry,
    "PatchHistoryEntrySummary": PatchHistoryEntrySummary,
    "PatchSummary": PatchSummary,
    "ReinstateDataGuardAssociationDetails": ReinstateDataGuardAssociationDetails,
    "RestoreAutonomousDataWarehouseDetails": RestoreAutonomousDataWarehouseDetails,
    "RestoreAutonomousDatabaseDetails": RestoreAutonomousDatabaseDetails,
    "RestoreDatabaseDetails": RestoreDatabaseDetails,
    "ScanDetails": ScanDetails,
    "SwitchoverDataGuardAssociationDetails": SwitchoverDataGuardAssociationDetails,
    "UpdateAutonomousContainerDatabaseDetails": UpdateAutonomousContainerDatabaseDetails,
    "UpdateAutonomousDataWarehouseDetails": UpdateAutonomousDataWarehouseDetails,
    "UpdateAutonomousDatabaseDetails": UpdateAutonomousDatabaseDetails,
    "UpdateAutonomousDatabaseWalletDetails": UpdateAutonomousDatabaseWalletDetails,
    "UpdateAutonomousExadataInfrastructureDetails": UpdateAutonomousExadataInfrastructureDetails,
    "UpdateBackupDestinationDetails": UpdateBackupDestinationDetails,
    "UpdateDatabaseDetails": UpdateDatabaseDetails,
    "UpdateDbHomeDetails": UpdateDbHomeDetails,
    "UpdateDbSystemDetails": UpdateDbSystemDetails,
    "UpdateExadataInfrastructureDetails": UpdateExadataInfrastructureDetails,
    "UpdateMaintenanceRunDetails": UpdateMaintenanceRunDetails,
    "UpdateVmClusterDetails": UpdateVmClusterDetails,
    "UpdateVmClusterNetworkDetails": UpdateVmClusterNetworkDetails,
    "VmCluster": VmCluster,
    "VmClusterNetwork": VmClusterNetwork,
    "VmClusterNetworkDetails": VmClusterNetworkDetails,
    "VmClusterNetworkSummary": VmClusterNetworkSummary,
    "VmClusterSummary": VmClusterSummary,
    "VmNetworkDetails": VmNetworkDetails,
    "WorkloadType": WorkloadType
}
