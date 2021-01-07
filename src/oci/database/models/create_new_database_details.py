# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_database_base import CreateDatabaseBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNewDatabaseDetails(CreateDatabaseBase):
    """
    Details for creating a new database.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNewDatabaseDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateNewDatabaseDetails.source` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_home_id:
            The value to assign to the db_home_id property of this CreateNewDatabaseDetails.
        :type db_home_id: str

        :param db_version:
            The value to assign to the db_version property of this CreateNewDatabaseDetails.
        :type db_version: str

        :param source:
            The value to assign to the source property of this CreateNewDatabaseDetails.
            Allowed values for this property are: "NONE", "DB_BACKUP"
        :type source: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateNewDatabaseDetails.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this CreateNewDatabaseDetails.
        :type kms_key_version_id: str

        :param database:
            The value to assign to the database property of this CreateNewDatabaseDetails.
        :type database: oci.database.models.CreateDatabaseDetails

        """
        self.swagger_types = {
            'db_home_id': 'str',
            'db_version': 'str',
            'source': 'str',
            'kms_key_id': 'str',
            'kms_key_version_id': 'str',
            'database': 'CreateDatabaseDetails'
        }

        self.attribute_map = {
            'db_home_id': 'dbHomeId',
            'db_version': 'dbVersion',
            'source': 'source',
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'database': 'database'
        }

        self._db_home_id = None
        self._db_version = None
        self._source = None
        self._kms_key_id = None
        self._kms_key_version_id = None
        self._database = None
        self._source = 'NONE'

    @property
    def database(self):
        """
        **[Required]** Gets the database of this CreateNewDatabaseDetails.

        :return: The database of this CreateNewDatabaseDetails.
        :rtype: oci.database.models.CreateDatabaseDetails
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this CreateNewDatabaseDetails.

        :param database: The database of this CreateNewDatabaseDetails.
        :type: oci.database.models.CreateDatabaseDetails
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
