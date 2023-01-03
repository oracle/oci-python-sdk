# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvoicelineComputedUsageSummary(object):
    """
    Computed Usage Summary object
    """

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "PROMOTION"
    TYPE_PROMOTION = "PROMOTION"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "DO_NOT_BILL"
    TYPE_DO_NOT_BILL = "DO_NOT_BILL"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "USAGE"
    TYPE_USAGE = "USAGE"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "COMMIT"
    TYPE_COMMIT = "COMMIT"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "OVERAGE"
    TYPE_OVERAGE = "OVERAGE"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "PAY_AS_YOU_GO"
    TYPE_PAY_AS_YOU_GO = "PAY_AS_YOU_GO"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "MONTHLY_MINIMUM"
    TYPE_MONTHLY_MINIMUM = "MONTHLY_MINIMUM"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "DELAYED_USAGE_INVOICE_TIMING"
    TYPE_DELAYED_USAGE_INVOICE_TIMING = "DELAYED_USAGE_INVOICE_TIMING"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "DELAYED_USAGE_COMMITMENT_EXP"
    TYPE_DELAYED_USAGE_COMMITMENT_EXP = "DELAYED_USAGE_COMMITMENT_EXP"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "ON_ACCOUNT_CREDIT"
    TYPE_ON_ACCOUNT_CREDIT = "ON_ACCOUNT_CREDIT"

    #: A constant which can be used with the type property of a InvoicelineComputedUsageSummary.
    #: This constant has a value of "SERVICE_CREDIT"
    TYPE_SERVICE_CREDIT = "SERVICE_CREDIT"

    def __init__(self, **kwargs):
        """
        Initializes a new InvoicelineComputedUsageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parent_product:
            The value to assign to the parent_product property of this InvoicelineComputedUsageSummary.
        :type parent_product: oci.onesubscription.models.InvoicingProduct

        :param product:
            The value to assign to the product property of this InvoicelineComputedUsageSummary.
        :type product: oci.onesubscription.models.InvoicingProduct

        :param quantity:
            The value to assign to the quantity property of this InvoicelineComputedUsageSummary.
        :type quantity: float

        :param net_unit_price:
            The value to assign to the net_unit_price property of this InvoicelineComputedUsageSummary.
        :type net_unit_price: float

        :param time_metered_on:
            The value to assign to the time_metered_on property of this InvoicelineComputedUsageSummary.
        :type time_metered_on: datetime

        :param type:
            The value to assign to the type property of this InvoicelineComputedUsageSummary.
            Allowed values for this property are: "PROMOTION", "DO_NOT_BILL", "USAGE", "COMMIT", "OVERAGE", "PAY_AS_YOU_GO", "MONTHLY_MINIMUM", "DELAYED_USAGE_INVOICE_TIMING", "DELAYED_USAGE_COMMITMENT_EXP", "ON_ACCOUNT_CREDIT", "SERVICE_CREDIT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param cost:
            The value to assign to the cost property of this InvoicelineComputedUsageSummary.
        :type cost: float

        :param cost_rounded:
            The value to assign to the cost_rounded property of this InvoicelineComputedUsageSummary.
        :type cost_rounded: float

        """
        self.swagger_types = {
            'parent_product': 'InvoicingProduct',
            'product': 'InvoicingProduct',
            'quantity': 'float',
            'net_unit_price': 'float',
            'time_metered_on': 'datetime',
            'type': 'str',
            'cost': 'float',
            'cost_rounded': 'float'
        }

        self.attribute_map = {
            'parent_product': 'parentProduct',
            'product': 'product',
            'quantity': 'quantity',
            'net_unit_price': 'netUnitPrice',
            'time_metered_on': 'timeMeteredOn',
            'type': 'type',
            'cost': 'cost',
            'cost_rounded': 'costRounded'
        }

        self._parent_product = None
        self._product = None
        self._quantity = None
        self._net_unit_price = None
        self._time_metered_on = None
        self._type = None
        self._cost = None
        self._cost_rounded = None

    @property
    def parent_product(self):
        """
        **[Required]** Gets the parent_product of this InvoicelineComputedUsageSummary.

        :return: The parent_product of this InvoicelineComputedUsageSummary.
        :rtype: oci.onesubscription.models.InvoicingProduct
        """
        return self._parent_product

    @parent_product.setter
    def parent_product(self, parent_product):
        """
        Sets the parent_product of this InvoicelineComputedUsageSummary.

        :param parent_product: The parent_product of this InvoicelineComputedUsageSummary.
        :type: oci.onesubscription.models.InvoicingProduct
        """
        self._parent_product = parent_product

    @property
    def product(self):
        """
        Gets the product of this InvoicelineComputedUsageSummary.

        :return: The product of this InvoicelineComputedUsageSummary.
        :rtype: oci.onesubscription.models.InvoicingProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this InvoicelineComputedUsageSummary.

        :param product: The product of this InvoicelineComputedUsageSummary.
        :type: oci.onesubscription.models.InvoicingProduct
        """
        self._product = product

    @property
    def quantity(self):
        """
        **[Required]** Gets the quantity of this InvoicelineComputedUsageSummary.
        Total Quantity that was used for computation


        :return: The quantity of this InvoicelineComputedUsageSummary.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this InvoicelineComputedUsageSummary.
        Total Quantity that was used for computation


        :param quantity: The quantity of this InvoicelineComputedUsageSummary.
        :type: float
        """
        self._quantity = quantity

    @property
    def net_unit_price(self):
        """
        **[Required]** Gets the net_unit_price of this InvoicelineComputedUsageSummary.
        Net Unit Price for the product in consideration, price actual.


        :return: The net_unit_price of this InvoicelineComputedUsageSummary.
        :rtype: float
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this InvoicelineComputedUsageSummary.
        Net Unit Price for the product in consideration, price actual.


        :param net_unit_price: The net_unit_price of this InvoicelineComputedUsageSummary.
        :type: float
        """
        self._net_unit_price = net_unit_price

    @property
    def time_metered_on(self):
        """
        **[Required]** Gets the time_metered_on of this InvoicelineComputedUsageSummary.
        Metered Service date.


        :return: The time_metered_on of this InvoicelineComputedUsageSummary.
        :rtype: datetime
        """
        return self._time_metered_on

    @time_metered_on.setter
    def time_metered_on(self, time_metered_on):
        """
        Sets the time_metered_on of this InvoicelineComputedUsageSummary.
        Metered Service date.


        :param time_metered_on: The time_metered_on of this InvoicelineComputedUsageSummary.
        :type: datetime
        """
        self._time_metered_on = time_metered_on

    @property
    def type(self):
        """
        **[Required]** Gets the type of this InvoicelineComputedUsageSummary.
        Usage compute type in SPM.

        Allowed values for this property are: "PROMOTION", "DO_NOT_BILL", "USAGE", "COMMIT", "OVERAGE", "PAY_AS_YOU_GO", "MONTHLY_MINIMUM", "DELAYED_USAGE_INVOICE_TIMING", "DELAYED_USAGE_COMMITMENT_EXP", "ON_ACCOUNT_CREDIT", "SERVICE_CREDIT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this InvoicelineComputedUsageSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InvoicelineComputedUsageSummary.
        Usage compute type in SPM.


        :param type: The type of this InvoicelineComputedUsageSummary.
        :type: str
        """
        allowed_values = ["PROMOTION", "DO_NOT_BILL", "USAGE", "COMMIT", "OVERAGE", "PAY_AS_YOU_GO", "MONTHLY_MINIMUM", "DELAYED_USAGE_INVOICE_TIMING", "DELAYED_USAGE_COMMITMENT_EXP", "ON_ACCOUNT_CREDIT", "SERVICE_CREDIT"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def cost(self):
        """
        Gets the cost of this InvoicelineComputedUsageSummary.
        Sum of Usage/Service Billing Line net Amount


        :return: The cost of this InvoicelineComputedUsageSummary.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this InvoicelineComputedUsageSummary.
        Sum of Usage/Service Billing Line net Amount


        :param cost: The cost of this InvoicelineComputedUsageSummary.
        :type: float
        """
        self._cost = cost

    @property
    def cost_rounded(self):
        """
        **[Required]** Gets the cost_rounded of this InvoicelineComputedUsageSummary.
        Computed Line Amount rounded.


        :return: The cost_rounded of this InvoicelineComputedUsageSummary.
        :rtype: float
        """
        return self._cost_rounded

    @cost_rounded.setter
    def cost_rounded(self, cost_rounded):
        """
        Sets the cost_rounded of this InvoicelineComputedUsageSummary.
        Computed Line Amount rounded.


        :param cost_rounded: The cost_rounded of this InvoicelineComputedUsageSummary.
        :type: float
        """
        self._cost_rounded = cost_rounded

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
