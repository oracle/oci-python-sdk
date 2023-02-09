# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_protected_database_compartment_details import ChangeProtectedDatabaseCompartmentDetails
from .change_protection_policy_compartment_details import ChangeProtectionPolicyCompartmentDetails
from .change_recovery_service_subnet_compartment_details import ChangeRecoveryServiceSubnetCompartmentDetails
from .create_protected_database_details import CreateProtectedDatabaseDetails
from .create_protection_policy_details import CreateProtectionPolicyDetails
from .create_recovery_service_subnet_details import CreateRecoveryServiceSubnetDetails
from .fetch_protected_database_configuration_details import FetchProtectedDatabaseConfigurationDetails
from .metrics import Metrics
from .metrics_summary import MetricsSummary
from .protected_database import ProtectedDatabase
from .protected_database_collection import ProtectedDatabaseCollection
from .protected_database_summary import ProtectedDatabaseSummary
from .protection_policy import ProtectionPolicy
from .protection_policy_collection import ProtectionPolicyCollection
from .protection_policy_summary import ProtectionPolicySummary
from .recovery_service_subnet import RecoveryServiceSubnet
from .recovery_service_subnet_collection import RecoveryServiceSubnetCollection
from .recovery_service_subnet_details import RecoveryServiceSubnetDetails
from .recovery_service_subnet_input import RecoveryServiceSubnetInput
from .recovery_service_subnet_summary import RecoveryServiceSubnetSummary
from .update_protected_database_details import UpdateProtectedDatabaseDetails
from .update_protection_policy_details import UpdateProtectionPolicyDetails
from .update_recovery_service_subnet_details import UpdateRecoveryServiceSubnetDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for recovery services.
recovery_type_mapping = {
    "ChangeProtectedDatabaseCompartmentDetails": ChangeProtectedDatabaseCompartmentDetails,
    "ChangeProtectionPolicyCompartmentDetails": ChangeProtectionPolicyCompartmentDetails,
    "ChangeRecoveryServiceSubnetCompartmentDetails": ChangeRecoveryServiceSubnetCompartmentDetails,
    "CreateProtectedDatabaseDetails": CreateProtectedDatabaseDetails,
    "CreateProtectionPolicyDetails": CreateProtectionPolicyDetails,
    "CreateRecoveryServiceSubnetDetails": CreateRecoveryServiceSubnetDetails,
    "FetchProtectedDatabaseConfigurationDetails": FetchProtectedDatabaseConfigurationDetails,
    "Metrics": Metrics,
    "MetricsSummary": MetricsSummary,
    "ProtectedDatabase": ProtectedDatabase,
    "ProtectedDatabaseCollection": ProtectedDatabaseCollection,
    "ProtectedDatabaseSummary": ProtectedDatabaseSummary,
    "ProtectionPolicy": ProtectionPolicy,
    "ProtectionPolicyCollection": ProtectionPolicyCollection,
    "ProtectionPolicySummary": ProtectionPolicySummary,
    "RecoveryServiceSubnet": RecoveryServiceSubnet,
    "RecoveryServiceSubnetCollection": RecoveryServiceSubnetCollection,
    "RecoveryServiceSubnetDetails": RecoveryServiceSubnetDetails,
    "RecoveryServiceSubnetInput": RecoveryServiceSubnetInput,
    "RecoveryServiceSubnetSummary": RecoveryServiceSubnetSummary,
    "UpdateProtectedDatabaseDetails": UpdateProtectedDatabaseDetails,
    "UpdateProtectionPolicyDetails": UpdateProtectionPolicyDetails,
    "UpdateRecoveryServiceSubnetDetails": UpdateRecoveryServiceSubnetDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
