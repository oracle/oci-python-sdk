# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbBackupConfig(object):
    """
    Backup Options
    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_ONE"
    AUTO_BACKUP_WINDOW_SLOT_ONE = "SLOT_ONE"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_TWO"
    AUTO_BACKUP_WINDOW_SLOT_TWO = "SLOT_TWO"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_THREE"
    AUTO_BACKUP_WINDOW_SLOT_THREE = "SLOT_THREE"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_FOUR"
    AUTO_BACKUP_WINDOW_SLOT_FOUR = "SLOT_FOUR"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_FIVE"
    AUTO_BACKUP_WINDOW_SLOT_FIVE = "SLOT_FIVE"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_SIX"
    AUTO_BACKUP_WINDOW_SLOT_SIX = "SLOT_SIX"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_SEVEN"
    AUTO_BACKUP_WINDOW_SLOT_SEVEN = "SLOT_SEVEN"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_EIGHT"
    AUTO_BACKUP_WINDOW_SLOT_EIGHT = "SLOT_EIGHT"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_NINE"
    AUTO_BACKUP_WINDOW_SLOT_NINE = "SLOT_NINE"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_TEN"
    AUTO_BACKUP_WINDOW_SLOT_TEN = "SLOT_TEN"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_ELEVEN"
    AUTO_BACKUP_WINDOW_SLOT_ELEVEN = "SLOT_ELEVEN"

    #: A constant which can be used with the auto_backup_window property of a DbBackupConfig.
    #: This constant has a value of "SLOT_TWELVE"
    AUTO_BACKUP_WINDOW_SLOT_TWELVE = "SLOT_TWELVE"

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

        :param auto_backup_window:
            The value to assign to the auto_backup_window property of this DbBackupConfig.
            Allowed values for this property are: "SLOT_ONE", "SLOT_TWO", "SLOT_THREE", "SLOT_FOUR", "SLOT_FIVE", "SLOT_SIX", "SLOT_SEVEN", "SLOT_EIGHT", "SLOT_NINE", "SLOT_TEN", "SLOT_ELEVEN", "SLOT_TWELVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type auto_backup_window: str

        :param backup_destination_details:
            The value to assign to the backup_destination_details property of this DbBackupConfig.
        :type backup_destination_details: list[oci.database.models.BackupDestinationDetails]

        """
        self.swagger_types = {
            'auto_backup_enabled': 'bool',
            'recovery_window_in_days': 'int',
            'auto_backup_window': 'str',
            'backup_destination_details': 'list[BackupDestinationDetails]'
        }

        self.attribute_map = {
            'auto_backup_enabled': 'autoBackupEnabled',
            'recovery_window_in_days': 'recoveryWindowInDays',
            'auto_backup_window': 'autoBackupWindow',
            'backup_destination_details': 'backupDestinationDetails'
        }

        self._auto_backup_enabled = None
        self._recovery_window_in_days = None
        self._auto_backup_window = None
        self._backup_destination_details = None

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

    @property
    def auto_backup_window(self):
        """
        Gets the auto_backup_window of this DbBackupConfig.
        Time window selected for initiating automatic backup for the database system. There are twelve available two-hour time windows. If no option is selected, a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM (exclusive).

        Example: `SLOT_TWO`

        Allowed values for this property are: "SLOT_ONE", "SLOT_TWO", "SLOT_THREE", "SLOT_FOUR", "SLOT_FIVE", "SLOT_SIX", "SLOT_SEVEN", "SLOT_EIGHT", "SLOT_NINE", "SLOT_TEN", "SLOT_ELEVEN", "SLOT_TWELVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The auto_backup_window of this DbBackupConfig.
        :rtype: str
        """
        return self._auto_backup_window

    @auto_backup_window.setter
    def auto_backup_window(self, auto_backup_window):
        """
        Sets the auto_backup_window of this DbBackupConfig.
        Time window selected for initiating automatic backup for the database system. There are twelve available two-hour time windows. If no option is selected, a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM (exclusive).

        Example: `SLOT_TWO`


        :param auto_backup_window: The auto_backup_window of this DbBackupConfig.
        :type: str
        """
        allowed_values = ["SLOT_ONE", "SLOT_TWO", "SLOT_THREE", "SLOT_FOUR", "SLOT_FIVE", "SLOT_SIX", "SLOT_SEVEN", "SLOT_EIGHT", "SLOT_NINE", "SLOT_TEN", "SLOT_ELEVEN", "SLOT_TWELVE"]
        if not value_allowed_none_or_none_sentinel(auto_backup_window, allowed_values):
            auto_backup_window = 'UNKNOWN_ENUM_VALUE'
        self._auto_backup_window = auto_backup_window

    @property
    def backup_destination_details(self):
        """
        Gets the backup_destination_details of this DbBackupConfig.
        Backup destination details.


        :return: The backup_destination_details of this DbBackupConfig.
        :rtype: list[oci.database.models.BackupDestinationDetails]
        """
        return self._backup_destination_details

    @backup_destination_details.setter
    def backup_destination_details(self, backup_destination_details):
        """
        Sets the backup_destination_details of this DbBackupConfig.
        Backup destination details.


        :param backup_destination_details: The backup_destination_details of this DbBackupConfig.
        :type: list[oci.database.models.BackupDestinationDetails]
        """
        self._backup_destination_details = backup_destination_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
