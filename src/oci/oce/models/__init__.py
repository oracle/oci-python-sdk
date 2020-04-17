# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_oce_instance_compartment_details import ChangeOceInstanceCompartmentDetails
from .create_oce_instance_details import CreateOceInstanceDetails
from .identity_stripe_details import IdentityStripeDetails
from .oce_instance import OceInstance
from .oce_instance_summary import OceInstanceSummary
from .update_oce_instance_details import UpdateOceInstanceDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .workflow_monitor import WorkflowMonitor
from .workflow_step import WorkflowStep

# Maps type names to classes for oce services.
oce_type_mapping = {
    "ChangeOceInstanceCompartmentDetails": ChangeOceInstanceCompartmentDetails,
    "CreateOceInstanceDetails": CreateOceInstanceDetails,
    "IdentityStripeDetails": IdentityStripeDetails,
    "OceInstance": OceInstance,
    "OceInstanceSummary": OceInstanceSummary,
    "UpdateOceInstanceDetails": UpdateOceInstanceDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkflowMonitor": WorkflowMonitor,
    "WorkflowStep": WorkflowStep
}
