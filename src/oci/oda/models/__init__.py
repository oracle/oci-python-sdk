# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .change_oda_instance_compartment_details import ChangeOdaInstanceCompartmentDetails
from .create_oda_instance_details import CreateOdaInstanceDetails
from .error_body import ErrorBody
from .oda_instance import OdaInstance
from .oda_instance_summary import OdaInstanceSummary
from .update_oda_instance_details import UpdateOdaInstanceDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for oda services.
oda_type_mapping = {
    "ChangeOdaInstanceCompartmentDetails": ChangeOdaInstanceCompartmentDetails,
    "CreateOdaInstanceDetails": CreateOdaInstanceDetails,
    "ErrorBody": ErrorBody,
    "OdaInstance": OdaInstance,
    "OdaInstanceSummary": OdaInstanceSummary,
    "UpdateOdaInstanceDetails": UpdateOdaInstanceDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
