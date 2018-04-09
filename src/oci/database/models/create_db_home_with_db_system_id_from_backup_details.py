# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .create_db_home_with_db_system_id_base import CreateDbHomeWithDbSystemIdBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeWithDbSystemIdFromBackupDetails(CreateDbHomeWithDbSystemIdBase):
    """
    CreateDbHomeWithDbSystemIdFromBackupDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeWithDbSystemIdFromBackupDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDbHomeWithDbSystemIdFromBackupDetails.source` attribute
        of this class is ``DB_BACKUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_system_id:
            The value to assign to the db_system_id property of this CreateDbHomeWithDbSystemIdFromBackupDetails.
        :type db_system_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeWithDbSystemIdFromBackupDetails.
        :type display_name: str

        :param source:
            The value to assign to the source property of this CreateDbHomeWithDbSystemIdFromBackupDetails.
            Allowed values for this property are: "NONE", "DB_BACKUP"
        :type source: str

        :param database:
            The value to assign to the database property of this CreateDbHomeWithDbSystemIdFromBackupDetails.
        :type database: CreateDatabaseFromBackupDetails

        """
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
        **[Required]** Gets the database of this CreateDbHomeWithDbSystemIdFromBackupDetails.

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
