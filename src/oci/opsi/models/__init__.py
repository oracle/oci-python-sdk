# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .database_details import DatabaseDetails
from .database_insight_summary import DatabaseInsightSummary
from .database_insights import DatabaseInsights
from .database_insights_collection import DatabaseInsightsCollection
from .historical_data_item import HistoricalDataItem
from .ingest_sql_bucket_details import IngestSqlBucketDetails
from .ingest_sql_bucket_response_details import IngestSqlBucketResponseDetails
from .ingest_sql_plan_lines_details import IngestSqlPlanLinesDetails
from .ingest_sql_plan_lines_response_details import IngestSqlPlanLinesResponseDetails
from .ingest_sql_text_details import IngestSqlTextDetails
from .ingest_sql_text_response_details import IngestSqlTextResponseDetails
from .projected_data_item import ProjectedDataItem
from .resource_capacity_trend_aggregation import ResourceCapacityTrendAggregation
from .resource_insight_current_utilization import ResourceInsightCurrentUtilization
from .resource_insight_projected_utilization import ResourceInsightProjectedUtilization
from .resource_insight_projected_utilization_item import ResourceInsightProjectedUtilizationItem
from .resource_statistics import ResourceStatistics
from .resource_statistics_aggregation import ResourceStatisticsAggregation
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
from .sql_text import SqlText
from .sql_text_collection import SqlTextCollection
from .sql_text_summary import SqlTextSummary
from .summarize_database_insight_resource_capacity_trend_aggregation_collection import SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection
from .summarize_database_insight_resource_forecast_trend_aggregation import SummarizeDatabaseInsightResourceForecastTrendAggregation
from .summarize_database_insight_resource_statistics_aggregation_collection import SummarizeDatabaseInsightResourceStatisticsAggregationCollection
from .summarize_database_insight_resource_usage_aggregation import SummarizeDatabaseInsightResourceUsageAggregation
from .summarize_database_insight_resource_usage_trend_aggregation_collection import SummarizeDatabaseInsightResourceUsageTrendAggregationCollection
from .summarize_database_insight_resource_utilization_insight_aggregation import SummarizeDatabaseInsightResourceUtilizationInsightAggregation

# Maps type names to classes for opsi services.
opsi_type_mapping = {
    "DatabaseDetails": DatabaseDetails,
    "DatabaseInsightSummary": DatabaseInsightSummary,
    "DatabaseInsights": DatabaseInsights,
    "DatabaseInsightsCollection": DatabaseInsightsCollection,
    "HistoricalDataItem": HistoricalDataItem,
    "IngestSqlBucketDetails": IngestSqlBucketDetails,
    "IngestSqlBucketResponseDetails": IngestSqlBucketResponseDetails,
    "IngestSqlPlanLinesDetails": IngestSqlPlanLinesDetails,
    "IngestSqlPlanLinesResponseDetails": IngestSqlPlanLinesResponseDetails,
    "IngestSqlTextDetails": IngestSqlTextDetails,
    "IngestSqlTextResponseDetails": IngestSqlTextResponseDetails,
    "ProjectedDataItem": ProjectedDataItem,
    "ResourceCapacityTrendAggregation": ResourceCapacityTrendAggregation,
    "ResourceInsightCurrentUtilization": ResourceInsightCurrentUtilization,
    "ResourceInsightProjectedUtilization": ResourceInsightProjectedUtilization,
    "ResourceInsightProjectedUtilizationItem": ResourceInsightProjectedUtilizationItem,
    "ResourceStatistics": ResourceStatistics,
    "ResourceStatisticsAggregation": ResourceStatisticsAggregation,
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
    "SqlText": SqlText,
    "SqlTextCollection": SqlTextCollection,
    "SqlTextSummary": SqlTextSummary,
    "SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection": SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection,
    "SummarizeDatabaseInsightResourceForecastTrendAggregation": SummarizeDatabaseInsightResourceForecastTrendAggregation,
    "SummarizeDatabaseInsightResourceStatisticsAggregationCollection": SummarizeDatabaseInsightResourceStatisticsAggregationCollection,
    "SummarizeDatabaseInsightResourceUsageAggregation": SummarizeDatabaseInsightResourceUsageAggregation,
    "SummarizeDatabaseInsightResourceUsageTrendAggregationCollection": SummarizeDatabaseInsightResourceUsageTrendAggregationCollection,
    "SummarizeDatabaseInsightResourceUtilizationInsightAggregation": SummarizeDatabaseInsightResourceUtilizationInsightAggregation
}
