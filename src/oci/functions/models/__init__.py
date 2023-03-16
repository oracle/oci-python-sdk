# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .application import Application
from .application_summary import ApplicationSummary
from .application_trace_config import ApplicationTraceConfig
from .change_application_compartment_details import ChangeApplicationCompartmentDetails
from .config_details import ConfigDetails
from .constant_provisioned_concurrency_config import ConstantProvisionedConcurrencyConfig
from .create_application_details import CreateApplicationDetails
from .create_function_details import CreateFunctionDetails
from .function import Function
from .function_provisioned_concurrency_config import FunctionProvisionedConcurrencyConfig
from .function_source_details import FunctionSourceDetails
from .function_summary import FunctionSummary
from .function_trace_config import FunctionTraceConfig
from .image_policy_config import ImagePolicyConfig
from .key_details import KeyDetails
from .none_provisioned_concurrency_config import NoneProvisionedConcurrencyConfig
from .pbf_listing import PbfListing
from .pbf_listing_summary import PbfListingSummary
from .pbf_listing_version import PbfListingVersion
from .pbf_listing_version_summary import PbfListingVersionSummary
from .pbf_listing_versions_collection import PbfListingVersionsCollection
from .pbf_listings_collection import PbfListingsCollection
from .policy_details import PolicyDetails
from .pre_built_function_source_details import PreBuiltFunctionSourceDetails
from .publisher_details import PublisherDetails
from .requirement_details import RequirementDetails
from .trigger import Trigger
from .trigger_summary import TriggerSummary
from .triggers_collection import TriggersCollection
from .update_application_details import UpdateApplicationDetails
from .update_function_details import UpdateFunctionDetails

# Maps type names to classes for functions services.
functions_type_mapping = {
    "Application": Application,
    "ApplicationSummary": ApplicationSummary,
    "ApplicationTraceConfig": ApplicationTraceConfig,
    "ChangeApplicationCompartmentDetails": ChangeApplicationCompartmentDetails,
    "ConfigDetails": ConfigDetails,
    "ConstantProvisionedConcurrencyConfig": ConstantProvisionedConcurrencyConfig,
    "CreateApplicationDetails": CreateApplicationDetails,
    "CreateFunctionDetails": CreateFunctionDetails,
    "Function": Function,
    "FunctionProvisionedConcurrencyConfig": FunctionProvisionedConcurrencyConfig,
    "FunctionSourceDetails": FunctionSourceDetails,
    "FunctionSummary": FunctionSummary,
    "FunctionTraceConfig": FunctionTraceConfig,
    "ImagePolicyConfig": ImagePolicyConfig,
    "KeyDetails": KeyDetails,
    "NoneProvisionedConcurrencyConfig": NoneProvisionedConcurrencyConfig,
    "PbfListing": PbfListing,
    "PbfListingSummary": PbfListingSummary,
    "PbfListingVersion": PbfListingVersion,
    "PbfListingVersionSummary": PbfListingVersionSummary,
    "PbfListingVersionsCollection": PbfListingVersionsCollection,
    "PbfListingsCollection": PbfListingsCollection,
    "PolicyDetails": PolicyDetails,
    "PreBuiltFunctionSourceDetails": PreBuiltFunctionSourceDetails,
    "PublisherDetails": PublisherDetails,
    "RequirementDetails": RequirementDetails,
    "Trigger": Trigger,
    "TriggerSummary": TriggerSummary,
    "TriggersCollection": TriggersCollection,
    "UpdateApplicationDetails": UpdateApplicationDetails,
    "UpdateFunctionDetails": UpdateFunctionDetails
}
