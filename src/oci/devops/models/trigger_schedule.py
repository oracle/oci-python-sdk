# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TriggerSchedule(object):
    """
    Specifies a trigger schedule. Timing information for when to initiate automated syncs.
    """

    #: A constant which can be used with the schedule_type property of a TriggerSchedule.
    #: This constant has a value of "NONE"
    SCHEDULE_TYPE_NONE = "NONE"

    #: A constant which can be used with the schedule_type property of a TriggerSchedule.
    #: This constant has a value of "DEFAULT"
    SCHEDULE_TYPE_DEFAULT = "DEFAULT"

    #: A constant which can be used with the schedule_type property of a TriggerSchedule.
    #: This constant has a value of "CUSTOM"
    SCHEDULE_TYPE_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new TriggerSchedule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schedule_type:
            The value to assign to the schedule_type property of this TriggerSchedule.
            Allowed values for this property are: "NONE", "DEFAULT", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type schedule_type: str

        :param custom_schedule:
            The value to assign to the custom_schedule property of this TriggerSchedule.
        :type custom_schedule: str

        """
        self.swagger_types = {
            'schedule_type': 'str',
            'custom_schedule': 'str'
        }

        self.attribute_map = {
            'schedule_type': 'scheduleType',
            'custom_schedule': 'customSchedule'
        }

        self._schedule_type = None
        self._custom_schedule = None

    @property
    def schedule_type(self):
        """
        **[Required]** Gets the schedule_type of this TriggerSchedule.
        Different types of trigger schedule:
        NONE - No automated synchronization schedule.
        DEFAULT - Trigger schedule is every 30 minutes.
        CUSTOM - Custom triggering schedule.

        Allowed values for this property are: "NONE", "DEFAULT", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The schedule_type of this TriggerSchedule.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this TriggerSchedule.
        Different types of trigger schedule:
        NONE - No automated synchronization schedule.
        DEFAULT - Trigger schedule is every 30 minutes.
        CUSTOM - Custom triggering schedule.


        :param schedule_type: The schedule_type of this TriggerSchedule.
        :type: str
        """
        allowed_values = ["NONE", "DEFAULT", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(schedule_type, allowed_values):
            schedule_type = 'UNKNOWN_ENUM_VALUE'
        self._schedule_type = schedule_type

    @property
    def custom_schedule(self):
        """
        Gets the custom_schedule of this TriggerSchedule.
        Valid if type is CUSTOM. Following RFC 5545 recurrence rules, we can specify starting time, occurrence frequency, and interval size.
        Example for frequency could be DAILY/WEEKLY/HOURLY or any RFC 5545 supported frequency, which is followed by start time of this window.
        You can control the start time with BYHOUR, BYMINUTE and BYSECONDS. It is followed by the interval size.


        :return: The custom_schedule of this TriggerSchedule.
        :rtype: str
        """
        return self._custom_schedule

    @custom_schedule.setter
    def custom_schedule(self, custom_schedule):
        """
        Sets the custom_schedule of this TriggerSchedule.
        Valid if type is CUSTOM. Following RFC 5545 recurrence rules, we can specify starting time, occurrence frequency, and interval size.
        Example for frequency could be DAILY/WEEKLY/HOURLY or any RFC 5545 supported frequency, which is followed by start time of this window.
        You can control the start time with BYHOUR, BYMINUTE and BYSECONDS. It is followed by the interval size.


        :param custom_schedule: The custom_schedule of this TriggerSchedule.
        :type: str
        """
        self._custom_schedule = custom_schedule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
