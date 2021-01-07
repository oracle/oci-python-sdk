# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateEndpointSettings(object):
    """
    Optional settings if the stream pool is private.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateEndpointSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subnet_id:
            The value to assign to the subnet_id property of this PrivateEndpointSettings.
        :type subnet_id: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this PrivateEndpointSettings.
        :type private_endpoint_ip: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this PrivateEndpointSettings.
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
        Gets the subnet_id of this PrivateEndpointSettings.
        The subnet id from which the private stream pool can be accessed.
        Trying to access the streams from another network location will result in an error.


        :return: The subnet_id of this PrivateEndpointSettings.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this PrivateEndpointSettings.
        The subnet id from which the private stream pool can be accessed.
        Trying to access the streams from another network location will result in an error.


        :param subnet_id: The subnet_id of this PrivateEndpointSettings.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this PrivateEndpointSettings.
        The private IP associated with the stream pool in the associated subnetId.
        The stream pool's FQDN resolves to that IP and should be used - instead of the private IP - in order to not trigger any TLS issues.


        :return: The private_endpoint_ip of this PrivateEndpointSettings.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this PrivateEndpointSettings.
        The private IP associated with the stream pool in the associated subnetId.
        The stream pool's FQDN resolves to that IP and should be used - instead of the private IP - in order to not trigger any TLS issues.


        :param private_endpoint_ip: The private_endpoint_ip of this PrivateEndpointSettings.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this PrivateEndpointSettings.
        The optional list of network security groups that are associated with the private endpoint of the stream pool.


        :return: The nsg_ids of this PrivateEndpointSettings.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this PrivateEndpointSettings.
        The optional list of network security groups that are associated with the private endpoint of the stream pool.


        :param nsg_ids: The nsg_ids of this PrivateEndpointSettings.
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
