# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Vnic(object):

    def __init__(self, **kwargs):
        """
        Initializes a new Vnic object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this Vnic.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Vnic.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Vnic.
        :type display_name: str

        :param hostname_label:
            The value to assign to the hostname_label property of this Vnic.
        :type hostname_label: str

        :param id:
            The value to assign to the id property of this Vnic.
        :type id: str

        :param is_primary:
            The value to assign to the is_primary property of this Vnic.
        :type is_primary: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Vnic.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param mac_address:
            The value to assign to the mac_address property of this Vnic.
        :type mac_address: str

        :param private_ip:
            The value to assign to the private_ip property of this Vnic.
        :type private_ip: str

        :param public_ip:
            The value to assign to the public_ip property of this Vnic.
        :type public_ip: str

        :param skip_source_dest_check:
            The value to assign to the skip_source_dest_check property of this Vnic.
        :type skip_source_dest_check: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this Vnic.
        :type subnet_id: str

        :param time_created:
            The value to assign to the time_created property of this Vnic.
        :type time_created: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'hostname_label': 'str',
            'id': 'str',
            'is_primary': 'bool',
            'lifecycle_state': 'str',
            'mac_address': 'str',
            'private_ip': 'str',
            'public_ip': 'str',
            'skip_source_dest_check': 'bool',
            'subnet_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'hostname_label': 'hostnameLabel',
            'id': 'id',
            'is_primary': 'isPrimary',
            'lifecycle_state': 'lifecycleState',
            'mac_address': 'macAddress',
            'private_ip': 'privateIp',
            'public_ip': 'publicIp',
            'skip_source_dest_check': 'skipSourceDestCheck',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._hostname_label = None
        self._id = None
        self._is_primary = None
        self._lifecycle_state = None
        self._mac_address = None
        self._private_ip = None
        self._public_ip = None
        self._skip_source_dest_check = None
        self._subnet_id = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Vnic.
        The VNIC's Availability Domain.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this Vnic.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Vnic.
        The VNIC's Availability Domain.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this Vnic.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Vnic.
        The OCID of the compartment containing the VNIC.


        :return: The compartment_id of this Vnic.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vnic.
        The OCID of the compartment containing the VNIC.


        :param compartment_id: The compartment_id of this Vnic.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Vnic.
        A user-friendly name. Does not have to be unique.
        Avoid entering confidential information.


        :return: The display_name of this Vnic.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Vnic.
        A user-friendly name. Does not have to be unique.
        Avoid entering confidential information.


        :param display_name: The display_name of this Vnic.
        :type: str
        """
        self._display_name = display_name

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this Vnic.
        The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
        portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `bminstance-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :return: The hostname_label of this Vnic.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this Vnic.
        The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
        portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `bminstance-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this Vnic.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def id(self):
        """
        Gets the id of this Vnic.
        The OCID of the VNIC.


        :return: The id of this Vnic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vnic.
        The OCID of the VNIC.


        :param id: The id of this Vnic.
        :type: str
        """
        self._id = id

    @property
    def is_primary(self):
        """
        Gets the is_primary of this Vnic.
        Whether the VNIC is the primary VNIC (the VNIC that is automatically created
        and attached during instance launch).


        :return: The is_primary of this Vnic.
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """
        Sets the is_primary of this Vnic.
        Whether the VNIC is the primary VNIC (the VNIC that is automatically created
        and attached during instance launch).


        :param is_primary: The is_primary of this Vnic.
        :type: bool
        """
        self._is_primary = is_primary

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Vnic.
        The current state of the VNIC.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Vnic.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Vnic.
        The current state of the VNIC.


        :param lifecycle_state: The lifecycle_state of this Vnic.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def mac_address(self):
        """
        Gets the mac_address of this Vnic.
        The MAC address of the VNIC.

        Example: `00:00:17:B6:4D:DD`


        :return: The mac_address of this Vnic.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this Vnic.
        The MAC address of the VNIC.

        Example: `00:00:17:B6:4D:DD`


        :param mac_address: The mac_address of this Vnic.
        :type: str
        """
        self._mac_address = mac_address

    @property
    def private_ip(self):
        """
        Gets the private_ip of this Vnic.
        The private IP address of the primary `privateIp` object on the VNIC.
        The address is within the CIDR of the VNIC's subnet.

        Example: `10.0.3.3`


        :return: The private_ip of this Vnic.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this Vnic.
        The private IP address of the primary `privateIp` object on the VNIC.
        The address is within the CIDR of the VNIC's subnet.

        Example: `10.0.3.3`


        :param private_ip: The private_ip of this Vnic.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """
        Gets the public_ip of this Vnic.
        The public IP address of the VNIC, if one is assigned.


        :return: The public_ip of this Vnic.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """
        Sets the public_ip of this Vnic.
        The public IP address of the VNIC, if one is assigned.


        :param public_ip: The public_ip of this Vnic.
        :type: str
        """
        self._public_ip = public_ip

    @property
    def skip_source_dest_check(self):
        """
        Gets the skip_source_dest_check of this Vnic.
        Whether the source/destination check is disabled on the VNIC.
        Defaults to `false`, which means the check is performed. For information
        about why you would skip the source/destination check, see
        `Using a Private IP as a Route Target`__.

        Example: `true`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm#privateip


        :return: The skip_source_dest_check of this Vnic.
        :rtype: bool
        """
        return self._skip_source_dest_check

    @skip_source_dest_check.setter
    def skip_source_dest_check(self, skip_source_dest_check):
        """
        Sets the skip_source_dest_check of this Vnic.
        Whether the source/destination check is disabled on the VNIC.
        Defaults to `false`, which means the check is performed. For information
        about why you would skip the source/destination check, see
        `Using a Private IP as a Route Target`__.

        Example: `true`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm#privateip


        :param skip_source_dest_check: The skip_source_dest_check of this Vnic.
        :type: bool
        """
        self._skip_source_dest_check = skip_source_dest_check

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this Vnic.
        The OCID of the subnet the VNIC is in.


        :return: The subnet_id of this Vnic.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Vnic.
        The OCID of the subnet the VNIC is in.


        :param subnet_id: The subnet_id of this Vnic.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Vnic.
        The date and time the VNIC was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Vnic.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vnic.
        The date and time the VNIC was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this Vnic.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
