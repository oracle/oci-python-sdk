# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221208


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CccInfrastructureManagementNode(object):
    """
    Information about an individual management node in a Compute Cloud@Customer infrastructure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CccInfrastructureManagementNode object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ip:
            The value to assign to the ip property of this CccInfrastructureManagementNode.
        :type ip: str

        :param hostname:
            The value to assign to the hostname property of this CccInfrastructureManagementNode.
        :type hostname: str

        """
        self.swagger_types = {
            'ip': 'str',
            'hostname': 'str'
        }
        self.attribute_map = {
            'ip': 'ip',
            'hostname': 'hostname'
        }
        self._ip = None
        self._hostname = None

    @property
    def ip(self):
        """
        Gets the ip of this CccInfrastructureManagementNode.
        Address of the management node.


        :return: The ip of this CccInfrastructureManagementNode.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this CccInfrastructureManagementNode.
        Address of the management node.


        :param ip: The ip of this CccInfrastructureManagementNode.
        :type: str
        """
        self._ip = ip

    @property
    def hostname(self):
        """
        Gets the hostname of this CccInfrastructureManagementNode.
        Hostname for interface to the management node.


        :return: The hostname of this CccInfrastructureManagementNode.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CccInfrastructureManagementNode.
        Hostname for interface to the management node.


        :param hostname: The hostname of this CccInfrastructureManagementNode.
        :type: str
        """
        self._hostname = hostname

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
