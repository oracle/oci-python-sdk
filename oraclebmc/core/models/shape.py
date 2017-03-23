# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class Shape(object):

    def __init__(self):

        self.swagger_types = {
            'shape': 'str'
        }

        self.attribute_map = {
            'shape': 'shape'
        }

        self._shape = None

    @property
    def shape(self):
        """
        Gets the shape of this Shape.
        The name of the shape. You can enumerate all available shapes by calling
        :func:`list_shapes`.


        :return: The shape of this Shape.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this Shape.
        The name of the shape. You can enumerate all available shapes by calling
        :func:`list_shapes`.


        :param shape: The shape of this Shape.
        :type: str
        """
        self._shape = shape

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
