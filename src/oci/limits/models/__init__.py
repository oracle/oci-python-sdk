# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_lock_details import AddLockDetails
from .create_quota_details import CreateQuotaDetails
from .limit_definition_summary import LimitDefinitionSummary
from .limit_value_summary import LimitValueSummary
from .quota import Quota
from .quota_summary import QuotaSummary
from .remove_lock_details import RemoveLockDetails
from .resource_availability import ResourceAvailability
from .resource_lock import ResourceLock
from .service_summary import ServiceSummary
from .update_quota_details import UpdateQuotaDetails

# Maps type names to classes for limits services.
limits_type_mapping = {
    "AddLockDetails": AddLockDetails,
    "CreateQuotaDetails": CreateQuotaDetails,
    "LimitDefinitionSummary": LimitDefinitionSummary,
    "LimitValueSummary": LimitValueSummary,
    "Quota": Quota,
    "QuotaSummary": QuotaSummary,
    "RemoveLockDetails": RemoveLockDetails,
    "ResourceAvailability": ResourceAvailability,
    "ResourceLock": ResourceLock,
    "ServiceSummary": ServiceSummary,
    "UpdateQuotaDetails": UpdateQuotaDetails
}
