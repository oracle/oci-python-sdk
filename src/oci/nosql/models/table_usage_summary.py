# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TableUsageSummary(object):
    """
    TableUsageSummary represents a single usage record, or slice, that includes
    information about read and write throughput consumed during that period
    as well as the current information regarding storage capacity. In
    addition the count of throttling exceptions for the period is reported.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TableUsageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param seconds_in_period:
            The value to assign to the seconds_in_period property of this TableUsageSummary.
        :type seconds_in_period: int

        :param read_units:
            The value to assign to the read_units property of this TableUsageSummary.
        :type read_units: int

        :param write_units:
            The value to assign to the write_units property of this TableUsageSummary.
        :type write_units: int

        :param storage_in_g_bs:
            The value to assign to the storage_in_g_bs property of this TableUsageSummary.
        :type storage_in_g_bs: int

        :param read_throttle_count:
            The value to assign to the read_throttle_count property of this TableUsageSummary.
        :type read_throttle_count: int

        :param write_throttle_count:
            The value to assign to the write_throttle_count property of this TableUsageSummary.
        :type write_throttle_count: int

        :param storage_throttle_count:
            The value to assign to the storage_throttle_count property of this TableUsageSummary.
        :type storage_throttle_count: int

        """
        self.swagger_types = {
            'seconds_in_period': 'int',
            'read_units': 'int',
            'write_units': 'int',
            'storage_in_g_bs': 'int',
            'read_throttle_count': 'int',
            'write_throttle_count': 'int',
            'storage_throttle_count': 'int'
        }

        self.attribute_map = {
            'seconds_in_period': 'secondsInPeriod',
            'read_units': 'readUnits',
            'write_units': 'writeUnits',
            'storage_in_g_bs': 'storageInGBs',
            'read_throttle_count': 'readThrottleCount',
            'write_throttle_count': 'writeThrottleCount',
            'storage_throttle_count': 'storageThrottleCount'
        }

        self._seconds_in_period = None
        self._read_units = None
        self._write_units = None
        self._storage_in_g_bs = None
        self._read_throttle_count = None
        self._write_throttle_count = None
        self._storage_throttle_count = None

    @property
    def seconds_in_period(self):
        """
        Gets the seconds_in_period of this TableUsageSummary.
        The length of the sampling period.


        :return: The seconds_in_period of this TableUsageSummary.
        :rtype: int
        """
        return self._seconds_in_period

    @seconds_in_period.setter
    def seconds_in_period(self, seconds_in_period):
        """
        Sets the seconds_in_period of this TableUsageSummary.
        The length of the sampling period.


        :param seconds_in_period: The seconds_in_period of this TableUsageSummary.
        :type: int
        """
        self._seconds_in_period = seconds_in_period

    @property
    def read_units(self):
        """
        Gets the read_units of this TableUsageSummary.
        Read throughput during the sampling period.


        :return: The read_units of this TableUsageSummary.
        :rtype: int
        """
        return self._read_units

    @read_units.setter
    def read_units(self, read_units):
        """
        Sets the read_units of this TableUsageSummary.
        Read throughput during the sampling period.


        :param read_units: The read_units of this TableUsageSummary.
        :type: int
        """
        self._read_units = read_units

    @property
    def write_units(self):
        """
        Gets the write_units of this TableUsageSummary.
        Write throughput during the sampling period.


        :return: The write_units of this TableUsageSummary.
        :rtype: int
        """
        return self._write_units

    @write_units.setter
    def write_units(self, write_units):
        """
        Sets the write_units of this TableUsageSummary.
        Write throughput during the sampling period.


        :param write_units: The write_units of this TableUsageSummary.
        :type: int
        """
        self._write_units = write_units

    @property
    def storage_in_g_bs(self):
        """
        Gets the storage_in_g_bs of this TableUsageSummary.
        The size of the table, in GB.


        :return: The storage_in_g_bs of this TableUsageSummary.
        :rtype: int
        """
        return self._storage_in_g_bs

    @storage_in_g_bs.setter
    def storage_in_g_bs(self, storage_in_g_bs):
        """
        Sets the storage_in_g_bs of this TableUsageSummary.
        The size of the table, in GB.


        :param storage_in_g_bs: The storage_in_g_bs of this TableUsageSummary.
        :type: int
        """
        self._storage_in_g_bs = storage_in_g_bs

    @property
    def read_throttle_count(self):
        """
        Gets the read_throttle_count of this TableUsageSummary.
        The number of times reads were throttled due to exceeding
        the read throughput limit.


        :return: The read_throttle_count of this TableUsageSummary.
        :rtype: int
        """
        return self._read_throttle_count

    @read_throttle_count.setter
    def read_throttle_count(self, read_throttle_count):
        """
        Sets the read_throttle_count of this TableUsageSummary.
        The number of times reads were throttled due to exceeding
        the read throughput limit.


        :param read_throttle_count: The read_throttle_count of this TableUsageSummary.
        :type: int
        """
        self._read_throttle_count = read_throttle_count

    @property
    def write_throttle_count(self):
        """
        Gets the write_throttle_count of this TableUsageSummary.
        The number of times writes were throttled due to exceeding
        the write throughput limit.


        :return: The write_throttle_count of this TableUsageSummary.
        :rtype: int
        """
        return self._write_throttle_count

    @write_throttle_count.setter
    def write_throttle_count(self, write_throttle_count):
        """
        Sets the write_throttle_count of this TableUsageSummary.
        The number of times writes were throttled due to exceeding
        the write throughput limit.


        :param write_throttle_count: The write_throttle_count of this TableUsageSummary.
        :type: int
        """
        self._write_throttle_count = write_throttle_count

    @property
    def storage_throttle_count(self):
        """
        Gets the storage_throttle_count of this TableUsageSummary.
        The number of times writes were throttled because the table
        exceeded its size limit.


        :return: The storage_throttle_count of this TableUsageSummary.
        :rtype: int
        """
        return self._storage_throttle_count

    @storage_throttle_count.setter
    def storage_throttle_count(self, storage_throttle_count):
        """
        Sets the storage_throttle_count of this TableUsageSummary.
        The number of times writes were throttled because the table
        exceeded its size limit.


        :param storage_throttle_count: The storage_throttle_count of this TableUsageSummary.
        :type: int
        """
        self._storage_throttle_count = storage_throttle_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
