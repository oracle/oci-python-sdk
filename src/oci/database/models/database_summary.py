# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseSummary(object):

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseSummary object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param character_set:
            The value to assign to the character_set property of this DatabaseSummary.
        :type character_set: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseSummary.
        :type compartment_id: str

        :param db_backup_config:
            The value to assign to the db_backup_config property of this DatabaseSummary.
        :type db_backup_config: DbBackupConfig

        :param db_home_id:
            The value to assign to the db_home_id property of this DatabaseSummary.
        :type db_home_id: str

        :param db_name:
            The value to assign to the db_name property of this DatabaseSummary.
        :type db_name: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this DatabaseSummary.
        :type db_unique_name: str

        :param db_workload:
            The value to assign to the db_workload property of this DatabaseSummary.
        :type db_workload: str

        :param id:
            The value to assign to the id property of this DatabaseSummary.
        :type id: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseSummary.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this DatabaseSummary.
        :type ncharacter_set: str

        :param pdb_name:
            The value to assign to the pdb_name property of this DatabaseSummary.
        :type pdb_name: str

        :param time_created:
            The value to assign to the time_created property of this DatabaseSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'character_set': 'str',
            'compartment_id': 'str',
            'db_backup_config': 'DbBackupConfig',
            'db_home_id': 'str',
            'db_name': 'str',
            'db_unique_name': 'str',
            'db_workload': 'str',
            'id': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'ncharacter_set': 'str',
            'pdb_name': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'character_set': 'characterSet',
            'compartment_id': 'compartmentId',
            'db_backup_config': 'dbBackupConfig',
            'db_home_id': 'dbHomeId',
            'db_name': 'dbName',
            'db_unique_name': 'dbUniqueName',
            'db_workload': 'dbWorkload',
            'id': 'id',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'ncharacter_set': 'ncharacterSet',
            'pdb_name': 'pdbName',
            'time_created': 'timeCreated'
        }

        self._character_set = None
        self._compartment_id = None
        self._db_backup_config = None
        self._db_home_id = None
        self._db_name = None
        self._db_unique_name = None
        self._db_workload = None
        self._id = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._ncharacter_set = None
        self._pdb_name = None
        self._time_created = None

    @property
    def character_set(self):
        """
        Gets the character_set of this DatabaseSummary.
        The character set for the database.


        :return: The character_set of this DatabaseSummary.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """
        Sets the character_set of this DatabaseSummary.
        The character set for the database.


        :param character_set: The character_set of this DatabaseSummary.
        :type: str
        """
        self._character_set = character_set

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DatabaseSummary.
        The OCID of the compartment.


        :return: The compartment_id of this DatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this DatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_backup_config(self):
        """
        Gets the db_backup_config of this DatabaseSummary.

        :return: The db_backup_config of this DatabaseSummary.
        :rtype: DbBackupConfig
        """
        return self._db_backup_config

    @db_backup_config.setter
    def db_backup_config(self, db_backup_config):
        """
        Sets the db_backup_config of this DatabaseSummary.

        :param db_backup_config: The db_backup_config of this DatabaseSummary.
        :type: DbBackupConfig
        """
        self._db_backup_config = db_backup_config

    @property
    def db_home_id(self):
        """
        Gets the db_home_id of this DatabaseSummary.
        The OCID of the database home.


        :return: The db_home_id of this DatabaseSummary.
        :rtype: str
        """
        return self._db_home_id

    @db_home_id.setter
    def db_home_id(self, db_home_id):
        """
        Sets the db_home_id of this DatabaseSummary.
        The OCID of the database home.


        :param db_home_id: The db_home_id of this DatabaseSummary.
        :type: str
        """
        self._db_home_id = db_home_id

    @property
    def db_name(self):
        """
        Gets the db_name of this DatabaseSummary.
        The database name.


        :return: The db_name of this DatabaseSummary.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this DatabaseSummary.
        The database name.


        :param db_name: The db_name of this DatabaseSummary.
        :type: str
        """
        self._db_name = db_name

    @property
    def db_unique_name(self):
        """
        Gets the db_unique_name of this DatabaseSummary.
        A system-generated name for the database to ensure uniqueness within an Oracle Data Guard group (a primary database and its standby databases). The unique name cannot be changed.


        :return: The db_unique_name of this DatabaseSummary.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this DatabaseSummary.
        A system-generated name for the database to ensure uniqueness within an Oracle Data Guard group (a primary database and its standby databases). The unique name cannot be changed.


        :param db_unique_name: The db_unique_name of this DatabaseSummary.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def db_workload(self):
        """
        Gets the db_workload of this DatabaseSummary.
        Database workload type.


        :return: The db_workload of this DatabaseSummary.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this DatabaseSummary.
        Database workload type.


        :param db_workload: The db_workload of this DatabaseSummary.
        :type: str
        """
        self._db_workload = db_workload

    @property
    def id(self):
        """
        Gets the id of this DatabaseSummary.
        The OCID of the database.


        :return: The id of this DatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatabaseSummary.
        The OCID of the database.


        :param id: The id of this DatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DatabaseSummary.
        Additional information about the current lifecycleState.


        :return: The lifecycle_details of this DatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DatabaseSummary.
        Additional information about the current lifecycleState.


        :param lifecycle_details: The lifecycle_details of this DatabaseSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DatabaseSummary.
        The current state of the database.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DatabaseSummary.
        The current state of the database.


        :param lifecycle_state: The lifecycle_state of this DatabaseSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def ncharacter_set(self):
        """
        Gets the ncharacter_set of this DatabaseSummary.
        The national character set for the database.


        :return: The ncharacter_set of this DatabaseSummary.
        :rtype: str
        """
        return self._ncharacter_set

    @ncharacter_set.setter
    def ncharacter_set(self, ncharacter_set):
        """
        Sets the ncharacter_set of this DatabaseSummary.
        The national character set for the database.


        :param ncharacter_set: The ncharacter_set of this DatabaseSummary.
        :type: str
        """
        self._ncharacter_set = ncharacter_set

    @property
    def pdb_name(self):
        """
        Gets the pdb_name of this DatabaseSummary.
        Pluggable database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.


        :return: The pdb_name of this DatabaseSummary.
        :rtype: str
        """
        return self._pdb_name

    @pdb_name.setter
    def pdb_name(self, pdb_name):
        """
        Sets the pdb_name of this DatabaseSummary.
        Pluggable database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.


        :param pdb_name: The pdb_name of this DatabaseSummary.
        :type: str
        """
        self._pdb_name = pdb_name

    @property
    def time_created(self):
        """
        Gets the time_created of this DatabaseSummary.
        The date and time the database was created.


        :return: The time_created of this DatabaseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DatabaseSummary.
        The date and time the database was created.


        :param time_created: The time_created of this DatabaseSummary.
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
