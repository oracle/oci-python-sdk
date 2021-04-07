# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .application import Application
from .application_summary import ApplicationSummary
from .application_trace_config import ApplicationTraceConfig
from .change_application_compartment_details import ChangeApplicationCompartmentDetails
from .create_application_details import CreateApplicationDetails
from .create_function_details import CreateFunctionDetails
from .function import Function
from .function_summary import FunctionSummary
from .function_trace_config import FunctionTraceConfig
from .update_application_details import UpdateApplicationDetails
from .update_function_details import UpdateFunctionDetails

# Maps type names to classes for functions services.
functions_type_mapping = {
    "Application": Application,
    "ApplicationSummary": ApplicationSummary,
    "ApplicationTraceConfig": ApplicationTraceConfig,
    "ChangeApplicationCompartmentDetails": ChangeApplicationCompartmentDetails,
    "CreateApplicationDetails": CreateApplicationDetails,
    "CreateFunctionDetails": CreateFunctionDetails,
    "Function": Function,
    "FunctionSummary": FunctionSummary,
    "FunctionTraceConfig": FunctionTraceConfig,
    "UpdateApplicationDetails": UpdateApplicationDetails,
    "UpdateFunctionDetails": UpdateFunctionDetails
}
