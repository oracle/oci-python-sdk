# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .aggregate_network_data_details import AggregateNetworkDataDetails
from .aggregated_network_data import AggregatedNetworkData
from .aggregated_network_data_result import AggregatedNetworkDataResult
from .browser_monitor_configuration import BrowserMonitorConfiguration
from .create_dedicated_vantage_point_details import CreateDedicatedVantagePointDetails
from .create_monitor_details import CreateMonitorDetails
from .create_script_details import CreateScriptDetails
from .dedicated_vantage_point import DedicatedVantagePoint
from .dedicated_vantage_point_collection import DedicatedVantagePointCollection
from .dedicated_vantage_point_summary import DedicatedVantagePointSummary
from .dns_configuration import DnsConfiguration
from .dvp_stack_details import DvpStackDetails
from .geo_summary import GeoSummary
from .header import Header
from .link import Link
from .monitor import Monitor
from .monitor_collection import MonitorCollection
from .monitor_configuration import MonitorConfiguration
from .monitor_result import MonitorResult
from .monitor_result_data import MonitorResultData
from .monitor_script_parameter import MonitorScriptParameter
from .monitor_script_parameter_info import MonitorScriptParameterInfo
from .monitor_status_count_map import MonitorStatusCountMap
from .monitor_summary import MonitorSummary
from .network_configuration import NetworkConfiguration
from .node import Node
from .oracle_rm_stack import OracleRMStack
from .public_vantage_point_collection import PublicVantagePointCollection
from .public_vantage_point_summary import PublicVantagePointSummary
from .request_authentication_details import RequestAuthenticationDetails
from .request_query_param import RequestQueryParam
from .rest_monitor_configuration import RestMonitorConfiguration
from .script import Script
from .script_collection import ScriptCollection
from .script_parameter import ScriptParameter
from .script_parameter_info import ScriptParameterInfo
from .script_summary import ScriptSummary
from .scripted_browser_monitor_configuration import ScriptedBrowserMonitorConfiguration
from .scripted_rest_monitor_configuration import ScriptedRestMonitorConfiguration
from .update_dedicated_vantage_point_details import UpdateDedicatedVantagePointDetails
from .update_monitor_details import UpdateMonitorDetails
from .update_script_details import UpdateScriptDetails
from .vantage_point_execution import VantagePointExecution
from .vantage_point_info import VantagePointInfo
from .vantage_point_node import VantagePointNode
from .verify_text import VerifyText

# Maps type names to classes for apm_synthetics services.
apm_synthetics_type_mapping = {
    "AggregateNetworkDataDetails": AggregateNetworkDataDetails,
    "AggregatedNetworkData": AggregatedNetworkData,
    "AggregatedNetworkDataResult": AggregatedNetworkDataResult,
    "BrowserMonitorConfiguration": BrowserMonitorConfiguration,
    "CreateDedicatedVantagePointDetails": CreateDedicatedVantagePointDetails,
    "CreateMonitorDetails": CreateMonitorDetails,
    "CreateScriptDetails": CreateScriptDetails,
    "DedicatedVantagePoint": DedicatedVantagePoint,
    "DedicatedVantagePointCollection": DedicatedVantagePointCollection,
    "DedicatedVantagePointSummary": DedicatedVantagePointSummary,
    "DnsConfiguration": DnsConfiguration,
    "DvpStackDetails": DvpStackDetails,
    "GeoSummary": GeoSummary,
    "Header": Header,
    "Link": Link,
    "Monitor": Monitor,
    "MonitorCollection": MonitorCollection,
    "MonitorConfiguration": MonitorConfiguration,
    "MonitorResult": MonitorResult,
    "MonitorResultData": MonitorResultData,
    "MonitorScriptParameter": MonitorScriptParameter,
    "MonitorScriptParameterInfo": MonitorScriptParameterInfo,
    "MonitorStatusCountMap": MonitorStatusCountMap,
    "MonitorSummary": MonitorSummary,
    "NetworkConfiguration": NetworkConfiguration,
    "Node": Node,
    "OracleRMStack": OracleRMStack,
    "PublicVantagePointCollection": PublicVantagePointCollection,
    "PublicVantagePointSummary": PublicVantagePointSummary,
    "RequestAuthenticationDetails": RequestAuthenticationDetails,
    "RequestQueryParam": RequestQueryParam,
    "RestMonitorConfiguration": RestMonitorConfiguration,
    "Script": Script,
    "ScriptCollection": ScriptCollection,
    "ScriptParameter": ScriptParameter,
    "ScriptParameterInfo": ScriptParameterInfo,
    "ScriptSummary": ScriptSummary,
    "ScriptedBrowserMonitorConfiguration": ScriptedBrowserMonitorConfiguration,
    "ScriptedRestMonitorConfiguration": ScriptedRestMonitorConfiguration,
    "UpdateDedicatedVantagePointDetails": UpdateDedicatedVantagePointDetails,
    "UpdateMonitorDetails": UpdateMonitorDetails,
    "UpdateScriptDetails": UpdateScriptDetails,
    "VantagePointExecution": VantagePointExecution,
    "VantagePointInfo": VantagePointInfo,
    "VantagePointNode": VantagePointNode,
    "VerifyText": VerifyText
}
