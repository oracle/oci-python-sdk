# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateJobDetails(object):
    """
    Job properties that can be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateJobDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateJobDetails.
        :type description: str

        :param schedule_cron_expression:
            The value to assign to the schedule_cron_expression property of this UpdateJobDetails.
        :type schedule_cron_expression: str

        :param time_schedule_begin:
            The value to assign to the time_schedule_begin property of this UpdateJobDetails.
        :type time_schedule_begin: datetime

        :param time_schedule_end:
            The value to assign to the time_schedule_end property of this UpdateJobDetails.
        :type time_schedule_end: datetime

        :param connection_key:
            The value to assign to the connection_key property of this UpdateJobDetails.
        :type connection_key: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'schedule_cron_expression': 'str',
            'time_schedule_begin': 'datetime',
            'time_schedule_end': 'datetime',
            'connection_key': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'schedule_cron_expression': 'scheduleCronExpression',
            'time_schedule_begin': 'timeScheduleBegin',
            'time_schedule_end': 'timeScheduleEnd',
            'connection_key': 'connectionKey'
        }

        self._display_name = None
        self._description = None
        self._schedule_cron_expression = None
        self._time_schedule_begin = None
        self._time_schedule_end = None
        self._connection_key = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateJobDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateJobDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateJobDetails.
        Detailed description of the job.


        :return: The description of this UpdateJobDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateJobDetails.
        Detailed description of the job.


        :param description: The description of this UpdateJobDetails.
        :type: str
        """
        self._description = description

    @property
    def schedule_cron_expression(self):
        """
        Gets the schedule_cron_expression of this UpdateJobDetails.
        Interval on which the job will be run. Value is specified as a cron-supported time specification \"nickname\".
        The following subset of those is supported: @monthly, @weekly, @daily, @hourly.


        :return: The schedule_cron_expression of this UpdateJobDetails.
        :rtype: str
        """
        return self._schedule_cron_expression

    @schedule_cron_expression.setter
    def schedule_cron_expression(self, schedule_cron_expression):
        """
        Sets the schedule_cron_expression of this UpdateJobDetails.
        Interval on which the job will be run. Value is specified as a cron-supported time specification \"nickname\".
        The following subset of those is supported: @monthly, @weekly, @daily, @hourly.


        :param schedule_cron_expression: The schedule_cron_expression of this UpdateJobDetails.
        :type: str
        """
        self._schedule_cron_expression = schedule_cron_expression

    @property
    def time_schedule_begin(self):
        """
        Gets the time_schedule_begin of this UpdateJobDetails.
        Date that the schedule should be operational. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_schedule_begin of this UpdateJobDetails.
        :rtype: datetime
        """
        return self._time_schedule_begin

    @time_schedule_begin.setter
    def time_schedule_begin(self, time_schedule_begin):
        """
        Sets the time_schedule_begin of this UpdateJobDetails.
        Date that the schedule should be operational. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_schedule_begin: The time_schedule_begin of this UpdateJobDetails.
        :type: datetime
        """
        self._time_schedule_begin = time_schedule_begin

    @property
    def time_schedule_end(self):
        """
        Gets the time_schedule_end of this UpdateJobDetails.
        Date that the schedule should end from being operational. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_schedule_end of this UpdateJobDetails.
        :rtype: datetime
        """
        return self._time_schedule_end

    @time_schedule_end.setter
    def time_schedule_end(self, time_schedule_end):
        """
        Sets the time_schedule_end of this UpdateJobDetails.
        Date that the schedule should end from being operational. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_schedule_end: The time_schedule_end of this UpdateJobDetails.
        :type: datetime
        """
        self._time_schedule_end = time_schedule_end

    @property
    def connection_key(self):
        """
        Gets the connection_key of this UpdateJobDetails.
        The key of the connection resource that is used for the harvest by this job.


        :return: The connection_key of this UpdateJobDetails.
        :rtype: str
        """
        return self._connection_key

    @connection_key.setter
    def connection_key(self, connection_key):
        """
        Sets the connection_key of this UpdateJobDetails.
        The key of the connection resource that is used for the harvest by this job.


        :param connection_key: The connection_key of this UpdateJobDetails.
        :type: str
        """
        self._connection_key = connection_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
