# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseUpgradeSourceBase(object):
    """
    Details for the database upgrade source.
    """

    #: A constant which can be used with the source property of a DatabaseUpgradeSourceBase.
    #: This constant has a value of "DB_HOME"
    SOURCE_DB_HOME = "DB_HOME"

    #: A constant which can be used with the source property of a DatabaseUpgradeSourceBase.
    #: This constant has a value of "DB_VERSION"
    SOURCE_DB_VERSION = "DB_VERSION"

    #: A constant which can be used with the source property of a DatabaseUpgradeSourceBase.
    #: This constant has a value of "DB_SOFTWARE_IMAGE"
    SOURCE_DB_SOFTWARE_IMAGE = "DB_SOFTWARE_IMAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseUpgradeSourceBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.DatabaseUpgradeWithDbHomeDetails`
        * :class:`~oci.database.models.DatabaseUpgradeWithDatabaseSoftwareImageDetails`
        * :class:`~oci.database.models.DatabaseUpgradeWithDbVersionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this DatabaseUpgradeSourceBase.
            Allowed values for this property are: "DB_HOME", "DB_VERSION", "DB_SOFTWARE_IMAGE"
        :type source: str

        """
        self.swagger_types = {
            'source': 'str'
        }

        self.attribute_map = {
            'source': 'source'
        }

        self._source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'DB_HOME':
            return 'DatabaseUpgradeWithDbHomeDetails'

        if type == 'DB_SOFTWARE_IMAGE':
            return 'DatabaseUpgradeWithDatabaseSoftwareImageDetails'

        if type == 'DB_VERSION':
            return 'DatabaseUpgradeWithDbVersionDetails'
        else:
            return 'DatabaseUpgradeSourceBase'

    @property
    def source(self):
        """
        Gets the source of this DatabaseUpgradeSourceBase.
        The source of the Oracle Database software to be used for the upgrade.
         - Use `DB_HOME` to specify an existing Database Home to upgrade the database. The database is moved to the target Database Home and makes use of the Oracle Database software version of the target Database Home.
         - Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database.
         - Use `DB_SOFTWARE_IMAGE` to specify a `database software image`__ to upgrade the database.

        __ https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm

        Allowed values for this property are: "DB_HOME", "DB_VERSION", "DB_SOFTWARE_IMAGE"


        :return: The source of this DatabaseUpgradeSourceBase.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this DatabaseUpgradeSourceBase.
        The source of the Oracle Database software to be used for the upgrade.
         - Use `DB_HOME` to specify an existing Database Home to upgrade the database. The database is moved to the target Database Home and makes use of the Oracle Database software version of the target Database Home.
         - Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database.
         - Use `DB_SOFTWARE_IMAGE` to specify a `database software image`__ to upgrade the database.

        __ https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm


        :param source: The source of this DatabaseUpgradeSourceBase.
        :type: str
        """
        allowed_values = ["DB_HOME", "DB_VERSION", "DB_SOFTWARE_IMAGE"]
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
