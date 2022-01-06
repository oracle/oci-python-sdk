# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActivityTimeSeriesMetrics(object):
    """
    The response object representing activityMetric details for a specific database at a particular time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ActivityTimeSeriesMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this ActivityTimeSeriesMetrics.
        :type timestamp: datetime

        :param cpu_time:
            The value to assign to the cpu_time property of this ActivityTimeSeriesMetrics.
        :type cpu_time: oci.database_management.models.MetricDataPoint

        :param wait_time:
            The value to assign to the wait_time property of this ActivityTimeSeriesMetrics.
        :type wait_time: oci.database_management.models.MetricDataPoint

        :param user_io_time:
            The value to assign to the user_io_time property of this ActivityTimeSeriesMetrics.
        :type user_io_time: oci.database_management.models.MetricDataPoint

        :param cpu_count:
            The value to assign to the cpu_count property of this ActivityTimeSeriesMetrics.
        :type cpu_count: oci.database_management.models.MetricDataPoint

        :param cluster:
            The value to assign to the cluster property of this ActivityTimeSeriesMetrics.
        :type cluster: oci.database_management.models.MetricDataPoint

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'cpu_time': 'MetricDataPoint',
            'wait_time': 'MetricDataPoint',
            'user_io_time': 'MetricDataPoint',
            'cpu_count': 'MetricDataPoint',
            'cluster': 'MetricDataPoint'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'cpu_time': 'cpuTime',
            'wait_time': 'waitTime',
            'user_io_time': 'userIoTime',
            'cpu_count': 'cpuCount',
            'cluster': 'cluster'
        }

        self._timestamp = None
        self._cpu_time = None
        self._wait_time = None
        self._user_io_time = None
        self._cpu_count = None
        self._cluster = None

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ActivityTimeSeriesMetrics.
        The date and time the activity metric was created.


        :return: The timestamp of this ActivityTimeSeriesMetrics.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ActivityTimeSeriesMetrics.
        The date and time the activity metric was created.


        :param timestamp: The timestamp of this ActivityTimeSeriesMetrics.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def cpu_time(self):
        """
        Gets the cpu_time of this ActivityTimeSeriesMetrics.

        :return: The cpu_time of this ActivityTimeSeriesMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        """
        Sets the cpu_time of this ActivityTimeSeriesMetrics.

        :param cpu_time: The cpu_time of this ActivityTimeSeriesMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._cpu_time = cpu_time

    @property
    def wait_time(self):
        """
        Gets the wait_time of this ActivityTimeSeriesMetrics.

        :return: The wait_time of this ActivityTimeSeriesMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._wait_time

    @wait_time.setter
    def wait_time(self, wait_time):
        """
        Sets the wait_time of this ActivityTimeSeriesMetrics.

        :param wait_time: The wait_time of this ActivityTimeSeriesMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._wait_time = wait_time

    @property
    def user_io_time(self):
        """
        Gets the user_io_time of this ActivityTimeSeriesMetrics.

        :return: The user_io_time of this ActivityTimeSeriesMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._user_io_time

    @user_io_time.setter
    def user_io_time(self, user_io_time):
        """
        Sets the user_io_time of this ActivityTimeSeriesMetrics.

        :param user_io_time: The user_io_time of this ActivityTimeSeriesMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._user_io_time = user_io_time

    @property
    def cpu_count(self):
        """
        Gets the cpu_count of this ActivityTimeSeriesMetrics.

        :return: The cpu_count of this ActivityTimeSeriesMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """
        Sets the cpu_count of this ActivityTimeSeriesMetrics.

        :param cpu_count: The cpu_count of this ActivityTimeSeriesMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._cpu_count = cpu_count

    @property
    def cluster(self):
        """
        Gets the cluster of this ActivityTimeSeriesMetrics.

        :return: The cluster of this ActivityTimeSeriesMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """
        Sets the cluster of this ActivityTimeSeriesMetrics.

        :param cluster: The cluster of this ActivityTimeSeriesMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._cluster = cluster

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
