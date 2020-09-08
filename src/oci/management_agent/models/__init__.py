# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .create_management_agent_install_key_details import CreateManagementAgentInstallKeyDetails
from .deploy_plugins_details import DeployPluginsDetails
from .management_agent import ManagementAgent
from .management_agent_error import ManagementAgentError
from .management_agent_image import ManagementAgentImage
from .management_agent_image_summary import ManagementAgentImageSummary
from .management_agent_install_key import ManagementAgentInstallKey
from .management_agent_install_key_summary import ManagementAgentInstallKeySummary
from .management_agent_plugin import ManagementAgentPlugin
from .management_agent_plugin_details import ManagementAgentPluginDetails
from .management_agent_plugin_summary import ManagementAgentPluginSummary
from .management_agent_summary import ManagementAgentSummary
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
    "CreateManagementAgentInstallKeyDetails": CreateManagementAgentInstallKeyDetails,
    "DeployPluginsDetails": DeployPluginsDetails,
    "ManagementAgent": ManagementAgent,
    "ManagementAgentError": ManagementAgentError,
    "ManagementAgentImage": ManagementAgentImage,
    "ManagementAgentImageSummary": ManagementAgentImageSummary,
    "ManagementAgentInstallKey": ManagementAgentInstallKey,
    "ManagementAgentInstallKeySummary": ManagementAgentInstallKeySummary,
    "ManagementAgentPlugin": ManagementAgentPlugin,
    "ManagementAgentPluginDetails": ManagementAgentPluginDetails,
    "ManagementAgentPluginSummary": ManagementAgentPluginSummary,
    "ManagementAgentSummary": ManagementAgentSummary,
    "UpdateManagementAgentDetails": UpdateManagementAgentDetails,
    "UpdateManagementAgentInstallKeyDetails": UpdateManagementAgentInstallKeyDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkSubmissionKey": WorkSubmissionKey
}
