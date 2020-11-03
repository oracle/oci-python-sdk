# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TableCollection(object):
    """
    Results of ListTables.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TableCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this TableCollection.
        :type items: list[TableSummary]

        :param max_auto_reclaimable_tables:
            The value to assign to the max_auto_reclaimable_tables property of this TableCollection.
        :type max_auto_reclaimable_tables: int

        :param auto_reclaimable_tables:
            The value to assign to the auto_reclaimable_tables property of this TableCollection.
        :type auto_reclaimable_tables: int

        """
        self.swagger_types = {
            'items': 'list[TableSummary]',
            'max_auto_reclaimable_tables': 'int',
            'auto_reclaimable_tables': 'int'
        }

        self.attribute_map = {
            'items': 'items',
            'max_auto_reclaimable_tables': 'maxAutoReclaimableTables',
            'auto_reclaimable_tables': 'autoReclaimableTables'
        }

        self._items = None
        self._max_auto_reclaimable_tables = None
        self._auto_reclaimable_tables = None

    @property
    def items(self):
        """
        Gets the items of this TableCollection.
        A page of TableSummary objects.


        :return: The items of this TableCollection.
        :rtype: list[TableSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this TableCollection.
        A page of TableSummary objects.


        :param items: The items of this TableCollection.
        :type: list[TableSummary]
        """
        self._items = items

    @property
    def max_auto_reclaimable_tables(self):
        """
        Gets the max_auto_reclaimable_tables of this TableCollection.
        The maximum number of reclaimable tables allowed in the tenancy.


        :return: The max_auto_reclaimable_tables of this TableCollection.
        :rtype: int
        """
        return self._max_auto_reclaimable_tables

    @max_auto_reclaimable_tables.setter
    def max_auto_reclaimable_tables(self, max_auto_reclaimable_tables):
        """
        Sets the max_auto_reclaimable_tables of this TableCollection.
        The maximum number of reclaimable tables allowed in the tenancy.


        :param max_auto_reclaimable_tables: The max_auto_reclaimable_tables of this TableCollection.
        :type: int
        """
        self._max_auto_reclaimable_tables = max_auto_reclaimable_tables

    @property
    def auto_reclaimable_tables(self):
        """
        Gets the auto_reclaimable_tables of this TableCollection.
        The current number of reclaimable tables in the tenancy.


        :return: The auto_reclaimable_tables of this TableCollection.
        :rtype: int
        """
        return self._auto_reclaimable_tables

    @auto_reclaimable_tables.setter
    def auto_reclaimable_tables(self, auto_reclaimable_tables):
        """
        Sets the auto_reclaimable_tables of this TableCollection.
        The current number of reclaimable tables in the tenancy.


        :param auto_reclaimable_tables: The auto_reclaimable_tables of this TableCollection.
        :type: int
        """
        self._auto_reclaimable_tables = auto_reclaimable_tables

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
