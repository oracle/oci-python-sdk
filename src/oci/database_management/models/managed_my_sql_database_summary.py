# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedMySqlDatabaseSummary(object):
    """
    The details of the Managed MySQL Database.
    """

    #: A constant which can be used with the database_type property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "EXTERNAL"
    DATABASE_TYPE_EXTERNAL = "EXTERNAL"

    #: A constant which can be used with the database_type property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "MDS"
    DATABASE_TYPE_MDS = "MDS"

    #: A constant which can be used with the management_state property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "ENABLED"
    MANAGEMENT_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the management_state property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "DISABLED"
    MANAGEMENT_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ManagedMySqlDatabaseSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedMySqlDatabaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedMySqlDatabaseSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedMySqlDatabaseSummary.
        :type compartment_id: str

        :param db_name:
            The value to assign to the db_name property of this ManagedMySqlDatabaseSummary.
        :type db_name: str

        :param db_version:
            The value to assign to the db_version property of this ManagedMySqlDatabaseSummary.
        :type db_version: str

        :param time_created:
            The value to assign to the time_created property of this ManagedMySqlDatabaseSummary.
        :type time_created: datetime

        :param name:
            The value to assign to the name property of this ManagedMySqlDatabaseSummary.
        :type name: str

        :param database_type:
            The value to assign to the database_type property of this ManagedMySqlDatabaseSummary.
            Allowed values for this property are: "EXTERNAL", "MDS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param management_state:
            The value to assign to the management_state property of this ManagedMySqlDatabaseSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type management_state: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagedMySqlDatabaseSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param heat_wave_management_type:
            The value to assign to the heat_wave_management_type property of this ManagedMySqlDatabaseSummary.
        :type heat_wave_management_type: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'db_name': 'str',
            'db_version': 'str',
            'time_created': 'datetime',
            'name': 'str',
            'database_type': 'str',
            'management_state': 'str',
            'lifecycle_state': 'str',
            'heat_wave_management_type': 'str'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'db_name': 'dbName',
            'db_version': 'dbVersion',
            'time_created': 'timeCreated',
            'name': 'name',
            'database_type': 'databaseType',
            'management_state': 'managementState',
            'lifecycle_state': 'lifecycleState',
            'heat_wave_management_type': 'heatWaveManagementType'
        }
        self._id = None
        self._compartment_id = None
        self._db_name = None
        self._db_version = None
        self._time_created = None
        self._name = None
        self._database_type = None
        self._management_state = None
        self._lifecycle_state = None
        self._heat_wave_management_type = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedMySqlDatabaseSummary.
        The OCID of the Managed MySQL Database.


        :return: The id of this ManagedMySqlDatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedMySqlDatabaseSummary.
        The OCID of the Managed MySQL Database.


        :param id: The id of this ManagedMySqlDatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedMySqlDatabaseSummary.
        The OCID of the compartment.


        :return: The compartment_id of this ManagedMySqlDatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedMySqlDatabaseSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this ManagedMySqlDatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this ManagedMySqlDatabaseSummary.
        The name of the MySQL Database.


        :return: The db_name of this ManagedMySqlDatabaseSummary.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this ManagedMySqlDatabaseSummary.
        The name of the MySQL Database.


        :param db_name: The db_name of this ManagedMySqlDatabaseSummary.
        :type: str
        """
        self._db_name = db_name

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this ManagedMySqlDatabaseSummary.
        The version of the MySQL Database.


        :return: The db_version of this ManagedMySqlDatabaseSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this ManagedMySqlDatabaseSummary.
        The version of the MySQL Database.


        :param db_version: The db_version of this ManagedMySqlDatabaseSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ManagedMySqlDatabaseSummary.
        The date and time the Managed MySQL Database was created.


        :return: The time_created of this ManagedMySqlDatabaseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagedMySqlDatabaseSummary.
        The date and time the Managed MySQL Database was created.


        :param time_created: The time_created of this ManagedMySqlDatabaseSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedMySqlDatabaseSummary.
        The name of the Managed MySQL Database.


        :return: The name of this ManagedMySqlDatabaseSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedMySqlDatabaseSummary.
        The name of the Managed MySQL Database.


        :param name: The name of this ManagedMySqlDatabaseSummary.
        :type: str
        """
        self._name = name

    @property
    def database_type(self):
        """
        Gets the database_type of this ManagedMySqlDatabaseSummary.
        The type of the MySQL Database. Indicates whether the database
        is external or MDS.

        Allowed values for this property are: "EXTERNAL", "MDS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this ManagedMySqlDatabaseSummary.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this ManagedMySqlDatabaseSummary.
        The type of the MySQL Database. Indicates whether the database
        is external or MDS.


        :param database_type: The database_type of this ManagedMySqlDatabaseSummary.
        :type: str
        """
        allowed_values = ["EXTERNAL", "MDS"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def management_state(self):
        """
        Gets the management_state of this ManagedMySqlDatabaseSummary.
        Indicates database management status.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The management_state of this ManagedMySqlDatabaseSummary.
        :rtype: str
        """
        return self._management_state

    @management_state.setter
    def management_state(self, management_state):
        """
        Sets the management_state of this ManagedMySqlDatabaseSummary.
        Indicates database management status.


        :param management_state: The management_state of this ManagedMySqlDatabaseSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(management_state, allowed_values):
            management_state = 'UNKNOWN_ENUM_VALUE'
        self._management_state = management_state

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ManagedMySqlDatabaseSummary.
        Indicates lifecycle  state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ManagedMySqlDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagedMySqlDatabaseSummary.
        Indicates lifecycle  state of the resource.


        :param lifecycle_state: The lifecycle_state of this ManagedMySqlDatabaseSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def heat_wave_management_type(self):
        """
        Gets the heat_wave_management_type of this ManagedMySqlDatabaseSummary.
        The customer's selected type for HeatWave management.


        :return: The heat_wave_management_type of this ManagedMySqlDatabaseSummary.
        :rtype: str
        """
        return self._heat_wave_management_type

    @heat_wave_management_type.setter
    def heat_wave_management_type(self, heat_wave_management_type):
        """
        Sets the heat_wave_management_type of this ManagedMySqlDatabaseSummary.
        The customer's selected type for HeatWave management.


        :param heat_wave_management_type: The heat_wave_management_type of this ManagedMySqlDatabaseSummary.
        :type: str
        """
        self._heat_wave_management_type = heat_wave_management_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
