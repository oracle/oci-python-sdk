# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogEntry(object):
    """
    Log entry for an operation resulting from a job's execution.
    """

    #: A constant which can be used with the type property of a LogEntry.
    #: This constant has a value of "TERRAFORM_CONSOLE"
    TYPE_TERRAFORM_CONSOLE = "TERRAFORM_CONSOLE"

    #: A constant which can be used with the level property of a LogEntry.
    #: This constant has a value of "TRACE"
    LEVEL_TRACE = "TRACE"

    #: A constant which can be used with the level property of a LogEntry.
    #: This constant has a value of "DEBUG"
    LEVEL_DEBUG = "DEBUG"

    #: A constant which can be used with the level property of a LogEntry.
    #: This constant has a value of "INFO"
    LEVEL_INFO = "INFO"

    #: A constant which can be used with the level property of a LogEntry.
    #: This constant has a value of "WARN"
    LEVEL_WARN = "WARN"

    #: A constant which can be used with the level property of a LogEntry.
    #: This constant has a value of "ERROR"
    LEVEL_ERROR = "ERROR"

    #: A constant which can be used with the level property of a LogEntry.
    #: This constant has a value of "FATAL"
    LEVEL_FATAL = "FATAL"

    def __init__(self, **kwargs):
        """
        Initializes a new LogEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this LogEntry.
            Allowed values for this property are: "TERRAFORM_CONSOLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param level:
            The value to assign to the level property of this LogEntry.
            Allowed values for this property are: "TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type level: str

        :param timestamp:
            The value to assign to the timestamp property of this LogEntry.
        :type timestamp: datetime

        :param message:
            The value to assign to the message property of this LogEntry.
        :type message: str

        """
        self.swagger_types = {
            'type': 'str',
            'level': 'str',
            'timestamp': 'datetime',
            'message': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'level': 'level',
            'timestamp': 'timestamp',
            'message': 'message'
        }

        self._type = None
        self._level = None
        self._timestamp = None
        self._message = None

    @property
    def type(self):
        """
        Gets the type of this LogEntry.
        Specifies the log type for the log entry.

        Allowed values for this property are: "TERRAFORM_CONSOLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this LogEntry.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LogEntry.
        Specifies the log type for the log entry.


        :param type: The type of this LogEntry.
        :type: str
        """
        allowed_values = ["TERRAFORM_CONSOLE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def level(self):
        """
        Gets the level of this LogEntry.
        Specifies the severity level of the log entry.

        Allowed values for this property are: "TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The level of this LogEntry.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this LogEntry.
        Specifies the severity level of the log entry.


        :param level: The level of this LogEntry.
        :type: str
        """
        allowed_values = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
        if not value_allowed_none_or_none_sentinel(level, allowed_values):
            level = 'UNKNOWN_ENUM_VALUE'
        self._level = level

    @property
    def timestamp(self):
        """
        Gets the timestamp of this LogEntry.
        The date and time of the log entry.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The timestamp of this LogEntry.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this LogEntry.
        The date and time of the log entry.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param timestamp: The timestamp of this LogEntry.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def message(self):
        """
        Gets the message of this LogEntry.
        The log entry value.


        :return: The message of this LogEntry.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this LogEntry.
        The log entry value.


        :param message: The message of this LogEntry.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
