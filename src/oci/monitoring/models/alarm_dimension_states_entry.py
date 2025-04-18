# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180401


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlarmDimensionStatesEntry(object):
    """
    A timestamped alarm state entry for a metric stream.
    """

    #: A constant which can be used with the status property of a AlarmDimensionStatesEntry.
    #: This constant has a value of "FIRING"
    STATUS_FIRING = "FIRING"

    #: A constant which can be used with the status property of a AlarmDimensionStatesEntry.
    #: This constant has a value of "OK"
    STATUS_OK = "OK"

    def __init__(self, **kwargs):
        """
        Initializes a new AlarmDimensionStatesEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param alarm_summary:
            The value to assign to the alarm_summary property of this AlarmDimensionStatesEntry.
        :type alarm_summary: str

        :param dimensions:
            The value to assign to the dimensions property of this AlarmDimensionStatesEntry.
        :type dimensions: dict(str, str)

        :param status:
            The value to assign to the status property of this AlarmDimensionStatesEntry.
            Allowed values for this property are: "FIRING", "OK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param rule_name:
            The value to assign to the rule_name property of this AlarmDimensionStatesEntry.
        :type rule_name: str

        :param timestamp:
            The value to assign to the timestamp property of this AlarmDimensionStatesEntry.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'alarm_summary': 'str',
            'dimensions': 'dict(str, str)',
            'status': 'str',
            'rule_name': 'str',
            'timestamp': 'datetime'
        }
        self.attribute_map = {
            'alarm_summary': 'alarmSummary',
            'dimensions': 'dimensions',
            'status': 'status',
            'rule_name': 'ruleName',
            'timestamp': 'timestamp'
        }
        self._alarm_summary = None
        self._dimensions = None
        self._status = None
        self._rule_name = None
        self._timestamp = None

    @property
    def alarm_summary(self):
        """
        **[Required]** Gets the alarm_summary of this AlarmDimensionStatesEntry.
        Customizable alarm summary (`alarmSummary` `alarm message parameter`__).
        Optionally include `dynamic variables`__.
        The alarm summary appears within the body of the alarm message and in responses to
        :func:`list_alarms_status`
        :func:`get_alarm_history` and
        :func:`retrieve_dimension_states`.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/alarm-message-format.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm


        :return: The alarm_summary of this AlarmDimensionStatesEntry.
        :rtype: str
        """
        return self._alarm_summary

    @alarm_summary.setter
    def alarm_summary(self, alarm_summary):
        """
        Sets the alarm_summary of this AlarmDimensionStatesEntry.
        Customizable alarm summary (`alarmSummary` `alarm message parameter`__).
        Optionally include `dynamic variables`__.
        The alarm summary appears within the body of the alarm message and in responses to
        :func:`list_alarms_status`
        :func:`get_alarm_history` and
        :func:`retrieve_dimension_states`.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/alarm-message-format.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm


        :param alarm_summary: The alarm_summary of this AlarmDimensionStatesEntry.
        :type: str
        """
        self._alarm_summary = alarm_summary

    @property
    def dimensions(self):
        """
        **[Required]** Gets the dimensions of this AlarmDimensionStatesEntry.
        Indicator of the metric stream associated with the alarm state entry. Includes one or more dimension key-value pairs.


        :return: The dimensions of this AlarmDimensionStatesEntry.
        :rtype: dict(str, str)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this AlarmDimensionStatesEntry.
        Indicator of the metric stream associated with the alarm state entry. Includes one or more dimension key-value pairs.


        :param dimensions: The dimensions of this AlarmDimensionStatesEntry.
        :type: dict(str, str)
        """
        self._dimensions = dimensions

    @property
    def status(self):
        """
        **[Required]** Gets the status of this AlarmDimensionStatesEntry.
        Transition state (status value) associated with the alarm state entry.

        Example: `FIRING`

        Allowed values for this property are: "FIRING", "OK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AlarmDimensionStatesEntry.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AlarmDimensionStatesEntry.
        Transition state (status value) associated with the alarm state entry.

        Example: `FIRING`


        :param status: The status of this AlarmDimensionStatesEntry.
        :type: str
        """
        allowed_values = ["FIRING", "OK"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def rule_name(self):
        """
        **[Required]** Gets the rule_name of this AlarmDimensionStatesEntry.
        Identifier of the alarm's base values for alarm evaluation, for use when the alarm contains overrides.
        Default value is `BASE`. For information about alarm overrides, see :func:`alarm_override`.


        :return: The rule_name of this AlarmDimensionStatesEntry.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """
        Sets the rule_name of this AlarmDimensionStatesEntry.
        Identifier of the alarm's base values for alarm evaluation, for use when the alarm contains overrides.
        Default value is `BASE`. For information about alarm overrides, see :func:`alarm_override`.


        :param rule_name: The rule_name of this AlarmDimensionStatesEntry.
        :type: str
        """
        self._rule_name = rule_name

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this AlarmDimensionStatesEntry.
        Transition time associated with the alarm state entry. Format defined by RFC3339.

        Example: `2022-02-01T01:02:29.600Z`


        :return: The timestamp of this AlarmDimensionStatesEntry.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this AlarmDimensionStatesEntry.
        Transition time associated with the alarm state entry. Format defined by RFC3339.

        Example: `2022-02-01T01:02:29.600Z`


        :param timestamp: The timestamp of this AlarmDimensionStatesEntry.
        :type: datetime
        """
        self._timestamp = timestamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
