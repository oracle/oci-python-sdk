# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .create_redeemable_user_details import CreateRedeemableUserDetails
from .monthly_reward_summary import MonthlyRewardSummary
from .product_collection import ProductCollection
from .product_summary import ProductSummary
from .redeemable_user import RedeemableUser
from .redeemable_user_collection import RedeemableUserCollection
from .redeemable_user_summary import RedeemableUserSummary
from .redemption_collection import RedemptionCollection
from .redemption_summary import RedemptionSummary
from .reward_collection import RewardCollection
from .reward_details import RewardDetails

# Maps type names to classes for usage services.
usage_type_mapping = {
    "CreateRedeemableUserDetails": CreateRedeemableUserDetails,
    "MonthlyRewardSummary": MonthlyRewardSummary,
    "ProductCollection": ProductCollection,
    "ProductSummary": ProductSummary,
    "RedeemableUser": RedeemableUser,
    "RedeemableUserCollection": RedeemableUserCollection,
    "RedeemableUserSummary": RedeemableUserSummary,
    "RedemptionCollection": RedemptionCollection,
    "RedemptionSummary": RedemptionSummary,
    "RewardCollection": RewardCollection,
    "RewardDetails": RewardDetails
}
