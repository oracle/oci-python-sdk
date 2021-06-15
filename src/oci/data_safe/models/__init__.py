# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activate_target_database_details import ActivateTargetDatabaseDetails
from .autonomous_database_details import AutonomousDatabaseDetails
from .change_data_safe_private_endpoint_compartment_details import ChangeDataSafePrivateEndpointCompartmentDetails
from .change_on_prem_connector_compartment_details import ChangeOnPremConnectorCompartmentDetails
from .change_target_database_compartment_details import ChangeTargetDatabaseCompartmentDetails
from .connection_option import ConnectionOption
from .create_data_safe_private_endpoint_details import CreateDataSafePrivateEndpointDetails
from .create_on_prem_connector_details import CreateOnPremConnectorDetails
from .create_target_database_details import CreateTargetDatabaseDetails
from .credentials import Credentials
from .data_safe_configuration import DataSafeConfiguration
from .data_safe_private_endpoint import DataSafePrivateEndpoint
from .data_safe_private_endpoint_summary import DataSafePrivateEndpointSummary
from .database_cloud_service_details import DatabaseCloudServiceDetails
from .database_details import DatabaseDetails
from .enable_data_safe_configuration_details import EnableDataSafeConfigurationDetails
from .generate_on_prem_connector_configuration_details import GenerateOnPremConnectorConfigurationDetails
from .installed_database_details import InstalledDatabaseDetails
from .on_prem_connector import OnPremConnector
from .on_prem_connector_summary import OnPremConnectorSummary
from .on_premise_connector import OnPremiseConnector
from .private_endpoint import PrivateEndpoint
from .target_database import TargetDatabase
from .target_database_summary import TargetDatabaseSummary
from .tls_config import TlsConfig
from .update_data_safe_private_endpoint_details import UpdateDataSafePrivateEndpointDetails
from .update_on_prem_connector_details import UpdateOnPremConnectorDetails
from .update_on_prem_connector_wallet_details import UpdateOnPremConnectorWalletDetails
from .update_target_database_details import UpdateTargetDatabaseDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for data_safe services.
data_safe_type_mapping = {
    "ActivateTargetDatabaseDetails": ActivateTargetDatabaseDetails,
    "AutonomousDatabaseDetails": AutonomousDatabaseDetails,
    "ChangeDataSafePrivateEndpointCompartmentDetails": ChangeDataSafePrivateEndpointCompartmentDetails,
    "ChangeOnPremConnectorCompartmentDetails": ChangeOnPremConnectorCompartmentDetails,
    "ChangeTargetDatabaseCompartmentDetails": ChangeTargetDatabaseCompartmentDetails,
    "ConnectionOption": ConnectionOption,
    "CreateDataSafePrivateEndpointDetails": CreateDataSafePrivateEndpointDetails,
    "CreateOnPremConnectorDetails": CreateOnPremConnectorDetails,
    "CreateTargetDatabaseDetails": CreateTargetDatabaseDetails,
    "Credentials": Credentials,
    "DataSafeConfiguration": DataSafeConfiguration,
    "DataSafePrivateEndpoint": DataSafePrivateEndpoint,
    "DataSafePrivateEndpointSummary": DataSafePrivateEndpointSummary,
    "DatabaseCloudServiceDetails": DatabaseCloudServiceDetails,
    "DatabaseDetails": DatabaseDetails,
    "EnableDataSafeConfigurationDetails": EnableDataSafeConfigurationDetails,
    "GenerateOnPremConnectorConfigurationDetails": GenerateOnPremConnectorConfigurationDetails,
    "InstalledDatabaseDetails": InstalledDatabaseDetails,
    "OnPremConnector": OnPremConnector,
    "OnPremConnectorSummary": OnPremConnectorSummary,
    "OnPremiseConnector": OnPremiseConnector,
    "PrivateEndpoint": PrivateEndpoint,
    "TargetDatabase": TargetDatabase,
    "TargetDatabaseSummary": TargetDatabaseSummary,
    "TlsConfig": TlsConfig,
    "UpdateDataSafePrivateEndpointDetails": UpdateDataSafePrivateEndpointDetails,
    "UpdateOnPremConnectorDetails": UpdateOnPremConnectorDetails,
    "UpdateOnPremConnectorWalletDetails": UpdateOnPremConnectorWalletDetails,
    "UpdateTargetDatabaseDetails": UpdateTargetDatabaseDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
