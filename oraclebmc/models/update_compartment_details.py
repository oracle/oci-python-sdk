# coding: utf-8
# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.


from ..util import formatted_flat_dict


class UpdateCompartmentDetails(object):

    def __init__(self):

        self.swagger_types = {
            'description': 'str'
        }

        self.attribute_map = {
            'description': 'description'
        }

        self._description = None

    @property
    def description(self):
        """
        Gets the description of this UpdateCompartmentDetails.
        The description you assign to the compartment. Does not have to be unique, and it's changeable.

        :return: The description of this UpdateCompartmentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCompartmentDetails.
        The description you assign to the compartment. Does not have to be unique, and it's changeable.

        :param description: The description of this UpdateCompartmentDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
