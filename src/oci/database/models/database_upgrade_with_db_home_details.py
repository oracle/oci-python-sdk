# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_upgrade_source_base import DatabaseUpgradeSourceBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseUpgradeWithDbHomeDetails(DatabaseUpgradeSourceBase):
    """
    Details of Database Home to be used to upgrade a database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseUpgradeWithDbHomeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.DatabaseUpgradeWithDbHomeDetails.source` attribute
        of this class is ``DB_HOME`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this DatabaseUpgradeWithDbHomeDetails.
            Allowed values for this property are: "DB_HOME", "DB_VERSION", "DB_SOFTWARE_IMAGE"
        :type source: str

        :param db_home_id:
            The value to assign to the db_home_id property of this DatabaseUpgradeWithDbHomeDetails.
        :type db_home_id: str

        """
        self.swagger_types = {
            'source': 'str',
            'db_home_id': 'str'
        }

        self.attribute_map = {
            'source': 'source',
            'db_home_id': 'dbHomeId'
        }

        self._source = None
        self._db_home_id = None
        self._source = 'DB_HOME'

    @property
    def db_home_id(self):
        """
        **[Required]** Gets the db_home_id of this DatabaseUpgradeWithDbHomeDetails.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_home_id of this DatabaseUpgradeWithDbHomeDetails.
        :rtype: str
        """
        return self._db_home_id

    @db_home_id.setter
    def db_home_id(self, db_home_id):
        """
        Sets the db_home_id of this DatabaseUpgradeWithDbHomeDetails.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_home_id: The db_home_id of this DatabaseUpgradeWithDbHomeDetails.
        :type: str
        """
        self._db_home_id = db_home_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
