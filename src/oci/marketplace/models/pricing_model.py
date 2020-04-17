# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PricingModel(object):
    """
    The model for pricing.
    """

    #: A constant which can be used with the type property of a PricingModel.
    #: This constant has a value of "FREE"
    TYPE_FREE = "FREE"

    #: A constant which can be used with the type property of a PricingModel.
    #: This constant has a value of "BYOL"
    TYPE_BYOL = "BYOL"

    #: A constant which can be used with the type property of a PricingModel.
    #: This constant has a value of "PAYGO"
    TYPE_PAYGO = "PAYGO"

    #: A constant which can be used with the pay_go_strategy property of a PricingModel.
    #: This constant has a value of "PER_OCPU_LINEAR"
    PAY_GO_STRATEGY_PER_OCPU_LINEAR = "PER_OCPU_LINEAR"

    #: A constant which can be used with the pay_go_strategy property of a PricingModel.
    #: This constant has a value of "PER_OCPU_MIN_BILLING"
    PAY_GO_STRATEGY_PER_OCPU_MIN_BILLING = "PER_OCPU_MIN_BILLING"

    #: A constant which can be used with the pay_go_strategy property of a PricingModel.
    #: This constant has a value of "PER_INSTANCE"
    PAY_GO_STRATEGY_PER_INSTANCE = "PER_INSTANCE"

    #: A constant which can be used with the pay_go_strategy property of a PricingModel.
    #: This constant has a value of "PER_INSTANCE_MONTHLY_INCLUSIVE"
    PAY_GO_STRATEGY_PER_INSTANCE_MONTHLY_INCLUSIVE = "PER_INSTANCE_MONTHLY_INCLUSIVE"

    #: A constant which can be used with the currency property of a PricingModel.
    #: This constant has a value of "USD"
    CURRENCY_USD = "USD"

    def __init__(self, **kwargs):
        """
        Initializes a new PricingModel object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this PricingModel.
            Allowed values for this property are: "FREE", "BYOL", "PAYGO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param pay_go_strategy:
            The value to assign to the pay_go_strategy property of this PricingModel.
            Allowed values for this property are: "PER_OCPU_LINEAR", "PER_OCPU_MIN_BILLING", "PER_INSTANCE", "PER_INSTANCE_MONTHLY_INCLUSIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type pay_go_strategy: str

        :param currency:
            The value to assign to the currency property of this PricingModel.
            Allowed values for this property are: "USD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type currency: str

        :param rate:
            The value to assign to the rate property of this PricingModel.
        :type rate: float

        """
        self.swagger_types = {
            'type': 'str',
            'pay_go_strategy': 'str',
            'currency': 'str',
            'rate': 'float'
        }

        self.attribute_map = {
            'type': 'type',
            'pay_go_strategy': 'payGoStrategy',
            'currency': 'currency',
            'rate': 'rate'
        }

        self._type = None
        self._pay_go_strategy = None
        self._currency = None
        self._rate = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this PricingModel.
        The type of the pricing model.

        Allowed values for this property are: "FREE", "BYOL", "PAYGO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this PricingModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PricingModel.
        The type of the pricing model.


        :param type: The type of this PricingModel.
        :type: str
        """
        allowed_values = ["FREE", "BYOL", "PAYGO"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def pay_go_strategy(self):
        """
        Gets the pay_go_strategy of this PricingModel.
        The type of pricing for a PAYGO model, eg PER_OCPU_LINEAR, PER_OCPU_MIN_BILLING, PER_INSTANCE.  Null if type is not PAYGO.

        Allowed values for this property are: "PER_OCPU_LINEAR", "PER_OCPU_MIN_BILLING", "PER_INSTANCE", "PER_INSTANCE_MONTHLY_INCLUSIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The pay_go_strategy of this PricingModel.
        :rtype: str
        """
        return self._pay_go_strategy

    @pay_go_strategy.setter
    def pay_go_strategy(self, pay_go_strategy):
        """
        Sets the pay_go_strategy of this PricingModel.
        The type of pricing for a PAYGO model, eg PER_OCPU_LINEAR, PER_OCPU_MIN_BILLING, PER_INSTANCE.  Null if type is not PAYGO.


        :param pay_go_strategy: The pay_go_strategy of this PricingModel.
        :type: str
        """
        allowed_values = ["PER_OCPU_LINEAR", "PER_OCPU_MIN_BILLING", "PER_INSTANCE", "PER_INSTANCE_MONTHLY_INCLUSIVE"]
        if not value_allowed_none_or_none_sentinel(pay_go_strategy, allowed_values):
            pay_go_strategy = 'UNKNOWN_ENUM_VALUE'
        self._pay_go_strategy = pay_go_strategy

    @property
    def currency(self):
        """
        Gets the currency of this PricingModel.
        The currency of the pricing model.

        Allowed values for this property are: "USD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The currency of this PricingModel.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PricingModel.
        The currency of the pricing model.


        :param currency: The currency of this PricingModel.
        :type: str
        """
        allowed_values = ["USD"]
        if not value_allowed_none_or_none_sentinel(currency, allowed_values):
            currency = 'UNKNOWN_ENUM_VALUE'
        self._currency = currency

    @property
    def rate(self):
        """
        Gets the rate of this PricingModel.
        The pricing rate.


        :return: The rate of this PricingModel.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this PricingModel.
        The pricing rate.


        :param rate: The rate of this PricingModel.
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
