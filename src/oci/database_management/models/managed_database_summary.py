# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedDatabaseSummary(object):
    """
    A summary of the Managed Database.
    """

    #: A constant which can be used with the database_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedDatabaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedDatabaseSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedDatabaseSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this ManagedDatabaseSummary.
        :type name: str

        :param database_type:
            The value to assign to the database_type property of this ManagedDatabaseSummary.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this ManagedDatabaseSummary.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param is_cluster:
            The value to assign to the is_cluster property of this ManagedDatabaseSummary.
        :type is_cluster: bool

        :param parent_container_id:
            The value to assign to the parent_container_id property of this ManagedDatabaseSummary.
        :type parent_container_id: str

        :param time_created:
            The value to assign to the time_created property of this ManagedDatabaseSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'database_type': 'str',
            'database_sub_type': 'str',
            'is_cluster': 'bool',
            'parent_container_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'is_cluster': 'isCluster',
            'parent_container_id': 'parentContainerId',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._database_type = None
        self._database_sub_type = None
        self._is_cluster = None
        self._parent_container_id = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedDatabaseSummary.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedDatabaseSummary.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ManagedDatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ManagedDatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedDatabaseSummary.
        The name of the Managed Database.


        :return: The name of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedDatabaseSummary.
        The name of the Managed Database.


        :param name: The name of this ManagedDatabaseSummary.
        :type: str
        """
        self._name = name

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this ManagedDatabaseSummary.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this ManagedDatabaseSummary.
        The type of Oracle Database installation.


        :param database_type: The database_type of this ManagedDatabaseSummary.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        **[Required]** Gets the database_sub_type of this ManagedDatabaseSummary.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this ManagedDatabaseSummary.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.


        :param database_sub_type: The database_sub_type of this ManagedDatabaseSummary.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def is_cluster(self):
        """
        **[Required]** Gets the is_cluster of this ManagedDatabaseSummary.
        Indicates whether the Oracle Database is part of a cluster.


        :return: The is_cluster of this ManagedDatabaseSummary.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this ManagedDatabaseSummary.
        Indicates whether the Oracle Database is part of a cluster.


        :param is_cluster: The is_cluster of this ManagedDatabaseSummary.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def parent_container_id(self):
        """
        Gets the parent_container_id of this ManagedDatabaseSummary.
        The `OCID`__ of the parent Container Database
        if the Managed Database is a Pluggable Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The parent_container_id of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._parent_container_id

    @parent_container_id.setter
    def parent_container_id(self, parent_container_id):
        """
        Sets the parent_container_id of this ManagedDatabaseSummary.
        The `OCID`__ of the parent Container Database
        if the Managed Database is a Pluggable Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param parent_container_id: The parent_container_id of this ManagedDatabaseSummary.
        :type: str
        """
        self._parent_container_id = parent_container_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ManagedDatabaseSummary.
        The date and time the Managed Database was created.


        :return: The time_created of this ManagedDatabaseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagedDatabaseSummary.
        The date and time the Managed Database was created.


        :param time_created: The time_created of this ManagedDatabaseSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
