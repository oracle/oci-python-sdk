# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataProfileDetails(object):
    """
    The data profile payload.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataProfileDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param read_operation_config:
            The value to assign to the read_operation_config property of this CreateDataProfileDetails.
        :type read_operation_config: oci.data_connectivity.models.ReadOperationConfig

        :param data_asset:
            The value to assign to the data_asset property of this CreateDataProfileDetails.
        :type data_asset: oci.data_connectivity.models.DataAsset

        :param connection:
            The value to assign to the connection property of this CreateDataProfileDetails.
        :type connection: oci.data_connectivity.models.Connection

        :param schema:
            The value to assign to the schema property of this CreateDataProfileDetails.
        :type schema: oci.data_connectivity.models.Schema

        :param data_entity:
            The value to assign to the data_entity property of this CreateDataProfileDetails.
        :type data_entity: oci.data_connectivity.models.DataEntity

        :param profile_config:
            The value to assign to the profile_config property of this CreateDataProfileDetails.
        :type profile_config: oci.data_connectivity.models.ProfileConfig

        """
        self.swagger_types = {
            'read_operation_config': 'ReadOperationConfig',
            'data_asset': 'DataAsset',
            'connection': 'Connection',
            'schema': 'Schema',
            'data_entity': 'DataEntity',
            'profile_config': 'ProfileConfig'
        }

        self.attribute_map = {
            'read_operation_config': 'readOperationConfig',
            'data_asset': 'dataAsset',
            'connection': 'connection',
            'schema': 'schema',
            'data_entity': 'dataEntity',
            'profile_config': 'profileConfig'
        }

        self._read_operation_config = None
        self._data_asset = None
        self._connection = None
        self._schema = None
        self._data_entity = None
        self._profile_config = None

    @property
    def read_operation_config(self):
        """
        Gets the read_operation_config of this CreateDataProfileDetails.

        :return: The read_operation_config of this CreateDataProfileDetails.
        :rtype: oci.data_connectivity.models.ReadOperationConfig
        """
        return self._read_operation_config

    @read_operation_config.setter
    def read_operation_config(self, read_operation_config):
        """
        Sets the read_operation_config of this CreateDataProfileDetails.

        :param read_operation_config: The read_operation_config of this CreateDataProfileDetails.
        :type: oci.data_connectivity.models.ReadOperationConfig
        """
        self._read_operation_config = read_operation_config

    @property
    def data_asset(self):
        """
        Gets the data_asset of this CreateDataProfileDetails.

        :return: The data_asset of this CreateDataProfileDetails.
        :rtype: oci.data_connectivity.models.DataAsset
        """
        return self._data_asset

    @data_asset.setter
    def data_asset(self, data_asset):
        """
        Sets the data_asset of this CreateDataProfileDetails.

        :param data_asset: The data_asset of this CreateDataProfileDetails.
        :type: oci.data_connectivity.models.DataAsset
        """
        self._data_asset = data_asset

    @property
    def connection(self):
        """
        Gets the connection of this CreateDataProfileDetails.

        :return: The connection of this CreateDataProfileDetails.
        :rtype: oci.data_connectivity.models.Connection
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this CreateDataProfileDetails.

        :param connection: The connection of this CreateDataProfileDetails.
        :type: oci.data_connectivity.models.Connection
        """
        self._connection = connection

    @property
    def schema(self):
        """
        Gets the schema of this CreateDataProfileDetails.

        :return: The schema of this CreateDataProfileDetails.
        :rtype: oci.data_connectivity.models.Schema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this CreateDataProfileDetails.

        :param schema: The schema of this CreateDataProfileDetails.
        :type: oci.data_connectivity.models.Schema
        """
        self._schema = schema

    @property
    def data_entity(self):
        """
        Gets the data_entity of this CreateDataProfileDetails.

        :return: The data_entity of this CreateDataProfileDetails.
        :rtype: oci.data_connectivity.models.DataEntity
        """
        return self._data_entity

    @data_entity.setter
    def data_entity(self, data_entity):
        """
        Sets the data_entity of this CreateDataProfileDetails.

        :param data_entity: The data_entity of this CreateDataProfileDetails.
        :type: oci.data_connectivity.models.DataEntity
        """
        self._data_entity = data_entity

    @property
    def profile_config(self):
        """
        Gets the profile_config of this CreateDataProfileDetails.

        :return: The profile_config of this CreateDataProfileDetails.
        :rtype: oci.data_connectivity.models.ProfileConfig
        """
        return self._profile_config

    @profile_config.setter
    def profile_config(self, profile_config):
        """
        Sets the profile_config of this CreateDataProfileDetails.

        :param profile_config: The profile_config of this CreateDataProfileDetails.
        :type: oci.data_connectivity.models.ProfileConfig
        """
        self._profile_config = profile_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
