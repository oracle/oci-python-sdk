# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .schedule_trigger import ScheduleTrigger
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleIntervalTrigger(ScheduleTrigger):
    """
    The interval schedule trigger.
    """

    #: A constant which can be used with the frequency property of a ScheduleIntervalTrigger.
    #: This constant has a value of "HOURLY"
    FREQUENCY_HOURLY = "HOURLY"

    #: A constant which can be used with the frequency property of a ScheduleIntervalTrigger.
    #: This constant has a value of "DAILY"
    FREQUENCY_DAILY = "DAILY"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleIntervalTrigger object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.ScheduleIntervalTrigger.trigger_type` attribute
        of this class is ``INTERVAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param trigger_type:
            The value to assign to the trigger_type property of this ScheduleIntervalTrigger.
            Allowed values for this property are: "CRON", "INTERVAL", "ICAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type trigger_type: str

        :param time_start:
            The value to assign to the time_start property of this ScheduleIntervalTrigger.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this ScheduleIntervalTrigger.
        :type time_end: datetime

        :param frequency:
            The value to assign to the frequency property of this ScheduleIntervalTrigger.
            Allowed values for this property are: "HOURLY", "DAILY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type frequency: str

        :param interval:
            The value to assign to the interval property of this ScheduleIntervalTrigger.
        :type interval: int

        :param is_random_start_time:
            The value to assign to the is_random_start_time property of this ScheduleIntervalTrigger.
        :type is_random_start_time: bool

        """
        self.swagger_types = {
            'trigger_type': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'frequency': 'str',
            'interval': 'int',
            'is_random_start_time': 'bool'
        }
        self.attribute_map = {
            'trigger_type': 'triggerType',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'frequency': 'frequency',
            'interval': 'interval',
            'is_random_start_time': 'isRandomStartTime'
        }
        self._trigger_type = None
        self._time_start = None
        self._time_end = None
        self._frequency = None
        self._interval = None
        self._is_random_start_time = None
        self._trigger_type = 'INTERVAL'

    @property
    def frequency(self):
        """
        **[Required]** Gets the frequency of this ScheduleIntervalTrigger.
        The type of frequency

        Allowed values for this property are: "HOURLY", "DAILY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The frequency of this ScheduleIntervalTrigger.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """
        Sets the frequency of this ScheduleIntervalTrigger.
        The type of frequency


        :param frequency: The frequency of this ScheduleIntervalTrigger.
        :type: str
        """
        allowed_values = ["HOURLY", "DAILY"]
        if not value_allowed_none_or_none_sentinel(frequency, allowed_values):
            frequency = 'UNKNOWN_ENUM_VALUE'
        self._frequency = frequency

    @property
    def interval(self):
        """
        **[Required]** Gets the interval of this ScheduleIntervalTrigger.
        The interval of frequency.


        :return: The interval of this ScheduleIntervalTrigger.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this ScheduleIntervalTrigger.
        The interval of frequency.


        :param interval: The interval of this ScheduleIntervalTrigger.
        :type: int
        """
        self._interval = interval

    @property
    def is_random_start_time(self):
        """
        Gets the is_random_start_time of this ScheduleIntervalTrigger.
        when true and timeStart is null, system generate a random start time between now and now + interval;
        isRandomStartTime can be true if timeStart is null.


        :return: The is_random_start_time of this ScheduleIntervalTrigger.
        :rtype: bool
        """
        return self._is_random_start_time

    @is_random_start_time.setter
    def is_random_start_time(self, is_random_start_time):
        """
        Sets the is_random_start_time of this ScheduleIntervalTrigger.
        when true and timeStart is null, system generate a random start time between now and now + interval;
        isRandomStartTime can be true if timeStart is null.


        :param is_random_start_time: The is_random_start_time of this ScheduleIntervalTrigger.
        :type: bool
        """
        self._is_random_start_time = is_random_start_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
