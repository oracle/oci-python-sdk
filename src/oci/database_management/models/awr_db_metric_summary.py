# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDbMetricSummary(object):
    """
    The summary of the AWR metric data for a particular metric at a specific time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDbMetricSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrDbMetricSummary.
        :type name: str

        :param timestamp:
            The value to assign to the timestamp property of this AwrDbMetricSummary.
        :type timestamp: datetime

        :param avg_value:
            The value to assign to the avg_value property of this AwrDbMetricSummary.
        :type avg_value: float

        :param min_value:
            The value to assign to the min_value property of this AwrDbMetricSummary.
        :type min_value: float

        :param max_value:
            The value to assign to the max_value property of this AwrDbMetricSummary.
        :type max_value: float

        """
        self.swagger_types = {
            'name': 'str',
            'timestamp': 'datetime',
            'avg_value': 'float',
            'min_value': 'float',
            'max_value': 'float'
        }

        self.attribute_map = {
            'name': 'name',
            'timestamp': 'timestamp',
            'avg_value': 'avgValue',
            'min_value': 'minValue',
            'max_value': 'maxValue'
        }

        self._name = None
        self._timestamp = None
        self._avg_value = None
        self._min_value = None
        self._max_value = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AwrDbMetricSummary.
        The name of the metric.


        :return: The name of this AwrDbMetricSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AwrDbMetricSummary.
        The name of the metric.


        :param name: The name of this AwrDbMetricSummary.
        :type: str
        """
        self._name = name

    @property
    def timestamp(self):
        """
        Gets the timestamp of this AwrDbMetricSummary.
        The time of the sampling.


        :return: The timestamp of this AwrDbMetricSummary.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this AwrDbMetricSummary.
        The time of the sampling.


        :param timestamp: The timestamp of this AwrDbMetricSummary.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def avg_value(self):
        """
        Gets the avg_value of this AwrDbMetricSummary.
        The average value of the sampling period.


        :return: The avg_value of this AwrDbMetricSummary.
        :rtype: float
        """
        return self._avg_value

    @avg_value.setter
    def avg_value(self, avg_value):
        """
        Sets the avg_value of this AwrDbMetricSummary.
        The average value of the sampling period.


        :param avg_value: The avg_value of this AwrDbMetricSummary.
        :type: float
        """
        self._avg_value = avg_value

    @property
    def min_value(self):
        """
        Gets the min_value of this AwrDbMetricSummary.
        The minimum value of the sampling period.


        :return: The min_value of this AwrDbMetricSummary.
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """
        Sets the min_value of this AwrDbMetricSummary.
        The minimum value of the sampling period.


        :param min_value: The min_value of this AwrDbMetricSummary.
        :type: float
        """
        self._min_value = min_value

    @property
    def max_value(self):
        """
        Gets the max_value of this AwrDbMetricSummary.
        The maximum value of the sampling period.v


        :return: The max_value of this AwrDbMetricSummary.
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """
        Sets the max_value of this AwrDbMetricSummary.
        The maximum value of the sampling period.v


        :param max_value: The max_value of this AwrDbMetricSummary.
        :type: float
        """
        self._max_value = max_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
