# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaintenanceWindow(object):
    """
    The preferred day and time to perform maintenance.
    """

    #: A constant which can be used with the day_of_week property of a MaintenanceWindow.
    #: This constant has a value of "MONDAY"
    DAY_OF_WEEK_MONDAY = "MONDAY"

    #: A constant which can be used with the day_of_week property of a MaintenanceWindow.
    #: This constant has a value of "TUESDAY"
    DAY_OF_WEEK_TUESDAY = "TUESDAY"

    #: A constant which can be used with the day_of_week property of a MaintenanceWindow.
    #: This constant has a value of "WEDNESDAY"
    DAY_OF_WEEK_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the day_of_week property of a MaintenanceWindow.
    #: This constant has a value of "THURSDAY"
    DAY_OF_WEEK_THURSDAY = "THURSDAY"

    #: A constant which can be used with the day_of_week property of a MaintenanceWindow.
    #: This constant has a value of "FRIDAY"
    DAY_OF_WEEK_FRIDAY = "FRIDAY"

    #: A constant which can be used with the day_of_week property of a MaintenanceWindow.
    #: This constant has a value of "SATURDAY"
    DAY_OF_WEEK_SATURDAY = "SATURDAY"

    #: A constant which can be used with the day_of_week property of a MaintenanceWindow.
    #: This constant has a value of "SUNDAY"
    DAY_OF_WEEK_SUNDAY = "SUNDAY"

    def __init__(self, **kwargs):
        """
        Initializes a new MaintenanceWindow object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param day_of_week:
            The value to assign to the day_of_week property of this MaintenanceWindow.
            Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type day_of_week: str

        :param time_start:
            The value to assign to the time_start property of this MaintenanceWindow.
        :type time_start: str

        """
        self.swagger_types = {
            'day_of_week': 'str',
            'time_start': 'str'
        }
        self.attribute_map = {
            'day_of_week': 'dayOfWeek',
            'time_start': 'timeStart'
        }
        self._day_of_week = None
        self._time_start = None

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this MaintenanceWindow.
        Day of the week when the maintainence window starts.

        Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The day_of_week of this MaintenanceWindow.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this MaintenanceWindow.
        Day of the week when the maintainence window starts.


        :param day_of_week: The day_of_week of this MaintenanceWindow.
        :type: str
        """
        allowed_values = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        if not value_allowed_none_or_none_sentinel(day_of_week, allowed_values):
            day_of_week = 'UNKNOWN_ENUM_VALUE'
        self._day_of_week = day_of_week

    @property
    def time_start(self):
        """
        Gets the time_start of this MaintenanceWindow.
        The time to start the maintenance window. The format is 'HH:MM', 'HH:MM' represents the time in UTC.

        Example: `22:00`


        :return: The time_start of this MaintenanceWindow.
        :rtype: str
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this MaintenanceWindow.
        The time to start the maintenance window. The format is 'HH:MM', 'HH:MM' represents the time in UTC.

        Example: `22:00`


        :param time_start: The time_start of this MaintenanceWindow.
        :type: str
        """
        self._time_start = time_start

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
