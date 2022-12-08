# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMessagesResultEntry(object):
    """
    Represents the result of a UpdateMessages request, whether it was successful or not.
    If a message was successfully updated in the queue, the entry includes the `id` and `visibleAfter` fields.
    If a message failed to be updated in the queue, the entry includes the `errorCode` and `errorMessage` fields.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMessagesResultEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this UpdateMessagesResultEntry.
        :type id: int

        :param visible_after:
            The value to assign to the visible_after property of this UpdateMessagesResultEntry.
        :type visible_after: datetime

        :param error_code:
            The value to assign to the error_code property of this UpdateMessagesResultEntry.
        :type error_code: int

        :param error_message:
            The value to assign to the error_message property of this UpdateMessagesResultEntry.
        :type error_message: str

        """
        self.swagger_types = {
            'id': 'int',
            'visible_after': 'datetime',
            'error_code': 'int',
            'error_message': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'visible_after': 'visibleAfter',
            'error_code': 'errorCode',
            'error_message': 'errorMessage'
        }

        self._id = None
        self._visible_after = None
        self._error_code = None
        self._error_message = None

    @property
    def id(self):
        """
        Gets the id of this UpdateMessagesResultEntry.
        The id of the message that's been updated.


        :return: The id of this UpdateMessagesResultEntry.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateMessagesResultEntry.
        The id of the message that's been updated.


        :param id: The id of this UpdateMessagesResultEntry.
        :type: int
        """
        self._id = id

    @property
    def visible_after(self):
        """
        Gets the visible_after of this UpdateMessagesResultEntry.
        The time after which the message will be visible to other consumers. An RFC3339 formatted datetime string


        :return: The visible_after of this UpdateMessagesResultEntry.
        :rtype: datetime
        """
        return self._visible_after

    @visible_after.setter
    def visible_after(self, visible_after):
        """
        Sets the visible_after of this UpdateMessagesResultEntry.
        The time after which the message will be visible to other consumers. An RFC3339 formatted datetime string


        :param visible_after: The visible_after of this UpdateMessagesResultEntry.
        :type: datetime
        """
        self._visible_after = visible_after

    @property
    def error_code(self):
        """
        Gets the error_code of this UpdateMessagesResultEntry.
        The error code, in case the message was not successfully updated in the queue.


        :return: The error_code of this UpdateMessagesResultEntry.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this UpdateMessagesResultEntry.
        The error code, in case the message was not successfully updated in the queue.


        :param error_code: The error_code of this UpdateMessagesResultEntry.
        :type: int
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """
        Gets the error_message of this UpdateMessagesResultEntry.
        A human-readable error message associated with the error code.


        :return: The error_message of this UpdateMessagesResultEntry.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this UpdateMessagesResultEntry.
        A human-readable error message associated with the error code.


        :param error_message: The error_message of this UpdateMessagesResultEntry.
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
