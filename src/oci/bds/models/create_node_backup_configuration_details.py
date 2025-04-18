# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNodeBackupConfigurationDetails(object):
    """
    The information about the NodeBackupConfiguration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNodeBackupConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level_type_details:
            The value to assign to the level_type_details property of this CreateNodeBackupConfigurationDetails.
        :type level_type_details: oci.bds.models.LevelTypeDetails

        :param display_name:
            The value to assign to the display_name property of this CreateNodeBackupConfigurationDetails.
        :type display_name: str

        :param timezone:
            The value to assign to the timezone property of this CreateNodeBackupConfigurationDetails.
        :type timezone: str

        :param schedule:
            The value to assign to the schedule property of this CreateNodeBackupConfigurationDetails.
        :type schedule: str

        :param number_of_backups_to_retain:
            The value to assign to the number_of_backups_to_retain property of this CreateNodeBackupConfigurationDetails.
        :type number_of_backups_to_retain: int

        :param backup_type:
            The value to assign to the backup_type property of this CreateNodeBackupConfigurationDetails.
        :type backup_type: str

        """
        self.swagger_types = {
            'level_type_details': 'LevelTypeDetails',
            'display_name': 'str',
            'timezone': 'str',
            'schedule': 'str',
            'number_of_backups_to_retain': 'int',
            'backup_type': 'str'
        }
        self.attribute_map = {
            'level_type_details': 'levelTypeDetails',
            'display_name': 'displayName',
            'timezone': 'timezone',
            'schedule': 'schedule',
            'number_of_backups_to_retain': 'numberOfBackupsToRetain',
            'backup_type': 'backupType'
        }
        self._level_type_details = None
        self._display_name = None
        self._timezone = None
        self._schedule = None
        self._number_of_backups_to_retain = None
        self._backup_type = None

    @property
    def level_type_details(self):
        """
        **[Required]** Gets the level_type_details of this CreateNodeBackupConfigurationDetails.

        :return: The level_type_details of this CreateNodeBackupConfigurationDetails.
        :rtype: oci.bds.models.LevelTypeDetails
        """
        return self._level_type_details

    @level_type_details.setter
    def level_type_details(self, level_type_details):
        """
        Sets the level_type_details of this CreateNodeBackupConfigurationDetails.

        :param level_type_details: The level_type_details of this CreateNodeBackupConfigurationDetails.
        :type: oci.bds.models.LevelTypeDetails
        """
        self._level_type_details = level_type_details

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateNodeBackupConfigurationDetails.
        A user-friendly name. Only ASCII alphanumeric characters with no spaces allowed. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :return: The display_name of this CreateNodeBackupConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateNodeBackupConfigurationDetails.
        A user-friendly name. Only ASCII alphanumeric characters with no spaces allowed. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :param display_name: The display_name of this CreateNodeBackupConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def timezone(self):
        """
        Gets the timezone of this CreateNodeBackupConfigurationDetails.
        The time zone of the execution schedule, in IANA time zone database name format


        :return: The timezone of this CreateNodeBackupConfigurationDetails.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this CreateNodeBackupConfigurationDetails.
        The time zone of the execution schedule, in IANA time zone database name format


        :param timezone: The timezone of this CreateNodeBackupConfigurationDetails.
        :type: str
        """
        self._timezone = timezone

    @property
    def schedule(self):
        """
        **[Required]** Gets the schedule of this CreateNodeBackupConfigurationDetails.
        Day/time recurrence (specified following RFC 5545) at which to trigger the backup process. Currently only DAILY, WEEKLY and MONTHLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR. Other fields are not supported.


        :return: The schedule of this CreateNodeBackupConfigurationDetails.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this CreateNodeBackupConfigurationDetails.
        Day/time recurrence (specified following RFC 5545) at which to trigger the backup process. Currently only DAILY, WEEKLY and MONTHLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR. Other fields are not supported.


        :param schedule: The schedule of this CreateNodeBackupConfigurationDetails.
        :type: str
        """
        self._schedule = schedule

    @property
    def number_of_backups_to_retain(self):
        """
        Gets the number_of_backups_to_retain of this CreateNodeBackupConfigurationDetails.
        Number of backup copies to retain.


        :return: The number_of_backups_to_retain of this CreateNodeBackupConfigurationDetails.
        :rtype: int
        """
        return self._number_of_backups_to_retain

    @number_of_backups_to_retain.setter
    def number_of_backups_to_retain(self, number_of_backups_to_retain):
        """
        Sets the number_of_backups_to_retain of this CreateNodeBackupConfigurationDetails.
        Number of backup copies to retain.


        :param number_of_backups_to_retain: The number_of_backups_to_retain of this CreateNodeBackupConfigurationDetails.
        :type: int
        """
        self._number_of_backups_to_retain = number_of_backups_to_retain

    @property
    def backup_type(self):
        """
        Gets the backup_type of this CreateNodeBackupConfigurationDetails.
        Incremental backup type includes only the changes since the last backup. Full backup type includes all changes since the volume was created.


        :return: The backup_type of this CreateNodeBackupConfigurationDetails.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this CreateNodeBackupConfigurationDetails.
        Incremental backup type includes only the changes since the last backup. Full backup type includes all changes since the volume was created.


        :param backup_type: The backup_type of this CreateNodeBackupConfigurationDetails.
        :type: str
        """
        self._backup_type = backup_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
