# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyAttribute(object):
    """
    An attribute within a key, the attribute property is being deprecated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KeyAttribute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param position:
            The value to assign to the position property of this KeyAttribute.
        :type position: int

        :param shape_field:
            The value to assign to the shape_field property of this KeyAttribute.
        :type shape_field: oci.data_integration.models.ShapeField

        :param attribute:
            The value to assign to the attribute property of this KeyAttribute.
        :type attribute: oci.data_integration.models.ShapeField

        """
        self.swagger_types = {
            'position': 'int',
            'shape_field': 'ShapeField',
            'attribute': 'ShapeField'
        }

        self.attribute_map = {
            'position': 'position',
            'shape_field': 'shapeField',
            'attribute': 'attribute'
        }

        self._position = None
        self._shape_field = None
        self._attribute = None

    @property
    def position(self):
        """
        Gets the position of this KeyAttribute.
        The position of the attribute.


        :return: The position of this KeyAttribute.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this KeyAttribute.
        The position of the attribute.


        :param position: The position of this KeyAttribute.
        :type: int
        """
        self._position = position

    @property
    def shape_field(self):
        """
        Gets the shape_field of this KeyAttribute.

        :return: The shape_field of this KeyAttribute.
        :rtype: oci.data_integration.models.ShapeField
        """
        return self._shape_field

    @shape_field.setter
    def shape_field(self, shape_field):
        """
        Sets the shape_field of this KeyAttribute.

        :param shape_field: The shape_field of this KeyAttribute.
        :type: oci.data_integration.models.ShapeField
        """
        self._shape_field = shape_field

    @property
    def attribute(self):
        """
        Gets the attribute of this KeyAttribute.

        :return: The attribute of this KeyAttribute.
        :rtype: oci.data_integration.models.ShapeField
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """
        Sets the attribute of this KeyAttribute.

        :param attribute: The attribute of this KeyAttribute.
        :type: oci.data_integration.models.ShapeField
        """
        self._attribute = attribute

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
