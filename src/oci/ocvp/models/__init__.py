# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_sddc_compartment_details import ChangeSddcCompartmentDetails
from .create_esxi_host_details import CreateEsxiHostDetails
from .create_sddc_details import CreateSddcDetails
from .esxi_host import EsxiHost
from .esxi_host_collection import EsxiHostCollection
from .esxi_host_summary import EsxiHostSummary
from .sddc import Sddc
from .sddc_collection import SddcCollection
from .sddc_summary import SddcSummary
from .supported_vmware_software_version_collection import SupportedVmwareSoftwareVersionCollection
from .supported_vmware_software_version_summary import SupportedVmwareSoftwareVersionSummary
from .update_esxi_host_details import UpdateEsxiHostDetails
from .update_sddc_details import UpdateSddcDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource

# Maps type names to classes for ocvp services.
ocvp_type_mapping = {
    "ChangeSddcCompartmentDetails": ChangeSddcCompartmentDetails,
    "CreateEsxiHostDetails": CreateEsxiHostDetails,
    "CreateSddcDetails": CreateSddcDetails,
    "EsxiHost": EsxiHost,
    "EsxiHostCollection": EsxiHostCollection,
    "EsxiHostSummary": EsxiHostSummary,
    "Sddc": Sddc,
    "SddcCollection": SddcCollection,
    "SddcSummary": SddcSummary,
    "SupportedVmwareSoftwareVersionCollection": SupportedVmwareSoftwareVersionCollection,
    "SupportedVmwareSoftwareVersionSummary": SupportedVmwareSoftwareVersionSummary,
    "UpdateEsxiHostDetails": UpdateEsxiHostDetails,
    "UpdateSddcDetails": UpdateSddcDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource
}
