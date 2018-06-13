# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Cluster(object):
    """
    A Kubernetes cluster.
    """

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new Cluster object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Cluster.
        :type id: str

        :param name:
            The value to assign to the name property of this Cluster.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Cluster.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this Cluster.
        :type vcn_id: str

        :param kubernetes_version:
            The value to assign to the kubernetes_version property of this Cluster.
        :type kubernetes_version: str

        :param options:
            The value to assign to the options property of this Cluster.
        :type options: ClusterCreateOptions

        :param metadata:
            The value to assign to the metadata property of this Cluster.
        :type metadata: ClusterMetadata

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Cluster.
            Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Cluster.
        :type lifecycle_details: str

        :param endpoints:
            The value to assign to the endpoints property of this Cluster.
        :type endpoints: ClusterEndpoints

        :param available_kubernetes_upgrades:
            The value to assign to the available_kubernetes_upgrades property of this Cluster.
        :type available_kubernetes_upgrades: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'vcn_id': 'str',
            'kubernetes_version': 'str',
            'options': 'ClusterCreateOptions',
            'metadata': 'ClusterMetadata',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'endpoints': 'ClusterEndpoints',
            'available_kubernetes_upgrades': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'kubernetes_version': 'kubernetesVersion',
            'options': 'options',
            'metadata': 'metadata',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'endpoints': 'endpoints',
            'available_kubernetes_upgrades': 'availableKubernetesUpgrades'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._vcn_id = None
        self._kubernetes_version = None
        self._options = None
        self._metadata = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._endpoints = None
        self._available_kubernetes_upgrades = None

    @property
    def id(self):
        """
        Gets the id of this Cluster.
        The OCID of the cluster.


        :return: The id of this Cluster.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Cluster.
        The OCID of the cluster.


        :param id: The id of this Cluster.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Cluster.
        The name of the cluster.


        :return: The name of this Cluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Cluster.
        The name of the cluster.


        :param name: The name of this Cluster.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Cluster.
        The OCID of the compartment in which the cluster exists.


        :return: The compartment_id of this Cluster.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Cluster.
        The OCID of the compartment in which the cluster exists.


        :param compartment_id: The compartment_id of this Cluster.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this Cluster.
        The OCID of the virtual cloud network (VCN) in which the cluster exists.


        :return: The vcn_id of this Cluster.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this Cluster.
        The OCID of the virtual cloud network (VCN) in which the cluster exists.


        :param vcn_id: The vcn_id of this Cluster.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def kubernetes_version(self):
        """
        Gets the kubernetes_version of this Cluster.
        The version of Kubernetes running on the cluster masters.


        :return: The kubernetes_version of this Cluster.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        """
        Sets the kubernetes_version of this Cluster.
        The version of Kubernetes running on the cluster masters.


        :param kubernetes_version: The kubernetes_version of this Cluster.
        :type: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def options(self):
        """
        Gets the options of this Cluster.
        Optional attributes for the cluster.


        :return: The options of this Cluster.
        :rtype: ClusterCreateOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this Cluster.
        Optional attributes for the cluster.


        :param options: The options of this Cluster.
        :type: ClusterCreateOptions
        """
        self._options = options

    @property
    def metadata(self):
        """
        Gets the metadata of this Cluster.
        Metadata about the cluster.


        :return: The metadata of this Cluster.
        :rtype: ClusterMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Cluster.
        Metadata about the cluster.


        :param metadata: The metadata of this Cluster.
        :type: ClusterMetadata
        """
        self._metadata = metadata

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Cluster.
        The state of the cluster masters.

        Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Cluster.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Cluster.
        The state of the cluster masters.


        :param lifecycle_state: The lifecycle_state of this Cluster.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Cluster.
        Details about the state of the cluster masters.


        :return: The lifecycle_details of this Cluster.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Cluster.
        Details about the state of the cluster masters.


        :param lifecycle_details: The lifecycle_details of this Cluster.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def endpoints(self):
        """
        Gets the endpoints of this Cluster.
        Endpoints served up by the cluster masters.


        :return: The endpoints of this Cluster.
        :rtype: ClusterEndpoints
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this Cluster.
        Endpoints served up by the cluster masters.


        :param endpoints: The endpoints of this Cluster.
        :type: ClusterEndpoints
        """
        self._endpoints = endpoints

    @property
    def available_kubernetes_upgrades(self):
        """
        Gets the available_kubernetes_upgrades of this Cluster.
        Available Kubernetes versions to which the clusters masters may be upgraded.


        :return: The available_kubernetes_upgrades of this Cluster.
        :rtype: list[str]
        """
        return self._available_kubernetes_upgrades

    @available_kubernetes_upgrades.setter
    def available_kubernetes_upgrades(self, available_kubernetes_upgrades):
        """
        Sets the available_kubernetes_upgrades of this Cluster.
        Available Kubernetes versions to which the clusters masters may be upgraded.


        :param available_kubernetes_upgrades: The available_kubernetes_upgrades of this Cluster.
        :type: list[str]
        """
        self._available_kubernetes_upgrades = available_kubernetes_upgrades

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
