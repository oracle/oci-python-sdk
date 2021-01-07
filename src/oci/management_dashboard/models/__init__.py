# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_management_dashboards_compartment_details import ChangeManagementDashboardsCompartmentDetails
from .change_management_saved_searches_compartment_details import ChangeManagementSavedSearchesCompartmentDetails
from .create_management_dashboard_details import CreateManagementDashboardDetails
from .create_management_saved_search_details import CreateManagementSavedSearchDetails
from .management_dashboard import ManagementDashboard
from .management_dashboard_collection import ManagementDashboardCollection
from .management_dashboard_export_details import ManagementDashboardExportDetails
from .management_dashboard_for_import_export_details import ManagementDashboardForImportExportDetails
from .management_dashboard_import_details import ManagementDashboardImportDetails
from .management_dashboard_summary import ManagementDashboardSummary
from .management_dashboard_tile_details import ManagementDashboardTileDetails
from .management_saved_search import ManagementSavedSearch
from .management_saved_search_collection import ManagementSavedSearchCollection
from .management_saved_search_for_import_details import ManagementSavedSearchForImportDetails
from .management_saved_search_summary import ManagementSavedSearchSummary
from .update_management_dashboard_details import UpdateManagementDashboardDetails
from .update_management_saved_search_details import UpdateManagementSavedSearchDetails

# Maps type names to classes for management_dashboard services.
management_dashboard_type_mapping = {
    "ChangeManagementDashboardsCompartmentDetails": ChangeManagementDashboardsCompartmentDetails,
    "ChangeManagementSavedSearchesCompartmentDetails": ChangeManagementSavedSearchesCompartmentDetails,
    "CreateManagementDashboardDetails": CreateManagementDashboardDetails,
    "CreateManagementSavedSearchDetails": CreateManagementSavedSearchDetails,
    "ManagementDashboard": ManagementDashboard,
    "ManagementDashboardCollection": ManagementDashboardCollection,
    "ManagementDashboardExportDetails": ManagementDashboardExportDetails,
    "ManagementDashboardForImportExportDetails": ManagementDashboardForImportExportDetails,
    "ManagementDashboardImportDetails": ManagementDashboardImportDetails,
    "ManagementDashboardSummary": ManagementDashboardSummary,
    "ManagementDashboardTileDetails": ManagementDashboardTileDetails,
    "ManagementSavedSearch": ManagementSavedSearch,
    "ManagementSavedSearchCollection": ManagementSavedSearchCollection,
    "ManagementSavedSearchForImportDetails": ManagementSavedSearchForImportDetails,
    "ManagementSavedSearchSummary": ManagementSavedSearchSummary,
    "UpdateManagementDashboardDetails": UpdateManagementDashboardDetails,
    "UpdateManagementSavedSearchDetails": UpdateManagementSavedSearchDetails
}
