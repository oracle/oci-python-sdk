# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .application import Application
from .application_summary import ApplicationSummary
from .change_application_compartment_details import ChangeApplicationCompartmentDetails
from .create_application_details import CreateApplicationDetails
from .create_function_details import CreateFunctionDetails
from .function import Function
from .function_summary import FunctionSummary
from .update_application_details import UpdateApplicationDetails
from .update_function_details import UpdateFunctionDetails

# Maps type names to classes for functions services.
functions_type_mapping = {
    "Application": Application,
    "ApplicationSummary": ApplicationSummary,
    "ChangeApplicationCompartmentDetails": ChangeApplicationCompartmentDetails,
    "CreateApplicationDetails": CreateApplicationDetails,
    "CreateFunctionDetails": CreateFunctionDetails,
    "Function": Function,
    "FunctionSummary": FunctionSummary,
    "UpdateApplicationDetails": UpdateApplicationDetails,
    "UpdateFunctionDetails": UpdateFunctionDetails
}
