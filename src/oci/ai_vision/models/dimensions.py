# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Dimensions(object):
    """
    Width and height of a page.
    """

    #: A constant which can be used with the unit property of a Dimensions.
    #: This constant has a value of "PIXEL"
    UNIT_PIXEL = "PIXEL"

    #: A constant which can be used with the unit property of a Dimensions.
    #: This constant has a value of "INCH"
    UNIT_INCH = "INCH"

    def __init__(self, **kwargs):
        """
        Initializes a new Dimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param width:
            The value to assign to the width property of this Dimensions.
        :type width: float

        :param height:
            The value to assign to the height property of this Dimensions.
        :type height: float

        :param unit:
            The value to assign to the unit property of this Dimensions.
            Allowed values for this property are: "PIXEL", "INCH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit: str

        """
        self.swagger_types = {
            'width': 'float',
            'height': 'float',
            'unit': 'str'
        }

        self.attribute_map = {
            'width': 'width',
            'height': 'height',
            'unit': 'unit'
        }

        self._width = None
        self._height = None
        self._unit = None

    @property
    def width(self):
        """
        **[Required]** Gets the width of this Dimensions.
        Width of a page.


        :return: The width of this Dimensions.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this Dimensions.
        Width of a page.


        :param width: The width of this Dimensions.
        :type: float
        """
        self._width = width

    @property
    def height(self):
        """
        **[Required]** Gets the height of this Dimensions.
        Height of a page.


        :return: The height of this Dimensions.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this Dimensions.
        Height of a page.


        :param height: The height of this Dimensions.
        :type: float
        """
        self._height = height

    @property
    def unit(self):
        """
        **[Required]** Gets the unit of this Dimensions.
        Unit of length.

        Allowed values for this property are: "PIXEL", "INCH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit of this Dimensions.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this Dimensions.
        Unit of length.


        :param unit: The unit of this Dimensions.
        :type: str
        """
        allowed_values = ["PIXEL", "INCH"]
        if not value_allowed_none_or_none_sentinel(unit, allowed_values):
            unit = 'UNKNOWN_ENUM_VALUE'
        self._unit = unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
