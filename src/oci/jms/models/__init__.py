# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .application_usage import ApplicationUsage
from .application_usage_collection import ApplicationUsageCollection
from .change_fleet_compartment_details import ChangeFleetCompartmentDetails
from .create_fleet_details import CreateFleetDetails
from .fleet import Fleet
from .fleet_agent_configuration import FleetAgentConfiguration
from .fleet_agent_os_configuration import FleetAgentOsConfiguration
from .fleet_collection import FleetCollection
from .fleet_summary import FleetSummary
from .installation_usage import InstallationUsage
from .installation_usage_collection import InstallationUsageCollection
from .jre_usage import JreUsage
from .jre_usage_collection import JreUsageCollection
from .managed_instance_usage import ManagedInstanceUsage
from .managed_instance_usage_collection import ManagedInstanceUsageCollection
from .operating_system import OperatingSystem
from .resource_inventory import ResourceInventory
from .update_fleet_agent_configuration_details import UpdateFleetAgentConfigurationDetails
from .update_fleet_details import UpdateFleetDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource

# Maps type names to classes for jms services.
jms_type_mapping = {
    "ApplicationUsage": ApplicationUsage,
    "ApplicationUsageCollection": ApplicationUsageCollection,
    "ChangeFleetCompartmentDetails": ChangeFleetCompartmentDetails,
    "CreateFleetDetails": CreateFleetDetails,
    "Fleet": Fleet,
    "FleetAgentConfiguration": FleetAgentConfiguration,
    "FleetAgentOsConfiguration": FleetAgentOsConfiguration,
    "FleetCollection": FleetCollection,
    "FleetSummary": FleetSummary,
    "InstallationUsage": InstallationUsage,
    "InstallationUsageCollection": InstallationUsageCollection,
    "JreUsage": JreUsage,
    "JreUsageCollection": JreUsageCollection,
    "ManagedInstanceUsage": ManagedInstanceUsage,
    "ManagedInstanceUsageCollection": ManagedInstanceUsageCollection,
    "OperatingSystem": OperatingSystem,
    "ResourceInventory": ResourceInventory,
    "UpdateFleetAgentConfigurationDetails": UpdateFleetAgentConfigurationDetails,
    "UpdateFleetDetails": UpdateFleetDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource
}
