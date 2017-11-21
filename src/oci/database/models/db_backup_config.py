# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbBackupConfig(object):

    def __init__(self, **kwargs):
        """
        Initializes a new DbBackupConfig object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param auto_backup_enabled:
            The value to assign to the auto_backup_enabled property of this DbBackupConfig.
        :type auto_backup_enabled: bool

        """
        self.swagger_types = {
            'auto_backup_enabled': 'bool'
        }

        self.attribute_map = {
            'auto_backup_enabled': 'autoBackupEnabled'
        }

        self._auto_backup_enabled = None

    @property
    def auto_backup_enabled(self):
        """
        Gets the auto_backup_enabled of this DbBackupConfig.
        If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.


        :return: The auto_backup_enabled of this DbBackupConfig.
        :rtype: bool
        """
        return self._auto_backup_enabled

    @auto_backup_enabled.setter
    def auto_backup_enabled(self, auto_backup_enabled):
        """
        Sets the auto_backup_enabled of this DbBackupConfig.
        If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.


        :param auto_backup_enabled: The auto_backup_enabled of this DbBackupConfig.
        :type: bool
        """
        self._auto_backup_enabled = auto_backup_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
