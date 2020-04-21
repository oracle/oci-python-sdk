# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .authorization_details import AuthorizationDetails
from .change_compartment_details import ChangeCompartmentDetails
from .configuration_field import ConfigurationField
from .create_migration_details import CreateMigrationDetails
from .create_source_details import CreateSourceDetails
from .discovery_details import DiscoveryDetails
from .ics_discovery_details import IcsDiscoveryDetails
from .internal_authorization_details import InternalAuthorizationDetails
from .internal_source_details import InternalSourceDetails
from .jcs_discovery_details import JcsDiscoveryDetails
from .migration import Migration
from .migration_summary import MigrationSummary
from .oac_discovery_details import OacDiscoveryDetails
from .ocic_authorization_details import OcicAuthorizationDetails
from .ocic_source_details import OcicSourceDetails
from .oic_discovery_details import OicDiscoveryDetails
from .pcs_discovery_details import PcsDiscoveryDetails
from .soacs_discovery_details import SoacsDiscoveryDetails
from .source import Source
from .source_application import SourceApplication
from .source_application_summary import SourceApplicationSummary
from .source_details import SourceDetails
from .source_summary import SourceSummary
from .update_migration_details import UpdateMigrationDetails
from .update_source_details import UpdateSourceDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for application_migration services.
application_migration_type_mapping = {
    "AuthorizationDetails": AuthorizationDetails,
    "ChangeCompartmentDetails": ChangeCompartmentDetails,
    "ConfigurationField": ConfigurationField,
    "CreateMigrationDetails": CreateMigrationDetails,
    "CreateSourceDetails": CreateSourceDetails,
    "DiscoveryDetails": DiscoveryDetails,
    "IcsDiscoveryDetails": IcsDiscoveryDetails,
    "InternalAuthorizationDetails": InternalAuthorizationDetails,
    "InternalSourceDetails": InternalSourceDetails,
    "JcsDiscoveryDetails": JcsDiscoveryDetails,
    "Migration": Migration,
    "MigrationSummary": MigrationSummary,
    "OacDiscoveryDetails": OacDiscoveryDetails,
    "OcicAuthorizationDetails": OcicAuthorizationDetails,
    "OcicSourceDetails": OcicSourceDetails,
    "OicDiscoveryDetails": OicDiscoveryDetails,
    "PcsDiscoveryDetails": PcsDiscoveryDetails,
    "SoacsDiscoveryDetails": SoacsDiscoveryDetails,
    "Source": Source,
    "SourceApplication": SourceApplication,
    "SourceApplicationSummary": SourceApplicationSummary,
    "SourceDetails": SourceDetails,
    "SourceSummary": SourceSummary,
    "UpdateMigrationDetails": UpdateMigrationDetails,
    "UpdateSourceDetails": UpdateSourceDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
