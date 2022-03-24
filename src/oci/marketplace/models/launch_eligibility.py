# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchEligibility(object):
    """
    Tenant eligibility and other information for launching a PIC image
    """

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_COUNTRY"
    INELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_COUNTRY = "INELIGIBLE_ACCOUNT_COUNTRY"

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "INELIGIBLE_REGION"
    INELIGIBILITY_REASON_INELIGIBLE_REGION = "INELIGIBLE_REGION"

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_BLACKLISTED"
    INELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_BLACKLISTED = "INELIGIBLE_ACCOUNT_BLACKLISTED"

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_FEATURE_DISABLED"
    INELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_FEATURE_DISABLED = "INELIGIBLE_ACCOUNT_FEATURE_DISABLED"

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_CURRENCY"
    INELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_CURRENCY = "INELIGIBLE_ACCOUNT_CURRENCY"

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_NOT_PAID"
    INELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_NOT_PAID = "INELIGIBLE_ACCOUNT_NOT_PAID"

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_INTERNAL"
    INELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_INTERNAL = "INELIGIBLE_ACCOUNT_INTERNAL"

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION"
    INELIGIBILITY_REASON_INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION = "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION"

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "INELIGIBLE_PAID_LISTING_THROTTLED"
    INELIGIBILITY_REASON_INELIGIBLE_PAID_LISTING_THROTTLED = "INELIGIBLE_PAID_LISTING_THROTTLED"

    #: A constant which can be used with the ineligibility_reason property of a LaunchEligibility.
    #: This constant has a value of "NOT_AUTHORIZED"
    INELIGIBILITY_REASON_NOT_AUTHORIZED = "NOT_AUTHORIZED"

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchEligibility object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param image_id:
            The value to assign to the image_id property of this LaunchEligibility.
        :type image_id: str

        :param is_launch_allowed:
            The value to assign to the is_launch_allowed property of this LaunchEligibility.
        :type is_launch_allowed: bool

        :param meters:
            The value to assign to the meters property of this LaunchEligibility.
        :type meters: str

        :param ineligibility_reason:
            The value to assign to the ineligibility_reason property of this LaunchEligibility.
            Allowed values for this property are: "INELIGIBLE_ACCOUNT_COUNTRY", "INELIGIBLE_REGION", "INELIGIBLE_ACCOUNT_BLACKLISTED", "INELIGIBLE_ACCOUNT_FEATURE_DISABLED", "INELIGIBLE_ACCOUNT_CURRENCY", "INELIGIBLE_ACCOUNT_NOT_PAID", "INELIGIBLE_ACCOUNT_INTERNAL", "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION", "INELIGIBLE_PAID_LISTING_THROTTLED", "NOT_AUTHORIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ineligibility_reason: str

        """
        self.swagger_types = {
            'image_id': 'str',
            'is_launch_allowed': 'bool',
            'meters': 'str',
            'ineligibility_reason': 'str'
        }

        self.attribute_map = {
            'image_id': 'imageId',
            'is_launch_allowed': 'isLaunchAllowed',
            'meters': 'meters',
            'ineligibility_reason': 'ineligibilityReason'
        }

        self._image_id = None
        self._is_launch_allowed = None
        self._meters = None
        self._ineligibility_reason = None

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this LaunchEligibility.
        PIC Image ID


        :return: The image_id of this LaunchEligibility.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this LaunchEligibility.
        PIC Image ID


        :param image_id: The image_id of this LaunchEligibility.
        :type: str
        """
        self._image_id = image_id

    @property
    def is_launch_allowed(self):
        """
        **[Required]** Gets the is_launch_allowed of this LaunchEligibility.
        Is the tenant permitted to launch the PIC image


        :return: The is_launch_allowed of this LaunchEligibility.
        :rtype: bool
        """
        return self._is_launch_allowed

    @is_launch_allowed.setter
    def is_launch_allowed(self, is_launch_allowed):
        """
        Sets the is_launch_allowed of this LaunchEligibility.
        Is the tenant permitted to launch the PIC image


        :param is_launch_allowed: The is_launch_allowed of this LaunchEligibility.
        :type: bool
        """
        self._is_launch_allowed = is_launch_allowed

    @property
    def meters(self):
        """
        Gets the meters of this LaunchEligibility.
        related meters for the PIC image


        :return: The meters of this LaunchEligibility.
        :rtype: str
        """
        return self._meters

    @meters.setter
    def meters(self, meters):
        """
        Sets the meters of this LaunchEligibility.
        related meters for the PIC image


        :param meters: The meters of this LaunchEligibility.
        :type: str
        """
        self._meters = meters

    @property
    def ineligibility_reason(self):
        """
        Gets the ineligibility_reason of this LaunchEligibility.
        Reason the account is ineligible to launch paid listings

        Allowed values for this property are: "INELIGIBLE_ACCOUNT_COUNTRY", "INELIGIBLE_REGION", "INELIGIBLE_ACCOUNT_BLACKLISTED", "INELIGIBLE_ACCOUNT_FEATURE_DISABLED", "INELIGIBLE_ACCOUNT_CURRENCY", "INELIGIBLE_ACCOUNT_NOT_PAID", "INELIGIBLE_ACCOUNT_INTERNAL", "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION", "INELIGIBLE_PAID_LISTING_THROTTLED", "NOT_AUTHORIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ineligibility_reason of this LaunchEligibility.
        :rtype: str
        """
        return self._ineligibility_reason

    @ineligibility_reason.setter
    def ineligibility_reason(self, ineligibility_reason):
        """
        Sets the ineligibility_reason of this LaunchEligibility.
        Reason the account is ineligible to launch paid listings


        :param ineligibility_reason: The ineligibility_reason of this LaunchEligibility.
        :type: str
        """
        allowed_values = ["INELIGIBLE_ACCOUNT_COUNTRY", "INELIGIBLE_REGION", "INELIGIBLE_ACCOUNT_BLACKLISTED", "INELIGIBLE_ACCOUNT_FEATURE_DISABLED", "INELIGIBLE_ACCOUNT_CURRENCY", "INELIGIBLE_ACCOUNT_NOT_PAID", "INELIGIBLE_ACCOUNT_INTERNAL", "INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION", "INELIGIBLE_PAID_LISTING_THROTTLED", "NOT_AUTHORIZED"]
        if not value_allowed_none_or_none_sentinel(ineligibility_reason, allowed_values):
            ineligibility_reason = 'UNKNOWN_ENUM_VALUE'
        self._ineligibility_reason = ineligibility_reason

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
