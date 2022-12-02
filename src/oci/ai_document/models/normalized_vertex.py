# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NormalizedVertex(object):
    """
    An (x, y) coordinate in the image with dimensions normalized from zero to one.
    The origin is at top left, with the positive x-axis pointing right and the positive y-axis pointing down.
    The bottom right corner is at (1, 1).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NormalizedVertex object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param x:
            The value to assign to the x property of this NormalizedVertex.
        :type x: float

        :param y:
            The value to assign to the y property of this NormalizedVertex.
        :type y: float

        """
        self.swagger_types = {
            'x': 'float',
            'y': 'float'
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y'
        }

        self._x = None
        self._y = None

    @property
    def x(self):
        """
        **[Required]** Gets the x of this NormalizedVertex.
        The X-axis normalized coordinate.


        :return: The x of this NormalizedVertex.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x of this NormalizedVertex.
        The X-axis normalized coordinate.


        :param x: The x of this NormalizedVertex.
        :type: float
        """
        self._x = x

    @property
    def y(self):
        """
        **[Required]** Gets the y of this NormalizedVertex.
        The Y-axis normalized coordinate.


        :return: The y of this NormalizedVertex.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y of this NormalizedVertex.
        The Y-axis normalized coordinate.


        :param y: The y of this NormalizedVertex.
        :type: float
        """
        self._y = y

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
