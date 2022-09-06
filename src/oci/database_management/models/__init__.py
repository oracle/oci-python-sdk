# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activity_time_series_metrics import ActivityTimeSeriesMetrics
from .add_data_files_details import AddDataFilesDetails
from .add_managed_database_to_managed_database_group_details import AddManagedDatabaseToManagedDatabaseGroupDetails
from .addm_task_summary import AddmTaskSummary
from .addm_tasks_collection import AddmTasksCollection
from .advisor_rule import AdvisorRule
from .alert_log_collection import AlertLogCollection
from .alert_log_count_summary import AlertLogCountSummary
from .alert_log_counts_collection import AlertLogCountsCollection
from .alert_log_summary import AlertLogSummary
from .allowed_parameter_value import AllowedParameterValue
from .asm_property import AsmProperty
from .asm_property_collection import AsmPropertyCollection
from .asm_property_summary import AsmPropertySummary
from .associated_database_collection import AssociatedDatabaseCollection
from .associated_database_summary import AssociatedDatabaseSummary
from .attention_log_collection import AttentionLogCollection
from .attention_log_count_summary import AttentionLogCountSummary
from .attention_log_counts_collection import AttentionLogCountsCollection
from .attention_log_summary import AttentionLogSummary
from .awr_db_collection import AwrDbCollection
from .awr_db_cpu_usage_collection import AwrDbCpuUsageCollection
from .awr_db_cpu_usage_summary import AwrDbCpuUsageSummary
from .awr_db_metric_collection import AwrDbMetricCollection
from .awr_db_metric_summary import AwrDbMetricSummary
from .awr_db_parameter_change_collection import AwrDbParameterChangeCollection
from .awr_db_parameter_change_summary import AwrDbParameterChangeSummary
from .awr_db_parameter_collection import AwrDbParameterCollection
from .awr_db_parameter_summary import AwrDbParameterSummary
from .awr_db_report import AwrDbReport
from .awr_db_snapshot_collection import AwrDbSnapshotCollection
from .awr_db_snapshot_range_collection import AwrDbSnapshotRangeCollection
from .awr_db_snapshot_range_summary import AwrDbSnapshotRangeSummary
from .awr_db_snapshot_summary import AwrDbSnapshotSummary
from .awr_db_sql_report import AwrDbSqlReport
from .awr_db_summary import AwrDbSummary
from .awr_db_sysstat_collection import AwrDbSysstatCollection
from .awr_db_sysstat_summary import AwrDbSysstatSummary
from .awr_db_top_wait_event_collection import AwrDbTopWaitEventCollection
from .awr_db_top_wait_event_summary import AwrDbTopWaitEventSummary
from .awr_db_wait_event_bucket_collection import AwrDbWaitEventBucketCollection
from .awr_db_wait_event_bucket_summary import AwrDbWaitEventBucketSummary
from .awr_db_wait_event_collection import AwrDbWaitEventCollection
from .awr_db_wait_event_summary import AwrDbWaitEventSummary
from .awr_query_result import AwrQueryResult
from .basic_preferred_credential import BasicPreferredCredential
from .change_database_parameter_details import ChangeDatabaseParameterDetails
from .change_database_parameters_details import ChangeDatabaseParametersDetails
from .change_db_management_private_endpoint_compartment_details import ChangeDbManagementPrivateEndpointCompartmentDetails
from .change_job_compartment_details import ChangeJobCompartmentDetails
from .change_managed_database_group_compartment_details import ChangeManagedDatabaseGroupCompartmentDetails
from .child_database import ChildDatabase
from .clone_sql_tuning_task_details import CloneSqlTuningTaskDetails
from .cluster_cache_metric import ClusterCacheMetric
from .consumer_group_privilege_collection import ConsumerGroupPrivilegeCollection
from .consumer_group_privilege_summary import ConsumerGroupPrivilegeSummary
from .cpu_utilization_aggregate_metrics import CpuUtilizationAggregateMetrics
from .create_db_management_private_endpoint_details import CreateDbManagementPrivateEndpointDetails
from .create_job_details import CreateJobDetails
from .create_managed_database_group_details import CreateManagedDatabaseGroupDetails
from .create_sql_job_details import CreateSqlJobDetails
from .create_tablespace_details import CreateTablespaceDetails
from .data_access_container_collection import DataAccessContainerCollection
from .data_access_container_summary import DataAccessContainerSummary
from .database_credentials import DatabaseCredentials
from .database_fleet_health_metrics import DatabaseFleetHealthMetrics
from .database_home_metric_definition import DatabaseHomeMetricDefinition
from .database_home_metrics import DatabaseHomeMetrics
from .database_io_aggregate_metrics import DatabaseIOAggregateMetrics
from .database_instance_home_metrics_definition import DatabaseInstanceHomeMetricsDefinition
from .database_parameter_summary import DatabaseParameterSummary
from .database_parameter_update_status import DatabaseParameterUpdateStatus
from .database_parameters_collection import DatabaseParametersCollection
from .database_storage_aggregate_metrics import DatabaseStorageAggregateMetrics
from .database_time_aggregate_metrics import DatabaseTimeAggregateMetrics
from .database_usage_metrics import DatabaseUsageMetrics
from .datafile import Datafile
from .db_management_private_endpoint import DbManagementPrivateEndpoint
from .db_management_private_endpoint_collection import DbManagementPrivateEndpointCollection
from .db_management_private_endpoint_summary import DbManagementPrivateEndpointSummary
from .drop_sql_tuning_task_details import DropSqlTuningTaskDetails
from .drop_tablespace_details import DropTablespaceDetails
from .execution_plan_stats_comparision import ExecutionPlanStatsComparision
from .failed_connections_aggregate_metrics import FailedConnectionsAggregateMetrics
from .finding_schema_or_operation import FindingSchemaOrOperation
from .fleet_metric_definition import FleetMetricDefinition
from .fleet_metric_summary_definition import FleetMetricSummaryDefinition
from .fleet_status_by_category import FleetStatusByCategory
from .fleet_summary import FleetSummary
from .historic_addm_result import HistoricAddmResult
from .implement_optimizer_statistics_advisor_recommendations_details import ImplementOptimizerStatisticsAdvisorRecommendationsDetails
from .implement_optimizer_statistics_advisor_recommendations_job import ImplementOptimizerStatisticsAdvisorRecommendationsJob
from .instance_details import InstanceDetails
from .job import Job
from .job_collection import JobCollection
from .job_database import JobDatabase
from .job_execution import JobExecution
from .job_execution_collection import JobExecutionCollection
from .job_execution_result_details import JobExecutionResultDetails
from .job_execution_result_location import JobExecutionResultLocation
from .job_execution_summary import JobExecutionSummary
from .job_executions_status_summary import JobExecutionsStatusSummary
from .job_executions_status_summary_collection import JobExecutionsStatusSummaryCollection
from .job_run import JobRun
from .job_run_collection import JobRunCollection
from .job_run_summary import JobRunSummary
from .job_schedule_details import JobScheduleDetails
from .job_summary import JobSummary
from .managed_database import ManagedDatabase
from .managed_database_collection import ManagedDatabaseCollection
from .managed_database_credential import ManagedDatabaseCredential
from .managed_database_group import ManagedDatabaseGroup
from .managed_database_group_collection import ManagedDatabaseGroupCollection
from .managed_database_group_summary import ManagedDatabaseGroupSummary
from .managed_database_password_credential import ManagedDatabasePasswordCredential
from .managed_database_secret_credential import ManagedDatabaseSecretCredential
from .managed_database_summary import ManagedDatabaseSummary
from .memory_aggregate_metrics import MemoryAggregateMetrics
from .metric_data_point import MetricDataPoint
from .metric_dimension_definition import MetricDimensionDefinition
from .metric_statistics_definition import MetricStatisticsDefinition
from .object_privilege_collection import ObjectPrivilegeCollection
from .object_privilege_summary import ObjectPrivilegeSummary
from .object_storage_job_execution_result_details import ObjectStorageJobExecutionResultDetails
from .object_storage_job_execution_result_location import ObjectStorageJobExecutionResultLocation
from .optimizer_database import OptimizerDatabase
from .optimizer_statistics_advisor_execution import OptimizerStatisticsAdvisorExecution
from .optimizer_statistics_advisor_execution_report import OptimizerStatisticsAdvisorExecutionReport
from .optimizer_statistics_advisor_execution_script import OptimizerStatisticsAdvisorExecutionScript
from .optimizer_statistics_advisor_execution_summary import OptimizerStatisticsAdvisorExecutionSummary
from .optimizer_statistics_advisor_executions_collection import OptimizerStatisticsAdvisorExecutionsCollection
from .optimizer_statistics_collection_aggregation_summary import OptimizerStatisticsCollectionAggregationSummary
from .optimizer_statistics_collection_aggregations_collection import OptimizerStatisticsCollectionAggregationsCollection
from .optimizer_statistics_collection_operation import OptimizerStatisticsCollectionOperation
from .optimizer_statistics_collection_operation_summary import OptimizerStatisticsCollectionOperationSummary
from .optimizer_statistics_collection_operations_collection import OptimizerStatisticsCollectionOperationsCollection
from .optimizer_statistics_operation_task import OptimizerStatisticsOperationTask
from .parent_group import ParentGroup
from .pdb_metrics import PdbMetrics
from .pdb_status_details import PdbStatusDetails
from .preferred_credential import PreferredCredential
from .preferred_credential_collection import PreferredCredentialCollection
from .preferred_credential_summary import PreferredCredentialSummary
from .proxied_for_user_collection import ProxiedForUserCollection
from .proxied_for_user_summary import ProxiedForUserSummary
from .proxy_user_collection import ProxyUserCollection
from .proxy_user_summary import ProxyUserSummary
from .recommendation import Recommendation
from .recommendation_example import RecommendationExample
from .recommendation_example_line import RecommendationExampleLine
from .recommendation_rationale import RecommendationRationale
from .remove_data_file_details import RemoveDataFileDetails
from .remove_managed_database_from_managed_database_group_details import RemoveManagedDatabaseFromManagedDatabaseGroupDetails
from .reset_database_parameters_details import ResetDatabaseParametersDetails
from .resize_data_file_details import ResizeDataFileDetails
from .role_collection import RoleCollection
from .role_summary import RoleSummary
from .rule_finding import RuleFinding
from .run_historic_addm_details import RunHistoricAddmDetails
from .schema_definition import SchemaDefinition
from .snapshot_details import SnapshotDetails
from .sql_job import SqlJob
from .sql_tuning_advisor_task_collection import SqlTuningAdvisorTaskCollection
from .sql_tuning_advisor_task_finding_collection import SqlTuningAdvisorTaskFindingCollection
from .sql_tuning_advisor_task_finding_summary import SqlTuningAdvisorTaskFindingSummary
from .sql_tuning_advisor_task_recommendation_collection import SqlTuningAdvisorTaskRecommendationCollection
from .sql_tuning_advisor_task_recommendation_summary import SqlTuningAdvisorTaskRecommendationSummary
from .sql_tuning_advisor_task_sql_execution_plan import SqlTuningAdvisorTaskSqlExecutionPlan
from .sql_tuning_advisor_task_summary import SqlTuningAdvisorTaskSummary
from .sql_tuning_advisor_task_summary_finding_benefits import SqlTuningAdvisorTaskSummaryFindingBenefits
from .sql_tuning_advisor_task_summary_finding_counts import SqlTuningAdvisorTaskSummaryFindingCounts
from .sql_tuning_advisor_task_summary_report import SqlTuningAdvisorTaskSummaryReport
from .sql_tuning_advisor_task_summary_report_index_finding_summary import SqlTuningAdvisorTaskSummaryReportIndexFindingSummary
from .sql_tuning_advisor_task_summary_report_object_stat_finding_summary import SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary
from .sql_tuning_advisor_task_summary_report_statement_counts import SqlTuningAdvisorTaskSummaryReportStatementCounts
from .sql_tuning_advisor_task_summary_report_statistics import SqlTuningAdvisorTaskSummaryReportStatistics
from .sql_tuning_advisor_task_summary_report_task_info import SqlTuningAdvisorTaskSummaryReportTaskInfo
from .sql_tuning_set_collection import SqlTuningSetCollection
from .sql_tuning_set_input import SqlTuningSetInput
from .sql_tuning_set_summary import SqlTuningSetSummary
from .sql_tuning_task_credential_details import SqlTuningTaskCredentialDetails
from .sql_tuning_task_password_credential_details import SqlTuningTaskPasswordCredentialDetails
from .sql_tuning_task_plan_stats import SqlTuningTaskPlanStats
from .sql_tuning_task_return import SqlTuningTaskReturn
from .sql_tuning_task_secret_credential_details import SqlTuningTaskSecretCredentialDetails
from .sql_tuning_task_sql_detail import SqlTuningTaskSqlDetail
from .sql_tuning_task_sql_execution_plan_step import SqlTuningTaskSqlExecutionPlanStep
from .start_sql_tuning_task_details import StartSqlTuningTaskDetails
from .statements_aggregate_metrics import StatementsAggregateMetrics
from .system_privilege_collection import SystemPrivilegeCollection
from .system_privilege_summary import SystemPrivilegeSummary
from .table_statistic_summary import TableStatisticSummary
from .table_statistics_collection import TableStatisticsCollection
from .tablespace import Tablespace
from .tablespace_admin_credential_details import TablespaceAdminCredentialDetails
from .tablespace_admin_password_credential_details import TablespaceAdminPasswordCredentialDetails
from .tablespace_admin_secret_credential_details import TablespaceAdminSecretCredentialDetails
from .tablespace_admin_status import TablespaceAdminStatus
from .tablespace_collection import TablespaceCollection
from .tablespace_storage_size import TablespaceStorageSize
from .tablespace_summary import TablespaceSummary
from .test_basic_preferred_credential_details import TestBasicPreferredCredentialDetails
from .test_preferred_credential_details import TestPreferredCredentialDetails
from .test_preferred_credential_status import TestPreferredCredentialStatus
from .time_series_metric_data_point import TimeSeriesMetricDataPoint
from .time_series_metric_definition import TimeSeriesMetricDefinition
from .update_basic_preferred_credential_details import UpdateBasicPreferredCredentialDetails
from .update_database_parameters_result import UpdateDatabaseParametersResult
from .update_db_management_private_endpoint_details import UpdateDbManagementPrivateEndpointDetails
from .update_job_details import UpdateJobDetails
from .update_managed_database_group_details import UpdateManagedDatabaseGroupDetails
from .update_preferred_credential_details import UpdatePreferredCredentialDetails
from .update_sql_job_details import UpdateSqlJobDetails
from .update_tablespace_details import UpdateTablespaceDetails
from .user import User
from .user_collection import UserCollection
from .user_summary import UserSummary
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for database_management services.
database_management_type_mapping = {
    "ActivityTimeSeriesMetrics": ActivityTimeSeriesMetrics,
    "AddDataFilesDetails": AddDataFilesDetails,
    "AddManagedDatabaseToManagedDatabaseGroupDetails": AddManagedDatabaseToManagedDatabaseGroupDetails,
    "AddmTaskSummary": AddmTaskSummary,
    "AddmTasksCollection": AddmTasksCollection,
    "AdvisorRule": AdvisorRule,
    "AlertLogCollection": AlertLogCollection,
    "AlertLogCountSummary": AlertLogCountSummary,
    "AlertLogCountsCollection": AlertLogCountsCollection,
    "AlertLogSummary": AlertLogSummary,
    "AllowedParameterValue": AllowedParameterValue,
    "AsmProperty": AsmProperty,
    "AsmPropertyCollection": AsmPropertyCollection,
    "AsmPropertySummary": AsmPropertySummary,
    "AssociatedDatabaseCollection": AssociatedDatabaseCollection,
    "AssociatedDatabaseSummary": AssociatedDatabaseSummary,
    "AttentionLogCollection": AttentionLogCollection,
    "AttentionLogCountSummary": AttentionLogCountSummary,
    "AttentionLogCountsCollection": AttentionLogCountsCollection,
    "AttentionLogSummary": AttentionLogSummary,
    "AwrDbCollection": AwrDbCollection,
    "AwrDbCpuUsageCollection": AwrDbCpuUsageCollection,
    "AwrDbCpuUsageSummary": AwrDbCpuUsageSummary,
    "AwrDbMetricCollection": AwrDbMetricCollection,
    "AwrDbMetricSummary": AwrDbMetricSummary,
    "AwrDbParameterChangeCollection": AwrDbParameterChangeCollection,
    "AwrDbParameterChangeSummary": AwrDbParameterChangeSummary,
    "AwrDbParameterCollection": AwrDbParameterCollection,
    "AwrDbParameterSummary": AwrDbParameterSummary,
    "AwrDbReport": AwrDbReport,
    "AwrDbSnapshotCollection": AwrDbSnapshotCollection,
    "AwrDbSnapshotRangeCollection": AwrDbSnapshotRangeCollection,
    "AwrDbSnapshotRangeSummary": AwrDbSnapshotRangeSummary,
    "AwrDbSnapshotSummary": AwrDbSnapshotSummary,
    "AwrDbSqlReport": AwrDbSqlReport,
    "AwrDbSummary": AwrDbSummary,
    "AwrDbSysstatCollection": AwrDbSysstatCollection,
    "AwrDbSysstatSummary": AwrDbSysstatSummary,
    "AwrDbTopWaitEventCollection": AwrDbTopWaitEventCollection,
    "AwrDbTopWaitEventSummary": AwrDbTopWaitEventSummary,
    "AwrDbWaitEventBucketCollection": AwrDbWaitEventBucketCollection,
    "AwrDbWaitEventBucketSummary": AwrDbWaitEventBucketSummary,
    "AwrDbWaitEventCollection": AwrDbWaitEventCollection,
    "AwrDbWaitEventSummary": AwrDbWaitEventSummary,
    "AwrQueryResult": AwrQueryResult,
    "BasicPreferredCredential": BasicPreferredCredential,
    "ChangeDatabaseParameterDetails": ChangeDatabaseParameterDetails,
    "ChangeDatabaseParametersDetails": ChangeDatabaseParametersDetails,
    "ChangeDbManagementPrivateEndpointCompartmentDetails": ChangeDbManagementPrivateEndpointCompartmentDetails,
    "ChangeJobCompartmentDetails": ChangeJobCompartmentDetails,
    "ChangeManagedDatabaseGroupCompartmentDetails": ChangeManagedDatabaseGroupCompartmentDetails,
    "ChildDatabase": ChildDatabase,
    "CloneSqlTuningTaskDetails": CloneSqlTuningTaskDetails,
    "ClusterCacheMetric": ClusterCacheMetric,
    "ConsumerGroupPrivilegeCollection": ConsumerGroupPrivilegeCollection,
    "ConsumerGroupPrivilegeSummary": ConsumerGroupPrivilegeSummary,
    "CpuUtilizationAggregateMetrics": CpuUtilizationAggregateMetrics,
    "CreateDbManagementPrivateEndpointDetails": CreateDbManagementPrivateEndpointDetails,
    "CreateJobDetails": CreateJobDetails,
    "CreateManagedDatabaseGroupDetails": CreateManagedDatabaseGroupDetails,
    "CreateSqlJobDetails": CreateSqlJobDetails,
    "CreateTablespaceDetails": CreateTablespaceDetails,
    "DataAccessContainerCollection": DataAccessContainerCollection,
    "DataAccessContainerSummary": DataAccessContainerSummary,
    "DatabaseCredentials": DatabaseCredentials,
    "DatabaseFleetHealthMetrics": DatabaseFleetHealthMetrics,
    "DatabaseHomeMetricDefinition": DatabaseHomeMetricDefinition,
    "DatabaseHomeMetrics": DatabaseHomeMetrics,
    "DatabaseIOAggregateMetrics": DatabaseIOAggregateMetrics,
    "DatabaseInstanceHomeMetricsDefinition": DatabaseInstanceHomeMetricsDefinition,
    "DatabaseParameterSummary": DatabaseParameterSummary,
    "DatabaseParameterUpdateStatus": DatabaseParameterUpdateStatus,
    "DatabaseParametersCollection": DatabaseParametersCollection,
    "DatabaseStorageAggregateMetrics": DatabaseStorageAggregateMetrics,
    "DatabaseTimeAggregateMetrics": DatabaseTimeAggregateMetrics,
    "DatabaseUsageMetrics": DatabaseUsageMetrics,
    "Datafile": Datafile,
    "DbManagementPrivateEndpoint": DbManagementPrivateEndpoint,
    "DbManagementPrivateEndpointCollection": DbManagementPrivateEndpointCollection,
    "DbManagementPrivateEndpointSummary": DbManagementPrivateEndpointSummary,
    "DropSqlTuningTaskDetails": DropSqlTuningTaskDetails,
    "DropTablespaceDetails": DropTablespaceDetails,
    "ExecutionPlanStatsComparision": ExecutionPlanStatsComparision,
    "FailedConnectionsAggregateMetrics": FailedConnectionsAggregateMetrics,
    "FindingSchemaOrOperation": FindingSchemaOrOperation,
    "FleetMetricDefinition": FleetMetricDefinition,
    "FleetMetricSummaryDefinition": FleetMetricSummaryDefinition,
    "FleetStatusByCategory": FleetStatusByCategory,
    "FleetSummary": FleetSummary,
    "HistoricAddmResult": HistoricAddmResult,
    "ImplementOptimizerStatisticsAdvisorRecommendationsDetails": ImplementOptimizerStatisticsAdvisorRecommendationsDetails,
    "ImplementOptimizerStatisticsAdvisorRecommendationsJob": ImplementOptimizerStatisticsAdvisorRecommendationsJob,
    "InstanceDetails": InstanceDetails,
    "Job": Job,
    "JobCollection": JobCollection,
    "JobDatabase": JobDatabase,
    "JobExecution": JobExecution,
    "JobExecutionCollection": JobExecutionCollection,
    "JobExecutionResultDetails": JobExecutionResultDetails,
    "JobExecutionResultLocation": JobExecutionResultLocation,
    "JobExecutionSummary": JobExecutionSummary,
    "JobExecutionsStatusSummary": JobExecutionsStatusSummary,
    "JobExecutionsStatusSummaryCollection": JobExecutionsStatusSummaryCollection,
    "JobRun": JobRun,
    "JobRunCollection": JobRunCollection,
    "JobRunSummary": JobRunSummary,
    "JobScheduleDetails": JobScheduleDetails,
    "JobSummary": JobSummary,
    "ManagedDatabase": ManagedDatabase,
    "ManagedDatabaseCollection": ManagedDatabaseCollection,
    "ManagedDatabaseCredential": ManagedDatabaseCredential,
    "ManagedDatabaseGroup": ManagedDatabaseGroup,
    "ManagedDatabaseGroupCollection": ManagedDatabaseGroupCollection,
    "ManagedDatabaseGroupSummary": ManagedDatabaseGroupSummary,
    "ManagedDatabasePasswordCredential": ManagedDatabasePasswordCredential,
    "ManagedDatabaseSecretCredential": ManagedDatabaseSecretCredential,
    "ManagedDatabaseSummary": ManagedDatabaseSummary,
    "MemoryAggregateMetrics": MemoryAggregateMetrics,
    "MetricDataPoint": MetricDataPoint,
    "MetricDimensionDefinition": MetricDimensionDefinition,
    "MetricStatisticsDefinition": MetricStatisticsDefinition,
    "ObjectPrivilegeCollection": ObjectPrivilegeCollection,
    "ObjectPrivilegeSummary": ObjectPrivilegeSummary,
    "ObjectStorageJobExecutionResultDetails": ObjectStorageJobExecutionResultDetails,
    "ObjectStorageJobExecutionResultLocation": ObjectStorageJobExecutionResultLocation,
    "OptimizerDatabase": OptimizerDatabase,
    "OptimizerStatisticsAdvisorExecution": OptimizerStatisticsAdvisorExecution,
    "OptimizerStatisticsAdvisorExecutionReport": OptimizerStatisticsAdvisorExecutionReport,
    "OptimizerStatisticsAdvisorExecutionScript": OptimizerStatisticsAdvisorExecutionScript,
    "OptimizerStatisticsAdvisorExecutionSummary": OptimizerStatisticsAdvisorExecutionSummary,
    "OptimizerStatisticsAdvisorExecutionsCollection": OptimizerStatisticsAdvisorExecutionsCollection,
    "OptimizerStatisticsCollectionAggregationSummary": OptimizerStatisticsCollectionAggregationSummary,
    "OptimizerStatisticsCollectionAggregationsCollection": OptimizerStatisticsCollectionAggregationsCollection,
    "OptimizerStatisticsCollectionOperation": OptimizerStatisticsCollectionOperation,
    "OptimizerStatisticsCollectionOperationSummary": OptimizerStatisticsCollectionOperationSummary,
    "OptimizerStatisticsCollectionOperationsCollection": OptimizerStatisticsCollectionOperationsCollection,
    "OptimizerStatisticsOperationTask": OptimizerStatisticsOperationTask,
    "ParentGroup": ParentGroup,
    "PdbMetrics": PdbMetrics,
    "PdbStatusDetails": PdbStatusDetails,
    "PreferredCredential": PreferredCredential,
    "PreferredCredentialCollection": PreferredCredentialCollection,
    "PreferredCredentialSummary": PreferredCredentialSummary,
    "ProxiedForUserCollection": ProxiedForUserCollection,
    "ProxiedForUserSummary": ProxiedForUserSummary,
    "ProxyUserCollection": ProxyUserCollection,
    "ProxyUserSummary": ProxyUserSummary,
    "Recommendation": Recommendation,
    "RecommendationExample": RecommendationExample,
    "RecommendationExampleLine": RecommendationExampleLine,
    "RecommendationRationale": RecommendationRationale,
    "RemoveDataFileDetails": RemoveDataFileDetails,
    "RemoveManagedDatabaseFromManagedDatabaseGroupDetails": RemoveManagedDatabaseFromManagedDatabaseGroupDetails,
    "ResetDatabaseParametersDetails": ResetDatabaseParametersDetails,
    "ResizeDataFileDetails": ResizeDataFileDetails,
    "RoleCollection": RoleCollection,
    "RoleSummary": RoleSummary,
    "RuleFinding": RuleFinding,
    "RunHistoricAddmDetails": RunHistoricAddmDetails,
    "SchemaDefinition": SchemaDefinition,
    "SnapshotDetails": SnapshotDetails,
    "SqlJob": SqlJob,
    "SqlTuningAdvisorTaskCollection": SqlTuningAdvisorTaskCollection,
    "SqlTuningAdvisorTaskFindingCollection": SqlTuningAdvisorTaskFindingCollection,
    "SqlTuningAdvisorTaskFindingSummary": SqlTuningAdvisorTaskFindingSummary,
    "SqlTuningAdvisorTaskRecommendationCollection": SqlTuningAdvisorTaskRecommendationCollection,
    "SqlTuningAdvisorTaskRecommendationSummary": SqlTuningAdvisorTaskRecommendationSummary,
    "SqlTuningAdvisorTaskSqlExecutionPlan": SqlTuningAdvisorTaskSqlExecutionPlan,
    "SqlTuningAdvisorTaskSummary": SqlTuningAdvisorTaskSummary,
    "SqlTuningAdvisorTaskSummaryFindingBenefits": SqlTuningAdvisorTaskSummaryFindingBenefits,
    "SqlTuningAdvisorTaskSummaryFindingCounts": SqlTuningAdvisorTaskSummaryFindingCounts,
    "SqlTuningAdvisorTaskSummaryReport": SqlTuningAdvisorTaskSummaryReport,
    "SqlTuningAdvisorTaskSummaryReportIndexFindingSummary": SqlTuningAdvisorTaskSummaryReportIndexFindingSummary,
    "SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary": SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary,
    "SqlTuningAdvisorTaskSummaryReportStatementCounts": SqlTuningAdvisorTaskSummaryReportStatementCounts,
    "SqlTuningAdvisorTaskSummaryReportStatistics": SqlTuningAdvisorTaskSummaryReportStatistics,
    "SqlTuningAdvisorTaskSummaryReportTaskInfo": SqlTuningAdvisorTaskSummaryReportTaskInfo,
    "SqlTuningSetCollection": SqlTuningSetCollection,
    "SqlTuningSetInput": SqlTuningSetInput,
    "SqlTuningSetSummary": SqlTuningSetSummary,
    "SqlTuningTaskCredentialDetails": SqlTuningTaskCredentialDetails,
    "SqlTuningTaskPasswordCredentialDetails": SqlTuningTaskPasswordCredentialDetails,
    "SqlTuningTaskPlanStats": SqlTuningTaskPlanStats,
    "SqlTuningTaskReturn": SqlTuningTaskReturn,
    "SqlTuningTaskSecretCredentialDetails": SqlTuningTaskSecretCredentialDetails,
    "SqlTuningTaskSqlDetail": SqlTuningTaskSqlDetail,
    "SqlTuningTaskSqlExecutionPlanStep": SqlTuningTaskSqlExecutionPlanStep,
    "StartSqlTuningTaskDetails": StartSqlTuningTaskDetails,
    "StatementsAggregateMetrics": StatementsAggregateMetrics,
    "SystemPrivilegeCollection": SystemPrivilegeCollection,
    "SystemPrivilegeSummary": SystemPrivilegeSummary,
    "TableStatisticSummary": TableStatisticSummary,
    "TableStatisticsCollection": TableStatisticsCollection,
    "Tablespace": Tablespace,
    "TablespaceAdminCredentialDetails": TablespaceAdminCredentialDetails,
    "TablespaceAdminPasswordCredentialDetails": TablespaceAdminPasswordCredentialDetails,
    "TablespaceAdminSecretCredentialDetails": TablespaceAdminSecretCredentialDetails,
    "TablespaceAdminStatus": TablespaceAdminStatus,
    "TablespaceCollection": TablespaceCollection,
    "TablespaceStorageSize": TablespaceStorageSize,
    "TablespaceSummary": TablespaceSummary,
    "TestBasicPreferredCredentialDetails": TestBasicPreferredCredentialDetails,
    "TestPreferredCredentialDetails": TestPreferredCredentialDetails,
    "TestPreferredCredentialStatus": TestPreferredCredentialStatus,
    "TimeSeriesMetricDataPoint": TimeSeriesMetricDataPoint,
    "TimeSeriesMetricDefinition": TimeSeriesMetricDefinition,
    "UpdateBasicPreferredCredentialDetails": UpdateBasicPreferredCredentialDetails,
    "UpdateDatabaseParametersResult": UpdateDatabaseParametersResult,
    "UpdateDbManagementPrivateEndpointDetails": UpdateDbManagementPrivateEndpointDetails,
    "UpdateJobDetails": UpdateJobDetails,
    "UpdateManagedDatabaseGroupDetails": UpdateManagedDatabaseGroupDetails,
    "UpdatePreferredCredentialDetails": UpdatePreferredCredentialDetails,
    "UpdateSqlJobDetails": UpdateSqlJobDetails,
    "UpdateTablespaceDetails": UpdateTablespaceDetails,
    "User": User,
    "UserCollection": UserCollection,
    "UserSummary": UserSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
