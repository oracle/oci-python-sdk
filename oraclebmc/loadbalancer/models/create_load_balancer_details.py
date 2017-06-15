# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateLoadBalancerDetails(object):

    def __init__(self):

        self.swagger_types = {
            'backend_sets': 'dict(str, BackendSetDetails)',
            'certificates': 'dict(str, CertificateDetails)',
            'compartment_id': 'str',
            'display_name': 'str',
            'is_private': 'bool',
            'listeners': 'dict(str, ListenerDetails)',
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
            'shape_name': 'shapeName',
            'subnet_ids': 'subnetIds'
        }

        self._backend_sets = None
        self._certificates = None
        self._compartment_id = None
        self._display_name = None
        self._is_private = None
        self._listeners = None
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
        Gets the compartment_id of this CreateLoadBalancerDetails.
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
        Gets the display_name of this CreateLoadBalancerDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.

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
        hosts the secondary (stand-by) load balancer. A public load balancer is accessible from the internet, depending on your
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
        hosts the secondary (stand-by) load balancer. A public load balancer is accessible from the internet, depending on your
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
    def shape_name(self):
        """
        Gets the shape_name of this CreateLoadBalancerDetails.
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
        Gets the subnet_ids of this CreateLoadBalancerDetails.
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
