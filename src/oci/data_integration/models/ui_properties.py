# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UIProperties(object):
    """
    The UI properties of the object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UIProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param coordinate_x:
            The value to assign to the coordinate_x property of this UIProperties.
        :type coordinate_x: float

        :param coordinate_y:
            The value to assign to the coordinate_y property of this UIProperties.
        :type coordinate_y: float

        """
        self.swagger_types = {
            'coordinate_x': 'float',
            'coordinate_y': 'float'
        }

        self.attribute_map = {
            'coordinate_x': 'coordinateX',
            'coordinate_y': 'coordinateY'
        }

        self._coordinate_x = None
        self._coordinate_y = None

    @property
    def coordinate_x(self):
        """
        Gets the coordinate_x of this UIProperties.
        The X coordinate of the object.


        :return: The coordinate_x of this UIProperties.
        :rtype: float
        """
        return self._coordinate_x

    @coordinate_x.setter
    def coordinate_x(self, coordinate_x):
        """
        Sets the coordinate_x of this UIProperties.
        The X coordinate of the object.


        :param coordinate_x: The coordinate_x of this UIProperties.
        :type: float
        """
        self._coordinate_x = coordinate_x

    @property
    def coordinate_y(self):
        """
        Gets the coordinate_y of this UIProperties.
        The Y coordinate of the object.


        :return: The coordinate_y of this UIProperties.
        :rtype: float
        """
        return self._coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, coordinate_y):
        """
        Sets the coordinate_y of this UIProperties.
        The Y coordinate of the object.


        :param coordinate_y: The coordinate_y of this UIProperties.
        :type: float
        """
        self._coordinate_y = coordinate_y

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
