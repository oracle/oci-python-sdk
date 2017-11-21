# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeWithDbSystemIdBase(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeWithDbSystemIdBase object with values from values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.CreateDbHomeWithDbSystemIdFromBackupDetails`
        * :class:`~oci.database.models.CreateDbHomeWithDbSystemIdDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_system_id:
            The value to assign to the db_system_id property of this CreateDbHomeWithDbSystemIdBase.
        :type db_system_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeWithDbSystemIdBase.
        :type display_name: str

        :param source:
            The value to assign to the source property of this CreateDbHomeWithDbSystemIdBase.
            Allowed values for this property are: "NONE", "DB_BACKUP"
        :type source: str

        """
        self.swagger_types = {
            'db_system_id': 'str',
            'display_name': 'str',
            'source': 'str'
        }

        self.attribute_map = {
            'db_system_id': 'dbSystemId',
            'display_name': 'displayName',
            'source': 'source'
        }

        self._db_system_id = None
        self._display_name = None
        self._source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'DB_BACKUP':
            return 'CreateDbHomeWithDbSystemIdFromBackupDetails'

        if type == 'NONE':
            return 'CreateDbHomeWithDbSystemIdDetails'
        else:
            return 'CreateDbHomeWithDbSystemIdBase'

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this CreateDbHomeWithDbSystemIdBase.
        The OCID of the DB System.


        :return: The db_system_id of this CreateDbHomeWithDbSystemIdBase.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this CreateDbHomeWithDbSystemIdBase.
        The OCID of the DB System.


        :param db_system_id: The db_system_id of this CreateDbHomeWithDbSystemIdBase.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDbHomeWithDbSystemIdBase.
        The user-provided name of the database home.


        :return: The display_name of this CreateDbHomeWithDbSystemIdBase.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDbHomeWithDbSystemIdBase.
        The user-provided name of the database home.


        :param display_name: The display_name of this CreateDbHomeWithDbSystemIdBase.
        :type: str
        """
        self._display_name = display_name

    @property
    def source(self):
        """
        Gets the source of this CreateDbHomeWithDbSystemIdBase.
        Source of database:
          NONE for creating a new database
          DB_BACKUP for creating a new database by restoring a backup

        Allowed values for this property are: "NONE", "DB_BACKUP"


        :return: The source of this CreateDbHomeWithDbSystemIdBase.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateDbHomeWithDbSystemIdBase.
        Source of database:
          NONE for creating a new database
          DB_BACKUP for creating a new database by restoring a backup


        :param source: The source of this CreateDbHomeWithDbSystemIdBase.
        :type: str
        """
        allowed_values = ["NONE", "DB_BACKUP"]
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source`, must be one of {0}"
                .format(allowed_values)
            )
        self._source = source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
