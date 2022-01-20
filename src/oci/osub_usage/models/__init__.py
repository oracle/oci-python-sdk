# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .computed_usage import ComputedUsage
from .computed_usage_aggregated_summary import ComputedUsageAggregatedSummary
from .computed_usage_aggregation import ComputedUsageAggregation
from .computed_usage_summary import ComputedUsageSummary
from .product import Product

# Maps type names to classes for osub_usage services.
osub_usage_type_mapping = {
    "ComputedUsage": ComputedUsage,
    "ComputedUsageAggregatedSummary": ComputedUsageAggregatedSummary,
    "ComputedUsageAggregation": ComputedUsageAggregation,
    "ComputedUsageSummary": ComputedUsageSummary,
    "Product": Product
}
