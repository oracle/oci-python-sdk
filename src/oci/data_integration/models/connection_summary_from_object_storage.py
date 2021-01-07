# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection_summary import ConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionSummaryFromObjectStorage(ConnectionSummary):
    """
    The connection details for an Oracle Object Storage data asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionSummaryFromObjectStorage object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.ConnectionSummaryFromObjectStorage.model_type` attribute
        of this class is ``ORACLE_OBJECT_STORAGE_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ConnectionSummaryFromObjectStorage.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this ConnectionSummaryFromObjectStorage.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ConnectionSummaryFromObjectStorage.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ConnectionSummaryFromObjectStorage.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this ConnectionSummaryFromObjectStorage.
        :type name: str

        :param description:
            The value to assign to the description property of this ConnectionSummaryFromObjectStorage.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this ConnectionSummaryFromObjectStorage.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this ConnectionSummaryFromObjectStorage.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this ConnectionSummaryFromObjectStorage.
        :type identifier: str

        :param primary_schema:
            The value to assign to the primary_schema property of this ConnectionSummaryFromObjectStorage.
        :type primary_schema: oci.data_integration.models.Schema

        :param connection_properties:
            The value to assign to the connection_properties property of this ConnectionSummaryFromObjectStorage.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param is_default:
            The value to assign to the is_default property of this ConnectionSummaryFromObjectStorage.
        :type is_default: bool

        :param metadata:
            The value to assign to the metadata property of this ConnectionSummaryFromObjectStorage.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this ConnectionSummaryFromObjectStorage.
        :type key_map: dict(str, str)

        :param credential_file_content:
            The value to assign to the credential_file_content property of this ConnectionSummaryFromObjectStorage.
        :type credential_file_content: str

        :param user_id:
            The value to assign to the user_id property of this ConnectionSummaryFromObjectStorage.
        :type user_id: str

        :param finger_print:
            The value to assign to the finger_print property of this ConnectionSummaryFromObjectStorage.
        :type finger_print: str

        :param pass_phrase:
            The value to assign to the pass_phrase property of this ConnectionSummaryFromObjectStorage.
        :type pass_phrase: str

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
            'credential_file_content': 'str',
            'user_id': 'str',
            'finger_print': 'str',
            'pass_phrase': 'str'
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
            'credential_file_content': 'credentialFileContent',
            'user_id': 'userId',
            'finger_print': 'fingerPrint',
            'pass_phrase': 'passPhrase'
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
        self._credential_file_content = None
        self._user_id = None
        self._finger_print = None
        self._pass_phrase = None
        self._model_type = 'ORACLE_OBJECT_STORAGE_CONNECTION'

    @property
    def credential_file_content(self):
        """
        Gets the credential_file_content of this ConnectionSummaryFromObjectStorage.
        The credential file content from an Oracle Object Storage wallet.


        :return: The credential_file_content of this ConnectionSummaryFromObjectStorage.
        :rtype: str
        """
        return self._credential_file_content

    @credential_file_content.setter
    def credential_file_content(self, credential_file_content):
        """
        Sets the credential_file_content of this ConnectionSummaryFromObjectStorage.
        The credential file content from an Oracle Object Storage wallet.


        :param credential_file_content: The credential_file_content of this ConnectionSummaryFromObjectStorage.
        :type: str
        """
        self._credential_file_content = credential_file_content

    @property
    def user_id(self):
        """
        Gets the user_id of this ConnectionSummaryFromObjectStorage.
        The OCI user OCID for the user to connect to.


        :return: The user_id of this ConnectionSummaryFromObjectStorage.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ConnectionSummaryFromObjectStorage.
        The OCI user OCID for the user to connect to.


        :param user_id: The user_id of this ConnectionSummaryFromObjectStorage.
        :type: str
        """
        self._user_id = user_id

    @property
    def finger_print(self):
        """
        Gets the finger_print of this ConnectionSummaryFromObjectStorage.
        The fingerprint for the user.


        :return: The finger_print of this ConnectionSummaryFromObjectStorage.
        :rtype: str
        """
        return self._finger_print

    @finger_print.setter
    def finger_print(self, finger_print):
        """
        Sets the finger_print of this ConnectionSummaryFromObjectStorage.
        The fingerprint for the user.


        :param finger_print: The finger_print of this ConnectionSummaryFromObjectStorage.
        :type: str
        """
        self._finger_print = finger_print

    @property
    def pass_phrase(self):
        """
        Gets the pass_phrase of this ConnectionSummaryFromObjectStorage.
        The passphrase for the connection.


        :return: The pass_phrase of this ConnectionSummaryFromObjectStorage.
        :rtype: str
        """
        return self._pass_phrase

    @pass_phrase.setter
    def pass_phrase(self, pass_phrase):
        """
        Sets the pass_phrase of this ConnectionSummaryFromObjectStorage.
        The passphrase for the connection.


        :param pass_phrase: The pass_phrase of this ConnectionSummaryFromObjectStorage.
        :type: str
        """
        self._pass_phrase = pass_phrase

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
