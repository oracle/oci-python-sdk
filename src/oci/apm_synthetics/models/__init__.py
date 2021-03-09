# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .browser_monitor_configuration import BrowserMonitorConfiguration
from .create_monitor_details import CreateMonitorDetails
from .create_script_details import CreateScriptDetails
from .geo_summary import GeoSummary
from .header import Header
from .monitor import Monitor
from .monitor_collection import MonitorCollection
from .monitor_configuration import MonitorConfiguration
from .monitor_result import MonitorResult
from .monitor_result_data import MonitorResultData
from .monitor_script_parameter import MonitorScriptParameter
from .monitor_script_parameter_info import MonitorScriptParameterInfo
from .monitor_status_count_map import MonitorStatusCountMap
from .monitor_summary import MonitorSummary
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
from .update_monitor_details import UpdateMonitorDetails
from .update_script_details import UpdateScriptDetails
from .vantage_point_info import VantagePointInfo
from .verify_text import VerifyText

# Maps type names to classes for apm_synthetics services.
apm_synthetics_type_mapping = {
    "BrowserMonitorConfiguration": BrowserMonitorConfiguration,
    "CreateMonitorDetails": CreateMonitorDetails,
    "CreateScriptDetails": CreateScriptDetails,
    "GeoSummary": GeoSummary,
    "Header": Header,
    "Monitor": Monitor,
    "MonitorCollection": MonitorCollection,
    "MonitorConfiguration": MonitorConfiguration,
    "MonitorResult": MonitorResult,
    "MonitorResultData": MonitorResultData,
    "MonitorScriptParameter": MonitorScriptParameter,
    "MonitorScriptParameterInfo": MonitorScriptParameterInfo,
    "MonitorStatusCountMap": MonitorStatusCountMap,
    "MonitorSummary": MonitorSummary,
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
    "UpdateMonitorDetails": UpdateMonitorDetails,
    "UpdateScriptDetails": UpdateScriptDetails,
    "VantagePointInfo": VantagePointInfo,
    "VerifyText": VerifyText
}
