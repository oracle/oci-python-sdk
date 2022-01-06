# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .schedule import Schedule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FixedFrequencySchedule(Schedule):
    """
    Fixed frequency schedule for a scheduled task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FixedFrequencySchedule object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.FixedFrequencySchedule.type` attribute
        of this class is ``FIXED_FREQUENCY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FixedFrequencySchedule.
            Allowed values for this property are: "FIXED_FREQUENCY", "CRON"
        :type type: str

        :param misfire_policy:
            The value to assign to the misfire_policy property of this FixedFrequencySchedule.
            Allowed values for this property are: "RETRY_ONCE", "RETRY_INDEFINITELY", "SKIP"
        :type misfire_policy: str

        :param time_of_first_execution:
            The value to assign to the time_of_first_execution property of this FixedFrequencySchedule.
        :type time_of_first_execution: datetime

        :param recurring_interval:
            The value to assign to the recurring_interval property of this FixedFrequencySchedule.
        :type recurring_interval: str

        :param repeat_count:
            The value to assign to the repeat_count property of this FixedFrequencySchedule.
        :type repeat_count: int

        """
        self.swagger_types = {
            'type': 'str',
            'misfire_policy': 'str',
            'time_of_first_execution': 'datetime',
            'recurring_interval': 'str',
            'repeat_count': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'misfire_policy': 'misfirePolicy',
            'time_of_first_execution': 'timeOfFirstExecution',
            'recurring_interval': 'recurringInterval',
            'repeat_count': 'repeatCount'
        }

        self._type = None
        self._misfire_policy = None
        self._time_of_first_execution = None
        self._recurring_interval = None
        self._repeat_count = None
        self._type = 'FIXED_FREQUENCY'

    @property
    def recurring_interval(self):
        """
        **[Required]** Gets the recurring_interval of this FixedFrequencySchedule.
        Recurring interval in ISO 8601 extended format as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations.
        The largest supported unit is D, e.g. P14D (not P2W).
        The value must be at least 5 minutes (PT5M) and at most 3 weeks (P21D or PT30240M).


        :return: The recurring_interval of this FixedFrequencySchedule.
        :rtype: str
        """
        return self._recurring_interval

    @recurring_interval.setter
    def recurring_interval(self, recurring_interval):
        """
        Sets the recurring_interval of this FixedFrequencySchedule.
        Recurring interval in ISO 8601 extended format as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations.
        The largest supported unit is D, e.g. P14D (not P2W).
        The value must be at least 5 minutes (PT5M) and at most 3 weeks (P21D or PT30240M).


        :param recurring_interval: The recurring_interval of this FixedFrequencySchedule.
        :type: str
        """
        self._recurring_interval = recurring_interval

    @property
    def repeat_count(self):
        """
        Gets the repeat_count of this FixedFrequencySchedule.
        Number of times (0-based) to execute until auto-stop.
        Default value -1 will execute indefinitely.
        Value 0 will execute once.


        :return: The repeat_count of this FixedFrequencySchedule.
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """
        Sets the repeat_count of this FixedFrequencySchedule.
        Number of times (0-based) to execute until auto-stop.
        Default value -1 will execute indefinitely.
        Value 0 will execute once.


        :param repeat_count: The repeat_count of this FixedFrequencySchedule.
        :type: int
        """
        self._repeat_count = repeat_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
