# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database:
            The value to assign to the database property of this CreateDbHomeDetails.
        :type database: CreateDatabaseDetails

        :param db_version:
            The value to assign to the db_version property of this CreateDbHomeDetails.
        :type db_version: str

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'database': 'CreateDatabaseDetails',
            'db_version': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'database': 'database',
            'db_version': 'dbVersion',
            'display_name': 'displayName'
        }

        self._database = None
        self._db_version = None
        self._display_name = None

    @property
    def database(self):
        """
        Gets the database of this CreateDbHomeDetails.

        :return: The database of this CreateDbHomeDetails.
        :rtype: CreateDatabaseDetails
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this CreateDbHomeDetails.

        :param database: The database of this CreateDbHomeDetails.
        :type: CreateDatabaseDetails
        """
        self._database = database

    @property
    def db_version(self):
        """
        Gets the db_version of this CreateDbHomeDetails.
        A valid Oracle database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :return: The db_version of this CreateDbHomeDetails.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this CreateDbHomeDetails.
        A valid Oracle database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :param db_version: The db_version of this CreateDbHomeDetails.
        :type: str
        """
        self._db_version = db_version

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDbHomeDetails.
        The user-provided name of the database home.


        :return: The display_name of this CreateDbHomeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDbHomeDetails.
        The user-provided name of the database home.


        :param display_name: The display_name of this CreateDbHomeDetails.
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
