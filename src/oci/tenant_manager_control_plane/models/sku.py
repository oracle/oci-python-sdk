# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Sku(object):
    """
    A single subscription SKU.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Sku object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param number:
            The value to assign to the number property of this Sku.
        :type number: str

        :param name:
            The value to assign to the name property of this Sku.
        :type name: str

        :param quantity:
            The value to assign to the quantity property of this Sku.
        :type quantity: int

        """
        self.swagger_types = {
            'number': 'str',
            'name': 'str',
            'quantity': 'int'
        }

        self.attribute_map = {
            'number': 'number',
            'name': 'name',
            'quantity': 'quantity'
        }

        self._number = None
        self._name = None
        self._quantity = None

    @property
    def number(self):
        """
        Gets the number of this Sku.
        SKU number.


        :return: The number of this Sku.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Sku.
        SKU number.


        :param number: The number of this Sku.
        :type: str
        """
        self._number = number

    @property
    def name(self):
        """
        Gets the name of this Sku.
        SKU name.


        :return: The name of this Sku.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Sku.
        SKU name.


        :param name: The name of this Sku.
        :type: str
        """
        self._name = name

    @property
    def quantity(self):
        """
        Gets the quantity of this Sku.
        SKU quantity.


        :return: The quantity of this Sku.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this Sku.
        SKU quantity.


        :param quantity: The quantity of this Sku.
        :type: int
        """
        self._quantity = quantity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
