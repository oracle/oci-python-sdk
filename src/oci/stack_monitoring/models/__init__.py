# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .associate_monitored_resources_details import AssociateMonitoredResourcesDetails
from .associated_monitored_resource import AssociatedMonitoredResource
from .associated_resources_collection import AssociatedResourcesCollection
from .associated_resources_summary import AssociatedResourcesSummary
from .association_details import AssociationDetails
from .association_resource_details import AssociationResourceDetails
from .change_monitored_resource_compartment_details import ChangeMonitoredResourceCompartmentDetails
from .connection_details import ConnectionDetails
from .create_discovery_job_details import CreateDiscoveryJobDetails
from .create_monitored_resource_details import CreateMonitoredResourceDetails
from .credential_collection import CredentialCollection
from .credential_details import CredentialDetails
from .credential_property import CredentialProperty
from .disassociate_monitored_resources_details import DisassociateMonitoredResourcesDetails
from .discovery_details import DiscoveryDetails
from .discovery_job import DiscoveryJob
from .discovery_job_collection import DiscoveryJobCollection
from .discovery_job_log_collection import DiscoveryJobLogCollection
from .discovery_job_log_summary import DiscoveryJobLogSummary
from .discovery_job_summary import DiscoveryJobSummary
from .encrypted_credentials import EncryptedCredentials
from .monitored_resource import MonitoredResource
from .monitored_resource_alias_credential import MonitoredResourceAliasCredential
from .monitored_resource_alias_source_credential import MonitoredResourceAliasSourceCredential
from .monitored_resource_association import MonitoredResourceAssociation
from .monitored_resource_association_summary import MonitoredResourceAssociationSummary
from .monitored_resource_associations_collection import MonitoredResourceAssociationsCollection
from .monitored_resource_collection import MonitoredResourceCollection
from .monitored_resource_credential import MonitoredResourceCredential
from .monitored_resource_member_summary import MonitoredResourceMemberSummary
from .monitored_resource_members_collection import MonitoredResourceMembersCollection
from .monitored_resource_property import MonitoredResourceProperty
from .monitored_resource_summary import MonitoredResourceSummary
from .plain_text_credentials import PlainTextCredentials
from .pre_existing_credentials import PreExistingCredentials
from .property_details import PropertyDetails
from .search_associated_resources_details import SearchAssociatedResourcesDetails
from .search_monitored_resource_associations_details import SearchMonitoredResourceAssociationsDetails
from .search_monitored_resource_members_details import SearchMonitoredResourceMembersDetails
from .search_monitored_resources_details import SearchMonitoredResourcesDetails
from .update_monitored_resource_details import UpdateMonitoredResourceDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for stack_monitoring services.
stack_monitoring_type_mapping = {
    "AssociateMonitoredResourcesDetails": AssociateMonitoredResourcesDetails,
    "AssociatedMonitoredResource": AssociatedMonitoredResource,
    "AssociatedResourcesCollection": AssociatedResourcesCollection,
    "AssociatedResourcesSummary": AssociatedResourcesSummary,
    "AssociationDetails": AssociationDetails,
    "AssociationResourceDetails": AssociationResourceDetails,
    "ChangeMonitoredResourceCompartmentDetails": ChangeMonitoredResourceCompartmentDetails,
    "ConnectionDetails": ConnectionDetails,
    "CreateDiscoveryJobDetails": CreateDiscoveryJobDetails,
    "CreateMonitoredResourceDetails": CreateMonitoredResourceDetails,
    "CredentialCollection": CredentialCollection,
    "CredentialDetails": CredentialDetails,
    "CredentialProperty": CredentialProperty,
    "DisassociateMonitoredResourcesDetails": DisassociateMonitoredResourcesDetails,
    "DiscoveryDetails": DiscoveryDetails,
    "DiscoveryJob": DiscoveryJob,
    "DiscoveryJobCollection": DiscoveryJobCollection,
    "DiscoveryJobLogCollection": DiscoveryJobLogCollection,
    "DiscoveryJobLogSummary": DiscoveryJobLogSummary,
    "DiscoveryJobSummary": DiscoveryJobSummary,
    "EncryptedCredentials": EncryptedCredentials,
    "MonitoredResource": MonitoredResource,
    "MonitoredResourceAliasCredential": MonitoredResourceAliasCredential,
    "MonitoredResourceAliasSourceCredential": MonitoredResourceAliasSourceCredential,
    "MonitoredResourceAssociation": MonitoredResourceAssociation,
    "MonitoredResourceAssociationSummary": MonitoredResourceAssociationSummary,
    "MonitoredResourceAssociationsCollection": MonitoredResourceAssociationsCollection,
    "MonitoredResourceCollection": MonitoredResourceCollection,
    "MonitoredResourceCredential": MonitoredResourceCredential,
    "MonitoredResourceMemberSummary": MonitoredResourceMemberSummary,
    "MonitoredResourceMembersCollection": MonitoredResourceMembersCollection,
    "MonitoredResourceProperty": MonitoredResourceProperty,
    "MonitoredResourceSummary": MonitoredResourceSummary,
    "PlainTextCredentials": PlainTextCredentials,
    "PreExistingCredentials": PreExistingCredentials,
    "PropertyDetails": PropertyDetails,
    "SearchAssociatedResourcesDetails": SearchAssociatedResourcesDetails,
    "SearchMonitoredResourceAssociationsDetails": SearchMonitoredResourceAssociationsDetails,
    "SearchMonitoredResourceMembersDetails": SearchMonitoredResourceMembersDetails,
    "SearchMonitoredResourcesDetails": SearchMonitoredResourcesDetails,
    "UpdateMonitoredResourceDetails": UpdateMonitoredResourceDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
