# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateEndpointDetails(object):
    """
    Optional parameters if a private stream pool is requested.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subnet_id:
            The value to assign to the subnet_id property of this PrivateEndpointDetails.
        :type subnet_id: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this PrivateEndpointDetails.
        :type private_endpoint_ip: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this PrivateEndpointDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'subnet_id': 'str',
            'private_endpoint_ip': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'subnet_id': 'subnetId',
            'private_endpoint_ip': 'privateEndpointIp',
            'nsg_ids': 'nsgIds'
        }

        self._subnet_id = None
        self._private_endpoint_ip = None
        self._nsg_ids = None

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this PrivateEndpointDetails.
        If specified, the stream pool will be private and only accessible from inside that subnet.
        Producing-to and consuming-from a stream inside a private stream pool can also only be done from inside the subnet.
        That value cannot be changed.


        :return: The subnet_id of this PrivateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this PrivateEndpointDetails.
        If specified, the stream pool will be private and only accessible from inside that subnet.
        Producing-to and consuming-from a stream inside a private stream pool can also only be done from inside the subnet.
        That value cannot be changed.


        :param subnet_id: The subnet_id of this PrivateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this PrivateEndpointDetails.
        The optional private IP you want to be associated with your private stream pool.
        That parameter can only be specified when the subnetId parameter is set. It cannot be changed.
        The private IP needs to be part of the CIDR range of the specified subnetId or the creation will fail.
        If not specified a random IP inside the subnet will be chosen.
        After the stream pool is created, a custom FQDN, pointing to this private IP, is created.
        The FQDN is then used to access the service instead of the private IP.


        :return: The private_endpoint_ip of this PrivateEndpointDetails.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this PrivateEndpointDetails.
        The optional private IP you want to be associated with your private stream pool.
        That parameter can only be specified when the subnetId parameter is set. It cannot be changed.
        The private IP needs to be part of the CIDR range of the specified subnetId or the creation will fail.
        If not specified a random IP inside the subnet will be chosen.
        After the stream pool is created, a custom FQDN, pointing to this private IP, is created.
        The FQDN is then used to access the service instead of the private IP.


        :param private_endpoint_ip: The private_endpoint_ip of this PrivateEndpointDetails.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this PrivateEndpointDetails.
        The optional list of network security groups to be used with the private endpoint of the stream pool.
        That value cannot be changed.


        :return: The nsg_ids of this PrivateEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this PrivateEndpointDetails.
        The optional list of network security groups to be used with the private endpoint of the stream pool.
        That value cannot be changed.


        :param nsg_ids: The nsg_ids of this PrivateEndpointDetails.
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
