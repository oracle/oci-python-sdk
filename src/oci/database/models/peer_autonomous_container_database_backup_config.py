# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PeerAutonomousContainerDatabaseBackupConfig(object):
    """
    Backup options for the standby Autonomous Container Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PeerAutonomousContainerDatabaseBackupConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backup_destination_details:
            The value to assign to the backup_destination_details property of this PeerAutonomousContainerDatabaseBackupConfig.
        :type backup_destination_details: list[oci.database.models.BackupDestinationDetails]

        :param recovery_window_in_days:
            The value to assign to the recovery_window_in_days property of this PeerAutonomousContainerDatabaseBackupConfig.
        :type recovery_window_in_days: int

        """
        self.swagger_types = {
            'backup_destination_details': 'list[BackupDestinationDetails]',
            'recovery_window_in_days': 'int'
        }

        self.attribute_map = {
            'backup_destination_details': 'backupDestinationDetails',
            'recovery_window_in_days': 'recoveryWindowInDays'
        }

        self._backup_destination_details = None
        self._recovery_window_in_days = None

    @property
    def backup_destination_details(self):
        """
        Gets the backup_destination_details of this PeerAutonomousContainerDatabaseBackupConfig.
        Backup destination details.


        :return: The backup_destination_details of this PeerAutonomousContainerDatabaseBackupConfig.
        :rtype: list[oci.database.models.BackupDestinationDetails]
        """
        return self._backup_destination_details

    @backup_destination_details.setter
    def backup_destination_details(self, backup_destination_details):
        """
        Sets the backup_destination_details of this PeerAutonomousContainerDatabaseBackupConfig.
        Backup destination details.


        :param backup_destination_details: The backup_destination_details of this PeerAutonomousContainerDatabaseBackupConfig.
        :type: list[oci.database.models.BackupDestinationDetails]
        """
        self._backup_destination_details = backup_destination_details

    @property
    def recovery_window_in_days(self):
        """
        Gets the recovery_window_in_days of this PeerAutonomousContainerDatabaseBackupConfig.
        Number of days between the current and the earliest point of recoverability covered by automatic backups.
        This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window.
        When the value is updated, it is applied to all existing automatic backups.


        :return: The recovery_window_in_days of this PeerAutonomousContainerDatabaseBackupConfig.
        :rtype: int
        """
        return self._recovery_window_in_days

    @recovery_window_in_days.setter
    def recovery_window_in_days(self, recovery_window_in_days):
        """
        Sets the recovery_window_in_days of this PeerAutonomousContainerDatabaseBackupConfig.
        Number of days between the current and the earliest point of recoverability covered by automatic backups.
        This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window.
        When the value is updated, it is applied to all existing automatic backups.


        :param recovery_window_in_days: The recovery_window_in_days of this PeerAutonomousContainerDatabaseBackupConfig.
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
