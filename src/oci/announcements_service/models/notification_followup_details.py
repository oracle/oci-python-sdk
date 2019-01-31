# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NotificationFollowupDetails(object):
    """
    Information represents a notification follow-up
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NotificationFollowupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this NotificationFollowupDetails.
        :type message: str

        :param time_created:
            The value to assign to the time_created property of this NotificationFollowupDetails.
        :type time_created: datetime

        """
        self.swagger_types = {
            'message': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'message': 'message',
            'time_created': 'timeCreated'
        }

        self._message = None
        self._time_created = None

    @property
    def message(self):
        """
        Gets the message of this NotificationFollowupDetails.
        The follow-up message, a markdown format input


        :return: The message of this NotificationFollowupDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this NotificationFollowupDetails.
        The follow-up message, a markdown format input


        :param message: The message of this NotificationFollowupDetails.
        :type: str
        """
        self._message = message

    @property
    def time_created(self):
        """
        Gets the time_created of this NotificationFollowupDetails.
        When the update is made


        :return: The time_created of this NotificationFollowupDetails.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this NotificationFollowupDetails.
        When the update is made


        :param time_created: The time_created of this NotificationFollowupDetails.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
