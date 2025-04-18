# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SnapshotSchedule(object):
    """
    The snapshot schedule is a structure within a parent file system snapshot policy. It contains data about
    the frequency of snapshot creation and the retention time of the taken snapshots.
    """

    #: A constant which can be used with the period property of a SnapshotSchedule.
    #: This constant has a value of "HOURLY"
    PERIOD_HOURLY = "HOURLY"

    #: A constant which can be used with the period property of a SnapshotSchedule.
    #: This constant has a value of "DAILY"
    PERIOD_DAILY = "DAILY"

    #: A constant which can be used with the period property of a SnapshotSchedule.
    #: This constant has a value of "WEEKLY"
    PERIOD_WEEKLY = "WEEKLY"

    #: A constant which can be used with the period property of a SnapshotSchedule.
    #: This constant has a value of "MONTHLY"
    PERIOD_MONTHLY = "MONTHLY"

    #: A constant which can be used with the period property of a SnapshotSchedule.
    #: This constant has a value of "YEARLY"
    PERIOD_YEARLY = "YEARLY"

    #: A constant which can be used with the time_zone property of a SnapshotSchedule.
    #: This constant has a value of "UTC"
    TIME_ZONE_UTC = "UTC"

    #: A constant which can be used with the time_zone property of a SnapshotSchedule.
    #: This constant has a value of "REGIONAL_DATA_CENTER_TIME"
    TIME_ZONE_REGIONAL_DATA_CENTER_TIME = "REGIONAL_DATA_CENTER_TIME"

    #: A constant which can be used with the day_of_week property of a SnapshotSchedule.
    #: This constant has a value of "MONDAY"
    DAY_OF_WEEK_MONDAY = "MONDAY"

    #: A constant which can be used with the day_of_week property of a SnapshotSchedule.
    #: This constant has a value of "TUESDAY"
    DAY_OF_WEEK_TUESDAY = "TUESDAY"

    #: A constant which can be used with the day_of_week property of a SnapshotSchedule.
    #: This constant has a value of "WEDNESDAY"
    DAY_OF_WEEK_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the day_of_week property of a SnapshotSchedule.
    #: This constant has a value of "THURSDAY"
    DAY_OF_WEEK_THURSDAY = "THURSDAY"

    #: A constant which can be used with the day_of_week property of a SnapshotSchedule.
    #: This constant has a value of "FRIDAY"
    DAY_OF_WEEK_FRIDAY = "FRIDAY"

    #: A constant which can be used with the day_of_week property of a SnapshotSchedule.
    #: This constant has a value of "SATURDAY"
    DAY_OF_WEEK_SATURDAY = "SATURDAY"

    #: A constant which can be used with the day_of_week property of a SnapshotSchedule.
    #: This constant has a value of "SUNDAY"
    DAY_OF_WEEK_SUNDAY = "SUNDAY"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "JANUARY"
    MONTH_JANUARY = "JANUARY"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "FEBRUARY"
    MONTH_FEBRUARY = "FEBRUARY"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "MARCH"
    MONTH_MARCH = "MARCH"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "APRIL"
    MONTH_APRIL = "APRIL"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "MAY"
    MONTH_MAY = "MAY"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "JUNE"
    MONTH_JUNE = "JUNE"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "JULY"
    MONTH_JULY = "JULY"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "AUGUST"
    MONTH_AUGUST = "AUGUST"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "SEPTEMBER"
    MONTH_SEPTEMBER = "SEPTEMBER"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "OCTOBER"
    MONTH_OCTOBER = "OCTOBER"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "NOVEMBER"
    MONTH_NOVEMBER = "NOVEMBER"

    #: A constant which can be used with the month property of a SnapshotSchedule.
    #: This constant has a value of "DECEMBER"
    MONTH_DECEMBER = "DECEMBER"

    def __init__(self, **kwargs):
        """
        Initializes a new SnapshotSchedule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schedule_prefix:
            The value to assign to the schedule_prefix property of this SnapshotSchedule.
        :type schedule_prefix: str

        :param time_schedule_start:
            The value to assign to the time_schedule_start property of this SnapshotSchedule.
        :type time_schedule_start: datetime

        :param period:
            The value to assign to the period property of this SnapshotSchedule.
            Allowed values for this property are: "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type period: str

        :param retention_duration_in_seconds:
            The value to assign to the retention_duration_in_seconds property of this SnapshotSchedule.
        :type retention_duration_in_seconds: int

        :param time_zone:
            The value to assign to the time_zone property of this SnapshotSchedule.
            Allowed values for this property are: "UTC", "REGIONAL_DATA_CENTER_TIME", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type time_zone: str

        :param hour_of_day:
            The value to assign to the hour_of_day property of this SnapshotSchedule.
        :type hour_of_day: int

        :param day_of_week:
            The value to assign to the day_of_week property of this SnapshotSchedule.
            Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type day_of_week: str

        :param day_of_month:
            The value to assign to the day_of_month property of this SnapshotSchedule.
        :type day_of_month: int

        :param month:
            The value to assign to the month property of this SnapshotSchedule.
            Allowed values for this property are: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type month: str

        """
        self.swagger_types = {
            'schedule_prefix': 'str',
            'time_schedule_start': 'datetime',
            'period': 'str',
            'retention_duration_in_seconds': 'int',
            'time_zone': 'str',
            'hour_of_day': 'int',
            'day_of_week': 'str',
            'day_of_month': 'int',
            'month': 'str'
        }
        self.attribute_map = {
            'schedule_prefix': 'schedulePrefix',
            'time_schedule_start': 'timeScheduleStart',
            'period': 'period',
            'retention_duration_in_seconds': 'retentionDurationInSeconds',
            'time_zone': 'timeZone',
            'hour_of_day': 'hourOfDay',
            'day_of_week': 'dayOfWeek',
            'day_of_month': 'dayOfMonth',
            'month': 'month'
        }
        self._schedule_prefix = None
        self._time_schedule_start = None
        self._period = None
        self._retention_duration_in_seconds = None
        self._time_zone = None
        self._hour_of_day = None
        self._day_of_week = None
        self._day_of_month = None
        self._month = None

    @property
    def schedule_prefix(self):
        """
        Gets the schedule_prefix of this SnapshotSchedule.
        A name prefix to be applied to snapshots created by this schedule.

        Example: `compliance1`


        :return: The schedule_prefix of this SnapshotSchedule.
        :rtype: str
        """
        return self._schedule_prefix

    @schedule_prefix.setter
    def schedule_prefix(self, schedule_prefix):
        """
        Sets the schedule_prefix of this SnapshotSchedule.
        A name prefix to be applied to snapshots created by this schedule.

        Example: `compliance1`


        :param schedule_prefix: The schedule_prefix of this SnapshotSchedule.
        :type: str
        """
        self._schedule_prefix = schedule_prefix

    @property
    def time_schedule_start(self):
        """
        Gets the time_schedule_start of this SnapshotSchedule.
        The starting point used to begin the scheduling of the snapshots based upon recurrence string
        in `RFC 3339`__ timestamp format.
        If no `timeScheduleStart` is provided, the value will be set to the time when the schedule was created.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_schedule_start of this SnapshotSchedule.
        :rtype: datetime
        """
        return self._time_schedule_start

    @time_schedule_start.setter
    def time_schedule_start(self, time_schedule_start):
        """
        Sets the time_schedule_start of this SnapshotSchedule.
        The starting point used to begin the scheduling of the snapshots based upon recurrence string
        in `RFC 3339`__ timestamp format.
        If no `timeScheduleStart` is provided, the value will be set to the time when the schedule was created.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_schedule_start: The time_schedule_start of this SnapshotSchedule.
        :type: datetime
        """
        self._time_schedule_start = time_schedule_start

    @property
    def period(self):
        """
        **[Required]** Gets the period of this SnapshotSchedule.
        The frequency of scheduled snapshots.

        Allowed values for this property are: "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The period of this SnapshotSchedule.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this SnapshotSchedule.
        The frequency of scheduled snapshots.


        :param period: The period of this SnapshotSchedule.
        :type: str
        """
        allowed_values = ["HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"]
        if not value_allowed_none_or_none_sentinel(period, allowed_values):
            period = 'UNKNOWN_ENUM_VALUE'
        self._period = period

    @property
    def retention_duration_in_seconds(self):
        """
        Gets the retention_duration_in_seconds of this SnapshotSchedule.
        The number of seconds to retain snapshots created with this schedule.
        Snapshot expiration time will not be set if this value is empty.


        :return: The retention_duration_in_seconds of this SnapshotSchedule.
        :rtype: int
        """
        return self._retention_duration_in_seconds

    @retention_duration_in_seconds.setter
    def retention_duration_in_seconds(self, retention_duration_in_seconds):
        """
        Sets the retention_duration_in_seconds of this SnapshotSchedule.
        The number of seconds to retain snapshots created with this schedule.
        Snapshot expiration time will not be set if this value is empty.


        :param retention_duration_in_seconds: The retention_duration_in_seconds of this SnapshotSchedule.
        :type: int
        """
        self._retention_duration_in_seconds = retention_duration_in_seconds

    @property
    def time_zone(self):
        """
        **[Required]** Gets the time_zone of this SnapshotSchedule.
        Time zone used for scheduling the snapshot.

        Allowed values for this property are: "UTC", "REGIONAL_DATA_CENTER_TIME", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The time_zone of this SnapshotSchedule.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this SnapshotSchedule.
        Time zone used for scheduling the snapshot.


        :param time_zone: The time_zone of this SnapshotSchedule.
        :type: str
        """
        allowed_values = ["UTC", "REGIONAL_DATA_CENTER_TIME"]
        if not value_allowed_none_or_none_sentinel(time_zone, allowed_values):
            time_zone = 'UNKNOWN_ENUM_VALUE'
        self._time_zone = time_zone

    @property
    def hour_of_day(self):
        """
        Gets the hour_of_day of this SnapshotSchedule.
        The hour of the day to create a DAILY, WEEKLY, MONTHLY, or YEARLY snapshot.
        If not set, the system chooses a value at creation time.


        :return: The hour_of_day of this SnapshotSchedule.
        :rtype: int
        """
        return self._hour_of_day

    @hour_of_day.setter
    def hour_of_day(self, hour_of_day):
        """
        Sets the hour_of_day of this SnapshotSchedule.
        The hour of the day to create a DAILY, WEEKLY, MONTHLY, or YEARLY snapshot.
        If not set, the system chooses a value at creation time.


        :param hour_of_day: The hour_of_day of this SnapshotSchedule.
        :type: int
        """
        self._hour_of_day = hour_of_day

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this SnapshotSchedule.
        The day of the week to create a scheduled snapshot.
        Used for WEEKLY snapshot schedules.
        If not set, the system chooses a value at creation time.

        Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The day_of_week of this SnapshotSchedule.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this SnapshotSchedule.
        The day of the week to create a scheduled snapshot.
        Used for WEEKLY snapshot schedules.
        If not set, the system chooses a value at creation time.


        :param day_of_week: The day_of_week of this SnapshotSchedule.
        :type: str
        """
        allowed_values = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        if not value_allowed_none_or_none_sentinel(day_of_week, allowed_values):
            day_of_week = 'UNKNOWN_ENUM_VALUE'
        self._day_of_week = day_of_week

    @property
    def day_of_month(self):
        """
        Gets the day_of_month of this SnapshotSchedule.
        The day of the month to create a scheduled snapshot.
        If the day does not exist for the month, snapshot creation will be skipped.
        Used for MONTHLY and YEARLY snapshot schedules.
        If not set, the system chooses a value at creation time.


        :return: The day_of_month of this SnapshotSchedule.
        :rtype: int
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """
        Sets the day_of_month of this SnapshotSchedule.
        The day of the month to create a scheduled snapshot.
        If the day does not exist for the month, snapshot creation will be skipped.
        Used for MONTHLY and YEARLY snapshot schedules.
        If not set, the system chooses a value at creation time.


        :param day_of_month: The day_of_month of this SnapshotSchedule.
        :type: int
        """
        self._day_of_month = day_of_month

    @property
    def month(self):
        """
        Gets the month of this SnapshotSchedule.
        The month to create a scheduled snapshot.
        Used only for YEARLY snapshot schedules.
        If not set, the system chooses a value at creation time.

        Allowed values for this property are: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The month of this SnapshotSchedule.
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """
        Sets the month of this SnapshotSchedule.
        The month to create a scheduled snapshot.
        Used only for YEARLY snapshot schedules.
        If not set, the system chooses a value at creation time.


        :param month: The month of this SnapshotSchedule.
        :type: str
        """
        allowed_values = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
        if not value_allowed_none_or_none_sentinel(month, allowed_values):
            month = 'UNKNOWN_ENUM_VALUE'
        self._month = month

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
