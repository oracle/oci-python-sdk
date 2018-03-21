# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRemotePeeringConnectionDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRemotePeeringConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRemotePeeringConnectionDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateRemotePeeringConnectionDetails.
        :type display_name: str

        :param drg_id:
            The value to assign to the drg_id property of this CreateRemotePeeringConnectionDetails.
        :type drg_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'drg_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'drg_id': 'drgId'
        }

        self._compartment_id = None
        self._display_name = None
        self._drg_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRemotePeeringConnectionDetails.
        The OCID of the compartment to contain the RPC.


        :return: The compartment_id of this CreateRemotePeeringConnectionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRemotePeeringConnectionDetails.
        The OCID of the compartment to contain the RPC.


        :param compartment_id: The compartment_id of this CreateRemotePeeringConnectionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateRemotePeeringConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateRemotePeeringConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRemotePeeringConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateRemotePeeringConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this CreateRemotePeeringConnectionDetails.
        The OCID of the DRG the RPC belongs to.


        :return: The drg_id of this CreateRemotePeeringConnectionDetails.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this CreateRemotePeeringConnectionDetails.
        The OCID of the DRG the RPC belongs to.


        :param drg_id: The drg_id of this CreateRemotePeeringConnectionDetails.
        :type: str
        """
        self._drg_id = drg_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
