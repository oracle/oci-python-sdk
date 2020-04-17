# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateLoadBalancerDetails(object):
    """
    The configuration details for creating a load balancer.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the ip_mode property of a CreateLoadBalancerDetails.
    #: This constant has a value of "IPV4"
    IP_MODE_IPV4 = "IPV4"

    #: A constant which can be used with the ip_mode property of a CreateLoadBalancerDetails.
    #: This constant has a value of "IPV6"
    IP_MODE_IPV6 = "IPV6"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateLoadBalancerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateLoadBalancerDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateLoadBalancerDetails.
        :type display_name: str

        :param shape_name:
            The value to assign to the shape_name property of this CreateLoadBalancerDetails.
        :type shape_name: str

        :param is_private:
            The value to assign to the is_private property of this CreateLoadBalancerDetails.
        :type is_private: bool

        :param ip_mode:
            The value to assign to the ip_mode property of this CreateLoadBalancerDetails.
            Allowed values for this property are: "IPV4", "IPV6"
        :type ip_mode: str

        :param listeners:
            The value to assign to the listeners property of this CreateLoadBalancerDetails.
        :type listeners: dict(str, ListenerDetails)

        :param hostnames:
            The value to assign to the hostnames property of this CreateLoadBalancerDetails.
        :type hostnames: dict(str, HostnameDetails)

        :param backend_sets:
            The value to assign to the backend_sets property of this CreateLoadBalancerDetails.
        :type backend_sets: dict(str, BackendSetDetails)

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this CreateLoadBalancerDetails.
        :type network_security_group_ids: list[str]

        :param subnet_ids:
            The value to assign to the subnet_ids property of this CreateLoadBalancerDetails.
        :type subnet_ids: list[str]

        :param certificates:
            The value to assign to the certificates property of this CreateLoadBalancerDetails.
        :type certificates: dict(str, CertificateDetails)

        :param path_route_sets:
            The value to assign to the path_route_sets property of this CreateLoadBalancerDetails.
        :type path_route_sets: dict(str, PathRouteSetDetails)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateLoadBalancerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateLoadBalancerDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param rule_sets:
            The value to assign to the rule_sets property of this CreateLoadBalancerDetails.
        :type rule_sets: dict(str, RuleSetDetails)

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'shape_name': 'str',
            'is_private': 'bool',
            'ip_mode': 'str',
            'listeners': 'dict(str, ListenerDetails)',
            'hostnames': 'dict(str, HostnameDetails)',
            'backend_sets': 'dict(str, BackendSetDetails)',
            'network_security_group_ids': 'list[str]',
            'subnet_ids': 'list[str]',
            'certificates': 'dict(str, CertificateDetails)',
            'path_route_sets': 'dict(str, PathRouteSetDetails)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'rule_sets': 'dict(str, RuleSetDetails)'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'shape_name': 'shapeName',
            'is_private': 'isPrivate',
            'ip_mode': 'ipMode',
            'listeners': 'listeners',
            'hostnames': 'hostnames',
            'backend_sets': 'backendSets',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'subnet_ids': 'subnetIds',
            'certificates': 'certificates',
            'path_route_sets': 'pathRouteSets',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'rule_sets': 'ruleSets'
        }

        self._compartment_id = None
        self._display_name = None
        self._shape_name = None
        self._is_private = None
        self._ip_mode = None
        self._listeners = None
        self._hostnames = None
        self._backend_sets = None
        self._network_security_group_ids = None
        self._subnet_ids = None
        self._certificates = None
        self._path_route_sets = None
        self._freeform_tags = None
        self._defined_tags = None
        self._rule_sets = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateLoadBalancerDetails.
        The `OCID`__ of the compartment in which to create the load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateLoadBalancerDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateLoadBalancerDetails.
        The `OCID`__ of the compartment in which to create the load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateLoadBalancerDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateLoadBalancerDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `example_load_balancer`


        :return: The display_name of this CreateLoadBalancerDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateLoadBalancerDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `example_load_balancer`


        :param display_name: The display_name of this CreateLoadBalancerDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this CreateLoadBalancerDetails.
        A template that determines the total pre-provisioned bandwidth (ingress plus egress).
        To get a list of available shapes, use the :func:`list_shapes`
        operation.

        Example: `100Mbps`


        :return: The shape_name of this CreateLoadBalancerDetails.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this CreateLoadBalancerDetails.
        A template that determines the total pre-provisioned bandwidth (ingress plus egress).
        To get a list of available shapes, use the :func:`list_shapes`
        operation.

        Example: `100Mbps`


        :param shape_name: The shape_name of this CreateLoadBalancerDetails.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def is_private(self):
        """
        Gets the is_private of this CreateLoadBalancerDetails.
        Whether the load balancer has a VCN-local (private) IP address.

        If \"true\", the service assigns a private IP address to the load balancer.

        If \"false\", the service assigns a public IP address to the load balancer.

        A public load balancer is accessible from the internet, depending on your VCN's
        `security list rules`__. For more information about public and
        private load balancers, see `How Load Balancing Works`__.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-load-balancing-works


        :return: The is_private of this CreateLoadBalancerDetails.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """
        Sets the is_private of this CreateLoadBalancerDetails.
        Whether the load balancer has a VCN-local (private) IP address.

        If \"true\", the service assigns a private IP address to the load balancer.

        If \"false\", the service assigns a public IP address to the load balancer.

        A public load balancer is accessible from the internet, depending on your VCN's
        `security list rules`__. For more information about public and
        private load balancers, see `How Load Balancing Works`__.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-load-balancing-works


        :param is_private: The is_private of this CreateLoadBalancerDetails.
        :type: bool
        """
        self._is_private = is_private

    @property
    def ip_mode(self):
        """
        Gets the ip_mode of this CreateLoadBalancerDetails.
        Whether the load balancer has an IPv4 or IPv6 IP address.

        If \"IPV4\", the service assigns an IPv4 address and the load balancer supports IPv4 traffic.

        If \"IPV6\", the service assigns an IPv6 address and the load balancer supports IPv6 traffic.

        Example: \"ipMode\":\"IPV6\"

        Allowed values for this property are: "IPV4", "IPV6"


        :return: The ip_mode of this CreateLoadBalancerDetails.
        :rtype: str
        """
        return self._ip_mode

    @ip_mode.setter
    def ip_mode(self, ip_mode):
        """
        Sets the ip_mode of this CreateLoadBalancerDetails.
        Whether the load balancer has an IPv4 or IPv6 IP address.

        If \"IPV4\", the service assigns an IPv4 address and the load balancer supports IPv4 traffic.

        If \"IPV6\", the service assigns an IPv6 address and the load balancer supports IPv6 traffic.

        Example: \"ipMode\":\"IPV6\"


        :param ip_mode: The ip_mode of this CreateLoadBalancerDetails.
        :type: str
        """
        allowed_values = ["IPV4", "IPV6"]
        if not value_allowed_none_or_none_sentinel(ip_mode, allowed_values):
            raise ValueError(
                "Invalid value for `ip_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._ip_mode = ip_mode

    @property
    def listeners(self):
        """
        Gets the listeners of this CreateLoadBalancerDetails.

        :return: The listeners of this CreateLoadBalancerDetails.
        :rtype: dict(str, ListenerDetails)
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """
        Sets the listeners of this CreateLoadBalancerDetails.

        :param listeners: The listeners of this CreateLoadBalancerDetails.
        :type: dict(str, ListenerDetails)
        """
        self._listeners = listeners

    @property
    def hostnames(self):
        """
        Gets the hostnames of this CreateLoadBalancerDetails.

        :return: The hostnames of this CreateLoadBalancerDetails.
        :rtype: dict(str, HostnameDetails)
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """
        Sets the hostnames of this CreateLoadBalancerDetails.

        :param hostnames: The hostnames of this CreateLoadBalancerDetails.
        :type: dict(str, HostnameDetails)
        """
        self._hostnames = hostnames

    @property
    def backend_sets(self):
        """
        Gets the backend_sets of this CreateLoadBalancerDetails.

        :return: The backend_sets of this CreateLoadBalancerDetails.
        :rtype: dict(str, BackendSetDetails)
        """
        return self._backend_sets

    @backend_sets.setter
    def backend_sets(self, backend_sets):
        """
        Sets the backend_sets of this CreateLoadBalancerDetails.

        :param backend_sets: The backend_sets of this CreateLoadBalancerDetails.
        :type: dict(str, BackendSetDetails)
        """
        self._backend_sets = backend_sets

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this CreateLoadBalancerDetails.
        An array of NSG `OCIDs`__ associated with this load balancer.

        During the load balancer's creation, the service adds the new load balancer to the specified NSGs.

        The benefits of using NSGs with the load balancer include:

        *  NSGs define network security rules to govern ingress and egress traffic for the load balancer.

        *  The network security rules of other resources can reference the NSGs associated with the load balancer
           to ensure access.

        Example: `[\"ocid1.nsg.oc1.phx.unique_ID\"]`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this CreateLoadBalancerDetails.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this CreateLoadBalancerDetails.
        An array of NSG `OCIDs`__ associated with this load balancer.

        During the load balancer's creation, the service adds the new load balancer to the specified NSGs.

        The benefits of using NSGs with the load balancer include:

        *  NSGs define network security rules to govern ingress and egress traffic for the load balancer.

        *  The network security rules of other resources can reference the NSGs associated with the load balancer
           to ensure access.

        Example: `[\"ocid1.nsg.oc1.phx.unique_ID\"]`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this CreateLoadBalancerDetails.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def subnet_ids(self):
        """
        **[Required]** Gets the subnet_ids of this CreateLoadBalancerDetails.
        An array of subnet `OCIDs`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_ids of this CreateLoadBalancerDetails.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this CreateLoadBalancerDetails.
        An array of subnet `OCIDs`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_ids: The subnet_ids of this CreateLoadBalancerDetails.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def certificates(self):
        """
        Gets the certificates of this CreateLoadBalancerDetails.

        :return: The certificates of this CreateLoadBalancerDetails.
        :rtype: dict(str, CertificateDetails)
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """
        Sets the certificates of this CreateLoadBalancerDetails.

        :param certificates: The certificates of this CreateLoadBalancerDetails.
        :type: dict(str, CertificateDetails)
        """
        self._certificates = certificates

    @property
    def path_route_sets(self):
        """
        Gets the path_route_sets of this CreateLoadBalancerDetails.

        :return: The path_route_sets of this CreateLoadBalancerDetails.
        :rtype: dict(str, PathRouteSetDetails)
        """
        return self._path_route_sets

    @path_route_sets.setter
    def path_route_sets(self, path_route_sets):
        """
        Sets the path_route_sets of this CreateLoadBalancerDetails.

        :param path_route_sets: The path_route_sets of this CreateLoadBalancerDetails.
        :type: dict(str, PathRouteSetDetails)
        """
        self._path_route_sets = path_route_sets

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateLoadBalancerDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateLoadBalancerDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateLoadBalancerDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateLoadBalancerDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateLoadBalancerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateLoadBalancerDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateLoadBalancerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateLoadBalancerDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def rule_sets(self):
        """
        Gets the rule_sets of this CreateLoadBalancerDetails.

        :return: The rule_sets of this CreateLoadBalancerDetails.
        :rtype: dict(str, RuleSetDetails)
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        """
        Sets the rule_sets of this CreateLoadBalancerDetails.

        :param rule_sets: The rule_sets of this CreateLoadBalancerDetails.
        :type: dict(str, RuleSetDetails)
        """
        self._rule_sets = rule_sets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
