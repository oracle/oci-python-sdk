# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestLogEntry(object):
    """
    A log message from the execution of a work request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestLogEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this WorkRequestLogEntry.
        :type message: str

        :param time_stamp:
            The value to assign to the time_stamp property of this WorkRequestLogEntry.
        :type time_stamp: datetime

        """
        self.swagger_types = {
            'message': 'str',
            'time_stamp': 'datetime'
        }

        self.attribute_map = {
            'message': 'message',
            'time_stamp': 'timeStamp'
        }

        self._message = None
        self._time_stamp = None

    @property
    def message(self):
        """
        **[Required]** Gets the message of this WorkRequestLogEntry.
        Human-readable log message.


        :return: The message of this WorkRequestLogEntry.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequestLogEntry.
        Human-readable log message.


        :param message: The message of this WorkRequestLogEntry.
        :type: str
        """
        self._message = message

    @property
    def time_stamp(self):
        """
        **[Required]** Gets the time_stamp of this WorkRequestLogEntry.
        When the log message was written. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_stamp of this WorkRequestLogEntry.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """
        Sets the time_stamp of this WorkRequestLogEntry.
        When the log message was written. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_stamp: The time_stamp of this WorkRequestLogEntry.
        :type: datetime
        """
        self._time_stamp = time_stamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
