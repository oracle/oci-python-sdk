# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .analytics_instance import AnalyticsInstance
from .analytics_instance_summary import AnalyticsInstanceSummary
from .capacity import Capacity
from .change_compartment_details import ChangeCompartmentDetails
from .create_analytics_instance_details import CreateAnalyticsInstanceDetails
from .scale_analytics_instance_details import ScaleAnalyticsInstanceDetails
from .update_analytics_instance_details import UpdateAnalyticsInstanceDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log import WorkRequestLog
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for analytics services.
analytics_type_mapping = {
    "AnalyticsInstance": AnalyticsInstance,
    "AnalyticsInstanceSummary": AnalyticsInstanceSummary,
    "Capacity": Capacity,
    "ChangeCompartmentDetails": ChangeCompartmentDetails,
    "CreateAnalyticsInstanceDetails": CreateAnalyticsInstanceDetails,
    "ScaleAnalyticsInstanceDetails": ScaleAnalyticsInstanceDetails,
    "UpdateAnalyticsInstanceDetails": UpdateAnalyticsInstanceDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
