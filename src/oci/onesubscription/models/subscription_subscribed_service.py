# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscriptionSubscribedService(object):
    """
    Subscribed Service summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubscriptionSubscribedService object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SubscriptionSubscribedService.
        :type id: str

        :param product:
            The value to assign to the product property of this SubscriptionSubscribedService.
        :type product: oci.onesubscription.models.SubscriptionProduct

        :param quantity:
            The value to assign to the quantity property of this SubscriptionSubscribedService.
        :type quantity: str

        :param status:
            The value to assign to the status property of this SubscriptionSubscribedService.
        :type status: str

        :param operation_type:
            The value to assign to the operation_type property of this SubscriptionSubscribedService.
        :type operation_type: str

        :param net_unit_price:
            The value to assign to the net_unit_price property of this SubscriptionSubscribedService.
        :type net_unit_price: str

        :param used_amount:
            The value to assign to the used_amount property of this SubscriptionSubscribedService.
        :type used_amount: str

        :param available_amount:
            The value to assign to the available_amount property of this SubscriptionSubscribedService.
        :type available_amount: str

        :param funded_allocation_value:
            The value to assign to the funded_allocation_value property of this SubscriptionSubscribedService.
        :type funded_allocation_value: str

        :param partner_transaction_type:
            The value to assign to the partner_transaction_type property of this SubscriptionSubscribedService.
        :type partner_transaction_type: str

        :param term_value:
            The value to assign to the term_value property of this SubscriptionSubscribedService.
        :type term_value: int

        :param term_value_uom:
            The value to assign to the term_value_uom property of this SubscriptionSubscribedService.
        :type term_value_uom: str

        :param booking_opty_number:
            The value to assign to the booking_opty_number property of this SubscriptionSubscribedService.
        :type booking_opty_number: str

        :param total_value:
            The value to assign to the total_value property of this SubscriptionSubscribedService.
        :type total_value: str

        :param original_promo_amount:
            The value to assign to the original_promo_amount property of this SubscriptionSubscribedService.
        :type original_promo_amount: str

        :param order_number:
            The value to assign to the order_number property of this SubscriptionSubscribedService.
        :type order_number: int

        :param data_center_region:
            The value to assign to the data_center_region property of this SubscriptionSubscribedService.
        :type data_center_region: str

        :param pricing_model:
            The value to assign to the pricing_model property of this SubscriptionSubscribedService.
        :type pricing_model: str

        :param program_type:
            The value to assign to the program_type property of this SubscriptionSubscribedService.
        :type program_type: str

        :param promo_type:
            The value to assign to the promo_type property of this SubscriptionSubscribedService.
        :type promo_type: str

        :param csi:
            The value to assign to the csi property of this SubscriptionSubscribedService.
        :type csi: int

        :param is_intent_to_pay:
            The value to assign to the is_intent_to_pay property of this SubscriptionSubscribedService.
        :type is_intent_to_pay: bool

        :param time_start:
            The value to assign to the time_start property of this SubscriptionSubscribedService.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this SubscriptionSubscribedService.
        :type time_end: datetime

        :param commitment_services:
            The value to assign to the commitment_services property of this SubscriptionSubscribedService.
        :type commitment_services: list[oci.onesubscription.models.CommitmentService]

        """
        self.swagger_types = {
            'id': 'str',
            'product': 'SubscriptionProduct',
            'quantity': 'str',
            'status': 'str',
            'operation_type': 'str',
            'net_unit_price': 'str',
            'used_amount': 'str',
            'available_amount': 'str',
            'funded_allocation_value': 'str',
            'partner_transaction_type': 'str',
            'term_value': 'int',
            'term_value_uom': 'str',
            'booking_opty_number': 'str',
            'total_value': 'str',
            'original_promo_amount': 'str',
            'order_number': 'int',
            'data_center_region': 'str',
            'pricing_model': 'str',
            'program_type': 'str',
            'promo_type': 'str',
            'csi': 'int',
            'is_intent_to_pay': 'bool',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'commitment_services': 'list[CommitmentService]'
        }

        self.attribute_map = {
            'id': 'id',
            'product': 'product',
            'quantity': 'quantity',
            'status': 'status',
            'operation_type': 'operationType',
            'net_unit_price': 'netUnitPrice',
            'used_amount': 'usedAmount',
            'available_amount': 'availableAmount',
            'funded_allocation_value': 'fundedAllocationValue',
            'partner_transaction_type': 'partnerTransactionType',
            'term_value': 'termValue',
            'term_value_uom': 'termValueUom',
            'booking_opty_number': 'bookingOptyNumber',
            'total_value': 'totalValue',
            'original_promo_amount': 'originalPromoAmount',
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
        self._used_amount = None
        self._available_amount = None
        self._funded_allocation_value = None
        self._partner_transaction_type = None
        self._term_value = None
        self._term_value_uom = None
        self._booking_opty_number = None
        self._total_value = None
        self._original_promo_amount = None
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
        **[Required]** Gets the id of this SubscriptionSubscribedService.
        SPM internal Subscribed Service ID


        :return: The id of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscriptionSubscribedService.
        SPM internal Subscribed Service ID


        :param id: The id of this SubscriptionSubscribedService.
        :type: str
        """
        self._id = id

    @property
    def product(self):
        """
        Gets the product of this SubscriptionSubscribedService.

        :return: The product of this SubscriptionSubscribedService.
        :rtype: oci.onesubscription.models.SubscriptionProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this SubscriptionSubscribedService.

        :param product: The product of this SubscriptionSubscribedService.
        :type: oci.onesubscription.models.SubscriptionProduct
        """
        self._product = product

    @property
    def quantity(self):
        """
        Gets the quantity of this SubscriptionSubscribedService.
        Subscribed service quantity


        :return: The quantity of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this SubscriptionSubscribedService.
        Subscribed service quantity


        :param quantity: The quantity of this SubscriptionSubscribedService.
        :type: str
        """
        self._quantity = quantity

    @property
    def status(self):
        """
        Gets the status of this SubscriptionSubscribedService.
        Subscribed service status


        :return: The status of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SubscriptionSubscribedService.
        Subscribed service status


        :param status: The status of this SubscriptionSubscribedService.
        :type: str
        """
        self._status = status

    @property
    def operation_type(self):
        """
        Gets the operation_type of this SubscriptionSubscribedService.
        Subscribed service operation type


        :return: The operation_type of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this SubscriptionSubscribedService.
        Subscribed service operation type


        :param operation_type: The operation_type of this SubscriptionSubscribedService.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def net_unit_price(self):
        """
        Gets the net_unit_price of this SubscriptionSubscribedService.
        Subscribed service net unit price


        :return: The net_unit_price of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this SubscriptionSubscribedService.
        Subscribed service net unit price


        :param net_unit_price: The net_unit_price of this SubscriptionSubscribedService.
        :type: str
        """
        self._net_unit_price = net_unit_price

    @property
    def used_amount(self):
        """
        Gets the used_amount of this SubscriptionSubscribedService.
        Subscribed service used amount


        :return: The used_amount of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        """
        Sets the used_amount of this SubscriptionSubscribedService.
        Subscribed service used amount


        :param used_amount: The used_amount of this SubscriptionSubscribedService.
        :type: str
        """
        self._used_amount = used_amount

    @property
    def available_amount(self):
        """
        Gets the available_amount of this SubscriptionSubscribedService.
        Subscribed sercice available or remaining amount


        :return: The available_amount of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._available_amount

    @available_amount.setter
    def available_amount(self, available_amount):
        """
        Sets the available_amount of this SubscriptionSubscribedService.
        Subscribed sercice available or remaining amount


        :param available_amount: The available_amount of this SubscriptionSubscribedService.
        :type: str
        """
        self._available_amount = available_amount

    @property
    def funded_allocation_value(self):
        """
        Gets the funded_allocation_value of this SubscriptionSubscribedService.
        Funded Allocation line value
        example: 12000.00


        :return: The funded_allocation_value of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._funded_allocation_value

    @funded_allocation_value.setter
    def funded_allocation_value(self, funded_allocation_value):
        """
        Sets the funded_allocation_value of this SubscriptionSubscribedService.
        Funded Allocation line value
        example: 12000.00


        :param funded_allocation_value: The funded_allocation_value of this SubscriptionSubscribedService.
        :type: str
        """
        self._funded_allocation_value = funded_allocation_value

    @property
    def partner_transaction_type(self):
        """
        Gets the partner_transaction_type of this SubscriptionSubscribedService.
        This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ


        :return: The partner_transaction_type of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._partner_transaction_type

    @partner_transaction_type.setter
    def partner_transaction_type(self, partner_transaction_type):
        """
        Sets the partner_transaction_type of this SubscriptionSubscribedService.
        This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ


        :param partner_transaction_type: The partner_transaction_type of this SubscriptionSubscribedService.
        :type: str
        """
        self._partner_transaction_type = partner_transaction_type

    @property
    def term_value(self):
        """
        Gets the term_value of this SubscriptionSubscribedService.
        Term value in Months


        :return: The term_value of this SubscriptionSubscribedService.
        :rtype: int
        """
        return self._term_value

    @term_value.setter
    def term_value(self, term_value):
        """
        Sets the term_value of this SubscriptionSubscribedService.
        Term value in Months


        :param term_value: The term_value of this SubscriptionSubscribedService.
        :type: int
        """
        self._term_value = term_value

    @property
    def term_value_uom(self):
        """
        Gets the term_value_uom of this SubscriptionSubscribedService.
        Term value UOM


        :return: The term_value_uom of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._term_value_uom

    @term_value_uom.setter
    def term_value_uom(self, term_value_uom):
        """
        Sets the term_value_uom of this SubscriptionSubscribedService.
        Term value UOM


        :param term_value_uom: The term_value_uom of this SubscriptionSubscribedService.
        :type: str
        """
        self._term_value_uom = term_value_uom

    @property
    def booking_opty_number(self):
        """
        Gets the booking_opty_number of this SubscriptionSubscribedService.
        Booking Opportunity Number of Subscribed Service


        :return: The booking_opty_number of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._booking_opty_number

    @booking_opty_number.setter
    def booking_opty_number(self, booking_opty_number):
        """
        Sets the booking_opty_number of this SubscriptionSubscribedService.
        Booking Opportunity Number of Subscribed Service


        :param booking_opty_number: The booking_opty_number of this SubscriptionSubscribedService.
        :type: str
        """
        self._booking_opty_number = booking_opty_number

    @property
    def total_value(self):
        """
        Gets the total_value of this SubscriptionSubscribedService.
        Subscribed service total value


        :return: The total_value of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._total_value

    @total_value.setter
    def total_value(self, total_value):
        """
        Sets the total_value of this SubscriptionSubscribedService.
        Subscribed service total value


        :param total_value: The total_value of this SubscriptionSubscribedService.
        :type: str
        """
        self._total_value = total_value

    @property
    def original_promo_amount(self):
        """
        Gets the original_promo_amount of this SubscriptionSubscribedService.
        Subscribed service Promotion Amount


        :return: The original_promo_amount of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._original_promo_amount

    @original_promo_amount.setter
    def original_promo_amount(self, original_promo_amount):
        """
        Sets the original_promo_amount of this SubscriptionSubscribedService.
        Subscribed service Promotion Amount


        :param original_promo_amount: The original_promo_amount of this SubscriptionSubscribedService.
        :type: str
        """
        self._original_promo_amount = original_promo_amount

    @property
    def order_number(self):
        """
        Gets the order_number of this SubscriptionSubscribedService.
        Sales Order Number associated to the subscribed service


        :return: The order_number of this SubscriptionSubscribedService.
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """
        Sets the order_number of this SubscriptionSubscribedService.
        Sales Order Number associated to the subscribed service


        :param order_number: The order_number of this SubscriptionSubscribedService.
        :type: int
        """
        self._order_number = order_number

    @property
    def data_center_region(self):
        """
        Gets the data_center_region of this SubscriptionSubscribedService.
        Subscribed service data center region


        :return: The data_center_region of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._data_center_region

    @data_center_region.setter
    def data_center_region(self, data_center_region):
        """
        Sets the data_center_region of this SubscriptionSubscribedService.
        Subscribed service data center region


        :param data_center_region: The data_center_region of this SubscriptionSubscribedService.
        :type: str
        """
        self._data_center_region = data_center_region

    @property
    def pricing_model(self):
        """
        Gets the pricing_model of this SubscriptionSubscribedService.
        Subscribed service pricing model


        :return: The pricing_model of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._pricing_model

    @pricing_model.setter
    def pricing_model(self, pricing_model):
        """
        Sets the pricing_model of this SubscriptionSubscribedService.
        Subscribed service pricing model


        :param pricing_model: The pricing_model of this SubscriptionSubscribedService.
        :type: str
        """
        self._pricing_model = pricing_model

    @property
    def program_type(self):
        """
        Gets the program_type of this SubscriptionSubscribedService.
        Subscribed service program type


        :return: The program_type of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._program_type

    @program_type.setter
    def program_type(self, program_type):
        """
        Sets the program_type of this SubscriptionSubscribedService.
        Subscribed service program type


        :param program_type: The program_type of this SubscriptionSubscribedService.
        :type: str
        """
        self._program_type = program_type

    @property
    def promo_type(self):
        """
        Gets the promo_type of this SubscriptionSubscribedService.
        Subscribed service promotion type


        :return: The promo_type of this SubscriptionSubscribedService.
        :rtype: str
        """
        return self._promo_type

    @promo_type.setter
    def promo_type(self, promo_type):
        """
        Sets the promo_type of this SubscriptionSubscribedService.
        Subscribed service promotion type


        :param promo_type: The promo_type of this SubscriptionSubscribedService.
        :type: str
        """
        self._promo_type = promo_type

    @property
    def csi(self):
        """
        Gets the csi of this SubscriptionSubscribedService.
        Subscribed service CSI number


        :return: The csi of this SubscriptionSubscribedService.
        :rtype: int
        """
        return self._csi

    @csi.setter
    def csi(self, csi):
        """
        Sets the csi of this SubscriptionSubscribedService.
        Subscribed service CSI number


        :param csi: The csi of this SubscriptionSubscribedService.
        :type: int
        """
        self._csi = csi

    @property
    def is_intent_to_pay(self):
        """
        Gets the is_intent_to_pay of this SubscriptionSubscribedService.
        Subscribed service intent to pay flag


        :return: The is_intent_to_pay of this SubscriptionSubscribedService.
        :rtype: bool
        """
        return self._is_intent_to_pay

    @is_intent_to_pay.setter
    def is_intent_to_pay(self, is_intent_to_pay):
        """
        Sets the is_intent_to_pay of this SubscriptionSubscribedService.
        Subscribed service intent to pay flag


        :param is_intent_to_pay: The is_intent_to_pay of this SubscriptionSubscribedService.
        :type: bool
        """
        self._is_intent_to_pay = is_intent_to_pay

    @property
    def time_start(self):
        """
        Gets the time_start of this SubscriptionSubscribedService.
        Subscribed service start date


        :return: The time_start of this SubscriptionSubscribedService.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this SubscriptionSubscribedService.
        Subscribed service start date


        :param time_start: The time_start of this SubscriptionSubscribedService.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this SubscriptionSubscribedService.
        Subscribed service end date


        :return: The time_end of this SubscriptionSubscribedService.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this SubscriptionSubscribedService.
        Subscribed service end date


        :param time_end: The time_end of this SubscriptionSubscribedService.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def commitment_services(self):
        """
        Gets the commitment_services of this SubscriptionSubscribedService.
        List of Commitment services of a line


        :return: The commitment_services of this SubscriptionSubscribedService.
        :rtype: list[oci.onesubscription.models.CommitmentService]
        """
        return self._commitment_services

    @commitment_services.setter
    def commitment_services(self, commitment_services):
        """
        Sets the commitment_services of this SubscriptionSubscribedService.
        List of Commitment services of a line


        :param commitment_services: The commitment_services of this SubscriptionSubscribedService.
        :type: list[oci.onesubscription.models.CommitmentService]
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
