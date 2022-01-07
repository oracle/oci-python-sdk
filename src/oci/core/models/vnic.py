# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Vnic(object):
    """
    A virtual network interface card. Each VNIC resides in a subnet in a VCN.
    An instance attaches to a VNIC to obtain a network connection into the VCN
    through that subnet. Each instance has a *primary VNIC* that is automatically
    created and attached during launch. You can add *secondary VNICs* to an
    instance after it's launched. For more information, see
    `Virtual Network Interface Cards (VNICs)`__.

    Each VNIC has a *primary private IP* that is automatically assigned during launch.
    You can add *secondary private IPs* to a VNIC after it's created. For more
    information, see :func:`create_private_ip` and
    `IP Addresses`__.


    If you are an Oracle Cloud VMware Solution customer, you will have secondary VNICs
    that reside in a VLAN instead of a subnet. These VNICs have other differences, which
    are called out in the descriptions of the relevant attributes in the `Vnic` object.
    Also see :class:`Vlan`.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Vnic.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Vnic.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Vnic.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a Vnic.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new Vnic object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this Vnic.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Vnic.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Vnic.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Vnic.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Vnic.
        :type freeform_tags: dict(str, str)

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

        :param nsg_ids:
            The value to assign to the nsg_ids property of this Vnic.
        :type nsg_ids: list[str]

        :param vlan_id:
            The value to assign to the vlan_id property of this Vnic.
        :type vlan_id: str

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
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostname_label': 'str',
            'id': 'str',
            'is_primary': 'bool',
            'lifecycle_state': 'str',
            'mac_address': 'str',
            'nsg_ids': 'list[str]',
            'vlan_id': 'str',
            'private_ip': 'str',
            'public_ip': 'str',
            'skip_source_dest_check': 'bool',
            'subnet_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'hostname_label': 'hostnameLabel',
            'id': 'id',
            'is_primary': 'isPrimary',
            'lifecycle_state': 'lifecycleState',
            'mac_address': 'macAddress',
            'nsg_ids': 'nsgIds',
            'vlan_id': 'vlanId',
            'private_ip': 'privateIp',
            'public_ip': 'publicIp',
            'skip_source_dest_check': 'skipSourceDestCheck',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._hostname_label = None
        self._id = None
        self._is_primary = None
        self._lifecycle_state = None
        self._mac_address = None
        self._nsg_ids = None
        self._vlan_id = None
        self._private_ip = None
        self._public_ip = None
        self._skip_source_dest_check = None
        self._subnet_id = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this Vnic.
        The VNIC's availability domain.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this Vnic.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Vnic.
        The VNIC's availability domain.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this Vnic.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Vnic.
        The `OCID`__ of the compartment containing the VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Vnic.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vnic.
        The `OCID`__ of the compartment containing the VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Vnic.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Vnic.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Vnic.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Vnic.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Vnic.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this Vnic.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Vnic.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Vnic.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Vnic.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Vnic.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Vnic.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Vnic.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Vnic.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

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
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


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
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this Vnic.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Vnic.
        The `OCID`__ of the VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Vnic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vnic.
        The `OCID`__ of the VNIC.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


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
        **[Required]** Gets the lifecycle_state of this Vnic.
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
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def mac_address(self):
        """
        Gets the mac_address of this Vnic.
        The MAC address of the VNIC.

        If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution,
        the MAC address is learned. If the VNIC belongs to a subnet, the
        MAC address is a static, Oracle-provided value.

        Example: `00:00:00:00:00:01`


        :return: The mac_address of this Vnic.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this Vnic.
        The MAC address of the VNIC.

        If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution,
        the MAC address is learned. If the VNIC belongs to a subnet, the
        MAC address is a static, Oracle-provided value.

        Example: `00:00:00:00:00:01`


        :param mac_address: The mac_address of this Vnic.
        :type: str
        """
        self._mac_address = mac_address

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this Vnic.
        A list of the OCIDs of the network security groups that the VNIC belongs to.

        If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
        belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the
        VNIC belongs to the NSGs that are associated with the VLAN itself. See :class:`Vlan`.

        For more information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this Vnic.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this Vnic.
        A list of the OCIDs of the network security groups that the VNIC belongs to.

        If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
        belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the
        VNIC belongs to the NSGs that are associated with the VLAN itself. See :class:`Vlan`.

        For more information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this Vnic.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def vlan_id(self):
        """
        Gets the vlan_id of this Vnic.
        If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
        belonging to a subnet), the `vlanId` is the `OCID`__ of the VLAN the VNIC is in. See
        :class:`Vlan`. If the VNIC is instead in a subnet, `subnetId` has a value.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vlan_id of this Vnic.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """
        Sets the vlan_id of this Vnic.
        If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
        belonging to a subnet), the `vlanId` is the `OCID`__ of the VLAN the VNIC is in. See
        :class:`Vlan`. If the VNIC is instead in a subnet, `subnetId` has a value.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vlan_id: The vlan_id of this Vnic.
        :type: str
        """
        self._vlan_id = vlan_id

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


        If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
        belonging to a subnet), the `skipSourceDestCheck` attribute is `true`.
        This is because the source/destination check is always disabled for VNICs in a VLAN.

        Example: `true`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip


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


        If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
        belonging to a subnet), the `skipSourceDestCheck` attribute is `true`.
        This is because the source/destination check is always disabled for VNICs in a VLAN.

        Example: `true`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip


        :param skip_source_dest_check: The skip_source_dest_check of this Vnic.
        :type: bool
        """
        self._skip_source_dest_check = skip_source_dest_check

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this Vnic.
        The `OCID`__ of the subnet the VNIC is in.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this Vnic.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Vnic.
        The `OCID`__ of the subnet the VNIC is in.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this Vnic.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Vnic.
        The date and time the VNIC was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Vnic.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vnic.
        The date and time the VNIC was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


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
