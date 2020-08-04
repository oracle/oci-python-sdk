# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .application import Application
from .application_parameter import ApplicationParameter
from .application_summary import ApplicationSummary
from .change_application_compartment_details import ChangeApplicationCompartmentDetails
from .change_private_endpoint_compartment_details import ChangePrivateEndpointCompartmentDetails
from .change_run_compartment_details import ChangeRunCompartmentDetails
from .create_application_details import CreateApplicationDetails
from .create_private_endpoint_details import CreatePrivateEndpointDetails
from .create_run_details import CreateRunDetails
from .private_endpoint import PrivateEndpoint
from .private_endpoint_collection import PrivateEndpointCollection
from .private_endpoint_summary import PrivateEndpointSummary
from .run import Run
from .run_log_summary import RunLogSummary
from .run_summary import RunSummary
from .update_application_details import UpdateApplicationDetails
from .update_private_endpoint_details import UpdatePrivateEndpointDetails
from .update_run_details import UpdateRunDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log import WorkRequestLog
from .work_request_log_collection import WorkRequestLogCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for data_flow services.
data_flow_type_mapping = {
    "Application": Application,
    "ApplicationParameter": ApplicationParameter,
    "ApplicationSummary": ApplicationSummary,
    "ChangeApplicationCompartmentDetails": ChangeApplicationCompartmentDetails,
    "ChangePrivateEndpointCompartmentDetails": ChangePrivateEndpointCompartmentDetails,
    "ChangeRunCompartmentDetails": ChangeRunCompartmentDetails,
    "CreateApplicationDetails": CreateApplicationDetails,
    "CreatePrivateEndpointDetails": CreatePrivateEndpointDetails,
    "CreateRunDetails": CreateRunDetails,
    "PrivateEndpoint": PrivateEndpoint,
    "PrivateEndpointCollection": PrivateEndpointCollection,
    "PrivateEndpointSummary": PrivateEndpointSummary,
    "Run": Run,
    "RunLogSummary": RunLogSummary,
    "RunSummary": RunSummary,
    "UpdateApplicationDetails": UpdateApplicationDetails,
    "UpdatePrivateEndpointDetails": UpdatePrivateEndpointDetails,
    "UpdateRunDetails": UpdateRunDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestLogCollection": WorkRequestLogCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
