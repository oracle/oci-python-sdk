# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .autonomous_data_warehouse import AutonomousDataWarehouse
from .autonomous_data_warehouse_backup import AutonomousDataWarehouseBackup
from .autonomous_data_warehouse_backup_summary import AutonomousDataWarehouseBackupSummary
from .autonomous_data_warehouse_connection_strings import AutonomousDataWarehouseConnectionStrings
from .autonomous_data_warehouse_summary import AutonomousDataWarehouseSummary
from .autonomous_database import AutonomousDatabase
from .autonomous_database_backup import AutonomousDatabaseBackup
from .autonomous_database_backup_summary import AutonomousDatabaseBackupSummary
from .autonomous_database_connection_strings import AutonomousDatabaseConnectionStrings
from .autonomous_database_summary import AutonomousDatabaseSummary
from .backup import Backup
from .backup_summary import BackupSummary
from .complete_external_backup_job_details import CompleteExternalBackupJobDetails
from .create_autonomous_data_warehouse_backup_details import CreateAutonomousDataWarehouseBackupDetails
from .create_autonomous_data_warehouse_details import CreateAutonomousDataWarehouseDetails
from .create_autonomous_database_backup_details import CreateAutonomousDatabaseBackupDetails
from .create_autonomous_database_details import CreateAutonomousDatabaseDetails
from .create_backup_details import CreateBackupDetails
from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from .create_data_guard_association_to_existing_db_system_details import CreateDataGuardAssociationToExistingDbSystemDetails
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
from .database_summary import DatabaseSummary
from .db_backup_config import DbBackupConfig
from .db_home import DbHome
from .db_home_summary import DbHomeSummary
from .db_node import DbNode
from .db_node_summary import DbNodeSummary
from .db_system import DbSystem
from .db_system_shape_summary import DbSystemShapeSummary
from .db_system_summary import DbSystemSummary
from .db_version_summary import DbVersionSummary
from .external_backup_job import ExternalBackupJob
from .failover_data_guard_association_details import FailoverDataGuardAssociationDetails
from .generate_autonomous_data_warehouse_wallet_details import GenerateAutonomousDataWarehouseWalletDetails
from .generate_autonomous_database_wallet_details import GenerateAutonomousDatabaseWalletDetails
from .launch_db_system_base import LaunchDbSystemBase
from .launch_db_system_details import LaunchDbSystemDetails
from .launch_db_system_from_backup_details import LaunchDbSystemFromBackupDetails
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
from .update_autonomous_data_warehouse_details import UpdateAutonomousDataWarehouseDetails
from .update_autonomous_database_details import UpdateAutonomousDatabaseDetails
from .update_database_details import UpdateDatabaseDetails
from .update_db_home_details import UpdateDbHomeDetails
from .update_db_system_details import UpdateDbSystemDetails

# Maps type names to classes for database services.
database_type_mapping = {
    "AutonomousDataWarehouse": AutonomousDataWarehouse,
    "AutonomousDataWarehouseBackup": AutonomousDataWarehouseBackup,
    "AutonomousDataWarehouseBackupSummary": AutonomousDataWarehouseBackupSummary,
    "AutonomousDataWarehouseConnectionStrings": AutonomousDataWarehouseConnectionStrings,
    "AutonomousDataWarehouseSummary": AutonomousDataWarehouseSummary,
    "AutonomousDatabase": AutonomousDatabase,
    "AutonomousDatabaseBackup": AutonomousDatabaseBackup,
    "AutonomousDatabaseBackupSummary": AutonomousDatabaseBackupSummary,
    "AutonomousDatabaseConnectionStrings": AutonomousDatabaseConnectionStrings,
    "AutonomousDatabaseSummary": AutonomousDatabaseSummary,
    "Backup": Backup,
    "BackupSummary": BackupSummary,
    "CompleteExternalBackupJobDetails": CompleteExternalBackupJobDetails,
    "CreateAutonomousDataWarehouseBackupDetails": CreateAutonomousDataWarehouseBackupDetails,
    "CreateAutonomousDataWarehouseDetails": CreateAutonomousDataWarehouseDetails,
    "CreateAutonomousDatabaseBackupDetails": CreateAutonomousDatabaseBackupDetails,
    "CreateAutonomousDatabaseDetails": CreateAutonomousDatabaseDetails,
    "CreateBackupDetails": CreateBackupDetails,
    "CreateDataGuardAssociationDetails": CreateDataGuardAssociationDetails,
    "CreateDataGuardAssociationToExistingDbSystemDetails": CreateDataGuardAssociationToExistingDbSystemDetails,
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
    "DatabaseSummary": DatabaseSummary,
    "DbBackupConfig": DbBackupConfig,
    "DbHome": DbHome,
    "DbHomeSummary": DbHomeSummary,
    "DbNode": DbNode,
    "DbNodeSummary": DbNodeSummary,
    "DbSystem": DbSystem,
    "DbSystemShapeSummary": DbSystemShapeSummary,
    "DbSystemSummary": DbSystemSummary,
    "DbVersionSummary": DbVersionSummary,
    "ExternalBackupJob": ExternalBackupJob,
    "FailoverDataGuardAssociationDetails": FailoverDataGuardAssociationDetails,
    "GenerateAutonomousDataWarehouseWalletDetails": GenerateAutonomousDataWarehouseWalletDetails,
    "GenerateAutonomousDatabaseWalletDetails": GenerateAutonomousDatabaseWalletDetails,
    "LaunchDbSystemBase": LaunchDbSystemBase,
    "LaunchDbSystemDetails": LaunchDbSystemDetails,
    "LaunchDbSystemFromBackupDetails": LaunchDbSystemFromBackupDetails,
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
    "UpdateAutonomousDataWarehouseDetails": UpdateAutonomousDataWarehouseDetails,
    "UpdateAutonomousDatabaseDetails": UpdateAutonomousDatabaseDetails,
    "UpdateDatabaseDetails": UpdateDatabaseDetails,
    "UpdateDbHomeDetails": UpdateDbHomeDetails,
    "UpdateDbSystemDetails": UpdateDbSystemDetails
}
