# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Datapoint(object):
    """
    Metric value for a specific timestamp.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Datapoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this Datapoint.
        :type timestamp: datetime

        :param value:
            The value to assign to the value property of this Datapoint.
        :type value: float

        :param count:
            The value to assign to the count property of this Datapoint.
        :type count: int

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'value': 'float',
            'count': 'int'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'value': 'value',
            'count': 'count'
        }

        self._timestamp = None
        self._value = None
        self._count = None

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this Datapoint.
        Timestamp for this metric value. Format defined by RFC3339.

        Example: `2019-02-01T01:02:29.600Z`


        :return: The timestamp of this Datapoint.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Datapoint.
        Timestamp for this metric value. Format defined by RFC3339.

        Example: `2019-02-01T01:02:29.600Z`


        :param timestamp: The timestamp of this Datapoint.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Datapoint.
        Numeric value of the metric.

        Example: `10.23`


        :return: The value of this Datapoint.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Datapoint.
        Numeric value of the metric.

        Example: `10.23`


        :param value: The value of this Datapoint.
        :type: float
        """
        self._value = value

    @property
    def count(self):
        """
        Gets the count of this Datapoint.
        The number of occurrences of the associated value in the set of data.

        Default is 1. Value must be greater than zero.


        :return: The count of this Datapoint.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this Datapoint.
        The number of occurrences of the associated value in the set of data.

        Default is 1. Value must be greater than zero.


        :param count: The count of this Datapoint.
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
