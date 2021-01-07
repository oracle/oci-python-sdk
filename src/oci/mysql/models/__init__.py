# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_analytics_cluster_details import AddAnalyticsClusterDetails
from .analytics_cluster import AnalyticsCluster
from .analytics_cluster_memory_estimate import AnalyticsClusterMemoryEstimate
from .analytics_cluster_node import AnalyticsClusterNode
from .analytics_cluster_schema_memory_estimate import AnalyticsClusterSchemaMemoryEstimate
from .analytics_cluster_summary import AnalyticsClusterSummary
from .analytics_cluster_table_memory_estimate import AnalyticsClusterTableMemoryEstimate
from .backup import Backup
from .backup_policy import BackupPolicy
from .backup_summary import BackupSummary
from .ca_certificate import CaCertificate
from .channel import Channel
from .channel_source import ChannelSource
from .channel_source_mysql import ChannelSourceMysql
from .channel_summary import ChannelSummary
from .channel_target import ChannelTarget
from .channel_target_db_system import ChannelTargetDbSystem
from .configuration import Configuration
from .configuration_summary import ConfigurationSummary
from .configuration_variables import ConfigurationVariables
from .create_backup_details import CreateBackupDetails
from .create_backup_policy_details import CreateBackupPolicyDetails
from .create_channel_details import CreateChannelDetails
from .create_channel_source_details import CreateChannelSourceDetails
from .create_channel_source_from_mysql_details import CreateChannelSourceFromMysqlDetails
from .create_channel_target_details import CreateChannelTargetDetails
from .create_channel_target_from_db_system_details import CreateChannelTargetFromDbSystemDetails
from .create_configuration_details import CreateConfigurationDetails
from .create_db_system_details import CreateDbSystemDetails
from .create_db_system_source_details import CreateDbSystemSourceDetails
from .create_db_system_source_from_backup_details import CreateDbSystemSourceFromBackupDetails
from .create_db_system_source_from_none_details import CreateDbSystemSourceFromNoneDetails
from .create_db_system_source_import_from_url_details import CreateDbSystemSourceImportFromUrlDetails
from .create_maintenance_details import CreateMaintenanceDetails
from .db_system import DbSystem
from .db_system_endpoint import DbSystemEndpoint
from .db_system_snapshot import DbSystemSnapshot
from .db_system_source import DbSystemSource
from .db_system_source_from_backup import DbSystemSourceFromBackup
from .db_system_source_from_none import DbSystemSourceFromNone
from .db_system_source_import_from_url import DbSystemSourceImportFromUrl
from .db_system_summary import DbSystemSummary
from .maintenance_details import MaintenanceDetails
from .pem_ca_certificate import PemCaCertificate
from .restart_db_system_details import RestartDbSystemDetails
from .shape_summary import ShapeSummary
from .stop_db_system_details import StopDbSystemDetails
from .update_analytics_cluster_details import UpdateAnalyticsClusterDetails
from .update_backup_details import UpdateBackupDetails
from .update_backup_policy_details import UpdateBackupPolicyDetails
from .update_channel_details import UpdateChannelDetails
from .update_channel_source_details import UpdateChannelSourceDetails
from .update_channel_source_from_mysql_details import UpdateChannelSourceFromMysqlDetails
from .update_channel_target_details import UpdateChannelTargetDetails
from .update_channel_target_from_db_system_details import UpdateChannelTargetFromDbSystemDetails
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
    "AddAnalyticsClusterDetails": AddAnalyticsClusterDetails,
    "AnalyticsCluster": AnalyticsCluster,
    "AnalyticsClusterMemoryEstimate": AnalyticsClusterMemoryEstimate,
    "AnalyticsClusterNode": AnalyticsClusterNode,
    "AnalyticsClusterSchemaMemoryEstimate": AnalyticsClusterSchemaMemoryEstimate,
    "AnalyticsClusterSummary": AnalyticsClusterSummary,
    "AnalyticsClusterTableMemoryEstimate": AnalyticsClusterTableMemoryEstimate,
    "Backup": Backup,
    "BackupPolicy": BackupPolicy,
    "BackupSummary": BackupSummary,
    "CaCertificate": CaCertificate,
    "Channel": Channel,
    "ChannelSource": ChannelSource,
    "ChannelSourceMysql": ChannelSourceMysql,
    "ChannelSummary": ChannelSummary,
    "ChannelTarget": ChannelTarget,
    "ChannelTargetDbSystem": ChannelTargetDbSystem,
    "Configuration": Configuration,
    "ConfigurationSummary": ConfigurationSummary,
    "ConfigurationVariables": ConfigurationVariables,
    "CreateBackupDetails": CreateBackupDetails,
    "CreateBackupPolicyDetails": CreateBackupPolicyDetails,
    "CreateChannelDetails": CreateChannelDetails,
    "CreateChannelSourceDetails": CreateChannelSourceDetails,
    "CreateChannelSourceFromMysqlDetails": CreateChannelSourceFromMysqlDetails,
    "CreateChannelTargetDetails": CreateChannelTargetDetails,
    "CreateChannelTargetFromDbSystemDetails": CreateChannelTargetFromDbSystemDetails,
    "CreateConfigurationDetails": CreateConfigurationDetails,
    "CreateDbSystemDetails": CreateDbSystemDetails,
    "CreateDbSystemSourceDetails": CreateDbSystemSourceDetails,
    "CreateDbSystemSourceFromBackupDetails": CreateDbSystemSourceFromBackupDetails,
    "CreateDbSystemSourceFromNoneDetails": CreateDbSystemSourceFromNoneDetails,
    "CreateDbSystemSourceImportFromUrlDetails": CreateDbSystemSourceImportFromUrlDetails,
    "CreateMaintenanceDetails": CreateMaintenanceDetails,
    "DbSystem": DbSystem,
    "DbSystemEndpoint": DbSystemEndpoint,
    "DbSystemSnapshot": DbSystemSnapshot,
    "DbSystemSource": DbSystemSource,
    "DbSystemSourceFromBackup": DbSystemSourceFromBackup,
    "DbSystemSourceFromNone": DbSystemSourceFromNone,
    "DbSystemSourceImportFromUrl": DbSystemSourceImportFromUrl,
    "DbSystemSummary": DbSystemSummary,
    "MaintenanceDetails": MaintenanceDetails,
    "PemCaCertificate": PemCaCertificate,
    "RestartDbSystemDetails": RestartDbSystemDetails,
    "ShapeSummary": ShapeSummary,
    "StopDbSystemDetails": StopDbSystemDetails,
    "UpdateAnalyticsClusterDetails": UpdateAnalyticsClusterDetails,
    "UpdateBackupDetails": UpdateBackupDetails,
    "UpdateBackupPolicyDetails": UpdateBackupPolicyDetails,
    "UpdateChannelDetails": UpdateChannelDetails,
    "UpdateChannelSourceDetails": UpdateChannelSourceDetails,
    "UpdateChannelSourceFromMysqlDetails": UpdateChannelSourceFromMysqlDetails,
    "UpdateChannelTargetDetails": UpdateChannelTargetDetails,
    "UpdateChannelTargetFromDbSystemDetails": UpdateChannelTargetFromDbSystemDetails,
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
