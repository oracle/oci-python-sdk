# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .configuration import Configuration
from .configuration_aggregation import ConfigurationAggregation
from .cost_analysis_ui import CostAnalysisUI
from .create_custom_table_details import CreateCustomTableDetails
from .create_query_details import CreateQueryDetails
from .custom_table import CustomTable
from .custom_table_collection import CustomTableCollection
from .custom_table_summary import CustomTableSummary
from .dimension import Dimension
from .filter import Filter
from .forecast import Forecast
from .query import Query
from .query_collection import QueryCollection
from .query_definition import QueryDefinition
from .query_summary import QuerySummary
from .report_query import ReportQuery
from .request_summarized_usages_details import RequestSummarizedUsagesDetails
from .saved_custom_table import SavedCustomTable
from .tag import Tag
from .update_custom_table_details import UpdateCustomTableDetails
from .update_query_details import UpdateQueryDetails
from .usage_aggregation import UsageAggregation
from .usage_summary import UsageSummary

# Maps type names to classes for usage_api services.
usage_api_type_mapping = {
    "Configuration": Configuration,
    "ConfigurationAggregation": ConfigurationAggregation,
    "CostAnalysisUI": CostAnalysisUI,
    "CreateCustomTableDetails": CreateCustomTableDetails,
    "CreateQueryDetails": CreateQueryDetails,
    "CustomTable": CustomTable,
    "CustomTableCollection": CustomTableCollection,
    "CustomTableSummary": CustomTableSummary,
    "Dimension": Dimension,
    "Filter": Filter,
    "Forecast": Forecast,
    "Query": Query,
    "QueryCollection": QueryCollection,
    "QueryDefinition": QueryDefinition,
    "QuerySummary": QuerySummary,
    "ReportQuery": ReportQuery,
    "RequestSummarizedUsagesDetails": RequestSummarizedUsagesDetails,
    "SavedCustomTable": SavedCustomTable,
    "Tag": Tag,
    "UpdateCustomTableDetails": UpdateCustomTableDetails,
    "UpdateQueryDetails": UpdateQueryDetails,
    "UsageAggregation": UsageAggregation,
    "UsageSummary": UsageSummary
}
