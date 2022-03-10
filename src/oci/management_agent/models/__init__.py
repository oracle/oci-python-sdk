# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .auto_upgradable_config import AutoUpgradableConfig
from .availability_history_summary import AvailabilityHistorySummary
from .create_management_agent_install_key_details import CreateManagementAgentInstallKeyDetails
from .deploy_plugins_details import DeployPluginsDetails
from .management_agent import ManagementAgent
from .management_agent_aggregation import ManagementAgentAggregation
from .management_agent_aggregation_collection import ManagementAgentAggregationCollection
from .management_agent_aggregation_dimensions import ManagementAgentAggregationDimensions
from .management_agent_error import ManagementAgentError
from .management_agent_image import ManagementAgentImage
from .management_agent_image_summary import ManagementAgentImageSummary
from .management_agent_install_key import ManagementAgentInstallKey
from .management_agent_install_key_summary import ManagementAgentInstallKeySummary
from .management_agent_plugin import ManagementAgentPlugin
from .management_agent_plugin_aggregation import ManagementAgentPluginAggregation
from .management_agent_plugin_aggregation_collection import ManagementAgentPluginAggregationCollection
from .management_agent_plugin_aggregation_dimensions import ManagementAgentPluginAggregationDimensions
from .management_agent_plugin_details import ManagementAgentPluginDetails
from .management_agent_plugin_summary import ManagementAgentPluginSummary
from .management_agent_summary import ManagementAgentSummary
from .set_auto_upgradable_config_details import SetAutoUpgradableConfigDetails
from .update_management_agent_details import UpdateManagementAgentDetails
from .update_management_agent_install_key_details import UpdateManagementAgentInstallKeyDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_submission_key import WorkSubmissionKey

# Maps type names to classes for management_agent services.
management_agent_type_mapping = {
    "AutoUpgradableConfig": AutoUpgradableConfig,
    "AvailabilityHistorySummary": AvailabilityHistorySummary,
    "CreateManagementAgentInstallKeyDetails": CreateManagementAgentInstallKeyDetails,
    "DeployPluginsDetails": DeployPluginsDetails,
    "ManagementAgent": ManagementAgent,
    "ManagementAgentAggregation": ManagementAgentAggregation,
    "ManagementAgentAggregationCollection": ManagementAgentAggregationCollection,
    "ManagementAgentAggregationDimensions": ManagementAgentAggregationDimensions,
    "ManagementAgentError": ManagementAgentError,
    "ManagementAgentImage": ManagementAgentImage,
    "ManagementAgentImageSummary": ManagementAgentImageSummary,
    "ManagementAgentInstallKey": ManagementAgentInstallKey,
    "ManagementAgentInstallKeySummary": ManagementAgentInstallKeySummary,
    "ManagementAgentPlugin": ManagementAgentPlugin,
    "ManagementAgentPluginAggregation": ManagementAgentPluginAggregation,
    "ManagementAgentPluginAggregationCollection": ManagementAgentPluginAggregationCollection,
    "ManagementAgentPluginAggregationDimensions": ManagementAgentPluginAggregationDimensions,
    "ManagementAgentPluginDetails": ManagementAgentPluginDetails,
    "ManagementAgentPluginSummary": ManagementAgentPluginSummary,
    "ManagementAgentSummary": ManagementAgentSummary,
    "SetAutoUpgradableConfigDetails": SetAutoUpgradableConfigDetails,
    "UpdateManagementAgentDetails": UpdateManagementAgentDetails,
    "UpdateManagementAgentInstallKeyDetails": UpdateManagementAgentInstallKeyDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkSubmissionKey": WorkSubmissionKey
}
