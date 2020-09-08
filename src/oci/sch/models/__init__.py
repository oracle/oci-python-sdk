# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_service_connector_compartment_details import ChangeServiceConnectorCompartmentDetails
from .create_service_connector_details import CreateServiceConnectorDetails
from .functions_target_details import FunctionsTargetDetails
from .log_rule_task_details import LogRuleTaskDetails
from .log_source import LogSource
from .logging_source_details import LoggingSourceDetails
from .monitoring_target_details import MonitoringTargetDetails
from .notifications_target_details import NotificationsTargetDetails
from .object_storage_target_details import ObjectStorageTargetDetails
from .service_connector import ServiceConnector
from .service_connector_collection import ServiceConnectorCollection
from .service_connector_summary import ServiceConnectorSummary
from .source_details import SourceDetails
from .streaming_target_details import StreamingTargetDetails
from .target_details import TargetDetails
from .task_details import TaskDetails
from .update_service_connector_details import UpdateServiceConnectorDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource

# Maps type names to classes for sch services.
sch_type_mapping = {
    "ChangeServiceConnectorCompartmentDetails": ChangeServiceConnectorCompartmentDetails,
    "CreateServiceConnectorDetails": CreateServiceConnectorDetails,
    "FunctionsTargetDetails": FunctionsTargetDetails,
    "LogRuleTaskDetails": LogRuleTaskDetails,
    "LogSource": LogSource,
    "LoggingSourceDetails": LoggingSourceDetails,
    "MonitoringTargetDetails": MonitoringTargetDetails,
    "NotificationsTargetDetails": NotificationsTargetDetails,
    "ObjectStorageTargetDetails": ObjectStorageTargetDetails,
    "ServiceConnector": ServiceConnector,
    "ServiceConnectorCollection": ServiceConnectorCollection,
    "ServiceConnectorSummary": ServiceConnectorSummary,
    "SourceDetails": SourceDetails,
    "StreamingTargetDetails": StreamingTargetDetails,
    "TargetDetails": TargetDetails,
    "TaskDetails": TaskDetails,
    "UpdateServiceConnectorDetails": UpdateServiceConnectorDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource
}
