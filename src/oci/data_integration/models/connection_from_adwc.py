# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionFromAdwc(Connection):
    """
    The connection details for an Autonomous Data Warehouse data asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionFromAdwc object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.ConnectionFromAdwc.model_type` attribute
        of this class is ``ORACLE_ADWC_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ConnectionFromAdwc.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", "BIP_CONNECTION", "LAKE_HOUSE_CONNECTION", "REST_NO_AUTH_CONNECTION", "REST_BASIC_AUTH_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this ConnectionFromAdwc.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ConnectionFromAdwc.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ConnectionFromAdwc.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this ConnectionFromAdwc.
        :type name: str

        :param description:
            The value to assign to the description property of this ConnectionFromAdwc.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this ConnectionFromAdwc.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this ConnectionFromAdwc.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this ConnectionFromAdwc.
        :type identifier: str

        :param primary_schema:
            The value to assign to the primary_schema property of this ConnectionFromAdwc.
        :type primary_schema: oci.data_integration.models.Schema

        :param connection_properties:
            The value to assign to the connection_properties property of this ConnectionFromAdwc.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param is_default:
            The value to assign to the is_default property of this ConnectionFromAdwc.
        :type is_default: bool

        :param metadata:
            The value to assign to the metadata property of this ConnectionFromAdwc.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this ConnectionFromAdwc.
        :type key_map: dict(str, str)

        :param tns_alias:
            The value to assign to the tns_alias property of this ConnectionFromAdwc.
        :type tns_alias: str

        :param tns_names:
            The value to assign to the tns_names property of this ConnectionFromAdwc.
        :type tns_names: list[str]

        :param username:
            The value to assign to the username property of this ConnectionFromAdwc.
        :type username: str

        :param password:
            The value to assign to the password property of this ConnectionFromAdwc.
        :type password: str

        :param password_secret:
            The value to assign to the password_secret property of this ConnectionFromAdwc.
        :type password_secret: oci.data_integration.models.SensitiveAttribute

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
            'tns_alias': 'str',
            'tns_names': 'list[str]',
            'username': 'str',
            'password': 'str',
            'password_secret': 'SensitiveAttribute'
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
            'tns_alias': 'tnsAlias',
            'tns_names': 'tnsNames',
            'username': 'username',
            'password': 'password',
            'password_secret': 'passwordSecret'
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
        self._tns_alias = None
        self._tns_names = None
        self._username = None
        self._password = None
        self._password_secret = None
        self._model_type = 'ORACLE_ADWC_CONNECTION'

    @property
    def tns_alias(self):
        """
        Gets the tns_alias of this ConnectionFromAdwc.
        The Autonomous Data Warehouse instance service name.


        :return: The tns_alias of this ConnectionFromAdwc.
        :rtype: str
        """
        return self._tns_alias

    @tns_alias.setter
    def tns_alias(self, tns_alias):
        """
        Sets the tns_alias of this ConnectionFromAdwc.
        The Autonomous Data Warehouse instance service name.


        :param tns_alias: The tns_alias of this ConnectionFromAdwc.
        :type: str
        """
        self._tns_alias = tns_alias

    @property
    def tns_names(self):
        """
        Gets the tns_names of this ConnectionFromAdwc.
        Array of service names that are available for selection in the tnsAlias property.


        :return: The tns_names of this ConnectionFromAdwc.
        :rtype: list[str]
        """
        return self._tns_names

    @tns_names.setter
    def tns_names(self, tns_names):
        """
        Sets the tns_names of this ConnectionFromAdwc.
        Array of service names that are available for selection in the tnsAlias property.


        :param tns_names: The tns_names of this ConnectionFromAdwc.
        :type: list[str]
        """
        self._tns_names = tns_names

    @property
    def username(self):
        """
        Gets the username of this ConnectionFromAdwc.
        The user name for the connection.


        :return: The username of this ConnectionFromAdwc.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ConnectionFromAdwc.
        The user name for the connection.


        :param username: The username of this ConnectionFromAdwc.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this ConnectionFromAdwc.
        The password for the connection.


        :return: The password of this ConnectionFromAdwc.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ConnectionFromAdwc.
        The password for the connection.


        :param password: The password of this ConnectionFromAdwc.
        :type: str
        """
        self._password = password

    @property
    def password_secret(self):
        """
        Gets the password_secret of this ConnectionFromAdwc.

        :return: The password_secret of this ConnectionFromAdwc.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._password_secret

    @password_secret.setter
    def password_secret(self, password_secret):
        """
        Sets the password_secret of this ConnectionFromAdwc.

        :param password_secret: The password_secret of this ConnectionFromAdwc.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._password_secret = password_secret

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
