# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_data_asset_details import CreateDataAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataAssetFromAdwc(CreateDataAssetDetails):
    """
    Details for the Autonomous Data Warehouse data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataAssetFromAdwc object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateDataAssetFromAdwc.model_type` attribute
        of this class is ``ORACLE_ADWC_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateDataAssetFromAdwc.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateDataAssetFromAdwc.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateDataAssetFromAdwc.
        :type model_version: str

        :param name:
            The value to assign to the name property of this CreateDataAssetFromAdwc.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateDataAssetFromAdwc.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateDataAssetFromAdwc.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateDataAssetFromAdwc.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this CreateDataAssetFromAdwc.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this CreateDataAssetFromAdwc.
        :type asset_properties: dict(str, str)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateDataAssetFromAdwc.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param service_name:
            The value to assign to the service_name property of this CreateDataAssetFromAdwc.
        :type service_name: str

        :param driver_class:
            The value to assign to the driver_class property of this CreateDataAssetFromAdwc.
        :type driver_class: str

        :param credential_file_content:
            The value to assign to the credential_file_content property of this CreateDataAssetFromAdwc.
        :type credential_file_content: str

        :param wallet_secret:
            The value to assign to the wallet_secret property of this CreateDataAssetFromAdwc.
        :type wallet_secret: oci.data_integration.models.SensitiveAttribute

        :param wallet_password_secret:
            The value to assign to the wallet_password_secret property of this CreateDataAssetFromAdwc.
        :type wallet_password_secret: oci.data_integration.models.SensitiveAttribute

        :param region_id:
            The value to assign to the region_id property of this CreateDataAssetFromAdwc.
        :type region_id: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this CreateDataAssetFromAdwc.
        :type tenancy_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDataAssetFromAdwc.
        :type compartment_id: str

        :param autonomous_db_id:
            The value to assign to the autonomous_db_id property of this CreateDataAssetFromAdwc.
        :type autonomous_db_id: str

        :param default_connection:
            The value to assign to the default_connection property of this CreateDataAssetFromAdwc.
        :type default_connection: oci.data_integration.models.CreateConnectionFromAdwc

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
            'wallet_secret': 'SensitiveAttribute',
            'wallet_password_secret': 'SensitiveAttribute',
            'region_id': 'str',
            'tenancy_id': 'str',
            'compartment_id': 'str',
            'autonomous_db_id': 'str',
            'default_connection': 'CreateConnectionFromAdwc'
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
            'wallet_secret': 'walletSecret',
            'wallet_password_secret': 'walletPasswordSecret',
            'region_id': 'regionId',
            'tenancy_id': 'tenancyId',
            'compartment_id': 'compartmentId',
            'autonomous_db_id': 'autonomousDbId',
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
        self._wallet_secret = None
        self._wallet_password_secret = None
        self._region_id = None
        self._tenancy_id = None
        self._compartment_id = None
        self._autonomous_db_id = None
        self._default_connection = None
        self._model_type = 'ORACLE_ADWC_DATA_ASSET'

    @property
    def service_name(self):
        """
        Gets the service_name of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse instance service name.


        :return: The service_name of this CreateDataAssetFromAdwc.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse instance service name.


        :param service_name: The service_name of this CreateDataAssetFromAdwc.
        :type: str
        """
        self._service_name = service_name

    @property
    def driver_class(self):
        """
        Gets the driver_class of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse driver class.


        :return: The driver_class of this CreateDataAssetFromAdwc.
        :rtype: str
        """
        return self._driver_class

    @driver_class.setter
    def driver_class(self, driver_class):
        """
        Sets the driver_class of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse driver class.


        :param driver_class: The driver_class of this CreateDataAssetFromAdwc.
        :type: str
        """
        self._driver_class = driver_class

    @property
    def credential_file_content(self):
        """
        Gets the credential_file_content of this CreateDataAssetFromAdwc.
        The credential file content from a Autonomous Data Warehouse wallet.


        :return: The credential_file_content of this CreateDataAssetFromAdwc.
        :rtype: str
        """
        return self._credential_file_content

    @credential_file_content.setter
    def credential_file_content(self, credential_file_content):
        """
        Sets the credential_file_content of this CreateDataAssetFromAdwc.
        The credential file content from a Autonomous Data Warehouse wallet.


        :param credential_file_content: The credential_file_content of this CreateDataAssetFromAdwc.
        :type: str
        """
        self._credential_file_content = credential_file_content

    @property
    def wallet_secret(self):
        """
        Gets the wallet_secret of this CreateDataAssetFromAdwc.

        :return: The wallet_secret of this CreateDataAssetFromAdwc.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._wallet_secret

    @wallet_secret.setter
    def wallet_secret(self, wallet_secret):
        """
        Sets the wallet_secret of this CreateDataAssetFromAdwc.

        :param wallet_secret: The wallet_secret of this CreateDataAssetFromAdwc.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._wallet_secret = wallet_secret

    @property
    def wallet_password_secret(self):
        """
        Gets the wallet_password_secret of this CreateDataAssetFromAdwc.

        :return: The wallet_password_secret of this CreateDataAssetFromAdwc.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._wallet_password_secret

    @wallet_password_secret.setter
    def wallet_password_secret(self, wallet_password_secret):
        """
        Sets the wallet_password_secret of this CreateDataAssetFromAdwc.

        :param wallet_password_secret: The wallet_password_secret of this CreateDataAssetFromAdwc.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._wallet_password_secret = wallet_password_secret

    @property
    def region_id(self):
        """
        Gets the region_id of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse instance region Id.


        :return: The region_id of this CreateDataAssetFromAdwc.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse instance region Id.


        :param region_id: The region_id of this CreateDataAssetFromAdwc.
        :type: str
        """
        self._region_id = region_id

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse instance tenancy Id.


        :return: The tenancy_id of this CreateDataAssetFromAdwc.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse instance tenancy Id.


        :param tenancy_id: The tenancy_id of this CreateDataAssetFromAdwc.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse instance compartment Id.


        :return: The compartment_id of this CreateDataAssetFromAdwc.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDataAssetFromAdwc.
        The Autonomous Data Warehouse instance compartment Id.


        :param compartment_id: The compartment_id of this CreateDataAssetFromAdwc.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def autonomous_db_id(self):
        """
        Gets the autonomous_db_id of this CreateDataAssetFromAdwc.
        Tha Autonomous Database Id


        :return: The autonomous_db_id of this CreateDataAssetFromAdwc.
        :rtype: str
        """
        return self._autonomous_db_id

    @autonomous_db_id.setter
    def autonomous_db_id(self, autonomous_db_id):
        """
        Sets the autonomous_db_id of this CreateDataAssetFromAdwc.
        Tha Autonomous Database Id


        :param autonomous_db_id: The autonomous_db_id of this CreateDataAssetFromAdwc.
        :type: str
        """
        self._autonomous_db_id = autonomous_db_id

    @property
    def default_connection(self):
        """
        Gets the default_connection of this CreateDataAssetFromAdwc.

        :return: The default_connection of this CreateDataAssetFromAdwc.
        :rtype: oci.data_integration.models.CreateConnectionFromAdwc
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this CreateDataAssetFromAdwc.

        :param default_connection: The default_connection of this CreateDataAssetFromAdwc.
        :type: oci.data_integration.models.CreateConnectionFromAdwc
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
