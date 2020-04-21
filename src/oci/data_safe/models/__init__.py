# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_data_safe_private_endpoint_compartment_details import ChangeDataSafePrivateEndpointCompartmentDetails
from .create_data_safe_private_endpoint_details import CreateDataSafePrivateEndpointDetails
from .data_safe_configuration import DataSafeConfiguration
from .data_safe_private_endpoint import DataSafePrivateEndpoint
from .data_safe_private_endpoint_summary import DataSafePrivateEndpointSummary
from .enable_data_safe_configuration_details import EnableDataSafeConfigurationDetails
from .update_data_safe_private_endpoint_details import UpdateDataSafePrivateEndpointDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for data_safe services.
data_safe_type_mapping = {
    "ChangeDataSafePrivateEndpointCompartmentDetails": ChangeDataSafePrivateEndpointCompartmentDetails,
    "CreateDataSafePrivateEndpointDetails": CreateDataSafePrivateEndpointDetails,
    "DataSafeConfiguration": DataSafeConfiguration,
    "DataSafePrivateEndpoint": DataSafePrivateEndpoint,
    "DataSafePrivateEndpointSummary": DataSafePrivateEndpointSummary,
    "EnableDataSafeConfigurationDetails": EnableDataSafeConfigurationDetails,
    "UpdateDataSafePrivateEndpointDetails": UpdateDataSafePrivateEndpointDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
