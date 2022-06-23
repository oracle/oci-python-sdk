# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_em_warehouse_compartment_details import ChangeEmWarehouseCompartmentDetails
from .create_em_warehouse_details import CreateEmWarehouseDetails
from .em_instances_details import EmInstancesDetails
from .em_warehouse import EmWarehouse
from .em_warehouse_collection import EmWarehouseCollection
from .em_warehouse_summary import EmWarehouseSummary
from .etl_run_collection import EtlRunCollection
from .etl_run_summary import EtlRunSummary
from .resource_usage import ResourceUsage
from .update_em_warehouse_details import UpdateEmWarehouseDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for em_warehouse services.
em_warehouse_type_mapping = {
    "ChangeEmWarehouseCompartmentDetails": ChangeEmWarehouseCompartmentDetails,
    "CreateEmWarehouseDetails": CreateEmWarehouseDetails,
    "EmInstancesDetails": EmInstancesDetails,
    "EmWarehouse": EmWarehouse,
    "EmWarehouseCollection": EmWarehouseCollection,
    "EmWarehouseSummary": EmWarehouseSummary,
    "EtlRunCollection": EtlRunCollection,
    "EtlRunSummary": EtlRunSummary,
    "ResourceUsage": ResourceUsage,
    "UpdateEmWarehouseDetails": UpdateEmWarehouseDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
