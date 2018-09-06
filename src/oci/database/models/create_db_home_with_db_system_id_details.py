# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .create_db_home_with_db_system_id_base import CreateDbHomeWithDbSystemIdBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeWithDbSystemIdDetails(CreateDbHomeWithDbSystemIdBase):
    """
    CreateDbHomeWithDbSystemIdDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeWithDbSystemIdDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDbHomeWithDbSystemIdDetails.source` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_system_id:
            The value to assign to the db_system_id property of this CreateDbHomeWithDbSystemIdDetails.
        :type db_system_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeWithDbSystemIdDetails.
        :type display_name: str

        :param source:
            The value to assign to the source property of this CreateDbHomeWithDbSystemIdDetails.
            Allowed values for this property are: "NONE", "DB_BACKUP"
        :type source: str

        :param database:
            The value to assign to the database property of this CreateDbHomeWithDbSystemIdDetails.
        :type database: CreateDatabaseDetails

        :param db_version:
            The value to assign to the db_version property of this CreateDbHomeWithDbSystemIdDetails.
        :type db_version: str

        """
        self.swagger_types = {
            'db_system_id': 'str',
            'display_name': 'str',
            'source': 'str',
            'database': 'CreateDatabaseDetails',
            'db_version': 'str'
        }

        self.attribute_map = {
            'db_system_id': 'dbSystemId',
            'display_name': 'displayName',
            'source': 'source',
            'database': 'database',
            'db_version': 'dbVersion'
        }

        self._db_system_id = None
        self._display_name = None
        self._source = None
        self._database = None
        self._db_version = None
        self._source = 'NONE'

    @property
    def database(self):
        """
        **[Required]** Gets the database of this CreateDbHomeWithDbSystemIdDetails.

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
    def db_version(self):
        """
        **[Required]** Gets the db_version of this CreateDbHomeWithDbSystemIdDetails.
        A valid Oracle Database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :return: The db_version of this CreateDbHomeWithDbSystemIdDetails.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this CreateDbHomeWithDbSystemIdDetails.
        A valid Oracle Database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :param db_version: The db_version of this CreateDbHomeWithDbSystemIdDetails.
        :type: str
        """
        self._db_version = db_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
