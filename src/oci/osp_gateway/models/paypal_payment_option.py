# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .payment_option import PaymentOption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PaypalPaymentOption(PaymentOption):
    """
    PayPal Payment related details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PaypalPaymentOption object with values from keyword arguments. The default value of the :py:attr:`~oci.osp_gateway.models.PaypalPaymentOption.payment_method` attribute
        of this class is ``PAYPAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wallet_instrument_id:
            The value to assign to the wallet_instrument_id property of this PaypalPaymentOption.
        :type wallet_instrument_id: str

        :param wallet_transaction_id:
            The value to assign to the wallet_transaction_id property of this PaypalPaymentOption.
        :type wallet_transaction_id: str

        :param payment_method:
            The value to assign to the payment_method property of this PaypalPaymentOption.
            Allowed values for this property are: "CREDIT_CARD", "PAYPAL"
        :type payment_method: str

        :param email_address:
            The value to assign to the email_address property of this PaypalPaymentOption.
        :type email_address: str

        :param first_name:
            The value to assign to the first_name property of this PaypalPaymentOption.
        :type first_name: str

        :param last_name:
            The value to assign to the last_name property of this PaypalPaymentOption.
        :type last_name: str

        :param ext_billing_agreement_id:
            The value to assign to the ext_billing_agreement_id property of this PaypalPaymentOption.
        :type ext_billing_agreement_id: str

        """
        self.swagger_types = {
            'wallet_instrument_id': 'str',
            'wallet_transaction_id': 'str',
            'payment_method': 'str',
            'email_address': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'ext_billing_agreement_id': 'str'
        }

        self.attribute_map = {
            'wallet_instrument_id': 'walletInstrumentId',
            'wallet_transaction_id': 'walletTransactionId',
            'payment_method': 'paymentMethod',
            'email_address': 'emailAddress',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'ext_billing_agreement_id': 'extBillingAgreementId'
        }

        self._wallet_instrument_id = None
        self._wallet_transaction_id = None
        self._payment_method = None
        self._email_address = None
        self._first_name = None
        self._last_name = None
        self._ext_billing_agreement_id = None
        self._payment_method = 'PAYPAL'

    @property
    def email_address(self):
        """
        Gets the email_address of this PaypalPaymentOption.
        The email address of the paypal user.


        :return: The email_address of this PaypalPaymentOption.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this PaypalPaymentOption.
        The email address of the paypal user.


        :param email_address: The email_address of this PaypalPaymentOption.
        :type: str
        """
        self._email_address = email_address

    @property
    def first_name(self):
        """
        Gets the first_name of this PaypalPaymentOption.
        First name of the paypal user.


        :return: The first_name of this PaypalPaymentOption.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this PaypalPaymentOption.
        First name of the paypal user.


        :param first_name: The first_name of this PaypalPaymentOption.
        :type: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this PaypalPaymentOption.
        Last name of the paypal user.


        :return: The last_name of this PaypalPaymentOption.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this PaypalPaymentOption.
        Last name of the paypal user.


        :param last_name: The last_name of this PaypalPaymentOption.
        :type: str
        """
        self._last_name = last_name

    @property
    def ext_billing_agreement_id(self):
        """
        Gets the ext_billing_agreement_id of this PaypalPaymentOption.
        Agreement id for the paypal account.


        :return: The ext_billing_agreement_id of this PaypalPaymentOption.
        :rtype: str
        """
        return self._ext_billing_agreement_id

    @ext_billing_agreement_id.setter
    def ext_billing_agreement_id(self, ext_billing_agreement_id):
        """
        Sets the ext_billing_agreement_id of this PaypalPaymentOption.
        Agreement id for the paypal account.


        :param ext_billing_agreement_id: The ext_billing_agreement_id of this PaypalPaymentOption.
        :type: str
        """
        self._ext_billing_agreement_id = ext_billing_agreement_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
