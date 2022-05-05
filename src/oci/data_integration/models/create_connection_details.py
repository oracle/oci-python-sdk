# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionDetails(object):
    """
    Properties used in connection create operations.
    """

    #: A constant which can be used with the model_type property of a CreateConnectionDetails.
    #: This constant has a value of "ORACLE_ADWC_CONNECTION"
    MODEL_TYPE_ORACLE_ADWC_CONNECTION = "ORACLE_ADWC_CONNECTION"

    #: A constant which can be used with the model_type property of a CreateConnectionDetails.
    #: This constant has a value of "ORACLE_ATP_CONNECTION"
    MODEL_TYPE_ORACLE_ATP_CONNECTION = "ORACLE_ATP_CONNECTION"

    #: A constant which can be used with the model_type property of a CreateConnectionDetails.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE_CONNECTION"
    MODEL_TYPE_ORACLE_OBJECT_STORAGE_CONNECTION = "ORACLE_OBJECT_STORAGE_CONNECTION"

    #: A constant which can be used with the model_type property of a CreateConnectionDetails.
    #: This constant has a value of "ORACLEDB_CONNECTION"
    MODEL_TYPE_ORACLEDB_CONNECTION = "ORACLEDB_CONNECTION"

    #: A constant which can be used with the model_type property of a CreateConnectionDetails.
    #: This constant has a value of "MYSQL_CONNECTION"
    MODEL_TYPE_MYSQL_CONNECTION = "MYSQL_CONNECTION"

    #: A constant which can be used with the model_type property of a CreateConnectionDetails.
    #: This constant has a value of "GENERIC_JDBC_CONNECTION"
    MODEL_TYPE_GENERIC_JDBC_CONNECTION = "GENERIC_JDBC_CONNECTION"

    #: A constant which can be used with the model_type property of a CreateConnectionDetails.
    #: This constant has a value of "BICC_CONNECTION"
    MODEL_TYPE_BICC_CONNECTION = "BICC_CONNECTION"

    #: A constant which can be used with the model_type property of a CreateConnectionDetails.
    #: This constant has a value of "AMAZON_S3_CONNECTION"
    MODEL_TYPE_AMAZON_S3_CONNECTION = "AMAZON_S3_CONNECTION"

    #: A constant which can be used with the model_type property of a CreateConnectionDetails.
    #: This constant has a value of "BIP_CONNECTION"
    MODEL_TYPE_BIP_CONNECTION = "BIP_CONNECTION"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.CreateConnectionFromMySQL`
        * :class:`~oci.data_integration.models.CreateConnectionFromAmazonS3`
        * :class:`~oci.data_integration.models.CreateConnectionFromJdbc`
        * :class:`~oci.data_integration.models.CreateConnectionFromBICC`
        * :class:`~oci.data_integration.models.CreateConnectionFromAtp`
        * :class:`~oci.data_integration.models.CreateConnectionFromBIP`
        * :class:`~oci.data_integration.models.CreateConnectionFromAdwc`
        * :class:`~oci.data_integration.models.CreateConnectionFromOracle`
        * :class:`~oci.data_integration.models.CreateConnectionFromObjectStorage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateConnectionDetails.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", "BIP_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateConnectionDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateConnectionDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateConnectionDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateConnectionDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateConnectionDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateConnectionDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateConnectionDetails.
        :type identifier: str

        :param connection_properties:
            The value to assign to the connection_properties property of this CreateConnectionDetails.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateConnectionDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

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
            'registry_metadata': 'RegistryMetadata'
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
            'registry_metadata': 'registryMetadata'
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'MYSQL_CONNECTION':
            return 'CreateConnectionFromMySQL'

        if type == 'AMAZON_S3_CONNECTION':
            return 'CreateConnectionFromAmazonS3'

        if type == 'GENERIC_JDBC_CONNECTION':
            return 'CreateConnectionFromJdbc'

        if type == 'BICC_CONNECTION':
            return 'CreateConnectionFromBICC'

        if type == 'ORACLE_ATP_CONNECTION':
            return 'CreateConnectionFromAtp'

        if type == 'BIP_CONNECTION':
            return 'CreateConnectionFromBIP'

        if type == 'ORACLE_ADWC_CONNECTION':
            return 'CreateConnectionFromAdwc'

        if type == 'ORACLEDB_CONNECTION':
            return 'CreateConnectionFromOracle'

        if type == 'ORACLE_OBJECT_STORAGE_CONNECTION':
            return 'CreateConnectionFromObjectStorage'
        else:
            return 'CreateConnectionDetails'

    @property
    def model_type(self):
        """
        Gets the model_type of this CreateConnectionDetails.
        The type of the connection.

        Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", "BIP_CONNECTION"


        :return: The model_type of this CreateConnectionDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateConnectionDetails.
        The type of the connection.


        :param model_type: The model_type of this CreateConnectionDetails.
        :type: str
        """
        allowed_values = ["ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", "BIP_CONNECTION"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this CreateConnectionDetails.
        Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.


        :return: The key of this CreateConnectionDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateConnectionDetails.
        Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.


        :param key: The key of this CreateConnectionDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateConnectionDetails.
        The model version of an object.


        :return: The model_version of this CreateConnectionDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateConnectionDetails.
        The model version of an object.


        :param model_version: The model_version of this CreateConnectionDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this CreateConnectionDetails.

        :return: The parent_ref of this CreateConnectionDetails.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this CreateConnectionDetails.

        :param parent_ref: The parent_ref of this CreateConnectionDetails.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateConnectionDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateConnectionDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateConnectionDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateConnectionDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateConnectionDetails.
        User-defined description for the connection.


        :return: The description of this CreateConnectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateConnectionDetails.
        User-defined description for the connection.


        :param description: The description of this CreateConnectionDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateConnectionDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateConnectionDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateConnectionDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateConnectionDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreateConnectionDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateConnectionDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateConnectionDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateConnectionDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def connection_properties(self):
        """
        Gets the connection_properties of this CreateConnectionDetails.
        The properties for the connection.


        :return: The connection_properties of this CreateConnectionDetails.
        :rtype: list[oci.data_integration.models.ConnectionProperty]
        """
        return self._connection_properties

    @connection_properties.setter
    def connection_properties(self, connection_properties):
        """
        Sets the connection_properties of this CreateConnectionDetails.
        The properties for the connection.


        :param connection_properties: The connection_properties of this CreateConnectionDetails.
        :type: list[oci.data_integration.models.ConnectionProperty]
        """
        self._connection_properties = connection_properties

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this CreateConnectionDetails.

        :return: The registry_metadata of this CreateConnectionDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreateConnectionDetails.

        :param registry_metadata: The registry_metadata of this CreateConnectionDetails.
        :type: oci.data_integration.models.RegistryMetadata
        """
        self._registry_metadata = registry_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
