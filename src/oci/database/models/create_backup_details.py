# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBackupDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBackupDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_id:
            The value to assign to the database_id property of this CreateBackupDetails.
        :type database_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateBackupDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'database_id': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'database_id': 'databaseId',
            'display_name': 'displayName'
        }

        self._database_id = None
        self._display_name = None

    @property
    def database_id(self):
        """
        Gets the database_id of this CreateBackupDetails.
        The OCID of the database.


        :return: The database_id of this CreateBackupDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this CreateBackupDetails.
        The OCID of the database.


        :param database_id: The database_id of this CreateBackupDetails.
        :type: str
        """
        self._database_id = database_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateBackupDetails.
        The user-friendly name for the backup. It does not have to be unique.


        :return: The display_name of this CreateBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBackupDetails.
        The user-friendly name for the backup. It does not have to be unique.


        :param display_name: The display_name of this CreateBackupDetails.
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
