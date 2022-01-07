# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Capacity(object):
    """
    Capacity limits for the instance pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Capacity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param max:
            The value to assign to the max property of this Capacity.
        :type max: int

        :param min:
            The value to assign to the min property of this Capacity.
        :type min: int

        :param initial:
            The value to assign to the initial property of this Capacity.
        :type initial: int

        """
        self.swagger_types = {
            'max': 'int',
            'min': 'int',
            'initial': 'int'
        }

        self.attribute_map = {
            'max': 'max',
            'min': 'min',
            'initial': 'initial'
        }

        self._max = None
        self._min = None
        self._initial = None

    @property
    def max(self):
        """
        Gets the max of this Capacity.
        For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed
        to increase to (scale out).

        For a schedule-based autoscaling policy, this value is not used.


        :return: The max of this Capacity.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this Capacity.
        For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed
        to increase to (scale out).

        For a schedule-based autoscaling policy, this value is not used.


        :param max: The max of this Capacity.
        :type: int
        """
        self._max = max

    @property
    def min(self):
        """
        Gets the min of this Capacity.
        For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed
        to decrease to (scale in).

        For a schedule-based autoscaling policy, this value is not used.


        :return: The min of this Capacity.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this Capacity.
        For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed
        to decrease to (scale in).

        For a schedule-based autoscaling policy, this value is not used.


        :param min: The min of this Capacity.
        :type: int
        """
        self._min = min

    @property
    def initial(self):
        """
        Gets the initial of this Capacity.
        For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool
        immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of
        instances is automatically adjusted from this initial number to a number that is based on the limits that
        you set.

        For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule
        that's defined in the autoscaling policy.


        :return: The initial of this Capacity.
        :rtype: int
        """
        return self._initial

    @initial.setter
    def initial(self, initial):
        """
        Sets the initial of this Capacity.
        For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool
        immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of
        instances is automatically adjusted from this initial number to a number that is based on the limits that
        you set.

        For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule
        that's defined in the autoscaling policy.


        :param initial: The initial of this Capacity.
        :type: int
        """
        self._initial = initial

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
