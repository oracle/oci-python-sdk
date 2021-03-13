# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateClusterEndpointConfigDetails(object):
    """
    The properties that define a request to update a cluster endpoint config.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateClusterEndpointConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateClusterEndpointConfigDetails.
        :type nsg_ids: list[str]

        :param is_public_ip_enabled:
            The value to assign to the is_public_ip_enabled property of this UpdateClusterEndpointConfigDetails.
        :type is_public_ip_enabled: bool

        """
        self.swagger_types = {
            'nsg_ids': 'list[str]',
            'is_public_ip_enabled': 'bool'
        }

        self.attribute_map = {
            'nsg_ids': 'nsgIds',
            'is_public_ip_enabled': 'isPublicIpEnabled'
        }

        self._nsg_ids = None
        self._is_public_ip_enabled = None

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateClusterEndpointConfigDetails.
        A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this UpdateClusterEndpointConfigDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateClusterEndpointConfigDetails.
        A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this UpdateClusterEndpointConfigDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def is_public_ip_enabled(self):
        """
        Gets the is_public_ip_enabled of this UpdateClusterEndpointConfigDetails.
        Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster update will fail.


        :return: The is_public_ip_enabled of this UpdateClusterEndpointConfigDetails.
        :rtype: bool
        """
        return self._is_public_ip_enabled

    @is_public_ip_enabled.setter
    def is_public_ip_enabled(self, is_public_ip_enabled):
        """
        Sets the is_public_ip_enabled of this UpdateClusterEndpointConfigDetails.
        Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster update will fail.


        :param is_public_ip_enabled: The is_public_ip_enabled of this UpdateClusterEndpointConfigDetails.
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
