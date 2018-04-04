# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateLoadBalancerDetails(object):
    """
    The configuration details for creating a load balancer.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateLoadBalancerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backend_sets:
            The value to assign to the backend_sets property of this CreateLoadBalancerDetails.
        :type backend_sets: dict(str, BackendSetDetails)

        :param certificates:
            The value to assign to the certificates property of this CreateLoadBalancerDetails.
        :type certificates: dict(str, CertificateDetails)

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateLoadBalancerDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateLoadBalancerDetails.
        :type display_name: str

        :param is_private:
            The value to assign to the is_private property of this CreateLoadBalancerDetails.
        :type is_private: bool

        :param listeners:
            The value to assign to the listeners property of this CreateLoadBalancerDetails.
        :type listeners: dict(str, ListenerDetails)

        :param path_route_sets:
            The value to assign to the path_route_sets property of this CreateLoadBalancerDetails.
        :type path_route_sets: dict(str, PathRouteSetDetails)

        :param shape_name:
            The value to assign to the shape_name property of this CreateLoadBalancerDetails.
        :type shape_name: str

        :param subnet_ids:
            The value to assign to the subnet_ids property of this CreateLoadBalancerDetails.
        :type subnet_ids: list[str]

        """
        self.swagger_types = {
            'backend_sets': 'dict(str, BackendSetDetails)',
            'certificates': 'dict(str, CertificateDetails)',
            'compartment_id': 'str',
            'display_name': 'str',
            'is_private': 'bool',
            'listeners': 'dict(str, ListenerDetails)',
            'path_route_sets': 'dict(str, PathRouteSetDetails)',
            'shape_name': 'str',
            'subnet_ids': 'list[str]'
        }

        self.attribute_map = {
            'backend_sets': 'backendSets',
            'certificates': 'certificates',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'is_private': 'isPrivate',
            'listeners': 'listeners',
            'path_route_sets': 'pathRouteSets',
            'shape_name': 'shapeName',
            'subnet_ids': 'subnetIds'
        }

        self._backend_sets = None
        self._certificates = None
        self._compartment_id = None
        self._display_name = None
        self._is_private = None
        self._listeners = None
        self._path_route_sets = None
        self._shape_name = None
        self._subnet_ids = None

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
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateLoadBalancerDetails.
        The `OCID`__ of the compartment in which to create the load balancer.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateLoadBalancerDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateLoadBalancerDetails.
        The `OCID`__ of the compartment in which to create the load balancer.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


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

        Example: `My load balancer`


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

        Example: `My load balancer`


        :param display_name: The display_name of this CreateLoadBalancerDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_private(self):
        """
        Gets the is_private of this CreateLoadBalancerDetails.
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

        Example: `false`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/securitylists.htm


        :return: The is_private of this CreateLoadBalancerDetails.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """
        Sets the is_private of this CreateLoadBalancerDetails.
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

        Example: `false`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/securitylists.htm


        :param is_private: The is_private of this CreateLoadBalancerDetails.
        :type: bool
        """
        self._is_private = is_private

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
    def subnet_ids(self):
        """
        **[Required]** Gets the subnet_ids of this CreateLoadBalancerDetails.
        An array of subnet `OCIDs`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_ids of this CreateLoadBalancerDetails.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this CreateLoadBalancerDetails.
        An array of subnet `OCIDs`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param subnet_ids: The subnet_ids of this CreateLoadBalancerDetails.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
