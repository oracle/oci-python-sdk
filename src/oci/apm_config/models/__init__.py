# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .apdex import Apdex
from .apdex_rules import ApdexRules
from .apdex_rules_summary import ApdexRulesSummary
from .config import Config
from .config_collection import ConfigCollection
from .config_summary import ConfigSummary
from .create_apdex_rules_details import CreateApdexRulesDetails
from .create_config_details import CreateConfigDetails
from .create_metric_group_details import CreateMetricGroupDetails
from .create_span_filter_details import CreateSpanFilterDetails
from .dimension import Dimension
from .metric import Metric
from .metric_group import MetricGroup
from .metric_group_summary import MetricGroupSummary
from .span_filter import SpanFilter
from .span_filter_summary import SpanFilterSummary
from .update_apdex_rules_details import UpdateApdexRulesDetails
from .update_config_details import UpdateConfigDetails
from .update_metric_group_details import UpdateMetricGroupDetails
from .update_span_filter_details import UpdateSpanFilterDetails

# Maps type names to classes for apm_config services.
apm_config_type_mapping = {
    "Apdex": Apdex,
    "ApdexRules": ApdexRules,
    "ApdexRulesSummary": ApdexRulesSummary,
    "Config": Config,
    "ConfigCollection": ConfigCollection,
    "ConfigSummary": ConfigSummary,
    "CreateApdexRulesDetails": CreateApdexRulesDetails,
    "CreateConfigDetails": CreateConfigDetails,
    "CreateMetricGroupDetails": CreateMetricGroupDetails,
    "CreateSpanFilterDetails": CreateSpanFilterDetails,
    "Dimension": Dimension,
    "Metric": Metric,
    "MetricGroup": MetricGroup,
    "MetricGroupSummary": MetricGroupSummary,
    "SpanFilter": SpanFilter,
    "SpanFilterSummary": SpanFilterSummary,
    "UpdateApdexRulesDetails": UpdateApdexRulesDetails,
    "UpdateConfigDetails": UpdateConfigDetails,
    "UpdateMetricGroupDetails": UpdateMetricGroupDetails,
    "UpdateSpanFilterDetails": UpdateSpanFilterDetails
}
