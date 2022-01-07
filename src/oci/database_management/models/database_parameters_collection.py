# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseParametersCollection(object):
    """
    A collection of database parameters.
    """

    #: A constant which can be used with the database_type property of a DatabaseParametersCollection.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a DatabaseParametersCollection.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_type property of a DatabaseParametersCollection.
    #: This constant has a value of "CLOUD_SIDB"
    DATABASE_TYPE_CLOUD_SIDB = "CLOUD_SIDB"

    #: A constant which can be used with the database_type property of a DatabaseParametersCollection.
    #: This constant has a value of "CLOUD_RAC"
    DATABASE_TYPE_CLOUD_RAC = "CLOUD_RAC"

    #: A constant which can be used with the database_type property of a DatabaseParametersCollection.
    #: This constant has a value of "SHARED"
    DATABASE_TYPE_SHARED = "SHARED"

    #: A constant which can be used with the database_type property of a DatabaseParametersCollection.
    #: This constant has a value of "DEDICATED"
    DATABASE_TYPE_DEDICATED = "DEDICATED"

    #: A constant which can be used with the database_sub_type property of a DatabaseParametersCollection.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a DatabaseParametersCollection.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a DatabaseParametersCollection.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the database_sub_type property of a DatabaseParametersCollection.
    #: This constant has a value of "ACD"
    DATABASE_SUB_TYPE_ACD = "ACD"

    #: A constant which can be used with the database_sub_type property of a DatabaseParametersCollection.
    #: This constant has a value of "ADB"
    DATABASE_SUB_TYPE_ADB = "ADB"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseParametersCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_name:
            The value to assign to the database_name property of this DatabaseParametersCollection.
        :type database_name: str

        :param database_type:
            The value to assign to the database_type property of this DatabaseParametersCollection.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this DatabaseParametersCollection.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param database_version:
            The value to assign to the database_version property of this DatabaseParametersCollection.
        :type database_version: str

        :param items:
            The value to assign to the items property of this DatabaseParametersCollection.
        :type items: list[oci.database_management.models.DatabaseParameterSummary]

        """
        self.swagger_types = {
            'database_name': 'str',
            'database_type': 'str',
            'database_sub_type': 'str',
            'database_version': 'str',
            'items': 'list[DatabaseParameterSummary]'
        }

        self.attribute_map = {
            'database_name': 'databaseName',
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'database_version': 'databaseVersion',
            'items': 'items'
        }

        self._database_name = None
        self._database_type = None
        self._database_sub_type = None
        self._database_version = None
        self._items = None

    @property
    def database_name(self):
        """
        **[Required]** Gets the database_name of this DatabaseParametersCollection.
        The name of the Managed Database.


        :return: The database_name of this DatabaseParametersCollection.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this DatabaseParametersCollection.
        The name of the Managed Database.


        :param database_name: The database_name of this DatabaseParametersCollection.
        :type: str
        """
        self._database_name = database_name

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this DatabaseParametersCollection.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this DatabaseParametersCollection.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this DatabaseParametersCollection.
        The type of Oracle Database installation.


        :param database_type: The database_type of this DatabaseParametersCollection.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        **[Required]** Gets the database_sub_type of this DatabaseParametersCollection.
        The subtype of the Oracle Database. Indicates whether the database
        is a Container Database, Pluggable Database, or a Non-container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this DatabaseParametersCollection.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this DatabaseParametersCollection.
        The subtype of the Oracle Database. Indicates whether the database
        is a Container Database, Pluggable Database, or a Non-container Database.


        :param database_sub_type: The database_sub_type of this DatabaseParametersCollection.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB", "ACD", "ADB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def database_version(self):
        """
        **[Required]** Gets the database_version of this DatabaseParametersCollection.
        The Oracle Database version.


        :return: The database_version of this DatabaseParametersCollection.
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """
        Sets the database_version of this DatabaseParametersCollection.
        The Oracle Database version.


        :param database_version: The database_version of this DatabaseParametersCollection.
        :type: str
        """
        self._database_version = database_version

    @property
    def items(self):
        """
        **[Required]** Gets the items of this DatabaseParametersCollection.
        An array of DatabaseParameterSummary objects.


        :return: The items of this DatabaseParametersCollection.
        :rtype: list[oci.database_management.models.DatabaseParameterSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this DatabaseParametersCollection.
        An array of DatabaseParameterSummary objects.


        :param items: The items of this DatabaseParametersCollection.
        :type: list[oci.database_management.models.DatabaseParameterSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
