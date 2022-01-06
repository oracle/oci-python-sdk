# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .schedule import Schedule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CronSchedule(Schedule):
    """
    Cron schedule for a scheduled task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CronSchedule object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.CronSchedule.type` attribute
        of this class is ``CRON`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CronSchedule.
            Allowed values for this property are: "FIXED_FREQUENCY", "CRON"
        :type type: str

        :param misfire_policy:
            The value to assign to the misfire_policy property of this CronSchedule.
            Allowed values for this property are: "RETRY_ONCE", "RETRY_INDEFINITELY", "SKIP"
        :type misfire_policy: str

        :param time_of_first_execution:
            The value to assign to the time_of_first_execution property of this CronSchedule.
        :type time_of_first_execution: datetime

        :param expression:
            The value to assign to the expression property of this CronSchedule.
        :type expression: str

        :param time_zone:
            The value to assign to the time_zone property of this CronSchedule.
        :type time_zone: str

        """
        self.swagger_types = {
            'type': 'str',
            'misfire_policy': 'str',
            'time_of_first_execution': 'datetime',
            'expression': 'str',
            'time_zone': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'misfire_policy': 'misfirePolicy',
            'time_of_first_execution': 'timeOfFirstExecution',
            'expression': 'expression',
            'time_zone': 'timeZone'
        }

        self._type = None
        self._misfire_policy = None
        self._time_of_first_execution = None
        self._expression = None
        self._time_zone = None
        self._type = 'CRON'

    @property
    def expression(self):
        """
        **[Required]** Gets the expression of this CronSchedule.
        Value in cron format.


        :return: The expression of this CronSchedule.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this CronSchedule.
        Value in cron format.


        :param expression: The expression of this CronSchedule.
        :type: str
        """
        self._expression = expression

    @property
    def time_zone(self):
        """
        **[Required]** Gets the time_zone of this CronSchedule.
        Time zone, by default UTC.


        :return: The time_zone of this CronSchedule.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this CronSchedule.
        Time zone, by default UTC.


        :param time_zone: The time_zone of this CronSchedule.
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
