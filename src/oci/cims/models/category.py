# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Category(object):
    """
    Details of Category of the incident
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Category object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param category_key:
            The value to assign to the category_key property of this Category.
        :type category_key: str

        :param name:
            The value to assign to the name property of this Category.
        :type name: str

        """
        self.swagger_types = {
            'category_key': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'category_key': 'categoryKey',
            'name': 'name'
        }

        self._category_key = None
        self._name = None

    @property
    def category_key(self):
        """
        Gets the category_key of this Category.
        Unique ID that identifies a Category


        :return: The category_key of this Category.
        :rtype: str
        """
        return self._category_key

    @category_key.setter
    def category_key(self, category_key):
        """
        Sets the category_key of this Category.
        Unique ID that identifies a Category


        :param category_key: The category_key of this Category.
        :type: str
        """
        self._category_key = category_key

    @property
    def name(self):
        """
        Gets the name of this Category.
        Name of category. eg: Compute, Identity


        :return: The name of this Category.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Category.
        Name of category. eg: Compute, Identity


        :param name: The name of this Category.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
