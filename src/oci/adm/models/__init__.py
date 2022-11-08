# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .application_dependency import ApplicationDependency
from .application_dependency_vulnerability_collection import ApplicationDependencyVulnerabilityCollection
from .application_dependency_vulnerability_summary import ApplicationDependencyVulnerabilitySummary
from .change_knowledge_base_compartment_details import ChangeKnowledgeBaseCompartmentDetails
from .change_vulnerability_audit_compartment_details import ChangeVulnerabilityAuditCompartmentDetails
from .create_knowledge_base_details import CreateKnowledgeBaseDetails
from .create_vulnerability_audit_details import CreateVulnerabilityAuditDetails
from .external_resource_vulnerability_audit_source import ExternalResourceVulnerabilityAuditSource
from .knowledge_base import KnowledgeBase
from .knowledge_base_collection import KnowledgeBaseCollection
from .knowledge_base_summary import KnowledgeBaseSummary
from .oci_resource_vulnerability_audit_source import OciResourceVulnerabilityAuditSource
from .unknown_source_vulnerability_audit_source import UnknownSourceVulnerabilityAuditSource
from .update_knowledge_base_details import UpdateKnowledgeBaseDetails
from .update_vulnerability_audit_details import UpdateVulnerabilityAuditDetails
from .vulnerability import Vulnerability
from .vulnerability_audit import VulnerabilityAudit
from .vulnerability_audit_collection import VulnerabilityAuditCollection
from .vulnerability_audit_configuration import VulnerabilityAuditConfiguration
from .vulnerability_audit_source import VulnerabilityAuditSource
from .vulnerability_audit_summary import VulnerabilityAuditSummary
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for adm services.
adm_type_mapping = {
    "ApplicationDependency": ApplicationDependency,
    "ApplicationDependencyVulnerabilityCollection": ApplicationDependencyVulnerabilityCollection,
    "ApplicationDependencyVulnerabilitySummary": ApplicationDependencyVulnerabilitySummary,
    "ChangeKnowledgeBaseCompartmentDetails": ChangeKnowledgeBaseCompartmentDetails,
    "ChangeVulnerabilityAuditCompartmentDetails": ChangeVulnerabilityAuditCompartmentDetails,
    "CreateKnowledgeBaseDetails": CreateKnowledgeBaseDetails,
    "CreateVulnerabilityAuditDetails": CreateVulnerabilityAuditDetails,
    "ExternalResourceVulnerabilityAuditSource": ExternalResourceVulnerabilityAuditSource,
    "KnowledgeBase": KnowledgeBase,
    "KnowledgeBaseCollection": KnowledgeBaseCollection,
    "KnowledgeBaseSummary": KnowledgeBaseSummary,
    "OciResourceVulnerabilityAuditSource": OciResourceVulnerabilityAuditSource,
    "UnknownSourceVulnerabilityAuditSource": UnknownSourceVulnerabilityAuditSource,
    "UpdateKnowledgeBaseDetails": UpdateKnowledgeBaseDetails,
    "UpdateVulnerabilityAuditDetails": UpdateVulnerabilityAuditDetails,
    "Vulnerability": Vulnerability,
    "VulnerabilityAudit": VulnerabilityAudit,
    "VulnerabilityAuditCollection": VulnerabilityAuditCollection,
    "VulnerabilityAuditConfiguration": VulnerabilityAuditConfiguration,
    "VulnerabilityAuditSource": VulnerabilityAuditSource,
    "VulnerabilityAuditSummary": VulnerabilityAuditSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
