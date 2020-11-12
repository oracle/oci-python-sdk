# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_upgrade_source_base import DatabaseUpgradeSourceBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseUpgradeWithDbVersionDetails(DatabaseUpgradeSourceBase):
    """
    Details of Database version for upgrading a database.
    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseUpgradeWithDbVersionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.DatabaseUpgradeWithDbVersionDetails.source` attribute
        of this class is ``DB_VERSION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this DatabaseUpgradeWithDbVersionDetails.
            Allowed values for this property are: "DB_HOME", "DB_VERSION", "DB_SOFTWARE_IMAGE"
        :type source: str

        :param db_version:
            The value to assign to the db_version property of this DatabaseUpgradeWithDbVersionDetails.
        :type db_version: str

        """
        self.swagger_types = {
            'source': 'str',
            'db_version': 'str'
        }

        self.attribute_map = {
            'source': 'source',
            'db_version': 'dbVersion'
        }

        self._source = None
        self._db_version = None
        self._source = 'DB_VERSION'

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this DatabaseUpgradeWithDbVersionDetails.
        A valid Oracle Database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :return: The db_version of this DatabaseUpgradeWithDbVersionDetails.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this DatabaseUpgradeWithDbVersionDetails.
        A valid Oracle Database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :param db_version: The db_version of this DatabaseUpgradeWithDbVersionDetails.
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
