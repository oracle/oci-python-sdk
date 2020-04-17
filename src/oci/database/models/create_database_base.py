# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseBase(object):
    """
    Details for creating a database.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the source property of a CreateDatabaseBase.
    #: This constant has a value of "NONE"
    SOURCE_NONE = "NONE"

    #: A constant which can be used with the source property of a CreateDatabaseBase.
    #: This constant has a value of "DB_BACKUP"
    SOURCE_DB_BACKUP = "DB_BACKUP"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.CreateNewDatabaseDetails`
        * :class:`~oci.database.models.CreateDatabaseFromBackup`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_home_id:
            The value to assign to the db_home_id property of this CreateDatabaseBase.
        :type db_home_id: str

        :param db_version:
            The value to assign to the db_version property of this CreateDatabaseBase.
        :type db_version: str

        :param source:
            The value to assign to the source property of this CreateDatabaseBase.
            Allowed values for this property are: "NONE", "DB_BACKUP"
        :type source: str

        """
        self.swagger_types = {
            'db_home_id': 'str',
            'db_version': 'str',
            'source': 'str'
        }

        self.attribute_map = {
            'db_home_id': 'dbHomeId',
            'db_version': 'dbVersion',
            'source': 'source'
        }

        self._db_home_id = None
        self._db_version = None
        self._source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'NONE':
            return 'CreateNewDatabaseDetails'

        if type == 'DB_BACKUP':
            return 'CreateDatabaseFromBackup'
        else:
            return 'CreateDatabaseBase'

    @property
    def db_home_id(self):
        """
        **[Required]** Gets the db_home_id of this CreateDatabaseBase.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_home_id of this CreateDatabaseBase.
        :rtype: str
        """
        return self._db_home_id

    @db_home_id.setter
    def db_home_id(self, db_home_id):
        """
        Sets the db_home_id of this CreateDatabaseBase.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_home_id: The db_home_id of this CreateDatabaseBase.
        :type: str
        """
        self._db_home_id = db_home_id

    @property
    def db_version(self):
        """
        Gets the db_version of this CreateDatabaseBase.
        A valid Oracle Database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :return: The db_version of this CreateDatabaseBase.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this CreateDatabaseBase.
        A valid Oracle Database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :param db_version: The db_version of this CreateDatabaseBase.
        :type: str
        """
        self._db_version = db_version

    @property
    def source(self):
        """
        **[Required]** Gets the source of this CreateDatabaseBase.
        The source of the database:
        Use `NONE` for creating a new database.
        Use `DB_BACKUP` for creating a new database by restoring from a backup.
        The default is `NONE`.

        Allowed values for this property are: "NONE", "DB_BACKUP"


        :return: The source of this CreateDatabaseBase.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateDatabaseBase.
        The source of the database:
        Use `NONE` for creating a new database.
        Use `DB_BACKUP` for creating a new database by restoring from a backup.
        The default is `NONE`.


        :param source: The source of this CreateDatabaseBase.
        :type: str
        """
        allowed_values = ["NONE", "DB_BACKUP"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            raise ValueError(
                "Invalid value for `source`, must be None or one of {0}"
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
