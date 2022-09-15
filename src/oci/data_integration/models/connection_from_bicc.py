# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionFromBICC(Connection):
    """
    The connection details for a FUSION_APP BICC Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionFromBICC object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.ConnectionFromBICC.model_type` attribute
        of this class is ``BICC_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ConnectionFromBICC.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", "BIP_CONNECTION", "LAKE_HOUSE_CONNECTION", "REST_NO_AUTH_CONNECTION", "REST_BASIC_AUTH_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this ConnectionFromBICC.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ConnectionFromBICC.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ConnectionFromBICC.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this ConnectionFromBICC.
        :type name: str

        :param description:
            The value to assign to the description property of this ConnectionFromBICC.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this ConnectionFromBICC.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this ConnectionFromBICC.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this ConnectionFromBICC.
        :type identifier: str

        :param primary_schema:
            The value to assign to the primary_schema property of this ConnectionFromBICC.
        :type primary_schema: oci.data_integration.models.Schema

        :param connection_properties:
            The value to assign to the connection_properties property of this ConnectionFromBICC.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param is_default:
            The value to assign to the is_default property of this ConnectionFromBICC.
        :type is_default: bool

        :param metadata:
            The value to assign to the metadata property of this ConnectionFromBICC.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this ConnectionFromBICC.
        :type key_map: dict(str, str)

        :param username:
            The value to assign to the username property of this ConnectionFromBICC.
        :type username: str

        :param password_secret:
            The value to assign to the password_secret property of this ConnectionFromBICC.
        :type password_secret: oci.data_integration.models.SensitiveAttribute

        :param default_external_storage:
            The value to assign to the default_external_storage property of this ConnectionFromBICC.
        :type default_external_storage: oci.data_integration.models.ExternalStorage

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'primary_schema': 'Schema',
            'connection_properties': 'list[ConnectionProperty]',
            'is_default': 'bool',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)',
            'username': 'str',
            'password_secret': 'SensitiveAttribute',
            'default_external_storage': 'ExternalStorage'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'primary_schema': 'primarySchema',
            'connection_properties': 'connectionProperties',
            'is_default': 'isDefault',
            'metadata': 'metadata',
            'key_map': 'keyMap',
            'username': 'username',
            'password_secret': 'passwordSecret',
            'default_external_storage': 'defaultExternalStorage'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._primary_schema = None
        self._connection_properties = None
        self._is_default = None
        self._metadata = None
        self._key_map = None
        self._username = None
        self._password_secret = None
        self._default_external_storage = None
        self._model_type = 'BICC_CONNECTION'

    @property
    def username(self):
        """
        Gets the username of this ConnectionFromBICC.
        The user name for the connection.


        :return: The username of this ConnectionFromBICC.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ConnectionFromBICC.
        The user name for the connection.


        :param username: The username of this ConnectionFromBICC.
        :type: str
        """
        self._username = username

    @property
    def password_secret(self):
        """
        Gets the password_secret of this ConnectionFromBICC.

        :return: The password_secret of this ConnectionFromBICC.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._password_secret

    @password_secret.setter
    def password_secret(self, password_secret):
        """
        Sets the password_secret of this ConnectionFromBICC.

        :param password_secret: The password_secret of this ConnectionFromBICC.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._password_secret = password_secret

    @property
    def default_external_storage(self):
        """
        Gets the default_external_storage of this ConnectionFromBICC.

        :return: The default_external_storage of this ConnectionFromBICC.
        :rtype: oci.data_integration.models.ExternalStorage
        """
        return self._default_external_storage

    @default_external_storage.setter
    def default_external_storage(self, default_external_storage):
        """
        Sets the default_external_storage of this ConnectionFromBICC.

        :param default_external_storage: The default_external_storage of this ConnectionFromBICC.
        :type: oci.data_integration.models.ExternalStorage
        """
        self._default_external_storage = default_external_storage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
