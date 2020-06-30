# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .configuration import Configuration
from .configuration_aggregation import ConfigurationAggregation
from .dimension import Dimension
from .filter import Filter
from .request_summarized_usages_details import RequestSummarizedUsagesDetails
from .tag import Tag
from .usage_aggregation import UsageAggregation
from .usage_summary import UsageSummary

# Maps type names to classes for usage_api services.
usage_api_type_mapping = {
    "Configuration": Configuration,
    "ConfigurationAggregation": ConfigurationAggregation,
    "Dimension": Dimension,
    "Filter": Filter,
    "RequestSummarizedUsagesDetails": RequestSummarizedUsagesDetails,
    "Tag": Tag,
    "UsageAggregation": UsageAggregation,
    "UsageSummary": UsageSummary
}
