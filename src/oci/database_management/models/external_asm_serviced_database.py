# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalAsmServicedDatabase(object):
    """
    The details of a database serviced by an external ASM.
    """

    #: A constant which can be used with the database_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "CLOUD_SIDB"
    DATABASE_TYPE_CLOUD_SIDB = "CLOUD_SIDB"

    #: A constant which can be used with the database_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "CLOUD_RAC"
    DATABASE_TYPE_CLOUD_RAC = "CLOUD_RAC"

    #: A constant which can be used with the database_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "SHARED"
    DATABASE_TYPE_SHARED = "SHARED"

    #: A constant which can be used with the database_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "DEDICATED"
    DATABASE_TYPE_DEDICATED = "DEDICATED"

    #: A constant which can be used with the database_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "CLOUD_AT_CUSTOMER"
    DATABASE_TYPE_CLOUD_AT_CUSTOMER = "CLOUD_AT_CUSTOMER"

    #: A constant which can be used with the database_sub_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the database_sub_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "ACD"
    DATABASE_SUB_TYPE_ACD = "ACD"

    #: A constant which can be used with the database_sub_type property of a ExternalAsmServicedDatabase.
    #: This constant has a value of "ADB"
    DATABASE_SUB_TYPE_ADB = "ADB"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalAsmServicedDatabase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param disk_groups:
            The value to assign to the disk_groups property of this ExternalAsmServicedDatabase.
        :type disk_groups: list[str]

        :param id:
            The value to assign to the id property of this ExternalAsmServicedDatabase.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalAsmServicedDatabase.
        :type display_name: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this ExternalAsmServicedDatabase.
        :type db_unique_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalAsmServicedDatabase.
        :type compartment_id: str

        :param database_type:
            The value to assign to the database_type property of this ExternalAsmServicedDatabase.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", "CLOUD_AT_CUSTOMER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this ExternalAsmServicedDatabase.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param is_managed:
            The value to assign to the is_managed property of this ExternalAsmServicedDatabase.
        :type is_managed: bool

        """
        self.swagger_types = {
            'disk_groups': 'list[str]',
            'id': 'str',
            'display_name': 'str',
            'db_unique_name': 'str',
            'compartment_id': 'str',
            'database_type': 'str',
            'database_sub_type': 'str',
            'is_managed': 'bool'
        }
        self.attribute_map = {
            'disk_groups': 'diskGroups',
            'id': 'id',
            'display_name': 'displayName',
            'db_unique_name': 'dbUniqueName',
            'compartment_id': 'compartmentId',
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'is_managed': 'isManaged'
        }
        self._disk_groups = None
        self._id = None
        self._display_name = None
        self._db_unique_name = None
        self._compartment_id = None
        self._database_type = None
        self._database_sub_type = None
        self._is_managed = None

    @property
    def disk_groups(self):
        """
        Gets the disk_groups of this ExternalAsmServicedDatabase.
        The list of ASM disk groups used by the database.


        :return: The disk_groups of this ExternalAsmServicedDatabase.
        :rtype: list[str]
        """
        return self._disk_groups

    @disk_groups.setter
    def disk_groups(self, disk_groups):
        """
        Sets the disk_groups of this ExternalAsmServicedDatabase.
        The list of ASM disk groups used by the database.


        :param disk_groups: The disk_groups of this ExternalAsmServicedDatabase.
        :type: list[str]
        """
        self._disk_groups = disk_groups

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalAsmServicedDatabase.
        The `OCID`__ of the external database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalAsmServicedDatabase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalAsmServicedDatabase.
        The `OCID`__ of the external database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalAsmServicedDatabase.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalAsmServicedDatabase.
        The user-friendly name for the database. The name does not have to be unique.


        :return: The display_name of this ExternalAsmServicedDatabase.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalAsmServicedDatabase.
        The user-friendly name for the database. The name does not have to be unique.


        :param display_name: The display_name of this ExternalAsmServicedDatabase.
        :type: str
        """
        self._display_name = display_name

    @property
    def db_unique_name(self):
        """
        Gets the db_unique_name of this ExternalAsmServicedDatabase.
        The unique name of the external database.


        :return: The db_unique_name of this ExternalAsmServicedDatabase.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this ExternalAsmServicedDatabase.
        The unique name of the external database.


        :param db_unique_name: The db_unique_name of this ExternalAsmServicedDatabase.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ExternalAsmServicedDatabase.
        The `OCID`__ of the compartment in which the external database resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalAsmServicedDatabase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalAsmServicedDatabase.
        The `OCID`__ of the compartment in which the external database resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalAsmServicedDatabase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def database_type(self):
        """
        Gets the database_type of this ExternalAsmServicedDatabase.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", "CLOUD_AT_CUSTOMER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this ExternalAsmServicedDatabase.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this ExternalAsmServicedDatabase.
        The type of Oracle Database installation.


        :param database_type: The database_type of this ExternalAsmServicedDatabase.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", "CLOUD_AT_CUSTOMER"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        Gets the database_sub_type of this ExternalAsmServicedDatabase.
        The subtype of Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this ExternalAsmServicedDatabase.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this ExternalAsmServicedDatabase.
        The subtype of Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.


        :param database_sub_type: The database_sub_type of this ExternalAsmServicedDatabase.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB", "ACD", "ADB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def is_managed(self):
        """
        Gets the is_managed of this ExternalAsmServicedDatabase.
        Indicates whether the database is a Managed Database or not.


        :return: The is_managed of this ExternalAsmServicedDatabase.
        :rtype: bool
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """
        Sets the is_managed of this ExternalAsmServicedDatabase.
        Indicates whether the database is a Managed Database or not.


        :param is_managed: The is_managed of this ExternalAsmServicedDatabase.
        :type: bool
        """
        self._is_managed = is_managed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
