# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataPreviewDetails(object):
    """
    The data preview request payload.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataPreviewDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param read_operation_config:
            The value to assign to the read_operation_config property of this CreateDataPreviewDetails.
        :type read_operation_config: oci.data_connectivity.models.ReadOperationConfig

        :param data_asset:
            The value to assign to the data_asset property of this CreateDataPreviewDetails.
        :type data_asset: oci.data_connectivity.models.DataAsset

        :param connection:
            The value to assign to the connection property of this CreateDataPreviewDetails.
        :type connection: oci.data_connectivity.models.Connection

        :param schema:
            The value to assign to the schema property of this CreateDataPreviewDetails.
        :type schema: oci.data_connectivity.models.Schema

        :param data_entity:
            The value to assign to the data_entity property of this CreateDataPreviewDetails.
        :type data_entity: oci.data_connectivity.models.DataEntity

        """
        self.swagger_types = {
            'read_operation_config': 'ReadOperationConfig',
            'data_asset': 'DataAsset',
            'connection': 'Connection',
            'schema': 'Schema',
            'data_entity': 'DataEntity'
        }

        self.attribute_map = {
            'read_operation_config': 'readOperationConfig',
            'data_asset': 'dataAsset',
            'connection': 'connection',
            'schema': 'schema',
            'data_entity': 'dataEntity'
        }

        self._read_operation_config = None
        self._data_asset = None
        self._connection = None
        self._schema = None
        self._data_entity = None

    @property
    def read_operation_config(self):
        """
        Gets the read_operation_config of this CreateDataPreviewDetails.

        :return: The read_operation_config of this CreateDataPreviewDetails.
        :rtype: oci.data_connectivity.models.ReadOperationConfig
        """
        return self._read_operation_config

    @read_operation_config.setter
    def read_operation_config(self, read_operation_config):
        """
        Sets the read_operation_config of this CreateDataPreviewDetails.

        :param read_operation_config: The read_operation_config of this CreateDataPreviewDetails.
        :type: oci.data_connectivity.models.ReadOperationConfig
        """
        self._read_operation_config = read_operation_config

    @property
    def data_asset(self):
        """
        Gets the data_asset of this CreateDataPreviewDetails.

        :return: The data_asset of this CreateDataPreviewDetails.
        :rtype: oci.data_connectivity.models.DataAsset
        """
        return self._data_asset

    @data_asset.setter
    def data_asset(self, data_asset):
        """
        Sets the data_asset of this CreateDataPreviewDetails.

        :param data_asset: The data_asset of this CreateDataPreviewDetails.
        :type: oci.data_connectivity.models.DataAsset
        """
        self._data_asset = data_asset

    @property
    def connection(self):
        """
        Gets the connection of this CreateDataPreviewDetails.

        :return: The connection of this CreateDataPreviewDetails.
        :rtype: oci.data_connectivity.models.Connection
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this CreateDataPreviewDetails.

        :param connection: The connection of this CreateDataPreviewDetails.
        :type: oci.data_connectivity.models.Connection
        """
        self._connection = connection

    @property
    def schema(self):
        """
        Gets the schema of this CreateDataPreviewDetails.

        :return: The schema of this CreateDataPreviewDetails.
        :rtype: oci.data_connectivity.models.Schema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this CreateDataPreviewDetails.

        :param schema: The schema of this CreateDataPreviewDetails.
        :type: oci.data_connectivity.models.Schema
        """
        self._schema = schema

    @property
    def data_entity(self):
        """
        Gets the data_entity of this CreateDataPreviewDetails.

        :return: The data_entity of this CreateDataPreviewDetails.
        :rtype: oci.data_connectivity.models.DataEntity
        """
        return self._data_entity

    @data_entity.setter
    def data_entity(self, data_entity):
        """
        Sets the data_entity of this CreateDataPreviewDetails.

        :param data_entity: The data_entity of this CreateDataPreviewDetails.
        :type: oci.data_connectivity.models.DataEntity
        """
        self._data_entity = data_entity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
