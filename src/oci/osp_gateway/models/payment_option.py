# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PaymentOption(object):
    """
    Payment option of a subscription.
    """

    #: A constant which can be used with the payment_method property of a PaymentOption.
    #: This constant has a value of "CREDIT_CARD"
    PAYMENT_METHOD_CREDIT_CARD = "CREDIT_CARD"

    #: A constant which can be used with the payment_method property of a PaymentOption.
    #: This constant has a value of "PAYPAL"
    PAYMENT_METHOD_PAYPAL = "PAYPAL"

    def __init__(self, **kwargs):
        """
        Initializes a new PaymentOption object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.osp_gateway.models.CreditCardPaymentOption`
        * :class:`~oci.osp_gateway.models.PaypalPaymentOption`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wallet_instrument_id:
            The value to assign to the wallet_instrument_id property of this PaymentOption.
        :type wallet_instrument_id: str

        :param wallet_transaction_id:
            The value to assign to the wallet_transaction_id property of this PaymentOption.
        :type wallet_transaction_id: str

        :param payment_method:
            The value to assign to the payment_method property of this PaymentOption.
            Allowed values for this property are: "CREDIT_CARD", "PAYPAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type payment_method: str

        """
        self.swagger_types = {
            'wallet_instrument_id': 'str',
            'wallet_transaction_id': 'str',
            'payment_method': 'str'
        }

        self.attribute_map = {
            'wallet_instrument_id': 'walletInstrumentId',
            'wallet_transaction_id': 'walletTransactionId',
            'payment_method': 'paymentMethod'
        }

        self._wallet_instrument_id = None
        self._wallet_transaction_id = None
        self._payment_method = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['paymentMethod']

        if type == 'CREDIT_CARD':
            return 'CreditCardPaymentOption'

        if type == 'PAYPAL':
            return 'PaypalPaymentOption'
        else:
            return 'PaymentOption'

    @property
    def wallet_instrument_id(self):
        """
        Gets the wallet_instrument_id of this PaymentOption.
        Wallet instrument internal id.


        :return: The wallet_instrument_id of this PaymentOption.
        :rtype: str
        """
        return self._wallet_instrument_id

    @wallet_instrument_id.setter
    def wallet_instrument_id(self, wallet_instrument_id):
        """
        Sets the wallet_instrument_id of this PaymentOption.
        Wallet instrument internal id.


        :param wallet_instrument_id: The wallet_instrument_id of this PaymentOption.
        :type: str
        """
        self._wallet_instrument_id = wallet_instrument_id

    @property
    def wallet_transaction_id(self):
        """
        Gets the wallet_transaction_id of this PaymentOption.
        Wallet transaction id.


        :return: The wallet_transaction_id of this PaymentOption.
        :rtype: str
        """
        return self._wallet_transaction_id

    @wallet_transaction_id.setter
    def wallet_transaction_id(self, wallet_transaction_id):
        """
        Sets the wallet_transaction_id of this PaymentOption.
        Wallet transaction id.


        :param wallet_transaction_id: The wallet_transaction_id of this PaymentOption.
        :type: str
        """
        self._wallet_transaction_id = wallet_transaction_id

    @property
    def payment_method(self):
        """
        **[Required]** Gets the payment_method of this PaymentOption.
        Payment method

        Allowed values for this property are: "CREDIT_CARD", "PAYPAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The payment_method of this PaymentOption.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this PaymentOption.
        Payment method


        :param payment_method: The payment_method of this PaymentOption.
        :type: str
        """
        allowed_values = ["CREDIT_CARD", "PAYPAL"]
        if not value_allowed_none_or_none_sentinel(payment_method, allowed_values):
            payment_method = 'UNKNOWN_ENUM_VALUE'
        self._payment_method = payment_method

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
