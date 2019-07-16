# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .create_quota_details import CreateQuotaDetails
from .quota import Quota
from .quota_summary import QuotaSummary
from .update_quota_details import UpdateQuotaDetails

# Maps type names to classes for limits services.
limits_type_mapping = {
    "CreateQuotaDetails": CreateQuotaDetails,
    "Quota": Quota,
    "QuotaSummary": QuotaSummary,
    "UpdateQuotaDetails": UpdateQuotaDetails
}
