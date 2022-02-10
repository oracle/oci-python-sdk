# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .aggregated_snapshot import AggregatedSnapshot
from .aggregated_stack_trace import AggregatedStackTrace
from .query_details import QueryDetails
from .query_result_metadata_summary import QueryResultMetadataSummary
from .query_result_response import QueryResultResponse
from .query_result_row import QueryResultRow
from .query_result_row_type_summary import QueryResultRowTypeSummary
from .query_results_grouped_by_summary import QueryResultsGroupedBySummary
from .query_results_ordered_by_summary import QueryResultsOrderedBySummary
from .quick_pick_summary import QuickPickSummary
from .snapshot_detail import SnapshotDetail
from .span import Span
from .span_log import SpanLog
from .span_log_collection import SpanLogCollection
from .span_snapshot import SpanSnapshot
from .stack_trace_element import StackTraceElement
from .tag import Tag
from .thread_snapshot import ThreadSnapshot
from .trace import Trace
from .trace_service_summary import TraceServiceSummary
from .trace_snapshot import TraceSnapshot
from .trace_span_summary import TraceSpanSummary

# Maps type names to classes for apm_traces services.
apm_traces_type_mapping = {
    "AggregatedSnapshot": AggregatedSnapshot,
    "AggregatedStackTrace": AggregatedStackTrace,
    "QueryDetails": QueryDetails,
    "QueryResultMetadataSummary": QueryResultMetadataSummary,
    "QueryResultResponse": QueryResultResponse,
    "QueryResultRow": QueryResultRow,
    "QueryResultRowTypeSummary": QueryResultRowTypeSummary,
    "QueryResultsGroupedBySummary": QueryResultsGroupedBySummary,
    "QueryResultsOrderedBySummary": QueryResultsOrderedBySummary,
    "QuickPickSummary": QuickPickSummary,
    "SnapshotDetail": SnapshotDetail,
    "Span": Span,
    "SpanLog": SpanLog,
    "SpanLogCollection": SpanLogCollection,
    "SpanSnapshot": SpanSnapshot,
    "StackTraceElement": StackTraceElement,
    "Tag": Tag,
    "ThreadSnapshot": ThreadSnapshot,
    "Trace": Trace,
    "TraceServiceSummary": TraceServiceSummary,
    "TraceSnapshot": TraceSnapshot,
    "TraceSpanSummary": TraceSpanSummary
}
