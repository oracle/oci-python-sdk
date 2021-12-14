# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .payment_detail import PaymentDetail
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OtherPaymentDetail(PaymentDetail):
    """
    Other Payment related details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OtherPaymentDetail object with values from keyword arguments. The default value of the :py:attr:`~oci.osp_gateway.models.OtherPaymentDetail.payment_method` attribute
        of this class is ``OTHER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_paid_on:
            The value to assign to the time_paid_on property of this OtherPaymentDetail.
        :type time_paid_on: datetime

        :param paid_by:
            The value to assign to the paid_by property of this OtherPaymentDetail.
        :type paid_by: str

        :param payment_method:
            The value to assign to the payment_method property of this OtherPaymentDetail.
            Allowed values for this property are: "CREDIT_CARD", "PAYPAL", "OTHER"
        :type payment_method: str

        :param amount_paid:
            The value to assign to the amount_paid property of this OtherPaymentDetail.
        :type amount_paid: float

        """
        self.swagger_types = {
            'time_paid_on': 'datetime',
            'paid_by': 'str',
            'payment_method': 'str',
            'amount_paid': 'float'
        }

        self.attribute_map = {
            'time_paid_on': 'timePaidOn',
            'paid_by': 'paidBy',
            'payment_method': 'paymentMethod',
            'amount_paid': 'amountPaid'
        }

        self._time_paid_on = None
        self._paid_by = None
        self._payment_method = None
        self._amount_paid = None
        self._payment_method = 'OTHER'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
