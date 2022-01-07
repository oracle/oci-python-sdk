# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublishResult(object):
    """
    The response to a PublishMessage call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PublishResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message_id:
            The value to assign to the message_id property of this PublishResult.
        :type message_id: str

        :param time_stamp:
            The value to assign to the time_stamp property of this PublishResult.
        :type time_stamp: datetime

        """
        self.swagger_types = {
            'message_id': 'str',
            'time_stamp': 'datetime'
        }

        self.attribute_map = {
            'message_id': 'messageId',
            'time_stamp': 'timeStamp'
        }

        self._message_id = None
        self._time_stamp = None

    @property
    def message_id(self):
        """
        **[Required]** Gets the message_id of this PublishResult.
        The UUID of the message.


        :return: The message_id of this PublishResult.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """
        Sets the message_id of this PublishResult.
        The UUID of the message.


        :param message_id: The message_id of this PublishResult.
        :type: str
        """
        self._message_id = message_id

    @property
    def time_stamp(self):
        """
        Gets the time_stamp of this PublishResult.
        The time that the service received the message.


        :return: The time_stamp of this PublishResult.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """
        Sets the time_stamp of this PublishResult.
        The time that the service received the message.


        :param time_stamp: The time_stamp of this PublishResult.
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
