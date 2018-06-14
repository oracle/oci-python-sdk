# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Node(object):
    """
    The properties that define a node.
    """

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "FAILING"
    LIFECYCLE_STATE_FAILING = "FAILING"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new Node object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Node.
        :type id: str

        :param name:
            The value to assign to the name property of this Node.
        :type name: str

        :param availability_domain:
            The value to assign to the availability_domain property of this Node.
        :type availability_domain: str

        :param subnet_id:
            The value to assign to the subnet_id property of this Node.
        :type subnet_id: str

        :param node_pool_id:
            The value to assign to the node_pool_id property of this Node.
        :type node_pool_id: str

        :param public_ip:
            The value to assign to the public_ip property of this Node.
        :type public_ip: str

        :param node_error:
            The value to assign to the node_error property of this Node.
        :type node_error: NodeError

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Node.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILING", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Node.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'availability_domain': 'str',
            'subnet_id': 'str',
            'node_pool_id': 'str',
            'public_ip': 'str',
            'node_error': 'NodeError',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'availability_domain': 'availabilityDomain',
            'subnet_id': 'subnetId',
            'node_pool_id': 'nodePoolId',
            'public_ip': 'publicIp',
            'node_error': 'nodeError',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._name = None
        self._availability_domain = None
        self._subnet_id = None
        self._node_pool_id = None
        self._public_ip = None
        self._node_error = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        Gets the id of this Node.
        The OCID of the compute instance backing this node.


        :return: The id of this Node.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Node.
        The OCID of the compute instance backing this node.


        :param id: The id of this Node.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Node.
        The name of the node.


        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Node.
        The name of the node.


        :param name: The name of this Node.
        :type: str
        """
        self._name = name

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Node.
        The name of the availability domain in which this node is placed.


        :return: The availability_domain of this Node.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Node.
        The name of the availability domain in which this node is placed.


        :param availability_domain: The availability_domain of this Node.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this Node.
        The OCID of the subnet in which this node is placed.


        :return: The subnet_id of this Node.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Node.
        The OCID of the subnet in which this node is placed.


        :param subnet_id: The subnet_id of this Node.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def node_pool_id(self):
        """
        Gets the node_pool_id of this Node.
        The OCID of the node pool to which this node belongs.


        :return: The node_pool_id of this Node.
        :rtype: str
        """
        return self._node_pool_id

    @node_pool_id.setter
    def node_pool_id(self, node_pool_id):
        """
        Sets the node_pool_id of this Node.
        The OCID of the node pool to which this node belongs.


        :param node_pool_id: The node_pool_id of this Node.
        :type: str
        """
        self._node_pool_id = node_pool_id

    @property
    def public_ip(self):
        """
        Gets the public_ip of this Node.
        The public IP address of this node.


        :return: The public_ip of this Node.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """
        Sets the public_ip of this Node.
        The public IP address of this node.


        :param public_ip: The public_ip of this Node.
        :type: str
        """
        self._public_ip = public_ip

    @property
    def node_error(self):
        """
        Gets the node_error of this Node.
        An error that may be associated with the node.


        :return: The node_error of this Node.
        :rtype: NodeError
        """
        return self._node_error

    @node_error.setter
    def node_error(self, node_error):
        """
        Sets the node_error of this Node.
        An error that may be associated with the node.


        :param node_error: The node_error of this Node.
        :type: NodeError
        """
        self._node_error = node_error

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Node.
        The state of the node.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILING", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Node.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Node.
        The state of the node.


        :param lifecycle_state: The lifecycle_state of this Node.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILING", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Node.
        Details about the state of the node.


        :return: The lifecycle_details of this Node.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Node.
        Details about the state of the node.


        :param lifecycle_details: The lifecycle_details of this Node.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
