# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BillingScheduleSummary(object):
    """
    Billing schedule details related to Subscription Id
    """

    #: A constant which can be used with the invoice_status property of a BillingScheduleSummary.
    #: This constant has a value of "INVOICED"
    INVOICE_STATUS_INVOICED = "INVOICED"

    #: A constant which can be used with the invoice_status property of a BillingScheduleSummary.
    #: This constant has a value of "NOT_INVOICED"
    INVOICE_STATUS_NOT_INVOICED = "NOT_INVOICED"

    def __init__(self, **kwargs):
        """
        Initializes a new BillingScheduleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subscribed_service_id:
            The value to assign to the subscribed_service_id property of this BillingScheduleSummary.
        :type subscribed_service_id: str

        :param time_start:
            The value to assign to the time_start property of this BillingScheduleSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this BillingScheduleSummary.
        :type time_end: datetime

        :param time_invoicing:
            The value to assign to the time_invoicing property of this BillingScheduleSummary.
        :type time_invoicing: datetime

        :param invoice_status:
            The value to assign to the invoice_status property of this BillingScheduleSummary.
            Allowed values for this property are: "INVOICED", "NOT_INVOICED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type invoice_status: str

        :param quantity:
            The value to assign to the quantity property of this BillingScheduleSummary.
        :type quantity: str

        :param net_unit_price:
            The value to assign to the net_unit_price property of this BillingScheduleSummary.
        :type net_unit_price: str

        :param amount:
            The value to assign to the amount property of this BillingScheduleSummary.
        :type amount: str

        :param billing_frequency:
            The value to assign to the billing_frequency property of this BillingScheduleSummary.
        :type billing_frequency: str

        :param ar_invoice_number:
            The value to assign to the ar_invoice_number property of this BillingScheduleSummary.
        :type ar_invoice_number: str

        :param ar_customer_transaction_id:
            The value to assign to the ar_customer_transaction_id property of this BillingScheduleSummary.
        :type ar_customer_transaction_id: str

        :param order_number:
            The value to assign to the order_number property of this BillingScheduleSummary.
        :type order_number: str

        :param product:
            The value to assign to the product property of this BillingScheduleSummary.
        :type product: oci.onesubscription.models.BillingScheduleProduct

        """
        self.swagger_types = {
            'subscribed_service_id': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_invoicing': 'datetime',
            'invoice_status': 'str',
            'quantity': 'str',
            'net_unit_price': 'str',
            'amount': 'str',
            'billing_frequency': 'str',
            'ar_invoice_number': 'str',
            'ar_customer_transaction_id': 'str',
            'order_number': 'str',
            'product': 'BillingScheduleProduct'
        }

        self.attribute_map = {
            'subscribed_service_id': 'subscribedServiceId',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_invoicing': 'timeInvoicing',
            'invoice_status': 'invoiceStatus',
            'quantity': 'quantity',
            'net_unit_price': 'netUnitPrice',
            'amount': 'amount',
            'billing_frequency': 'billingFrequency',
            'ar_invoice_number': 'arInvoiceNumber',
            'ar_customer_transaction_id': 'arCustomerTransactionId',
            'order_number': 'orderNumber',
            'product': 'product'
        }

        self._subscribed_service_id = None
        self._time_start = None
        self._time_end = None
        self._time_invoicing = None
        self._invoice_status = None
        self._quantity = None
        self._net_unit_price = None
        self._amount = None
        self._billing_frequency = None
        self._ar_invoice_number = None
        self._ar_customer_transaction_id = None
        self._order_number = None
        self._product = None

    @property
    def subscribed_service_id(self):
        """
        Gets the subscribed_service_id of this BillingScheduleSummary.
        SPM internal Subscribed Service ID


        :return: The subscribed_service_id of this BillingScheduleSummary.
        :rtype: str
        """
        return self._subscribed_service_id

    @subscribed_service_id.setter
    def subscribed_service_id(self, subscribed_service_id):
        """
        Sets the subscribed_service_id of this BillingScheduleSummary.
        SPM internal Subscribed Service ID


        :param subscribed_service_id: The subscribed_service_id of this BillingScheduleSummary.
        :type: str
        """
        self._subscribed_service_id = subscribed_service_id

    @property
    def time_start(self):
        """
        Gets the time_start of this BillingScheduleSummary.
        Billing schedule start date


        :return: The time_start of this BillingScheduleSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this BillingScheduleSummary.
        Billing schedule start date


        :param time_start: The time_start of this BillingScheduleSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this BillingScheduleSummary.
        Billing schedule end date


        :return: The time_end of this BillingScheduleSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this BillingScheduleSummary.
        Billing schedule end date


        :param time_end: The time_end of this BillingScheduleSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_invoicing(self):
        """
        Gets the time_invoicing of this BillingScheduleSummary.
        Billing schedule invoicing date


        :return: The time_invoicing of this BillingScheduleSummary.
        :rtype: datetime
        """
        return self._time_invoicing

    @time_invoicing.setter
    def time_invoicing(self, time_invoicing):
        """
        Sets the time_invoicing of this BillingScheduleSummary.
        Billing schedule invoicing date


        :param time_invoicing: The time_invoicing of this BillingScheduleSummary.
        :type: datetime
        """
        self._time_invoicing = time_invoicing

    @property
    def invoice_status(self):
        """
        Gets the invoice_status of this BillingScheduleSummary.
        Billing schedule invoice status

        Allowed values for this property are: "INVOICED", "NOT_INVOICED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The invoice_status of this BillingScheduleSummary.
        :rtype: str
        """
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, invoice_status):
        """
        Sets the invoice_status of this BillingScheduleSummary.
        Billing schedule invoice status


        :param invoice_status: The invoice_status of this BillingScheduleSummary.
        :type: str
        """
        allowed_values = ["INVOICED", "NOT_INVOICED"]
        if not value_allowed_none_or_none_sentinel(invoice_status, allowed_values):
            invoice_status = 'UNKNOWN_ENUM_VALUE'
        self._invoice_status = invoice_status

    @property
    def quantity(self):
        """
        Gets the quantity of this BillingScheduleSummary.
        Billing schedule quantity


        :return: The quantity of this BillingScheduleSummary.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this BillingScheduleSummary.
        Billing schedule quantity


        :param quantity: The quantity of this BillingScheduleSummary.
        :type: str
        """
        self._quantity = quantity

    @property
    def net_unit_price(self):
        """
        Gets the net_unit_price of this BillingScheduleSummary.
        Billing schedule net unit price


        :return: The net_unit_price of this BillingScheduleSummary.
        :rtype: str
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this BillingScheduleSummary.
        Billing schedule net unit price


        :param net_unit_price: The net_unit_price of this BillingScheduleSummary.
        :type: str
        """
        self._net_unit_price = net_unit_price

    @property
    def amount(self):
        """
        Gets the amount of this BillingScheduleSummary.
        Billing schedule line net amount


        :return: The amount of this BillingScheduleSummary.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this BillingScheduleSummary.
        Billing schedule line net amount


        :param amount: The amount of this BillingScheduleSummary.
        :type: str
        """
        self._amount = amount

    @property
    def billing_frequency(self):
        """
        Gets the billing_frequency of this BillingScheduleSummary.
        Billing frequency


        :return: The billing_frequency of this BillingScheduleSummary.
        :rtype: str
        """
        return self._billing_frequency

    @billing_frequency.setter
    def billing_frequency(self, billing_frequency):
        """
        Sets the billing_frequency of this BillingScheduleSummary.
        Billing frequency


        :param billing_frequency: The billing_frequency of this BillingScheduleSummary.
        :type: str
        """
        self._billing_frequency = billing_frequency

    @property
    def ar_invoice_number(self):
        """
        Gets the ar_invoice_number of this BillingScheduleSummary.
        Indicates the associated AR Invoice Number


        :return: The ar_invoice_number of this BillingScheduleSummary.
        :rtype: str
        """
        return self._ar_invoice_number

    @ar_invoice_number.setter
    def ar_invoice_number(self, ar_invoice_number):
        """
        Sets the ar_invoice_number of this BillingScheduleSummary.
        Indicates the associated AR Invoice Number


        :param ar_invoice_number: The ar_invoice_number of this BillingScheduleSummary.
        :type: str
        """
        self._ar_invoice_number = ar_invoice_number

    @property
    def ar_customer_transaction_id(self):
        """
        Gets the ar_customer_transaction_id of this BillingScheduleSummary.
        Indicates the associated AR Customer transaction id a unique identifier existing on AR.


        :return: The ar_customer_transaction_id of this BillingScheduleSummary.
        :rtype: str
        """
        return self._ar_customer_transaction_id

    @ar_customer_transaction_id.setter
    def ar_customer_transaction_id(self, ar_customer_transaction_id):
        """
        Sets the ar_customer_transaction_id of this BillingScheduleSummary.
        Indicates the associated AR Customer transaction id a unique identifier existing on AR.


        :param ar_customer_transaction_id: The ar_customer_transaction_id of this BillingScheduleSummary.
        :type: str
        """
        self._ar_customer_transaction_id = ar_customer_transaction_id

    @property
    def order_number(self):
        """
        Gets the order_number of this BillingScheduleSummary.
        Order number associated with the Subscribed Service


        :return: The order_number of this BillingScheduleSummary.
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """
        Sets the order_number of this BillingScheduleSummary.
        Order number associated with the Subscribed Service


        :param order_number: The order_number of this BillingScheduleSummary.
        :type: str
        """
        self._order_number = order_number

    @property
    def product(self):
        """
        Gets the product of this BillingScheduleSummary.

        :return: The product of this BillingScheduleSummary.
        :rtype: oci.onesubscription.models.BillingScheduleProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this BillingScheduleSummary.

        :param product: The product of this BillingScheduleSummary.
        :type: oci.onesubscription.models.BillingScheduleProduct
        """
        self._product = product

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
