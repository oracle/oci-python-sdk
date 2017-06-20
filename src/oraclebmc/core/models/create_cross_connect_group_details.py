# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateCrossConnectGroupDetails(object):

    def __init__(self):

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
        Gets the compartment_id of this CreateCrossConnectGroupDetails.
        The OCID of the compartment to contain the cross-connect group.


        :return: The compartment_id of this CreateCrossConnectGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCrossConnectGroupDetails.
        The OCID of the compartment to contain the cross-connect group.


        :param compartment_id: The compartment_id of this CreateCrossConnectGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateCrossConnectGroupDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CreateCrossConnectGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCrossConnectGroupDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateCrossConnectGroupDetails.
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
