# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscribedServiceSummary(object):
    """
    Subscribed Service summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubscribedServiceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SubscribedServiceSummary.
        :type id: str

        :param product:
            The value to assign to the product property of this SubscribedServiceSummary.
        :type product: oci.osub_subscription.models.SubscriptionProduct

        :param quantity:
            The value to assign to the quantity property of this SubscribedServiceSummary.
        :type quantity: str

        :param status:
            The value to assign to the status property of this SubscribedServiceSummary.
        :type status: str

        :param operation_type:
            The value to assign to the operation_type property of this SubscribedServiceSummary.
        :type operation_type: str

        :param net_unit_price:
            The value to assign to the net_unit_price property of this SubscribedServiceSummary.
        :type net_unit_price: str

        :param funded_allocation_value:
            The value to assign to the funded_allocation_value property of this SubscribedServiceSummary.
        :type funded_allocation_value: str

        :param partner_transaction_type:
            The value to assign to the partner_transaction_type property of this SubscribedServiceSummary.
        :type partner_transaction_type: str

        :param term_value:
            The value to assign to the term_value property of this SubscribedServiceSummary.
        :type term_value: int

        :param term_value_uom:
            The value to assign to the term_value_uom property of this SubscribedServiceSummary.
        :type term_value_uom: str

        :param booking_opty_number:
            The value to assign to the booking_opty_number property of this SubscribedServiceSummary.
        :type booking_opty_number: str

        :param total_value:
            The value to assign to the total_value property of this SubscribedServiceSummary.
        :type total_value: str

        :param order_number:
            The value to assign to the order_number property of this SubscribedServiceSummary.
        :type order_number: int

        :param data_center_region:
            The value to assign to the data_center_region property of this SubscribedServiceSummary.
        :type data_center_region: str

        :param pricing_model:
            The value to assign to the pricing_model property of this SubscribedServiceSummary.
        :type pricing_model: str

        :param program_type:
            The value to assign to the program_type property of this SubscribedServiceSummary.
        :type program_type: str

        :param promo_type:
            The value to assign to the promo_type property of this SubscribedServiceSummary.
        :type promo_type: str

        :param csi:
            The value to assign to the csi property of this SubscribedServiceSummary.
        :type csi: int

        :param is_intent_to_pay:
            The value to assign to the is_intent_to_pay property of this SubscribedServiceSummary.
        :type is_intent_to_pay: bool

        :param time_start:
            The value to assign to the time_start property of this SubscribedServiceSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this SubscribedServiceSummary.
        :type time_end: datetime

        :param commitment_services:
            The value to assign to the commitment_services property of this SubscribedServiceSummary.
        :type commitment_services: list[oci.osub_subscription.models.Commitment]

        """
        self.swagger_types = {
            'id': 'str',
            'product': 'SubscriptionProduct',
            'quantity': 'str',
            'status': 'str',
            'operation_type': 'str',
            'net_unit_price': 'str',
            'funded_allocation_value': 'str',
            'partner_transaction_type': 'str',
            'term_value': 'int',
            'term_value_uom': 'str',
            'booking_opty_number': 'str',
            'total_value': 'str',
            'order_number': 'int',
            'data_center_region': 'str',
            'pricing_model': 'str',
            'program_type': 'str',
            'promo_type': 'str',
            'csi': 'int',
            'is_intent_to_pay': 'bool',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'commitment_services': 'list[Commitment]'
        }

        self.attribute_map = {
            'id': 'id',
            'product': 'product',
            'quantity': 'quantity',
            'status': 'status',
            'operation_type': 'operationType',
            'net_unit_price': 'netUnitPrice',
            'funded_allocation_value': 'fundedAllocationValue',
            'partner_transaction_type': 'partnerTransactionType',
            'term_value': 'termValue',
            'term_value_uom': 'termValueUOM',
            'booking_opty_number': 'bookingOptyNumber',
            'total_value': 'totalValue',
            'order_number': 'orderNumber',
            'data_center_region': 'dataCenterRegion',
            'pricing_model': 'pricingModel',
            'program_type': 'programType',
            'promo_type': 'promoType',
            'csi': 'csi',
            'is_intent_to_pay': 'isIntentToPay',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'commitment_services': 'commitmentServices'
        }

        self._id = None
        self._product = None
        self._quantity = None
        self._status = None
        self._operation_type = None
        self._net_unit_price = None
        self._funded_allocation_value = None
        self._partner_transaction_type = None
        self._term_value = None
        self._term_value_uom = None
        self._booking_opty_number = None
        self._total_value = None
        self._order_number = None
        self._data_center_region = None
        self._pricing_model = None
        self._program_type = None
        self._promo_type = None
        self._csi = None
        self._is_intent_to_pay = None
        self._time_start = None
        self._time_end = None
        self._commitment_services = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SubscribedServiceSummary.
        SPM internal Subscribed Service ID


        :return: The id of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscribedServiceSummary.
        SPM internal Subscribed Service ID


        :param id: The id of this SubscribedServiceSummary.
        :type: str
        """
        self._id = id

    @property
    def product(self):
        """
        Gets the product of this SubscribedServiceSummary.

        :return: The product of this SubscribedServiceSummary.
        :rtype: oci.osub_subscription.models.SubscriptionProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this SubscribedServiceSummary.

        :param product: The product of this SubscribedServiceSummary.
        :type: oci.osub_subscription.models.SubscriptionProduct
        """
        self._product = product

    @property
    def quantity(self):
        """
        Gets the quantity of this SubscribedServiceSummary.
        Subscribed service quantity


        :return: The quantity of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this SubscribedServiceSummary.
        Subscribed service quantity


        :param quantity: The quantity of this SubscribedServiceSummary.
        :type: str
        """
        self._quantity = quantity

    @property
    def status(self):
        """
        Gets the status of this SubscribedServiceSummary.
        Subscribed service status


        :return: The status of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SubscribedServiceSummary.
        Subscribed service status


        :param status: The status of this SubscribedServiceSummary.
        :type: str
        """
        self._status = status

    @property
    def operation_type(self):
        """
        Gets the operation_type of this SubscribedServiceSummary.
        Subscribed service operation type


        :return: The operation_type of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this SubscribedServiceSummary.
        Subscribed service operation type


        :param operation_type: The operation_type of this SubscribedServiceSummary.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def net_unit_price(self):
        """
        Gets the net_unit_price of this SubscribedServiceSummary.
        Subscribed service net unit price


        :return: The net_unit_price of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this SubscribedServiceSummary.
        Subscribed service net unit price


        :param net_unit_price: The net_unit_price of this SubscribedServiceSummary.
        :type: str
        """
        self._net_unit_price = net_unit_price

    @property
    def funded_allocation_value(self):
        """
        Gets the funded_allocation_value of this SubscribedServiceSummary.
        Funded Allocation line value
        example: 12000.00


        :return: The funded_allocation_value of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._funded_allocation_value

    @funded_allocation_value.setter
    def funded_allocation_value(self, funded_allocation_value):
        """
        Sets the funded_allocation_value of this SubscribedServiceSummary.
        Funded Allocation line value
        example: 12000.00


        :param funded_allocation_value: The funded_allocation_value of this SubscribedServiceSummary.
        :type: str
        """
        self._funded_allocation_value = funded_allocation_value

    @property
    def partner_transaction_type(self):
        """
        Gets the partner_transaction_type of this SubscribedServiceSummary.
        This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ


        :return: The partner_transaction_type of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._partner_transaction_type

    @partner_transaction_type.setter
    def partner_transaction_type(self, partner_transaction_type):
        """
        Sets the partner_transaction_type of this SubscribedServiceSummary.
        This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ


        :param partner_transaction_type: The partner_transaction_type of this SubscribedServiceSummary.
        :type: str
        """
        self._partner_transaction_type = partner_transaction_type

    @property
    def term_value(self):
        """
        Gets the term_value of this SubscribedServiceSummary.
        Term value in Months


        :return: The term_value of this SubscribedServiceSummary.
        :rtype: int
        """
        return self._term_value

    @term_value.setter
    def term_value(self, term_value):
        """
        Sets the term_value of this SubscribedServiceSummary.
        Term value in Months


        :param term_value: The term_value of this SubscribedServiceSummary.
        :type: int
        """
        self._term_value = term_value

    @property
    def term_value_uom(self):
        """
        Gets the term_value_uom of this SubscribedServiceSummary.
        Term value UOM


        :return: The term_value_uom of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._term_value_uom

    @term_value_uom.setter
    def term_value_uom(self, term_value_uom):
        """
        Sets the term_value_uom of this SubscribedServiceSummary.
        Term value UOM


        :param term_value_uom: The term_value_uom of this SubscribedServiceSummary.
        :type: str
        """
        self._term_value_uom = term_value_uom

    @property
    def booking_opty_number(self):
        """
        Gets the booking_opty_number of this SubscribedServiceSummary.
        Booking Opportunity Number of Subscribed Service


        :return: The booking_opty_number of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._booking_opty_number

    @booking_opty_number.setter
    def booking_opty_number(self, booking_opty_number):
        """
        Sets the booking_opty_number of this SubscribedServiceSummary.
        Booking Opportunity Number of Subscribed Service


        :param booking_opty_number: The booking_opty_number of this SubscribedServiceSummary.
        :type: str
        """
        self._booking_opty_number = booking_opty_number

    @property
    def total_value(self):
        """
        Gets the total_value of this SubscribedServiceSummary.
        Subscribed service total value


        :return: The total_value of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._total_value

    @total_value.setter
    def total_value(self, total_value):
        """
        Sets the total_value of this SubscribedServiceSummary.
        Subscribed service total value


        :param total_value: The total_value of this SubscribedServiceSummary.
        :type: str
        """
        self._total_value = total_value

    @property
    def order_number(self):
        """
        Gets the order_number of this SubscribedServiceSummary.
        Sales Order Number associated to the subscribed service


        :return: The order_number of this SubscribedServiceSummary.
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """
        Sets the order_number of this SubscribedServiceSummary.
        Sales Order Number associated to the subscribed service


        :param order_number: The order_number of this SubscribedServiceSummary.
        :type: int
        """
        self._order_number = order_number

    @property
    def data_center_region(self):
        """
        Gets the data_center_region of this SubscribedServiceSummary.
        Subscribed service data center region


        :return: The data_center_region of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._data_center_region

    @data_center_region.setter
    def data_center_region(self, data_center_region):
        """
        Sets the data_center_region of this SubscribedServiceSummary.
        Subscribed service data center region


        :param data_center_region: The data_center_region of this SubscribedServiceSummary.
        :type: str
        """
        self._data_center_region = data_center_region

    @property
    def pricing_model(self):
        """
        Gets the pricing_model of this SubscribedServiceSummary.
        Subscribed service pricing model


        :return: The pricing_model of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._pricing_model

    @pricing_model.setter
    def pricing_model(self, pricing_model):
        """
        Sets the pricing_model of this SubscribedServiceSummary.
        Subscribed service pricing model


        :param pricing_model: The pricing_model of this SubscribedServiceSummary.
        :type: str
        """
        self._pricing_model = pricing_model

    @property
    def program_type(self):
        """
        Gets the program_type of this SubscribedServiceSummary.
        Subscribed service program type


        :return: The program_type of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._program_type

    @program_type.setter
    def program_type(self, program_type):
        """
        Sets the program_type of this SubscribedServiceSummary.
        Subscribed service program type


        :param program_type: The program_type of this SubscribedServiceSummary.
        :type: str
        """
        self._program_type = program_type

    @property
    def promo_type(self):
        """
        Gets the promo_type of this SubscribedServiceSummary.
        Subscribed service promotion type


        :return: The promo_type of this SubscribedServiceSummary.
        :rtype: str
        """
        return self._promo_type

    @promo_type.setter
    def promo_type(self, promo_type):
        """
        Sets the promo_type of this SubscribedServiceSummary.
        Subscribed service promotion type


        :param promo_type: The promo_type of this SubscribedServiceSummary.
        :type: str
        """
        self._promo_type = promo_type

    @property
    def csi(self):
        """
        Gets the csi of this SubscribedServiceSummary.
        Subscribed service CSI number


        :return: The csi of this SubscribedServiceSummary.
        :rtype: int
        """
        return self._csi

    @csi.setter
    def csi(self, csi):
        """
        Sets the csi of this SubscribedServiceSummary.
        Subscribed service CSI number


        :param csi: The csi of this SubscribedServiceSummary.
        :type: int
        """
        self._csi = csi

    @property
    def is_intent_to_pay(self):
        """
        Gets the is_intent_to_pay of this SubscribedServiceSummary.
        Subscribed service intent to pay flag


        :return: The is_intent_to_pay of this SubscribedServiceSummary.
        :rtype: bool
        """
        return self._is_intent_to_pay

    @is_intent_to_pay.setter
    def is_intent_to_pay(self, is_intent_to_pay):
        """
        Sets the is_intent_to_pay of this SubscribedServiceSummary.
        Subscribed service intent to pay flag


        :param is_intent_to_pay: The is_intent_to_pay of this SubscribedServiceSummary.
        :type: bool
        """
        self._is_intent_to_pay = is_intent_to_pay

    @property
    def time_start(self):
        """
        Gets the time_start of this SubscribedServiceSummary.
        Subscribed service start date


        :return: The time_start of this SubscribedServiceSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this SubscribedServiceSummary.
        Subscribed service start date


        :param time_start: The time_start of this SubscribedServiceSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this SubscribedServiceSummary.
        Subscribed service end date


        :return: The time_end of this SubscribedServiceSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this SubscribedServiceSummary.
        Subscribed service end date


        :param time_end: The time_end of this SubscribedServiceSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def commitment_services(self):
        """
        Gets the commitment_services of this SubscribedServiceSummary.
        List of Commitment services of a line


        :return: The commitment_services of this SubscribedServiceSummary.
        :rtype: list[oci.osub_subscription.models.Commitment]
        """
        return self._commitment_services

    @commitment_services.setter
    def commitment_services(self, commitment_services):
        """
        Sets the commitment_services of this SubscribedServiceSummary.
        List of Commitment services of a line


        :param commitment_services: The commitment_services of this SubscribedServiceSummary.
        :type: list[oci.osub_subscription.models.Commitment]
        """
        self._commitment_services = commitment_services

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
