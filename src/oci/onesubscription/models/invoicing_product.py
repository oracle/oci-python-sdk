# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvoicingProduct(object):
    """
    Product description
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InvoicingProduct object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param part_number:
            The value to assign to the part_number property of this InvoicingProduct.
        :type part_number: str

        :param name:
            The value to assign to the name property of this InvoicingProduct.
        :type name: str

        :param unit_of_measure:
            The value to assign to the unit_of_measure property of this InvoicingProduct.
        :type unit_of_measure: str

        :param billing_category:
            The value to assign to the billing_category property of this InvoicingProduct.
        :type billing_category: str

        :param product_category:
            The value to assign to the product_category property of this InvoicingProduct.
        :type product_category: str

        :param ucm_rate_card_part_type:
            The value to assign to the ucm_rate_card_part_type property of this InvoicingProduct.
        :type ucm_rate_card_part_type: str

        """
        self.swagger_types = {
            'part_number': 'str',
            'name': 'str',
            'unit_of_measure': 'str',
            'billing_category': 'str',
            'product_category': 'str',
            'ucm_rate_card_part_type': 'str'
        }

        self.attribute_map = {
            'part_number': 'partNumber',
            'name': 'name',
            'unit_of_measure': 'unitOfMeasure',
            'billing_category': 'billingCategory',
            'product_category': 'productCategory',
            'ucm_rate_card_part_type': 'ucmRateCardPartType'
        }

        self._part_number = None
        self._name = None
        self._unit_of_measure = None
        self._billing_category = None
        self._product_category = None
        self._ucm_rate_card_part_type = None

    @property
    def part_number(self):
        """
        **[Required]** Gets the part_number of this InvoicingProduct.
        Product part number


        :return: The part_number of this InvoicingProduct.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this InvoicingProduct.
        Product part number


        :param part_number: The part_number of this InvoicingProduct.
        :type: str
        """
        self._part_number = part_number

    @property
    def name(self):
        """
        **[Required]** Gets the name of this InvoicingProduct.
        Product name


        :return: The name of this InvoicingProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InvoicingProduct.
        Product name


        :param name: The name of this InvoicingProduct.
        :type: str
        """
        self._name = name

    @property
    def unit_of_measure(self):
        """
        **[Required]** Gets the unit_of_measure of this InvoicingProduct.
        Unit of Measure


        :return: The unit_of_measure of this InvoicingProduct.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this InvoicingProduct.
        Unit of Measure


        :param unit_of_measure: The unit_of_measure of this InvoicingProduct.
        :type: str
        """
        self._unit_of_measure = unit_of_measure

    @property
    def billing_category(self):
        """
        Gets the billing_category of this InvoicingProduct.
        Metered service billing category


        :return: The billing_category of this InvoicingProduct.
        :rtype: str
        """
        return self._billing_category

    @billing_category.setter
    def billing_category(self, billing_category):
        """
        Sets the billing_category of this InvoicingProduct.
        Metered service billing category


        :param billing_category: The billing_category of this InvoicingProduct.
        :type: str
        """
        self._billing_category = billing_category

    @property
    def product_category(self):
        """
        Gets the product_category of this InvoicingProduct.
        Product category


        :return: The product_category of this InvoicingProduct.
        :rtype: str
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """
        Sets the product_category of this InvoicingProduct.
        Product category


        :param product_category: The product_category of this InvoicingProduct.
        :type: str
        """
        self._product_category = product_category

    @property
    def ucm_rate_card_part_type(self):
        """
        **[Required]** Gets the ucm_rate_card_part_type of this InvoicingProduct.
        Rate card part type of Product


        :return: The ucm_rate_card_part_type of this InvoicingProduct.
        :rtype: str
        """
        return self._ucm_rate_card_part_type

    @ucm_rate_card_part_type.setter
    def ucm_rate_card_part_type(self, ucm_rate_card_part_type):
        """
        Sets the ucm_rate_card_part_type of this InvoicingProduct.
        Rate card part type of Product


        :param ucm_rate_card_part_type: The ucm_rate_card_part_type of this InvoicingProduct.
        :type: str
        """
        self._ucm_rate_card_part_type = ucm_rate_card_part_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
