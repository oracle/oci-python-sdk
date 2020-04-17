# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestError(object):
    """
    Description of the unexpected error that prevented completion of the request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestError object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this WorkRequestError.
        :type code: str

        :param message:
            The value to assign to the message property of this WorkRequestError.
        :type message: str

        :param time_stamp:
            The value to assign to the time_stamp property of this WorkRequestError.
        :type time_stamp: datetime

        """
        self.swagger_types = {
            'code': 'str',
            'message': 'str',
            'time_stamp': 'datetime'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'time_stamp': 'timeStamp'
        }

        self._code = None
        self._message = None
        self._time_stamp = None

    @property
    def code(self):
        """
        **[Required]** Gets the code of this WorkRequestError.
        A machine-usable code for the error that occurred. Error codes are listed at
        (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)


        :return: The code of this WorkRequestError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this WorkRequestError.
        A machine-usable code for the error that occurred. Error codes are listed at
        (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)


        :param code: The code of this WorkRequestError.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        **[Required]** Gets the message of this WorkRequestError.
        A human-readable description of the issue.


        :return: The message of this WorkRequestError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequestError.
        A human-readable description of the issue.


        :param message: The message of this WorkRequestError.
        :type: str
        """
        self._message = message

    @property
    def time_stamp(self):
        """
        **[Required]** Gets the time_stamp of this WorkRequestError.
        When the error occurred. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_stamp of this WorkRequestError.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """
        Sets the time_stamp of this WorkRequestError.
        When the error occurred. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_stamp: The time_stamp of this WorkRequestError.
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
