# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Nic(object):
    """
    The VNIC configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Nic object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this Nic.
        :type label: str

        :param switch_name:
            The value to assign to the switch_name property of this Nic.
        :type switch_name: str

        :param mac_address:
            The value to assign to the mac_address property of this Nic.
        :type mac_address: str

        :param mac_address_type:
            The value to assign to the mac_address_type property of this Nic.
        :type mac_address_type: str

        :param network_name:
            The value to assign to the network_name property of this Nic.
        :type network_name: str

        :param ip_addresses:
            The value to assign to the ip_addresses property of this Nic.
        :type ip_addresses: list[str]

        """
        self.swagger_types = {
            'label': 'str',
            'switch_name': 'str',
            'mac_address': 'str',
            'mac_address_type': 'str',
            'network_name': 'str',
            'ip_addresses': 'list[str]'
        }

        self.attribute_map = {
            'label': 'label',
            'switch_name': 'switchName',
            'mac_address': 'macAddress',
            'mac_address_type': 'macAddressType',
            'network_name': 'networkName',
            'ip_addresses': 'ipAddresses'
        }

        self._label = None
        self._switch_name = None
        self._mac_address = None
        self._mac_address_type = None
        self._network_name = None
        self._ip_addresses = None

    @property
    def label(self):
        """
        Gets the label of this Nic.
        Provides a label and summary information for the device.


        :return: The label of this Nic.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Nic.
        Provides a label and summary information for the device.


        :param label: The label of this Nic.
        :type: str
        """
        self._label = label

    @property
    def switch_name(self):
        """
        Gets the switch_name of this Nic.
        Switch name.


        :return: The switch_name of this Nic.
        :rtype: str
        """
        return self._switch_name

    @switch_name.setter
    def switch_name(self, switch_name):
        """
        Sets the switch_name of this Nic.
        Switch name.


        :param switch_name: The switch_name of this Nic.
        :type: str
        """
        self._switch_name = switch_name

    @property
    def mac_address(self):
        """
        Gets the mac_address of this Nic.
        Mac address of the VM.


        :return: The mac_address of this Nic.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this Nic.
        Mac address of the VM.


        :param mac_address: The mac_address of this Nic.
        :type: str
        """
        self._mac_address = mac_address

    @property
    def mac_address_type(self):
        """
        Gets the mac_address_type of this Nic.
        Mac address type.


        :return: The mac_address_type of this Nic.
        :rtype: str
        """
        return self._mac_address_type

    @mac_address_type.setter
    def mac_address_type(self, mac_address_type):
        """
        Sets the mac_address_type of this Nic.
        Mac address type.


        :param mac_address_type: The mac_address_type of this Nic.
        :type: str
        """
        self._mac_address_type = mac_address_type

    @property
    def network_name(self):
        """
        Gets the network_name of this Nic.
        Network name.


        :return: The network_name of this Nic.
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        """
        Sets the network_name of this Nic.
        Network name.


        :param network_name: The network_name of this Nic.
        :type: str
        """
        self._network_name = network_name

    @property
    def ip_addresses(self):
        """
        Gets the ip_addresses of this Nic.
        List of IP addresses.


        :return: The ip_addresses of this Nic.
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this Nic.
        List of IP addresses.


        :param ip_addresses: The ip_addresses of this Nic.
        :type: list[str]
        """
        self._ip_addresses = ip_addresses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
