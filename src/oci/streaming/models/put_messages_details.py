# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PutMessagesDetails(object):
    """
    Object that represents an array of messages to emit to a stream.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PutMessagesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param messages:
            The value to assign to the messages property of this PutMessagesDetails.
        :type messages: list[oci.streaming.models.PutMessagesDetailsEntry]

        """
        self.swagger_types = {
            'messages': 'list[PutMessagesDetailsEntry]'
        }

        self.attribute_map = {
            'messages': 'messages'
        }

        self._messages = None

    @property
    def messages(self):
        """
        **[Required]** Gets the messages of this PutMessagesDetails.
        The array of messages to put into a stream.


        :return: The messages of this PutMessagesDetails.
        :rtype: list[oci.streaming.models.PutMessagesDetailsEntry]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this PutMessagesDetails.
        The array of messages to put into a stream.


        :param messages: The messages of this PutMessagesDetails.
        :type: list[oci.streaming.models.PutMessagesDetailsEntry]
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
