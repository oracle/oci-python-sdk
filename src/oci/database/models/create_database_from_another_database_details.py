# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseFromAnotherDatabaseDetails(object):
    """
    CreateDatabaseFromAnotherDatabaseDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseFromAnotherDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_id:
            The value to assign to the database_id property of this CreateDatabaseFromAnotherDatabaseDetails.
        :type database_id: str

        :param backup_tde_password:
            The value to assign to the backup_tde_password property of this CreateDatabaseFromAnotherDatabaseDetails.
        :type backup_tde_password: str

        :param admin_password:
            The value to assign to the admin_password property of this CreateDatabaseFromAnotherDatabaseDetails.
        :type admin_password: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this CreateDatabaseFromAnotherDatabaseDetails.
        :type db_unique_name: str

        :param db_name:
            The value to assign to the db_name property of this CreateDatabaseFromAnotherDatabaseDetails.
        :type db_name: str

        :param time_stamp_for_point_in_time_recovery:
            The value to assign to the time_stamp_for_point_in_time_recovery property of this CreateDatabaseFromAnotherDatabaseDetails.
        :type time_stamp_for_point_in_time_recovery: datetime

        """
        self.swagger_types = {
            'database_id': 'str',
            'backup_tde_password': 'str',
            'admin_password': 'str',
            'db_unique_name': 'str',
            'db_name': 'str',
            'time_stamp_for_point_in_time_recovery': 'datetime'
        }

        self.attribute_map = {
            'database_id': 'databaseId',
            'backup_tde_password': 'backupTDEPassword',
            'admin_password': 'adminPassword',
            'db_unique_name': 'dbUniqueName',
            'db_name': 'dbName',
            'time_stamp_for_point_in_time_recovery': 'timeStampForPointInTimeRecovery'
        }

        self._database_id = None
        self._backup_tde_password = None
        self._admin_password = None
        self._db_unique_name = None
        self._db_name = None
        self._time_stamp_for_point_in_time_recovery = None

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this CreateDatabaseFromAnotherDatabaseDetails.
        The database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this CreateDatabaseFromAnotherDatabaseDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this CreateDatabaseFromAnotherDatabaseDetails.
        The database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this CreateDatabaseFromAnotherDatabaseDetails.
        :type: str
        """
        self._database_id = database_id

    @property
    def backup_tde_password(self):
        """
        **[Required]** Gets the backup_tde_password of this CreateDatabaseFromAnotherDatabaseDetails.
        The password to open the TDE wallet.


        :return: The backup_tde_password of this CreateDatabaseFromAnotherDatabaseDetails.
        :rtype: str
        """
        return self._backup_tde_password

    @backup_tde_password.setter
    def backup_tde_password(self, backup_tde_password):
        """
        Sets the backup_tde_password of this CreateDatabaseFromAnotherDatabaseDetails.
        The password to open the TDE wallet.


        :param backup_tde_password: The backup_tde_password of this CreateDatabaseFromAnotherDatabaseDetails.
        :type: str
        """
        self._backup_tde_password = backup_tde_password

    @property
    def admin_password(self):
        """
        **[Required]** Gets the admin_password of this CreateDatabaseFromAnotherDatabaseDetails.
        A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :return: The admin_password of this CreateDatabaseFromAnotherDatabaseDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateDatabaseFromAnotherDatabaseDetails.
        A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :param admin_password: The admin_password of this CreateDatabaseFromAnotherDatabaseDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def db_unique_name(self):
        """
        Gets the db_unique_name of this CreateDatabaseFromAnotherDatabaseDetails.
        The `DB_UNIQUE_NAME` of the Oracle Database being backed up.


        :return: The db_unique_name of this CreateDatabaseFromAnotherDatabaseDetails.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this CreateDatabaseFromAnotherDatabaseDetails.
        The `DB_UNIQUE_NAME` of the Oracle Database being backed up.


        :param db_unique_name: The db_unique_name of this CreateDatabaseFromAnotherDatabaseDetails.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def db_name(self):
        """
        Gets the db_name of this CreateDatabaseFromAnotherDatabaseDetails.
        The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.


        :return: The db_name of this CreateDatabaseFromAnotherDatabaseDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this CreateDatabaseFromAnotherDatabaseDetails.
        The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.


        :param db_name: The db_name of this CreateDatabaseFromAnotherDatabaseDetails.
        :type: str
        """
        self._db_name = db_name

    @property
    def time_stamp_for_point_in_time_recovery(self):
        """
        Gets the time_stamp_for_point_in_time_recovery of this CreateDatabaseFromAnotherDatabaseDetails.
        The point in time of the original database from which the new database is created. If not specifed, the latest backup is used to create the database.


        :return: The time_stamp_for_point_in_time_recovery of this CreateDatabaseFromAnotherDatabaseDetails.
        :rtype: datetime
        """
        return self._time_stamp_for_point_in_time_recovery

    @time_stamp_for_point_in_time_recovery.setter
    def time_stamp_for_point_in_time_recovery(self, time_stamp_for_point_in_time_recovery):
        """
        Sets the time_stamp_for_point_in_time_recovery of this CreateDatabaseFromAnotherDatabaseDetails.
        The point in time of the original database from which the new database is created. If not specifed, the latest backup is used to create the database.


        :param time_stamp_for_point_in_time_recovery: The time_stamp_for_point_in_time_recovery of this CreateDatabaseFromAnotherDatabaseDetails.
        :type: datetime
        """
        self._time_stamp_for_point_in_time_recovery = time_stamp_for_point_in_time_recovery

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
