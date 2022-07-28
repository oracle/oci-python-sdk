# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .network_channel import NetworkChannel
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceVnicChannel(NetworkChannel):
    """
    Specifies the configuration to access private resources in customer tenancy using service managed VNIC.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceVnicChannel object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ServiceVnicChannel.network_channel_type` attribute
        of this class is ``SERVICE_VNIC_CHANNEL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_channel_type:
            The value to assign to the network_channel_type property of this ServiceVnicChannel.
            Allowed values for this property are: "PRIVATE_ENDPOINT_CHANNEL", "SERVICE_VNIC_CHANNEL"
        :type network_channel_type: str

        :param subnet_id:
            The value to assign to the subnet_id property of this ServiceVnicChannel.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this ServiceVnicChannel.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'network_channel_type': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'network_channel_type': 'networkChannelType',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds'
        }

        self._network_channel_type = None
        self._subnet_id = None
        self._nsg_ids = None
        self._network_channel_type = 'SERVICE_VNIC_CHANNEL'

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this ServiceVnicChannel.
        The OCID of the subnet where private resources exist.


        :return: The subnet_id of this ServiceVnicChannel.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this ServiceVnicChannel.
        The OCID of the subnet where private resources exist.


        :param subnet_id: The subnet_id of this ServiceVnicChannel.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this ServiceVnicChannel.
        An array of network security group OCIDs.


        :return: The nsg_ids of this ServiceVnicChannel.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this ServiceVnicChannel.
        An array of network security group OCIDs.


        :param nsg_ids: The nsg_ids of this ServiceVnicChannel.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
