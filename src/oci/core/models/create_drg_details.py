# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrgDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrgDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDrgDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateDrgDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName'
        }

        self._compartment_id = None
        self._display_name = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateDrgDetails.
        The OCID of the compartment to contain the DRG.


        :return: The compartment_id of this CreateDrgDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDrgDetails.
        The OCID of the compartment to contain the DRG.


        :param compartment_id: The compartment_id of this CreateDrgDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDrgDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateDrgDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDrgDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDrgDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
