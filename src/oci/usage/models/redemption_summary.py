# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RedemptionSummary(object):
    """
    The redemption summary for the requested subscription ID and date range.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RedemptionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_redeemed:
            The value to assign to the time_redeemed property of this RedemptionSummary.
        :type time_redeemed: datetime

        :param redemption_email:
            The value to assign to the redemption_email property of this RedemptionSummary.
        :type redemption_email: str

        :param redemption_code:
            The value to assign to the redemption_code property of this RedemptionSummary.
        :type redemption_code: str

        :param invoice_number:
            The value to assign to the invoice_number property of this RedemptionSummary.
        :type invoice_number: str

        :param invoice_total_amount:
            The value to assign to the invoice_total_amount property of this RedemptionSummary.
        :type invoice_total_amount: float

        :param invoice_currency:
            The value to assign to the invoice_currency property of this RedemptionSummary.
        :type invoice_currency: str

        :param redeemed_rewards:
            The value to assign to the redeemed_rewards property of this RedemptionSummary.
        :type redeemed_rewards: float

        :param base_rewards:
            The value to assign to the base_rewards property of this RedemptionSummary.
        :type base_rewards: float

        :param fx_rate:
            The value to assign to the fx_rate property of this RedemptionSummary.
        :type fx_rate: float

        :param time_invoiced:
            The value to assign to the time_invoiced property of this RedemptionSummary.
        :type time_invoiced: datetime

        """
        self.swagger_types = {
            'time_redeemed': 'datetime',
            'redemption_email': 'str',
            'redemption_code': 'str',
            'invoice_number': 'str',
            'invoice_total_amount': 'float',
            'invoice_currency': 'str',
            'redeemed_rewards': 'float',
            'base_rewards': 'float',
            'fx_rate': 'float',
            'time_invoiced': 'datetime'
        }

        self.attribute_map = {
            'time_redeemed': 'timeRedeemed',
            'redemption_email': 'redemptionEmail',
            'redemption_code': 'redemptionCode',
            'invoice_number': 'invoiceNumber',
            'invoice_total_amount': 'invoiceTotalAmount',
            'invoice_currency': 'invoiceCurrency',
            'redeemed_rewards': 'redeemedRewards',
            'base_rewards': 'baseRewards',
            'fx_rate': 'fxRate',
            'time_invoiced': 'timeInvoiced'
        }

        self._time_redeemed = None
        self._redemption_email = None
        self._redemption_code = None
        self._invoice_number = None
        self._invoice_total_amount = None
        self._invoice_currency = None
        self._redeemed_rewards = None
        self._base_rewards = None
        self._fx_rate = None
        self._time_invoiced = None

    @property
    def time_redeemed(self):
        """
        Gets the time_redeemed of this RedemptionSummary.
        It provides redeem date.


        :return: The time_redeemed of this RedemptionSummary.
        :rtype: datetime
        """
        return self._time_redeemed

    @time_redeemed.setter
    def time_redeemed(self, time_redeemed):
        """
        Sets the time_redeemed of this RedemptionSummary.
        It provides redeem date.


        :param time_redeemed: The time_redeemed of this RedemptionSummary.
        :type: datetime
        """
        self._time_redeemed = time_redeemed

    @property
    def redemption_email(self):
        """
        Gets the redemption_email of this RedemptionSummary.
        It provides the redemption email id.


        :return: The redemption_email of this RedemptionSummary.
        :rtype: str
        """
        return self._redemption_email

    @redemption_email.setter
    def redemption_email(self, redemption_email):
        """
        Sets the redemption_email of this RedemptionSummary.
        It provides the redemption email id.


        :param redemption_email: The redemption_email of this RedemptionSummary.
        :type: str
        """
        self._redemption_email = redemption_email

    @property
    def redemption_code(self):
        """
        Gets the redemption_code of this RedemptionSummary.
        The redemption code used in the Billing Center during the reward redemption process.


        :return: The redemption_code of this RedemptionSummary.
        :rtype: str
        """
        return self._redemption_code

    @redemption_code.setter
    def redemption_code(self, redemption_code):
        """
        Sets the redemption_code of this RedemptionSummary.
        The redemption code used in the Billing Center during the reward redemption process.


        :param redemption_code: The redemption_code of this RedemptionSummary.
        :type: str
        """
        self._redemption_code = redemption_code

    @property
    def invoice_number(self):
        """
        Gets the invoice_number of this RedemptionSummary.
        It provides the invoice number against the redemption.


        :return: The invoice_number of this RedemptionSummary.
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """
        Sets the invoice_number of this RedemptionSummary.
        It provides the invoice number against the redemption.


        :param invoice_number: The invoice_number of this RedemptionSummary.
        :type: str
        """
        self._invoice_number = invoice_number

    @property
    def invoice_total_amount(self):
        """
        Gets the invoice_total_amount of this RedemptionSummary.
        It provides the invoice total amount of given redemption.


        :return: The invoice_total_amount of this RedemptionSummary.
        :rtype: float
        """
        return self._invoice_total_amount

    @invoice_total_amount.setter
    def invoice_total_amount(self, invoice_total_amount):
        """
        Sets the invoice_total_amount of this RedemptionSummary.
        It provides the invoice total amount of given redemption.


        :param invoice_total_amount: The invoice_total_amount of this RedemptionSummary.
        :type: float
        """
        self._invoice_total_amount = invoice_total_amount

    @property
    def invoice_currency(self):
        """
        Gets the invoice_currency of this RedemptionSummary.
        The currency associated with invoice.


        :return: The invoice_currency of this RedemptionSummary.
        :rtype: str
        """
        return self._invoice_currency

    @invoice_currency.setter
    def invoice_currency(self, invoice_currency):
        """
        Sets the invoice_currency of this RedemptionSummary.
        The currency associated with invoice.


        :param invoice_currency: The invoice_currency of this RedemptionSummary.
        :type: str
        """
        self._invoice_currency = invoice_currency

    @property
    def redeemed_rewards(self):
        """
        Gets the redeemed_rewards of this RedemptionSummary.
        It provides the redeemed rewards in invoice currency.


        :return: The redeemed_rewards of this RedemptionSummary.
        :rtype: float
        """
        return self._redeemed_rewards

    @redeemed_rewards.setter
    def redeemed_rewards(self, redeemed_rewards):
        """
        Sets the redeemed_rewards of this RedemptionSummary.
        It provides the redeemed rewards in invoice currency.


        :param redeemed_rewards: The redeemed_rewards of this RedemptionSummary.
        :type: float
        """
        self._redeemed_rewards = redeemed_rewards

    @property
    def base_rewards(self):
        """
        Gets the base_rewards of this RedemptionSummary.
        It provides the redeemed rewards in base/subscription currency.


        :return: The base_rewards of this RedemptionSummary.
        :rtype: float
        """
        return self._base_rewards

    @base_rewards.setter
    def base_rewards(self, base_rewards):
        """
        Sets the base_rewards of this RedemptionSummary.
        It provides the redeemed rewards in base/subscription currency.


        :param base_rewards: The base_rewards of this RedemptionSummary.
        :type: float
        """
        self._base_rewards = base_rewards

    @property
    def fx_rate(self):
        """
        Gets the fx_rate of this RedemptionSummary.
        It provides the fxRate between invoice currency and subscription currency.


        :return: The fx_rate of this RedemptionSummary.
        :rtype: float
        """
        return self._fx_rate

    @fx_rate.setter
    def fx_rate(self, fx_rate):
        """
        Sets the fx_rate of this RedemptionSummary.
        It provides the fxRate between invoice currency and subscription currency.


        :param fx_rate: The fx_rate of this RedemptionSummary.
        :type: float
        """
        self._fx_rate = fx_rate

    @property
    def time_invoiced(self):
        """
        Gets the time_invoiced of this RedemptionSummary.
        It provides the invoice date.


        :return: The time_invoiced of this RedemptionSummary.
        :rtype: datetime
        """
        return self._time_invoiced

    @time_invoiced.setter
    def time_invoiced(self, time_invoiced):
        """
        Sets the time_invoiced of this RedemptionSummary.
        It provides the invoice date.


        :param time_invoiced: The time_invoiced of this RedemptionSummary.
        :type: datetime
        """
        self._time_invoiced = time_invoiced

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
