# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activate_target_database_details import ActivateTargetDatabaseDetails
from .alert import Alert
from .alert_aggregation_items import AlertAggregationItems
from .alert_analytics_collection import AlertAnalyticsCollection
from .alert_collection import AlertCollection
from .alert_policy import AlertPolicy
from .alert_policy_collection import AlertPolicyCollection
from .alert_policy_rule import AlertPolicyRule
from .alert_policy_rule_collection import AlertPolicyRuleCollection
from .alert_policy_rule_summary import AlertPolicyRuleSummary
from .alert_policy_summary import AlertPolicySummary
from .alert_summary import AlertSummary
from .alerts_aggregation_dimension import AlertsAggregationDimension
from .apply_discovery_job_results_details import ApplyDiscoveryJobResultsDetails
from .audit_archive_retrieval import AuditArchiveRetrieval
from .audit_archive_retrieval_collection import AuditArchiveRetrievalCollection
from .audit_archive_retrieval_summary import AuditArchiveRetrievalSummary
from .audit_conditions import AuditConditions
from .audit_event_aggregation_dimensions import AuditEventAggregationDimensions
from .audit_event_aggregation_items import AuditEventAggregationItems
from .audit_event_analytics_collection import AuditEventAnalyticsCollection
from .audit_event_collection import AuditEventCollection
from .audit_event_summary import AuditEventSummary
from .audit_policy import AuditPolicy
from .audit_policy_aggregation_items import AuditPolicyAggregationItems
from .audit_policy_analytic_collection import AuditPolicyAnalyticCollection
from .audit_policy_collection import AuditPolicyCollection
from .audit_policy_dimensions import AuditPolicyDimensions
from .audit_policy_summary import AuditPolicySummary
from .audit_profile import AuditProfile
from .audit_profile_aggregation_items import AuditProfileAggregationItems
from .audit_profile_analytic_collection import AuditProfileAnalyticCollection
from .audit_profile_collection import AuditProfileCollection
from .audit_profile_dimensions import AuditProfileDimensions
from .audit_profile_summary import AuditProfileSummary
from .audit_specification import AuditSpecification
from .audit_trail import AuditTrail
from .audit_trail_aggregation_items import AuditTrailAggregationItems
from .audit_trail_analytic_collection import AuditTrailAnalyticCollection
from .audit_trail_collection import AuditTrailCollection
from .audit_trail_dimensions import AuditTrailDimensions
from .audit_trail_summary import AuditTrailSummary
from .autonomous_database_details import AutonomousDatabaseDetails
from .available_audit_volume_collection import AvailableAuditVolumeCollection
from .available_audit_volume_summary import AvailableAuditVolumeSummary
from .calculate_audit_volume_available_details import CalculateAuditVolumeAvailableDetails
from .calculate_audit_volume_collected_details import CalculateAuditVolumeCollectedDetails
from .change_alert_compartment_details import ChangeAlertCompartmentDetails
from .change_alert_policy_compartment_details import ChangeAlertPolicyCompartmentDetails
from .change_audit_archive_retrieval_compartment_details import ChangeAuditArchiveRetrievalCompartmentDetails
from .change_audit_policy_compartment_details import ChangeAuditPolicyCompartmentDetails
from .change_audit_profile_compartment_details import ChangeAuditProfileCompartmentDetails
from .change_data_safe_private_endpoint_compartment_details import ChangeDataSafePrivateEndpointCompartmentDetails
from .change_discovery_job_compartment_details import ChangeDiscoveryJobCompartmentDetails
from .change_library_masking_format_compartment_details import ChangeLibraryMaskingFormatCompartmentDetails
from .change_masking_policy_compartment_details import ChangeMaskingPolicyCompartmentDetails
from .change_on_prem_connector_compartment_details import ChangeOnPremConnectorCompartmentDetails
from .change_report_compartment_details import ChangeReportCompartmentDetails
from .change_report_definition_compartment_details import ChangeReportDefinitionCompartmentDetails
from .change_retention_details import ChangeRetentionDetails
from .change_security_assessment_compartment_details import ChangeSecurityAssessmentCompartmentDetails
from .change_sensitive_data_model_compartment_details import ChangeSensitiveDataModelCompartmentDetails
from .change_sensitive_type_compartment_details import ChangeSensitiveTypeCompartmentDetails
from .change_target_alert_policy_association_compartment_details import ChangeTargetAlertPolicyAssociationCompartmentDetails
from .change_target_database_compartment_details import ChangeTargetDatabaseCompartmentDetails
from .change_user_assessment_compartment_details import ChangeUserAssessmentCompartmentDetails
from .collected_audit_volume_collection import CollectedAuditVolumeCollection
from .collected_audit_volume_summary import CollectedAuditVolumeSummary
from .column import Column
from .column_filter import ColumnFilter
from .column_sorting import ColumnSorting
from .column_source_details import ColumnSourceDetails
from .column_source_from_sdm_details import ColumnSourceFromSdmDetails
from .column_source_from_target_details import ColumnSourceFromTargetDetails
from .column_summary import ColumnSummary
from .compare_security_assessment_details import CompareSecurityAssessmentDetails
from .compare_user_assessment_details import CompareUserAssessmentDetails
from .compatible_formats_for_data_types import CompatibleFormatsForDataTypes
from .compatible_formats_for_sensitive_types import CompatibleFormatsForSensitiveTypes
from .connection_option import ConnectionOption
from .create_alert_policy_details import CreateAlertPolicyDetails
from .create_alert_policy_rule_details import CreateAlertPolicyRuleDetails
from .create_audit_archive_retrieval_details import CreateAuditArchiveRetrievalDetails
from .create_audit_policy_details import CreateAuditPolicyDetails
from .create_audit_profile_details import CreateAuditProfileDetails
from .create_column_source_details import CreateColumnSourceDetails
from .create_column_source_from_sdm_details import CreateColumnSourceFromSdmDetails
from .create_column_source_from_target_details import CreateColumnSourceFromTargetDetails
from .create_data_safe_private_endpoint_details import CreateDataSafePrivateEndpointDetails
from .create_discovery_job_details import CreateDiscoveryJobDetails
from .create_library_masking_format_details import CreateLibraryMaskingFormatDetails
from .create_masking_column_details import CreateMaskingColumnDetails
from .create_masking_policy_details import CreateMaskingPolicyDetails
from .create_on_prem_connector_details import CreateOnPremConnectorDetails
from .create_report_definition_details import CreateReportDefinitionDetails
from .create_security_assessment_details import CreateSecurityAssessmentDetails
from .create_sensitive_category_details import CreateSensitiveCategoryDetails
from .create_sensitive_column_details import CreateSensitiveColumnDetails
from .create_sensitive_data_model_details import CreateSensitiveDataModelDetails
from .create_sensitive_type_details import CreateSensitiveTypeDetails
from .create_sensitive_type_pattern_details import CreateSensitiveTypePatternDetails
from .create_target_alert_policy_association_details import CreateTargetAlertPolicyAssociationDetails
from .create_target_database_details import CreateTargetDatabaseDetails
from .create_user_assessment_details import CreateUserAssessmentDetails
from .credentials import Credentials
from .data_safe_configuration import DataSafeConfiguration
from .data_safe_private_endpoint import DataSafePrivateEndpoint
from .data_safe_private_endpoint_summary import DataSafePrivateEndpointSummary
from .database_cloud_service_details import DatabaseCloudServiceDetails
from .database_details import DatabaseDetails
from .delete_rows_format_entry import DeleteRowsFormatEntry
from .deterministic_encryption_date_format_entry import DeterministicEncryptionDateFormatEntry
from .deterministic_encryption_format_entry import DeterministicEncryptionFormatEntry
from .deterministic_substitution_format_entry import DeterministicSubstitutionFormatEntry
from .diffs import Diffs
from .dimensions import Dimensions
from .discovery_analytics_collection import DiscoveryAnalyticsCollection
from .discovery_analytics_summary import DiscoveryAnalyticsSummary
from .discovery_job import DiscoveryJob
from .discovery_job_collection import DiscoveryJobCollection
from .discovery_job_result import DiscoveryJobResult
from .discovery_job_result_collection import DiscoveryJobResultCollection
from .discovery_job_result_summary import DiscoveryJobResultSummary
from .discovery_job_summary import DiscoveryJobSummary
from .download_discovery_report_details import DownloadDiscoveryReportDetails
from .download_masking_log_details import DownloadMaskingLogDetails
from .download_masking_policy_details import DownloadMaskingPolicyDetails
from .download_masking_report_details import DownloadMaskingReportDetails
from .download_security_assessment_report_details import DownloadSecurityAssessmentReportDetails
from .download_sensitive_data_model_details import DownloadSensitiveDataModelDetails
from .download_user_assessment_report_details import DownloadUserAssessmentReportDetails
from .enable_conditions import EnableConditions
from .enable_data_safe_configuration_details import EnableDataSafeConfigurationDetails
from .finding import Finding
from .finding_summary import FindingSummary
from .fixed_number_format_entry import FixedNumberFormatEntry
from .fixed_string_format_entry import FixedStringFormatEntry
from .format_entry import FormatEntry
from .format_summary import FormatSummary
from .formats_for_data_type import FormatsForDataType
from .formats_for_sensitive_type import FormatsForSensitiveType
from .generate_discovery_report_for_download_details import GenerateDiscoveryReportForDownloadDetails
from .generate_masking_policy_for_download_details import GenerateMaskingPolicyForDownloadDetails
from .generate_masking_report_for_download_details import GenerateMaskingReportForDownloadDetails
from .generate_on_prem_connector_configuration_details import GenerateOnPremConnectorConfigurationDetails
from .generate_report_details import GenerateReportDetails
from .generate_security_assessment_report_details import GenerateSecurityAssessmentReportDetails
from .generate_sensitive_data_model_for_download_details import GenerateSensitiveDataModelForDownloadDetails
from .generate_user_assessment_report_details import GenerateUserAssessmentReportDetails
from .global_settings import GlobalSettings
from .grant_summary import GrantSummary
from .initialization_parameter import InitializationParameter
from .installed_database_details import InstalledDatabaseDetails
from .library_masking_format import LibraryMaskingFormat
from .library_masking_format_collection import LibraryMaskingFormatCollection
from .library_masking_format_entry import LibraryMaskingFormatEntry
from .library_masking_format_summary import LibraryMaskingFormatSummary
from .mask_data_details import MaskDataDetails
from .masked_column_collection import MaskedColumnCollection
from .masked_column_summary import MaskedColumnSummary
from .masking_analytics_collection import MaskingAnalyticsCollection
from .masking_analytics_dimensions import MaskingAnalyticsDimensions
from .masking_analytics_summary import MaskingAnalyticsSummary
from .masking_column import MaskingColumn
from .masking_column_collection import MaskingColumnCollection
from .masking_column_summary import MaskingColumnSummary
from .masking_format import MaskingFormat
from .masking_policy import MaskingPolicy
from .masking_policy_collection import MaskingPolicyCollection
from .masking_policy_summary import MaskingPolicySummary
from .masking_report import MaskingReport
from .masking_report_collection import MaskingReportCollection
from .masking_report_summary import MaskingReportSummary
from .modified_attributes import ModifiedAttributes
from .modify_global_settings_details import ModifyGlobalSettingsDetails
from .null_value_format_entry import NullValueFormatEntry
from .on_prem_connector import OnPremConnector
from .on_prem_connector_summary import OnPremConnectorSummary
from .on_premise_connector import OnPremiseConnector
from .ppf_format_entry import PPFFormatEntry
from .patch_alert_policy_rule_details import PatchAlertPolicyRuleDetails
from .patch_alerts_details import PatchAlertsDetails
from .patch_discovery_job_result_details import PatchDiscoveryJobResultDetails
from .patch_insert_instruction import PatchInsertInstruction
from .patch_instruction import PatchInstruction
from .patch_masking_columns_details import PatchMaskingColumnsDetails
from .patch_merge_instruction import PatchMergeInstruction
from .patch_remove_instruction import PatchRemoveInstruction
from .patch_sensitive_column_details import PatchSensitiveColumnDetails
from .preserve_original_data_format_entry import PreserveOriginalDataFormatEntry
from .private_endpoint import PrivateEndpoint
from .profile_details import ProfileDetails
from .provision_audit_conditions import ProvisionAuditConditions
from .provision_audit_policy_details import ProvisionAuditPolicyDetails
from .random_date_format_entry import RandomDateFormatEntry
from .random_decimal_number_format_entry import RandomDecimalNumberFormatEntry
from .random_digits_format_entry import RandomDigitsFormatEntry
from .random_list_format_entry import RandomListFormatEntry
from .random_number_format_entry import RandomNumberFormatEntry
from .random_string_format_entry import RandomStringFormatEntry
from .random_substitution_format_entry import RandomSubstitutionFormatEntry
from .references import References
from .regular_expression_format_entry import RegularExpressionFormatEntry
from .report import Report
from .report_collection import ReportCollection
from .report_definition import ReportDefinition
from .report_definition_collection import ReportDefinitionCollection
from .report_definition_summary import ReportDefinitionSummary
from .report_summary import ReportSummary
from .role_summary import RoleSummary
from .run_security_assessment_details import RunSecurityAssessmentDetails
from .run_user_assessment_details import RunUserAssessmentDetails
from .sql_expression_format_entry import SQLExpressionFormatEntry
from .schema_summary import SchemaSummary
from .section_statistics import SectionStatistics
from .security_assessment import SecurityAssessment
from .security_assessment_base_line_details import SecurityAssessmentBaseLineDetails
from .security_assessment_comparison import SecurityAssessmentComparison
from .security_assessment_comparison_per_target import SecurityAssessmentComparisonPerTarget
from .security_assessment_statistics import SecurityAssessmentStatistics
from .security_assessment_summary import SecurityAssessmentSummary
from .sensitive_category import SensitiveCategory
from .sensitive_column import SensitiveColumn
from .sensitive_column_collection import SensitiveColumnCollection
from .sensitive_column_summary import SensitiveColumnSummary
from .sensitive_data_model import SensitiveDataModel
from .sensitive_data_model_collection import SensitiveDataModelCollection
from .sensitive_data_model_summary import SensitiveDataModelSummary
from .sensitive_type import SensitiveType
from .sensitive_type_collection import SensitiveTypeCollection
from .sensitive_type_pattern import SensitiveTypePattern
from .sensitive_type_summary import SensitiveTypeSummary
from .shuffle_format_entry import ShuffleFormatEntry
from .start_audit_trail_details import StartAuditTrailDetails
from .substring_format_entry import SubstringFormatEntry
from .summary import Summary
from .table_summary import TableSummary
from .target_alert_policy_association import TargetAlertPolicyAssociation
from .target_alert_policy_association_collection import TargetAlertPolicyAssociationCollection
from .target_alert_policy_association_summary import TargetAlertPolicyAssociationSummary
from .target_database import TargetDatabase
from .target_database_summary import TargetDatabaseSummary
from .tls_config import TlsConfig
from .truncate_table_format_entry import TruncateTableFormatEntry
from .udf_format_entry import UDFFormatEntry
from .update_alert_details import UpdateAlertDetails
from .update_alert_policy_rule_details import UpdateAlertPolicyRuleDetails
from .update_audit_archive_retrieval_details import UpdateAuditArchiveRetrievalDetails
from .update_audit_policy_details import UpdateAuditPolicyDetails
from .update_audit_profile_details import UpdateAuditProfileDetails
from .update_audit_trail_details import UpdateAuditTrailDetails
from .update_column_source_details import UpdateColumnSourceDetails
from .update_column_source_sdm_details import UpdateColumnSourceSdmDetails
from .update_column_source_target_details import UpdateColumnSourceTargetDetails
from .update_data_safe_private_endpoint_details import UpdateDataSafePrivateEndpointDetails
from .update_library_masking_format_details import UpdateLibraryMaskingFormatDetails
from .update_masking_column_details import UpdateMaskingColumnDetails
from .update_masking_policy_details import UpdateMaskingPolicyDetails
from .update_on_prem_connector_details import UpdateOnPremConnectorDetails
from .update_on_prem_connector_wallet_details import UpdateOnPremConnectorWalletDetails
from .update_report_definition_details import UpdateReportDefinitionDetails
from .update_security_assessment_details import UpdateSecurityAssessmentDetails
from .update_sensitive_category_details import UpdateSensitiveCategoryDetails
from .update_sensitive_column_details import UpdateSensitiveColumnDetails
from .update_sensitive_data_model_details import UpdateSensitiveDataModelDetails
from .update_sensitive_type_details import UpdateSensitiveTypeDetails
from .update_sensitive_type_pattern_details import UpdateSensitiveTypePatternDetails
from .update_target_alert_policy_association_details import UpdateTargetAlertPolicyAssociationDetails
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
    "Alert": Alert,
    "AlertAggregationItems": AlertAggregationItems,
    "AlertAnalyticsCollection": AlertAnalyticsCollection,
    "AlertCollection": AlertCollection,
    "AlertPolicy": AlertPolicy,
    "AlertPolicyCollection": AlertPolicyCollection,
    "AlertPolicyRule": AlertPolicyRule,
    "AlertPolicyRuleCollection": AlertPolicyRuleCollection,
    "AlertPolicyRuleSummary": AlertPolicyRuleSummary,
    "AlertPolicySummary": AlertPolicySummary,
    "AlertSummary": AlertSummary,
    "AlertsAggregationDimension": AlertsAggregationDimension,
    "ApplyDiscoveryJobResultsDetails": ApplyDiscoveryJobResultsDetails,
    "AuditArchiveRetrieval": AuditArchiveRetrieval,
    "AuditArchiveRetrievalCollection": AuditArchiveRetrievalCollection,
    "AuditArchiveRetrievalSummary": AuditArchiveRetrievalSummary,
    "AuditConditions": AuditConditions,
    "AuditEventAggregationDimensions": AuditEventAggregationDimensions,
    "AuditEventAggregationItems": AuditEventAggregationItems,
    "AuditEventAnalyticsCollection": AuditEventAnalyticsCollection,
    "AuditEventCollection": AuditEventCollection,
    "AuditEventSummary": AuditEventSummary,
    "AuditPolicy": AuditPolicy,
    "AuditPolicyAggregationItems": AuditPolicyAggregationItems,
    "AuditPolicyAnalyticCollection": AuditPolicyAnalyticCollection,
    "AuditPolicyCollection": AuditPolicyCollection,
    "AuditPolicyDimensions": AuditPolicyDimensions,
    "AuditPolicySummary": AuditPolicySummary,
    "AuditProfile": AuditProfile,
    "AuditProfileAggregationItems": AuditProfileAggregationItems,
    "AuditProfileAnalyticCollection": AuditProfileAnalyticCollection,
    "AuditProfileCollection": AuditProfileCollection,
    "AuditProfileDimensions": AuditProfileDimensions,
    "AuditProfileSummary": AuditProfileSummary,
    "AuditSpecification": AuditSpecification,
    "AuditTrail": AuditTrail,
    "AuditTrailAggregationItems": AuditTrailAggregationItems,
    "AuditTrailAnalyticCollection": AuditTrailAnalyticCollection,
    "AuditTrailCollection": AuditTrailCollection,
    "AuditTrailDimensions": AuditTrailDimensions,
    "AuditTrailSummary": AuditTrailSummary,
    "AutonomousDatabaseDetails": AutonomousDatabaseDetails,
    "AvailableAuditVolumeCollection": AvailableAuditVolumeCollection,
    "AvailableAuditVolumeSummary": AvailableAuditVolumeSummary,
    "CalculateAuditVolumeAvailableDetails": CalculateAuditVolumeAvailableDetails,
    "CalculateAuditVolumeCollectedDetails": CalculateAuditVolumeCollectedDetails,
    "ChangeAlertCompartmentDetails": ChangeAlertCompartmentDetails,
    "ChangeAlertPolicyCompartmentDetails": ChangeAlertPolicyCompartmentDetails,
    "ChangeAuditArchiveRetrievalCompartmentDetails": ChangeAuditArchiveRetrievalCompartmentDetails,
    "ChangeAuditPolicyCompartmentDetails": ChangeAuditPolicyCompartmentDetails,
    "ChangeAuditProfileCompartmentDetails": ChangeAuditProfileCompartmentDetails,
    "ChangeDataSafePrivateEndpointCompartmentDetails": ChangeDataSafePrivateEndpointCompartmentDetails,
    "ChangeDiscoveryJobCompartmentDetails": ChangeDiscoveryJobCompartmentDetails,
    "ChangeLibraryMaskingFormatCompartmentDetails": ChangeLibraryMaskingFormatCompartmentDetails,
    "ChangeMaskingPolicyCompartmentDetails": ChangeMaskingPolicyCompartmentDetails,
    "ChangeOnPremConnectorCompartmentDetails": ChangeOnPremConnectorCompartmentDetails,
    "ChangeReportCompartmentDetails": ChangeReportCompartmentDetails,
    "ChangeReportDefinitionCompartmentDetails": ChangeReportDefinitionCompartmentDetails,
    "ChangeRetentionDetails": ChangeRetentionDetails,
    "ChangeSecurityAssessmentCompartmentDetails": ChangeSecurityAssessmentCompartmentDetails,
    "ChangeSensitiveDataModelCompartmentDetails": ChangeSensitiveDataModelCompartmentDetails,
    "ChangeSensitiveTypeCompartmentDetails": ChangeSensitiveTypeCompartmentDetails,
    "ChangeTargetAlertPolicyAssociationCompartmentDetails": ChangeTargetAlertPolicyAssociationCompartmentDetails,
    "ChangeTargetDatabaseCompartmentDetails": ChangeTargetDatabaseCompartmentDetails,
    "ChangeUserAssessmentCompartmentDetails": ChangeUserAssessmentCompartmentDetails,
    "CollectedAuditVolumeCollection": CollectedAuditVolumeCollection,
    "CollectedAuditVolumeSummary": CollectedAuditVolumeSummary,
    "Column": Column,
    "ColumnFilter": ColumnFilter,
    "ColumnSorting": ColumnSorting,
    "ColumnSourceDetails": ColumnSourceDetails,
    "ColumnSourceFromSdmDetails": ColumnSourceFromSdmDetails,
    "ColumnSourceFromTargetDetails": ColumnSourceFromTargetDetails,
    "ColumnSummary": ColumnSummary,
    "CompareSecurityAssessmentDetails": CompareSecurityAssessmentDetails,
    "CompareUserAssessmentDetails": CompareUserAssessmentDetails,
    "CompatibleFormatsForDataTypes": CompatibleFormatsForDataTypes,
    "CompatibleFormatsForSensitiveTypes": CompatibleFormatsForSensitiveTypes,
    "ConnectionOption": ConnectionOption,
    "CreateAlertPolicyDetails": CreateAlertPolicyDetails,
    "CreateAlertPolicyRuleDetails": CreateAlertPolicyRuleDetails,
    "CreateAuditArchiveRetrievalDetails": CreateAuditArchiveRetrievalDetails,
    "CreateAuditPolicyDetails": CreateAuditPolicyDetails,
    "CreateAuditProfileDetails": CreateAuditProfileDetails,
    "CreateColumnSourceDetails": CreateColumnSourceDetails,
    "CreateColumnSourceFromSdmDetails": CreateColumnSourceFromSdmDetails,
    "CreateColumnSourceFromTargetDetails": CreateColumnSourceFromTargetDetails,
    "CreateDataSafePrivateEndpointDetails": CreateDataSafePrivateEndpointDetails,
    "CreateDiscoveryJobDetails": CreateDiscoveryJobDetails,
    "CreateLibraryMaskingFormatDetails": CreateLibraryMaskingFormatDetails,
    "CreateMaskingColumnDetails": CreateMaskingColumnDetails,
    "CreateMaskingPolicyDetails": CreateMaskingPolicyDetails,
    "CreateOnPremConnectorDetails": CreateOnPremConnectorDetails,
    "CreateReportDefinitionDetails": CreateReportDefinitionDetails,
    "CreateSecurityAssessmentDetails": CreateSecurityAssessmentDetails,
    "CreateSensitiveCategoryDetails": CreateSensitiveCategoryDetails,
    "CreateSensitiveColumnDetails": CreateSensitiveColumnDetails,
    "CreateSensitiveDataModelDetails": CreateSensitiveDataModelDetails,
    "CreateSensitiveTypeDetails": CreateSensitiveTypeDetails,
    "CreateSensitiveTypePatternDetails": CreateSensitiveTypePatternDetails,
    "CreateTargetAlertPolicyAssociationDetails": CreateTargetAlertPolicyAssociationDetails,
    "CreateTargetDatabaseDetails": CreateTargetDatabaseDetails,
    "CreateUserAssessmentDetails": CreateUserAssessmentDetails,
    "Credentials": Credentials,
    "DataSafeConfiguration": DataSafeConfiguration,
    "DataSafePrivateEndpoint": DataSafePrivateEndpoint,
    "DataSafePrivateEndpointSummary": DataSafePrivateEndpointSummary,
    "DatabaseCloudServiceDetails": DatabaseCloudServiceDetails,
    "DatabaseDetails": DatabaseDetails,
    "DeleteRowsFormatEntry": DeleteRowsFormatEntry,
    "DeterministicEncryptionDateFormatEntry": DeterministicEncryptionDateFormatEntry,
    "DeterministicEncryptionFormatEntry": DeterministicEncryptionFormatEntry,
    "DeterministicSubstitutionFormatEntry": DeterministicSubstitutionFormatEntry,
    "Diffs": Diffs,
    "Dimensions": Dimensions,
    "DiscoveryAnalyticsCollection": DiscoveryAnalyticsCollection,
    "DiscoveryAnalyticsSummary": DiscoveryAnalyticsSummary,
    "DiscoveryJob": DiscoveryJob,
    "DiscoveryJobCollection": DiscoveryJobCollection,
    "DiscoveryJobResult": DiscoveryJobResult,
    "DiscoveryJobResultCollection": DiscoveryJobResultCollection,
    "DiscoveryJobResultSummary": DiscoveryJobResultSummary,
    "DiscoveryJobSummary": DiscoveryJobSummary,
    "DownloadDiscoveryReportDetails": DownloadDiscoveryReportDetails,
    "DownloadMaskingLogDetails": DownloadMaskingLogDetails,
    "DownloadMaskingPolicyDetails": DownloadMaskingPolicyDetails,
    "DownloadMaskingReportDetails": DownloadMaskingReportDetails,
    "DownloadSecurityAssessmentReportDetails": DownloadSecurityAssessmentReportDetails,
    "DownloadSensitiveDataModelDetails": DownloadSensitiveDataModelDetails,
    "DownloadUserAssessmentReportDetails": DownloadUserAssessmentReportDetails,
    "EnableConditions": EnableConditions,
    "EnableDataSafeConfigurationDetails": EnableDataSafeConfigurationDetails,
    "Finding": Finding,
    "FindingSummary": FindingSummary,
    "FixedNumberFormatEntry": FixedNumberFormatEntry,
    "FixedStringFormatEntry": FixedStringFormatEntry,
    "FormatEntry": FormatEntry,
    "FormatSummary": FormatSummary,
    "FormatsForDataType": FormatsForDataType,
    "FormatsForSensitiveType": FormatsForSensitiveType,
    "GenerateDiscoveryReportForDownloadDetails": GenerateDiscoveryReportForDownloadDetails,
    "GenerateMaskingPolicyForDownloadDetails": GenerateMaskingPolicyForDownloadDetails,
    "GenerateMaskingReportForDownloadDetails": GenerateMaskingReportForDownloadDetails,
    "GenerateOnPremConnectorConfigurationDetails": GenerateOnPremConnectorConfigurationDetails,
    "GenerateReportDetails": GenerateReportDetails,
    "GenerateSecurityAssessmentReportDetails": GenerateSecurityAssessmentReportDetails,
    "GenerateSensitiveDataModelForDownloadDetails": GenerateSensitiveDataModelForDownloadDetails,
    "GenerateUserAssessmentReportDetails": GenerateUserAssessmentReportDetails,
    "GlobalSettings": GlobalSettings,
    "GrantSummary": GrantSummary,
    "InitializationParameter": InitializationParameter,
    "InstalledDatabaseDetails": InstalledDatabaseDetails,
    "LibraryMaskingFormat": LibraryMaskingFormat,
    "LibraryMaskingFormatCollection": LibraryMaskingFormatCollection,
    "LibraryMaskingFormatEntry": LibraryMaskingFormatEntry,
    "LibraryMaskingFormatSummary": LibraryMaskingFormatSummary,
    "MaskDataDetails": MaskDataDetails,
    "MaskedColumnCollection": MaskedColumnCollection,
    "MaskedColumnSummary": MaskedColumnSummary,
    "MaskingAnalyticsCollection": MaskingAnalyticsCollection,
    "MaskingAnalyticsDimensions": MaskingAnalyticsDimensions,
    "MaskingAnalyticsSummary": MaskingAnalyticsSummary,
    "MaskingColumn": MaskingColumn,
    "MaskingColumnCollection": MaskingColumnCollection,
    "MaskingColumnSummary": MaskingColumnSummary,
    "MaskingFormat": MaskingFormat,
    "MaskingPolicy": MaskingPolicy,
    "MaskingPolicyCollection": MaskingPolicyCollection,
    "MaskingPolicySummary": MaskingPolicySummary,
    "MaskingReport": MaskingReport,
    "MaskingReportCollection": MaskingReportCollection,
    "MaskingReportSummary": MaskingReportSummary,
    "ModifiedAttributes": ModifiedAttributes,
    "ModifyGlobalSettingsDetails": ModifyGlobalSettingsDetails,
    "NullValueFormatEntry": NullValueFormatEntry,
    "OnPremConnector": OnPremConnector,
    "OnPremConnectorSummary": OnPremConnectorSummary,
    "OnPremiseConnector": OnPremiseConnector,
    "PPFFormatEntry": PPFFormatEntry,
    "PatchAlertPolicyRuleDetails": PatchAlertPolicyRuleDetails,
    "PatchAlertsDetails": PatchAlertsDetails,
    "PatchDiscoveryJobResultDetails": PatchDiscoveryJobResultDetails,
    "PatchInsertInstruction": PatchInsertInstruction,
    "PatchInstruction": PatchInstruction,
    "PatchMaskingColumnsDetails": PatchMaskingColumnsDetails,
    "PatchMergeInstruction": PatchMergeInstruction,
    "PatchRemoveInstruction": PatchRemoveInstruction,
    "PatchSensitiveColumnDetails": PatchSensitiveColumnDetails,
    "PreserveOriginalDataFormatEntry": PreserveOriginalDataFormatEntry,
    "PrivateEndpoint": PrivateEndpoint,
    "ProfileDetails": ProfileDetails,
    "ProvisionAuditConditions": ProvisionAuditConditions,
    "ProvisionAuditPolicyDetails": ProvisionAuditPolicyDetails,
    "RandomDateFormatEntry": RandomDateFormatEntry,
    "RandomDecimalNumberFormatEntry": RandomDecimalNumberFormatEntry,
    "RandomDigitsFormatEntry": RandomDigitsFormatEntry,
    "RandomListFormatEntry": RandomListFormatEntry,
    "RandomNumberFormatEntry": RandomNumberFormatEntry,
    "RandomStringFormatEntry": RandomStringFormatEntry,
    "RandomSubstitutionFormatEntry": RandomSubstitutionFormatEntry,
    "References": References,
    "RegularExpressionFormatEntry": RegularExpressionFormatEntry,
    "Report": Report,
    "ReportCollection": ReportCollection,
    "ReportDefinition": ReportDefinition,
    "ReportDefinitionCollection": ReportDefinitionCollection,
    "ReportDefinitionSummary": ReportDefinitionSummary,
    "ReportSummary": ReportSummary,
    "RoleSummary": RoleSummary,
    "RunSecurityAssessmentDetails": RunSecurityAssessmentDetails,
    "RunUserAssessmentDetails": RunUserAssessmentDetails,
    "SQLExpressionFormatEntry": SQLExpressionFormatEntry,
    "SchemaSummary": SchemaSummary,
    "SectionStatistics": SectionStatistics,
    "SecurityAssessment": SecurityAssessment,
    "SecurityAssessmentBaseLineDetails": SecurityAssessmentBaseLineDetails,
    "SecurityAssessmentComparison": SecurityAssessmentComparison,
    "SecurityAssessmentComparisonPerTarget": SecurityAssessmentComparisonPerTarget,
    "SecurityAssessmentStatistics": SecurityAssessmentStatistics,
    "SecurityAssessmentSummary": SecurityAssessmentSummary,
    "SensitiveCategory": SensitiveCategory,
    "SensitiveColumn": SensitiveColumn,
    "SensitiveColumnCollection": SensitiveColumnCollection,
    "SensitiveColumnSummary": SensitiveColumnSummary,
    "SensitiveDataModel": SensitiveDataModel,
    "SensitiveDataModelCollection": SensitiveDataModelCollection,
    "SensitiveDataModelSummary": SensitiveDataModelSummary,
    "SensitiveType": SensitiveType,
    "SensitiveTypeCollection": SensitiveTypeCollection,
    "SensitiveTypePattern": SensitiveTypePattern,
    "SensitiveTypeSummary": SensitiveTypeSummary,
    "ShuffleFormatEntry": ShuffleFormatEntry,
    "StartAuditTrailDetails": StartAuditTrailDetails,
    "SubstringFormatEntry": SubstringFormatEntry,
    "Summary": Summary,
    "TableSummary": TableSummary,
    "TargetAlertPolicyAssociation": TargetAlertPolicyAssociation,
    "TargetAlertPolicyAssociationCollection": TargetAlertPolicyAssociationCollection,
    "TargetAlertPolicyAssociationSummary": TargetAlertPolicyAssociationSummary,
    "TargetDatabase": TargetDatabase,
    "TargetDatabaseSummary": TargetDatabaseSummary,
    "TlsConfig": TlsConfig,
    "TruncateTableFormatEntry": TruncateTableFormatEntry,
    "UDFFormatEntry": UDFFormatEntry,
    "UpdateAlertDetails": UpdateAlertDetails,
    "UpdateAlertPolicyRuleDetails": UpdateAlertPolicyRuleDetails,
    "UpdateAuditArchiveRetrievalDetails": UpdateAuditArchiveRetrievalDetails,
    "UpdateAuditPolicyDetails": UpdateAuditPolicyDetails,
    "UpdateAuditProfileDetails": UpdateAuditProfileDetails,
    "UpdateAuditTrailDetails": UpdateAuditTrailDetails,
    "UpdateColumnSourceDetails": UpdateColumnSourceDetails,
    "UpdateColumnSourceSdmDetails": UpdateColumnSourceSdmDetails,
    "UpdateColumnSourceTargetDetails": UpdateColumnSourceTargetDetails,
    "UpdateDataSafePrivateEndpointDetails": UpdateDataSafePrivateEndpointDetails,
    "UpdateLibraryMaskingFormatDetails": UpdateLibraryMaskingFormatDetails,
    "UpdateMaskingColumnDetails": UpdateMaskingColumnDetails,
    "UpdateMaskingPolicyDetails": UpdateMaskingPolicyDetails,
    "UpdateOnPremConnectorDetails": UpdateOnPremConnectorDetails,
    "UpdateOnPremConnectorWalletDetails": UpdateOnPremConnectorWalletDetails,
    "UpdateReportDefinitionDetails": UpdateReportDefinitionDetails,
    "UpdateSecurityAssessmentDetails": UpdateSecurityAssessmentDetails,
    "UpdateSensitiveCategoryDetails": UpdateSensitiveCategoryDetails,
    "UpdateSensitiveColumnDetails": UpdateSensitiveColumnDetails,
    "UpdateSensitiveDataModelDetails": UpdateSensitiveDataModelDetails,
    "UpdateSensitiveTypeDetails": UpdateSensitiveTypeDetails,
    "UpdateSensitiveTypePatternDetails": UpdateSensitiveTypePatternDetails,
    "UpdateTargetAlertPolicyAssociationDetails": UpdateTargetAlertPolicyAssociationDetails,
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
