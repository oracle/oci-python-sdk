# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .backup import Backup
from .backup_policy import BackupPolicy
from .backup_summary import BackupSummary
from .configuration import Configuration
from .configuration_summary import ConfigurationSummary
from .configuration_variables import ConfigurationVariables
from .create_backup_details import CreateBackupDetails
from .create_backup_policy_details import CreateBackupPolicyDetails
from .create_configuration_details import CreateConfigurationDetails
from .create_db_system_details import CreateDbSystemDetails
from .create_db_system_source_details import CreateDbSystemSourceDetails
from .create_db_system_source_from_backup_details import CreateDbSystemSourceFromBackupDetails
from .create_db_system_source_import_from_url_details import CreateDbSystemSourceImportFromUrlDetails
from .create_maintenance_details import CreateMaintenanceDetails
from .db_system import DbSystem
from .db_system_endpoint import DbSystemEndpoint
from .db_system_source import DbSystemSource
from .db_system_source_from_backup import DbSystemSourceFromBackup
from .db_system_source_import_from_url import DbSystemSourceImportFromUrl
from .db_system_summary import DbSystemSummary
from .maintenance_details import MaintenanceDetails
from .restart_db_system_details import RestartDbSystemDetails
from .shape_summary import ShapeSummary
from .stop_db_system_details import StopDbSystemDetails
from .update_backup_details import UpdateBackupDetails
from .update_backup_policy_details import UpdateBackupPolicyDetails
from .update_configuration_details import UpdateConfigurationDetails
from .update_db_system_details import UpdateDbSystemDetails
from .update_maintenance_details import UpdateMaintenanceDetails
from .version import Version
from .version_summary import VersionSummary
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for mysql services.
mysql_type_mapping = {
    "Backup": Backup,
    "BackupPolicy": BackupPolicy,
    "BackupSummary": BackupSummary,
    "Configuration": Configuration,
    "ConfigurationSummary": ConfigurationSummary,
    "ConfigurationVariables": ConfigurationVariables,
    "CreateBackupDetails": CreateBackupDetails,
    "CreateBackupPolicyDetails": CreateBackupPolicyDetails,
    "CreateConfigurationDetails": CreateConfigurationDetails,
    "CreateDbSystemDetails": CreateDbSystemDetails,
    "CreateDbSystemSourceDetails": CreateDbSystemSourceDetails,
    "CreateDbSystemSourceFromBackupDetails": CreateDbSystemSourceFromBackupDetails,
    "CreateDbSystemSourceImportFromUrlDetails": CreateDbSystemSourceImportFromUrlDetails,
    "CreateMaintenanceDetails": CreateMaintenanceDetails,
    "DbSystem": DbSystem,
    "DbSystemEndpoint": DbSystemEndpoint,
    "DbSystemSource": DbSystemSource,
    "DbSystemSourceFromBackup": DbSystemSourceFromBackup,
    "DbSystemSourceImportFromUrl": DbSystemSourceImportFromUrl,
    "DbSystemSummary": DbSystemSummary,
    "MaintenanceDetails": MaintenanceDetails,
    "RestartDbSystemDetails": RestartDbSystemDetails,
    "ShapeSummary": ShapeSummary,
    "StopDbSystemDetails": StopDbSystemDetails,
    "UpdateBackupDetails": UpdateBackupDetails,
    "UpdateBackupPolicyDetails": UpdateBackupPolicyDetails,
    "UpdateConfigurationDetails": UpdateConfigurationDetails,
    "UpdateDbSystemDetails": UpdateDbSystemDetails,
    "UpdateMaintenanceDetails": UpdateMaintenanceDetails,
    "Version": Version,
    "VersionSummary": VersionSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
