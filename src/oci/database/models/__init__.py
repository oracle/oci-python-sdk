# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .backup import Backup
from .backup_summary import BackupSummary
from .create_backup_details import CreateBackupDetails
from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from .create_data_guard_association_to_existing_db_system_details import CreateDataGuardAssociationToExistingDbSystemDetails
from .create_database_details import CreateDatabaseDetails
from .create_database_from_backup_details import CreateDatabaseFromBackupDetails
from .create_db_home_details import CreateDbHomeDetails
from .create_db_home_with_db_system_id_base import CreateDbHomeWithDbSystemIdBase
from .create_db_home_with_db_system_id_details import CreateDbHomeWithDbSystemIdDetails
from .create_db_home_with_db_system_id_from_backup_details import CreateDbHomeWithDbSystemIdFromBackupDetails
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
from .failover_data_guard_association_details import FailoverDataGuardAssociationDetails
from .launch_db_system_details import LaunchDbSystemDetails
from .patch import Patch
from .patch_details import PatchDetails
from .patch_history_entry import PatchHistoryEntry
from .patch_history_entry_summary import PatchHistoryEntrySummary
from .patch_summary import PatchSummary
from .reinstate_data_guard_association_details import ReinstateDataGuardAssociationDetails
from .restore_database_details import RestoreDatabaseDetails
from .switchover_data_guard_association_details import SwitchoverDataGuardAssociationDetails
from .update_database_details import UpdateDatabaseDetails
from .update_db_home_details import UpdateDbHomeDetails
from .update_db_system_details import UpdateDbSystemDetails

# Maps type names to classes for database services.
database_type_mapping = {
    "Backup": Backup,
    "BackupSummary": BackupSummary,
    "CreateBackupDetails": CreateBackupDetails,
    "CreateDataGuardAssociationDetails": CreateDataGuardAssociationDetails,
    "CreateDataGuardAssociationToExistingDbSystemDetails": CreateDataGuardAssociationToExistingDbSystemDetails,
    "CreateDatabaseDetails": CreateDatabaseDetails,
    "CreateDatabaseFromBackupDetails": CreateDatabaseFromBackupDetails,
    "CreateDbHomeDetails": CreateDbHomeDetails,
    "CreateDbHomeWithDbSystemIdBase": CreateDbHomeWithDbSystemIdBase,
    "CreateDbHomeWithDbSystemIdDetails": CreateDbHomeWithDbSystemIdDetails,
    "CreateDbHomeWithDbSystemIdFromBackupDetails": CreateDbHomeWithDbSystemIdFromBackupDetails,
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
    "FailoverDataGuardAssociationDetails": FailoverDataGuardAssociationDetails,
    "LaunchDbSystemDetails": LaunchDbSystemDetails,
    "Patch": Patch,
    "PatchDetails": PatchDetails,
    "PatchHistoryEntry": PatchHistoryEntry,
    "PatchHistoryEntrySummary": PatchHistoryEntrySummary,
    "PatchSummary": PatchSummary,
    "ReinstateDataGuardAssociationDetails": ReinstateDataGuardAssociationDetails,
    "RestoreDatabaseDetails": RestoreDatabaseDetails,
    "SwitchoverDataGuardAssociationDetails": SwitchoverDataGuardAssociationDetails,
    "UpdateDatabaseDetails": UpdateDatabaseDetails,
    "UpdateDbHomeDetails": UpdateDbHomeDetails,
    "UpdateDbSystemDetails": UpdateDbSystemDetails
}
