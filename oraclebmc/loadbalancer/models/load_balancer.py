# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class LoadBalancer(object):

    def __init__(self):

        self.swagger_types = {
            'backend_sets': 'dict(str, BackendSet)',
            'certificates': 'dict(str, Certificate)',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'ip_addresses': 'list[IpAddress]',
            'is_private': 'bool',
            'lifecycle_state': 'str',
            'listeners': 'dict(str, Listener)',
            'shape_name': 'str',
            'subnet_ids': 'list[str]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'backend_sets': 'backendSets',
            'certificates': 'certificates',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'ip_addresses': 'ipAddresses',
            'is_private': 'isPrivate',
            'lifecycle_state': 'lifecycleState',
            'listeners': 'listeners',
            'shape_name': 'shapeName',
            'subnet_ids': 'subnetIds',
            'time_created': 'timeCreated'
        }

        self._backend_sets = None
        self._certificates = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._ip_addresses = None
        self._is_private = None
        self._lifecycle_state = None
        self._listeners = None
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
        Gets the compartment_id of this LoadBalancer.
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
    def display_name(self):
        """
        Gets the display_name of this LoadBalancer.
        A user-friendly name. It does not have to be unique, and it is changeable.

        Example: `My load balancer`


        :return: The display_name of this LoadBalancer.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LoadBalancer.
        A user-friendly name. It does not have to be unique, and it is changeable.

        Example: `My load balancer`


        :param display_name: The display_name of this LoadBalancer.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this LoadBalancer.
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
        hosts the secondary (stand-by) load balancer. A public load balancer is accessible from the internet, depending on your
        VCN's `security list rules`__.

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
        hosts the secondary (stand-by) load balancer. A public load balancer is accessible from the internet, depending on your
        VCN's `security list rules`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/securitylists.htm


        :param is_private: The is_private of this LoadBalancer.
        :type: bool
        """
        self._is_private = is_private

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this LoadBalancer.
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

        :param lifecycle_state: The lifecycle_state of this LoadBalancer.
        :type: str
        """
        allowed_values = ["CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED"]
        if lifecycle_state not in allowed_values:
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
    def shape_name(self):
        """
        Gets the shape_name of this LoadBalancer.
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
        Gets the time_created of this LoadBalancer.
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
