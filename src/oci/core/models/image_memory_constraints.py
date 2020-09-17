# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageMemoryConstraints(object):
    """
    OCPU options for an image and shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageMemoryConstraints object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param min_in_g_bs:
            The value to assign to the min_in_g_bs property of this ImageMemoryConstraints.
        :type min_in_g_bs: int

        :param max_in_g_bs:
            The value to assign to the max_in_g_bs property of this ImageMemoryConstraints.
        :type max_in_g_bs: int

        """
        self.swagger_types = {
            'min_in_g_bs': 'int',
            'max_in_g_bs': 'int'
        }

        self.attribute_map = {
            'min_in_g_bs': 'minInGBs',
            'max_in_g_bs': 'maxInGBs'
        }

        self._min_in_g_bs = None
        self._max_in_g_bs = None

    @property
    def min_in_g_bs(self):
        """
        Gets the min_in_g_bs of this ImageMemoryConstraints.
        The minimum amount of memory supported for this image and shape, in gigabytes.


        :return: The min_in_g_bs of this ImageMemoryConstraints.
        :rtype: int
        """
        return self._min_in_g_bs

    @min_in_g_bs.setter
    def min_in_g_bs(self, min_in_g_bs):
        """
        Sets the min_in_g_bs of this ImageMemoryConstraints.
        The minimum amount of memory supported for this image and shape, in gigabytes.


        :param min_in_g_bs: The min_in_g_bs of this ImageMemoryConstraints.
        :type: int
        """
        self._min_in_g_bs = min_in_g_bs

    @property
    def max_in_g_bs(self):
        """
        Gets the max_in_g_bs of this ImageMemoryConstraints.
        The maximum amount of memory supported for this image and shape, in gigabytes.


        :return: The max_in_g_bs of this ImageMemoryConstraints.
        :rtype: int
        """
        return self._max_in_g_bs

    @max_in_g_bs.setter
    def max_in_g_bs(self, max_in_g_bs):
        """
        Sets the max_in_g_bs of this ImageMemoryConstraints.
        The maximum amount of memory supported for this image and shape, in gigabytes.


        :param max_in_g_bs: The max_in_g_bs of this ImageMemoryConstraints.
        :type: int
        """
        self._max_in_g_bs = max_in_g_bs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
