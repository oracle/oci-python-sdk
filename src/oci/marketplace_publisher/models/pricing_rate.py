# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PricingRate(object):
    """
    A pricing plan rate provided by the Publisher.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PricingRate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param billing_currency:
            The value to assign to the billing_currency property of this PricingRate.
        :type billing_currency: str

        :param rate:
            The value to assign to the rate property of this PricingRate.
        :type rate: float

        """
        self.swagger_types = {
            'billing_currency': 'str',
            'rate': 'float'
        }
        self.attribute_map = {
            'billing_currency': 'billingCurrency',
            'rate': 'rate'
        }
        self._billing_currency = None
        self._rate = None

    @property
    def billing_currency(self):
        """
        **[Required]** Gets the billing_currency of this PricingRate.
        The currency supported, in the format specified by ISO-4217


        :return: The billing_currency of this PricingRate.
        :rtype: str
        """
        return self._billing_currency

    @billing_currency.setter
    def billing_currency(self, billing_currency):
        """
        Sets the billing_currency of this PricingRate.
        The currency supported, in the format specified by ISO-4217


        :param billing_currency: The billing_currency of this PricingRate.
        :type: str
        """
        self._billing_currency = billing_currency

    @property
    def rate(self):
        """
        **[Required]** Gets the rate of this PricingRate.
        Tha amount for the currency type.


        :return: The rate of this PricingRate.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this PricingRate.
        Tha amount for the currency type.


        :param rate: The rate of this PricingRate.
        :type: float
        """
        self._rate = rate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
