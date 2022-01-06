# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PutMessagesResult(object):
    """
    The response to a :func:`put_messages` request. It indicates the number
    of failed messages as well as an array of results for successful and failed messages.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PutMessagesResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param failures:
            The value to assign to the failures property of this PutMessagesResult.
        :type failures: int

        :param entries:
            The value to assign to the entries property of this PutMessagesResult.
        :type entries: list[oci.streaming.models.PutMessagesResultEntry]

        """
        self.swagger_types = {
            'failures': 'int',
            'entries': 'list[PutMessagesResultEntry]'
        }

        self.attribute_map = {
            'failures': 'failures',
            'entries': 'entries'
        }

        self._failures = None
        self._entries = None

    @property
    def failures(self):
        """
        **[Required]** Gets the failures of this PutMessagesResult.
        The number of messages that failed to be added to the stream.


        :return: The failures of this PutMessagesResult.
        :rtype: int
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        """
        Sets the failures of this PutMessagesResult.
        The number of messages that failed to be added to the stream.


        :param failures: The failures of this PutMessagesResult.
        :type: int
        """
        self._failures = failures

    @property
    def entries(self):
        """
        **[Required]** Gets the entries of this PutMessagesResult.
        An array of items representing the result of each message.
        The order is guaranteed to be the same as in the `PutMessagesDetails` object.
        If a message was successfully appended to the stream, the entry includes the `offset`, `partition`, and `timestamp`.
        If a message failed to be appended to the stream, the entry includes the `error` and `errorMessage`.


        :return: The entries of this PutMessagesResult.
        :rtype: list[oci.streaming.models.PutMessagesResultEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this PutMessagesResult.
        An array of items representing the result of each message.
        The order is guaranteed to be the same as in the `PutMessagesDetails` object.
        If a message was successfully appended to the stream, the entry includes the `offset`, `partition`, and `timestamp`.
        If a message failed to be appended to the stream, the entry includes the `error` and `errorMessage`.


        :param entries: The entries of this PutMessagesResult.
        :type: list[oci.streaming.models.PutMessagesResultEntry]
        """
        self._entries = entries

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
