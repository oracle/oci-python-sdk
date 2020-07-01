# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .analytics_instance import AnalyticsInstance
from .analytics_instance_summary import AnalyticsInstanceSummary
from .capacity import Capacity
from .change_analytics_instance_network_endpoint_details import ChangeAnalyticsInstanceNetworkEndpointDetails
from .change_compartment_details import ChangeCompartmentDetails
from .create_analytics_instance_details import CreateAnalyticsInstanceDetails
from .network_endpoint_details import NetworkEndpointDetails
from .private_endpoint_details import PrivateEndpointDetails
from .public_endpoint_details import PublicEndpointDetails
from .scale_analytics_instance_details import ScaleAnalyticsInstanceDetails
from .update_analytics_instance_details import UpdateAnalyticsInstanceDetails
from .virtual_cloud_network import VirtualCloudNetwork
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
    "ChangeAnalyticsInstanceNetworkEndpointDetails": ChangeAnalyticsInstanceNetworkEndpointDetails,
    "ChangeCompartmentDetails": ChangeCompartmentDetails,
    "CreateAnalyticsInstanceDetails": CreateAnalyticsInstanceDetails,
    "NetworkEndpointDetails": NetworkEndpointDetails,
    "PrivateEndpointDetails": PrivateEndpointDetails,
    "PublicEndpointDetails": PublicEndpointDetails,
    "ScaleAnalyticsInstanceDetails": ScaleAnalyticsInstanceDetails,
    "UpdateAnalyticsInstanceDetails": UpdateAnalyticsInstanceDetails,
    "VirtualCloudNetwork": VirtualCloudNetwork,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
