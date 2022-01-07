# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_data_asset_details import UpdateDataAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDataAssetFromJdbc(UpdateDataAssetDetails):
    """
    Details for the Autonomous Transaction Processing data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDataAssetFromJdbc object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.UpdateDataAssetFromJdbc.model_type` attribute
        of this class is ``GENERIC_JDBC_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this UpdateDataAssetFromJdbc.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this UpdateDataAssetFromJdbc.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this UpdateDataAssetFromJdbc.
        :type model_version: str

        :param name:
            The value to assign to the name property of this UpdateDataAssetFromJdbc.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateDataAssetFromJdbc.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UpdateDataAssetFromJdbc.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this UpdateDataAssetFromJdbc.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this UpdateDataAssetFromJdbc.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this UpdateDataAssetFromJdbc.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this UpdateDataAssetFromJdbc.
        :type asset_properties: dict(str, str)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateDataAssetFromJdbc.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param host:
            The value to assign to the host property of this UpdateDataAssetFromJdbc.
        :type host: str

        :param port:
            The value to assign to the port property of this UpdateDataAssetFromJdbc.
        :type port: str

        :param data_asset_type:
            The value to assign to the data_asset_type property of this UpdateDataAssetFromJdbc.
        :type data_asset_type: str

        :param default_connection:
            The value to assign to the default_connection property of this UpdateDataAssetFromJdbc.
        :type default_connection: oci.data_integration.models.UpdateConnectionFromJdbc

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'registry_metadata': 'RegistryMetadata',
            'host': 'str',
            'port': 'str',
            'data_asset_type': 'str',
            'default_connection': 'UpdateConnectionFromJdbc'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'registry_metadata': 'registryMetadata',
            'host': 'host',
            'port': 'port',
            'data_asset_type': 'dataAssetType',
            'default_connection': 'defaultConnection'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._registry_metadata = None
        self._host = None
        self._port = None
        self._data_asset_type = None
        self._default_connection = None
        self._model_type = 'GENERIC_JDBC_DATA_ASSET'

    @property
    def host(self):
        """
        Gets the host of this UpdateDataAssetFromJdbc.
        The generic JDBC host name.


        :return: The host of this UpdateDataAssetFromJdbc.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this UpdateDataAssetFromJdbc.
        The generic JDBC host name.


        :param host: The host of this UpdateDataAssetFromJdbc.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this UpdateDataAssetFromJdbc.
        The generic JDBC port number.


        :return: The port of this UpdateDataAssetFromJdbc.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateDataAssetFromJdbc.
        The generic JDBC port number.


        :param port: The port of this UpdateDataAssetFromJdbc.
        :type: str
        """
        self._port = port

    @property
    def data_asset_type(self):
        """
        Gets the data_asset_type of this UpdateDataAssetFromJdbc.
        The data asset type for the generic JDBC data asset.


        :return: The data_asset_type of this UpdateDataAssetFromJdbc.
        :rtype: str
        """
        return self._data_asset_type

    @data_asset_type.setter
    def data_asset_type(self, data_asset_type):
        """
        Sets the data_asset_type of this UpdateDataAssetFromJdbc.
        The data asset type for the generic JDBC data asset.


        :param data_asset_type: The data_asset_type of this UpdateDataAssetFromJdbc.
        :type: str
        """
        self._data_asset_type = data_asset_type

    @property
    def default_connection(self):
        """
        Gets the default_connection of this UpdateDataAssetFromJdbc.

        :return: The default_connection of this UpdateDataAssetFromJdbc.
        :rtype: oci.data_integration.models.UpdateConnectionFromJdbc
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this UpdateDataAssetFromJdbc.

        :param default_connection: The default_connection of this UpdateDataAssetFromJdbc.
        :type: oci.data_integration.models.UpdateConnectionFromJdbc
        """
        self._default_connection = default_connection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
