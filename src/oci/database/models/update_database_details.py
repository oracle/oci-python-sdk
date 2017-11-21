# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDatabaseDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDatabaseDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_backup_config:
            The value to assign to the db_backup_config property of this UpdateDatabaseDetails.
        :type db_backup_config: DbBackupConfig

        """
        self.swagger_types = {
            'db_backup_config': 'DbBackupConfig'
        }

        self.attribute_map = {
            'db_backup_config': 'dbBackupConfig'
        }

        self._db_backup_config = None

    @property
    def db_backup_config(self):
        """
        Gets the db_backup_config of this UpdateDatabaseDetails.

        :return: The db_backup_config of this UpdateDatabaseDetails.
        :rtype: DbBackupConfig
        """
        return self._db_backup_config

    @db_backup_config.setter
    def db_backup_config(self, db_backup_config):
        """
        Sets the db_backup_config of this UpdateDatabaseDetails.

        :param db_backup_config: The db_backup_config of this UpdateDatabaseDetails.
        :type: DbBackupConfig
        """
        self._db_backup_config = db_backup_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
