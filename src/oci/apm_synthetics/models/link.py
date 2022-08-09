# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Link(object):
    """
    link between 2 nodes
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Link object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Link.
        :type id: str

        :param source:
            The value to assign to the source property of this Link.
        :type source: str

        :param destination:
            The value to assign to the destination property of this Link.
        :type destination: str

        :param repeat_count:
            The value to assign to the repeat_count property of this Link.
        :type repeat_count: int

        :param forwarding_loss:
            The value to assign to the forwarding_loss property of this Link.
        :type forwarding_loss: float

        :param delay_in_milliseconds:
            The value to assign to the delay_in_milliseconds property of this Link.
        :type delay_in_milliseconds: float

        :param min_delay_in_milliseconds:
            The value to assign to the min_delay_in_milliseconds property of this Link.
        :type min_delay_in_milliseconds: float

        :param max_delay_in_milliseconds:
            The value to assign to the max_delay_in_milliseconds property of this Link.
        :type max_delay_in_milliseconds: float

        """
        self.swagger_types = {
            'id': 'str',
            'source': 'str',
            'destination': 'str',
            'repeat_count': 'int',
            'forwarding_loss': 'float',
            'delay_in_milliseconds': 'float',
            'min_delay_in_milliseconds': 'float',
            'max_delay_in_milliseconds': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'source': 'source',
            'destination': 'destination',
            'repeat_count': 'repeatCount',
            'forwarding_loss': 'forwardingLoss',
            'delay_in_milliseconds': 'delayInMilliseconds',
            'min_delay_in_milliseconds': 'minDelayInMilliseconds',
            'max_delay_in_milliseconds': 'maxDelayInMilliseconds'
        }

        self._id = None
        self._source = None
        self._destination = None
        self._repeat_count = None
        self._forwarding_loss = None
        self._delay_in_milliseconds = None
        self._min_delay_in_milliseconds = None
        self._max_delay_in_milliseconds = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Link.
        id of Link


        :return: The id of this Link.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Link.
        id of Link


        :param id: The id of this Link.
        :type: str
        """
        self._id = id

    @property
    def source(self):
        """
        Gets the source of this Link.
        source node id


        :return: The source of this Link.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this Link.
        source node id


        :param source: The source of this Link.
        :type: str
        """
        self._source = source

    @property
    def destination(self):
        """
        Gets the destination of this Link.
        destination node id


        :return: The destination of this Link.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this Link.
        destination node id


        :param destination: The destination of this Link.
        :type: str
        """
        self._destination = destination

    @property
    def repeat_count(self):
        """
        Gets the repeat_count of this Link.
        number of times this link is repeated


        :return: The repeat_count of this Link.
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """
        Sets the repeat_count of this Link.
        number of times this link is repeated


        :param repeat_count: The repeat_count of this Link.
        :type: int
        """
        self._repeat_count = repeat_count

    @property
    def forwarding_loss(self):
        """
        Gets the forwarding_loss of this Link.
        average packet loss


        :return: The forwarding_loss of this Link.
        :rtype: float
        """
        return self._forwarding_loss

    @forwarding_loss.setter
    def forwarding_loss(self, forwarding_loss):
        """
        Sets the forwarding_loss of this Link.
        average packet loss


        :param forwarding_loss: The forwarding_loss of this Link.
        :type: float
        """
        self._forwarding_loss = forwarding_loss

    @property
    def delay_in_milliseconds(self):
        """
        Gets the delay_in_milliseconds of this Link.
        difference of packet response time between source and destination in milliseconds


        :return: The delay_in_milliseconds of this Link.
        :rtype: float
        """
        return self._delay_in_milliseconds

    @delay_in_milliseconds.setter
    def delay_in_milliseconds(self, delay_in_milliseconds):
        """
        Sets the delay_in_milliseconds of this Link.
        difference of packet response time between source and destination in milliseconds


        :param delay_in_milliseconds: The delay_in_milliseconds of this Link.
        :type: float
        """
        self._delay_in_milliseconds = delay_in_milliseconds

    @property
    def min_delay_in_milliseconds(self):
        """
        Gets the min_delay_in_milliseconds of this Link.
        minimum delay in milliseconds


        :return: The min_delay_in_milliseconds of this Link.
        :rtype: float
        """
        return self._min_delay_in_milliseconds

    @min_delay_in_milliseconds.setter
    def min_delay_in_milliseconds(self, min_delay_in_milliseconds):
        """
        Sets the min_delay_in_milliseconds of this Link.
        minimum delay in milliseconds


        :param min_delay_in_milliseconds: The min_delay_in_milliseconds of this Link.
        :type: float
        """
        self._min_delay_in_milliseconds = min_delay_in_milliseconds

    @property
    def max_delay_in_milliseconds(self):
        """
        Gets the max_delay_in_milliseconds of this Link.
        maximum delay in milliseconds


        :return: The max_delay_in_milliseconds of this Link.
        :rtype: float
        """
        return self._max_delay_in_milliseconds

    @max_delay_in_milliseconds.setter
    def max_delay_in_milliseconds(self, max_delay_in_milliseconds):
        """
        Sets the max_delay_in_milliseconds of this Link.
        maximum delay in milliseconds


        :param max_delay_in_milliseconds: The max_delay_in_milliseconds of this Link.
        :type: float
        """
        self._max_delay_in_milliseconds = max_delay_in_milliseconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
