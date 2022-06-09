# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RateCardSummary(object):
    """
    Rate Card Summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RateCardSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subscribed_service_id:
            The value to assign to the subscribed_service_id property of this RateCardSummary.
        :type subscribed_service_id: str

        :param product:
            The value to assign to the product property of this RateCardSummary.
        :type product: oci.onesubscription.models.RateCardProduct

        :param time_start:
            The value to assign to the time_start property of this RateCardSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this RateCardSummary.
        :type time_end: datetime

        :param net_unit_price:
            The value to assign to the net_unit_price property of this RateCardSummary.
        :type net_unit_price: str

        :param discretionary_discount_percentage:
            The value to assign to the discretionary_discount_percentage property of this RateCardSummary.
        :type discretionary_discount_percentage: str

        :param overage_price:
            The value to assign to the overage_price property of this RateCardSummary.
        :type overage_price: str

        :param is_tier:
            The value to assign to the is_tier property of this RateCardSummary.
        :type is_tier: bool

        :param currency:
            The value to assign to the currency property of this RateCardSummary.
        :type currency: oci.onesubscription.models.SubscriptionCurrency

        :param rate_card_tiers:
            The value to assign to the rate_card_tiers property of this RateCardSummary.
        :type rate_card_tiers: list[oci.onesubscription.models.RateCardTier]

        """
        self.swagger_types = {
            'subscribed_service_id': 'str',
            'product': 'RateCardProduct',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'net_unit_price': 'str',
            'discretionary_discount_percentage': 'str',
            'overage_price': 'str',
            'is_tier': 'bool',
            'currency': 'SubscriptionCurrency',
            'rate_card_tiers': 'list[RateCardTier]'
        }

        self.attribute_map = {
            'subscribed_service_id': 'subscribedServiceId',
            'product': 'product',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'net_unit_price': 'netUnitPrice',
            'discretionary_discount_percentage': 'discretionaryDiscountPercentage',
            'overage_price': 'overagePrice',
            'is_tier': 'isTier',
            'currency': 'currency',
            'rate_card_tiers': 'rateCardTiers'
        }

        self._subscribed_service_id = None
        self._product = None
        self._time_start = None
        self._time_end = None
        self._net_unit_price = None
        self._discretionary_discount_percentage = None
        self._overage_price = None
        self._is_tier = None
        self._currency = None
        self._rate_card_tiers = None

    @property
    def subscribed_service_id(self):
        """
        Gets the subscribed_service_id of this RateCardSummary.
        SPM internal Subscribed Service ID


        :return: The subscribed_service_id of this RateCardSummary.
        :rtype: str
        """
        return self._subscribed_service_id

    @subscribed_service_id.setter
    def subscribed_service_id(self, subscribed_service_id):
        """
        Sets the subscribed_service_id of this RateCardSummary.
        SPM internal Subscribed Service ID


        :param subscribed_service_id: The subscribed_service_id of this RateCardSummary.
        :type: str
        """
        self._subscribed_service_id = subscribed_service_id

    @property
    def product(self):
        """
        **[Required]** Gets the product of this RateCardSummary.

        :return: The product of this RateCardSummary.
        :rtype: oci.onesubscription.models.RateCardProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this RateCardSummary.

        :param product: The product of this RateCardSummary.
        :type: oci.onesubscription.models.RateCardProduct
        """
        self._product = product

    @property
    def time_start(self):
        """
        Gets the time_start of this RateCardSummary.
        Rate card start date


        :return: The time_start of this RateCardSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this RateCardSummary.
        Rate card start date


        :param time_start: The time_start of this RateCardSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this RateCardSummary.
        Rate card end date


        :return: The time_end of this RateCardSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this RateCardSummary.
        Rate card end date


        :param time_end: The time_end of this RateCardSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def net_unit_price(self):
        """
        **[Required]** Gets the net_unit_price of this RateCardSummary.
        Rate card net unit price


        :return: The net_unit_price of this RateCardSummary.
        :rtype: str
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this RateCardSummary.
        Rate card net unit price


        :param net_unit_price: The net_unit_price of this RateCardSummary.
        :type: str
        """
        self._net_unit_price = net_unit_price

    @property
    def discretionary_discount_percentage(self):
        """
        Gets the discretionary_discount_percentage of this RateCardSummary.
        Rate card discretionary discount percentage


        :return: The discretionary_discount_percentage of this RateCardSummary.
        :rtype: str
        """
        return self._discretionary_discount_percentage

    @discretionary_discount_percentage.setter
    def discretionary_discount_percentage(self, discretionary_discount_percentage):
        """
        Sets the discretionary_discount_percentage of this RateCardSummary.
        Rate card discretionary discount percentage


        :param discretionary_discount_percentage: The discretionary_discount_percentage of this RateCardSummary.
        :type: str
        """
        self._discretionary_discount_percentage = discretionary_discount_percentage

    @property
    def overage_price(self):
        """
        **[Required]** Gets the overage_price of this RateCardSummary.
        Rate card overage price


        :return: The overage_price of this RateCardSummary.
        :rtype: str
        """
        return self._overage_price

    @overage_price.setter
    def overage_price(self, overage_price):
        """
        Sets the overage_price of this RateCardSummary.
        Rate card overage price


        :param overage_price: The overage_price of this RateCardSummary.
        :type: str
        """
        self._overage_price = overage_price

    @property
    def is_tier(self):
        """
        Gets the is_tier of this RateCardSummary.
        Rate card price tier flag


        :return: The is_tier of this RateCardSummary.
        :rtype: bool
        """
        return self._is_tier

    @is_tier.setter
    def is_tier(self, is_tier):
        """
        Sets the is_tier of this RateCardSummary.
        Rate card price tier flag


        :param is_tier: The is_tier of this RateCardSummary.
        :type: bool
        """
        self._is_tier = is_tier

    @property
    def currency(self):
        """
        Gets the currency of this RateCardSummary.

        :return: The currency of this RateCardSummary.
        :rtype: oci.onesubscription.models.SubscriptionCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this RateCardSummary.

        :param currency: The currency of this RateCardSummary.
        :type: oci.onesubscription.models.SubscriptionCurrency
        """
        self._currency = currency

    @property
    def rate_card_tiers(self):
        """
        Gets the rate_card_tiers of this RateCardSummary.
        List of tiered rate card prices


        :return: The rate_card_tiers of this RateCardSummary.
        :rtype: list[oci.onesubscription.models.RateCardTier]
        """
        return self._rate_card_tiers

    @rate_card_tiers.setter
    def rate_card_tiers(self, rate_card_tiers):
        """
        Sets the rate_card_tiers of this RateCardSummary.
        List of tiered rate card prices


        :param rate_card_tiers: The rate_card_tiers of this RateCardSummary.
        :type: list[oci.onesubscription.models.RateCardTier]
        """
        self._rate_card_tiers = rate_card_tiers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
