# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Group(object):
    """
    Represents the current state of a consumer group, including partition reservations and committed offsets.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Group object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stream_id:
            The value to assign to the stream_id property of this Group.
        :type stream_id: str

        :param group_name:
            The value to assign to the group_name property of this Group.
        :type group_name: str

        :param reservations:
            The value to assign to the reservations property of this Group.
        :type reservations: list[oci.streaming.models.PartitionReservation]

        """
        self.swagger_types = {
            'stream_id': 'str',
            'group_name': 'str',
            'reservations': 'list[PartitionReservation]'
        }

        self.attribute_map = {
            'stream_id': 'streamId',
            'group_name': 'groupName',
            'reservations': 'reservations'
        }

        self._stream_id = None
        self._group_name = None
        self._reservations = None

    @property
    def stream_id(self):
        """
        **[Required]** Gets the stream_id of this Group.
        The streamId for which the group exists.


        :return: The stream_id of this Group.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this Group.
        The streamId for which the group exists.


        :param stream_id: The stream_id of this Group.
        :type: str
        """
        self._stream_id = stream_id

    @property
    def group_name(self):
        """
        **[Required]** Gets the group_name of this Group.
        The name of the consumer group.


        :return: The group_name of this Group.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this Group.
        The name of the consumer group.


        :param group_name: The group_name of this Group.
        :type: str
        """
        self._group_name = group_name

    @property
    def reservations(self):
        """
        Gets the reservations of this Group.
        An array of the partition reservations of a group.


        :return: The reservations of this Group.
        :rtype: list[oci.streaming.models.PartitionReservation]
        """
        return self._reservations

    @reservations.setter
    def reservations(self, reservations):
        """
        Sets the reservations of this Group.
        An array of the partition reservations of a group.


        :param reservations: The reservations of this Group.
        :type: list[oci.streaming.models.PartitionReservation]
        """
        self._reservations = reservations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
