# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .azure_data_lake_storage_connection import AzureDataLakeStorageConnection
from .azure_data_lake_storage_connection_summary import AzureDataLakeStorageConnectionSummary
from .azure_synapse_connection import AzureSynapseConnection
from .azure_synapse_connection_summary import AzureSynapseConnectionSummary
from .cancel_deployment_backup_details import CancelDeploymentBackupDetails
from .change_connection_compartment_details import ChangeConnectionCompartmentDetails
from .change_database_registration_compartment_details import ChangeDatabaseRegistrationCompartmentDetails
from .change_deployment_backup_compartment_details import ChangeDeploymentBackupCompartmentDetails
from .change_deployment_compartment_details import ChangeDeploymentCompartmentDetails
from .collect_deployment_diagnostic_details import CollectDeploymentDiagnosticDetails
from .connection import Connection
from .connection_assignment import ConnectionAssignment
from .connection_assignment_collection import ConnectionAssignmentCollection
from .connection_assignment_summary import ConnectionAssignmentSummary
from .connection_collection import ConnectionCollection
from .connection_summary import ConnectionSummary
from .create_azure_data_lake_storage_connection_details import CreateAzureDataLakeStorageConnectionDetails
from .create_azure_synapse_connection_details import CreateAzureSynapseConnectionDetails
from .create_connection_assignment_details import CreateConnectionAssignmentDetails
from .create_connection_details import CreateConnectionDetails
from .create_database_registration_details import CreateDatabaseRegistrationDetails
from .create_deployment_backup_details import CreateDeploymentBackupDetails
from .create_deployment_details import CreateDeploymentDetails
from .create_golden_gate_connection_details import CreateGoldenGateConnectionDetails
from .create_kafka_connection_details import CreateKafkaConnectionDetails
from .create_kafka_schema_registry_connection_details import CreateKafkaSchemaRegistryConnectionDetails
from .create_mysql_connection_details import CreateMysqlConnectionDetails
from .create_oci_object_storage_connection_details import CreateOciObjectStorageConnectionDetails
from .create_ogg_deployment_details import CreateOggDeploymentDetails
from .create_oracle_connection_details import CreateOracleConnectionDetails
from .create_postgresql_connection_details import CreatePostgresqlConnectionDetails
from .database_registration import DatabaseRegistration
from .database_registration_collection import DatabaseRegistrationCollection
from .database_registration_summary import DatabaseRegistrationSummary
from .default_cancel_deployment_backup_details import DefaultCancelDeploymentBackupDetails
from .default_restore_deployment_details import DefaultRestoreDeploymentDetails
from .default_start_deployment_details import DefaultStartDeploymentDetails
from .default_stop_deployment_details import DefaultStopDeploymentDetails
from .deployment import Deployment
from .deployment_backup import DeploymentBackup
from .deployment_backup_collection import DeploymentBackupCollection
from .deployment_backup_summary import DeploymentBackupSummary
from .deployment_collection import DeploymentCollection
from .deployment_diagnostic_data import DeploymentDiagnosticData
from .deployment_message_collection import DeploymentMessageCollection
from .deployment_summary import DeploymentSummary
from .deployment_type_collection import DeploymentTypeCollection
from .deployment_type_summary import DeploymentTypeSummary
from .deployment_upgrade import DeploymentUpgrade
from .deployment_upgrade_collection import DeploymentUpgradeCollection
from .deployment_upgrade_summary import DeploymentUpgradeSummary
from .golden_gate_connection import GoldenGateConnection
from .golden_gate_connection_summary import GoldenGateConnectionSummary
from .ingress_ip_details import IngressIpDetails
from .kafka_bootstrap_server import KafkaBootstrapServer
from .kafka_connection import KafkaConnection
from .kafka_connection_summary import KafkaConnectionSummary
from .kafka_schema_registry_connection import KafkaSchemaRegistryConnection
from .kafka_schema_registry_connection_summary import KafkaSchemaRegistryConnectionSummary
from .message_summary import MessageSummary
from .mysql_connection import MysqlConnection
from .mysql_connection_summary import MysqlConnectionSummary
from .name_value_pair import NameValuePair
from .oci_object_storage_connection import OciObjectStorageConnection
from .oci_object_storage_connection_summary import OciObjectStorageConnectionSummary
from .ogg_deployment import OggDeployment
from .oracle_connection import OracleConnection
from .oracle_connection_summary import OracleConnectionSummary
from .postgresql_connection import PostgresqlConnection
from .postgresql_connection_summary import PostgresqlConnectionSummary
from .restore_deployment_details import RestoreDeploymentDetails
from .start_deployment_details import StartDeploymentDetails
from .stop_deployment_details import StopDeploymentDetails
from .trail_file_collection import TrailFileCollection
from .trail_file_summary import TrailFileSummary
from .trail_sequence_collection import TrailSequenceCollection
from .trail_sequence_summary import TrailSequenceSummary
from .update_azure_data_lake_storage_connection_details import UpdateAzureDataLakeStorageConnectionDetails
from .update_azure_synapse_connection_details import UpdateAzureSynapseConnectionDetails
from .update_connection_details import UpdateConnectionDetails
from .update_database_registration_details import UpdateDatabaseRegistrationDetails
from .update_deployment_backup_details import UpdateDeploymentBackupDetails
from .update_deployment_details import UpdateDeploymentDetails
from .update_golden_gate_connection_details import UpdateGoldenGateConnectionDetails
from .update_kafka_connection_details import UpdateKafkaConnectionDetails
from .update_kafka_schema_registry_connection_details import UpdateKafkaSchemaRegistryConnectionDetails
from .update_mysql_connection_details import UpdateMysqlConnectionDetails
from .update_oci_object_storage_connection_details import UpdateOciObjectStorageConnectionDetails
from .update_ogg_deployment_details import UpdateOggDeploymentDetails
from .update_oracle_connection_details import UpdateOracleConnectionDetails
from .update_postgresql_connection_details import UpdatePostgresqlConnectionDetails
from .upgrade_deployment_current_release_details import UpgradeDeploymentCurrentReleaseDetails
from .upgrade_deployment_details import UpgradeDeploymentDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource

# Maps type names to classes for golden_gate services.
golden_gate_type_mapping = {
    "AzureDataLakeStorageConnection": AzureDataLakeStorageConnection,
    "AzureDataLakeStorageConnectionSummary": AzureDataLakeStorageConnectionSummary,
    "AzureSynapseConnection": AzureSynapseConnection,
    "AzureSynapseConnectionSummary": AzureSynapseConnectionSummary,
    "CancelDeploymentBackupDetails": CancelDeploymentBackupDetails,
    "ChangeConnectionCompartmentDetails": ChangeConnectionCompartmentDetails,
    "ChangeDatabaseRegistrationCompartmentDetails": ChangeDatabaseRegistrationCompartmentDetails,
    "ChangeDeploymentBackupCompartmentDetails": ChangeDeploymentBackupCompartmentDetails,
    "ChangeDeploymentCompartmentDetails": ChangeDeploymentCompartmentDetails,
    "CollectDeploymentDiagnosticDetails": CollectDeploymentDiagnosticDetails,
    "Connection": Connection,
    "ConnectionAssignment": ConnectionAssignment,
    "ConnectionAssignmentCollection": ConnectionAssignmentCollection,
    "ConnectionAssignmentSummary": ConnectionAssignmentSummary,
    "ConnectionCollection": ConnectionCollection,
    "ConnectionSummary": ConnectionSummary,
    "CreateAzureDataLakeStorageConnectionDetails": CreateAzureDataLakeStorageConnectionDetails,
    "CreateAzureSynapseConnectionDetails": CreateAzureSynapseConnectionDetails,
    "CreateConnectionAssignmentDetails": CreateConnectionAssignmentDetails,
    "CreateConnectionDetails": CreateConnectionDetails,
    "CreateDatabaseRegistrationDetails": CreateDatabaseRegistrationDetails,
    "CreateDeploymentBackupDetails": CreateDeploymentBackupDetails,
    "CreateDeploymentDetails": CreateDeploymentDetails,
    "CreateGoldenGateConnectionDetails": CreateGoldenGateConnectionDetails,
    "CreateKafkaConnectionDetails": CreateKafkaConnectionDetails,
    "CreateKafkaSchemaRegistryConnectionDetails": CreateKafkaSchemaRegistryConnectionDetails,
    "CreateMysqlConnectionDetails": CreateMysqlConnectionDetails,
    "CreateOciObjectStorageConnectionDetails": CreateOciObjectStorageConnectionDetails,
    "CreateOggDeploymentDetails": CreateOggDeploymentDetails,
    "CreateOracleConnectionDetails": CreateOracleConnectionDetails,
    "CreatePostgresqlConnectionDetails": CreatePostgresqlConnectionDetails,
    "DatabaseRegistration": DatabaseRegistration,
    "DatabaseRegistrationCollection": DatabaseRegistrationCollection,
    "DatabaseRegistrationSummary": DatabaseRegistrationSummary,
    "DefaultCancelDeploymentBackupDetails": DefaultCancelDeploymentBackupDetails,
    "DefaultRestoreDeploymentDetails": DefaultRestoreDeploymentDetails,
    "DefaultStartDeploymentDetails": DefaultStartDeploymentDetails,
    "DefaultStopDeploymentDetails": DefaultStopDeploymentDetails,
    "Deployment": Deployment,
    "DeploymentBackup": DeploymentBackup,
    "DeploymentBackupCollection": DeploymentBackupCollection,
    "DeploymentBackupSummary": DeploymentBackupSummary,
    "DeploymentCollection": DeploymentCollection,
    "DeploymentDiagnosticData": DeploymentDiagnosticData,
    "DeploymentMessageCollection": DeploymentMessageCollection,
    "DeploymentSummary": DeploymentSummary,
    "DeploymentTypeCollection": DeploymentTypeCollection,
    "DeploymentTypeSummary": DeploymentTypeSummary,
    "DeploymentUpgrade": DeploymentUpgrade,
    "DeploymentUpgradeCollection": DeploymentUpgradeCollection,
    "DeploymentUpgradeSummary": DeploymentUpgradeSummary,
    "GoldenGateConnection": GoldenGateConnection,
    "GoldenGateConnectionSummary": GoldenGateConnectionSummary,
    "IngressIpDetails": IngressIpDetails,
    "KafkaBootstrapServer": KafkaBootstrapServer,
    "KafkaConnection": KafkaConnection,
    "KafkaConnectionSummary": KafkaConnectionSummary,
    "KafkaSchemaRegistryConnection": KafkaSchemaRegistryConnection,
    "KafkaSchemaRegistryConnectionSummary": KafkaSchemaRegistryConnectionSummary,
    "MessageSummary": MessageSummary,
    "MysqlConnection": MysqlConnection,
    "MysqlConnectionSummary": MysqlConnectionSummary,
    "NameValuePair": NameValuePair,
    "OciObjectStorageConnection": OciObjectStorageConnection,
    "OciObjectStorageConnectionSummary": OciObjectStorageConnectionSummary,
    "OggDeployment": OggDeployment,
    "OracleConnection": OracleConnection,
    "OracleConnectionSummary": OracleConnectionSummary,
    "PostgresqlConnection": PostgresqlConnection,
    "PostgresqlConnectionSummary": PostgresqlConnectionSummary,
    "RestoreDeploymentDetails": RestoreDeploymentDetails,
    "StartDeploymentDetails": StartDeploymentDetails,
    "StopDeploymentDetails": StopDeploymentDetails,
    "TrailFileCollection": TrailFileCollection,
    "TrailFileSummary": TrailFileSummary,
    "TrailSequenceCollection": TrailSequenceCollection,
    "TrailSequenceSummary": TrailSequenceSummary,
    "UpdateAzureDataLakeStorageConnectionDetails": UpdateAzureDataLakeStorageConnectionDetails,
    "UpdateAzureSynapseConnectionDetails": UpdateAzureSynapseConnectionDetails,
    "UpdateConnectionDetails": UpdateConnectionDetails,
    "UpdateDatabaseRegistrationDetails": UpdateDatabaseRegistrationDetails,
    "UpdateDeploymentBackupDetails": UpdateDeploymentBackupDetails,
    "UpdateDeploymentDetails": UpdateDeploymentDetails,
    "UpdateGoldenGateConnectionDetails": UpdateGoldenGateConnectionDetails,
    "UpdateKafkaConnectionDetails": UpdateKafkaConnectionDetails,
    "UpdateKafkaSchemaRegistryConnectionDetails": UpdateKafkaSchemaRegistryConnectionDetails,
    "UpdateMysqlConnectionDetails": UpdateMysqlConnectionDetails,
    "UpdateOciObjectStorageConnectionDetails": UpdateOciObjectStorageConnectionDetails,
    "UpdateOggDeploymentDetails": UpdateOggDeploymentDetails,
    "UpdateOracleConnectionDetails": UpdateOracleConnectionDetails,
    "UpdatePostgresqlConnectionDetails": UpdatePostgresqlConnectionDetails,
    "UpgradeDeploymentCurrentReleaseDetails": UpgradeDeploymentCurrentReleaseDetails,
    "UpgradeDeploymentDetails": UpgradeDeploymentDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource
}
