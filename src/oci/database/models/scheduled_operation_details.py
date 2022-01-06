# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledOperationDetails(object):
    """
    Details of scheduled operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledOperationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param day_of_week:
            The value to assign to the day_of_week property of this ScheduledOperationDetails.
        :type day_of_week: oci.database.models.DayOfWeek

        :param scheduled_start_time:
            The value to assign to the scheduled_start_time property of this ScheduledOperationDetails.
        :type scheduled_start_time: str

        :param scheduled_stop_time:
            The value to assign to the scheduled_stop_time property of this ScheduledOperationDetails.
        :type scheduled_stop_time: str

        """
        self.swagger_types = {
            'day_of_week': 'DayOfWeek',
            'scheduled_start_time': 'str',
            'scheduled_stop_time': 'str'
        }

        self.attribute_map = {
            'day_of_week': 'dayOfWeek',
            'scheduled_start_time': 'scheduledStartTime',
            'scheduled_stop_time': 'scheduledStopTime'
        }

        self._day_of_week = None
        self._scheduled_start_time = None
        self._scheduled_stop_time = None

    @property
    def day_of_week(self):
        """
        **[Required]** Gets the day_of_week of this ScheduledOperationDetails.

        :return: The day_of_week of this ScheduledOperationDetails.
        :rtype: oci.database.models.DayOfWeek
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this ScheduledOperationDetails.

        :param day_of_week: The day_of_week of this ScheduledOperationDetails.
        :type: oci.database.models.DayOfWeek
        """
        self._day_of_week = day_of_week

    @property
    def scheduled_start_time(self):
        """
        Gets the scheduled_start_time of this ScheduledOperationDetails.
        auto start time. value must be of ISO-8601 format \"HH:mm\"


        :return: The scheduled_start_time of this ScheduledOperationDetails.
        :rtype: str
        """
        return self._scheduled_start_time

    @scheduled_start_time.setter
    def scheduled_start_time(self, scheduled_start_time):
        """
        Sets the scheduled_start_time of this ScheduledOperationDetails.
        auto start time. value must be of ISO-8601 format \"HH:mm\"


        :param scheduled_start_time: The scheduled_start_time of this ScheduledOperationDetails.
        :type: str
        """
        self._scheduled_start_time = scheduled_start_time

    @property
    def scheduled_stop_time(self):
        """
        Gets the scheduled_stop_time of this ScheduledOperationDetails.
        auto stop time. value must be of ISO-8601 format \"HH:mm\"


        :return: The scheduled_stop_time of this ScheduledOperationDetails.
        :rtype: str
        """
        return self._scheduled_stop_time

    @scheduled_stop_time.setter
    def scheduled_stop_time(self, scheduled_stop_time):
        """
        Sets the scheduled_stop_time of this ScheduledOperationDetails.
        auto stop time. value must be of ISO-8601 format \"HH:mm\"


        :param scheduled_stop_time: The scheduled_stop_time of this ScheduledOperationDetails.
        :type: str
        """
        self._scheduled_stop_time = scheduled_stop_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
