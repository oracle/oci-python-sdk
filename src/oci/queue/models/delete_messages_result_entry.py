# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeleteMessagesResultEntry(object):
    """
    Represents the result of a DeleteMessages request, whether it was successful or not.
    If a message was successfully deleted from the queue, the entry does not contain any fields.
    If a message failed to be deleted from the queue, the entry includes the `errorCode` and `errorMessage` fields.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeleteMessagesResultEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param error_code:
            The value to assign to the error_code property of this DeleteMessagesResultEntry.
        :type error_code: int

        :param error_message:
            The value to assign to the error_message property of this DeleteMessagesResultEntry.
        :type error_message: str

        """
        self.swagger_types = {
            'error_code': 'int',
            'error_message': 'str'
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'error_message': 'errorMessage'
        }

        self._error_code = None
        self._error_message = None

    @property
    def error_code(self):
        """
        Gets the error_code of this DeleteMessagesResultEntry.
        The error code, in case the message was not successfully deleted from the queue.


        :return: The error_code of this DeleteMessagesResultEntry.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this DeleteMessagesResultEntry.
        The error code, in case the message was not successfully deleted from the queue.


        :param error_code: The error_code of this DeleteMessagesResultEntry.
        :type: int
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """
        Gets the error_message of this DeleteMessagesResultEntry.
        A human-readable error message associated with the error code.


        :return: The error_message of this DeleteMessagesResultEntry.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this DeleteMessagesResultEntry.
        A human-readable error message associated with the error code.


        :param error_message: The error_message of this DeleteMessagesResultEntry.
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
