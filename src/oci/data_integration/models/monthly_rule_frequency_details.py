# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .abstract_frequency_details import AbstractFrequencyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonthlyRuleFrequencyDetails(AbstractFrequencyDetails):
    """
    Frequency Details model for monthly frequency based on week of month and day of week.
    """

    #: A constant which can be used with the week_of_month property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "FIRST"
    WEEK_OF_MONTH_FIRST = "FIRST"

    #: A constant which can be used with the week_of_month property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "SECOND"
    WEEK_OF_MONTH_SECOND = "SECOND"

    #: A constant which can be used with the week_of_month property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "THIRD"
    WEEK_OF_MONTH_THIRD = "THIRD"

    #: A constant which can be used with the week_of_month property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "FOURTH"
    WEEK_OF_MONTH_FOURTH = "FOURTH"

    #: A constant which can be used with the week_of_month property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "FIFTH"
    WEEK_OF_MONTH_FIFTH = "FIFTH"

    #: A constant which can be used with the week_of_month property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "LAST"
    WEEK_OF_MONTH_LAST = "LAST"

    #: A constant which can be used with the day_of_week property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "SUNDAY"
    DAY_OF_WEEK_SUNDAY = "SUNDAY"

    #: A constant which can be used with the day_of_week property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "MONDAY"
    DAY_OF_WEEK_MONDAY = "MONDAY"

    #: A constant which can be used with the day_of_week property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "TUESDAY"
    DAY_OF_WEEK_TUESDAY = "TUESDAY"

    #: A constant which can be used with the day_of_week property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "WEDNESDAY"
    DAY_OF_WEEK_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the day_of_week property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "THURSDAY"
    DAY_OF_WEEK_THURSDAY = "THURSDAY"

    #: A constant which can be used with the day_of_week property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "FRIDAY"
    DAY_OF_WEEK_FRIDAY = "FRIDAY"

    #: A constant which can be used with the day_of_week property of a MonthlyRuleFrequencyDetails.
    #: This constant has a value of "SATURDAY"
    DAY_OF_WEEK_SATURDAY = "SATURDAY"

    def __init__(self, **kwargs):
        """
        Initializes a new MonthlyRuleFrequencyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.MonthlyRuleFrequencyDetails.model_type` attribute
        of this class is ``MONTHLY_RULE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this MonthlyRuleFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "MONTHLY_RULE", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param frequency:
            The value to assign to the frequency property of this MonthlyRuleFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type frequency: str

        :param week_of_month:
            The value to assign to the week_of_month property of this MonthlyRuleFrequencyDetails.
            Allowed values for this property are: "FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "LAST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type week_of_month: str

        :param interval:
            The value to assign to the interval property of this MonthlyRuleFrequencyDetails.
        :type interval: int

        :param time:
            The value to assign to the time property of this MonthlyRuleFrequencyDetails.
        :type time: oci.data_integration.models.Time

        :param day_of_week:
            The value to assign to the day_of_week property of this MonthlyRuleFrequencyDetails.
            Allowed values for this property are: "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type day_of_week: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'frequency': 'str',
            'week_of_month': 'str',
            'interval': 'int',
            'time': 'Time',
            'day_of_week': 'str'
        }
        self.attribute_map = {
            'model_type': 'modelType',
            'frequency': 'frequency',
            'week_of_month': 'weekOfMonth',
            'interval': 'interval',
            'time': 'time',
            'day_of_week': 'dayOfWeek'
        }
        self._model_type = None
        self._frequency = None
        self._week_of_month = None
        self._interval = None
        self._time = None
        self._day_of_week = None
        self._model_type = 'MONTHLY_RULE'

    @property
    def week_of_month(self):
        """
        Gets the week_of_month of this MonthlyRuleFrequencyDetails.
        This holds the week of the month in which the schedule should be triggered.

        Allowed values for this property are: "FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "LAST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The week_of_month of this MonthlyRuleFrequencyDetails.
        :rtype: str
        """
        return self._week_of_month

    @week_of_month.setter
    def week_of_month(self, week_of_month):
        """
        Sets the week_of_month of this MonthlyRuleFrequencyDetails.
        This holds the week of the month in which the schedule should be triggered.


        :param week_of_month: The week_of_month of this MonthlyRuleFrequencyDetails.
        :type: str
        """
        allowed_values = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "LAST"]
        if not value_allowed_none_or_none_sentinel(week_of_month, allowed_values):
            week_of_month = 'UNKNOWN_ENUM_VALUE'
        self._week_of_month = week_of_month

    @property
    def interval(self):
        """
        Gets the interval of this MonthlyRuleFrequencyDetails.
        This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.


        :return: The interval of this MonthlyRuleFrequencyDetails.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this MonthlyRuleFrequencyDetails.
        This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.


        :param interval: The interval of this MonthlyRuleFrequencyDetails.
        :type: int
        """
        self._interval = interval

    @property
    def time(self):
        """
        Gets the time of this MonthlyRuleFrequencyDetails.

        :return: The time of this MonthlyRuleFrequencyDetails.
        :rtype: oci.data_integration.models.Time
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this MonthlyRuleFrequencyDetails.

        :param time: The time of this MonthlyRuleFrequencyDetails.
        :type: oci.data_integration.models.Time
        """
        self._time = time

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this MonthlyRuleFrequencyDetails.
        This holds the day of the week on which the schedule should be triggered.

        Allowed values for this property are: "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The day_of_week of this MonthlyRuleFrequencyDetails.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this MonthlyRuleFrequencyDetails.
        This holds the day of the week on which the schedule should be triggered.


        :param day_of_week: The day_of_week of this MonthlyRuleFrequencyDetails.
        :type: str
        """
        allowed_values = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        if not value_allowed_none_or_none_sentinel(day_of_week, allowed_values):
            day_of_week = 'UNKNOWN_ENUM_VALUE'
        self._day_of_week = day_of_week

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
