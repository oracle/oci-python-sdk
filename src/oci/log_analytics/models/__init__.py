# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .abstract_column import AbstractColumn
from .abstract_command_descriptor import AbstractCommandDescriptor
from .abstract_field import AbstractField
from .abstract_parser_test_result_log_entry import AbstractParserTestResultLogEntry
from .abstract_parser_test_result_log_line import AbstractParserTestResultLogLine
from .action import Action
from .add_entity_association_details import AddEntityAssociationDetails
from .add_fields_command_descriptor import AddFieldsCommandDescriptor
from .archiving_configuration import ArchivingConfiguration
from .argument import Argument
from .association_summary_report import AssociationSummaryReport
from .auto_lookups import AutoLookups
from .bottom_command_descriptor import BottomCommandDescriptor
from .bucket_command_descriptor import BucketCommandDescriptor
from .bucket_range import BucketRange
from .change_log_analytics_entity_compartment_details import ChangeLogAnalyticsEntityCompartmentDetails
from .change_log_analytics_log_group_compartment_details import ChangeLogAnalyticsLogGroupCompartmentDetails
from .change_log_analytics_object_collection_rule_compartment_details import ChangeLogAnalyticsObjectCollectionRuleCompartmentDetails
from .change_scheduled_task_compartment_details import ChangeScheduledTaskCompartmentDetails
from .char_encoding_collection import CharEncodingCollection
from .chart_column import ChartColumn
from .chart_data_column import ChartDataColumn
from .classify_column import ClassifyColumn
from .classify_command_descriptor import ClassifyCommandDescriptor
from .cluster_command_descriptor import ClusterCommandDescriptor
from .cluster_compare_command_descriptor import ClusterCompareCommandDescriptor
from .cluster_details_command_descriptor import ClusterDetailsCommandDescriptor
from .cluster_split_command_descriptor import ClusterSplitCommandDescriptor
from .column import Column
from .column_name import ColumnName
from .column_name_collection import ColumnNameCollection
from .command_descriptor import CommandDescriptor
from .create_acceleration_task_details import CreateAccelerationTaskDetails
from .create_log_analytics_entity_details import CreateLogAnalyticsEntityDetails
from .create_log_analytics_entity_type_details import CreateLogAnalyticsEntityTypeDetails
from .create_log_analytics_log_group_details import CreateLogAnalyticsLogGroupDetails
from .create_log_analytics_object_collection_rule_details import CreateLogAnalyticsObjectCollectionRuleDetails
from .create_scheduled_task_details import CreateScheduledTaskDetails
from .create_standard_task_details import CreateStandardTaskDetails
from .cron_schedule import CronSchedule
from .delete_command_descriptor import DeleteCommandDescriptor
from .delete_log_analytics_association import DeleteLogAnalyticsAssociation
from .delete_log_analytics_association_details import DeleteLogAnalyticsAssociationDetails
from .delta_command_descriptor import DeltaCommandDescriptor
from .demo_mode_command_descriptor import DemoModeCommandDescriptor
from .distinct_command_descriptor import DistinctCommandDescriptor
from .efd_regex_result import EfdRegexResult
from .entity_type_property import EntityTypeProperty
from .error_details import ErrorDetails
from .estimate_purge_data_size_details import EstimatePurgeDataSizeDetails
from .estimate_purge_data_size_result import EstimatePurgeDataSizeResult
from .eval_command_descriptor import EvalCommandDescriptor
from .event_stats_command_descriptor import EventStatsCommandDescriptor
from .export_content import ExportContent
from .export_details import ExportDetails
from .extended_fields_validation_result import ExtendedFieldsValidationResult
from .extract_command_descriptor import ExtractCommandDescriptor
from .extract_log_field_results import ExtractLogFieldResults
from .extract_log_header_details import ExtractLogHeaderDetails
from .extract_log_header_results import ExtractLogHeaderResults
from .field import Field
from .field_argument import FieldArgument
from .field_summary_command_descriptor import FieldSummaryCommandDescriptor
from .field_summary_report import FieldSummaryReport
from .field_value import FieldValue
from .fields_add_remove_field import FieldsAddRemoveField
from .fields_command_descriptor import FieldsCommandDescriptor
from .file_validation_response import FileValidationResponse
from .filter import Filter
from .filter_details import FilterDetails
from .filter_output import FilterOutput
from .fixed_frequency_schedule import FixedFrequencySchedule
from .function_field import FunctionField
from .head_command_descriptor import HeadCommandDescriptor
from .highlight_command_descriptor import HighlightCommandDescriptor
from .highlight_rows_command_descriptor import HighlightRowsCommandDescriptor
from .indexes import Indexes
from .label_names import LabelNames
from .label_priority import LabelPriority
from .label_priority_collection import LabelPriorityCollection
from .label_source_collection import LabelSourceCollection
from .label_source_summary import LabelSourceSummary
from .label_summary_report import LabelSummaryReport
from .link_command_descriptor import LinkCommandDescriptor
from .link_details_command_descriptor import LinkDetailsCommandDescriptor
from .literal_argument import LiteralArgument
from .log_analytics_associated_entity import LogAnalyticsAssociatedEntity
from .log_analytics_associated_entity_collection import LogAnalyticsAssociatedEntityCollection
from .log_analytics_association import LogAnalyticsAssociation
from .log_analytics_association_collection import LogAnalyticsAssociationCollection
from .log_analytics_association_parameter import LogAnalyticsAssociationParameter
from .log_analytics_association_parameter_collection import LogAnalyticsAssociationParameterCollection
from .log_analytics_config_work_request import LogAnalyticsConfigWorkRequest
from .log_analytics_config_work_request_collection import LogAnalyticsConfigWorkRequestCollection
from .log_analytics_config_work_request_payload import LogAnalyticsConfigWorkRequestPayload
from .log_analytics_config_work_request_summary import LogAnalyticsConfigWorkRequestSummary
from .log_analytics_entity import LogAnalyticsEntity
from .log_analytics_entity_collection import LogAnalyticsEntityCollection
from .log_analytics_entity_summary import LogAnalyticsEntitySummary
from .log_analytics_entity_summary_report import LogAnalyticsEntitySummaryReport
from .log_analytics_entity_type import LogAnalyticsEntityType
from .log_analytics_entity_type_collection import LogAnalyticsEntityTypeCollection
from .log_analytics_entity_type_summary import LogAnalyticsEntityTypeSummary
from .log_analytics_extended_field import LogAnalyticsExtendedField
from .log_analytics_field import LogAnalyticsField
from .log_analytics_field_collection import LogAnalyticsFieldCollection
from .log_analytics_field_summary import LogAnalyticsFieldSummary
from .log_analytics_import_custom_change_list import LogAnalyticsImportCustomChangeList
from .log_analytics_import_custom_content import LogAnalyticsImportCustomContent
from .log_analytics_label import LogAnalyticsLabel
from .log_analytics_label_alias import LogAnalyticsLabelAlias
from .log_analytics_label_collection import LogAnalyticsLabelCollection
from .log_analytics_label_definition import LogAnalyticsLabelDefinition
from .log_analytics_label_operator import LogAnalyticsLabelOperator
from .log_analytics_label_operator_collection import LogAnalyticsLabelOperatorCollection
from .log_analytics_label_summary import LogAnalyticsLabelSummary
from .log_analytics_label_view import LogAnalyticsLabelView
from .log_analytics_log_group import LogAnalyticsLogGroup
from .log_analytics_log_group_summary import LogAnalyticsLogGroupSummary
from .log_analytics_log_group_summary_collection import LogAnalyticsLogGroupSummaryCollection
from .log_analytics_lookup import LogAnalyticsLookup
from .log_analytics_meta_function import LogAnalyticsMetaFunction
from .log_analytics_meta_function_argument import LogAnalyticsMetaFunctionArgument
from .log_analytics_meta_function_collection import LogAnalyticsMetaFunctionCollection
from .log_analytics_meta_source_type import LogAnalyticsMetaSourceType
from .log_analytics_meta_source_type_collection import LogAnalyticsMetaSourceTypeCollection
from .log_analytics_metric import LogAnalyticsMetric
from .log_analytics_object_collection_rule import LogAnalyticsObjectCollectionRule
from .log_analytics_object_collection_rule_collection import LogAnalyticsObjectCollectionRuleCollection
from .log_analytics_object_collection_rule_summary import LogAnalyticsObjectCollectionRuleSummary
from .log_analytics_parameter import LogAnalyticsParameter
from .log_analytics_parser import LogAnalyticsParser
from .log_analytics_parser_collection import LogAnalyticsParserCollection
from .log_analytics_parser_field import LogAnalyticsParserField
from .log_analytics_parser_filter import LogAnalyticsParserFilter
from .log_analytics_parser_function import LogAnalyticsParserFunction
from .log_analytics_parser_function_collection import LogAnalyticsParserFunctionCollection
from .log_analytics_parser_function_parameter import LogAnalyticsParserFunctionParameter
from .log_analytics_parser_meta_plugin import LogAnalyticsParserMetaPlugin
from .log_analytics_parser_meta_plugin_collection import LogAnalyticsParserMetaPluginCollection
from .log_analytics_parser_meta_plugin_parameter import LogAnalyticsParserMetaPluginParameter
from .log_analytics_parser_summary import LogAnalyticsParserSummary
from .log_analytics_pattern_filter import LogAnalyticsPatternFilter
from .log_analytics_source import LogAnalyticsSource
from .log_analytics_source_collection import LogAnalyticsSourceCollection
from .log_analytics_source_data_filter import LogAnalyticsSourceDataFilter
from .log_analytics_source_entity_type import LogAnalyticsSourceEntityType
from .log_analytics_source_extended_field_definition import LogAnalyticsSourceExtendedFieldDefinition
from .log_analytics_source_extended_field_definition_collection import LogAnalyticsSourceExtendedFieldDefinitionCollection
from .log_analytics_source_function import LogAnalyticsSourceFunction
from .log_analytics_source_label_condition import LogAnalyticsSourceLabelCondition
from .log_analytics_source_metadata_field import LogAnalyticsSourceMetadataField
from .log_analytics_source_metric import LogAnalyticsSourceMetric
from .log_analytics_source_pattern import LogAnalyticsSourcePattern
from .log_analytics_source_pattern_collection import LogAnalyticsSourcePatternCollection
from .log_analytics_source_summary import LogAnalyticsSourceSummary
from .log_group_summary_report import LogGroupSummaryReport
from .lookup_command_descriptor import LookupCommandDescriptor
from .lookup_field import LookupField
from .macro_command_descriptor import MacroCommandDescriptor
from .match_info import MatchInfo
from .multi_search_command_descriptor import MultiSearchCommandDescriptor
from .namespace import Namespace
from .namespace_collection import NamespaceCollection
from .namespace_summary import NamespaceSummary
from .parse_query_details import ParseQueryDetails
from .parse_query_output import ParseQueryOutput
from .parsed_content import ParsedContent
from .parsed_field import ParsedField
from .parser_summary_report import ParserSummaryReport
from .parser_test_result import ParserTestResult
from .property_override import PropertyOverride
from .purge_action import PurgeAction
from .purge_storage_data_details import PurgeStorageDataDetails
from .query_aggregation import QueryAggregation
from .query_details import QueryDetails
from .query_work_request import QueryWorkRequest
from .query_work_request_collection import QueryWorkRequestCollection
from .query_work_request_summary import QueryWorkRequestSummary
from .recall_archived_data_details import RecallArchivedDataDetails
from .regex_command_descriptor import RegexCommandDescriptor
from .regex_match_result import RegexMatchResult
from .release_recalled_data_details import ReleaseRecalledDataDetails
from .remove_entity_associations_details import RemoveEntityAssociationsDetails
from .rename_command_descriptor import RenameCommandDescriptor
from .result_column import ResultColumn
from .schedule import Schedule
from .scheduled_task import ScheduledTask
from .scheduled_task_collection import ScheduledTaskCollection
from .scheduled_task_summary import ScheduledTaskSummary
from .scheduler_resource import SchedulerResource
from .scope_filter import ScopeFilter
from .search_command_descriptor import SearchCommandDescriptor
from .search_lookup_command_descriptor import SearchLookupCommandDescriptor
from .sort_command_descriptor import SortCommandDescriptor
from .sort_field import SortField
from .source_mapping_response import SourceMappingResponse
from .source_summary_report import SourceSummaryReport
from .source_validate_details import SourceValidateDetails
from .source_validate_results import SourceValidateResults
from .stats_command_descriptor import StatsCommandDescriptor
from .status_summary import StatusSummary
from .step_info import StepInfo
from .storage import Storage
from .storage_usage import StorageUsage
from .storage_work_request import StorageWorkRequest
from .storage_work_request_collection import StorageWorkRequestCollection
from .storage_work_request_summary import StorageWorkRequestSummary
from .stream_action import StreamAction
from .success import Success
from .suggest_details import SuggestDetails
from .suggest_output import SuggestOutput
from .tail_command_descriptor import TailCommandDescriptor
from .test_parser_payload_details import TestParserPayloadDetails
from .time_column import TimeColumn
from .time_compare_command_descriptor import TimeCompareCommandDescriptor
from .time_range import TimeRange
from .time_stats_command_descriptor import TimeStatsCommandDescriptor
from .timezone_collection import TimezoneCollection
from .top_command_descriptor import TopCommandDescriptor
from .trend_column import TrendColumn
from .ui_parser_test_metadata import UiParserTestMetadata
from .update_log_analytics_entity_details import UpdateLogAnalyticsEntityDetails
from .update_log_analytics_entity_type_details import UpdateLogAnalyticsEntityTypeDetails
from .update_log_analytics_log_group_details import UpdateLogAnalyticsLogGroupDetails
from .update_log_analytics_object_collection_rule_details import UpdateLogAnalyticsObjectCollectionRuleDetails
from .update_scheduled_task_details import UpdateScheduledTaskDetails
from .update_storage_details import UpdateStorageDetails
from .upload import Upload
from .upload_collection import UploadCollection
from .upload_file_collection import UploadFileCollection
from .upload_file_status import UploadFileStatus
from .upload_file_summary import UploadFileSummary
from .upload_summary import UploadSummary
from .upload_warning_collection import UploadWarningCollection
from .upload_warning_summary import UploadWarningSummary
from .upsert_log_analytics_association import UpsertLogAnalyticsAssociation
from .upsert_log_analytics_association_details import UpsertLogAnalyticsAssociationDetails
from .upsert_log_analytics_field_details import UpsertLogAnalyticsFieldDetails
from .upsert_log_analytics_label_details import UpsertLogAnalyticsLabelDetails
from .upsert_log_analytics_parser_details import UpsertLogAnalyticsParserDetails
from .upsert_log_analytics_source_details import UpsertLogAnalyticsSourceDetails
from .usage_status_item import UsageStatusItem
from .verify_output import VerifyOutput
from .violation import Violation
from .where_command_descriptor import WhereCommandDescriptor
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log import WorkRequestLog
from .work_request_log_collection import WorkRequestLogCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for log_analytics services.
log_analytics_type_mapping = {
    "AbstractColumn": AbstractColumn,
    "AbstractCommandDescriptor": AbstractCommandDescriptor,
    "AbstractField": AbstractField,
    "AbstractParserTestResultLogEntry": AbstractParserTestResultLogEntry,
    "AbstractParserTestResultLogLine": AbstractParserTestResultLogLine,
    "Action": Action,
    "AddEntityAssociationDetails": AddEntityAssociationDetails,
    "AddFieldsCommandDescriptor": AddFieldsCommandDescriptor,
    "ArchivingConfiguration": ArchivingConfiguration,
    "Argument": Argument,
    "AssociationSummaryReport": AssociationSummaryReport,
    "AutoLookups": AutoLookups,
    "BottomCommandDescriptor": BottomCommandDescriptor,
    "BucketCommandDescriptor": BucketCommandDescriptor,
    "BucketRange": BucketRange,
    "ChangeLogAnalyticsEntityCompartmentDetails": ChangeLogAnalyticsEntityCompartmentDetails,
    "ChangeLogAnalyticsLogGroupCompartmentDetails": ChangeLogAnalyticsLogGroupCompartmentDetails,
    "ChangeLogAnalyticsObjectCollectionRuleCompartmentDetails": ChangeLogAnalyticsObjectCollectionRuleCompartmentDetails,
    "ChangeScheduledTaskCompartmentDetails": ChangeScheduledTaskCompartmentDetails,
    "CharEncodingCollection": CharEncodingCollection,
    "ChartColumn": ChartColumn,
    "ChartDataColumn": ChartDataColumn,
    "ClassifyColumn": ClassifyColumn,
    "ClassifyCommandDescriptor": ClassifyCommandDescriptor,
    "ClusterCommandDescriptor": ClusterCommandDescriptor,
    "ClusterCompareCommandDescriptor": ClusterCompareCommandDescriptor,
    "ClusterDetailsCommandDescriptor": ClusterDetailsCommandDescriptor,
    "ClusterSplitCommandDescriptor": ClusterSplitCommandDescriptor,
    "Column": Column,
    "ColumnName": ColumnName,
    "ColumnNameCollection": ColumnNameCollection,
    "CommandDescriptor": CommandDescriptor,
    "CreateAccelerationTaskDetails": CreateAccelerationTaskDetails,
    "CreateLogAnalyticsEntityDetails": CreateLogAnalyticsEntityDetails,
    "CreateLogAnalyticsEntityTypeDetails": CreateLogAnalyticsEntityTypeDetails,
    "CreateLogAnalyticsLogGroupDetails": CreateLogAnalyticsLogGroupDetails,
    "CreateLogAnalyticsObjectCollectionRuleDetails": CreateLogAnalyticsObjectCollectionRuleDetails,
    "CreateScheduledTaskDetails": CreateScheduledTaskDetails,
    "CreateStandardTaskDetails": CreateStandardTaskDetails,
    "CronSchedule": CronSchedule,
    "DeleteCommandDescriptor": DeleteCommandDescriptor,
    "DeleteLogAnalyticsAssociation": DeleteLogAnalyticsAssociation,
    "DeleteLogAnalyticsAssociationDetails": DeleteLogAnalyticsAssociationDetails,
    "DeltaCommandDescriptor": DeltaCommandDescriptor,
    "DemoModeCommandDescriptor": DemoModeCommandDescriptor,
    "DistinctCommandDescriptor": DistinctCommandDescriptor,
    "EfdRegexResult": EfdRegexResult,
    "EntityTypeProperty": EntityTypeProperty,
    "ErrorDetails": ErrorDetails,
    "EstimatePurgeDataSizeDetails": EstimatePurgeDataSizeDetails,
    "EstimatePurgeDataSizeResult": EstimatePurgeDataSizeResult,
    "EvalCommandDescriptor": EvalCommandDescriptor,
    "EventStatsCommandDescriptor": EventStatsCommandDescriptor,
    "ExportContent": ExportContent,
    "ExportDetails": ExportDetails,
    "ExtendedFieldsValidationResult": ExtendedFieldsValidationResult,
    "ExtractCommandDescriptor": ExtractCommandDescriptor,
    "ExtractLogFieldResults": ExtractLogFieldResults,
    "ExtractLogHeaderDetails": ExtractLogHeaderDetails,
    "ExtractLogHeaderResults": ExtractLogHeaderResults,
    "Field": Field,
    "FieldArgument": FieldArgument,
    "FieldSummaryCommandDescriptor": FieldSummaryCommandDescriptor,
    "FieldSummaryReport": FieldSummaryReport,
    "FieldValue": FieldValue,
    "FieldsAddRemoveField": FieldsAddRemoveField,
    "FieldsCommandDescriptor": FieldsCommandDescriptor,
    "FileValidationResponse": FileValidationResponse,
    "Filter": Filter,
    "FilterDetails": FilterDetails,
    "FilterOutput": FilterOutput,
    "FixedFrequencySchedule": FixedFrequencySchedule,
    "FunctionField": FunctionField,
    "HeadCommandDescriptor": HeadCommandDescriptor,
    "HighlightCommandDescriptor": HighlightCommandDescriptor,
    "HighlightRowsCommandDescriptor": HighlightRowsCommandDescriptor,
    "Indexes": Indexes,
    "LabelNames": LabelNames,
    "LabelPriority": LabelPriority,
    "LabelPriorityCollection": LabelPriorityCollection,
    "LabelSourceCollection": LabelSourceCollection,
    "LabelSourceSummary": LabelSourceSummary,
    "LabelSummaryReport": LabelSummaryReport,
    "LinkCommandDescriptor": LinkCommandDescriptor,
    "LinkDetailsCommandDescriptor": LinkDetailsCommandDescriptor,
    "LiteralArgument": LiteralArgument,
    "LogAnalyticsAssociatedEntity": LogAnalyticsAssociatedEntity,
    "LogAnalyticsAssociatedEntityCollection": LogAnalyticsAssociatedEntityCollection,
    "LogAnalyticsAssociation": LogAnalyticsAssociation,
    "LogAnalyticsAssociationCollection": LogAnalyticsAssociationCollection,
    "LogAnalyticsAssociationParameter": LogAnalyticsAssociationParameter,
    "LogAnalyticsAssociationParameterCollection": LogAnalyticsAssociationParameterCollection,
    "LogAnalyticsConfigWorkRequest": LogAnalyticsConfigWorkRequest,
    "LogAnalyticsConfigWorkRequestCollection": LogAnalyticsConfigWorkRequestCollection,
    "LogAnalyticsConfigWorkRequestPayload": LogAnalyticsConfigWorkRequestPayload,
    "LogAnalyticsConfigWorkRequestSummary": LogAnalyticsConfigWorkRequestSummary,
    "LogAnalyticsEntity": LogAnalyticsEntity,
    "LogAnalyticsEntityCollection": LogAnalyticsEntityCollection,
    "LogAnalyticsEntitySummary": LogAnalyticsEntitySummary,
    "LogAnalyticsEntitySummaryReport": LogAnalyticsEntitySummaryReport,
    "LogAnalyticsEntityType": LogAnalyticsEntityType,
    "LogAnalyticsEntityTypeCollection": LogAnalyticsEntityTypeCollection,
    "LogAnalyticsEntityTypeSummary": LogAnalyticsEntityTypeSummary,
    "LogAnalyticsExtendedField": LogAnalyticsExtendedField,
    "LogAnalyticsField": LogAnalyticsField,
    "LogAnalyticsFieldCollection": LogAnalyticsFieldCollection,
    "LogAnalyticsFieldSummary": LogAnalyticsFieldSummary,
    "LogAnalyticsImportCustomChangeList": LogAnalyticsImportCustomChangeList,
    "LogAnalyticsImportCustomContent": LogAnalyticsImportCustomContent,
    "LogAnalyticsLabel": LogAnalyticsLabel,
    "LogAnalyticsLabelAlias": LogAnalyticsLabelAlias,
    "LogAnalyticsLabelCollection": LogAnalyticsLabelCollection,
    "LogAnalyticsLabelDefinition": LogAnalyticsLabelDefinition,
    "LogAnalyticsLabelOperator": LogAnalyticsLabelOperator,
    "LogAnalyticsLabelOperatorCollection": LogAnalyticsLabelOperatorCollection,
    "LogAnalyticsLabelSummary": LogAnalyticsLabelSummary,
    "LogAnalyticsLabelView": LogAnalyticsLabelView,
    "LogAnalyticsLogGroup": LogAnalyticsLogGroup,
    "LogAnalyticsLogGroupSummary": LogAnalyticsLogGroupSummary,
    "LogAnalyticsLogGroupSummaryCollection": LogAnalyticsLogGroupSummaryCollection,
    "LogAnalyticsLookup": LogAnalyticsLookup,
    "LogAnalyticsMetaFunction": LogAnalyticsMetaFunction,
    "LogAnalyticsMetaFunctionArgument": LogAnalyticsMetaFunctionArgument,
    "LogAnalyticsMetaFunctionCollection": LogAnalyticsMetaFunctionCollection,
    "LogAnalyticsMetaSourceType": LogAnalyticsMetaSourceType,
    "LogAnalyticsMetaSourceTypeCollection": LogAnalyticsMetaSourceTypeCollection,
    "LogAnalyticsMetric": LogAnalyticsMetric,
    "LogAnalyticsObjectCollectionRule": LogAnalyticsObjectCollectionRule,
    "LogAnalyticsObjectCollectionRuleCollection": LogAnalyticsObjectCollectionRuleCollection,
    "LogAnalyticsObjectCollectionRuleSummary": LogAnalyticsObjectCollectionRuleSummary,
    "LogAnalyticsParameter": LogAnalyticsParameter,
    "LogAnalyticsParser": LogAnalyticsParser,
    "LogAnalyticsParserCollection": LogAnalyticsParserCollection,
    "LogAnalyticsParserField": LogAnalyticsParserField,
    "LogAnalyticsParserFilter": LogAnalyticsParserFilter,
    "LogAnalyticsParserFunction": LogAnalyticsParserFunction,
    "LogAnalyticsParserFunctionCollection": LogAnalyticsParserFunctionCollection,
    "LogAnalyticsParserFunctionParameter": LogAnalyticsParserFunctionParameter,
    "LogAnalyticsParserMetaPlugin": LogAnalyticsParserMetaPlugin,
    "LogAnalyticsParserMetaPluginCollection": LogAnalyticsParserMetaPluginCollection,
    "LogAnalyticsParserMetaPluginParameter": LogAnalyticsParserMetaPluginParameter,
    "LogAnalyticsParserSummary": LogAnalyticsParserSummary,
    "LogAnalyticsPatternFilter": LogAnalyticsPatternFilter,
    "LogAnalyticsSource": LogAnalyticsSource,
    "LogAnalyticsSourceCollection": LogAnalyticsSourceCollection,
    "LogAnalyticsSourceDataFilter": LogAnalyticsSourceDataFilter,
    "LogAnalyticsSourceEntityType": LogAnalyticsSourceEntityType,
    "LogAnalyticsSourceExtendedFieldDefinition": LogAnalyticsSourceExtendedFieldDefinition,
    "LogAnalyticsSourceExtendedFieldDefinitionCollection": LogAnalyticsSourceExtendedFieldDefinitionCollection,
    "LogAnalyticsSourceFunction": LogAnalyticsSourceFunction,
    "LogAnalyticsSourceLabelCondition": LogAnalyticsSourceLabelCondition,
    "LogAnalyticsSourceMetadataField": LogAnalyticsSourceMetadataField,
    "LogAnalyticsSourceMetric": LogAnalyticsSourceMetric,
    "LogAnalyticsSourcePattern": LogAnalyticsSourcePattern,
    "LogAnalyticsSourcePatternCollection": LogAnalyticsSourcePatternCollection,
    "LogAnalyticsSourceSummary": LogAnalyticsSourceSummary,
    "LogGroupSummaryReport": LogGroupSummaryReport,
    "LookupCommandDescriptor": LookupCommandDescriptor,
    "LookupField": LookupField,
    "MacroCommandDescriptor": MacroCommandDescriptor,
    "MatchInfo": MatchInfo,
    "MultiSearchCommandDescriptor": MultiSearchCommandDescriptor,
    "Namespace": Namespace,
    "NamespaceCollection": NamespaceCollection,
    "NamespaceSummary": NamespaceSummary,
    "ParseQueryDetails": ParseQueryDetails,
    "ParseQueryOutput": ParseQueryOutput,
    "ParsedContent": ParsedContent,
    "ParsedField": ParsedField,
    "ParserSummaryReport": ParserSummaryReport,
    "ParserTestResult": ParserTestResult,
    "PropertyOverride": PropertyOverride,
    "PurgeAction": PurgeAction,
    "PurgeStorageDataDetails": PurgeStorageDataDetails,
    "QueryAggregation": QueryAggregation,
    "QueryDetails": QueryDetails,
    "QueryWorkRequest": QueryWorkRequest,
    "QueryWorkRequestCollection": QueryWorkRequestCollection,
    "QueryWorkRequestSummary": QueryWorkRequestSummary,
    "RecallArchivedDataDetails": RecallArchivedDataDetails,
    "RegexCommandDescriptor": RegexCommandDescriptor,
    "RegexMatchResult": RegexMatchResult,
    "ReleaseRecalledDataDetails": ReleaseRecalledDataDetails,
    "RemoveEntityAssociationsDetails": RemoveEntityAssociationsDetails,
    "RenameCommandDescriptor": RenameCommandDescriptor,
    "ResultColumn": ResultColumn,
    "Schedule": Schedule,
    "ScheduledTask": ScheduledTask,
    "ScheduledTaskCollection": ScheduledTaskCollection,
    "ScheduledTaskSummary": ScheduledTaskSummary,
    "SchedulerResource": SchedulerResource,
    "ScopeFilter": ScopeFilter,
    "SearchCommandDescriptor": SearchCommandDescriptor,
    "SearchLookupCommandDescriptor": SearchLookupCommandDescriptor,
    "SortCommandDescriptor": SortCommandDescriptor,
    "SortField": SortField,
    "SourceMappingResponse": SourceMappingResponse,
    "SourceSummaryReport": SourceSummaryReport,
    "SourceValidateDetails": SourceValidateDetails,
    "SourceValidateResults": SourceValidateResults,
    "StatsCommandDescriptor": StatsCommandDescriptor,
    "StatusSummary": StatusSummary,
    "StepInfo": StepInfo,
    "Storage": Storage,
    "StorageUsage": StorageUsage,
    "StorageWorkRequest": StorageWorkRequest,
    "StorageWorkRequestCollection": StorageWorkRequestCollection,
    "StorageWorkRequestSummary": StorageWorkRequestSummary,
    "StreamAction": StreamAction,
    "Success": Success,
    "SuggestDetails": SuggestDetails,
    "SuggestOutput": SuggestOutput,
    "TailCommandDescriptor": TailCommandDescriptor,
    "TestParserPayloadDetails": TestParserPayloadDetails,
    "TimeColumn": TimeColumn,
    "TimeCompareCommandDescriptor": TimeCompareCommandDescriptor,
    "TimeRange": TimeRange,
    "TimeStatsCommandDescriptor": TimeStatsCommandDescriptor,
    "TimezoneCollection": TimezoneCollection,
    "TopCommandDescriptor": TopCommandDescriptor,
    "TrendColumn": TrendColumn,
    "UiParserTestMetadata": UiParserTestMetadata,
    "UpdateLogAnalyticsEntityDetails": UpdateLogAnalyticsEntityDetails,
    "UpdateLogAnalyticsEntityTypeDetails": UpdateLogAnalyticsEntityTypeDetails,
    "UpdateLogAnalyticsLogGroupDetails": UpdateLogAnalyticsLogGroupDetails,
    "UpdateLogAnalyticsObjectCollectionRuleDetails": UpdateLogAnalyticsObjectCollectionRuleDetails,
    "UpdateScheduledTaskDetails": UpdateScheduledTaskDetails,
    "UpdateStorageDetails": UpdateStorageDetails,
    "Upload": Upload,
    "UploadCollection": UploadCollection,
    "UploadFileCollection": UploadFileCollection,
    "UploadFileStatus": UploadFileStatus,
    "UploadFileSummary": UploadFileSummary,
    "UploadSummary": UploadSummary,
    "UploadWarningCollection": UploadWarningCollection,
    "UploadWarningSummary": UploadWarningSummary,
    "UpsertLogAnalyticsAssociation": UpsertLogAnalyticsAssociation,
    "UpsertLogAnalyticsAssociationDetails": UpsertLogAnalyticsAssociationDetails,
    "UpsertLogAnalyticsFieldDetails": UpsertLogAnalyticsFieldDetails,
    "UpsertLogAnalyticsLabelDetails": UpsertLogAnalyticsLabelDetails,
    "UpsertLogAnalyticsParserDetails": UpsertLogAnalyticsParserDetails,
    "UpsertLogAnalyticsSourceDetails": UpsertLogAnalyticsSourceDetails,
    "UsageStatusItem": UsageStatusItem,
    "VerifyOutput": VerifyOutput,
    "Violation": Violation,
    "WhereCommandDescriptor": WhereCommandDescriptor,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestLogCollection": WorkRequestLogCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
