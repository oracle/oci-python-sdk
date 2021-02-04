# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activity_time_series_metrics import ActivityTimeSeriesMetrics
from .add_managed_database_to_managed_database_group_details import AddManagedDatabaseToManagedDatabaseGroupDetails
from .change_job_compartment_details import ChangeJobCompartmentDetails
from .change_managed_database_group_compartment_details import ChangeManagedDatabaseGroupCompartmentDetails
from .child_database import ChildDatabase
from .create_job_details import CreateJobDetails
from .create_managed_database_group_details import CreateManagedDatabaseGroupDetails
from .create_sql_job_details import CreateSqlJobDetails
from .database_fleet_health_metrics import DatabaseFleetHealthMetrics
from .database_home_metric_definition import DatabaseHomeMetricDefinition
from .database_home_metrics import DatabaseHomeMetrics
from .database_io_aggregate_metrics import DatabaseIOAggregateMetrics
from .database_storage_aggregate_metrics import DatabaseStorageAggregateMetrics
from .database_time_aggregate_metrics import DatabaseTimeAggregateMetrics
from .database_usage_metrics import DatabaseUsageMetrics
from .fleet_metric_definition import FleetMetricDefinition
from .fleet_metric_summary_definition import FleetMetricSummaryDefinition
from .fleet_status_by_category import FleetStatusByCategory
from .fleet_summary import FleetSummary
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
from .remove_managed_database_from_managed_database_group_details import RemoveManagedDatabaseFromManagedDatabaseGroupDetails
from .sql_job import SqlJob
from .update_managed_database_group_details import UpdateManagedDatabaseGroupDetails

# Maps type names to classes for database_management services.
database_management_type_mapping = {
    "ActivityTimeSeriesMetrics": ActivityTimeSeriesMetrics,
    "AddManagedDatabaseToManagedDatabaseGroupDetails": AddManagedDatabaseToManagedDatabaseGroupDetails,
    "ChangeJobCompartmentDetails": ChangeJobCompartmentDetails,
    "ChangeManagedDatabaseGroupCompartmentDetails": ChangeManagedDatabaseGroupCompartmentDetails,
    "ChildDatabase": ChildDatabase,
    "CreateJobDetails": CreateJobDetails,
    "CreateManagedDatabaseGroupDetails": CreateManagedDatabaseGroupDetails,
    "CreateSqlJobDetails": CreateSqlJobDetails,
    "DatabaseFleetHealthMetrics": DatabaseFleetHealthMetrics,
    "DatabaseHomeMetricDefinition": DatabaseHomeMetricDefinition,
    "DatabaseHomeMetrics": DatabaseHomeMetrics,
    "DatabaseIOAggregateMetrics": DatabaseIOAggregateMetrics,
    "DatabaseStorageAggregateMetrics": DatabaseStorageAggregateMetrics,
    "DatabaseTimeAggregateMetrics": DatabaseTimeAggregateMetrics,
    "DatabaseUsageMetrics": DatabaseUsageMetrics,
    "FleetMetricDefinition": FleetMetricDefinition,
    "FleetMetricSummaryDefinition": FleetMetricSummaryDefinition,
    "FleetStatusByCategory": FleetStatusByCategory,
    "FleetSummary": FleetSummary,
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
    "RemoveManagedDatabaseFromManagedDatabaseGroupDetails": RemoveManagedDatabaseFromManagedDatabaseGroupDetails,
    "SqlJob": SqlJob,
    "UpdateManagedDatabaseGroupDetails": UpdateManagedDatabaseGroupDetails
}
