# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Region(object):

    def __init__(self, **kwargs):
        """
        Initializes a new Region object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Region.
        :type key: str

        :param name:
            The value to assign to the name property of this Region.
        :type name: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name'
        }

        self._key = None
        self._name = None

    @property
    def key(self):
        """
        Gets the key of this Region.
        The key of the region.

        Allowed values are:
        - `PHX`
        - `IAD`
        - `FRA`


        :return: The key of this Region.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Region.
        The key of the region.

        Allowed values are:
        - `PHX`
        - `IAD`
        - `FRA`


        :param key: The key of this Region.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this Region.
        The name of the region.

        Allowed values are:
        - `us-phoenix-1`
        - `us-ashburn-1`
        - `eu-frankfurt-1`


        :return: The name of this Region.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Region.
        The name of the region.

        Allowed values are:
        - `us-phoenix-1`
        - `us-ashburn-1`
        - `eu-frankfurt-1`


        :param name: The name of this Region.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
