# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .audit_event import AuditEvent
from .configuration import Configuration
from .data import Data
from .identity import Identity
from .request import Request
from .response import Response
from .state_change import StateChange
from .update_configuration_details import UpdateConfigurationDetails

# Maps type names to classes for audit services.
audit_type_mapping = {
    "AuditEvent": AuditEvent,
    "Configuration": Configuration,
    "Data": Data,
    "Identity": Identity,
    "Request": Request,
    "Response": Response,
    "StateChange": StateChange,
    "UpdateConfigurationDetails": UpdateConfigurationDetails
}
