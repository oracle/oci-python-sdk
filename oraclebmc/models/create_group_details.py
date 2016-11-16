# coding: utf-8
# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.


from ..util import formatted_flat_dict


class CreateGroupDetails(object):

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
        Gets the compartment_id of this CreateGroupDetails.
        The OCID of the tenancy containing the group.

        :return: The compartment_id of this CreateGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateGroupDetails.
        The OCID of the tenancy containing the group.

        :param compartment_id: The compartment_id of this CreateGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this CreateGroupDetails.
        A unique, unchangeable name you assign to the group during creation. Must be unique across all groups
        in the tenancy.

        :return: The name of this CreateGroupDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateGroupDetails.
        A unique, unchangeable name you assign to the group during creation. Must be unique across all groups
        in the tenancy.

        :param name: The name of this CreateGroupDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateGroupDetails.
        The non-unique, changeable description you assign to the group during creation.

        :return: The description of this CreateGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateGroupDetails.
        The non-unique, changeable description you assign to the group during creation.

        :param description: The description of this CreateGroupDetails.
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
