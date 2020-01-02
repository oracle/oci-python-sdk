# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousContainerDatabaseBackupConfig(object):
    """
    Backup options for the Autonomous Container Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousContainerDatabaseBackupConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recovery_window_in_days:
            The value to assign to the recovery_window_in_days property of this AutonomousContainerDatabaseBackupConfig.
        :type recovery_window_in_days: int

        """
        self.swagger_types = {
            'recovery_window_in_days': 'int'
        }

        self.attribute_map = {
            'recovery_window_in_days': 'recoveryWindowInDays'
        }

        self._recovery_window_in_days = None

    @property
    def recovery_window_in_days(self):
        """
        Gets the recovery_window_in_days of this AutonomousContainerDatabaseBackupConfig.
        Number of days between the current and the earliest point of recoverability covered by automatic backups.
        This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window.
        When the value is updated, it is applied to all existing automatic backups.


        :return: The recovery_window_in_days of this AutonomousContainerDatabaseBackupConfig.
        :rtype: int
        """
        return self._recovery_window_in_days

    @recovery_window_in_days.setter
    def recovery_window_in_days(self, recovery_window_in_days):
        """
        Sets the recovery_window_in_days of this AutonomousContainerDatabaseBackupConfig.
        Number of days between the current and the earliest point of recoverability covered by automatic backups.
        This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window.
        When the value is updated, it is applied to all existing automatic backups.


        :param recovery_window_in_days: The recovery_window_in_days of this AutonomousContainerDatabaseBackupConfig.
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
