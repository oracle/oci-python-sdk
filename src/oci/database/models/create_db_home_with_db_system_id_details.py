# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_db_home_base import CreateDbHomeBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeWithDbSystemIdDetails(CreateDbHomeBase):
    """
    Note that a valid `dbSystemId` value must be supplied for the `CreateDbHomeWithDbSystemId` API operation to successfully complete.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeWithDbSystemIdDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDbHomeWithDbSystemIdDetails.source` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeWithDbSystemIdDetails.
        :type display_name: str

        :param source:
            The value to assign to the source property of this CreateDbHomeWithDbSystemIdDetails.
            Allowed values for this property are: "NONE", "DB_BACKUP", "VM_CLUSTER_NEW"
        :type source: str

        :param db_system_id:
            The value to assign to the db_system_id property of this CreateDbHomeWithDbSystemIdDetails.
        :type db_system_id: str

        :param db_version:
            The value to assign to the db_version property of this CreateDbHomeWithDbSystemIdDetails.
        :type db_version: str

        :param database:
            The value to assign to the database property of this CreateDbHomeWithDbSystemIdDetails.
        :type database: CreateDatabaseDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'source': 'str',
            'db_system_id': 'str',
            'db_version': 'str',
            'database': 'CreateDatabaseDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'source': 'source',
            'db_system_id': 'dbSystemId',
            'db_version': 'dbVersion',
            'database': 'database'
        }

        self._display_name = None
        self._source = None
        self._db_system_id = None
        self._db_version = None
        self._database = None
        self._source = 'NONE'

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this CreateDbHomeWithDbSystemIdDetails.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_system_id of this CreateDbHomeWithDbSystemIdDetails.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this CreateDbHomeWithDbSystemIdDetails.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_system_id: The db_system_id of this CreateDbHomeWithDbSystemIdDetails.
        :type: str
        """
        self._db_system_id = db_system_id

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
