# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCompartmentDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCompartmentDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateCompartmentDetails.
        :type description: str

        :param name:
            The value to assign to the name property of this UpdateCompartmentDetails.
        :type name: str

        """
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

    @property
    def name(self):
        """
        Gets the name of this UpdateCompartmentDetails.
        The new name you assign to the compartment. The name must be unique across all compartments in the tenancy.


        :return: The name of this UpdateCompartmentDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateCompartmentDetails.
        The new name you assign to the compartment. The name must be unique across all compartments in the tenancy.


        :param name: The name of this UpdateCompartmentDetails.
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
