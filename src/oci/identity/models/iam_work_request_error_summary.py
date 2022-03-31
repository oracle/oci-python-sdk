# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IamWorkRequestErrorSummary(object):
    """
    (For tenancies that support identity domains) An error encountered while executing an operation that is tracked by a IAM work request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IamWorkRequestErrorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this IamWorkRequestErrorSummary.
        :type code: str

        :param message:
            The value to assign to the message property of this IamWorkRequestErrorSummary.
        :type message: str

        :param timestamp:
            The value to assign to the timestamp property of this IamWorkRequestErrorSummary.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'code': 'str',
            'message': 'str',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'timestamp': 'timestamp'
        }

        self._code = None
        self._message = None
        self._timestamp = None

    @property
    def code(self):
        """
        **[Required]** Gets the code of this IamWorkRequestErrorSummary.
        A machine-usable code for the error that occured.


        :return: The code of this IamWorkRequestErrorSummary.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this IamWorkRequestErrorSummary.
        A machine-usable code for the error that occured.


        :param code: The code of this IamWorkRequestErrorSummary.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        **[Required]** Gets the message of this IamWorkRequestErrorSummary.
        A human-readable error string.


        :return: The message of this IamWorkRequestErrorSummary.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this IamWorkRequestErrorSummary.
        A human-readable error string.


        :param message: The message of this IamWorkRequestErrorSummary.
        :type: str
        """
        self._message = message

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this IamWorkRequestErrorSummary.
        The date and time the error occurred.


        :return: The timestamp of this IamWorkRequestErrorSummary.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this IamWorkRequestErrorSummary.
        The date and time the error occurred.


        :param timestamp: The timestamp of this IamWorkRequestErrorSummary.
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
