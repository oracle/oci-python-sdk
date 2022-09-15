# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .data_attribution import DataAttribution
from .data_visibility import DataVisibility
from .entity_reference import EntityReference
from .geodata_details import GeodataDetails
from .indicator import Indicator
from .indicator_attribute import IndicatorAttribute
from .indicator_attribute_summary import IndicatorAttributeSummary
from .indicator_count_collection import IndicatorCountCollection
from .indicator_count_dimensions import IndicatorCountDimensions
from .indicator_count_summary import IndicatorCountSummary
from .indicator_reference import IndicatorReference
from .indicator_relationship import IndicatorRelationship
from .indicator_source_summary import IndicatorSourceSummary
from .indicator_summary import IndicatorSummary
from .indicator_summary_collection import IndicatorSummaryCollection
from .summarize_indicators_details import SummarizeIndicatorsDetails
from .threat_type import ThreatType
from .threat_type_summary import ThreatTypeSummary
from .threat_types_collection import ThreatTypesCollection

# Maps type names to classes for threat_intelligence services.
threat_intelligence_type_mapping = {
    "DataAttribution": DataAttribution,
    "DataVisibility": DataVisibility,
    "EntityReference": EntityReference,
    "GeodataDetails": GeodataDetails,
    "Indicator": Indicator,
    "IndicatorAttribute": IndicatorAttribute,
    "IndicatorAttributeSummary": IndicatorAttributeSummary,
    "IndicatorCountCollection": IndicatorCountCollection,
    "IndicatorCountDimensions": IndicatorCountDimensions,
    "IndicatorCountSummary": IndicatorCountSummary,
    "IndicatorReference": IndicatorReference,
    "IndicatorRelationship": IndicatorRelationship,
    "IndicatorSourceSummary": IndicatorSourceSummary,
    "IndicatorSummary": IndicatorSummary,
    "IndicatorSummaryCollection": IndicatorSummaryCollection,
    "SummarizeIndicatorsDetails": SummarizeIndicatorsDetails,
    "ThreatType": ThreatType,
    "ThreatTypeSummary": ThreatTypeSummary,
    "ThreatTypesCollection": ThreatTypesCollection
}
