# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FacetedSearchCustomProperty(object):
    """
    Details about custom property
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FacetedSearchCustomProperty object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this FacetedSearchCustomProperty.
        :type name: str

        :param value:
            The value to assign to the value property of this FacetedSearchCustomProperty.
        :type value: str

        :param data_type:
            The value to assign to the data_type property of this FacetedSearchCustomProperty.
        :type data_type: str

        """
        self.swagger_types = {
            'name': 'str',
            'value': 'str',
            'data_type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value',
            'data_type': 'dataType'
        }

        self._name = None
        self._value = None
        self._data_type = None

    @property
    def name(self):
        """
        Gets the name of this FacetedSearchCustomProperty.
        Name of custom property field


        :return: The name of this FacetedSearchCustomProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FacetedSearchCustomProperty.
        Name of custom property field


        :param name: The name of this FacetedSearchCustomProperty.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        Gets the value of this FacetedSearchCustomProperty.
        Value of the custom property field


        :return: The value of this FacetedSearchCustomProperty.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this FacetedSearchCustomProperty.
        Value of the custom property field


        :param value: The value of this FacetedSearchCustomProperty.
        :type: str
        """
        self._value = value

    @property
    def data_type(self):
        """
        Gets the data_type of this FacetedSearchCustomProperty.
        Data type of the custom property field


        :return: The data_type of this FacetedSearchCustomProperty.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this FacetedSearchCustomProperty.
        Data type of the custom property field


        :param data_type: The data_type of this FacetedSearchCustomProperty.
        :type: str
        """
        self._data_type = data_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
