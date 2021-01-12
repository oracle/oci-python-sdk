# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_data_safe_private_endpoint_compartment_details import ChangeDataSafePrivateEndpointCompartmentDetails
from .change_on_prem_connector_compartment_details import ChangeOnPremConnectorCompartmentDetails
from .create_data_safe_private_endpoint_details import CreateDataSafePrivateEndpointDetails
from .create_on_prem_connector_details import CreateOnPremConnectorDetails
from .data_safe_configuration import DataSafeConfiguration
from .data_safe_private_endpoint import DataSafePrivateEndpoint
from .data_safe_private_endpoint_summary import DataSafePrivateEndpointSummary
from .enable_data_safe_configuration_details import EnableDataSafeConfigurationDetails
from .generate_on_prem_connector_configuration_details import GenerateOnPremConnectorConfigurationDetails
from .on_prem_connector import OnPremConnector
from .on_prem_connector_summary import OnPremConnectorSummary
from .update_data_safe_private_endpoint_details import UpdateDataSafePrivateEndpointDetails
from .update_on_prem_connector_details import UpdateOnPremConnectorDetails
from .update_on_prem_connector_wallet_details import UpdateOnPremConnectorWalletDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for data_safe services.
data_safe_type_mapping = {
    "ChangeDataSafePrivateEndpointCompartmentDetails": ChangeDataSafePrivateEndpointCompartmentDetails,
    "ChangeOnPremConnectorCompartmentDetails": ChangeOnPremConnectorCompartmentDetails,
    "CreateDataSafePrivateEndpointDetails": CreateDataSafePrivateEndpointDetails,
    "CreateOnPremConnectorDetails": CreateOnPremConnectorDetails,
    "DataSafeConfiguration": DataSafeConfiguration,
    "DataSafePrivateEndpoint": DataSafePrivateEndpoint,
    "DataSafePrivateEndpointSummary": DataSafePrivateEndpointSummary,
    "EnableDataSafeConfigurationDetails": EnableDataSafeConfigurationDetails,
    "GenerateOnPremConnectorConfigurationDetails": GenerateOnPremConnectorConfigurationDetails,
    "OnPremConnector": OnPremConnector,
    "OnPremConnectorSummary": OnPremConnectorSummary,
    "UpdateDataSafePrivateEndpointDetails": UpdateDataSafePrivateEndpointDetails,
    "UpdateOnPremConnectorDetails": UpdateOnPremConnectorDetails,
    "UpdateOnPremConnectorWalletDetails": UpdateOnPremConnectorWalletDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
