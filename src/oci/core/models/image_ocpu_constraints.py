# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageOcpuConstraints(object):
    """
    OCPU options for an image and shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageOcpuConstraints object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param min:
            The value to assign to the min property of this ImageOcpuConstraints.
        :type min: int

        :param max:
            The value to assign to the max property of this ImageOcpuConstraints.
        :type max: int

        """
        self.swagger_types = {
            'min': 'int',
            'max': 'int'
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
        Gets the min of this ImageOcpuConstraints.
        The minimum number of OCPUs supported for this image and shape.


        :return: The min of this ImageOcpuConstraints.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this ImageOcpuConstraints.
        The minimum number of OCPUs supported for this image and shape.


        :param min: The min of this ImageOcpuConstraints.
        :type: int
        """
        self._min = min

    @property
    def max(self):
        """
        Gets the max of this ImageOcpuConstraints.
        The maximum number of OCPUs supported for this image and shape.


        :return: The max of this ImageOcpuConstraints.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this ImageOcpuConstraints.
        The maximum number of OCPUs supported for this image and shape.


        :param max: The max of this ImageOcpuConstraints.
        :type: int
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
