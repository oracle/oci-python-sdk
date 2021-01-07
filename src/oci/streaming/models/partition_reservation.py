# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PartitionReservation(object):
    """
    Represents the state of a single partition reservation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PartitionReservation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param partition:
            The value to assign to the partition property of this PartitionReservation.
        :type partition: str

        :param committed_offset:
            The value to assign to the committed_offset property of this PartitionReservation.
        :type committed_offset: int

        :param reserved_instance:
            The value to assign to the reserved_instance property of this PartitionReservation.
        :type reserved_instance: str

        :param time_reserved_until:
            The value to assign to the time_reserved_until property of this PartitionReservation.
        :type time_reserved_until: datetime

        """
        self.swagger_types = {
            'partition': 'str',
            'committed_offset': 'int',
            'reserved_instance': 'str',
            'time_reserved_until': 'datetime'
        }

        self.attribute_map = {
            'partition': 'partition',
            'committed_offset': 'committedOffset',
            'reserved_instance': 'reservedInstance',
            'time_reserved_until': 'timeReservedUntil'
        }

        self._partition = None
        self._committed_offset = None
        self._reserved_instance = None
        self._time_reserved_until = None

    @property
    def partition(self):
        """
        Gets the partition of this PartitionReservation.
        The partition for which the reservation applies.


        :return: The partition of this PartitionReservation.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """
        Sets the partition of this PartitionReservation.
        The partition for which the reservation applies.


        :param partition: The partition of this PartitionReservation.
        :type: str
        """
        self._partition = partition

    @property
    def committed_offset(self):
        """
        Gets the committed_offset of this PartitionReservation.
        The latest offset which has been committed for this partition.


        :return: The committed_offset of this PartitionReservation.
        :rtype: int
        """
        return self._committed_offset

    @committed_offset.setter
    def committed_offset(self, committed_offset):
        """
        Sets the committed_offset of this PartitionReservation.
        The latest offset which has been committed for this partition.


        :param committed_offset: The committed_offset of this PartitionReservation.
        :type: int
        """
        self._committed_offset = committed_offset

    @property
    def reserved_instance(self):
        """
        Gets the reserved_instance of this PartitionReservation.
        The consumer instance which currently has the partition reserved.


        :return: The reserved_instance of this PartitionReservation.
        :rtype: str
        """
        return self._reserved_instance

    @reserved_instance.setter
    def reserved_instance(self, reserved_instance):
        """
        Sets the reserved_instance of this PartitionReservation.
        The consumer instance which currently has the partition reserved.


        :param reserved_instance: The reserved_instance of this PartitionReservation.
        :type: str
        """
        self._reserved_instance = reserved_instance

    @property
    def time_reserved_until(self):
        """
        Gets the time_reserved_until of this PartitionReservation.
        A timestamp when the current reservation expires.


        :return: The time_reserved_until of this PartitionReservation.
        :rtype: datetime
        """
        return self._time_reserved_until

    @time_reserved_until.setter
    def time_reserved_until(self, time_reserved_until):
        """
        Sets the time_reserved_until of this PartitionReservation.
        A timestamp when the current reservation expires.


        :param time_reserved_until: The time_reserved_until of this PartitionReservation.
        :type: datetime
        """
        self._time_reserved_until = time_reserved_until

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
