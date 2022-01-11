# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_table_compartment_details import ChangeTableCompartmentDetails
from .column import Column
from .create_index_details import CreateIndexDetails
from .create_table_details import CreateTableDetails
from .delete_row_result import DeleteRowResult
from .index import Index
from .index_collection import IndexCollection
from .index_key import IndexKey
from .index_summary import IndexSummary
from .prepared_statement import PreparedStatement
from .query_details import QueryDetails
from .query_result_collection import QueryResultCollection
from .request_usage import RequestUsage
from .row import Row
from .schema import Schema
from .statement_summary import StatementSummary
from .table import Table
from .table_collection import TableCollection
from .table_limits import TableLimits
from .table_summary import TableSummary
from .table_usage_collection import TableUsageCollection
from .table_usage_summary import TableUsageSummary
from .update_row_details import UpdateRowDetails
from .update_row_result import UpdateRowResult
from .update_table_details import UpdateTableDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for nosql services.
nosql_type_mapping = {
    "ChangeTableCompartmentDetails": ChangeTableCompartmentDetails,
    "Column": Column,
    "CreateIndexDetails": CreateIndexDetails,
    "CreateTableDetails": CreateTableDetails,
    "DeleteRowResult": DeleteRowResult,
    "Index": Index,
    "IndexCollection": IndexCollection,
    "IndexKey": IndexKey,
    "IndexSummary": IndexSummary,
    "PreparedStatement": PreparedStatement,
    "QueryDetails": QueryDetails,
    "QueryResultCollection": QueryResultCollection,
    "RequestUsage": RequestUsage,
    "Row": Row,
    "Schema": Schema,
    "StatementSummary": StatementSummary,
    "Table": Table,
    "TableCollection": TableCollection,
    "TableLimits": TableLimits,
    "TableSummary": TableSummary,
    "TableUsageCollection": TableUsageCollection,
    "TableUsageSummary": TableUsageSummary,
    "UpdateRowDetails": UpdateRowDetails,
    "UpdateRowResult": UpdateRowResult,
    "UpdateTableDetails": UpdateTableDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
