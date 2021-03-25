# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UsageStatusItem(object):
    """
    UsageStatusItem
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UsageStatusItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_type:
            The value to assign to the data_type property of this UsageStatusItem.
        :type data_type: str

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this UsageStatusItem.
        :type is_multi_valued: bool

        :param current_usage:
            The value to assign to the current_usage property of this UsageStatusItem.
        :type current_usage: int

        :param max_available:
            The value to assign to the max_available property of this UsageStatusItem.
        :type max_available: int

        """
        self.swagger_types = {
            'data_type': 'str',
            'is_multi_valued': 'bool',
            'current_usage': 'int',
            'max_available': 'int'
        }

        self.attribute_map = {
            'data_type': 'dataType',
            'is_multi_valued': 'isMultiValued',
            'current_usage': 'currentUsage',
            'max_available': 'maxAvailable'
        }

        self._data_type = None
        self._is_multi_valued = None
        self._current_usage = None
        self._max_available = None

    @property
    def data_type(self):
        """
        Gets the data_type of this UsageStatusItem.
        The field data type.


        :return: The data_type of this UsageStatusItem.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this UsageStatusItem.
        The field data type.


        :param data_type: The data_type of this UsageStatusItem.
        :type: str
        """
        self._data_type = data_type

    @property
    def is_multi_valued(self):
        """
        Gets the is_multi_valued of this UsageStatusItem.
        A flag indicating whether or not the field is multi-valued.


        :return: The is_multi_valued of this UsageStatusItem.
        :rtype: bool
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued):
        """
        Sets the is_multi_valued of this UsageStatusItem.
        A flag indicating whether or not the field is multi-valued.


        :param is_multi_valued: The is_multi_valued of this UsageStatusItem.
        :type: bool
        """
        self._is_multi_valued = is_multi_valued

    @property
    def current_usage(self):
        """
        Gets the current_usage of this UsageStatusItem.
        The current usage of the field.


        :return: The current_usage of this UsageStatusItem.
        :rtype: int
        """
        return self._current_usage

    @current_usage.setter
    def current_usage(self, current_usage):
        """
        Sets the current_usage of this UsageStatusItem.
        The current usage of the field.


        :param current_usage: The current_usage of this UsageStatusItem.
        :type: int
        """
        self._current_usage = current_usage

    @property
    def max_available(self):
        """
        Gets the max_available of this UsageStatusItem.
        The maximum availability of the field.


        :return: The max_available of this UsageStatusItem.
        :rtype: int
        """
        return self._max_available

    @max_available.setter
    def max_available(self, max_available):
        """
        Sets the max_available of this UsageStatusItem.
        The maximum availability of the field.


        :param max_available: The max_available of this UsageStatusItem.
        :type: int
        """
        self._max_available = max_available

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
