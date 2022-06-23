# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .endpoint import Endpoint
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VlanEndpoint(Endpoint):
    """
    Defines the details required for a VLAN-type `Endpoint`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VlanEndpoint object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.VlanEndpoint.type` attribute
        of this class is ``VLAN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VlanEndpoint.
            Allowed values for this property are: "IP_ADDRESS", "SUBNET", "COMPUTE_INSTANCE", "VNIC", "LOAD_BALANCER", "LOAD_BALANCER_LISTENER", "NETWORK_LOAD_BALANCER", "NETWORK_LOAD_BALANCER_LISTENER", "VLAN"
        :type type: str

        :param address:
            The value to assign to the address property of this VlanEndpoint.
        :type address: str

        :param vlan_id:
            The value to assign to the vlan_id property of this VlanEndpoint.
        :type vlan_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'address': 'str',
            'vlan_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'address': 'address',
            'vlan_id': 'vlanId'
        }

        self._type = None
        self._address = None
        self._vlan_id = None
        self._type = 'VLAN'

    @property
    def address(self):
        """
        **[Required]** Gets the address of this VlanEndpoint.
        The IPv4 address of the `Endpoint`.


        :return: The address of this VlanEndpoint.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this VlanEndpoint.
        The IPv4 address of the `Endpoint`.


        :param address: The address of this VlanEndpoint.
        :type: str
        """
        self._address = address

    @property
    def vlan_id(self):
        """
        **[Required]** Gets the vlan_id of this VlanEndpoint.
        The `OCID`__ of the VLAN containing the IP address.
        This can be used to disambiguate which VLAN is queried, in case the endpoint IP
        address belongs to more than one VLAN (when there are VLANs with overlapping IP ranges).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vlan_id of this VlanEndpoint.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """
        Sets the vlan_id of this VlanEndpoint.
        The `OCID`__ of the VLAN containing the IP address.
        This can be used to disambiguate which VLAN is queried, in case the endpoint IP
        address belongs to more than one VLAN (when there are VLANs with overlapping IP ranges).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vlan_id: The vlan_id of this VlanEndpoint.
        :type: str
        """
        self._vlan_id = vlan_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
