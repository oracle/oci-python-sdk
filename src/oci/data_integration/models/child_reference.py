# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChildReference(object):
    """
    Child reference contains application configuration information.
    """

    #: A constant which can be used with the type property of a ChildReference.
    #: This constant has a value of "ORACLEDB_CONNECTION"
    TYPE_ORACLEDB_CONNECTION = "ORACLEDB_CONNECTION"

    #: A constant which can be used with the type property of a ChildReference.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE_CONNECTION"
    TYPE_ORACLE_OBJECT_STORAGE_CONNECTION = "ORACLE_OBJECT_STORAGE_CONNECTION"

    #: A constant which can be used with the type property of a ChildReference.
    #: This constant has a value of "ORACLE_ATP_CONNECTION"
    TYPE_ORACLE_ATP_CONNECTION = "ORACLE_ATP_CONNECTION"

    #: A constant which can be used with the type property of a ChildReference.
    #: This constant has a value of "ORACLE_ADWC_CONNECTION"
    TYPE_ORACLE_ADWC_CONNECTION = "ORACLE_ADWC_CONNECTION"

    #: A constant which can be used with the type property of a ChildReference.
    #: This constant has a value of "MYSQL_CONNECTION"
    TYPE_MYSQL_CONNECTION = "MYSQL_CONNECTION"

    #: A constant which can be used with the type property of a ChildReference.
    #: This constant has a value of "GENERIC_JDBC_CONNECTION"
    TYPE_GENERIC_JDBC_CONNECTION = "GENERIC_JDBC_CONNECTION"

    #: A constant which can be used with the type property of a ChildReference.
    #: This constant has a value of "BIP_CONNECTION"
    TYPE_BIP_CONNECTION = "BIP_CONNECTION"

    #: A constant which can be used with the type property of a ChildReference.
    #: This constant has a value of "BICC_CONNECTION"
    TYPE_BICC_CONNECTION = "BICC_CONNECTION"

    #: A constant which can be used with the type property of a ChildReference.
    #: This constant has a value of "AMAZON_S3_CONNECTION"
    TYPE_AMAZON_S3_CONNECTION = "AMAZON_S3_CONNECTION"

    def __init__(self, **kwargs):
        """
        Initializes a new ChildReference object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ChildReference.
        :type key: str

        :param name:
            The value to assign to the name property of this ChildReference.
        :type name: str

        :param identifier:
            The value to assign to the identifier property of this ChildReference.
        :type identifier: str

        :param identifier_path:
            The value to assign to the identifier_path property of this ChildReference.
        :type identifier_path: str

        :param description:
            The value to assign to the description property of this ChildReference.
        :type description: str

        :param type:
            The value to assign to the type property of this ChildReference.
            Allowed values for this property are: "ORACLEDB_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_ADWC_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BIP_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param target_object:
            The value to assign to the target_object property of this ChildReference.
        :type target_object: object

        :param aggregator_key:
            The value to assign to the aggregator_key property of this ChildReference.
        :type aggregator_key: str

        :param used_by:
            The value to assign to the used_by property of this ChildReference.
        :type used_by: list[oci.data_integration.models.ReferenceUsedBy]

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'identifier': 'str',
            'identifier_path': 'str',
            'description': 'str',
            'type': 'str',
            'target_object': 'object',
            'aggregator_key': 'str',
            'used_by': 'list[ReferenceUsedBy]'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'identifier': 'identifier',
            'identifier_path': 'identifierPath',
            'description': 'description',
            'type': 'type',
            'target_object': 'targetObject',
            'aggregator_key': 'aggregatorKey',
            'used_by': 'usedBy'
        }

        self._key = None
        self._name = None
        self._identifier = None
        self._identifier_path = None
        self._description = None
        self._type = None
        self._target_object = None
        self._aggregator_key = None
        self._used_by = None

    @property
    def key(self):
        """
        Gets the key of this ChildReference.
        The reference's key, key of the object that is being used by a published object or its dependents.


        :return: The key of this ChildReference.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ChildReference.
        The reference's key, key of the object that is being used by a published object or its dependents.


        :param key: The key of this ChildReference.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this ChildReference.
        The name of reference object.


        :return: The name of this ChildReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ChildReference.
        The name of reference object.


        :param name: The name of this ChildReference.
        :type: str
        """
        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this ChildReference.
        The identifier of reference object.


        :return: The identifier of this ChildReference.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ChildReference.
        The identifier of reference object.


        :param identifier: The identifier of this ChildReference.
        :type: str
        """
        self._identifier = identifier

    @property
    def identifier_path(self):
        """
        Gets the identifier_path of this ChildReference.
        The identifier path of reference object.


        :return: The identifier_path of this ChildReference.
        :rtype: str
        """
        return self._identifier_path

    @identifier_path.setter
    def identifier_path(self, identifier_path):
        """
        Sets the identifier_path of this ChildReference.
        The identifier path of reference object.


        :param identifier_path: The identifier_path of this ChildReference.
        :type: str
        """
        self._identifier_path = identifier_path

    @property
    def description(self):
        """
        Gets the description of this ChildReference.
        The description of reference object.


        :return: The description of this ChildReference.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ChildReference.
        The description of reference object.


        :param description: The description of this ChildReference.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        Gets the type of this ChildReference.
        The type of the reference object.

        Allowed values for this property are: "ORACLEDB_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_ADWC_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BIP_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ChildReference.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ChildReference.
        The type of the reference object.


        :param type: The type of this ChildReference.
        :type: str
        """
        allowed_values = ["ORACLEDB_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_ADWC_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BIP_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def target_object(self):
        """
        Gets the target_object of this ChildReference.
        The new reference object to use instead of the original reference. For example, this can be a data asset reference.


        :return: The target_object of this ChildReference.
        :rtype: object
        """
        return self._target_object

    @target_object.setter
    def target_object(self, target_object):
        """
        Sets the target_object of this ChildReference.
        The new reference object to use instead of the original reference. For example, this can be a data asset reference.


        :param target_object: The target_object of this ChildReference.
        :type: object
        """
        self._target_object = target_object

    @property
    def aggregator_key(self):
        """
        Gets the aggregator_key of this ChildReference.
        The aggregator key of the child reference object. For example, this can be a data asset key.


        :return: The aggregator_key of this ChildReference.
        :rtype: str
        """
        return self._aggregator_key

    @aggregator_key.setter
    def aggregator_key(self, aggregator_key):
        """
        Sets the aggregator_key of this ChildReference.
        The aggregator key of the child reference object. For example, this can be a data asset key.


        :param aggregator_key: The aggregator_key of this ChildReference.
        :type: str
        """
        self._aggregator_key = aggregator_key

    @property
    def used_by(self):
        """
        Gets the used_by of this ChildReference.
        List of published objects where this is used.


        :return: The used_by of this ChildReference.
        :rtype: list[oci.data_integration.models.ReferenceUsedBy]
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        """
        Sets the used_by of this ChildReference.
        List of published objects where this is used.


        :param used_by: The used_by of this ChildReference.
        :type: list[oci.data_integration.models.ReferenceUsedBy]
        """
        self._used_by = used_by

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
