# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220509


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceNetworkInterface(object):
    """
    Describes a network interface.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceNetworkInterface object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param association:
            The value to assign to the association property of this InstanceNetworkInterface.
        :type association: oci.cloud_bridge.models.InstanceNetworkInterfaceAssociation

        :param attachment:
            The value to assign to the attachment property of this InstanceNetworkInterface.
        :type attachment: oci.cloud_bridge.models.InstanceNetworkInterfaceAttachment

        :param description:
            The value to assign to the description property of this InstanceNetworkInterface.
        :type description: str

        :param security_groups:
            The value to assign to the security_groups property of this InstanceNetworkInterface.
        :type security_groups: list[oci.cloud_bridge.models.GroupIdentifier]

        :param interface_type:
            The value to assign to the interface_type property of this InstanceNetworkInterface.
        :type interface_type: str

        :param ipv4_prefixes:
            The value to assign to the ipv4_prefixes property of this InstanceNetworkInterface.
        :type ipv4_prefixes: list[str]

        :param ipv6_addresses:
            The value to assign to the ipv6_addresses property of this InstanceNetworkInterface.
        :type ipv6_addresses: list[str]

        :param ipv6_prefixes:
            The value to assign to the ipv6_prefixes property of this InstanceNetworkInterface.
        :type ipv6_prefixes: list[str]

        :param mac_address:
            The value to assign to the mac_address property of this InstanceNetworkInterface.
        :type mac_address: str

        :param network_interface_key:
            The value to assign to the network_interface_key property of this InstanceNetworkInterface.
        :type network_interface_key: str

        :param owner_key:
            The value to assign to the owner_key property of this InstanceNetworkInterface.
        :type owner_key: str

        :param private_ip_addresses:
            The value to assign to the private_ip_addresses property of this InstanceNetworkInterface.
        :type private_ip_addresses: list[oci.cloud_bridge.models.InstancePrivateIpAddress]

        :param is_source_dest_check:
            The value to assign to the is_source_dest_check property of this InstanceNetworkInterface.
        :type is_source_dest_check: bool

        :param status:
            The value to assign to the status property of this InstanceNetworkInterface.
        :type status: str

        :param subnet_key:
            The value to assign to the subnet_key property of this InstanceNetworkInterface.
        :type subnet_key: str

        """
        self.swagger_types = {
            'association': 'InstanceNetworkInterfaceAssociation',
            'attachment': 'InstanceNetworkInterfaceAttachment',
            'description': 'str',
            'security_groups': 'list[GroupIdentifier]',
            'interface_type': 'str',
            'ipv4_prefixes': 'list[str]',
            'ipv6_addresses': 'list[str]',
            'ipv6_prefixes': 'list[str]',
            'mac_address': 'str',
            'network_interface_key': 'str',
            'owner_key': 'str',
            'private_ip_addresses': 'list[InstancePrivateIpAddress]',
            'is_source_dest_check': 'bool',
            'status': 'str',
            'subnet_key': 'str'
        }
        self.attribute_map = {
            'association': 'association',
            'attachment': 'attachment',
            'description': 'description',
            'security_groups': 'securityGroups',
            'interface_type': 'interfaceType',
            'ipv4_prefixes': 'ipv4Prefixes',
            'ipv6_addresses': 'ipv6Addresses',
            'ipv6_prefixes': 'ipv6Prefixes',
            'mac_address': 'macAddress',
            'network_interface_key': 'networkInterfaceKey',
            'owner_key': 'ownerKey',
            'private_ip_addresses': 'privateIpAddresses',
            'is_source_dest_check': 'isSourceDestCheck',
            'status': 'status',
            'subnet_key': 'subnetKey'
        }
        self._association = None
        self._attachment = None
        self._description = None
        self._security_groups = None
        self._interface_type = None
        self._ipv4_prefixes = None
        self._ipv6_addresses = None
        self._ipv6_prefixes = None
        self._mac_address = None
        self._network_interface_key = None
        self._owner_key = None
        self._private_ip_addresses = None
        self._is_source_dest_check = None
        self._status = None
        self._subnet_key = None

    @property
    def association(self):
        """
        Gets the association of this InstanceNetworkInterface.

        :return: The association of this InstanceNetworkInterface.
        :rtype: oci.cloud_bridge.models.InstanceNetworkInterfaceAssociation
        """
        return self._association

    @association.setter
    def association(self, association):
        """
        Sets the association of this InstanceNetworkInterface.

        :param association: The association of this InstanceNetworkInterface.
        :type: oci.cloud_bridge.models.InstanceNetworkInterfaceAssociation
        """
        self._association = association

    @property
    def attachment(self):
        """
        Gets the attachment of this InstanceNetworkInterface.

        :return: The attachment of this InstanceNetworkInterface.
        :rtype: oci.cloud_bridge.models.InstanceNetworkInterfaceAttachment
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """
        Sets the attachment of this InstanceNetworkInterface.

        :param attachment: The attachment of this InstanceNetworkInterface.
        :type: oci.cloud_bridge.models.InstanceNetworkInterfaceAttachment
        """
        self._attachment = attachment

    @property
    def description(self):
        """
        Gets the description of this InstanceNetworkInterface.
        The description.


        :return: The description of this InstanceNetworkInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this InstanceNetworkInterface.
        The description.


        :param description: The description of this InstanceNetworkInterface.
        :type: str
        """
        self._description = description

    @property
    def security_groups(self):
        """
        Gets the security_groups of this InstanceNetworkInterface.
        The security groups.


        :return: The security_groups of this InstanceNetworkInterface.
        :rtype: list[oci.cloud_bridge.models.GroupIdentifier]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """
        Sets the security_groups of this InstanceNetworkInterface.
        The security groups.


        :param security_groups: The security_groups of this InstanceNetworkInterface.
        :type: list[oci.cloud_bridge.models.GroupIdentifier]
        """
        self._security_groups = security_groups

    @property
    def interface_type(self):
        """
        Gets the interface_type of this InstanceNetworkInterface.
        The type of network interface.


        :return: The interface_type of this InstanceNetworkInterface.
        :rtype: str
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """
        Sets the interface_type of this InstanceNetworkInterface.
        The type of network interface.


        :param interface_type: The interface_type of this InstanceNetworkInterface.
        :type: str
        """
        self._interface_type = interface_type

    @property
    def ipv4_prefixes(self):
        """
        Gets the ipv4_prefixes of this InstanceNetworkInterface.
        The IPv4 delegated prefixes that are assigned to the network interface.


        :return: The ipv4_prefixes of this InstanceNetworkInterface.
        :rtype: list[str]
        """
        return self._ipv4_prefixes

    @ipv4_prefixes.setter
    def ipv4_prefixes(self, ipv4_prefixes):
        """
        Sets the ipv4_prefixes of this InstanceNetworkInterface.
        The IPv4 delegated prefixes that are assigned to the network interface.


        :param ipv4_prefixes: The ipv4_prefixes of this InstanceNetworkInterface.
        :type: list[str]
        """
        self._ipv4_prefixes = ipv4_prefixes

    @property
    def ipv6_addresses(self):
        """
        Gets the ipv6_addresses of this InstanceNetworkInterface.
        The IPv6 addresses associated with the network interface.


        :return: The ipv6_addresses of this InstanceNetworkInterface.
        :rtype: list[str]
        """
        return self._ipv6_addresses

    @ipv6_addresses.setter
    def ipv6_addresses(self, ipv6_addresses):
        """
        Sets the ipv6_addresses of this InstanceNetworkInterface.
        The IPv6 addresses associated with the network interface.


        :param ipv6_addresses: The ipv6_addresses of this InstanceNetworkInterface.
        :type: list[str]
        """
        self._ipv6_addresses = ipv6_addresses

    @property
    def ipv6_prefixes(self):
        """
        Gets the ipv6_prefixes of this InstanceNetworkInterface.
        The IPv6 delegated prefixes that are assigned to the network interface.


        :return: The ipv6_prefixes of this InstanceNetworkInterface.
        :rtype: list[str]
        """
        return self._ipv6_prefixes

    @ipv6_prefixes.setter
    def ipv6_prefixes(self, ipv6_prefixes):
        """
        Sets the ipv6_prefixes of this InstanceNetworkInterface.
        The IPv6 delegated prefixes that are assigned to the network interface.


        :param ipv6_prefixes: The ipv6_prefixes of this InstanceNetworkInterface.
        :type: list[str]
        """
        self._ipv6_prefixes = ipv6_prefixes

    @property
    def mac_address(self):
        """
        Gets the mac_address of this InstanceNetworkInterface.
        The MAC address.


        :return: The mac_address of this InstanceNetworkInterface.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this InstanceNetworkInterface.
        The MAC address.


        :param mac_address: The mac_address of this InstanceNetworkInterface.
        :type: str
        """
        self._mac_address = mac_address

    @property
    def network_interface_key(self):
        """
        Gets the network_interface_key of this InstanceNetworkInterface.
        The ID of the network interface.


        :return: The network_interface_key of this InstanceNetworkInterface.
        :rtype: str
        """
        return self._network_interface_key

    @network_interface_key.setter
    def network_interface_key(self, network_interface_key):
        """
        Sets the network_interface_key of this InstanceNetworkInterface.
        The ID of the network interface.


        :param network_interface_key: The network_interface_key of this InstanceNetworkInterface.
        :type: str
        """
        self._network_interface_key = network_interface_key

    @property
    def owner_key(self):
        """
        Gets the owner_key of this InstanceNetworkInterface.
        The ID of the AWS account that created the network interface.


        :return: The owner_key of this InstanceNetworkInterface.
        :rtype: str
        """
        return self._owner_key

    @owner_key.setter
    def owner_key(self, owner_key):
        """
        Sets the owner_key of this InstanceNetworkInterface.
        The ID of the AWS account that created the network interface.


        :param owner_key: The owner_key of this InstanceNetworkInterface.
        :type: str
        """
        self._owner_key = owner_key

    @property
    def private_ip_addresses(self):
        """
        Gets the private_ip_addresses of this InstanceNetworkInterface.
        The private IPv4 addresses associated with the network interface.


        :return: The private_ip_addresses of this InstanceNetworkInterface.
        :rtype: list[oci.cloud_bridge.models.InstancePrivateIpAddress]
        """
        return self._private_ip_addresses

    @private_ip_addresses.setter
    def private_ip_addresses(self, private_ip_addresses):
        """
        Sets the private_ip_addresses of this InstanceNetworkInterface.
        The private IPv4 addresses associated with the network interface.


        :param private_ip_addresses: The private_ip_addresses of this InstanceNetworkInterface.
        :type: list[oci.cloud_bridge.models.InstancePrivateIpAddress]
        """
        self._private_ip_addresses = private_ip_addresses

    @property
    def is_source_dest_check(self):
        """
        Gets the is_source_dest_check of this InstanceNetworkInterface.
        Indicates whether source/destination checking is enabled.


        :return: The is_source_dest_check of this InstanceNetworkInterface.
        :rtype: bool
        """
        return self._is_source_dest_check

    @is_source_dest_check.setter
    def is_source_dest_check(self, is_source_dest_check):
        """
        Sets the is_source_dest_check of this InstanceNetworkInterface.
        Indicates whether source/destination checking is enabled.


        :param is_source_dest_check: The is_source_dest_check of this InstanceNetworkInterface.
        :type: bool
        """
        self._is_source_dest_check = is_source_dest_check

    @property
    def status(self):
        """
        Gets the status of this InstanceNetworkInterface.
        The status of the network interface.


        :return: The status of this InstanceNetworkInterface.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InstanceNetworkInterface.
        The status of the network interface.


        :param status: The status of this InstanceNetworkInterface.
        :type: str
        """
        self._status = status

    @property
    def subnet_key(self):
        """
        Gets the subnet_key of this InstanceNetworkInterface.
        The ID of the subnet.


        :return: The subnet_key of this InstanceNetworkInterface.
        :rtype: str
        """
        return self._subnet_key

    @subnet_key.setter
    def subnet_key(self, subnet_key):
        """
        Sets the subnet_key of this InstanceNetworkInterface.
        The ID of the subnet.


        :param subnet_key: The subnet_key of this InstanceNetworkInterface.
        :type: str
        """
        self._subnet_key = subnet_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
