# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbBackupConfig(object):
    """
    Backup Options
    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbBackupConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param auto_backup_enabled:
            The value to assign to the auto_backup_enabled property of this DbBackupConfig.
        :type auto_backup_enabled: bool

        :param recovery_window_in_days:
            The value to assign to the recovery_window_in_days property of this DbBackupConfig.
        :type recovery_window_in_days: int

        """
        self.swagger_types = {
            'auto_backup_enabled': 'bool',
            'recovery_window_in_days': 'int'
        }

        self.attribute_map = {
            'auto_backup_enabled': 'autoBackupEnabled',
            'recovery_window_in_days': 'recoveryWindowInDays'
        }

        self._auto_backup_enabled = None
        self._recovery_window_in_days = None

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

    @property
    def recovery_window_in_days(self):
        """
        Gets the recovery_window_in_days of this DbBackupConfig.
        Number of days between the current and the earliest point of recoverability covered by automatic backups.
        This value applies to automatic backups only. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window.
        When the value is updated, it is applied to all existing automatic backups.


        :return: The recovery_window_in_days of this DbBackupConfig.
        :rtype: int
        """
        return self._recovery_window_in_days

    @recovery_window_in_days.setter
    def recovery_window_in_days(self, recovery_window_in_days):
        """
        Sets the recovery_window_in_days of this DbBackupConfig.
        Number of days between the current and the earliest point of recoverability covered by automatic backups.
        This value applies to automatic backups only. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window.
        When the value is updated, it is applied to all existing automatic backups.


        :param recovery_window_in_days: The recovery_window_in_days of this DbBackupConfig.
        :type: int
        """
        self._recovery_window_in_days = recovery_window_in_days

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
