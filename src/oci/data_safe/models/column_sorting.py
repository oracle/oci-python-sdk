# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ColumnSorting(object):
    """
    Sorting the data at the column level.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ColumnSorting object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_name:
            The value to assign to the field_name property of this ColumnSorting.
        :type field_name: str

        :param is_ascending:
            The value to assign to the is_ascending property of this ColumnSorting.
        :type is_ascending: bool

        :param sorting_order:
            The value to assign to the sorting_order property of this ColumnSorting.
        :type sorting_order: int

        """
        self.swagger_types = {
            'field_name': 'str',
            'is_ascending': 'bool',
            'sorting_order': 'int'
        }

        self.attribute_map = {
            'field_name': 'fieldName',
            'is_ascending': 'isAscending',
            'sorting_order': 'sortingOrder'
        }

        self._field_name = None
        self._is_ascending = None
        self._sorting_order = None

    @property
    def field_name(self):
        """
        **[Required]** Gets the field_name of this ColumnSorting.
        Name of the column that must be sorted.


        :return: The field_name of this ColumnSorting.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this ColumnSorting.
        Name of the column that must be sorted.


        :param field_name: The field_name of this ColumnSorting.
        :type: str
        """
        self._field_name = field_name

    @property
    def is_ascending(self):
        """
        **[Required]** Gets the is_ascending of this ColumnSorting.
        Indicates if the column must be sorted in ascending order. Values can either be 'true' or 'false'.


        :return: The is_ascending of this ColumnSorting.
        :rtype: bool
        """
        return self._is_ascending

    @is_ascending.setter
    def is_ascending(self, is_ascending):
        """
        Sets the is_ascending of this ColumnSorting.
        Indicates if the column must be sorted in ascending order. Values can either be 'true' or 'false'.


        :param is_ascending: The is_ascending of this ColumnSorting.
        :type: bool
        """
        self._is_ascending = is_ascending

    @property
    def sorting_order(self):
        """
        **[Required]** Gets the sorting_order of this ColumnSorting.
        Indicates the order at which column must be sorted.


        :return: The sorting_order of this ColumnSorting.
        :rtype: int
        """
        return self._sorting_order

    @sorting_order.setter
    def sorting_order(self, sorting_order):
        """
        Sets the sorting_order of this ColumnSorting.
        Indicates the order at which column must be sorted.


        :param sorting_order: The sorting_order of this ColumnSorting.
        :type: int
        """
        self._sorting_order = sorting_order

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
