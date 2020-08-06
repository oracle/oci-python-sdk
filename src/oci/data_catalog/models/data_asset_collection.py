# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetCollection(object):
    """
    Results of a data assets listing. A data asset is often synonymous with a 'System', such as a database, or may be a file container or a message stream.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param count:
            The value to assign to the count property of this DataAssetCollection.
        :type count: int

        :param items:
            The value to assign to the items property of this DataAssetCollection.
        :type items: list[DataAssetSummary]

        """
        self.swagger_types = {
            'count': 'int',
            'items': 'list[DataAssetSummary]'
        }

        self.attribute_map = {
            'count': 'count',
            'items': 'items'
        }

        self._count = None
        self._items = None

    @property
    def count(self):
        """
        Gets the count of this DataAssetCollection.
        Total number of items returned.


        :return: The count of this DataAssetCollection.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this DataAssetCollection.
        Total number of items returned.


        :param count: The count of this DataAssetCollection.
        :type: int
        """
        self._count = count

    @property
    def items(self):
        """
        **[Required]** Gets the items of this DataAssetCollection.
        Collection of data asset summaries.


        :return: The items of this DataAssetCollection.
        :rtype: list[DataAssetSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this DataAssetCollection.
        Collection of data asset summaries.


        :param items: The items of this DataAssetCollection.
        :type: list[DataAssetSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
