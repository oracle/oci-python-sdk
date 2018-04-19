# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeBackupSchedule(object):
    """
    Defines a chronological recurrence pattern for creating scheduled backups at a particular periodicity.
    """

    #: A constant which can be used with the backup_type property of a VolumeBackupSchedule.
    #: This constant has a value of "FULL"
    BACKUP_TYPE_FULL = "FULL"

    #: A constant which can be used with the backup_type property of a VolumeBackupSchedule.
    #: This constant has a value of "INCREMENTAL"
    BACKUP_TYPE_INCREMENTAL = "INCREMENTAL"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_HOUR"
    PERIOD_ONE_HOUR = "ONE_HOUR"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_DAY"
    PERIOD_ONE_DAY = "ONE_DAY"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_WEEK"
    PERIOD_ONE_WEEK = "ONE_WEEK"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_MONTH"
    PERIOD_ONE_MONTH = "ONE_MONTH"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_YEAR"
    PERIOD_ONE_YEAR = "ONE_YEAR"

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeBackupSchedule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backup_type:
            The value to assign to the backup_type property of this VolumeBackupSchedule.
            Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type backup_type: str

        :param offset_seconds:
            The value to assign to the offset_seconds property of this VolumeBackupSchedule.
        :type offset_seconds: int

        :param period:
            The value to assign to the period property of this VolumeBackupSchedule.
            Allowed values for this property are: "ONE_HOUR", "ONE_DAY", "ONE_WEEK", "ONE_MONTH", "ONE_YEAR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type period: str

        :param retention_seconds:
            The value to assign to the retention_seconds property of this VolumeBackupSchedule.
        :type retention_seconds: int

        """
        self.swagger_types = {
            'backup_type': 'str',
            'offset_seconds': 'int',
            'period': 'str',
            'retention_seconds': 'int'
        }

        self.attribute_map = {
            'backup_type': 'backupType',
            'offset_seconds': 'offsetSeconds',
            'period': 'period',
            'retention_seconds': 'retentionSeconds'
        }

        self._backup_type = None
        self._offset_seconds = None
        self._period = None
        self._retention_seconds = None

    @property
    def backup_type(self):
        """
        **[Required]** Gets the backup_type of this VolumeBackupSchedule.
        The type of backup to create.

        Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The backup_type of this VolumeBackupSchedule.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this VolumeBackupSchedule.
        The type of backup to create.


        :param backup_type: The backup_type of this VolumeBackupSchedule.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(backup_type, allowed_values):
            backup_type = 'UNKNOWN_ENUM_VALUE'
        self._backup_type = backup_type

    @property
    def offset_seconds(self):
        """
        **[Required]** Gets the offset_seconds of this VolumeBackupSchedule.
        The number of seconds (positive or negative) that the backup time should be shifted from the default interval boundaries specified by the period.


        :return: The offset_seconds of this VolumeBackupSchedule.
        :rtype: int
        """
        return self._offset_seconds

    @offset_seconds.setter
    def offset_seconds(self, offset_seconds):
        """
        Sets the offset_seconds of this VolumeBackupSchedule.
        The number of seconds (positive or negative) that the backup time should be shifted from the default interval boundaries specified by the period.


        :param offset_seconds: The offset_seconds of this VolumeBackupSchedule.
        :type: int
        """
        self._offset_seconds = offset_seconds

    @property
    def period(self):
        """
        **[Required]** Gets the period of this VolumeBackupSchedule.
        How often the backup should occur.

        Allowed values for this property are: "ONE_HOUR", "ONE_DAY", "ONE_WEEK", "ONE_MONTH", "ONE_YEAR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The period of this VolumeBackupSchedule.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this VolumeBackupSchedule.
        How often the backup should occur.


        :param period: The period of this VolumeBackupSchedule.
        :type: str
        """
        allowed_values = ["ONE_HOUR", "ONE_DAY", "ONE_WEEK", "ONE_MONTH", "ONE_YEAR"]
        if not value_allowed_none_or_none_sentinel(period, allowed_values):
            period = 'UNKNOWN_ENUM_VALUE'
        self._period = period

    @property
    def retention_seconds(self):
        """
        **[Required]** Gets the retention_seconds of this VolumeBackupSchedule.
        How long, in seconds, backups created by this schedule should be kept until being automatically deleted.


        :return: The retention_seconds of this VolumeBackupSchedule.
        :rtype: int
        """
        return self._retention_seconds

    @retention_seconds.setter
    def retention_seconds(self, retention_seconds):
        """
        Sets the retention_seconds of this VolumeBackupSchedule.
        How long, in seconds, backups created by this schedule should be kept until being automatically deleted.


        :param retention_seconds: The retention_seconds of this VolumeBackupSchedule.
        :type: int
        """
        self._retention_seconds = retention_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
