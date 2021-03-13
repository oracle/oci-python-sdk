# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateClusterEndpointConfigDetails(object):
    """
    The properties that define the network configuration for the Cluster endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateClusterEndpointConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateClusterEndpointConfigDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateClusterEndpointConfigDetails.
        :type nsg_ids: list[str]

        :param is_public_ip_enabled:
            The value to assign to the is_public_ip_enabled property of this CreateClusterEndpointConfigDetails.
        :type is_public_ip_enabled: bool

        """
        self.swagger_types = {
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'is_public_ip_enabled': 'bool'
        }

        self.attribute_map = {
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'is_public_ip_enabled': 'isPublicIpEnabled'
        }

        self._subnet_id = None
        self._nsg_ids = None
        self._is_public_ip_enabled = None

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this CreateClusterEndpointConfigDetails.
        The OCID of the regional subnet in which to place the Cluster endpoint.


        :return: The subnet_id of this CreateClusterEndpointConfigDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateClusterEndpointConfigDetails.
        The OCID of the regional subnet in which to place the Cluster endpoint.


        :param subnet_id: The subnet_id of this CreateClusterEndpointConfigDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateClusterEndpointConfigDetails.
        A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this CreateClusterEndpointConfigDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateClusterEndpointConfigDetails.
        A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this CreateClusterEndpointConfigDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def is_public_ip_enabled(self):
        """
        Gets the is_public_ip_enabled of this CreateClusterEndpointConfigDetails.
        Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster provisioning will fail.


        :return: The is_public_ip_enabled of this CreateClusterEndpointConfigDetails.
        :rtype: bool
        """
        return self._is_public_ip_enabled

    @is_public_ip_enabled.setter
    def is_public_ip_enabled(self, is_public_ip_enabled):
        """
        Sets the is_public_ip_enabled of this CreateClusterEndpointConfigDetails.
        Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster provisioning will fail.


        :param is_public_ip_enabled: The is_public_ip_enabled of this CreateClusterEndpointConfigDetails.
        :type: bool
        """
        self._is_public_ip_enabled = is_public_ip_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
