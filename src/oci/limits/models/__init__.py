# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

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
