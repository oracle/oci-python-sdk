# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponderExecutionTrendAggregation(object):
    """
    Provides the timestamps and their corresponding number of remediations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResponderExecutionTrendAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimensions_map:
            The value to assign to the dimensions_map property of this ResponderExecutionTrendAggregation.
        :type dimensions_map: dict(str, str)

        :param start_timestamp:
            The value to assign to the start_timestamp property of this ResponderExecutionTrendAggregation.
        :type start_timestamp: float

        :param duration_in_seconds:
            The value to assign to the duration_in_seconds property of this ResponderExecutionTrendAggregation.
        :type duration_in_seconds: int

        :param count:
            The value to assign to the count property of this ResponderExecutionTrendAggregation.
        :type count: int

        """
        self.swagger_types = {
            'dimensions_map': 'dict(str, str)',
            'start_timestamp': 'float',
            'duration_in_seconds': 'int',
            'count': 'int'
        }

        self.attribute_map = {
            'dimensions_map': 'dimensionsMap',
            'start_timestamp': 'startTimestamp',
            'duration_in_seconds': 'durationInSeconds',
            'count': 'count'
        }

        self._dimensions_map = None
        self._start_timestamp = None
        self._duration_in_seconds = None
        self._count = None

    @property
    def dimensions_map(self):
        """
        **[Required]** Gets the dimensions_map of this ResponderExecutionTrendAggregation.
        The key-value pairs of dimensions and their names.


        :return: The dimensions_map of this ResponderExecutionTrendAggregation.
        :rtype: dict(str, str)
        """
        return self._dimensions_map

    @dimensions_map.setter
    def dimensions_map(self, dimensions_map):
        """
        Sets the dimensions_map of this ResponderExecutionTrendAggregation.
        The key-value pairs of dimensions and their names.


        :param dimensions_map: The dimensions_map of this ResponderExecutionTrendAggregation.
        :type: dict(str, str)
        """
        self._dimensions_map = dimensions_map

    @property
    def start_timestamp(self):
        """
        **[Required]** Gets the start_timestamp of this ResponderExecutionTrendAggregation.
        Start Time in epoch seconds


        :return: The start_timestamp of this ResponderExecutionTrendAggregation.
        :rtype: float
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """
        Sets the start_timestamp of this ResponderExecutionTrendAggregation.
        Start Time in epoch seconds


        :param start_timestamp: The start_timestamp of this ResponderExecutionTrendAggregation.
        :type: float
        """
        self._start_timestamp = start_timestamp

    @property
    def duration_in_seconds(self):
        """
        **[Required]** Gets the duration_in_seconds of this ResponderExecutionTrendAggregation.
        Duration


        :return: The duration_in_seconds of this ResponderExecutionTrendAggregation.
        :rtype: int
        """
        return self._duration_in_seconds

    @duration_in_seconds.setter
    def duration_in_seconds(self, duration_in_seconds):
        """
        Sets the duration_in_seconds of this ResponderExecutionTrendAggregation.
        Duration


        :param duration_in_seconds: The duration_in_seconds of this ResponderExecutionTrendAggregation.
        :type: int
        """
        self._duration_in_seconds = duration_in_seconds

    @property
    def count(self):
        """
        **[Required]** Gets the count of this ResponderExecutionTrendAggregation.
        The number of remediations for a given time.


        :return: The count of this ResponderExecutionTrendAggregation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this ResponderExecutionTrendAggregation.
        The number of remediations for a given time.


        :param count: The count of this ResponderExecutionTrendAggregation.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
