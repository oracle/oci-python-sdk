# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .create_db_home_with_db_system_id_base import CreateDbHomeWithDbSystemIdBase
from ...util import formatted_flat_dict


class CreateDbHomeWithDbSystemIdFromBackupDetails(CreateDbHomeWithDbSystemIdBase):

    def __init__(self):

        self.swagger_types = {
            'db_system_id': 'str',
            'display_name': 'str',
            'source': 'str',
            'database': 'CreateDatabaseFromBackupDetails'
        }

        self.attribute_map = {
            'db_system_id': 'dbSystemId',
            'display_name': 'displayName',
            'source': 'source',
            'database': 'database'
        }

        self._db_system_id = None
        self._display_name = None
        self._source = None
        self._database = None
        self._source = 'DB_BACKUP'

    @property
    def database(self):
        """
        Gets the database of this CreateDbHomeWithDbSystemIdFromBackupDetails.

        :return: The database of this CreateDbHomeWithDbSystemIdFromBackupDetails.
        :rtype: CreateDatabaseFromBackupDetails
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this CreateDbHomeWithDbSystemIdFromBackupDetails.

        :param database: The database of this CreateDbHomeWithDbSystemIdFromBackupDetails.
        :type: CreateDatabaseFromBackupDetails
        """
        self._database = database

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
