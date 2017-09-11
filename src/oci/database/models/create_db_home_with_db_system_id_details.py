# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateDbHomeWithDbSystemIdDetails(object):

    def __init__(self):

        self.swagger_types = {
            'database': 'CreateDatabaseDetails',
            'db_system_id': 'str',
            'db_version': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'database': 'database',
            'db_system_id': 'dbSystemId',
            'db_version': 'dbVersion',
            'display_name': 'displayName'
        }

        self._database = None
        self._db_system_id = None
        self._db_version = None
        self._display_name = None

    @property
    def database(self):
        """
        Gets the database of this CreateDbHomeWithDbSystemIdDetails.

        :return: The database of this CreateDbHomeWithDbSystemIdDetails.
        :rtype: CreateDatabaseDetails
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this CreateDbHomeWithDbSystemIdDetails.

        :param database: The database of this CreateDbHomeWithDbSystemIdDetails.
        :type: CreateDatabaseDetails
        """
        self._database = database

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this CreateDbHomeWithDbSystemIdDetails.
        The OCID of the DB System.


        :return: The db_system_id of this CreateDbHomeWithDbSystemIdDetails.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this CreateDbHomeWithDbSystemIdDetails.
        The OCID of the DB System.


        :param db_system_id: The db_system_id of this CreateDbHomeWithDbSystemIdDetails.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def db_version(self):
        """
        Gets the db_version of this CreateDbHomeWithDbSystemIdDetails.
        A valid Oracle database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :return: The db_version of this CreateDbHomeWithDbSystemIdDetails.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this CreateDbHomeWithDbSystemIdDetails.
        A valid Oracle database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :param db_version: The db_version of this CreateDbHomeWithDbSystemIdDetails.
        :type: str
        """
        self._db_version = db_version

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDbHomeWithDbSystemIdDetails.
        The user-provided name of the database home.


        :return: The display_name of this CreateDbHomeWithDbSystemIdDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDbHomeWithDbSystemIdDetails.
        The user-provided name of the database home.


        :param display_name: The display_name of this CreateDbHomeWithDbSystemIdDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
