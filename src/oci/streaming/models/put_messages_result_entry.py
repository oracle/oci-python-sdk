# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PutMessagesResultEntry(object):
    """
    Represents the result of a :func:`put_messages` request, whether it was successful or not.
    If a message was successfully appended to the stream, the entry includes the `offset`, `partition`, and `timestamp`.
    If the message failed to be appended to the stream, the entry includes the `error` and `errorMessage`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PutMessagesResultEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param partition:
            The value to assign to the partition property of this PutMessagesResultEntry.
        :type partition: str

        :param offset:
            The value to assign to the offset property of this PutMessagesResultEntry.
        :type offset: int

        :param timestamp:
            The value to assign to the timestamp property of this PutMessagesResultEntry.
        :type timestamp: datetime

        :param error:
            The value to assign to the error property of this PutMessagesResultEntry.
        :type error: str

        :param error_message:
            The value to assign to the error_message property of this PutMessagesResultEntry.
        :type error_message: str

        """
        self.swagger_types = {
            'partition': 'str',
            'offset': 'int',
            'timestamp': 'datetime',
            'error': 'str',
            'error_message': 'str'
        }

        self.attribute_map = {
            'partition': 'partition',
            'offset': 'offset',
            'timestamp': 'timestamp',
            'error': 'error',
            'error_message': 'errorMessage'
        }

        self._partition = None
        self._offset = None
        self._timestamp = None
        self._error = None
        self._error_message = None

    @property
    def partition(self):
        """
        Gets the partition of this PutMessagesResultEntry.
        The ID of the partition where the message was stored.


        :return: The partition of this PutMessagesResultEntry.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """
        Sets the partition of this PutMessagesResultEntry.
        The ID of the partition where the message was stored.


        :param partition: The partition of this PutMessagesResultEntry.
        :type: str
        """
        self._partition = partition

    @property
    def offset(self):
        """
        Gets the offset of this PutMessagesResultEntry.
        The offset of the message in the partition.


        :return: The offset of this PutMessagesResultEntry.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this PutMessagesResultEntry.
        The offset of the message in the partition.


        :param offset: The offset of this PutMessagesResultEntry.
        :type: int
        """
        self._offset = offset

    @property
    def timestamp(self):
        """
        Gets the timestamp of this PutMessagesResultEntry.
        The timestamp indicating when the server appended the message to the stream.


        :return: The timestamp of this PutMessagesResultEntry.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this PutMessagesResultEntry.
        The timestamp indicating when the server appended the message to the stream.


        :param timestamp: The timestamp of this PutMessagesResultEntry.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def error(self):
        """
        Gets the error of this PutMessagesResultEntry.
        The error code, in case the message was not successfully appended to the stream.


        :return: The error of this PutMessagesResultEntry.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this PutMessagesResultEntry.
        The error code, in case the message was not successfully appended to the stream.


        :param error: The error of this PutMessagesResultEntry.
        :type: str
        """
        self._error = error

    @property
    def error_message(self):
        """
        Gets the error_message of this PutMessagesResultEntry.
        A human-readable error message associated with the error code.


        :return: The error_message of this PutMessagesResultEntry.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this PutMessagesResultEntry.
        A human-readable error message associated with the error code.


        :param error_message: The error_message of this PutMessagesResultEntry.
        :type: str
        """
        self._error_message = error_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
