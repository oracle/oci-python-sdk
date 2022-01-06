# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .archiving import Archiving
from .category import Category
from .change_log_group_compartment_details import ChangeLogGroupCompartmentDetails
from .change_log_log_group_details import ChangeLogLogGroupDetails
from .change_log_saved_search_compartment_details import ChangeLogSavedSearchCompartmentDetails
from .change_unified_agent_configuration_compartment_details import ChangeUnifiedAgentConfigurationCompartmentDetails
from .configuration import Configuration
from .create_log_details import CreateLogDetails
from .create_log_group_details import CreateLogGroupDetails
from .create_log_saved_search_details import CreateLogSavedSearchDetails
from .create_unified_agent_configuration_details import CreateUnifiedAgentConfigurationDetails
from .grok_pattern import GrokPattern
from .group_association_details import GroupAssociationDetails
from .log import Log
from .log_group import LogGroup
from .log_group_summary import LogGroupSummary
from .log_included_search import LogIncludedSearch
from .log_included_search_summary import LogIncludedSearchSummary
from .log_included_search_summary_collection import LogIncludedSearchSummaryCollection
from .log_saved_search import LogSavedSearch
from .log_saved_search_summary import LogSavedSearchSummary
from .log_saved_search_summary_collection import LogSavedSearchSummaryCollection
from .log_summary import LogSummary
from .oci_service import OciService
from .parameter import Parameter
from .resource_type import ResourceType
from .service_summary import ServiceSummary
from .source import Source
from .source_update_details import SourceUpdateDetails
from .unified_agent_apache2_parser import UnifiedAgentApache2Parser
from .unified_agent_apache_error_parser import UnifiedAgentApacheErrorParser
from .unified_agent_auditd_parser import UnifiedAgentAuditdParser
from .unified_agent_configuration import UnifiedAgentConfiguration
from .unified_agent_configuration_collection import UnifiedAgentConfigurationCollection
from .unified_agent_configuration_summary import UnifiedAgentConfigurationSummary
from .unified_agent_csv_parser import UnifiedAgentCsvParser
from .unified_agent_grok_parser import UnifiedAgentGrokParser
from .unified_agent_logging_configuration import UnifiedAgentLoggingConfiguration
from .unified_agent_logging_destination import UnifiedAgentLoggingDestination
from .unified_agent_logging_source import UnifiedAgentLoggingSource
from .unified_agent_msgpack_parser import UnifiedAgentMsgpackParser
from .unified_agent_multiline_grok_parser import UnifiedAgentMultilineGrokParser
from .unified_agent_multiline_parser import UnifiedAgentMultilineParser
from .unified_agent_none_parser import UnifiedAgentNoneParser
from .unified_agent_parser import UnifiedAgentParser
from .unified_agent_regex_parser import UnifiedAgentRegexParser
from .unified_agent_service_configuration_details import UnifiedAgentServiceConfigurationDetails
from .unified_agent_syslog_parser import UnifiedAgentSyslogParser
from .unified_agent_tail_log_source import UnifiedAgentTailLogSource
from .unified_agent_tsv_parser import UnifiedAgentTsvParser
from .unified_agent_windows_event_source import UnifiedAgentWindowsEventSource
from .unified_json_parser import UnifiedJSONParser
from .update_configuration_details import UpdateConfigurationDetails
from .update_log_details import UpdateLogDetails
from .update_log_group_details import UpdateLogGroupDetails
from .update_log_saved_search_details import UpdateLogSavedSearchDetails
from .update_unified_agent_configuration_details import UpdateUnifiedAgentConfigurationDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log import WorkRequestLog
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for logging services.
logging_type_mapping = {
    "Archiving": Archiving,
    "Category": Category,
    "ChangeLogGroupCompartmentDetails": ChangeLogGroupCompartmentDetails,
    "ChangeLogLogGroupDetails": ChangeLogLogGroupDetails,
    "ChangeLogSavedSearchCompartmentDetails": ChangeLogSavedSearchCompartmentDetails,
    "ChangeUnifiedAgentConfigurationCompartmentDetails": ChangeUnifiedAgentConfigurationCompartmentDetails,
    "Configuration": Configuration,
    "CreateLogDetails": CreateLogDetails,
    "CreateLogGroupDetails": CreateLogGroupDetails,
    "CreateLogSavedSearchDetails": CreateLogSavedSearchDetails,
    "CreateUnifiedAgentConfigurationDetails": CreateUnifiedAgentConfigurationDetails,
    "GrokPattern": GrokPattern,
    "GroupAssociationDetails": GroupAssociationDetails,
    "Log": Log,
    "LogGroup": LogGroup,
    "LogGroupSummary": LogGroupSummary,
    "LogIncludedSearch": LogIncludedSearch,
    "LogIncludedSearchSummary": LogIncludedSearchSummary,
    "LogIncludedSearchSummaryCollection": LogIncludedSearchSummaryCollection,
    "LogSavedSearch": LogSavedSearch,
    "LogSavedSearchSummary": LogSavedSearchSummary,
    "LogSavedSearchSummaryCollection": LogSavedSearchSummaryCollection,
    "LogSummary": LogSummary,
    "OciService": OciService,
    "Parameter": Parameter,
    "ResourceType": ResourceType,
    "ServiceSummary": ServiceSummary,
    "Source": Source,
    "SourceUpdateDetails": SourceUpdateDetails,
    "UnifiedAgentApache2Parser": UnifiedAgentApache2Parser,
    "UnifiedAgentApacheErrorParser": UnifiedAgentApacheErrorParser,
    "UnifiedAgentAuditdParser": UnifiedAgentAuditdParser,
    "UnifiedAgentConfiguration": UnifiedAgentConfiguration,
    "UnifiedAgentConfigurationCollection": UnifiedAgentConfigurationCollection,
    "UnifiedAgentConfigurationSummary": UnifiedAgentConfigurationSummary,
    "UnifiedAgentCsvParser": UnifiedAgentCsvParser,
    "UnifiedAgentGrokParser": UnifiedAgentGrokParser,
    "UnifiedAgentLoggingConfiguration": UnifiedAgentLoggingConfiguration,
    "UnifiedAgentLoggingDestination": UnifiedAgentLoggingDestination,
    "UnifiedAgentLoggingSource": UnifiedAgentLoggingSource,
    "UnifiedAgentMsgpackParser": UnifiedAgentMsgpackParser,
    "UnifiedAgentMultilineGrokParser": UnifiedAgentMultilineGrokParser,
    "UnifiedAgentMultilineParser": UnifiedAgentMultilineParser,
    "UnifiedAgentNoneParser": UnifiedAgentNoneParser,
    "UnifiedAgentParser": UnifiedAgentParser,
    "UnifiedAgentRegexParser": UnifiedAgentRegexParser,
    "UnifiedAgentServiceConfigurationDetails": UnifiedAgentServiceConfigurationDetails,
    "UnifiedAgentSyslogParser": UnifiedAgentSyslogParser,
    "UnifiedAgentTailLogSource": UnifiedAgentTailLogSource,
    "UnifiedAgentTsvParser": UnifiedAgentTsvParser,
    "UnifiedAgentWindowsEventSource": UnifiedAgentWindowsEventSource,
    "UnifiedJSONParser": UnifiedJSONParser,
    "UpdateConfigurationDetails": UpdateConfigurationDetails,
    "UpdateLogDetails": UpdateLogDetails,
    "UpdateLogGroupDetails": UpdateLogGroupDetails,
    "UpdateLogSavedSearchDetails": UpdateLogSavedSearchDetails,
    "UpdateUnifiedAgentConfigurationDetails": UpdateUnifiedAgentConfigurationDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
