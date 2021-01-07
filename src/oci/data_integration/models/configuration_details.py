# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationDetails(object):
    """
    A key map. If provided, key is replaced with generated key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_asset:
            The value to assign to the data_asset property of this ConfigurationDetails.
        :type data_asset: oci.data_integration.models.DataAsset

        :param connection:
            The value to assign to the connection property of this ConfigurationDetails.
        :type connection: oci.data_integration.models.Connection

        :param compartment_id:
            The value to assign to the compartment_id property of this ConfigurationDetails.
        :type compartment_id: str

        :param schema:
            The value to assign to the schema property of this ConfigurationDetails.
        :type schema: oci.data_integration.models.Schema

        """
        self.swagger_types = {
            'data_asset': 'DataAsset',
            'connection': 'Connection',
            'compartment_id': 'str',
            'schema': 'Schema'
        }

        self.attribute_map = {
            'data_asset': 'dataAsset',
            'connection': 'connection',
            'compartment_id': 'compartmentId',
            'schema': 'schema'
        }

        self._data_asset = None
        self._connection = None
        self._compartment_id = None
        self._schema = None

    @property
    def data_asset(self):
        """
        Gets the data_asset of this ConfigurationDetails.

        :return: The data_asset of this ConfigurationDetails.
        :rtype: oci.data_integration.models.DataAsset
        """
        return self._data_asset

    @data_asset.setter
    def data_asset(self, data_asset):
        """
        Sets the data_asset of this ConfigurationDetails.

        :param data_asset: The data_asset of this ConfigurationDetails.
        :type: oci.data_integration.models.DataAsset
        """
        self._data_asset = data_asset

    @property
    def connection(self):
        """
        Gets the connection of this ConfigurationDetails.

        :return: The connection of this ConfigurationDetails.
        :rtype: oci.data_integration.models.Connection
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this ConfigurationDetails.

        :param connection: The connection of this ConfigurationDetails.
        :type: oci.data_integration.models.Connection
        """
        self._connection = connection

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ConfigurationDetails.
        The compartment ID of the object store.


        :return: The compartment_id of this ConfigurationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConfigurationDetails.
        The compartment ID of the object store.


        :param compartment_id: The compartment_id of this ConfigurationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def schema(self):
        """
        Gets the schema of this ConfigurationDetails.

        :return: The schema of this ConfigurationDetails.
        :rtype: oci.data_integration.models.Schema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this ConfigurationDetails.

        :param schema: The schema of this ConfigurationDetails.
        :type: oci.data_integration.models.Schema
        """
        self._schema = schema

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
