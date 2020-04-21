# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .create_quota_details import CreateQuotaDetails
from .limit_definition_summary import LimitDefinitionSummary
from .limit_value_summary import LimitValueSummary
from .quota import Quota
from .quota_summary import QuotaSummary
from .resource_availability import ResourceAvailability
from .service_summary import ServiceSummary
from .update_quota_details import UpdateQuotaDetails

# Maps type names to classes for limits services.
limits_type_mapping = {
    "CreateQuotaDetails": CreateQuotaDetails,
    "LimitDefinitionSummary": LimitDefinitionSummary,
    "LimitValueSummary": LimitValueSummary,
    "Quota": Quota,
    "QuotaSummary": QuotaSummary,
    "ResourceAvailability": ResourceAvailability,
    "ServiceSummary": ServiceSummary,
    "UpdateQuotaDetails": UpdateQuotaDetails
}
