# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConnectionDetails(object):
    """
    Properties used in connection update operations.
    """

    #: A constant which can be used with the model_type property of a UpdateConnectionDetails.
    #: This constant has a value of "ORACLE_ADWC_CONNECTION"
    MODEL_TYPE_ORACLE_ADWC_CONNECTION = "ORACLE_ADWC_CONNECTION"

    #: A constant which can be used with the model_type property of a UpdateConnectionDetails.
    #: This constant has a value of "ORACLE_ATP_CONNECTION"
    MODEL_TYPE_ORACLE_ATP_CONNECTION = "ORACLE_ATP_CONNECTION"

    #: A constant which can be used with the model_type property of a UpdateConnectionDetails.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE_CONNECTION"
    MODEL_TYPE_ORACLE_OBJECT_STORAGE_CONNECTION = "ORACLE_OBJECT_STORAGE_CONNECTION"

    #: A constant which can be used with the model_type property of a UpdateConnectionDetails.
    #: This constant has a value of "ORACLEDB_CONNECTION"
    MODEL_TYPE_ORACLEDB_CONNECTION = "ORACLEDB_CONNECTION"

    #: A constant which can be used with the model_type property of a UpdateConnectionDetails.
    #: This constant has a value of "MYSQL_CONNECTION"
    MODEL_TYPE_MYSQL_CONNECTION = "MYSQL_CONNECTION"

    #: A constant which can be used with the model_type property of a UpdateConnectionDetails.
    #: This constant has a value of "GENERIC_JDBC_CONNECTION"
    MODEL_TYPE_GENERIC_JDBC_CONNECTION = "GENERIC_JDBC_CONNECTION"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConnectionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.UpdateConnectionFromJdbc`
        * :class:`~oci.data_integration.models.UpdateConnectionFromObjectStorage`
        * :class:`~oci.data_integration.models.UpdateConnectionFromAtp`
        * :class:`~oci.data_integration.models.UpdateConnectionFromOracle`
        * :class:`~oci.data_integration.models.UpdateConnectionFromAdwc`
        * :class:`~oci.data_integration.models.UpdateConnectionFromMySQL`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this UpdateConnectionDetails.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this UpdateConnectionDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this UpdateConnectionDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this UpdateConnectionDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this UpdateConnectionDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateConnectionDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UpdateConnectionDetails.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this UpdateConnectionDetails.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this UpdateConnectionDetails.
        :type identifier: str

        :param connection_properties:
            The value to assign to the connection_properties property of this UpdateConnectionDetails.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateConnectionDetails.
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
            'object_version': 'int',
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
            'object_version': 'objectVersion',
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
        self._object_version = None
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

        if type == 'GENERIC_JDBC_CONNECTION':
            return 'UpdateConnectionFromJdbc'

        if type == 'ORACLE_OBJECT_STORAGE_CONNECTION':
            return 'UpdateConnectionFromObjectStorage'

        if type == 'ORACLE_ATP_CONNECTION':
            return 'UpdateConnectionFromAtp'

        if type == 'ORACLEDB_CONNECTION':
            return 'UpdateConnectionFromOracle'

        if type == 'ORACLE_ADWC_CONNECTION':
            return 'UpdateConnectionFromAdwc'

        if type == 'MYSQL_CONNECTION':
            return 'UpdateConnectionFromMySQL'
        else:
            return 'UpdateConnectionDetails'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this UpdateConnectionDetails.
        The type of the connection.

        Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION"


        :return: The model_type of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this UpdateConnectionDetails.
        The type of the connection.


        :param model_type: The model_type of this UpdateConnectionDetails.
        :type: str
        """
        allowed_values = ["ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def key(self):
        """
        **[Required]** Gets the key of this UpdateConnectionDetails.
        Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.


        :return: The key of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this UpdateConnectionDetails.
        Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.


        :param key: The key of this UpdateConnectionDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this UpdateConnectionDetails.
        The model version of an object.


        :return: The model_version of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this UpdateConnectionDetails.
        The model version of an object.


        :param model_version: The model_version of this UpdateConnectionDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this UpdateConnectionDetails.

        :return: The parent_ref of this UpdateConnectionDetails.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this UpdateConnectionDetails.

        :param parent_ref: The parent_ref of this UpdateConnectionDetails.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this UpdateConnectionDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateConnectionDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this UpdateConnectionDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateConnectionDetails.
        User-defined description for the connection.


        :return: The description of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateConnectionDetails.
        User-defined description for the connection.


        :param description: The description of this UpdateConnectionDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this UpdateConnectionDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this UpdateConnectionDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this UpdateConnectionDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this UpdateConnectionDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def object_version(self):
        """
        **[Required]** Gets the object_version of this UpdateConnectionDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this UpdateConnectionDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this UpdateConnectionDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this UpdateConnectionDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def identifier(self):
        """
        Gets the identifier of this UpdateConnectionDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this UpdateConnectionDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this UpdateConnectionDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def connection_properties(self):
        """
        Gets the connection_properties of this UpdateConnectionDetails.
        The properties for the connection.


        :return: The connection_properties of this UpdateConnectionDetails.
        :rtype: list[oci.data_integration.models.ConnectionProperty]
        """
        return self._connection_properties

    @connection_properties.setter
    def connection_properties(self, connection_properties):
        """
        Sets the connection_properties of this UpdateConnectionDetails.
        The properties for the connection.


        :param connection_properties: The connection_properties of this UpdateConnectionDetails.
        :type: list[oci.data_integration.models.ConnectionProperty]
        """
        self._connection_properties = connection_properties

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this UpdateConnectionDetails.

        :return: The registry_metadata of this UpdateConnectionDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this UpdateConnectionDetails.

        :param registry_metadata: The registry_metadata of this UpdateConnectionDetails.
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
