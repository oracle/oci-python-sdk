# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activity_time_series_metrics import ActivityTimeSeriesMetrics
from .add_managed_database_to_managed_database_group_details import AddManagedDatabaseToManagedDatabaseGroupDetails
from .allowed_parameter_value import AllowedParameterValue
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
from .change_database_parameter_details import ChangeDatabaseParameterDetails
from .change_database_parameters_details import ChangeDatabaseParametersDetails
from .change_job_compartment_details import ChangeJobCompartmentDetails
from .change_managed_database_group_compartment_details import ChangeManagedDatabaseGroupCompartmentDetails
from .child_database import ChildDatabase
from .cluster_cache_metric import ClusterCacheMetric
from .create_job_details import CreateJobDetails
from .create_managed_database_group_details import CreateManagedDatabaseGroupDetails
from .create_sql_job_details import CreateSqlJobDetails
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
from .fleet_metric_definition import FleetMetricDefinition
from .fleet_metric_summary_definition import FleetMetricSummaryDefinition
from .fleet_status_by_category import FleetStatusByCategory
from .fleet_summary import FleetSummary
from .instance_details import InstanceDetails
from .job import Job
from .job_collection import JobCollection
from .job_database import JobDatabase
from .job_execution import JobExecution
from .job_execution_collection import JobExecutionCollection
from .job_execution_result_details import JobExecutionResultDetails
from .job_execution_result_location import JobExecutionResultLocation
from .job_execution_summary import JobExecutionSummary
from .job_run import JobRun
from .job_run_collection import JobRunCollection
from .job_run_summary import JobRunSummary
from .job_summary import JobSummary
from .managed_database import ManagedDatabase
from .managed_database_collection import ManagedDatabaseCollection
from .managed_database_group import ManagedDatabaseGroup
from .managed_database_group_collection import ManagedDatabaseGroupCollection
from .managed_database_group_summary import ManagedDatabaseGroupSummary
from .managed_database_summary import ManagedDatabaseSummary
from .memory_aggregate_metrics import MemoryAggregateMetrics
from .metric_data_point import MetricDataPoint
from .metric_dimension_definition import MetricDimensionDefinition
from .object_storage_job_execution_result_details import ObjectStorageJobExecutionResultDetails
from .object_storage_job_execution_result_location import ObjectStorageJobExecutionResultLocation
from .parent_group import ParentGroup
from .pdb_status_details import PdbStatusDetails
from .remove_managed_database_from_managed_database_group_details import RemoveManagedDatabaseFromManagedDatabaseGroupDetails
from .reset_database_parameters_details import ResetDatabaseParametersDetails
from .sql_job import SqlJob
from .tablespace import Tablespace
from .tablespace_collection import TablespaceCollection
from .tablespace_summary import TablespaceSummary
from .time_series_metric_data_point import TimeSeriesMetricDataPoint
from .time_series_metric_definition import TimeSeriesMetricDefinition
from .update_database_parameters_result import UpdateDatabaseParametersResult
from .update_managed_database_group_details import UpdateManagedDatabaseGroupDetails

# Maps type names to classes for database_management services.
database_management_type_mapping = {
    "ActivityTimeSeriesMetrics": ActivityTimeSeriesMetrics,
    "AddManagedDatabaseToManagedDatabaseGroupDetails": AddManagedDatabaseToManagedDatabaseGroupDetails,
    "AllowedParameterValue": AllowedParameterValue,
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
    "ChangeDatabaseParameterDetails": ChangeDatabaseParameterDetails,
    "ChangeDatabaseParametersDetails": ChangeDatabaseParametersDetails,
    "ChangeJobCompartmentDetails": ChangeJobCompartmentDetails,
    "ChangeManagedDatabaseGroupCompartmentDetails": ChangeManagedDatabaseGroupCompartmentDetails,
    "ChildDatabase": ChildDatabase,
    "ClusterCacheMetric": ClusterCacheMetric,
    "CreateJobDetails": CreateJobDetails,
    "CreateManagedDatabaseGroupDetails": CreateManagedDatabaseGroupDetails,
    "CreateSqlJobDetails": CreateSqlJobDetails,
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
    "FleetMetricDefinition": FleetMetricDefinition,
    "FleetMetricSummaryDefinition": FleetMetricSummaryDefinition,
    "FleetStatusByCategory": FleetStatusByCategory,
    "FleetSummary": FleetSummary,
    "InstanceDetails": InstanceDetails,
    "Job": Job,
    "JobCollection": JobCollection,
    "JobDatabase": JobDatabase,
    "JobExecution": JobExecution,
    "JobExecutionCollection": JobExecutionCollection,
    "JobExecutionResultDetails": JobExecutionResultDetails,
    "JobExecutionResultLocation": JobExecutionResultLocation,
    "JobExecutionSummary": JobExecutionSummary,
    "JobRun": JobRun,
    "JobRunCollection": JobRunCollection,
    "JobRunSummary": JobRunSummary,
    "JobSummary": JobSummary,
    "ManagedDatabase": ManagedDatabase,
    "ManagedDatabaseCollection": ManagedDatabaseCollection,
    "ManagedDatabaseGroup": ManagedDatabaseGroup,
    "ManagedDatabaseGroupCollection": ManagedDatabaseGroupCollection,
    "ManagedDatabaseGroupSummary": ManagedDatabaseGroupSummary,
    "ManagedDatabaseSummary": ManagedDatabaseSummary,
    "MemoryAggregateMetrics": MemoryAggregateMetrics,
    "MetricDataPoint": MetricDataPoint,
    "MetricDimensionDefinition": MetricDimensionDefinition,
    "ObjectStorageJobExecutionResultDetails": ObjectStorageJobExecutionResultDetails,
    "ObjectStorageJobExecutionResultLocation": ObjectStorageJobExecutionResultLocation,
    "ParentGroup": ParentGroup,
    "PdbStatusDetails": PdbStatusDetails,
    "RemoveManagedDatabaseFromManagedDatabaseGroupDetails": RemoveManagedDatabaseFromManagedDatabaseGroupDetails,
    "ResetDatabaseParametersDetails": ResetDatabaseParametersDetails,
    "SqlJob": SqlJob,
    "Tablespace": Tablespace,
    "TablespaceCollection": TablespaceCollection,
    "TablespaceSummary": TablespaceSummary,
    "TimeSeriesMetricDataPoint": TimeSeriesMetricDataPoint,
    "TimeSeriesMetricDefinition": TimeSeriesMetricDefinition,
    "UpdateDatabaseParametersResult": UpdateDatabaseParametersResult,
    "UpdateManagedDatabaseGroupDetails": UpdateManagedDatabaseGroupDetails
}
