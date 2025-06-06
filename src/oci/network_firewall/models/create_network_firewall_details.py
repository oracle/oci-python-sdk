# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNetworkFirewallDetails(object):
    """
    The information about new Network Firewall.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNetworkFirewallDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateNetworkFirewallDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateNetworkFirewallDetails.
        :type compartment_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateNetworkFirewallDetails.
        :type subnet_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateNetworkFirewallDetails.
        :type availability_domain: str

        :param network_firewall_policy_id:
            The value to assign to the network_firewall_policy_id property of this CreateNetworkFirewallDetails.
        :type network_firewall_policy_id: str

        :param ipv4_address:
            The value to assign to the ipv4_address property of this CreateNetworkFirewallDetails.
        :type ipv4_address: str

        :param ipv6_address:
            The value to assign to the ipv6_address property of this CreateNetworkFirewallDetails.
        :type ipv6_address: str

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this CreateNetworkFirewallDetails.
        :type network_security_group_ids: list[str]

        :param nat_configuration:
            The value to assign to the nat_configuration property of this CreateNetworkFirewallDetails.
        :type nat_configuration: oci.network_firewall.models.NatConfigurationRequest

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateNetworkFirewallDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateNetworkFirewallDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'subnet_id': 'str',
            'availability_domain': 'str',
            'network_firewall_policy_id': 'str',
            'ipv4_address': 'str',
            'ipv6_address': 'str',
            'network_security_group_ids': 'list[str]',
            'nat_configuration': 'NatConfigurationRequest',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'subnet_id': 'subnetId',
            'availability_domain': 'availabilityDomain',
            'network_firewall_policy_id': 'networkFirewallPolicyId',
            'ipv4_address': 'ipv4Address',
            'ipv6_address': 'ipv6Address',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'nat_configuration': 'natConfiguration',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._compartment_id = None
        self._subnet_id = None
        self._availability_domain = None
        self._network_firewall_policy_id = None
        self._ipv4_address = None
        self._ipv6_address = None
        self._network_security_group_ids = None
        self._nat_configuration = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateNetworkFirewallDetails.
        A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateNetworkFirewallDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateNetworkFirewallDetails.
        A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateNetworkFirewallDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateNetworkFirewallDetails.
        The `OCID`__ of the compartment containing the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateNetworkFirewallDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateNetworkFirewallDetails.
        The `OCID`__ of the compartment containing the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateNetworkFirewallDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateNetworkFirewallDetails.
        The `OCID`__ of the subnet associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateNetworkFirewallDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateNetworkFirewallDetails.
        The `OCID`__ of the subnet associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateNetworkFirewallDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this CreateNetworkFirewallDetails.
        Availability Domain where Network Firewall instance is created.
        To get a list of availability domains for a tenancy, use :func:`list_availability_domains` operation.
        Example: `kIdk:PHX-AD-1`


        :return: The availability_domain of this CreateNetworkFirewallDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateNetworkFirewallDetails.
        Availability Domain where Network Firewall instance is created.
        To get a list of availability domains for a tenancy, use :func:`list_availability_domains` operation.
        Example: `kIdk:PHX-AD-1`


        :param availability_domain: The availability_domain of this CreateNetworkFirewallDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def network_firewall_policy_id(self):
        """
        **[Required]** Gets the network_firewall_policy_id of this CreateNetworkFirewallDetails.
        The `OCID`__ of the Network Firewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The network_firewall_policy_id of this CreateNetworkFirewallDetails.
        :rtype: str
        """
        return self._network_firewall_policy_id

    @network_firewall_policy_id.setter
    def network_firewall_policy_id(self, network_firewall_policy_id):
        """
        Sets the network_firewall_policy_id of this CreateNetworkFirewallDetails.
        The `OCID`__ of the Network Firewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param network_firewall_policy_id: The network_firewall_policy_id of this CreateNetworkFirewallDetails.
        :type: str
        """
        self._network_firewall_policy_id = network_firewall_policy_id

    @property
    def ipv4_address(self):
        """
        Gets the ipv4_address of this CreateNetworkFirewallDetails.
        IPv4 address for the Network Firewall.


        :return: The ipv4_address of this CreateNetworkFirewallDetails.
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """
        Sets the ipv4_address of this CreateNetworkFirewallDetails.
        IPv4 address for the Network Firewall.


        :param ipv4_address: The ipv4_address of this CreateNetworkFirewallDetails.
        :type: str
        """
        self._ipv4_address = ipv4_address

    @property
    def ipv6_address(self):
        """
        Gets the ipv6_address of this CreateNetworkFirewallDetails.
        IPv6 address for the Network Firewall.


        :return: The ipv6_address of this CreateNetworkFirewallDetails.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """
        Sets the ipv6_address of this CreateNetworkFirewallDetails.
        IPv6 address for the Network Firewall.


        :param ipv6_address: The ipv6_address of this CreateNetworkFirewallDetails.
        :type: str
        """
        self._ipv6_address = ipv6_address

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this CreateNetworkFirewallDetails.
        An array of network security groups `OCID`__ associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this CreateNetworkFirewallDetails.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this CreateNetworkFirewallDetails.
        An array of network security groups `OCID`__ associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this CreateNetworkFirewallDetails.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def nat_configuration(self):
        """
        Gets the nat_configuration of this CreateNetworkFirewallDetails.

        :return: The nat_configuration of this CreateNetworkFirewallDetails.
        :rtype: oci.network_firewall.models.NatConfigurationRequest
        """
        return self._nat_configuration

    @nat_configuration.setter
    def nat_configuration(self, nat_configuration):
        """
        Sets the nat_configuration of this CreateNetworkFirewallDetails.

        :param nat_configuration: The nat_configuration of this CreateNetworkFirewallDetails.
        :type: oci.network_firewall.models.NatConfigurationRequest
        """
        self._nat_configuration = nat_configuration

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateNetworkFirewallDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateNetworkFirewallDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateNetworkFirewallDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateNetworkFirewallDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateNetworkFirewallDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateNetworkFirewallDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateNetworkFirewallDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateNetworkFirewallDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
