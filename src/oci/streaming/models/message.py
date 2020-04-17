# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Message(object):
    """
    A message in a stream.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Message object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stream:
            The value to assign to the stream property of this Message.
        :type stream: str

        :param partition:
            The value to assign to the partition property of this Message.
        :type partition: str

        :param key:
            The value to assign to the key property of this Message.
        :type key: str

        :param value:
            The value to assign to the value property of this Message.
        :type value: str

        :param offset:
            The value to assign to the offset property of this Message.
        :type offset: int

        :param timestamp:
            The value to assign to the timestamp property of this Message.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'stream': 'str',
            'partition': 'str',
            'key': 'str',
            'value': 'str',
            'offset': 'int',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'stream': 'stream',
            'partition': 'partition',
            'key': 'key',
            'value': 'value',
            'offset': 'offset',
            'timestamp': 'timestamp'
        }

        self._stream = None
        self._partition = None
        self._key = None
        self._value = None
        self._offset = None
        self._timestamp = None

    @property
    def stream(self):
        """
        **[Required]** Gets the stream of this Message.
        The name of the stream that the message belongs to.


        :return: The stream of this Message.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """
        Sets the stream of this Message.
        The name of the stream that the message belongs to.


        :param stream: The stream of this Message.
        :type: str
        """
        self._stream = stream

    @property
    def partition(self):
        """
        **[Required]** Gets the partition of this Message.
        The ID of the partition where the message is stored.


        :return: The partition of this Message.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """
        Sets the partition of this Message.
        The ID of the partition where the message is stored.


        :param partition: The partition of this Message.
        :type: str
        """
        self._partition = partition

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Message.
        The key associated with the message, expressed as a byte array.


        :return: The key of this Message.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Message.
        The key associated with the message, expressed as a byte array.


        :param key: The key of this Message.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Message.
        The value associated with the message, expressed as a byte array.


        :return: The value of this Message.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Message.
        The value associated with the message, expressed as a byte array.


        :param value: The value of this Message.
        :type: str
        """
        self._value = value

    @property
    def offset(self):
        """
        **[Required]** Gets the offset of this Message.
        The offset of the message, which uniquely identifies it within the partition.


        :return: The offset of this Message.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this Message.
        The offset of the message, which uniquely identifies it within the partition.


        :param offset: The offset of this Message.
        :type: int
        """
        self._offset = offset

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this Message.
        The timestamp indicating when the server appended the message to the stream.


        :return: The timestamp of this Message.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Message.
        The timestamp indicating when the server appended the message to the stream.


        :param timestamp: The timestamp of this Message.
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
