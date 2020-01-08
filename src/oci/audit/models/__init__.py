# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

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
