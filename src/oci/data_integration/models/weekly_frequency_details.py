# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_frequency_details import AbstractFrequencyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WeeklyFrequencyDetails(AbstractFrequencyDetails):
    """
    Frequency Details model for weekly frequency based on day of week.
    """

    #: A constant which can be used with the days property of a WeeklyFrequencyDetails.
    #: This constant has a value of "SUNDAY"
    DAYS_SUNDAY = "SUNDAY"

    #: A constant which can be used with the days property of a WeeklyFrequencyDetails.
    #: This constant has a value of "MONDAY"
    DAYS_MONDAY = "MONDAY"

    #: A constant which can be used with the days property of a WeeklyFrequencyDetails.
    #: This constant has a value of "TUESDAY"
    DAYS_TUESDAY = "TUESDAY"

    #: A constant which can be used with the days property of a WeeklyFrequencyDetails.
    #: This constant has a value of "WEDNESDAY"
    DAYS_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the days property of a WeeklyFrequencyDetails.
    #: This constant has a value of "THURSDAY"
    DAYS_THURSDAY = "THURSDAY"

    #: A constant which can be used with the days property of a WeeklyFrequencyDetails.
    #: This constant has a value of "FRIDAY"
    DAYS_FRIDAY = "FRIDAY"

    #: A constant which can be used with the days property of a WeeklyFrequencyDetails.
    #: This constant has a value of "SATURDAY"
    DAYS_SATURDAY = "SATURDAY"

    def __init__(self, **kwargs):
        """
        Initializes a new WeeklyFrequencyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.WeeklyFrequencyDetails.model_type` attribute
        of this class is ``WEEKLY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this WeeklyFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "MONTHLY_RULE", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param frequency:
            The value to assign to the frequency property of this WeeklyFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type frequency: str

        :param time:
            The value to assign to the time property of this WeeklyFrequencyDetails.
        :type time: oci.data_integration.models.Time

        :param days:
            The value to assign to the days property of this WeeklyFrequencyDetails.
            Allowed values for items in this list are: "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type days: list[str]

        """
        self.swagger_types = {
            'model_type': 'str',
            'frequency': 'str',
            'time': 'Time',
            'days': 'list[str]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'frequency': 'frequency',
            'time': 'time',
            'days': 'days'
        }

        self._model_type = None
        self._frequency = None
        self._time = None
        self._days = None
        self._model_type = 'WEEKLY'

    @property
    def time(self):
        """
        Gets the time of this WeeklyFrequencyDetails.

        :return: The time of this WeeklyFrequencyDetails.
        :rtype: oci.data_integration.models.Time
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this WeeklyFrequencyDetails.

        :param time: The time of this WeeklyFrequencyDetails.
        :type: oci.data_integration.models.Time
        """
        self._time = time

    @property
    def days(self):
        """
        Gets the days of this WeeklyFrequencyDetails.
        A list of days of the week to be scheduled. i.e. execute on Monday and Thursday.

        Allowed values for items in this list are: "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The days of this WeeklyFrequencyDetails.
        :rtype: list[str]
        """
        return self._days

    @days.setter
    def days(self, days):
        """
        Sets the days of this WeeklyFrequencyDetails.
        A list of days of the week to be scheduled. i.e. execute on Monday and Thursday.


        :param days: The days of this WeeklyFrequencyDetails.
        :type: list[str]
        """
        allowed_values = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        if days:
            days[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in days]
        self._days = days

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
