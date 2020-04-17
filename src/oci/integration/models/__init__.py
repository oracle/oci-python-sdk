# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_integration_instance_compartment_details import ChangeIntegrationInstanceCompartmentDetails
from .create_integration_instance_details import CreateIntegrationInstanceDetails
from .integration_instance import IntegrationInstance
from .integration_instance_summary import IntegrationInstanceSummary
from .update_integration_instance_details import UpdateIntegrationInstanceDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for integration services.
integration_type_mapping = {
    "ChangeIntegrationInstanceCompartmentDetails": ChangeIntegrationInstanceCompartmentDetails,
    "CreateIntegrationInstanceDetails": CreateIntegrationInstanceDetails,
    "IntegrationInstance": IntegrationInstance,
    "IntegrationInstanceSummary": IntegrationInstanceSummary,
    "UpdateIntegrationInstanceDetails": UpdateIntegrationInstanceDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
