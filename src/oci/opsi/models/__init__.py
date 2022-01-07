# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_em_managed_external_exadata_insight_members_details import AddEmManagedExternalExadataInsightMembersDetails
from .add_exadata_insight_members_details import AddExadataInsightMembersDetails
from .autonomous_database_configuration_summary import AutonomousDatabaseConfigurationSummary
from .autonomous_database_insight import AutonomousDatabaseInsight
from .autonomous_database_insight_summary import AutonomousDatabaseInsightSummary
from .awr_hub import AwrHub
from .awr_hub_summary import AwrHubSummary
from .awr_hub_summary_collection import AwrHubSummaryCollection
from .awr_hubs import AwrHubs
from .awr_report import AwrReport
from .awr_snapshot_collection import AwrSnapshotCollection
from .awr_snapshot_summary import AwrSnapshotSummary
from .awr_source_summary import AwrSourceSummary
from .change_database_insight_compartment_details import ChangeDatabaseInsightCompartmentDetails
from .change_enterprise_manager_bridge_compartment_details import ChangeEnterpriseManagerBridgeCompartmentDetails
from .change_exadata_insight_compartment_details import ChangeExadataInsightCompartmentDetails
from .change_host_insight_compartment_details import ChangeHostInsightCompartmentDetails
from .connection_details import ConnectionDetails
from .create_awr_hub_details import CreateAwrHubDetails
from .create_database_insight_details import CreateDatabaseInsightDetails
from .create_em_managed_external_database_insight_details import CreateEmManagedExternalDatabaseInsightDetails
from .create_em_managed_external_exadata_insight_details import CreateEmManagedExternalExadataInsightDetails
from .create_em_managed_external_exadata_member_entity_details import CreateEmManagedExternalExadataMemberEntityDetails
from .create_em_managed_external_host_insight_details import CreateEmManagedExternalHostInsightDetails
from .create_enterprise_manager_bridge_details import CreateEnterpriseManagerBridgeDetails
from .create_exadata_insight_details import CreateExadataInsightDetails
from .create_host_insight_details import CreateHostInsightDetails
from .create_macs_managed_external_host_insight_details import CreateMacsManagedExternalHostInsightDetails
from .create_operations_insights_warehouse_details import CreateOperationsInsightsWarehouseDetails
from .create_operations_insights_warehouse_user_details import CreateOperationsInsightsWarehouseUserDetails
from .credential_details import CredentialDetails
from .credentials_by_source import CredentialsBySource
from .db_external_instance import DBExternalInstance
from .db_external_properties import DBExternalProperties
from .dbos_config_instance import DBOSConfigInstance
from .database_configuration_collection import DatabaseConfigurationCollection
from .database_configuration_metric_group import DatabaseConfigurationMetricGroup
from .database_configuration_summary import DatabaseConfigurationSummary
from .database_details import DatabaseDetails
from .database_insight import DatabaseInsight
from .database_insight_summary import DatabaseInsightSummary
from .database_insights import DatabaseInsights
from .database_insights_collection import DatabaseInsightsCollection
from .disk_group_details import DiskGroupDetails
from .download_operations_insights_warehouse_wallet_details import DownloadOperationsInsightsWarehouseWalletDetails
from .em_managed_external_database_configuration_summary import EmManagedExternalDatabaseConfigurationSummary
from .em_managed_external_database_insight import EmManagedExternalDatabaseInsight
from .em_managed_external_database_insight_summary import EmManagedExternalDatabaseInsightSummary
from .em_managed_external_exadata_insight import EmManagedExternalExadataInsight
from .em_managed_external_exadata_insight_summary import EmManagedExternalExadataInsightSummary
from .em_managed_external_host_configuration_summary import EmManagedExternalHostConfigurationSummary
from .em_managed_external_host_insight import EmManagedExternalHostInsight
from .em_managed_external_host_insight_summary import EmManagedExternalHostInsightSummary
from .enable_database_insight_details import EnableDatabaseInsightDetails
from .enable_em_managed_external_database_insight_details import EnableEmManagedExternalDatabaseInsightDetails
from .enable_em_managed_external_exadata_insight_details import EnableEmManagedExternalExadataInsightDetails
from .enable_em_managed_external_host_insight_details import EnableEmManagedExternalHostInsightDetails
from .enable_exadata_insight_details import EnableExadataInsightDetails
from .enable_host_insight_details import EnableHostInsightDetails
from .enable_macs_managed_external_host_insight_details import EnableMacsManagedExternalHostInsightDetails
from .enterprise_manager_bridge import EnterpriseManagerBridge
from .enterprise_manager_bridge_collection import EnterpriseManagerBridgeCollection
from .enterprise_manager_bridge_summary import EnterpriseManagerBridgeSummary
from .enterprise_manager_bridges import EnterpriseManagerBridges
from .exadata_configuration_collection import ExadataConfigurationCollection
from .exadata_configuration_summary import ExadataConfigurationSummary
from .exadata_database_machine_configuration_summary import ExadataDatabaseMachineConfigurationSummary
from .exadata_database_statistics_summary import ExadataDatabaseStatisticsSummary
from .exadata_details import ExadataDetails
from .exadata_diskgroup_statistics_summary import ExadataDiskgroupStatisticsSummary
from .exadata_host_statistics_summary import ExadataHostStatisticsSummary
from .exadata_insight import ExadataInsight
from .exadata_insight_resource_capacity_trend_aggregation import ExadataInsightResourceCapacityTrendAggregation
from .exadata_insight_resource_capacity_trend_summary import ExadataInsightResourceCapacityTrendSummary
from .exadata_insight_resource_forecast_trend_summary import ExadataInsightResourceForecastTrendSummary
from .exadata_insight_resource_insight_utilization_item import ExadataInsightResourceInsightUtilizationItem
from .exadata_insight_resource_statistics import ExadataInsightResourceStatistics
from .exadata_insight_resource_statistics_aggregation import ExadataInsightResourceStatisticsAggregation
from .exadata_insight_summary import ExadataInsightSummary
from .exadata_insight_summary_collection import ExadataInsightSummaryCollection
from .exadata_insights import ExadataInsights
from .exadata_member_collection import ExadataMemberCollection
from .exadata_member_summary import ExadataMemberSummary
from .exadata_storage_server_statistics_summary import ExadataStorageServerStatisticsSummary
from .historical_data_item import HistoricalDataItem
from .host_configuration_collection import HostConfigurationCollection
from .host_configuration_metric_group import HostConfigurationMetricGroup
from .host_configuration_summary import HostConfigurationSummary
from .host_cpu_hardware_configuration import HostCpuHardwareConfiguration
from .host_cpu_statistics import HostCpuStatistics
from .host_cpu_usage import HostCpuUsage
from .host_details import HostDetails
from .host_entities import HostEntities
from .host_hardware_configuration import HostHardwareConfiguration
from .host_importable_agent_entity_summary import HostImportableAgentEntitySummary
from .host_insight import HostInsight
from .host_insight_resource_statistics_aggregation import HostInsightResourceStatisticsAggregation
from .host_insight_summary import HostInsightSummary
from .host_insight_summary_collection import HostInsightSummaryCollection
from .host_insights import HostInsights
from .host_instance_map import HostInstanceMap
from .host_memory_configuration import HostMemoryConfiguration
from .host_memory_statistics import HostMemoryStatistics
from .host_memory_usage import HostMemoryUsage
from .host_network_activity_summary import HostNetworkActivitySummary
from .host_network_configuration import HostNetworkConfiguration
from .host_performance_metric_group import HostPerformanceMetricGroup
from .host_product import HostProduct
from .host_resource_allocation import HostResourceAllocation
from .host_resource_capacity_trend_aggregation import HostResourceCapacityTrendAggregation
from .host_resource_statistics import HostResourceStatistics
from .hosted_entity_collection import HostedEntityCollection
from .hosted_entity_summary import HostedEntitySummary
from .importable_agent_entity_summary import ImportableAgentEntitySummary
from .importable_agent_entity_summary_collection import ImportableAgentEntitySummaryCollection
from .importable_enterprise_manager_entity import ImportableEnterpriseManagerEntity
from .importable_enterprise_manager_entity_collection import ImportableEnterpriseManagerEntityCollection
from .ingest_database_configuration_details import IngestDatabaseConfigurationDetails
from .ingest_database_configuration_response_details import IngestDatabaseConfigurationResponseDetails
from .ingest_host_configuration_details import IngestHostConfigurationDetails
from .ingest_host_configuration_response_details import IngestHostConfigurationResponseDetails
from .ingest_host_metrics_details import IngestHostMetricsDetails
from .ingest_host_metrics_response_details import IngestHostMetricsResponseDetails
from .ingest_sql_bucket_details import IngestSqlBucketDetails
from .ingest_sql_bucket_response_details import IngestSqlBucketResponseDetails
from .ingest_sql_plan_lines_details import IngestSqlPlanLinesDetails
from .ingest_sql_plan_lines_response_details import IngestSqlPlanLinesResponseDetails
from .ingest_sql_stats_details import IngestSqlStatsDetails
from .ingest_sql_stats_response_details import IngestSqlStatsResponseDetails
from .ingest_sql_text_details import IngestSqlTextDetails
from .ingest_sql_text_response_details import IngestSqlTextResponseDetails
from .instance_metrics import InstanceMetrics
from .macs_managed_external_database_configuration_summary import MacsManagedExternalDatabaseConfigurationSummary
from .macs_managed_external_database_insight import MacsManagedExternalDatabaseInsight
from .macs_managed_external_database_insight_summary import MacsManagedExternalDatabaseInsightSummary
from .macs_managed_external_host_configuration_summary import MacsManagedExternalHostConfigurationSummary
from .macs_managed_external_host_insight import MacsManagedExternalHostInsight
from .macs_managed_external_host_insight_summary import MacsManagedExternalHostInsightSummary
from .operations_insights_warehouse import OperationsInsightsWarehouse
from .operations_insights_warehouse_summary import OperationsInsightsWarehouseSummary
from .operations_insights_warehouse_summary_collection import OperationsInsightsWarehouseSummaryCollection
from .operations_insights_warehouse_user import OperationsInsightsWarehouseUser
from .operations_insights_warehouse_user_summary import OperationsInsightsWarehouseUserSummary
from .operations_insights_warehouse_user_summary_collection import OperationsInsightsWarehouseUserSummaryCollection
from .operations_insights_warehouse_users import OperationsInsightsWarehouseUsers
from .operations_insights_warehouses import OperationsInsightsWarehouses
from .projected_data_item import ProjectedDataItem
from .resource_capacity_trend_aggregation import ResourceCapacityTrendAggregation
from .resource_insight_current_utilization import ResourceInsightCurrentUtilization
from .resource_insight_projected_utilization import ResourceInsightProjectedUtilization
from .resource_insight_projected_utilization_item import ResourceInsightProjectedUtilizationItem
from .resource_statistics import ResourceStatistics
from .resource_statistics_aggregation import ResourceStatisticsAggregation
from .resource_usage_summary import ResourceUsageSummary
from .resource_usage_trend_aggregation import ResourceUsageTrendAggregation
from .sql_bucket import SqlBucket
from .sql_insight_aggregation import SqlInsightAggregation
from .sql_insight_aggregation_collection import SqlInsightAggregationCollection
from .sql_insight_thresholds import SqlInsightThresholds
from .sql_inventory import SqlInventory
from .sql_plan_collection import SqlPlanCollection
from .sql_plan_insight_aggregation import SqlPlanInsightAggregation
from .sql_plan_insight_aggregation_collection import SqlPlanInsightAggregationCollection
from .sql_plan_insights import SqlPlanInsights
from .sql_plan_line import SqlPlanLine
from .sql_plan_summary import SqlPlanSummary
from .sql_response_time_distribution_aggregation import SqlResponseTimeDistributionAggregation
from .sql_response_time_distribution_aggregation_collection import SqlResponseTimeDistributionAggregationCollection
from .sql_search_collection import SqlSearchCollection
from .sql_search_summary import SqlSearchSummary
from .sql_statistic_aggregation import SqlStatisticAggregation
from .sql_statistic_aggregation_collection import SqlStatisticAggregationCollection
from .sql_statistics import SqlStatistics
from .sql_statistics_time_series import SqlStatisticsTimeSeries
from .sql_statistics_time_series_aggregation import SqlStatisticsTimeSeriesAggregation
from .sql_statistics_time_series_aggregation_collection import SqlStatisticsTimeSeriesAggregationCollection
from .sql_statistics_time_series_by_plan_aggregation import SqlStatisticsTimeSeriesByPlanAggregation
from .sql_statistics_time_series_by_plan_aggregation_collection import SqlStatisticsTimeSeriesByPlanAggregationCollection
from .sql_stats import SqlStats
from .sql_text import SqlText
from .sql_text_collection import SqlTextCollection
from .sql_text_summary import SqlTextSummary
from .storage_server_details import StorageServerDetails
from .summarize_awr_sources_summaries_collection import SummarizeAwrSourcesSummariesCollection
from .summarize_database_insight_resource_capacity_trend_aggregation_collection import SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection
from .summarize_database_insight_resource_forecast_trend_aggregation import SummarizeDatabaseInsightResourceForecastTrendAggregation
from .summarize_database_insight_resource_statistics_aggregation_collection import SummarizeDatabaseInsightResourceStatisticsAggregationCollection
from .summarize_database_insight_resource_usage_aggregation import SummarizeDatabaseInsightResourceUsageAggregation
from .summarize_database_insight_resource_usage_trend_aggregation_collection import SummarizeDatabaseInsightResourceUsageTrendAggregationCollection
from .summarize_database_insight_resource_utilization_insight_aggregation import SummarizeDatabaseInsightResourceUtilizationInsightAggregation
from .summarize_database_insight_tablespace_usage_trend_aggregation_collection import SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection
from .summarize_exadata_insight_resource_capacity_trend_aggregation import SummarizeExadataInsightResourceCapacityTrendAggregation
from .summarize_exadata_insight_resource_capacity_trend_collection import SummarizeExadataInsightResourceCapacityTrendCollection
from .summarize_exadata_insight_resource_forecast_trend_aggregation import SummarizeExadataInsightResourceForecastTrendAggregation
from .summarize_exadata_insight_resource_forecast_trend_collection import SummarizeExadataInsightResourceForecastTrendCollection
from .summarize_exadata_insight_resource_statistics_aggregation_collection import SummarizeExadataInsightResourceStatisticsAggregationCollection
from .summarize_exadata_insight_resource_usage_aggregation import SummarizeExadataInsightResourceUsageAggregation
from .summarize_exadata_insight_resource_usage_collection import SummarizeExadataInsightResourceUsageCollection
from .summarize_exadata_insight_resource_utilization_insight_aggregation import SummarizeExadataInsightResourceUtilizationInsightAggregation
from .summarize_host_insight_resource_capacity_trend_aggregation_collection import SummarizeHostInsightResourceCapacityTrendAggregationCollection
from .summarize_host_insight_resource_forecast_trend_aggregation import SummarizeHostInsightResourceForecastTrendAggregation
from .summarize_host_insight_resource_statistics_aggregation_collection import SummarizeHostInsightResourceStatisticsAggregationCollection
from .summarize_host_insight_resource_usage_aggregation import SummarizeHostInsightResourceUsageAggregation
from .summarize_host_insight_resource_usage_trend_aggregation_collection import SummarizeHostInsightResourceUsageTrendAggregationCollection
from .summarize_host_insight_resource_utilization_insight_aggregation import SummarizeHostInsightResourceUtilizationInsightAggregation
from .summarize_operations_insights_warehouse_resource_usage_aggregation import SummarizeOperationsInsightsWarehouseResourceUsageAggregation
from .summary_statistics import SummaryStatistics
from .tablespace_usage_trend import TablespaceUsageTrend
from .tablespace_usage_trend_aggregation import TablespaceUsageTrendAggregation
from .update_autonomous_database_insight_details import UpdateAutonomousDatabaseInsightDetails
from .update_awr_hub_details import UpdateAwrHubDetails
from .update_database_insight_details import UpdateDatabaseInsightDetails
from .update_em_managed_external_database_insight_details import UpdateEmManagedExternalDatabaseInsightDetails
from .update_em_managed_external_exadata_insight_details import UpdateEmManagedExternalExadataInsightDetails
from .update_em_managed_external_host_insight_details import UpdateEmManagedExternalHostInsightDetails
from .update_enterprise_manager_bridge_details import UpdateEnterpriseManagerBridgeDetails
from .update_exadata_insight_details import UpdateExadataInsightDetails
from .update_host_insight_details import UpdateHostInsightDetails
from .update_macs_managed_external_database_insight_details import UpdateMacsManagedExternalDatabaseInsightDetails
from .update_macs_managed_external_host_insight_details import UpdateMacsManagedExternalHostInsightDetails
from .update_operations_insights_warehouse_details import UpdateOperationsInsightsWarehouseDetails
from .update_operations_insights_warehouse_user_details import UpdateOperationsInsightsWarehouseUserDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_requests import WorkRequests

# Maps type names to classes for opsi services.
opsi_type_mapping = {
    "AddEmManagedExternalExadataInsightMembersDetails": AddEmManagedExternalExadataInsightMembersDetails,
    "AddExadataInsightMembersDetails": AddExadataInsightMembersDetails,
    "AutonomousDatabaseConfigurationSummary": AutonomousDatabaseConfigurationSummary,
    "AutonomousDatabaseInsight": AutonomousDatabaseInsight,
    "AutonomousDatabaseInsightSummary": AutonomousDatabaseInsightSummary,
    "AwrHub": AwrHub,
    "AwrHubSummary": AwrHubSummary,
    "AwrHubSummaryCollection": AwrHubSummaryCollection,
    "AwrHubs": AwrHubs,
    "AwrReport": AwrReport,
    "AwrSnapshotCollection": AwrSnapshotCollection,
    "AwrSnapshotSummary": AwrSnapshotSummary,
    "AwrSourceSummary": AwrSourceSummary,
    "ChangeDatabaseInsightCompartmentDetails": ChangeDatabaseInsightCompartmentDetails,
    "ChangeEnterpriseManagerBridgeCompartmentDetails": ChangeEnterpriseManagerBridgeCompartmentDetails,
    "ChangeExadataInsightCompartmentDetails": ChangeExadataInsightCompartmentDetails,
    "ChangeHostInsightCompartmentDetails": ChangeHostInsightCompartmentDetails,
    "ConnectionDetails": ConnectionDetails,
    "CreateAwrHubDetails": CreateAwrHubDetails,
    "CreateDatabaseInsightDetails": CreateDatabaseInsightDetails,
    "CreateEmManagedExternalDatabaseInsightDetails": CreateEmManagedExternalDatabaseInsightDetails,
    "CreateEmManagedExternalExadataInsightDetails": CreateEmManagedExternalExadataInsightDetails,
    "CreateEmManagedExternalExadataMemberEntityDetails": CreateEmManagedExternalExadataMemberEntityDetails,
    "CreateEmManagedExternalHostInsightDetails": CreateEmManagedExternalHostInsightDetails,
    "CreateEnterpriseManagerBridgeDetails": CreateEnterpriseManagerBridgeDetails,
    "CreateExadataInsightDetails": CreateExadataInsightDetails,
    "CreateHostInsightDetails": CreateHostInsightDetails,
    "CreateMacsManagedExternalHostInsightDetails": CreateMacsManagedExternalHostInsightDetails,
    "CreateOperationsInsightsWarehouseDetails": CreateOperationsInsightsWarehouseDetails,
    "CreateOperationsInsightsWarehouseUserDetails": CreateOperationsInsightsWarehouseUserDetails,
    "CredentialDetails": CredentialDetails,
    "CredentialsBySource": CredentialsBySource,
    "DBExternalInstance": DBExternalInstance,
    "DBExternalProperties": DBExternalProperties,
    "DBOSConfigInstance": DBOSConfigInstance,
    "DatabaseConfigurationCollection": DatabaseConfigurationCollection,
    "DatabaseConfigurationMetricGroup": DatabaseConfigurationMetricGroup,
    "DatabaseConfigurationSummary": DatabaseConfigurationSummary,
    "DatabaseDetails": DatabaseDetails,
    "DatabaseInsight": DatabaseInsight,
    "DatabaseInsightSummary": DatabaseInsightSummary,
    "DatabaseInsights": DatabaseInsights,
    "DatabaseInsightsCollection": DatabaseInsightsCollection,
    "DiskGroupDetails": DiskGroupDetails,
    "DownloadOperationsInsightsWarehouseWalletDetails": DownloadOperationsInsightsWarehouseWalletDetails,
    "EmManagedExternalDatabaseConfigurationSummary": EmManagedExternalDatabaseConfigurationSummary,
    "EmManagedExternalDatabaseInsight": EmManagedExternalDatabaseInsight,
    "EmManagedExternalDatabaseInsightSummary": EmManagedExternalDatabaseInsightSummary,
    "EmManagedExternalExadataInsight": EmManagedExternalExadataInsight,
    "EmManagedExternalExadataInsightSummary": EmManagedExternalExadataInsightSummary,
    "EmManagedExternalHostConfigurationSummary": EmManagedExternalHostConfigurationSummary,
    "EmManagedExternalHostInsight": EmManagedExternalHostInsight,
    "EmManagedExternalHostInsightSummary": EmManagedExternalHostInsightSummary,
    "EnableDatabaseInsightDetails": EnableDatabaseInsightDetails,
    "EnableEmManagedExternalDatabaseInsightDetails": EnableEmManagedExternalDatabaseInsightDetails,
    "EnableEmManagedExternalExadataInsightDetails": EnableEmManagedExternalExadataInsightDetails,
    "EnableEmManagedExternalHostInsightDetails": EnableEmManagedExternalHostInsightDetails,
    "EnableExadataInsightDetails": EnableExadataInsightDetails,
    "EnableHostInsightDetails": EnableHostInsightDetails,
    "EnableMacsManagedExternalHostInsightDetails": EnableMacsManagedExternalHostInsightDetails,
    "EnterpriseManagerBridge": EnterpriseManagerBridge,
    "EnterpriseManagerBridgeCollection": EnterpriseManagerBridgeCollection,
    "EnterpriseManagerBridgeSummary": EnterpriseManagerBridgeSummary,
    "EnterpriseManagerBridges": EnterpriseManagerBridges,
    "ExadataConfigurationCollection": ExadataConfigurationCollection,
    "ExadataConfigurationSummary": ExadataConfigurationSummary,
    "ExadataDatabaseMachineConfigurationSummary": ExadataDatabaseMachineConfigurationSummary,
    "ExadataDatabaseStatisticsSummary": ExadataDatabaseStatisticsSummary,
    "ExadataDetails": ExadataDetails,
    "ExadataDiskgroupStatisticsSummary": ExadataDiskgroupStatisticsSummary,
    "ExadataHostStatisticsSummary": ExadataHostStatisticsSummary,
    "ExadataInsight": ExadataInsight,
    "ExadataInsightResourceCapacityTrendAggregation": ExadataInsightResourceCapacityTrendAggregation,
    "ExadataInsightResourceCapacityTrendSummary": ExadataInsightResourceCapacityTrendSummary,
    "ExadataInsightResourceForecastTrendSummary": ExadataInsightResourceForecastTrendSummary,
    "ExadataInsightResourceInsightUtilizationItem": ExadataInsightResourceInsightUtilizationItem,
    "ExadataInsightResourceStatistics": ExadataInsightResourceStatistics,
    "ExadataInsightResourceStatisticsAggregation": ExadataInsightResourceStatisticsAggregation,
    "ExadataInsightSummary": ExadataInsightSummary,
    "ExadataInsightSummaryCollection": ExadataInsightSummaryCollection,
    "ExadataInsights": ExadataInsights,
    "ExadataMemberCollection": ExadataMemberCollection,
    "ExadataMemberSummary": ExadataMemberSummary,
    "ExadataStorageServerStatisticsSummary": ExadataStorageServerStatisticsSummary,
    "HistoricalDataItem": HistoricalDataItem,
    "HostConfigurationCollection": HostConfigurationCollection,
    "HostConfigurationMetricGroup": HostConfigurationMetricGroup,
    "HostConfigurationSummary": HostConfigurationSummary,
    "HostCpuHardwareConfiguration": HostCpuHardwareConfiguration,
    "HostCpuStatistics": HostCpuStatistics,
    "HostCpuUsage": HostCpuUsage,
    "HostDetails": HostDetails,
    "HostEntities": HostEntities,
    "HostHardwareConfiguration": HostHardwareConfiguration,
    "HostImportableAgentEntitySummary": HostImportableAgentEntitySummary,
    "HostInsight": HostInsight,
    "HostInsightResourceStatisticsAggregation": HostInsightResourceStatisticsAggregation,
    "HostInsightSummary": HostInsightSummary,
    "HostInsightSummaryCollection": HostInsightSummaryCollection,
    "HostInsights": HostInsights,
    "HostInstanceMap": HostInstanceMap,
    "HostMemoryConfiguration": HostMemoryConfiguration,
    "HostMemoryStatistics": HostMemoryStatistics,
    "HostMemoryUsage": HostMemoryUsage,
    "HostNetworkActivitySummary": HostNetworkActivitySummary,
    "HostNetworkConfiguration": HostNetworkConfiguration,
    "HostPerformanceMetricGroup": HostPerformanceMetricGroup,
    "HostProduct": HostProduct,
    "HostResourceAllocation": HostResourceAllocation,
    "HostResourceCapacityTrendAggregation": HostResourceCapacityTrendAggregation,
    "HostResourceStatistics": HostResourceStatistics,
    "HostedEntityCollection": HostedEntityCollection,
    "HostedEntitySummary": HostedEntitySummary,
    "ImportableAgentEntitySummary": ImportableAgentEntitySummary,
    "ImportableAgentEntitySummaryCollection": ImportableAgentEntitySummaryCollection,
    "ImportableEnterpriseManagerEntity": ImportableEnterpriseManagerEntity,
    "ImportableEnterpriseManagerEntityCollection": ImportableEnterpriseManagerEntityCollection,
    "IngestDatabaseConfigurationDetails": IngestDatabaseConfigurationDetails,
    "IngestDatabaseConfigurationResponseDetails": IngestDatabaseConfigurationResponseDetails,
    "IngestHostConfigurationDetails": IngestHostConfigurationDetails,
    "IngestHostConfigurationResponseDetails": IngestHostConfigurationResponseDetails,
    "IngestHostMetricsDetails": IngestHostMetricsDetails,
    "IngestHostMetricsResponseDetails": IngestHostMetricsResponseDetails,
    "IngestSqlBucketDetails": IngestSqlBucketDetails,
    "IngestSqlBucketResponseDetails": IngestSqlBucketResponseDetails,
    "IngestSqlPlanLinesDetails": IngestSqlPlanLinesDetails,
    "IngestSqlPlanLinesResponseDetails": IngestSqlPlanLinesResponseDetails,
    "IngestSqlStatsDetails": IngestSqlStatsDetails,
    "IngestSqlStatsResponseDetails": IngestSqlStatsResponseDetails,
    "IngestSqlTextDetails": IngestSqlTextDetails,
    "IngestSqlTextResponseDetails": IngestSqlTextResponseDetails,
    "InstanceMetrics": InstanceMetrics,
    "MacsManagedExternalDatabaseConfigurationSummary": MacsManagedExternalDatabaseConfigurationSummary,
    "MacsManagedExternalDatabaseInsight": MacsManagedExternalDatabaseInsight,
    "MacsManagedExternalDatabaseInsightSummary": MacsManagedExternalDatabaseInsightSummary,
    "MacsManagedExternalHostConfigurationSummary": MacsManagedExternalHostConfigurationSummary,
    "MacsManagedExternalHostInsight": MacsManagedExternalHostInsight,
    "MacsManagedExternalHostInsightSummary": MacsManagedExternalHostInsightSummary,
    "OperationsInsightsWarehouse": OperationsInsightsWarehouse,
    "OperationsInsightsWarehouseSummary": OperationsInsightsWarehouseSummary,
    "OperationsInsightsWarehouseSummaryCollection": OperationsInsightsWarehouseSummaryCollection,
    "OperationsInsightsWarehouseUser": OperationsInsightsWarehouseUser,
    "OperationsInsightsWarehouseUserSummary": OperationsInsightsWarehouseUserSummary,
    "OperationsInsightsWarehouseUserSummaryCollection": OperationsInsightsWarehouseUserSummaryCollection,
    "OperationsInsightsWarehouseUsers": OperationsInsightsWarehouseUsers,
    "OperationsInsightsWarehouses": OperationsInsightsWarehouses,
    "ProjectedDataItem": ProjectedDataItem,
    "ResourceCapacityTrendAggregation": ResourceCapacityTrendAggregation,
    "ResourceInsightCurrentUtilization": ResourceInsightCurrentUtilization,
    "ResourceInsightProjectedUtilization": ResourceInsightProjectedUtilization,
    "ResourceInsightProjectedUtilizationItem": ResourceInsightProjectedUtilizationItem,
    "ResourceStatistics": ResourceStatistics,
    "ResourceStatisticsAggregation": ResourceStatisticsAggregation,
    "ResourceUsageSummary": ResourceUsageSummary,
    "ResourceUsageTrendAggregation": ResourceUsageTrendAggregation,
    "SqlBucket": SqlBucket,
    "SqlInsightAggregation": SqlInsightAggregation,
    "SqlInsightAggregationCollection": SqlInsightAggregationCollection,
    "SqlInsightThresholds": SqlInsightThresholds,
    "SqlInventory": SqlInventory,
    "SqlPlanCollection": SqlPlanCollection,
    "SqlPlanInsightAggregation": SqlPlanInsightAggregation,
    "SqlPlanInsightAggregationCollection": SqlPlanInsightAggregationCollection,
    "SqlPlanInsights": SqlPlanInsights,
    "SqlPlanLine": SqlPlanLine,
    "SqlPlanSummary": SqlPlanSummary,
    "SqlResponseTimeDistributionAggregation": SqlResponseTimeDistributionAggregation,
    "SqlResponseTimeDistributionAggregationCollection": SqlResponseTimeDistributionAggregationCollection,
    "SqlSearchCollection": SqlSearchCollection,
    "SqlSearchSummary": SqlSearchSummary,
    "SqlStatisticAggregation": SqlStatisticAggregation,
    "SqlStatisticAggregationCollection": SqlStatisticAggregationCollection,
    "SqlStatistics": SqlStatistics,
    "SqlStatisticsTimeSeries": SqlStatisticsTimeSeries,
    "SqlStatisticsTimeSeriesAggregation": SqlStatisticsTimeSeriesAggregation,
    "SqlStatisticsTimeSeriesAggregationCollection": SqlStatisticsTimeSeriesAggregationCollection,
    "SqlStatisticsTimeSeriesByPlanAggregation": SqlStatisticsTimeSeriesByPlanAggregation,
    "SqlStatisticsTimeSeriesByPlanAggregationCollection": SqlStatisticsTimeSeriesByPlanAggregationCollection,
    "SqlStats": SqlStats,
    "SqlText": SqlText,
    "SqlTextCollection": SqlTextCollection,
    "SqlTextSummary": SqlTextSummary,
    "StorageServerDetails": StorageServerDetails,
    "SummarizeAwrSourcesSummariesCollection": SummarizeAwrSourcesSummariesCollection,
    "SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection": SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection,
    "SummarizeDatabaseInsightResourceForecastTrendAggregation": SummarizeDatabaseInsightResourceForecastTrendAggregation,
    "SummarizeDatabaseInsightResourceStatisticsAggregationCollection": SummarizeDatabaseInsightResourceStatisticsAggregationCollection,
    "SummarizeDatabaseInsightResourceUsageAggregation": SummarizeDatabaseInsightResourceUsageAggregation,
    "SummarizeDatabaseInsightResourceUsageTrendAggregationCollection": SummarizeDatabaseInsightResourceUsageTrendAggregationCollection,
    "SummarizeDatabaseInsightResourceUtilizationInsightAggregation": SummarizeDatabaseInsightResourceUtilizationInsightAggregation,
    "SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection": SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection,
    "SummarizeExadataInsightResourceCapacityTrendAggregation": SummarizeExadataInsightResourceCapacityTrendAggregation,
    "SummarizeExadataInsightResourceCapacityTrendCollection": SummarizeExadataInsightResourceCapacityTrendCollection,
    "SummarizeExadataInsightResourceForecastTrendAggregation": SummarizeExadataInsightResourceForecastTrendAggregation,
    "SummarizeExadataInsightResourceForecastTrendCollection": SummarizeExadataInsightResourceForecastTrendCollection,
    "SummarizeExadataInsightResourceStatisticsAggregationCollection": SummarizeExadataInsightResourceStatisticsAggregationCollection,
    "SummarizeExadataInsightResourceUsageAggregation": SummarizeExadataInsightResourceUsageAggregation,
    "SummarizeExadataInsightResourceUsageCollection": SummarizeExadataInsightResourceUsageCollection,
    "SummarizeExadataInsightResourceUtilizationInsightAggregation": SummarizeExadataInsightResourceUtilizationInsightAggregation,
    "SummarizeHostInsightResourceCapacityTrendAggregationCollection": SummarizeHostInsightResourceCapacityTrendAggregationCollection,
    "SummarizeHostInsightResourceForecastTrendAggregation": SummarizeHostInsightResourceForecastTrendAggregation,
    "SummarizeHostInsightResourceStatisticsAggregationCollection": SummarizeHostInsightResourceStatisticsAggregationCollection,
    "SummarizeHostInsightResourceUsageAggregation": SummarizeHostInsightResourceUsageAggregation,
    "SummarizeHostInsightResourceUsageTrendAggregationCollection": SummarizeHostInsightResourceUsageTrendAggregationCollection,
    "SummarizeHostInsightResourceUtilizationInsightAggregation": SummarizeHostInsightResourceUtilizationInsightAggregation,
    "SummarizeOperationsInsightsWarehouseResourceUsageAggregation": SummarizeOperationsInsightsWarehouseResourceUsageAggregation,
    "SummaryStatistics": SummaryStatistics,
    "TablespaceUsageTrend": TablespaceUsageTrend,
    "TablespaceUsageTrendAggregation": TablespaceUsageTrendAggregation,
    "UpdateAutonomousDatabaseInsightDetails": UpdateAutonomousDatabaseInsightDetails,
    "UpdateAwrHubDetails": UpdateAwrHubDetails,
    "UpdateDatabaseInsightDetails": UpdateDatabaseInsightDetails,
    "UpdateEmManagedExternalDatabaseInsightDetails": UpdateEmManagedExternalDatabaseInsightDetails,
    "UpdateEmManagedExternalExadataInsightDetails": UpdateEmManagedExternalExadataInsightDetails,
    "UpdateEmManagedExternalHostInsightDetails": UpdateEmManagedExternalHostInsightDetails,
    "UpdateEnterpriseManagerBridgeDetails": UpdateEnterpriseManagerBridgeDetails,
    "UpdateExadataInsightDetails": UpdateExadataInsightDetails,
    "UpdateHostInsightDetails": UpdateHostInsightDetails,
    "UpdateMacsManagedExternalDatabaseInsightDetails": UpdateMacsManagedExternalDatabaseInsightDetails,
    "UpdateMacsManagedExternalHostInsightDetails": UpdateMacsManagedExternalHostInsightDetails,
    "UpdateOperationsInsightsWarehouseDetails": UpdateOperationsInsightsWarehouseDetails,
    "UpdateOperationsInsightsWarehouseUserDetails": UpdateOperationsInsightsWarehouseUserDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequests": WorkRequests
}
