# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryResultCollection(object):
    """
    The result of a query.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryResultCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this QueryResultCollection.
        :type items: list[dict(str, object)]

        :param usage:
            The value to assign to the usage property of this QueryResultCollection.
        :type usage: RequestUsage

        """
        self.swagger_types = {
            'items': 'list[dict(str, object)]',
            'usage': 'RequestUsage'
        }

        self.attribute_map = {
            'items': 'items',
            'usage': 'usage'
        }

        self._items = None
        self._usage = None

    @property
    def items(self):
        """
        Gets the items of this QueryResultCollection.
        Array of objects representing query results.


        :return: The items of this QueryResultCollection.
        :rtype: list[dict(str, object)]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this QueryResultCollection.
        Array of objects representing query results.


        :param items: The items of this QueryResultCollection.
        :type: list[dict(str, object)]
        """
        self._items = items

    @property
    def usage(self):
        """
        Gets the usage of this QueryResultCollection.

        :return: The usage of this QueryResultCollection.
        :rtype: RequestUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this QueryResultCollection.

        :param usage: The usage of this QueryResultCollection.
        :type: RequestUsage
        """
        self._usage = usage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
