# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_frequency_details import AbstractFrequencyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonthlyFrequencyDetails(AbstractFrequencyDetails):
    """
    Frequency Details model for monthly frequency.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonthlyFrequencyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.MonthlyFrequencyDetails.model_type` attribute
        of this class is ``MONTHLY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this MonthlyFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "MONTHLY_RULE", "CUSTOM"
        :type model_type: str

        :param frequency:
            The value to assign to the frequency property of this MonthlyFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "CUSTOM"
        :type frequency: str

        :param interval:
            The value to assign to the interval property of this MonthlyFrequencyDetails.
        :type interval: int

        :param time:
            The value to assign to the time property of this MonthlyFrequencyDetails.
        :type time: oci.data_integration.models.Time

        :param days:
            The value to assign to the days property of this MonthlyFrequencyDetails.
        :type days: list[int]

        """
        self.swagger_types = {
            'model_type': 'str',
            'frequency': 'str',
            'interval': 'int',
            'time': 'Time',
            'days': 'list[int]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'frequency': 'frequency',
            'interval': 'interval',
            'time': 'time',
            'days': 'days'
        }

        self._model_type = None
        self._frequency = None
        self._interval = None
        self._time = None
        self._days = None
        self._model_type = 'MONTHLY'

    @property
    def interval(self):
        """
        Gets the interval of this MonthlyFrequencyDetails.
        This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.


        :return: The interval of this MonthlyFrequencyDetails.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this MonthlyFrequencyDetails.
        This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.


        :param interval: The interval of this MonthlyFrequencyDetails.
        :type: int
        """
        self._interval = interval

    @property
    def time(self):
        """
        Gets the time of this MonthlyFrequencyDetails.

        :return: The time of this MonthlyFrequencyDetails.
        :rtype: oci.data_integration.models.Time
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this MonthlyFrequencyDetails.

        :param time: The time of this MonthlyFrequencyDetails.
        :type: oci.data_integration.models.Time
        """
        self._time = time

    @property
    def days(self):
        """
        Gets the days of this MonthlyFrequencyDetails.
        A list of days of the month to be scheduled. i.e. excute every 2nd,3rd, 10th of the month.


        :return: The days of this MonthlyFrequencyDetails.
        :rtype: list[int]
        """
        return self._days

    @days.setter
    def days(self, days):
        """
        Sets the days of this MonthlyFrequencyDetails.
        A list of days of the month to be scheduled. i.e. excute every 2nd,3rd, 10th of the month.


        :param days: The days of this MonthlyFrequencyDetails.
        :type: list[int]
        """
        self._days = days

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
