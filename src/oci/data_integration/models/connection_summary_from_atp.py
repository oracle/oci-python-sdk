# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection_summary import ConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionSummaryFromAtp(ConnectionSummary):
    """
    The ATP connection details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionSummaryFromAtp object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.ConnectionSummaryFromAtp.model_type` attribute
        of this class is ``ORACLE_ATP_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ConnectionSummaryFromAtp.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this ConnectionSummaryFromAtp.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ConnectionSummaryFromAtp.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ConnectionSummaryFromAtp.
        :type parent_ref: ParentReference

        :param name:
            The value to assign to the name property of this ConnectionSummaryFromAtp.
        :type name: str

        :param description:
            The value to assign to the description property of this ConnectionSummaryFromAtp.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this ConnectionSummaryFromAtp.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this ConnectionSummaryFromAtp.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this ConnectionSummaryFromAtp.
        :type identifier: str

        :param primary_schema:
            The value to assign to the primary_schema property of this ConnectionSummaryFromAtp.
        :type primary_schema: Schema

        :param connection_properties:
            The value to assign to the connection_properties property of this ConnectionSummaryFromAtp.
        :type connection_properties: list[ConnectionProperty]

        :param is_default:
            The value to assign to the is_default property of this ConnectionSummaryFromAtp.
        :type is_default: bool

        :param metadata:
            The value to assign to the metadata property of this ConnectionSummaryFromAtp.
        :type metadata: ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this ConnectionSummaryFromAtp.
        :type key_map: dict(str, str)

        :param username:
            The value to assign to the username property of this ConnectionSummaryFromAtp.
        :type username: str

        :param password:
            The value to assign to the password property of this ConnectionSummaryFromAtp.
        :type password: str

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
            'password': 'str'
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
            'password': 'password'
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
        self._password = None
        self._model_type = 'ORACLE_ATP_CONNECTION'

    @property
    def username(self):
        """
        Gets the username of this ConnectionSummaryFromAtp.
        The user name for the connection.


        :return: The username of this ConnectionSummaryFromAtp.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ConnectionSummaryFromAtp.
        The user name for the connection.


        :param username: The username of this ConnectionSummaryFromAtp.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this ConnectionSummaryFromAtp.
        The password for the connection.


        :return: The password of this ConnectionSummaryFromAtp.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ConnectionSummaryFromAtp.
        The password for the connection.


        :param password: The password of this ConnectionSummaryFromAtp.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
