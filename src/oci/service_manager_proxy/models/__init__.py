# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .error_entity import ErrorEntity
from .service_definition import ServiceDefinition
from .service_environment import ServiceEnvironment
from .service_environment_collection import ServiceEnvironmentCollection
from .service_environment_end_point_overview import ServiceEnvironmentEndPointOverview
from .service_environment_summary import ServiceEnvironmentSummary

# Maps type names to classes for service_manager_proxy services.
service_manager_proxy_type_mapping = {
    "ErrorEntity": ErrorEntity,
    "ServiceDefinition": ServiceDefinition,
    "ServiceEnvironment": ServiceEnvironment,
    "ServiceEnvironmentCollection": ServiceEnvironmentCollection,
    "ServiceEnvironmentEndPointOverview": ServiceEnvironmentEndPointOverview,
    "ServiceEnvironmentSummary": ServiceEnvironmentSummary
}
