# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDbCpuUsageSummary(object):
    """
    A summary of the AWR CPU resource limits and metrics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDbCpuUsageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this AwrDbCpuUsageSummary.
        :type timestamp: datetime

        :param avg_value:
            The value to assign to the avg_value property of this AwrDbCpuUsageSummary.
        :type avg_value: float

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'avg_value': 'float'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'avg_value': 'avgValue'
        }

        self._timestamp = None
        self._avg_value = None

    @property
    def timestamp(self):
        """
        Gets the timestamp of this AwrDbCpuUsageSummary.
        The timestamp for the CPU summary data.


        :return: The timestamp of this AwrDbCpuUsageSummary.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this AwrDbCpuUsageSummary.
        The timestamp for the CPU summary data.


        :param timestamp: The timestamp of this AwrDbCpuUsageSummary.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def avg_value(self):
        """
        Gets the avg_value of this AwrDbCpuUsageSummary.
        The average CPU usage per second.


        :return: The avg_value of this AwrDbCpuUsageSummary.
        :rtype: float
        """
        return self._avg_value

    @avg_value.setter
    def avg_value(self, avg_value):
        """
        Sets the avg_value of this AwrDbCpuUsageSummary.
        The average CPU usage per second.


        :param avg_value: The avg_value of this AwrDbCpuUsageSummary.
        :type: float
        """
        self._avg_value = avg_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
