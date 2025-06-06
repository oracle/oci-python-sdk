# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MySqlDatabaseObjectSummary(object):
    """
    Database objects to include or exclude from migration
    """

    #: A constant which can be used with the object_status property of a MySqlDatabaseObjectSummary.
    #: This constant has a value of "EXCLUDE"
    OBJECT_STATUS_EXCLUDE = "EXCLUDE"

    #: A constant which can be used with the object_status property of a MySqlDatabaseObjectSummary.
    #: This constant has a value of "INCLUDE"
    OBJECT_STATUS_INCLUDE = "INCLUDE"

    def __init__(self, **kwargs):
        """
        Initializes a new MySqlDatabaseObjectSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_status:
            The value to assign to the object_status property of this MySqlDatabaseObjectSummary.
            Allowed values for this property are: "EXCLUDE", "INCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type object_status: str

        :param schema:
            The value to assign to the schema property of this MySqlDatabaseObjectSummary.
        :type schema: str

        :param object_name:
            The value to assign to the object_name property of this MySqlDatabaseObjectSummary.
        :type object_name: str

        :param type:
            The value to assign to the type property of this MySqlDatabaseObjectSummary.
        :type type: str

        """
        self.swagger_types = {
            'object_status': 'str',
            'schema': 'str',
            'object_name': 'str',
            'type': 'str'
        }
        self.attribute_map = {
            'object_status': 'objectStatus',
            'schema': 'schema',
            'object_name': 'objectName',
            'type': 'type'
        }
        self._object_status = None
        self._schema = None
        self._object_name = None
        self._type = None

    @property
    def object_status(self):
        """
        Gets the object_status of this MySqlDatabaseObjectSummary.
        Object status.

        Allowed values for this property are: "EXCLUDE", "INCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The object_status of this MySqlDatabaseObjectSummary.
        :rtype: str
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this MySqlDatabaseObjectSummary.
        Object status.


        :param object_status: The object_status of this MySqlDatabaseObjectSummary.
        :type: str
        """
        allowed_values = ["EXCLUDE", "INCLUDE"]
        if not value_allowed_none_or_none_sentinel(object_status, allowed_values):
            object_status = 'UNKNOWN_ENUM_VALUE'
        self._object_status = object_status

    @property
    def schema(self):
        """
        **[Required]** Gets the schema of this MySqlDatabaseObjectSummary.
        Schema of the object (regular expression is allowed)


        :return: The schema of this MySqlDatabaseObjectSummary.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this MySqlDatabaseObjectSummary.
        Schema of the object (regular expression is allowed)


        :param schema: The schema of this MySqlDatabaseObjectSummary.
        :type: str
        """
        self._schema = schema

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this MySqlDatabaseObjectSummary.
        Name of the object (regular expression is allowed)


        :return: The object_name of this MySqlDatabaseObjectSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this MySqlDatabaseObjectSummary.
        Name of the object (regular expression is allowed)


        :param object_name: The object_name of this MySqlDatabaseObjectSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def type(self):
        """
        Gets the type of this MySqlDatabaseObjectSummary.
        Type of object to exclude.
        If not specified, matching owners and object names of type TABLE would be excluded.


        :return: The type of this MySqlDatabaseObjectSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MySqlDatabaseObjectSummary.
        Type of object to exclude.
        If not specified, matching owners and object names of type TABLE would be excluded.


        :param type: The type of this MySqlDatabaseObjectSummary.
        :type: str
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
