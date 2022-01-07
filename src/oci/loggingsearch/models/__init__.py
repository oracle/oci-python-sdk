# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .field_info import FieldInfo
from .search_logs_details import SearchLogsDetails
from .search_response import SearchResponse
from .search_result import SearchResult
from .search_result_summary import SearchResultSummary

# Maps type names to classes for loggingsearch services.
loggingsearch_type_mapping = {
    "FieldInfo": FieldInfo,
    "SearchLogsDetails": SearchLogsDetails,
    "SearchResponse": SearchResponse,
    "SearchResult": SearchResult,
    "SearchResultSummary": SearchResultSummary
}
