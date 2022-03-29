# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InternationalMarketPrice(object):
    """
    The model for international market pricing.
    """

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "USD"
    CURRENCY_CODE_USD = "USD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "CAD"
    CURRENCY_CODE_CAD = "CAD"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "INR"
    CURRENCY_CODE_INR = "INR"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "GBP"
    CURRENCY_CODE_GBP = "GBP"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "BRL"
    CURRENCY_CODE_BRL = "BRL"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "JPY"
    CURRENCY_CODE_JPY = "JPY"

    #: A constant which can be used with the currency_code property of a InternationalMarketPrice.
    #: This constant has a value of "OMR"
    CURRENCY_CODE_OMR = "OMR"

    def __init__(self, **kwargs):
        """
        Initializes a new InternationalMarketPrice object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param currency_code:
            The value to assign to the currency_code property of this InternationalMarketPrice.
            Allowed values for this property are: "USD", "CAD", "INR", "GBP", "BRL", "JPY", "OMR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type currency_code: str

        :param currency_symbol:
            The value to assign to the currency_symbol property of this InternationalMarketPrice.
        :type currency_symbol: str

        :param rate:
            The value to assign to the rate property of this InternationalMarketPrice.
        :type rate: float

        """
        self.swagger_types = {
            'currency_code': 'str',
            'currency_symbol': 'str',
            'rate': 'float'
        }

        self.attribute_map = {
            'currency_code': 'currencyCode',
            'currency_symbol': 'currencySymbol',
            'rate': 'rate'
        }

        self._currency_code = None
        self._currency_symbol = None
        self._rate = None

    @property
    def currency_code(self):
        """
        **[Required]** Gets the currency_code of this InternationalMarketPrice.
        The currency of the pricing model.

        Allowed values for this property are: "USD", "CAD", "INR", "GBP", "BRL", "JPY", "OMR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The currency_code of this InternationalMarketPrice.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this InternationalMarketPrice.
        The currency of the pricing model.


        :param currency_code: The currency_code of this InternationalMarketPrice.
        :type: str
        """
        allowed_values = ["USD", "CAD", "INR", "GBP", "BRL", "JPY", "OMR"]
        if not value_allowed_none_or_none_sentinel(currency_code, allowed_values):
            currency_code = 'UNKNOWN_ENUM_VALUE'
        self._currency_code = currency_code

    @property
    def currency_symbol(self):
        """
        Gets the currency_symbol of this InternationalMarketPrice.
        The symbol of the currency


        :return: The currency_symbol of this InternationalMarketPrice.
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """
        Sets the currency_symbol of this InternationalMarketPrice.
        The symbol of the currency


        :param currency_symbol: The currency_symbol of this InternationalMarketPrice.
        :type: str
        """
        self._currency_symbol = currency_symbol

    @property
    def rate(self):
        """
        **[Required]** Gets the rate of this InternationalMarketPrice.
        The pricing rate.


        :return: The rate of this InternationalMarketPrice.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this InternationalMarketPrice.
        The pricing rate.


        :param rate: The rate of this InternationalMarketPrice.
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
