# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activate_target_database_details import ActivateTargetDatabaseDetails
from .autonomous_database_details import AutonomousDatabaseDetails
from .change_data_safe_private_endpoint_compartment_details import ChangeDataSafePrivateEndpointCompartmentDetails
from .change_on_prem_connector_compartment_details import ChangeOnPremConnectorCompartmentDetails
from .change_security_assessment_compartment_details import ChangeSecurityAssessmentCompartmentDetails
from .change_target_database_compartment_details import ChangeTargetDatabaseCompartmentDetails
from .change_user_assessment_compartment_details import ChangeUserAssessmentCompartmentDetails
from .compare_security_assessment_details import CompareSecurityAssessmentDetails
from .compare_user_assessment_details import CompareUserAssessmentDetails
from .connection_option import ConnectionOption
from .create_data_safe_private_endpoint_details import CreateDataSafePrivateEndpointDetails
from .create_on_prem_connector_details import CreateOnPremConnectorDetails
from .create_security_assessment_details import CreateSecurityAssessmentDetails
from .create_target_database_details import CreateTargetDatabaseDetails
from .create_user_assessment_details import CreateUserAssessmentDetails
from .credentials import Credentials
from .data_safe_configuration import DataSafeConfiguration
from .data_safe_private_endpoint import DataSafePrivateEndpoint
from .data_safe_private_endpoint_summary import DataSafePrivateEndpointSummary
from .database_cloud_service_details import DatabaseCloudServiceDetails
from .database_details import DatabaseDetails
from .diffs import Diffs
from .download_security_assessment_report_details import DownloadSecurityAssessmentReportDetails
from .download_user_assessment_report_details import DownloadUserAssessmentReportDetails
from .enable_data_safe_configuration_details import EnableDataSafeConfigurationDetails
from .finding import Finding
from .finding_summary import FindingSummary
from .generate_on_prem_connector_configuration_details import GenerateOnPremConnectorConfigurationDetails
from .generate_security_assessment_report_details import GenerateSecurityAssessmentReportDetails
from .generate_user_assessment_report_details import GenerateUserAssessmentReportDetails
from .grant_summary import GrantSummary
from .initialization_parameter import InitializationParameter
from .installed_database_details import InstalledDatabaseDetails
from .on_prem_connector import OnPremConnector
from .on_prem_connector_summary import OnPremConnectorSummary
from .on_premise_connector import OnPremiseConnector
from .private_endpoint import PrivateEndpoint
from .profile_details import ProfileDetails
from .references import References
from .run_security_assessment_details import RunSecurityAssessmentDetails
from .run_user_assessment_details import RunUserAssessmentDetails
from .section_statistics import SectionStatistics
from .security_assessment import SecurityAssessment
from .security_assessment_base_line_details import SecurityAssessmentBaseLineDetails
from .security_assessment_comparison import SecurityAssessmentComparison
from .security_assessment_comparison_per_target import SecurityAssessmentComparisonPerTarget
from .security_assessment_statistics import SecurityAssessmentStatistics
from .security_assessment_summary import SecurityAssessmentSummary
from .target_database import TargetDatabase
from .target_database_summary import TargetDatabaseSummary
from .tls_config import TlsConfig
from .update_data_safe_private_endpoint_details import UpdateDataSafePrivateEndpointDetails
from .update_on_prem_connector_details import UpdateOnPremConnectorDetails
from .update_on_prem_connector_wallet_details import UpdateOnPremConnectorWalletDetails
from .update_security_assessment_details import UpdateSecurityAssessmentDetails
from .update_target_database_details import UpdateTargetDatabaseDetails
from .update_user_assessment_details import UpdateUserAssessmentDetails
from .user_aggregation import UserAggregation
from .user_assessment import UserAssessment
from .user_assessment_base_line_details import UserAssessmentBaseLineDetails
from .user_assessment_comparison import UserAssessmentComparison
from .user_assessment_summary import UserAssessmentSummary
from .user_details import UserDetails
from .user_summary import UserSummary
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for data_safe services.
data_safe_type_mapping = {
    "ActivateTargetDatabaseDetails": ActivateTargetDatabaseDetails,
    "AutonomousDatabaseDetails": AutonomousDatabaseDetails,
    "ChangeDataSafePrivateEndpointCompartmentDetails": ChangeDataSafePrivateEndpointCompartmentDetails,
    "ChangeOnPremConnectorCompartmentDetails": ChangeOnPremConnectorCompartmentDetails,
    "ChangeSecurityAssessmentCompartmentDetails": ChangeSecurityAssessmentCompartmentDetails,
    "ChangeTargetDatabaseCompartmentDetails": ChangeTargetDatabaseCompartmentDetails,
    "ChangeUserAssessmentCompartmentDetails": ChangeUserAssessmentCompartmentDetails,
    "CompareSecurityAssessmentDetails": CompareSecurityAssessmentDetails,
    "CompareUserAssessmentDetails": CompareUserAssessmentDetails,
    "ConnectionOption": ConnectionOption,
    "CreateDataSafePrivateEndpointDetails": CreateDataSafePrivateEndpointDetails,
    "CreateOnPremConnectorDetails": CreateOnPremConnectorDetails,
    "CreateSecurityAssessmentDetails": CreateSecurityAssessmentDetails,
    "CreateTargetDatabaseDetails": CreateTargetDatabaseDetails,
    "CreateUserAssessmentDetails": CreateUserAssessmentDetails,
    "Credentials": Credentials,
    "DataSafeConfiguration": DataSafeConfiguration,
    "DataSafePrivateEndpoint": DataSafePrivateEndpoint,
    "DataSafePrivateEndpointSummary": DataSafePrivateEndpointSummary,
    "DatabaseCloudServiceDetails": DatabaseCloudServiceDetails,
    "DatabaseDetails": DatabaseDetails,
    "Diffs": Diffs,
    "DownloadSecurityAssessmentReportDetails": DownloadSecurityAssessmentReportDetails,
    "DownloadUserAssessmentReportDetails": DownloadUserAssessmentReportDetails,
    "EnableDataSafeConfigurationDetails": EnableDataSafeConfigurationDetails,
    "Finding": Finding,
    "FindingSummary": FindingSummary,
    "GenerateOnPremConnectorConfigurationDetails": GenerateOnPremConnectorConfigurationDetails,
    "GenerateSecurityAssessmentReportDetails": GenerateSecurityAssessmentReportDetails,
    "GenerateUserAssessmentReportDetails": GenerateUserAssessmentReportDetails,
    "GrantSummary": GrantSummary,
    "InitializationParameter": InitializationParameter,
    "InstalledDatabaseDetails": InstalledDatabaseDetails,
    "OnPremConnector": OnPremConnector,
    "OnPremConnectorSummary": OnPremConnectorSummary,
    "OnPremiseConnector": OnPremiseConnector,
    "PrivateEndpoint": PrivateEndpoint,
    "ProfileDetails": ProfileDetails,
    "References": References,
    "RunSecurityAssessmentDetails": RunSecurityAssessmentDetails,
    "RunUserAssessmentDetails": RunUserAssessmentDetails,
    "SectionStatistics": SectionStatistics,
    "SecurityAssessment": SecurityAssessment,
    "SecurityAssessmentBaseLineDetails": SecurityAssessmentBaseLineDetails,
    "SecurityAssessmentComparison": SecurityAssessmentComparison,
    "SecurityAssessmentComparisonPerTarget": SecurityAssessmentComparisonPerTarget,
    "SecurityAssessmentStatistics": SecurityAssessmentStatistics,
    "SecurityAssessmentSummary": SecurityAssessmentSummary,
    "TargetDatabase": TargetDatabase,
    "TargetDatabaseSummary": TargetDatabaseSummary,
    "TlsConfig": TlsConfig,
    "UpdateDataSafePrivateEndpointDetails": UpdateDataSafePrivateEndpointDetails,
    "UpdateOnPremConnectorDetails": UpdateOnPremConnectorDetails,
    "UpdateOnPremConnectorWalletDetails": UpdateOnPremConnectorWalletDetails,
    "UpdateSecurityAssessmentDetails": UpdateSecurityAssessmentDetails,
    "UpdateTargetDatabaseDetails": UpdateTargetDatabaseDetails,
    "UpdateUserAssessmentDetails": UpdateUserAssessmentDetails,
    "UserAggregation": UserAggregation,
    "UserAssessment": UserAssessment,
    "UserAssessmentBaseLineDetails": UserAssessmentBaseLineDetails,
    "UserAssessmentComparison": UserAssessmentComparison,
    "UserAssessmentSummary": UserAssessmentSummary,
    "UserDetails": UserDetails,
    "UserSummary": UserSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
