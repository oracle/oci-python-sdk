# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .create_dashboard_details import CreateDashboardDetails
from .create_dashboard_group_details import CreateDashboardGroupDetails
from .create_v1_dashboard_details import CreateV1DashboardDetails
from .dashboard import Dashboard
from .dashboard_collection import DashboardCollection
from .dashboard_group import DashboardGroup
from .dashboard_group_collection import DashboardGroupCollection
from .dashboard_group_summary import DashboardGroupSummary
from .dashboard_summary import DashboardSummary
from .update_dashboard_details import UpdateDashboardDetails
from .update_dashboard_group_details import UpdateDashboardGroupDetails
from .update_v1_dashboard_details import UpdateV1DashboardDetails
from .v1_dashboard import V1Dashboard

# Maps type names to classes for dashboard_service services.
dashboard_service_type_mapping = {
    "CreateDashboardDetails": CreateDashboardDetails,
    "CreateDashboardGroupDetails": CreateDashboardGroupDetails,
    "CreateV1DashboardDetails": CreateV1DashboardDetails,
    "Dashboard": Dashboard,
    "DashboardCollection": DashboardCollection,
    "DashboardGroup": DashboardGroup,
    "DashboardGroupCollection": DashboardGroupCollection,
    "DashboardGroupSummary": DashboardGroupSummary,
    "DashboardSummary": DashboardSummary,
    "UpdateDashboardDetails": UpdateDashboardDetails,
    "UpdateDashboardGroupDetails": UpdateDashboardGroupDetails,
    "UpdateV1DashboardDetails": UpdateV1DashboardDetails,
    "V1Dashboard": V1Dashboard
}
