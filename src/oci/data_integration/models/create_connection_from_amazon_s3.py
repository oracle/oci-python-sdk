# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionFromAmazonS3(CreateConnectionDetails):
    """
    The details to create a Amazon S3 connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionFromAmazonS3 object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateConnectionFromAmazonS3.model_type` attribute
        of this class is ``AMAZON_S3_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateConnectionFromAmazonS3.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", "BIP_CONNECTION", "LAKE_HOUSE_CONNECTION", "REST_NO_AUTH_CONNECTION", "REST_BASIC_AUTH_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateConnectionFromAmazonS3.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateConnectionFromAmazonS3.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateConnectionFromAmazonS3.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateConnectionFromAmazonS3.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateConnectionFromAmazonS3.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateConnectionFromAmazonS3.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateConnectionFromAmazonS3.
        :type identifier: str

        :param connection_properties:
            The value to assign to the connection_properties property of this CreateConnectionFromAmazonS3.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateConnectionFromAmazonS3.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param access_key:
            The value to assign to the access_key property of this CreateConnectionFromAmazonS3.
        :type access_key: oci.data_integration.models.SensitiveAttribute

        :param secret_key:
            The value to assign to the secret_key property of this CreateConnectionFromAmazonS3.
        :type secret_key: oci.data_integration.models.SensitiveAttribute

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'connection_properties': 'list[ConnectionProperty]',
            'registry_metadata': 'RegistryMetadata',
            'access_key': 'SensitiveAttribute',
            'secret_key': 'SensitiveAttribute'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'connection_properties': 'connectionProperties',
            'registry_metadata': 'registryMetadata',
            'access_key': 'accessKey',
            'secret_key': 'secretKey'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._connection_properties = None
        self._registry_metadata = None
        self._access_key = None
        self._secret_key = None
        self._model_type = 'AMAZON_S3_CONNECTION'

    @property
    def access_key(self):
        """
        Gets the access_key of this CreateConnectionFromAmazonS3.

        :return: The access_key of this CreateConnectionFromAmazonS3.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """
        Sets the access_key of this CreateConnectionFromAmazonS3.

        :param access_key: The access_key of this CreateConnectionFromAmazonS3.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        """
        Gets the secret_key of this CreateConnectionFromAmazonS3.

        :return: The secret_key of this CreateConnectionFromAmazonS3.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """
        Sets the secret_key of this CreateConnectionFromAmazonS3.

        :param secret_key: The secret_key of this CreateConnectionFromAmazonS3.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._secret_key = secret_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
