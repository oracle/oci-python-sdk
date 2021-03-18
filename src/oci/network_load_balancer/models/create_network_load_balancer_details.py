# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNetworkLoadBalancerDetails(object):
    """
    The properties that define a network load balancer. For more information, see
    `Managing a network load balancer`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, then
    contact an administrator. If you are an administrator who writes policies to give users access, then see
    `Getting Started with Policies`__.

    For information about endpoints and signing API requests, see
    `About the API`__. For information about available SDKs and tools, see
    `SDKS and Other Tools`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingloadbalancer.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm
    __ https://docs.cloud.oracle.com/Content/API/Concepts/sdks.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNetworkLoadBalancerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateNetworkLoadBalancerDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateNetworkLoadBalancerDetails.
        :type display_name: str

        :param is_preserve_source_destination:
            The value to assign to the is_preserve_source_destination property of this CreateNetworkLoadBalancerDetails.
        :type is_preserve_source_destination: bool

        :param reserved_ips:
            The value to assign to the reserved_ips property of this CreateNetworkLoadBalancerDetails.
        :type reserved_ips: list[oci.network_load_balancer.models.ReservedIP]

        :param is_private:
            The value to assign to the is_private property of this CreateNetworkLoadBalancerDetails.
        :type is_private: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateNetworkLoadBalancerDetails.
        :type subnet_id: str

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this CreateNetworkLoadBalancerDetails.
        :type network_security_group_ids: list[str]

        :param listeners:
            The value to assign to the listeners property of this CreateNetworkLoadBalancerDetails.
        :type listeners: dict(str, ListenerDetails)

        :param backend_sets:
            The value to assign to the backend_sets property of this CreateNetworkLoadBalancerDetails.
        :type backend_sets: dict(str, BackendSetDetails)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateNetworkLoadBalancerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateNetworkLoadBalancerDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'is_preserve_source_destination': 'bool',
            'reserved_ips': 'list[ReservedIP]',
            'is_private': 'bool',
            'subnet_id': 'str',
            'network_security_group_ids': 'list[str]',
            'listeners': 'dict(str, ListenerDetails)',
            'backend_sets': 'dict(str, BackendSetDetails)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'is_preserve_source_destination': 'isPreserveSourceDestination',
            'reserved_ips': 'reservedIps',
            'is_private': 'isPrivate',
            'subnet_id': 'subnetId',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'listeners': 'listeners',
            'backend_sets': 'backendSets',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._is_preserve_source_destination = None
        self._reserved_ips = None
        self._is_private = None
        self._subnet_id = None
        self._network_security_group_ids = None
        self._listeners = None
        self._backend_sets = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateNetworkLoadBalancerDetails.
        The `OCID`__ of the compartment containing the network load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateNetworkLoadBalancerDetails.
        The `OCID`__ of the compartment containing the network load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateNetworkLoadBalancerDetails.
        Network load balancer identifier, which can be renamed.


        :return: The display_name of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateNetworkLoadBalancerDetails.
        Network load balancer identifier, which can be renamed.


        :param display_name: The display_name of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_preserve_source_destination(self):
        """
        Gets the is_preserve_source_destination of this CreateNetworkLoadBalancerDetails.
        This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically
        enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.


        :return: The is_preserve_source_destination of this CreateNetworkLoadBalancerDetails.
        :rtype: bool
        """
        return self._is_preserve_source_destination

    @is_preserve_source_destination.setter
    def is_preserve_source_destination(self, is_preserve_source_destination):
        """
        Sets the is_preserve_source_destination of this CreateNetworkLoadBalancerDetails.
        This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically
        enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.


        :param is_preserve_source_destination: The is_preserve_source_destination of this CreateNetworkLoadBalancerDetails.
        :type: bool
        """
        self._is_preserve_source_destination = is_preserve_source_destination

    @property
    def reserved_ips(self):
        """
        Gets the reserved_ips of this CreateNetworkLoadBalancerDetails.
        An array of reserved Ips.


        :return: The reserved_ips of this CreateNetworkLoadBalancerDetails.
        :rtype: list[oci.network_load_balancer.models.ReservedIP]
        """
        return self._reserved_ips

    @reserved_ips.setter
    def reserved_ips(self, reserved_ips):
        """
        Sets the reserved_ips of this CreateNetworkLoadBalancerDetails.
        An array of reserved Ips.


        :param reserved_ips: The reserved_ips of this CreateNetworkLoadBalancerDetails.
        :type: list[oci.network_load_balancer.models.ReservedIP]
        """
        self._reserved_ips = reserved_ips

    @property
    def is_private(self):
        """
        Gets the is_private of this CreateNetworkLoadBalancerDetails.
        Whether the network load balancer has a virtual cloud network-local (private) IP address.

        If \"true\", then the service assigns a private IP address to the network load balancer.

        If \"false\", then the service assigns a public IP address to the network load balancer.

        A public network load balancer is accessible from the internet, depending on the
        `security list rules`__ for your virtual cloud network. For more information about public and
        private network load balancers,
        see `How Network Load Balancing Works`__.
        This value is true by default.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-network-load-balancing-works


        :return: The is_private of this CreateNetworkLoadBalancerDetails.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """
        Sets the is_private of this CreateNetworkLoadBalancerDetails.
        Whether the network load balancer has a virtual cloud network-local (private) IP address.

        If \"true\", then the service assigns a private IP address to the network load balancer.

        If \"false\", then the service assigns a public IP address to the network load balancer.

        A public network load balancer is accessible from the internet, depending on the
        `security list rules`__ for your virtual cloud network. For more information about public and
        private network load balancers,
        see `How Network Load Balancing Works`__.
        This value is true by default.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-network-load-balancing-works


        :param is_private: The is_private of this CreateNetworkLoadBalancerDetails.
        :type: bool
        """
        self._is_private = is_private

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateNetworkLoadBalancerDetails.
        The subnet in which the network load balancer is spawned `OCIDs`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateNetworkLoadBalancerDetails.
        The subnet in which the network load balancer is spawned `OCIDs`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this CreateNetworkLoadBalancerDetails.
        An array of network security groups `OCIDs`__ associated with the network load
        balancer.

        During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups.

        The benefits of associating the network load balancer with network security groups include:

        *  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer.

        *  The network security rules of other resources can reference the network security groups associated with the network load balancer
           to ensure access.

        Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this CreateNetworkLoadBalancerDetails.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this CreateNetworkLoadBalancerDetails.
        An array of network security groups `OCIDs`__ associated with the network load
        balancer.

        During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups.

        The benefits of associating the network load balancer with network security groups include:

        *  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer.

        *  The network security rules of other resources can reference the network security groups associated with the network load balancer
           to ensure access.

        Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this CreateNetworkLoadBalancerDetails.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def listeners(self):
        """
        Gets the listeners of this CreateNetworkLoadBalancerDetails.
        Listeners associated with the network load balancer.


        :return: The listeners of this CreateNetworkLoadBalancerDetails.
        :rtype: dict(str, ListenerDetails)
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """
        Sets the listeners of this CreateNetworkLoadBalancerDetails.
        Listeners associated with the network load balancer.


        :param listeners: The listeners of this CreateNetworkLoadBalancerDetails.
        :type: dict(str, ListenerDetails)
        """
        self._listeners = listeners

    @property
    def backend_sets(self):
        """
        Gets the backend_sets of this CreateNetworkLoadBalancerDetails.
        Backend sets associated with the network load balancer.


        :return: The backend_sets of this CreateNetworkLoadBalancerDetails.
        :rtype: dict(str, BackendSetDetails)
        """
        return self._backend_sets

    @backend_sets.setter
    def backend_sets(self, backend_sets):
        """
        Sets the backend_sets of this CreateNetworkLoadBalancerDetails.
        Backend sets associated with the network load balancer.


        :param backend_sets: The backend_sets of this CreateNetworkLoadBalancerDetails.
        :type: dict(str, BackendSetDetails)
        """
        self._backend_sets = backend_sets

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateNetworkLoadBalancerDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateNetworkLoadBalancerDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateNetworkLoadBalancerDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateNetworkLoadBalancerDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateNetworkLoadBalancerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateNetworkLoadBalancerDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateNetworkLoadBalancerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateNetworkLoadBalancerDetails.
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
