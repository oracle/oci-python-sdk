# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .payment_option import PaymentOption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreditCardPaymentOption(PaymentOption):
    """
    Credit card Payment related details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreditCardPaymentOption object with values from keyword arguments. The default value of the :py:attr:`~oci.osp_gateway.models.CreditCardPaymentOption.payment_method` attribute
        of this class is ``CREDIT_CARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wallet_instrument_id:
            The value to assign to the wallet_instrument_id property of this CreditCardPaymentOption.
        :type wallet_instrument_id: str

        :param wallet_transaction_id:
            The value to assign to the wallet_transaction_id property of this CreditCardPaymentOption.
        :type wallet_transaction_id: str

        :param payment_method:
            The value to assign to the payment_method property of this CreditCardPaymentOption.
            Allowed values for this property are: "CREDIT_CARD", "PAYPAL"
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
        self._payment_method = 'CREDIT_CARD'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
