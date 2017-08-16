# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CrossConnectLocation(object):

    def __init__(self):

        self.swagger_types = {
            'description': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'name': 'name'
        }

        self._description = None
        self._name = None

    @property
    def description(self):
        """
        Gets the description of this CrossConnectLocation.
        A description of the location.


        :return: The description of this CrossConnectLocation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CrossConnectLocation.
        A description of the location.


        :param description: The description of this CrossConnectLocation.
        :type: str
        """
        self._description = description

    @property
    def name(self):
        """
        Gets the name of this CrossConnectLocation.
        The name of the location.

        Example: `CyrusOne, Chandler, AZ`


        :return: The name of this CrossConnectLocation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CrossConnectLocation.
        The name of the location.

        Example: `CyrusOne, Chandler, AZ`


        :param name: The name of this CrossConnectLocation.
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
