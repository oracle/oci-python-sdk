# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeFromBackupDetails(object):
    """
    Details for creating a database home if you are creating a database by restoring from a database backup.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeFromBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database:
            The value to assign to the database property of this CreateDbHomeFromBackupDetails.
        :type database: CreateDatabaseFromBackupDetails

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeFromBackupDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'database': 'CreateDatabaseFromBackupDetails',
            'display_name': 'str'
        }

        self.attribute_map = {
            'database': 'database',
            'display_name': 'displayName'
        }

        self._database = None
        self._display_name = None

    @property
    def database(self):
        """
        **[Required]** Gets the database of this CreateDbHomeFromBackupDetails.

        :return: The database of this CreateDbHomeFromBackupDetails.
        :rtype: CreateDatabaseFromBackupDetails
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this CreateDbHomeFromBackupDetails.

        :param database: The database of this CreateDbHomeFromBackupDetails.
        :type: CreateDatabaseFromBackupDetails
        """
        self._database = database

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDbHomeFromBackupDetails.
        The user-provided name of the database home.


        :return: The display_name of this CreateDbHomeFromBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDbHomeFromBackupDetails.
        The user-provided name of the database home.


        :param display_name: The display_name of this CreateDbHomeFromBackupDetails.
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
