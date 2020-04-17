# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeOcpuOptions(object):
    """
    The possible configurations for the number of OCPUs available to an instance of this shape.
    If this field is null, then all instances of this shape have a fixed
    number of OCPUs equal to `ocpus`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeOcpuOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param min:
            The value to assign to the min property of this ShapeOcpuOptions.
        :type min: float

        :param max:
            The value to assign to the max property of this ShapeOcpuOptions.
        :type max: float

        """
        self.swagger_types = {
            'min': 'float',
            'max': 'float'
        }

        self.attribute_map = {
            'min': 'min',
            'max': 'max'
        }

        self._min = None
        self._max = None

    @property
    def min(self):
        """
        Gets the min of this ShapeOcpuOptions.
        The minimum number of OCPUs.


        :return: The min of this ShapeOcpuOptions.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this ShapeOcpuOptions.
        The minimum number of OCPUs.


        :param min: The min of this ShapeOcpuOptions.
        :type: float
        """
        self._min = min

    @property
    def max(self):
        """
        Gets the max of this ShapeOcpuOptions.
        The maximum number of OCPUs.


        :return: The max of this ShapeOcpuOptions.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this ShapeOcpuOptions.
        The maximum number of OCPUs.


        :param max: The max of this ShapeOcpuOptions.
        :type: float
        """
        self._max = max

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
