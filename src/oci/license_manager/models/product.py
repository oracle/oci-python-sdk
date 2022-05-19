# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Product(object):
    """
    Details of product.
    """

    #: A constant which can be used with the category property of a Product.
    #: This constant has a value of "BASE"
    CATEGORY_BASE = "BASE"

    #: A constant which can be used with the category property of a Product.
    #: This constant has a value of "OPTION"
    CATEGORY_OPTION = "OPTION"

    def __init__(self, **kwargs):
        """
        Initializes a new Product object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Product.
        :type name: str

        :param count:
            The value to assign to the count property of this Product.
        :type count: float

        :param category:
            The value to assign to the category property of this Product.
            Allowed values for this property are: "BASE", "OPTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type category: str

        """
        self.swagger_types = {
            'name': 'str',
            'count': 'float',
            'category': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'count': 'count',
            'category': 'category'
        }

        self._name = None
        self._count = None
        self._category = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Product.
        Name of the product.


        :return: The name of this Product.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Product.
        Name of the product.


        :param name: The name of this Product.
        :type: str
        """
        self._name = name

    @property
    def count(self):
        """
        **[Required]** Gets the count of this Product.
        Units required for the missing product.


        :return: The count of this Product.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this Product.
        Units required for the missing product.


        :param count: The count of this Product.
        :type: float
        """
        self._count = count

    @property
    def category(self):
        """
        **[Required]** Gets the category of this Product.
        Product category base or option.

        Allowed values for this property are: "BASE", "OPTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The category of this Product.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Product.
        Product category base or option.


        :param category: The category of this Product.
        :type: str
        """
        allowed_values = ["BASE", "OPTION"]
        if not value_allowed_none_or_none_sentinel(category, allowed_values):
            category = 'UNKNOWN_ENUM_VALUE'
        self._category = category

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
