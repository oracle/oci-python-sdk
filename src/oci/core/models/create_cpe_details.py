# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCpeDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCpeDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCpeDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateCpeDetails.
        :type display_name: str

        :param ip_address:
            The value to assign to the ip_address property of this CreateCpeDetails.
        :type ip_address: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'ip_address': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'ip_address': 'ipAddress'
        }

        self._compartment_id = None
        self._display_name = None
        self._ip_address = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCpeDetails.
        The OCID of the compartment to contain the CPE.


        :return: The compartment_id of this CreateCpeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCpeDetails.
        The OCID of the compartment to contain the CPE.


        :param compartment_id: The compartment_id of this CreateCpeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateCpeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateCpeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCpeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateCpeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this CreateCpeDetails.
        The public IP address of the on-premises router.

        Example: `143.19.23.16`


        :return: The ip_address of this CreateCpeDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateCpeDetails.
        The public IP address of the on-premises router.

        Example: `143.19.23.16`


        :param ip_address: The ip_address of this CreateCpeDetails.
        :type: str
        """
        self._ip_address = ip_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
