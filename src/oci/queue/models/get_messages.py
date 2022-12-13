# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GetMessages(object):
    """
    A list of messages from a queue.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GetMessages object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param messages:
            The value to assign to the messages property of this GetMessages.
        :type messages: list[oci.queue.models.GetMessage]

        """
        self.swagger_types = {
            'messages': 'list[GetMessage]'
        }

        self.attribute_map = {
            'messages': 'messages'
        }

        self._messages = None

    @property
    def messages(self):
        """
        **[Required]** Gets the messages of this GetMessages.
        List of messages from a queue.


        :return: The messages of this GetMessages.
        :rtype: list[oci.queue.models.GetMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this GetMessages.
        List of messages from a queue.


        :param messages: The messages of this GetMessages.
        :type: list[oci.queue.models.GetMessage]
        """
        self._messages = messages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other