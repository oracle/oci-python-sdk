# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMountTargetDetails(object):
    """
    CreateMountTargetDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMountTargetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateMountTargetDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMountTargetDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateMountTargetDetails.
        :type display_name: str

        :param hostname_label:
            The value to assign to the hostname_label property of this CreateMountTargetDetails.
        :type hostname_label: str

        :param ip_address:
            The value to assign to the ip_address property of this CreateMountTargetDetails.
        :type ip_address: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateMountTargetDetails.
        :type subnet_id: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'hostname_label': 'str',
            'ip_address': 'str',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'hostname_label': 'hostnameLabel',
            'ip_address': 'ipAddress',
            'subnet_id': 'subnetId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._hostname_label = None
        self._ip_address = None
        self._subnet_id = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateMountTargetDetails.
        The availability domain in which to create the mount target.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateMountTargetDetails.
        The availability domain in which to create the mount target.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this CreateMountTargetDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMountTargetDetails.
        The OCID of the compartment in which to create the mount target.


        :return: The compartment_id of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMountTargetDetails.
        The OCID of the compartment in which to create the mount target.


        :param compartment_id: The compartment_id of this CreateMountTargetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMountTargetDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :return: The display_name of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMountTargetDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :param display_name: The display_name of this CreateMountTargetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this CreateMountTargetDetails.
        The hostname for the mount target's IP address, used for
        DNS resolution. The value is the hostname portion of the private IP
        address's fully qualified domain name (FQDN). For example,
        `files-1` in the FQDN `files-1.subnet123.vcn1.oraclevcn.com`.
        Must be unique across all VNICs in the subnet and comply
        with `RFC 952`__
        and `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `files-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :return: The hostname_label of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this CreateMountTargetDetails.
        The hostname for the mount target's IP address, used for
        DNS resolution. The value is the hostname portion of the private IP
        address's fully qualified domain name (FQDN). For example,
        `files-1` in the FQDN `files-1.subnet123.vcn1.oraclevcn.com`.
        Must be unique across all VNICs in the subnet and comply
        with `RFC 952`__
        and `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `files-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this CreateMountTargetDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CreateMountTargetDetails.
        A private IP address of your choice. Must be an available IP address within
        the subnet's CIDR. If you don't specify a value, Oracle automatically
        assigns a private IP address from the subnet.

        Example: `10.0.3.3`


        :return: The ip_address of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateMountTargetDetails.
        A private IP address of your choice. Must be an available IP address within
        the subnet's CIDR. If you don't specify a value, Oracle automatically
        assigns a private IP address from the subnet.

        Example: `10.0.3.3`


        :param ip_address: The ip_address of this CreateMountTargetDetails.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateMountTargetDetails.
        The OCID of the subnet in which to create the mount target.


        :return: The subnet_id of this CreateMountTargetDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateMountTargetDetails.
        The OCID of the subnet in which to create the mount target.


        :param subnet_id: The subnet_id of this CreateMountTargetDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
