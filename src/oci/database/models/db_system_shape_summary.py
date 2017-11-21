# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemShapeSummary(object):

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemShapeSummary object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param available_core_count:
            The value to assign to the available_core_count property of this DbSystemShapeSummary.
        :type available_core_count: int

        :param name:
            The value to assign to the name property of this DbSystemShapeSummary.
        :type name: str

        :param shape:
            The value to assign to the shape property of this DbSystemShapeSummary.
        :type shape: str

        """
        self.swagger_types = {
            'available_core_count': 'int',
            'name': 'str',
            'shape': 'str'
        }

        self.attribute_map = {
            'available_core_count': 'availableCoreCount',
            'name': 'name',
            'shape': 'shape'
        }

        self._available_core_count = None
        self._name = None
        self._shape = None

    @property
    def available_core_count(self):
        """
        Gets the available_core_count of this DbSystemShapeSummary.
        The maximum number of CPU cores that can be enabled on the DB System.


        :return: The available_core_count of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._available_core_count

    @available_core_count.setter
    def available_core_count(self, available_core_count):
        """
        Sets the available_core_count of this DbSystemShapeSummary.
        The maximum number of CPU cores that can be enabled on the DB System.


        :param available_core_count: The available_core_count of this DbSystemShapeSummary.
        :type: int
        """
        self._available_core_count = available_core_count

    @property
    def name(self):
        """
        Gets the name of this DbSystemShapeSummary.
        The name of the shape used for the DB System.


        :return: The name of this DbSystemShapeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DbSystemShapeSummary.
        The name of the shape used for the DB System.


        :param name: The name of this DbSystemShapeSummary.
        :type: str
        """
        self._name = name

    @property
    def shape(self):
        """
        Gets the shape of this DbSystemShapeSummary.
        Deprecated. Use `name` instead of `shape`.


        :return: The shape of this DbSystemShapeSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DbSystemShapeSummary.
        Deprecated. Use `name` instead of `shape`.


        :param shape: The shape of this DbSystemShapeSummary.
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
