# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Type(object):
    """
    DataAsset and Connection Registry Attributes
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Type object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_asset_attributes:
            The value to assign to the data_asset_attributes property of this Type.
        :type data_asset_attributes: list[oci.data_connectivity.models.Attribute]

        :param connection_attributes:
            The value to assign to the connection_attributes property of this Type.
        :type connection_attributes: dict(str, list[Attribute])

        """
        self.swagger_types = {
            'data_asset_attributes': 'list[Attribute]',
            'connection_attributes': 'dict(str, list[Attribute])'
        }

        self.attribute_map = {
            'data_asset_attributes': 'dataAssetAttributes',
            'connection_attributes': 'connectionAttributes'
        }

        self._data_asset_attributes = None
        self._connection_attributes = None

    @property
    def data_asset_attributes(self):
        """
        **[Required]** Gets the data_asset_attributes of this Type.
        The list of attributes of the data asset.


        :return: The data_asset_attributes of this Type.
        :rtype: list[oci.data_connectivity.models.Attribute]
        """
        return self._data_asset_attributes

    @data_asset_attributes.setter
    def data_asset_attributes(self, data_asset_attributes):
        """
        Sets the data_asset_attributes of this Type.
        The list of attributes of the data asset.


        :param data_asset_attributes: The data_asset_attributes of this Type.
        :type: list[oci.data_connectivity.models.Attribute]
        """
        self._data_asset_attributes = data_asset_attributes

    @property
    def connection_attributes(self):
        """
        **[Required]** Gets the connection_attributes of this Type.
        Mapping the connectionType as the key to the list of attributes as the value.


        :return: The connection_attributes of this Type.
        :rtype: dict(str, list[Attribute])
        """
        return self._connection_attributes

    @connection_attributes.setter
    def connection_attributes(self, connection_attributes):
        """
        Sets the connection_attributes of this Type.
        Mapping the connectionType as the key to the list of attributes as the value.


        :param connection_attributes: The connection_attributes of this Type.
        :type: dict(str, list[Attribute])
        """
        self._connection_attributes = connection_attributes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
