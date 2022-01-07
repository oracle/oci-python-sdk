# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ThirdPartyPaidListingEligibility(object):
    """
    Tenant eligibility for using third party paid listings
    """

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "ELIGIBLE"
    ELIGIBILITY_REASON_ELIGIBLE = "ELIGIBLE"

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_COUNTRY"
    ELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_COUNTRY = "INELIGIBLE_ACCOUNT_COUNTRY"

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "INELIGIBLE_REGION"
    ELIGIBILITY_REASON_INELIGIBLE_REGION = "INELIGIBLE_REGION"

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_BLACKLISTED"
    ELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_BLACKLISTED = "INELIGIBLE_ACCOUNT_BLACKLISTED"

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_FEATURE_DISABLED"
    ELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_FEATURE_DISABLED = "INELIGIBLE_ACCOUNT_FEATURE_DISABLED"

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_CURRENCY"
    ELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_CURRENCY = "INELIGIBLE_ACCOUNT_CURRENCY"

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_NOT_PAID"
    ELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_NOT_PAID = "INELIGIBLE_ACCOUNT_NOT_PAID"

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_INTERNAL"
    ELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_INTERNAL = "INELIGIBLE_ACCOUNT_INTERNAL"

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION"
    ELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION = "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION"

    #: A constant which can be used with the eligibility_reason property of a ThirdPartyPaidListingEligibility.
    #: This constant has a value of "NOT_AUTHORIZED"
    ELIGIBILITY_REASON_NOT_AUTHORIZED = "NOT_AUTHORIZED"

    def __init__(self, **kwargs):
        """
        Initializes a new ThirdPartyPaidListingEligibility object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_paid_listing_eligible:
            The value to assign to the is_paid_listing_eligible property of this ThirdPartyPaidListingEligibility.
        :type is_paid_listing_eligible: bool

        :param is_paid_listing_throttled:
            The value to assign to the is_paid_listing_throttled property of this ThirdPartyPaidListingEligibility.
        :type is_paid_listing_throttled: bool

        :param eligibility_reason:
            The value to assign to the eligibility_reason property of this ThirdPartyPaidListingEligibility.
            Allowed values for this property are: "ELIGIBLE", "INELIGIBLE_ACCOUNT_COUNTRY", "INELIGIBLE_REGION", "INELIGIBLE_ACCOUNT_BLACKLISTED", "INELIGIBLE_ACCOUNT_FEATURE_DISABLED", "INELIGIBLE_ACCOUNT_CURRENCY", "INELIGIBLE_ACCOUNT_NOT_PAID", "INELIGIBLE_ACCOUNT_INTERNAL", "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION", "NOT_AUTHORIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type eligibility_reason: str

        """
        self.swagger_types = {
            'is_paid_listing_eligible': 'bool',
            'is_paid_listing_throttled': 'bool',
            'eligibility_reason': 'str'
        }

        self.attribute_map = {
            'is_paid_listing_eligible': 'isPaidListingEligible',
            'is_paid_listing_throttled': 'isPaidListingThrottled',
            'eligibility_reason': 'eligibilityReason'
        }

        self._is_paid_listing_eligible = None
        self._is_paid_listing_throttled = None
        self._eligibility_reason = None

    @property
    def is_paid_listing_eligible(self):
        """
        **[Required]** Gets the is_paid_listing_eligible of this ThirdPartyPaidListingEligibility.
        Whether the tenant is permitted to use paid listings


        :return: The is_paid_listing_eligible of this ThirdPartyPaidListingEligibility.
        :rtype: bool
        """
        return self._is_paid_listing_eligible

    @is_paid_listing_eligible.setter
    def is_paid_listing_eligible(self, is_paid_listing_eligible):
        """
        Sets the is_paid_listing_eligible of this ThirdPartyPaidListingEligibility.
        Whether the tenant is permitted to use paid listings


        :param is_paid_listing_eligible: The is_paid_listing_eligible of this ThirdPartyPaidListingEligibility.
        :type: bool
        """
        self._is_paid_listing_eligible = is_paid_listing_eligible

    @property
    def is_paid_listing_throttled(self):
        """
        **[Required]** Gets the is_paid_listing_throttled of this ThirdPartyPaidListingEligibility.
        Whether the tenant is currently prevented from using paid listings because of throttling


        :return: The is_paid_listing_throttled of this ThirdPartyPaidListingEligibility.
        :rtype: bool
        """
        return self._is_paid_listing_throttled

    @is_paid_listing_throttled.setter
    def is_paid_listing_throttled(self, is_paid_listing_throttled):
        """
        Sets the is_paid_listing_throttled of this ThirdPartyPaidListingEligibility.
        Whether the tenant is currently prevented from using paid listings because of throttling


        :param is_paid_listing_throttled: The is_paid_listing_throttled of this ThirdPartyPaidListingEligibility.
        :type: bool
        """
        self._is_paid_listing_throttled = is_paid_listing_throttled

    @property
    def eligibility_reason(self):
        """
        **[Required]** Gets the eligibility_reason of this ThirdPartyPaidListingEligibility.
        Reason the account is ineligible to launch paid listings

        Allowed values for this property are: "ELIGIBLE", "INELIGIBLE_ACCOUNT_COUNTRY", "INELIGIBLE_REGION", "INELIGIBLE_ACCOUNT_BLACKLISTED", "INELIGIBLE_ACCOUNT_FEATURE_DISABLED", "INELIGIBLE_ACCOUNT_CURRENCY", "INELIGIBLE_ACCOUNT_NOT_PAID", "INELIGIBLE_ACCOUNT_INTERNAL", "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION", "NOT_AUTHORIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The eligibility_reason of this ThirdPartyPaidListingEligibility.
        :rtype: str
        """
        return self._eligibility_reason

    @eligibility_reason.setter
    def eligibility_reason(self, eligibility_reason):
        """
        Sets the eligibility_reason of this ThirdPartyPaidListingEligibility.
        Reason the account is ineligible to launch paid listings


        :param eligibility_reason: The eligibility_reason of this ThirdPartyPaidListingEligibility.
        :type: str
        """
        allowed_values = ["ELIGIBLE", "INELIGIBLE_ACCOUNT_COUNTRY", "INELIGIBLE_REGION", "INELIGIBLE_ACCOUNT_BLACKLISTED", "INELIGIBLE_ACCOUNT_FEATURE_DISABLED", "INELIGIBLE_ACCOUNT_CURRENCY", "INELIGIBLE_ACCOUNT_NOT_PAID", "INELIGIBLE_ACCOUNT_INTERNAL", "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION", "NOT_AUTHORIZED"]
        if not value_allowed_none_or_none_sentinel(eligibility_reason, allowed_values):
            eligibility_reason = 'UNKNOWN_ENUM_VALUE'
        self._eligibility_reason = eligibility_reason

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
