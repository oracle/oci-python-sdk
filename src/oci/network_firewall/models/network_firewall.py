# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkFirewall(object):
    """
    A network firewall is a security resource that exists in a subnet of your choice and controls incoming and outgoing network traffic based on a set of security rules. Each firewall is associated with a policy. Traffic is routed to and from the firewall from resources such as internet gateways and dynamic routing gateways (DRGs). For more information, see `Overview of Network Firewall`__

    __ https://docs.cloud.oracle.com/iaas/Content/network-firewall/overview.htm
    """

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewall.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewall.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewall.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewall.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewall.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewall.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewall.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkFirewall object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this NetworkFirewall.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NetworkFirewall.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this NetworkFirewall.
        :type display_name: str

        :param subnet_id:
            The value to assign to the subnet_id property of this NetworkFirewall.
        :type subnet_id: str

        :param ipv4_address:
            The value to assign to the ipv4_address property of this NetworkFirewall.
        :type ipv4_address: str

        :param ipv6_address:
            The value to assign to the ipv6_address property of this NetworkFirewall.
        :type ipv6_address: str

        :param network_firewall_policy_id:
            The value to assign to the network_firewall_policy_id property of this NetworkFirewall.
        :type network_firewall_policy_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this NetworkFirewall.
        :type availability_domain: str

        :param nat_configuration:
            The value to assign to the nat_configuration property of this NetworkFirewall.
        :type nat_configuration: oci.network_firewall.models.NatConfigurationResponse

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this NetworkFirewall.
        :type network_security_group_ids: list[str]

        :param time_created:
            The value to assign to the time_created property of this NetworkFirewall.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this NetworkFirewall.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this NetworkFirewall.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this NetworkFirewall.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this NetworkFirewall.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this NetworkFirewall.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this NetworkFirewall.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'subnet_id': 'str',
            'ipv4_address': 'str',
            'ipv6_address': 'str',
            'network_firewall_policy_id': 'str',
            'availability_domain': 'str',
            'nat_configuration': 'NatConfigurationResponse',
            'network_security_group_ids': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'subnet_id': 'subnetId',
            'ipv4_address': 'ipv4Address',
            'ipv6_address': 'ipv6Address',
            'network_firewall_policy_id': 'networkFirewallPolicyId',
            'availability_domain': 'availabilityDomain',
            'nat_configuration': 'natConfiguration',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._subnet_id = None
        self._ipv4_address = None
        self._ipv6_address = None
        self._network_firewall_policy_id = None
        self._availability_domain = None
        self._nat_configuration = None
        self._network_security_group_ids = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this NetworkFirewall.
        The `OCID`__ of the Network Firewall resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this NetworkFirewall.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NetworkFirewall.
        The `OCID`__ of the Network Firewall resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this NetworkFirewall.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this NetworkFirewall.
        The `OCID`__ of the compartment containing the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this NetworkFirewall.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this NetworkFirewall.
        The `OCID`__ of the compartment containing the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this NetworkFirewall.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this NetworkFirewall.
        A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this NetworkFirewall.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this NetworkFirewall.
        A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this NetworkFirewall.
        :type: str
        """
        self._display_name = display_name

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this NetworkFirewall.
        The `OCID`__ of the subnet associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this NetworkFirewall.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this NetworkFirewall.
        The `OCID`__ of the subnet associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this NetworkFirewall.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def ipv4_address(self):
        """
        Gets the ipv4_address of this NetworkFirewall.
        IPv4 address for the Network Firewall.


        :return: The ipv4_address of this NetworkFirewall.
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """
        Sets the ipv4_address of this NetworkFirewall.
        IPv4 address for the Network Firewall.


        :param ipv4_address: The ipv4_address of this NetworkFirewall.
        :type: str
        """
        self._ipv4_address = ipv4_address

    @property
    def ipv6_address(self):
        """
        Gets the ipv6_address of this NetworkFirewall.
        IPv6 address for the Network Firewall.


        :return: The ipv6_address of this NetworkFirewall.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """
        Sets the ipv6_address of this NetworkFirewall.
        IPv6 address for the Network Firewall.


        :param ipv6_address: The ipv6_address of this NetworkFirewall.
        :type: str
        """
        self._ipv6_address = ipv6_address

    @property
    def network_firewall_policy_id(self):
        """
        **[Required]** Gets the network_firewall_policy_id of this NetworkFirewall.
        The `OCID`__ of the Network Firewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The network_firewall_policy_id of this NetworkFirewall.
        :rtype: str
        """
        return self._network_firewall_policy_id

    @network_firewall_policy_id.setter
    def network_firewall_policy_id(self, network_firewall_policy_id):
        """
        Sets the network_firewall_policy_id of this NetworkFirewall.
        The `OCID`__ of the Network Firewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param network_firewall_policy_id: The network_firewall_policy_id of this NetworkFirewall.
        :type: str
        """
        self._network_firewall_policy_id = network_firewall_policy_id

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this NetworkFirewall.
        Availability Domain where Network Firewall instance is created.
        To get a list of availability domains for a tenancy, use the :func:`list_availability_domains` operation.
        Example: `kIdk:PHX-AD-1`


        :return: The availability_domain of this NetworkFirewall.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this NetworkFirewall.
        Availability Domain where Network Firewall instance is created.
        To get a list of availability domains for a tenancy, use the :func:`list_availability_domains` operation.
        Example: `kIdk:PHX-AD-1`


        :param availability_domain: The availability_domain of this NetworkFirewall.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def nat_configuration(self):
        """
        Gets the nat_configuration of this NetworkFirewall.

        :return: The nat_configuration of this NetworkFirewall.
        :rtype: oci.network_firewall.models.NatConfigurationResponse
        """
        return self._nat_configuration

    @nat_configuration.setter
    def nat_configuration(self, nat_configuration):
        """
        Sets the nat_configuration of this NetworkFirewall.

        :param nat_configuration: The nat_configuration of this NetworkFirewall.
        :type: oci.network_firewall.models.NatConfigurationResponse
        """
        self._nat_configuration = nat_configuration

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this NetworkFirewall.
        An array of network security groups `OCID`__ associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this NetworkFirewall.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this NetworkFirewall.
        An array of network security groups `OCID`__ associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this NetworkFirewall.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this NetworkFirewall.
        The time at which the Network Firewall was created in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this NetworkFirewall.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this NetworkFirewall.
        The time at which the Network Firewall was created in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this NetworkFirewall.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this NetworkFirewall.
        The time at which the Network Firewall was updated in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this NetworkFirewall.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this NetworkFirewall.
        The time at which the Network Firewall was updated in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this NetworkFirewall.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this NetworkFirewall.
        The current state of the Network Firewall.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this NetworkFirewall.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this NetworkFirewall.
        The current state of the Network Firewall.


        :param lifecycle_state: The lifecycle_state of this NetworkFirewall.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this NetworkFirewall.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in 'FAILED' state.


        :return: The lifecycle_details of this NetworkFirewall.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this NetworkFirewall.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in 'FAILED' state.


        :param lifecycle_details: The lifecycle_details of this NetworkFirewall.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this NetworkFirewall.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this NetworkFirewall.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this NetworkFirewall.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this NetworkFirewall.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this NetworkFirewall.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this NetworkFirewall.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this NetworkFirewall.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this NetworkFirewall.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this NetworkFirewall.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this NetworkFirewall.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this NetworkFirewall.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this NetworkFirewall.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
