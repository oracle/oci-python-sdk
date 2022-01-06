# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationCreateVnicDetails(object):
    """
    Contains the properties of the VNIC for an instance configuration. See :class:`CreateVnicDetails`
    and `Instance Configurations`__ for more information.

    __ https://docs.cloud.oracle.com/iaas/Content/Compute/Concepts/instancemanagement.htm#config
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationCreateVnicDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param assign_public_ip:
            The value to assign to the assign_public_ip property of this InstanceConfigurationCreateVnicDetails.
        :type assign_public_ip: bool

        :param assign_private_dns_record:
            The value to assign to the assign_private_dns_record property of this InstanceConfigurationCreateVnicDetails.
        :type assign_private_dns_record: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this InstanceConfigurationCreateVnicDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationCreateVnicDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InstanceConfigurationCreateVnicDetails.
        :type freeform_tags: dict(str, str)

        :param hostname_label:
            The value to assign to the hostname_label property of this InstanceConfigurationCreateVnicDetails.
        :type hostname_label: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this InstanceConfigurationCreateVnicDetails.
        :type nsg_ids: list[str]

        :param private_ip:
            The value to assign to the private_ip property of this InstanceConfigurationCreateVnicDetails.
        :type private_ip: str

        :param skip_source_dest_check:
            The value to assign to the skip_source_dest_check property of this InstanceConfigurationCreateVnicDetails.
        :type skip_source_dest_check: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this InstanceConfigurationCreateVnicDetails.
        :type subnet_id: str

        """
        self.swagger_types = {
            'assign_public_ip': 'bool',
            'assign_private_dns_record': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostname_label': 'str',
            'nsg_ids': 'list[str]',
            'private_ip': 'str',
            'skip_source_dest_check': 'bool',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'assign_public_ip': 'assignPublicIp',
            'assign_private_dns_record': 'assignPrivateDnsRecord',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'hostname_label': 'hostnameLabel',
            'nsg_ids': 'nsgIds',
            'private_ip': 'privateIp',
            'skip_source_dest_check': 'skipSourceDestCheck',
            'subnet_id': 'subnetId'
        }

        self._assign_public_ip = None
        self._assign_private_dns_record = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._hostname_label = None
        self._nsg_ids = None
        self._private_ip = None
        self._skip_source_dest_check = None
        self._subnet_id = None

    @property
    def assign_public_ip(self):
        """
        Gets the assign_public_ip of this InstanceConfigurationCreateVnicDetails.
        Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of :class:`CreateVnicDetails`
        for more information.


        :return: The assign_public_ip of this InstanceConfigurationCreateVnicDetails.
        :rtype: bool
        """
        return self._assign_public_ip

    @assign_public_ip.setter
    def assign_public_ip(self, assign_public_ip):
        """
        Sets the assign_public_ip of this InstanceConfigurationCreateVnicDetails.
        Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of :class:`CreateVnicDetails`
        for more information.


        :param assign_public_ip: The assign_public_ip of this InstanceConfigurationCreateVnicDetails.
        :type: bool
        """
        self._assign_public_ip = assign_public_ip

    @property
    def assign_private_dns_record(self):
        """
        Gets the assign_private_dns_record of this InstanceConfigurationCreateVnicDetails.
        Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of :class:`CreateVnicDetails`
        for more information.


        :return: The assign_private_dns_record of this InstanceConfigurationCreateVnicDetails.
        :rtype: bool
        """
        return self._assign_private_dns_record

    @assign_private_dns_record.setter
    def assign_private_dns_record(self, assign_private_dns_record):
        """
        Sets the assign_private_dns_record of this InstanceConfigurationCreateVnicDetails.
        Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of :class:`CreateVnicDetails`
        for more information.


        :param assign_private_dns_record: The assign_private_dns_record of this InstanceConfigurationCreateVnicDetails.
        :type: bool
        """
        self._assign_private_dns_record = assign_private_dns_record

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this InstanceConfigurationCreateVnicDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this InstanceConfigurationCreateVnicDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InstanceConfigurationCreateVnicDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this InstanceConfigurationCreateVnicDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceConfigurationCreateVnicDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this InstanceConfigurationCreateVnicDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceConfigurationCreateVnicDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this InstanceConfigurationCreateVnicDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InstanceConfigurationCreateVnicDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this InstanceConfigurationCreateVnicDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InstanceConfigurationCreateVnicDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this InstanceConfigurationCreateVnicDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this InstanceConfigurationCreateVnicDetails.
        The hostname for the VNIC's primary private IP.
        See the `hostnameLabel` attribute of :class:`CreateVnicDetails` for more information.


        :return: The hostname_label of this InstanceConfigurationCreateVnicDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this InstanceConfigurationCreateVnicDetails.
        The hostname for the VNIC's primary private IP.
        See the `hostnameLabel` attribute of :class:`CreateVnicDetails` for more information.


        :param hostname_label: The hostname_label of this InstanceConfigurationCreateVnicDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this InstanceConfigurationCreateVnicDetails.
        A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this InstanceConfigurationCreateVnicDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this InstanceConfigurationCreateVnicDetails.
        A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this InstanceConfigurationCreateVnicDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def private_ip(self):
        """
        Gets the private_ip of this InstanceConfigurationCreateVnicDetails.
        A private IP address of your choice to assign to the VNIC.
        See the `privateIp` attribute of :class:`CreateVnicDetails` for more information.


        :return: The private_ip of this InstanceConfigurationCreateVnicDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this InstanceConfigurationCreateVnicDetails.
        A private IP address of your choice to assign to the VNIC.
        See the `privateIp` attribute of :class:`CreateVnicDetails` for more information.


        :param private_ip: The private_ip of this InstanceConfigurationCreateVnicDetails.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def skip_source_dest_check(self):
        """
        Gets the skip_source_dest_check of this InstanceConfigurationCreateVnicDetails.
        Whether the source/destination check is disabled on the VNIC.
        See the `skipSourceDestCheck` attribute of :class:`CreateVnicDetails` for more information.


        :return: The skip_source_dest_check of this InstanceConfigurationCreateVnicDetails.
        :rtype: bool
        """
        return self._skip_source_dest_check

    @skip_source_dest_check.setter
    def skip_source_dest_check(self, skip_source_dest_check):
        """
        Sets the skip_source_dest_check of this InstanceConfigurationCreateVnicDetails.
        Whether the source/destination check is disabled on the VNIC.
        See the `skipSourceDestCheck` attribute of :class:`CreateVnicDetails` for more information.


        :param skip_source_dest_check: The skip_source_dest_check of this InstanceConfigurationCreateVnicDetails.
        :type: bool
        """
        self._skip_source_dest_check = skip_source_dest_check

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this InstanceConfigurationCreateVnicDetails.
        The OCID of the subnet to create the VNIC in.
        See the `subnetId` attribute of :class:`CreateVnicDetails` for more information.


        :return: The subnet_id of this InstanceConfigurationCreateVnicDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this InstanceConfigurationCreateVnicDetails.
        The OCID of the subnet to create the VNIC in.
        See the `subnetId` attribute of :class:`CreateVnicDetails` for more information.


        :param subnet_id: The subnet_id of this InstanceConfigurationCreateVnicDetails.
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
