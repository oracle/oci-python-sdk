# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProductSummary(object):
    """
    Provides details about product rewards and the usage amount.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProductSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param product_number:
            The value to assign to the product_number property of this ProductSummary.
        :type product_number: str

        :param product_name:
            The value to assign to the product_name property of this ProductSummary.
        :type product_name: str

        :param usage_amount:
            The value to assign to the usage_amount property of this ProductSummary.
        :type usage_amount: float

        :param earned_rewards:
            The value to assign to the earned_rewards property of this ProductSummary.
        :type earned_rewards: float

        :param is_eligible_to_earn_rewards:
            The value to assign to the is_eligible_to_earn_rewards property of this ProductSummary.
        :type is_eligible_to_earn_rewards: bool

        """
        self.swagger_types = {
            'product_number': 'str',
            'product_name': 'str',
            'usage_amount': 'float',
            'earned_rewards': 'float',
            'is_eligible_to_earn_rewards': 'bool'
        }

        self.attribute_map = {
            'product_number': 'productNumber',
            'product_name': 'productName',
            'usage_amount': 'usageAmount',
            'earned_rewards': 'earnedRewards',
            'is_eligible_to_earn_rewards': 'isEligibleToEarnRewards'
        }

        self._product_number = None
        self._product_name = None
        self._usage_amount = None
        self._earned_rewards = None
        self._is_eligible_to_earn_rewards = None

    @property
    def product_number(self):
        """
        Gets the product_number of this ProductSummary.
        The rate card product number.


        :return: The product_number of this ProductSummary.
        :rtype: str
        """
        return self._product_number

    @product_number.setter
    def product_number(self, product_number):
        """
        Sets the product_number of this ProductSummary.
        The rate card product number.


        :param product_number: The product_number of this ProductSummary.
        :type: str
        """
        self._product_number = product_number

    @property
    def product_name(self):
        """
        Gets the product_name of this ProductSummary.
        The rate card product name.


        :return: The product_name of this ProductSummary.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this ProductSummary.
        The rate card product name.


        :param product_name: The product_name of this ProductSummary.
        :type: str
        """
        self._product_name = product_name

    @property
    def usage_amount(self):
        """
        Gets the usage_amount of this ProductSummary.
        The rate card product usage amount.


        :return: The usage_amount of this ProductSummary.
        :rtype: float
        """
        return self._usage_amount

    @usage_amount.setter
    def usage_amount(self, usage_amount):
        """
        Sets the usage_amount of this ProductSummary.
        The rate card product usage amount.


        :param usage_amount: The usage_amount of this ProductSummary.
        :type: float
        """
        self._usage_amount = usage_amount

    @property
    def earned_rewards(self):
        """
        Gets the earned_rewards of this ProductSummary.
        The earned rewards for the product.


        :return: The earned_rewards of this ProductSummary.
        :rtype: float
        """
        return self._earned_rewards

    @earned_rewards.setter
    def earned_rewards(self, earned_rewards):
        """
        Sets the earned_rewards of this ProductSummary.
        The earned rewards for the product.


        :param earned_rewards: The earned_rewards of this ProductSummary.
        :type: float
        """
        self._earned_rewards = earned_rewards

    @property
    def is_eligible_to_earn_rewards(self):
        """
        Gets the is_eligible_to_earn_rewards of this ProductSummary.
        The boolean parameter to indicate if the product is eligible to earn rewards.


        :return: The is_eligible_to_earn_rewards of this ProductSummary.
        :rtype: bool
        """
        return self._is_eligible_to_earn_rewards

    @is_eligible_to_earn_rewards.setter
    def is_eligible_to_earn_rewards(self, is_eligible_to_earn_rewards):
        """
        Sets the is_eligible_to_earn_rewards of this ProductSummary.
        The boolean parameter to indicate if the product is eligible to earn rewards.


        :param is_eligible_to_earn_rewards: The is_eligible_to_earn_rewards of this ProductSummary.
        :type: bool
        """
        self._is_eligible_to_earn_rewards = is_eligible_to_earn_rewards

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
