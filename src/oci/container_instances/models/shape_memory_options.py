# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeMemoryOptions(object):
    """
    For a flexible shape, the amount of memory available for instances that use this shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeMemoryOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param min_in_gbs:
            The value to assign to the min_in_gbs property of this ShapeMemoryOptions.
        :type min_in_gbs: float

        :param max_in_gbs:
            The value to assign to the max_in_gbs property of this ShapeMemoryOptions.
        :type max_in_gbs: float

        :param default_per_ocpu_in_gbs:
            The value to assign to the default_per_ocpu_in_gbs property of this ShapeMemoryOptions.
        :type default_per_ocpu_in_gbs: float

        :param min_per_ocpu_in_gbs:
            The value to assign to the min_per_ocpu_in_gbs property of this ShapeMemoryOptions.
        :type min_per_ocpu_in_gbs: float

        :param max_per_ocpu_in_gbs:
            The value to assign to the max_per_ocpu_in_gbs property of this ShapeMemoryOptions.
        :type max_per_ocpu_in_gbs: float

        """
        self.swagger_types = {
            'min_in_gbs': 'float',
            'max_in_gbs': 'float',
            'default_per_ocpu_in_gbs': 'float',
            'min_per_ocpu_in_gbs': 'float',
            'max_per_ocpu_in_gbs': 'float'
        }

        self.attribute_map = {
            'min_in_gbs': 'minInGBs',
            'max_in_gbs': 'maxInGBs',
            'default_per_ocpu_in_gbs': 'defaultPerOcpuInGBs',
            'min_per_ocpu_in_gbs': 'minPerOcpuInGBs',
            'max_per_ocpu_in_gbs': 'maxPerOcpuInGBs'
        }

        self._min_in_gbs = None
        self._max_in_gbs = None
        self._default_per_ocpu_in_gbs = None
        self._min_per_ocpu_in_gbs = None
        self._max_per_ocpu_in_gbs = None

    @property
    def min_in_gbs(self):
        """
        **[Required]** Gets the min_in_gbs of this ShapeMemoryOptions.
        The minimum amount of memory, in gigabytes.


        :return: The min_in_gbs of this ShapeMemoryOptions.
        :rtype: float
        """
        return self._min_in_gbs

    @min_in_gbs.setter
    def min_in_gbs(self, min_in_gbs):
        """
        Sets the min_in_gbs of this ShapeMemoryOptions.
        The minimum amount of memory, in gigabytes.


        :param min_in_gbs: The min_in_gbs of this ShapeMemoryOptions.
        :type: float
        """
        self._min_in_gbs = min_in_gbs

    @property
    def max_in_gbs(self):
        """
        **[Required]** Gets the max_in_gbs of this ShapeMemoryOptions.
        The maximum amount of memory, in gigabytes.


        :return: The max_in_gbs of this ShapeMemoryOptions.
        :rtype: float
        """
        return self._max_in_gbs

    @max_in_gbs.setter
    def max_in_gbs(self, max_in_gbs):
        """
        Sets the max_in_gbs of this ShapeMemoryOptions.
        The maximum amount of memory, in gigabytes.


        :param max_in_gbs: The max_in_gbs of this ShapeMemoryOptions.
        :type: float
        """
        self._max_in_gbs = max_in_gbs

    @property
    def default_per_ocpu_in_gbs(self):
        """
        **[Required]** Gets the default_per_ocpu_in_gbs of this ShapeMemoryOptions.
        The default amount of memory per OCPU available for this shape, in gigabytes.


        :return: The default_per_ocpu_in_gbs of this ShapeMemoryOptions.
        :rtype: float
        """
        return self._default_per_ocpu_in_gbs

    @default_per_ocpu_in_gbs.setter
    def default_per_ocpu_in_gbs(self, default_per_ocpu_in_gbs):
        """
        Sets the default_per_ocpu_in_gbs of this ShapeMemoryOptions.
        The default amount of memory per OCPU available for this shape, in gigabytes.


        :param default_per_ocpu_in_gbs: The default_per_ocpu_in_gbs of this ShapeMemoryOptions.
        :type: float
        """
        self._default_per_ocpu_in_gbs = default_per_ocpu_in_gbs

    @property
    def min_per_ocpu_in_gbs(self):
        """
        **[Required]** Gets the min_per_ocpu_in_gbs of this ShapeMemoryOptions.
        The minimum amount of memory per OCPU available for this shape, in gigabytes.


        :return: The min_per_ocpu_in_gbs of this ShapeMemoryOptions.
        :rtype: float
        """
        return self._min_per_ocpu_in_gbs

    @min_per_ocpu_in_gbs.setter
    def min_per_ocpu_in_gbs(self, min_per_ocpu_in_gbs):
        """
        Sets the min_per_ocpu_in_gbs of this ShapeMemoryOptions.
        The minimum amount of memory per OCPU available for this shape, in gigabytes.


        :param min_per_ocpu_in_gbs: The min_per_ocpu_in_gbs of this ShapeMemoryOptions.
        :type: float
        """
        self._min_per_ocpu_in_gbs = min_per_ocpu_in_gbs

    @property
    def max_per_ocpu_in_gbs(self):
        """
        **[Required]** Gets the max_per_ocpu_in_gbs of this ShapeMemoryOptions.
        The maximum amount of memory per OCPU available for this shape, in gigabytes.


        :return: The max_per_ocpu_in_gbs of this ShapeMemoryOptions.
        :rtype: float
        """
        return self._max_per_ocpu_in_gbs

    @max_per_ocpu_in_gbs.setter
    def max_per_ocpu_in_gbs(self, max_per_ocpu_in_gbs):
        """
        Sets the max_per_ocpu_in_gbs of this ShapeMemoryOptions.
        The maximum amount of memory per OCPU available for this shape, in gigabytes.


        :param max_per_ocpu_in_gbs: The max_per_ocpu_in_gbs of this ShapeMemoryOptions.
        :type: float
        """
        self._max_per_ocpu_in_gbs = max_per_ocpu_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
