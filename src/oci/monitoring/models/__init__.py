# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .aggregated_datapoint import AggregatedDatapoint
from .alarm import Alarm
from .alarm_dimension_states_collection import AlarmDimensionStatesCollection
from .alarm_dimension_states_entry import AlarmDimensionStatesEntry
from .alarm_history_collection import AlarmHistoryCollection
from .alarm_history_entry import AlarmHistoryEntry
from .alarm_status_summary import AlarmStatusSummary
from .alarm_summary import AlarmSummary
from .change_alarm_compartment_details import ChangeAlarmCompartmentDetails
from .create_alarm_details import CreateAlarmDetails
from .datapoint import Datapoint
from .failed_metric_record import FailedMetricRecord
from .list_metrics_details import ListMetricsDetails
from .metric import Metric
from .metric_data import MetricData
from .metric_data_details import MetricDataDetails
from .post_metric_data_details import PostMetricDataDetails
from .post_metric_data_response_details import PostMetricDataResponseDetails
from .retrieve_dimension_states_details import RetrieveDimensionStatesDetails
from .summarize_metrics_data_details import SummarizeMetricsDataDetails
from .suppression import Suppression
from .update_alarm_details import UpdateAlarmDetails

# Maps type names to classes for monitoring services.
monitoring_type_mapping = {
    "AggregatedDatapoint": AggregatedDatapoint,
    "Alarm": Alarm,
    "AlarmDimensionStatesCollection": AlarmDimensionStatesCollection,
    "AlarmDimensionStatesEntry": AlarmDimensionStatesEntry,
    "AlarmHistoryCollection": AlarmHistoryCollection,
    "AlarmHistoryEntry": AlarmHistoryEntry,
    "AlarmStatusSummary": AlarmStatusSummary,
    "AlarmSummary": AlarmSummary,
    "ChangeAlarmCompartmentDetails": ChangeAlarmCompartmentDetails,
    "CreateAlarmDetails": CreateAlarmDetails,
    "Datapoint": Datapoint,
    "FailedMetricRecord": FailedMetricRecord,
    "ListMetricsDetails": ListMetricsDetails,
    "Metric": Metric,
    "MetricData": MetricData,
    "MetricDataDetails": MetricDataDetails,
    "PostMetricDataDetails": PostMetricDataDetails,
    "PostMetricDataResponseDetails": PostMetricDataResponseDetails,
    "RetrieveDimensionStatesDetails": RetrieveDimensionStatesDetails,
    "SummarizeMetricsDataDetails": SummarizeMetricsDataDetails,
    "Suppression": Suppression,
    "UpdateAlarmDetails": UpdateAlarmDetails
}
