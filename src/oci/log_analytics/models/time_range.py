# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TimeRange(object):
    """
    Specify time range. This paramter can be overwritten if time criteria is specified in the query string. If no time criteria are found in query string this time range is used.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TimeRange object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_start:
            The value to assign to the time_start property of this TimeRange.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this TimeRange.
        :type time_end: datetime

        :param time_zone:
            The value to assign to the time_zone property of this TimeRange.
        :type time_zone: str

        """
        self.swagger_types = {
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_zone': 'str'
        }

        self.attribute_map = {
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_zone': 'timeZone'
        }

        self._time_start = None
        self._time_end = None
        self._time_zone = None

    @property
    def time_start(self):
        """
        **[Required]** Gets the time_start of this TimeRange.
        Time for query to start matching results from. Start time must be less than end time otherwise it will result in error.


        :return: The time_start of this TimeRange.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this TimeRange.
        Time for query to start matching results from. Start time must be less than end time otherwise it will result in error.


        :param time_start: The time_start of this TimeRange.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        **[Required]** Gets the time_end of this TimeRange.
        Time for query to stop matching results to. End Time must be greater than or equal to start time otherwise it will result in error.


        :return: The time_end of this TimeRange.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this TimeRange.
        Time for query to stop matching results to. End Time must be greater than or equal to start time otherwise it will result in error.


        :param time_end: The time_end of this TimeRange.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_zone(self):
        """
        Gets the time_zone of this TimeRange.
        Time zone for query.


        :return: The time_zone of this TimeRange.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this TimeRange.
        Time zone for query.


        :param time_zone: The time_zone of this TimeRange.
        :type: str
        """
        self._time_zone = time_zone

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
