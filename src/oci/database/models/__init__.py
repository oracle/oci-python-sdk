# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

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
from .autonomous_db_preview_version_summary import AutonomousDbPreviewVersionSummary
from .autonomous_exadata_infrastructure import AutonomousExadataInfrastructure
from .autonomous_exadata_infrastructure_maintenance_window import AutonomousExadataInfrastructureMaintenanceWindow
from .autonomous_exadata_infrastructure_shape_summary import AutonomousExadataInfrastructureShapeSummary
from .autonomous_exadata_infrastructure_summary import AutonomousExadataInfrastructureSummary
from .backup import Backup
from .backup_summary import BackupSummary
from .change_compartment_details import ChangeCompartmentDetails
from .complete_external_backup_job_details import CompleteExternalBackupJobDetails
from .create_autonomous_container_database_details import CreateAutonomousContainerDatabaseDetails
from .create_autonomous_data_warehouse_backup_details import CreateAutonomousDataWarehouseBackupDetails
from .create_autonomous_data_warehouse_details import CreateAutonomousDataWarehouseDetails
from .create_autonomous_database_backup_details import CreateAutonomousDatabaseBackupDetails
from .create_autonomous_database_base import CreateAutonomousDatabaseBase
from .create_autonomous_database_clone_details import CreateAutonomousDatabaseCloneDetails
from .create_autonomous_database_details import CreateAutonomousDatabaseDetails
from .create_backup_details import CreateBackupDetails
from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from .create_data_guard_association_to_existing_db_system_details import CreateDataGuardAssociationToExistingDbSystemDetails
from .create_data_guard_association_with_new_db_system_details import CreateDataGuardAssociationWithNewDbSystemDetails
from .create_database_details import CreateDatabaseDetails
from .create_database_from_backup_details import CreateDatabaseFromBackupDetails
from .create_db_home_details import CreateDbHomeDetails
from .create_db_home_from_backup_details import CreateDbHomeFromBackupDetails
from .create_db_home_with_db_system_id_base import CreateDbHomeWithDbSystemIdBase
from .create_db_home_with_db_system_id_details import CreateDbHomeWithDbSystemIdDetails
from .create_db_home_with_db_system_id_from_backup_details import CreateDbHomeWithDbSystemIdFromBackupDetails
from .create_external_backup_job_details import CreateExternalBackupJobDetails
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
from .db_system_shape_summary import DbSystemShapeSummary
from .db_system_summary import DbSystemSummary
from .db_version_summary import DbVersionSummary
from .exadata_iorm_config import ExadataIormConfig
from .exadata_iorm_config_update_details import ExadataIormConfigUpdateDetails
from .external_backup_job import ExternalBackupJob
from .failover_data_guard_association_details import FailoverDataGuardAssociationDetails
from .generate_autonomous_data_warehouse_wallet_details import GenerateAutonomousDataWarehouseWalletDetails
from .generate_autonomous_database_wallet_details import GenerateAutonomousDatabaseWalletDetails
from .launch_autonomous_exadata_infrastructure_details import LaunchAutonomousExadataInfrastructureDetails
from .launch_db_system_base import LaunchDbSystemBase
from .launch_db_system_details import LaunchDbSystemDetails
from .launch_db_system_from_backup_details import LaunchDbSystemFromBackupDetails
from .maintenance_run import MaintenanceRun
from .maintenance_run_summary import MaintenanceRunSummary
from .maintenance_window import MaintenanceWindow
from .month import Month
from .patch import Patch
from .patch_details import PatchDetails
from .patch_history_entry import PatchHistoryEntry
from .patch_history_entry_summary import PatchHistoryEntrySummary
from .patch_summary import PatchSummary
from .reinstate_data_guard_association_details import ReinstateDataGuardAssociationDetails
from .restore_autonomous_data_warehouse_details import RestoreAutonomousDataWarehouseDetails
from .restore_autonomous_database_details import RestoreAutonomousDatabaseDetails
from .restore_database_details import RestoreDatabaseDetails
from .switchover_data_guard_association_details import SwitchoverDataGuardAssociationDetails
from .update_autonomous_container_database_details import UpdateAutonomousContainerDatabaseDetails
from .update_autonomous_data_warehouse_details import UpdateAutonomousDataWarehouseDetails
from .update_autonomous_database_details import UpdateAutonomousDatabaseDetails
from .update_autonomous_exadata_infrastructure_details import UpdateAutonomousExadataInfrastructureDetails
from .update_database_details import UpdateDatabaseDetails
from .update_db_home_details import UpdateDbHomeDetails
from .update_db_system_details import UpdateDbSystemDetails
from .update_maintenance_run_details import UpdateMaintenanceRunDetails

# Maps type names to classes for database services.
database_type_mapping = {
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
    "AutonomousDbPreviewVersionSummary": AutonomousDbPreviewVersionSummary,
    "AutonomousExadataInfrastructure": AutonomousExadataInfrastructure,
    "AutonomousExadataInfrastructureMaintenanceWindow": AutonomousExadataInfrastructureMaintenanceWindow,
    "AutonomousExadataInfrastructureShapeSummary": AutonomousExadataInfrastructureShapeSummary,
    "AutonomousExadataInfrastructureSummary": AutonomousExadataInfrastructureSummary,
    "Backup": Backup,
    "BackupSummary": BackupSummary,
    "ChangeCompartmentDetails": ChangeCompartmentDetails,
    "CompleteExternalBackupJobDetails": CompleteExternalBackupJobDetails,
    "CreateAutonomousContainerDatabaseDetails": CreateAutonomousContainerDatabaseDetails,
    "CreateAutonomousDataWarehouseBackupDetails": CreateAutonomousDataWarehouseBackupDetails,
    "CreateAutonomousDataWarehouseDetails": CreateAutonomousDataWarehouseDetails,
    "CreateAutonomousDatabaseBackupDetails": CreateAutonomousDatabaseBackupDetails,
    "CreateAutonomousDatabaseBase": CreateAutonomousDatabaseBase,
    "CreateAutonomousDatabaseCloneDetails": CreateAutonomousDatabaseCloneDetails,
    "CreateAutonomousDatabaseDetails": CreateAutonomousDatabaseDetails,
    "CreateBackupDetails": CreateBackupDetails,
    "CreateDataGuardAssociationDetails": CreateDataGuardAssociationDetails,
    "CreateDataGuardAssociationToExistingDbSystemDetails": CreateDataGuardAssociationToExistingDbSystemDetails,
    "CreateDataGuardAssociationWithNewDbSystemDetails": CreateDataGuardAssociationWithNewDbSystemDetails,
    "CreateDatabaseDetails": CreateDatabaseDetails,
    "CreateDatabaseFromBackupDetails": CreateDatabaseFromBackupDetails,
    "CreateDbHomeDetails": CreateDbHomeDetails,
    "CreateDbHomeFromBackupDetails": CreateDbHomeFromBackupDetails,
    "CreateDbHomeWithDbSystemIdBase": CreateDbHomeWithDbSystemIdBase,
    "CreateDbHomeWithDbSystemIdDetails": CreateDbHomeWithDbSystemIdDetails,
    "CreateDbHomeWithDbSystemIdFromBackupDetails": CreateDbHomeWithDbSystemIdFromBackupDetails,
    "CreateExternalBackupJobDetails": CreateExternalBackupJobDetails,
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
    "DbSystemShapeSummary": DbSystemShapeSummary,
    "DbSystemSummary": DbSystemSummary,
    "DbVersionSummary": DbVersionSummary,
    "ExadataIormConfig": ExadataIormConfig,
    "ExadataIormConfigUpdateDetails": ExadataIormConfigUpdateDetails,
    "ExternalBackupJob": ExternalBackupJob,
    "FailoverDataGuardAssociationDetails": FailoverDataGuardAssociationDetails,
    "GenerateAutonomousDataWarehouseWalletDetails": GenerateAutonomousDataWarehouseWalletDetails,
    "GenerateAutonomousDatabaseWalletDetails": GenerateAutonomousDatabaseWalletDetails,
    "LaunchAutonomousExadataInfrastructureDetails": LaunchAutonomousExadataInfrastructureDetails,
    "LaunchDbSystemBase": LaunchDbSystemBase,
    "LaunchDbSystemDetails": LaunchDbSystemDetails,
    "LaunchDbSystemFromBackupDetails": LaunchDbSystemFromBackupDetails,
    "MaintenanceRun": MaintenanceRun,
    "MaintenanceRunSummary": MaintenanceRunSummary,
    "MaintenanceWindow": MaintenanceWindow,
    "Month": Month,
    "Patch": Patch,
    "PatchDetails": PatchDetails,
    "PatchHistoryEntry": PatchHistoryEntry,
    "PatchHistoryEntrySummary": PatchHistoryEntrySummary,
    "PatchSummary": PatchSummary,
    "ReinstateDataGuardAssociationDetails": ReinstateDataGuardAssociationDetails,
    "RestoreAutonomousDataWarehouseDetails": RestoreAutonomousDataWarehouseDetails,
    "RestoreAutonomousDatabaseDetails": RestoreAutonomousDatabaseDetails,
    "RestoreDatabaseDetails": RestoreDatabaseDetails,
    "SwitchoverDataGuardAssociationDetails": SwitchoverDataGuardAssociationDetails,
    "UpdateAutonomousContainerDatabaseDetails": UpdateAutonomousContainerDatabaseDetails,
    "UpdateAutonomousDataWarehouseDetails": UpdateAutonomousDataWarehouseDetails,
    "UpdateAutonomousDatabaseDetails": UpdateAutonomousDatabaseDetails,
    "UpdateAutonomousExadataInfrastructureDetails": UpdateAutonomousExadataInfrastructureDetails,
    "UpdateDatabaseDetails": UpdateDatabaseDetails,
    "UpdateDbHomeDetails": UpdateDbHomeDetails,
    "UpdateDbSystemDetails": UpdateDbSystemDetails,
    "UpdateMaintenanceRunDetails": UpdateMaintenanceRunDetails
}
