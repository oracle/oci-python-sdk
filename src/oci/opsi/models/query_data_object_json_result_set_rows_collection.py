# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .query_data_object_result_set_rows_collection import QueryDataObjectResultSetRowsCollection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryDataObjectJsonResultSetRowsCollection(QueryDataObjectResultSetRowsCollection):
    """
    Collection of result set rows from the data object query.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryDataObjectJsonResultSetRowsCollection object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.QueryDataObjectJsonResultSetRowsCollection.format` attribute
        of this class is ``JSON`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format:
            The value to assign to the format property of this QueryDataObjectJsonResultSetRowsCollection.
            Allowed values for this property are: "JSON"
        :type format: str

        :param items:
            The value to assign to the items property of this QueryDataObjectJsonResultSetRowsCollection.
        :type items: list[object]

        :param items_metadata:
            The value to assign to the items_metadata property of this QueryDataObjectJsonResultSetRowsCollection.
        :type items_metadata: list[oci.opsi.models.QueryDataObjectResultSetColumnMetadata]

        """
        self.swagger_types = {
            'format': 'str',
            'items': 'list[object]',
            'items_metadata': 'list[QueryDataObjectResultSetColumnMetadata]'
        }

        self.attribute_map = {
            'format': 'format',
            'items': 'items',
            'items_metadata': 'itemsMetadata'
        }

        self._format = None
        self._items = None
        self._items_metadata = None
        self._format = 'JSON'

    @property
    def items(self):
        """
        **[Required]** Gets the items of this QueryDataObjectJsonResultSetRowsCollection.
        Array of result set rows.


        :return: The items of this QueryDataObjectJsonResultSetRowsCollection.
        :rtype: list[object]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this QueryDataObjectJsonResultSetRowsCollection.
        Array of result set rows.


        :param items: The items of this QueryDataObjectJsonResultSetRowsCollection.
        :type: list[object]
        """
        self._items = items

    @property
    def items_metadata(self):
        """
        **[Required]** Gets the items_metadata of this QueryDataObjectJsonResultSetRowsCollection.
        Array of QueryDataObjectResultSetColumnMetadata objects that describe the result set columns.


        :return: The items_metadata of this QueryDataObjectJsonResultSetRowsCollection.
        :rtype: list[oci.opsi.models.QueryDataObjectResultSetColumnMetadata]
        """
        return self._items_metadata

    @items_metadata.setter
    def items_metadata(self, items_metadata):
        """
        Sets the items_metadata of this QueryDataObjectJsonResultSetRowsCollection.
        Array of QueryDataObjectResultSetColumnMetadata objects that describe the result set columns.


        :param items_metadata: The items_metadata of this QueryDataObjectJsonResultSetRowsCollection.
        :type: list[oci.opsi.models.QueryDataObjectResultSetColumnMetadata]
        """
        self._items_metadata = items_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
