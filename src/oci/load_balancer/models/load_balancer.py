# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancer(object):
    """
    The properties that define a load balancer. For more information, see
    `Managing a Load Balancer`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    For information about endpoints and signing API requests, see
    `About the API`__. For information about available SDKs and tools, see
    `SDKS and Other Tools`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Balance/Tasks/managingloadbalancer.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/usingapi.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdks.htm
    """

    #: A constant which can be used with the lifecycle_state property of a LoadBalancer.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a LoadBalancer.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a LoadBalancer.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LoadBalancer.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a LoadBalancer.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backend_sets:
            The value to assign to the backend_sets property of this LoadBalancer.
        :type backend_sets: dict(str, BackendSet)

        :param certificates:
            The value to assign to the certificates property of this LoadBalancer.
        :type certificates: dict(str, Certificate)

        :param compartment_id:
            The value to assign to the compartment_id property of this LoadBalancer.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this LoadBalancer.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this LoadBalancer.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LoadBalancer.
        :type freeform_tags: dict(str, str)

        :param hostnames:
            The value to assign to the hostnames property of this LoadBalancer.
        :type hostnames: dict(str, Hostname)

        :param id:
            The value to assign to the id property of this LoadBalancer.
        :type id: str

        :param ip_addresses:
            The value to assign to the ip_addresses property of this LoadBalancer.
        :type ip_addresses: list[IpAddress]

        :param is_private:
            The value to assign to the is_private property of this LoadBalancer.
        :type is_private: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LoadBalancer.
            Allowed values for this property are: "CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param listeners:
            The value to assign to the listeners property of this LoadBalancer.
        :type listeners: dict(str, Listener)

        :param path_route_sets:
            The value to assign to the path_route_sets property of this LoadBalancer.
        :type path_route_sets: dict(str, PathRouteSet)

        :param shape_name:
            The value to assign to the shape_name property of this LoadBalancer.
        :type shape_name: str

        :param subnet_ids:
            The value to assign to the subnet_ids property of this LoadBalancer.
        :type subnet_ids: list[str]

        :param time_created:
            The value to assign to the time_created property of this LoadBalancer.
        :type time_created: datetime

        """
        self.swagger_types = {
            'backend_sets': 'dict(str, BackendSet)',
            'certificates': 'dict(str, Certificate)',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostnames': 'dict(str, Hostname)',
            'id': 'str',
            'ip_addresses': 'list[IpAddress]',
            'is_private': 'bool',
            'lifecycle_state': 'str',
            'listeners': 'dict(str, Listener)',
            'path_route_sets': 'dict(str, PathRouteSet)',
            'shape_name': 'str',
            'subnet_ids': 'list[str]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'backend_sets': 'backendSets',
            'certificates': 'certificates',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'hostnames': 'hostnames',
            'id': 'id',
            'ip_addresses': 'ipAddresses',
            'is_private': 'isPrivate',
            'lifecycle_state': 'lifecycleState',
            'listeners': 'listeners',
            'path_route_sets': 'pathRouteSets',
            'shape_name': 'shapeName',
            'subnet_ids': 'subnetIds',
            'time_created': 'timeCreated'
        }

        self._backend_sets = None
        self._certificates = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._hostnames = None
        self._id = None
        self._ip_addresses = None
        self._is_private = None
        self._lifecycle_state = None
        self._listeners = None
        self._path_route_sets = None
        self._shape_name = None
        self._subnet_ids = None
        self._time_created = None

    @property
    def backend_sets(self):
        """
        Gets the backend_sets of this LoadBalancer.

        :return: The backend_sets of this LoadBalancer.
        :rtype: dict(str, BackendSet)
        """
        return self._backend_sets

    @backend_sets.setter
    def backend_sets(self, backend_sets):
        """
        Sets the backend_sets of this LoadBalancer.

        :param backend_sets: The backend_sets of this LoadBalancer.
        :type: dict(str, BackendSet)
        """
        self._backend_sets = backend_sets

    @property
    def certificates(self):
        """
        Gets the certificates of this LoadBalancer.

        :return: The certificates of this LoadBalancer.
        :rtype: dict(str, Certificate)
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """
        Sets the certificates of this LoadBalancer.

        :param certificates: The certificates of this LoadBalancer.
        :type: dict(str, Certificate)
        """
        self._certificates = certificates

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LoadBalancer.
        The `OCID`__ of the compartment containing the load balancer.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LoadBalancer.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LoadBalancer.
        The `OCID`__ of the compartment containing the load balancer.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LoadBalancer.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LoadBalancer.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this LoadBalancer.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LoadBalancer.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this LoadBalancer.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this LoadBalancer.
        A user-friendly name. It does not have to be unique, and it is changeable.

        Example: `example_load_balancer`


        :return: The display_name of this LoadBalancer.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LoadBalancer.
        A user-friendly name. It does not have to be unique, and it is changeable.

        Example: `example_load_balancer`


        :param display_name: The display_name of this LoadBalancer.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LoadBalancer.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this LoadBalancer.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LoadBalancer.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this LoadBalancer.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def hostnames(self):
        """
        Gets the hostnames of this LoadBalancer.

        :return: The hostnames of this LoadBalancer.
        :rtype: dict(str, Hostname)
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """
        Sets the hostnames of this LoadBalancer.

        :param hostnames: The hostnames of this LoadBalancer.
        :type: dict(str, Hostname)
        """
        self._hostnames = hostnames

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LoadBalancer.
        The `OCID`__ of the load balancer.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The id of this LoadBalancer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LoadBalancer.
        The `OCID`__ of the load balancer.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this LoadBalancer.
        :type: str
        """
        self._id = id

    @property
    def ip_addresses(self):
        """
        Gets the ip_addresses of this LoadBalancer.
        An array of IP addresses.


        :return: The ip_addresses of this LoadBalancer.
        :rtype: list[IpAddress]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this LoadBalancer.
        An array of IP addresses.


        :param ip_addresses: The ip_addresses of this LoadBalancer.
        :type: list[IpAddress]
        """
        self._ip_addresses = ip_addresses

    @property
    def is_private(self):
        """
        Gets the is_private of this LoadBalancer.
        Whether the load balancer has a VCN-local (private) IP address.

        If \"true\", the service assigns a private IP address to the load balancer. The load balancer requires only one subnet
        to host both the primary and secondary load balancers. The private IP address is local to the subnet. The load balancer
        is accessible only from within the VCN that contains the associated subnet, or as further restricted by your security
        list rules. The load balancer can route traffic to any backend server that is reachable from the VCN.

        For a private load balancer, both the primary and secondary load balancer hosts are within the same Availability Domain.

        If \"false\", the service assigns a public IP address to the load balancer. A load balancer with a public IP address
        requires two subnets, each in a different Availability Domain. One subnet hosts the primary load balancer and the other
        hosts the secondary (standby) load balancer. A public load balancer is accessible from the internet, depending on your
        VCN's `security list rules`__.

        Example: `true`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/securitylists.htm


        :return: The is_private of this LoadBalancer.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """
        Sets the is_private of this LoadBalancer.
        Whether the load balancer has a VCN-local (private) IP address.

        If \"true\", the service assigns a private IP address to the load balancer. The load balancer requires only one subnet
        to host both the primary and secondary load balancers. The private IP address is local to the subnet. The load balancer
        is accessible only from within the VCN that contains the associated subnet, or as further restricted by your security
        list rules. The load balancer can route traffic to any backend server that is reachable from the VCN.

        For a private load balancer, both the primary and secondary load balancer hosts are within the same Availability Domain.

        If \"false\", the service assigns a public IP address to the load balancer. A load balancer with a public IP address
        requires two subnets, each in a different Availability Domain. One subnet hosts the primary load balancer and the other
        hosts the secondary (standby) load balancer. A public load balancer is accessible from the internet, depending on your
        VCN's `security list rules`__.

        Example: `true`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/securitylists.htm


        :param is_private: The is_private of this LoadBalancer.
        :type: bool
        """
        self._is_private = is_private

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this LoadBalancer.
        The current state of the load balancer.

        Allowed values for this property are: "CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LoadBalancer.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LoadBalancer.
        The current state of the load balancer.


        :param lifecycle_state: The lifecycle_state of this LoadBalancer.
        :type: str
        """
        allowed_values = ["CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def listeners(self):
        """
        Gets the listeners of this LoadBalancer.

        :return: The listeners of this LoadBalancer.
        :rtype: dict(str, Listener)
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """
        Sets the listeners of this LoadBalancer.

        :param listeners: The listeners of this LoadBalancer.
        :type: dict(str, Listener)
        """
        self._listeners = listeners

    @property
    def path_route_sets(self):
        """
        Gets the path_route_sets of this LoadBalancer.

        :return: The path_route_sets of this LoadBalancer.
        :rtype: dict(str, PathRouteSet)
        """
        return self._path_route_sets

    @path_route_sets.setter
    def path_route_sets(self, path_route_sets):
        """
        Sets the path_route_sets of this LoadBalancer.

        :param path_route_sets: The path_route_sets of this LoadBalancer.
        :type: dict(str, PathRouteSet)
        """
        self._path_route_sets = path_route_sets

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this LoadBalancer.
        A template that determines the total pre-provisioned bandwidth (ingress plus egress).
        To get a list of available shapes, use the :func:`list_shapes`
        operation.

        Example: `100Mbps`


        :return: The shape_name of this LoadBalancer.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this LoadBalancer.
        A template that determines the total pre-provisioned bandwidth (ingress plus egress).
        To get a list of available shapes, use the :func:`list_shapes`
        operation.

        Example: `100Mbps`


        :param shape_name: The shape_name of this LoadBalancer.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def subnet_ids(self):
        """
        Gets the subnet_ids of this LoadBalancer.
        An array of subnet `OCIDs`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_ids of this LoadBalancer.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this LoadBalancer.
        An array of subnet `OCIDs`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param subnet_ids: The subnet_ids of this LoadBalancer.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LoadBalancer.
        The date and time the load balancer was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this LoadBalancer.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LoadBalancer.
        The date and time the load balancer was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this LoadBalancer.
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
