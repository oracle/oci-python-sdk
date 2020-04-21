# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaintenanceWindow(object):
    """
    The scheduling details for the quarterly maintenance window. Patching and system updates take place during the maintenance window.
    """

    #: A constant which can be used with the preference property of a MaintenanceWindow.
    #: This constant has a value of "NO_PREFERENCE"
    PREFERENCE_NO_PREFERENCE = "NO_PREFERENCE"

    #: A constant which can be used with the preference property of a MaintenanceWindow.
    #: This constant has a value of "CUSTOM_PREFERENCE"
    PREFERENCE_CUSTOM_PREFERENCE = "CUSTOM_PREFERENCE"

    def __init__(self, **kwargs):
        """
        Initializes a new MaintenanceWindow object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param preference:
            The value to assign to the preference property of this MaintenanceWindow.
            Allowed values for this property are: "NO_PREFERENCE", "CUSTOM_PREFERENCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type preference: str

        :param months:
            The value to assign to the months property of this MaintenanceWindow.
        :type months: list[Month]

        :param weeks_of_month:
            The value to assign to the weeks_of_month property of this MaintenanceWindow.
        :type weeks_of_month: list[int]

        :param days_of_week:
            The value to assign to the days_of_week property of this MaintenanceWindow.
        :type days_of_week: list[DayOfWeek]

        :param hours_of_day:
            The value to assign to the hours_of_day property of this MaintenanceWindow.
        :type hours_of_day: list[int]

        :param lead_time_in_weeks:
            The value to assign to the lead_time_in_weeks property of this MaintenanceWindow.
        :type lead_time_in_weeks: int

        """
        self.swagger_types = {
            'preference': 'str',
            'months': 'list[Month]',
            'weeks_of_month': 'list[int]',
            'days_of_week': 'list[DayOfWeek]',
            'hours_of_day': 'list[int]',
            'lead_time_in_weeks': 'int'
        }

        self.attribute_map = {
            'preference': 'preference',
            'months': 'months',
            'weeks_of_month': 'weeksOfMonth',
            'days_of_week': 'daysOfWeek',
            'hours_of_day': 'hoursOfDay',
            'lead_time_in_weeks': 'leadTimeInWeeks'
        }

        self._preference = None
        self._months = None
        self._weeks_of_month = None
        self._days_of_week = None
        self._hours_of_day = None
        self._lead_time_in_weeks = None

    @property
    def preference(self):
        """
        **[Required]** Gets the preference of this MaintenanceWindow.
        The maintenance window scheduling preference.

        Allowed values for this property are: "NO_PREFERENCE", "CUSTOM_PREFERENCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The preference of this MaintenanceWindow.
        :rtype: str
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        """
        Sets the preference of this MaintenanceWindow.
        The maintenance window scheduling preference.


        :param preference: The preference of this MaintenanceWindow.
        :type: str
        """
        allowed_values = ["NO_PREFERENCE", "CUSTOM_PREFERENCE"]
        if not value_allowed_none_or_none_sentinel(preference, allowed_values):
            preference = 'UNKNOWN_ENUM_VALUE'
        self._preference = preference

    @property
    def months(self):
        """
        Gets the months of this MaintenanceWindow.
        Months during the year when maintenance should be performed.


        :return: The months of this MaintenanceWindow.
        :rtype: list[Month]
        """
        return self._months

    @months.setter
    def months(self, months):
        """
        Sets the months of this MaintenanceWindow.
        Months during the year when maintenance should be performed.


        :param months: The months of this MaintenanceWindow.
        :type: list[Month]
        """
        self._months = months

    @property
    def weeks_of_month(self):
        """
        Gets the weeks_of_month of this MaintenanceWindow.
        Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
        For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2. Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
        Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of the week and hours that maintenance will be performed.


        :return: The weeks_of_month of this MaintenanceWindow.
        :rtype: list[int]
        """
        return self._weeks_of_month

    @weeks_of_month.setter
    def weeks_of_month(self, weeks_of_month):
        """
        Sets the weeks_of_month of this MaintenanceWindow.
        Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
        For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2. Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
        Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of the week and hours that maintenance will be performed.


        :param weeks_of_month: The weeks_of_month of this MaintenanceWindow.
        :type: list[int]
        """
        self._weeks_of_month = weeks_of_month

    @property
    def days_of_week(self):
        """
        Gets the days_of_week of this MaintenanceWindow.
        Days during the week when maintenance should be performed.


        :return: The days_of_week of this MaintenanceWindow.
        :rtype: list[DayOfWeek]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        """
        Sets the days_of_week of this MaintenanceWindow.
        Days during the week when maintenance should be performed.


        :param days_of_week: The days_of_week of this MaintenanceWindow.
        :type: list[DayOfWeek]
        """
        self._days_of_week = days_of_week

    @property
    def hours_of_day(self):
        """
        Gets the hours_of_day of this MaintenanceWindow.
        The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
        - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12 - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59 UTC


        :return: The hours_of_day of this MaintenanceWindow.
        :rtype: list[int]
        """
        return self._hours_of_day

    @hours_of_day.setter
    def hours_of_day(self, hours_of_day):
        """
        Sets the hours_of_day of this MaintenanceWindow.
        The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
        - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12 - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59 UTC


        :param hours_of_day: The hours_of_day of this MaintenanceWindow.
        :type: list[int]
        """
        self._hours_of_day = hours_of_day

    @property
    def lead_time_in_weeks(self):
        """
        Gets the lead_time_in_weeks of this MaintenanceWindow.
        Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.


        :return: The lead_time_in_weeks of this MaintenanceWindow.
        :rtype: int
        """
        return self._lead_time_in_weeks

    @lead_time_in_weeks.setter
    def lead_time_in_weeks(self, lead_time_in_weeks):
        """
        Sets the lead_time_in_weeks of this MaintenanceWindow.
        Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.


        :param lead_time_in_weeks: The lead_time_in_weeks of this MaintenanceWindow.
        :type: int
        """
        self._lead_time_in_weeks = lead_time_in_weeks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
