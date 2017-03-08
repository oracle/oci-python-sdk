# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateCompartmentDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description'
        }

        self._compartment_id = None
        self._name = None
        self._description = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateCompartmentDetails.
        The OCID of the tenancy containing the compartment.


        :return: The compartment_id of this CreateCompartmentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCompartmentDetails.
        The OCID of the tenancy containing the compartment.


        :param compartment_id: The compartment_id of this CreateCompartmentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this CreateCompartmentDetails.
        The name you assign to the compartment during creation. The name must be unique across all compartments
        in the tenancy and cannot be changed.


        :return: The name of this CreateCompartmentDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateCompartmentDetails.
        The name you assign to the compartment during creation. The name must be unique across all compartments
        in the tenancy and cannot be changed.


        :param name: The name of this CreateCompartmentDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateCompartmentDetails.
        The description you assign to the compartment during creation. Does not have to be unique, and it's changeable.


        :return: The description of this CreateCompartmentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateCompartmentDetails.
        The description you assign to the compartment during creation. Does not have to be unique, and it's changeable.


        :param description: The description of this CreateCompartmentDetails.
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
