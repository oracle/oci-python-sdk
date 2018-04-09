# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Shape(object):
    """
    A compute instance shape that can be used in :func:`launch_instance`.
    For more information, see `Overview of the Compute Service`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Concepts/computeoverview.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Shape object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape:
            The value to assign to the shape property of this Shape.
        :type shape: str

        """
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
        **[Required]** Gets the shape of this Shape.
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
