# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .admin_credentials import AdminCredentials
from .advisor_report import AdvisorReport
from .advisor_report_bucket_details import AdvisorReportBucketDetails
from .advisor_report_location_details import AdvisorReportLocationDetails
from .advisor_settings import AdvisorSettings
from .agent import Agent
from .agent_collection import AgentCollection
from .agent_image_collection import AgentImageCollection
from .agent_image_summary import AgentImageSummary
from .agent_summary import AgentSummary
from .change_agent_compartment_details import ChangeAgentCompartmentDetails
from .change_connection_compartment_details import ChangeConnectionCompartmentDetails
from .change_migration_compartment_details import ChangeMigrationCompartmentDetails
from .clone_migration_details import CloneMigrationDetails
from .connect_descriptor import ConnectDescriptor
from .connection import Connection
from .connection_collection import ConnectionCollection
from .connection_summary import ConnectionSummary
from .create_admin_credentials import CreateAdminCredentials
from .create_advisor_settings import CreateAdvisorSettings
from .create_agent_details import CreateAgentDetails
from .create_connect_descriptor import CreateConnectDescriptor
from .create_connection_details import CreateConnectionDetails
from .create_curl_transfer_details import CreateCurlTransferDetails
from .create_data_pump_parameters import CreateDataPumpParameters
from .create_data_pump_settings import CreateDataPumpSettings
from .create_data_transfer_medium_details import CreateDataTransferMediumDetails
from .create_database_link_details import CreateDatabaseLinkDetails
from .create_directory_object import CreateDirectoryObject
from .create_dump_transfer_details import CreateDumpTransferDetails
from .create_extract import CreateExtract
from .create_golden_gate_details import CreateGoldenGateDetails
from .create_golden_gate_hub import CreateGoldenGateHub
from .create_golden_gate_settings import CreateGoldenGateSettings
from .create_host_dump_transfer_details import CreateHostDumpTransferDetails
from .create_migration_details import CreateMigrationDetails
from .create_object_store_bucket import CreateObjectStoreBucket
from .create_oci_cli_dump_transfer_details import CreateOciCliDumpTransferDetails
from .create_private_endpoint import CreatePrivateEndpoint
from .create_replicat import CreateReplicat
from .create_ssh_details import CreateSshDetails
from .create_vault_details import CreateVaultDetails
from .curl_transfer_details import CurlTransferDetails
from .data_pump_parameters import DataPumpParameters
from .data_pump_settings import DataPumpSettings
from .data_transfer_medium_details import DataTransferMediumDetails
from .database_link_details import DatabaseLinkDetails
from .database_object import DatabaseObject
from .directory_object import DirectoryObject
from .dump_transfer_details import DumpTransferDetails
from .extract import Extract
from .generate_token import GenerateToken
from .golden_gate_details import GoldenGateDetails
from .golden_gate_hub import GoldenGateHub
from .golden_gate_settings import GoldenGateSettings
from .host_dump_transfer_details import HostDumpTransferDetails
from .job import Job
from .job_collection import JobCollection
from .job_output_summary import JobOutputSummary
from .job_output_summary_collection import JobOutputSummaryCollection
from .job_summary import JobSummary
from .log_location_bucket_details import LogLocationBucketDetails
from .metadata_remap import MetadataRemap
from .migration import Migration
from .migration_collection import MigrationCollection
from .migration_job_progress_resource import MigrationJobProgressResource
from .migration_job_progress_summary import MigrationJobProgressSummary
from .migration_object_type_summary import MigrationObjectTypeSummary
from .migration_object_type_summary_collection import MigrationObjectTypeSummaryCollection
from .migration_phase_collection import MigrationPhaseCollection
from .migration_phase_summary import MigrationPhaseSummary
from .migration_summary import MigrationSummary
from .object_store_bucket import ObjectStoreBucket
from .oci_cli_dump_transfer_details import OciCliDumpTransferDetails
from .par_link import ParLink
from .phase_extract_entry import PhaseExtractEntry
from .phase_status import PhaseStatus
from .private_endpoint_details import PrivateEndpointDetails
from .replicat import Replicat
from .resume_job_details import ResumeJobDetails
from .ssh_details import SshDetails
from .start_migration_details import StartMigrationDetails
from .unsupported_database_object import UnsupportedDatabaseObject
from .update_admin_credentials import UpdateAdminCredentials
from .update_advisor_settings import UpdateAdvisorSettings
from .update_agent_details import UpdateAgentDetails
from .update_connect_descriptor import UpdateConnectDescriptor
from .update_connection_details import UpdateConnectionDetails
from .update_curl_transfer_details import UpdateCurlTransferDetails
from .update_data_pump_parameters import UpdateDataPumpParameters
from .update_data_pump_settings import UpdateDataPumpSettings
from .update_data_transfer_medium_details import UpdateDataTransferMediumDetails
from .update_database_link_details import UpdateDatabaseLinkDetails
from .update_directory_object import UpdateDirectoryObject
from .update_dump_transfer_details import UpdateDumpTransferDetails
from .update_extract import UpdateExtract
from .update_golden_gate_details import UpdateGoldenGateDetails
from .update_golden_gate_hub import UpdateGoldenGateHub
from .update_golden_gate_settings import UpdateGoldenGateSettings
from .update_host_dump_transfer_details import UpdateHostDumpTransferDetails
from .update_job_details import UpdateJobDetails
from .update_migration_details import UpdateMigrationDetails
from .update_object_store_bucket import UpdateObjectStoreBucket
from .update_oci_cli_dump_transfer_details import UpdateOciCliDumpTransferDetails
from .update_private_endpoint import UpdatePrivateEndpoint
from .update_replicat import UpdateReplicat
from .update_ssh_details import UpdateSshDetails
from .update_vault_details import UpdateVaultDetails
from .vault_details import VaultDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for database_migration services.
database_migration_type_mapping = {
    "AdminCredentials": AdminCredentials,
    "AdvisorReport": AdvisorReport,
    "AdvisorReportBucketDetails": AdvisorReportBucketDetails,
    "AdvisorReportLocationDetails": AdvisorReportLocationDetails,
    "AdvisorSettings": AdvisorSettings,
    "Agent": Agent,
    "AgentCollection": AgentCollection,
    "AgentImageCollection": AgentImageCollection,
    "AgentImageSummary": AgentImageSummary,
    "AgentSummary": AgentSummary,
    "ChangeAgentCompartmentDetails": ChangeAgentCompartmentDetails,
    "ChangeConnectionCompartmentDetails": ChangeConnectionCompartmentDetails,
    "ChangeMigrationCompartmentDetails": ChangeMigrationCompartmentDetails,
    "CloneMigrationDetails": CloneMigrationDetails,
    "ConnectDescriptor": ConnectDescriptor,
    "Connection": Connection,
    "ConnectionCollection": ConnectionCollection,
    "ConnectionSummary": ConnectionSummary,
    "CreateAdminCredentials": CreateAdminCredentials,
    "CreateAdvisorSettings": CreateAdvisorSettings,
    "CreateAgentDetails": CreateAgentDetails,
    "CreateConnectDescriptor": CreateConnectDescriptor,
    "CreateConnectionDetails": CreateConnectionDetails,
    "CreateCurlTransferDetails": CreateCurlTransferDetails,
    "CreateDataPumpParameters": CreateDataPumpParameters,
    "CreateDataPumpSettings": CreateDataPumpSettings,
    "CreateDataTransferMediumDetails": CreateDataTransferMediumDetails,
    "CreateDatabaseLinkDetails": CreateDatabaseLinkDetails,
    "CreateDirectoryObject": CreateDirectoryObject,
    "CreateDumpTransferDetails": CreateDumpTransferDetails,
    "CreateExtract": CreateExtract,
    "CreateGoldenGateDetails": CreateGoldenGateDetails,
    "CreateGoldenGateHub": CreateGoldenGateHub,
    "CreateGoldenGateSettings": CreateGoldenGateSettings,
    "CreateHostDumpTransferDetails": CreateHostDumpTransferDetails,
    "CreateMigrationDetails": CreateMigrationDetails,
    "CreateObjectStoreBucket": CreateObjectStoreBucket,
    "CreateOciCliDumpTransferDetails": CreateOciCliDumpTransferDetails,
    "CreatePrivateEndpoint": CreatePrivateEndpoint,
    "CreateReplicat": CreateReplicat,
    "CreateSshDetails": CreateSshDetails,
    "CreateVaultDetails": CreateVaultDetails,
    "CurlTransferDetails": CurlTransferDetails,
    "DataPumpParameters": DataPumpParameters,
    "DataPumpSettings": DataPumpSettings,
    "DataTransferMediumDetails": DataTransferMediumDetails,
    "DatabaseLinkDetails": DatabaseLinkDetails,
    "DatabaseObject": DatabaseObject,
    "DirectoryObject": DirectoryObject,
    "DumpTransferDetails": DumpTransferDetails,
    "Extract": Extract,
    "GenerateToken": GenerateToken,
    "GoldenGateDetails": GoldenGateDetails,
    "GoldenGateHub": GoldenGateHub,
    "GoldenGateSettings": GoldenGateSettings,
    "HostDumpTransferDetails": HostDumpTransferDetails,
    "Job": Job,
    "JobCollection": JobCollection,
    "JobOutputSummary": JobOutputSummary,
    "JobOutputSummaryCollection": JobOutputSummaryCollection,
    "JobSummary": JobSummary,
    "LogLocationBucketDetails": LogLocationBucketDetails,
    "MetadataRemap": MetadataRemap,
    "Migration": Migration,
    "MigrationCollection": MigrationCollection,
    "MigrationJobProgressResource": MigrationJobProgressResource,
    "MigrationJobProgressSummary": MigrationJobProgressSummary,
    "MigrationObjectTypeSummary": MigrationObjectTypeSummary,
    "MigrationObjectTypeSummaryCollection": MigrationObjectTypeSummaryCollection,
    "MigrationPhaseCollection": MigrationPhaseCollection,
    "MigrationPhaseSummary": MigrationPhaseSummary,
    "MigrationSummary": MigrationSummary,
    "ObjectStoreBucket": ObjectStoreBucket,
    "OciCliDumpTransferDetails": OciCliDumpTransferDetails,
    "ParLink": ParLink,
    "PhaseExtractEntry": PhaseExtractEntry,
    "PhaseStatus": PhaseStatus,
    "PrivateEndpointDetails": PrivateEndpointDetails,
    "Replicat": Replicat,
    "ResumeJobDetails": ResumeJobDetails,
    "SshDetails": SshDetails,
    "StartMigrationDetails": StartMigrationDetails,
    "UnsupportedDatabaseObject": UnsupportedDatabaseObject,
    "UpdateAdminCredentials": UpdateAdminCredentials,
    "UpdateAdvisorSettings": UpdateAdvisorSettings,
    "UpdateAgentDetails": UpdateAgentDetails,
    "UpdateConnectDescriptor": UpdateConnectDescriptor,
    "UpdateConnectionDetails": UpdateConnectionDetails,
    "UpdateCurlTransferDetails": UpdateCurlTransferDetails,
    "UpdateDataPumpParameters": UpdateDataPumpParameters,
    "UpdateDataPumpSettings": UpdateDataPumpSettings,
    "UpdateDataTransferMediumDetails": UpdateDataTransferMediumDetails,
    "UpdateDatabaseLinkDetails": UpdateDatabaseLinkDetails,
    "UpdateDirectoryObject": UpdateDirectoryObject,
    "UpdateDumpTransferDetails": UpdateDumpTransferDetails,
    "UpdateExtract": UpdateExtract,
    "UpdateGoldenGateDetails": UpdateGoldenGateDetails,
    "UpdateGoldenGateHub": UpdateGoldenGateHub,
    "UpdateGoldenGateSettings": UpdateGoldenGateSettings,
    "UpdateHostDumpTransferDetails": UpdateHostDumpTransferDetails,
    "UpdateJobDetails": UpdateJobDetails,
    "UpdateMigrationDetails": UpdateMigrationDetails,
    "UpdateObjectStoreBucket": UpdateObjectStoreBucket,
    "UpdateOciCliDumpTransferDetails": UpdateOciCliDumpTransferDetails,
    "UpdatePrivateEndpoint": UpdatePrivateEndpoint,
    "UpdateReplicat": UpdateReplicat,
    "UpdateSshDetails": UpdateSshDetails,
    "UpdateVaultDetails": UpdateVaultDetails,
    "VaultDetails": VaultDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
