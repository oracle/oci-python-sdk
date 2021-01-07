# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_data_asset_details import CreateDataAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataAssetFromAtp(CreateDataAssetDetails):
    """
    Details for the Autonomous Transaction Processing data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataAssetFromAtp object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateDataAssetFromAtp.model_type` attribute
        of this class is ``ORACLE_ATP_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateDataAssetFromAtp.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateDataAssetFromAtp.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateDataAssetFromAtp.
        :type model_version: str

        :param name:
            The value to assign to the name property of this CreateDataAssetFromAtp.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateDataAssetFromAtp.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateDataAssetFromAtp.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateDataAssetFromAtp.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this CreateDataAssetFromAtp.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this CreateDataAssetFromAtp.
        :type asset_properties: dict(str, str)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateDataAssetFromAtp.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param service_name:
            The value to assign to the service_name property of this CreateDataAssetFromAtp.
        :type service_name: str

        :param driver_class:
            The value to assign to the driver_class property of this CreateDataAssetFromAtp.
        :type driver_class: str

        :param credential_file_content:
            The value to assign to the credential_file_content property of this CreateDataAssetFromAtp.
        :type credential_file_content: str

        :param default_connection:
            The value to assign to the default_connection property of this CreateDataAssetFromAtp.
        :type default_connection: oci.data_integration.models.CreateConnectionFromAtp

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'registry_metadata': 'RegistryMetadata',
            'service_name': 'str',
            'driver_class': 'str',
            'credential_file_content': 'str',
            'default_connection': 'CreateConnectionFromAtp'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'registry_metadata': 'registryMetadata',
            'service_name': 'serviceName',
            'driver_class': 'driverClass',
            'credential_file_content': 'credentialFileContent',
            'default_connection': 'defaultConnection'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._registry_metadata = None
        self._service_name = None
        self._driver_class = None
        self._credential_file_content = None
        self._default_connection = None
        self._model_type = 'ORACLE_ATP_DATA_ASSET'

    @property
    def service_name(self):
        """
        Gets the service_name of this CreateDataAssetFromAtp.
        The Autonomous Transaction Processing instance service name.


        :return: The service_name of this CreateDataAssetFromAtp.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this CreateDataAssetFromAtp.
        The Autonomous Transaction Processing instance service name.


        :param service_name: The service_name of this CreateDataAssetFromAtp.
        :type: str
        """
        self._service_name = service_name

    @property
    def driver_class(self):
        """
        Gets the driver_class of this CreateDataAssetFromAtp.
        The Autonomous Transaction Processing driver class.


        :return: The driver_class of this CreateDataAssetFromAtp.
        :rtype: str
        """
        return self._driver_class

    @driver_class.setter
    def driver_class(self, driver_class):
        """
        Sets the driver_class of this CreateDataAssetFromAtp.
        The Autonomous Transaction Processing driver class.


        :param driver_class: The driver_class of this CreateDataAssetFromAtp.
        :type: str
        """
        self._driver_class = driver_class

    @property
    def credential_file_content(self):
        """
        Gets the credential_file_content of this CreateDataAssetFromAtp.
        The credential file content from an Autonomous Transaction Processing wallet.


        :return: The credential_file_content of this CreateDataAssetFromAtp.
        :rtype: str
        """
        return self._credential_file_content

    @credential_file_content.setter
    def credential_file_content(self, credential_file_content):
        """
        Sets the credential_file_content of this CreateDataAssetFromAtp.
        The credential file content from an Autonomous Transaction Processing wallet.


        :param credential_file_content: The credential_file_content of this CreateDataAssetFromAtp.
        :type: str
        """
        self._credential_file_content = credential_file_content

    @property
    def default_connection(self):
        """
        Gets the default_connection of this CreateDataAssetFromAtp.

        :return: The default_connection of this CreateDataAssetFromAtp.
        :rtype: oci.data_integration.models.CreateConnectionFromAtp
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this CreateDataAssetFromAtp.

        :param default_connection: The default_connection of this CreateDataAssetFromAtp.
        :type: oci.data_integration.models.CreateConnectionFromAtp
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
