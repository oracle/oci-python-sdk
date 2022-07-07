# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Cluster(object):
    """
    A Kubernetes cluster. Avoid entering confidential information.
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

        :param endpoint_config:
            The value to assign to the endpoint_config property of this Cluster.
        :type endpoint_config: oci.container_engine.models.ClusterEndpointConfig

        :param vcn_id:
            The value to assign to the vcn_id property of this Cluster.
        :type vcn_id: str

        :param kubernetes_version:
            The value to assign to the kubernetes_version property of this Cluster.
        :type kubernetes_version: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this Cluster.
        :type kms_key_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Cluster.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Cluster.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Cluster.
        :type system_tags: dict(str, dict(str, object))

        :param options:
            The value to assign to the options property of this Cluster.
        :type options: oci.container_engine.models.ClusterCreateOptions

        :param metadata:
            The value to assign to the metadata property of this Cluster.
        :type metadata: oci.container_engine.models.ClusterMetadata

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
        :type endpoints: oci.container_engine.models.ClusterEndpoints

        :param available_kubernetes_upgrades:
            The value to assign to the available_kubernetes_upgrades property of this Cluster.
        :type available_kubernetes_upgrades: list[str]

        :param image_policy_config:
            The value to assign to the image_policy_config property of this Cluster.
        :type image_policy_config: oci.container_engine.models.ImagePolicyConfig

        :param cluster_pod_network_options:
            The value to assign to the cluster_pod_network_options property of this Cluster.
        :type cluster_pod_network_options: list[oci.container_engine.models.ClusterPodNetworkOptionDetails]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'endpoint_config': 'ClusterEndpointConfig',
            'vcn_id': 'str',
            'kubernetes_version': 'str',
            'kms_key_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'options': 'ClusterCreateOptions',
            'metadata': 'ClusterMetadata',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'endpoints': 'ClusterEndpoints',
            'available_kubernetes_upgrades': 'list[str]',
            'image_policy_config': 'ImagePolicyConfig',
            'cluster_pod_network_options': 'list[ClusterPodNetworkOptionDetails]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'endpoint_config': 'endpointConfig',
            'vcn_id': 'vcnId',
            'kubernetes_version': 'kubernetesVersion',
            'kms_key_id': 'kmsKeyId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'options': 'options',
            'metadata': 'metadata',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'endpoints': 'endpoints',
            'available_kubernetes_upgrades': 'availableKubernetesUpgrades',
            'image_policy_config': 'imagePolicyConfig',
            'cluster_pod_network_options': 'clusterPodNetworkOptions'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._endpoint_config = None
        self._vcn_id = None
        self._kubernetes_version = None
        self._kms_key_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._options = None
        self._metadata = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._endpoints = None
        self._available_kubernetes_upgrades = None
        self._image_policy_config = None
        self._cluster_pod_network_options = None

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
    def endpoint_config(self):
        """
        Gets the endpoint_config of this Cluster.
        The network configuration for access to the Cluster control plane.


        :return: The endpoint_config of this Cluster.
        :rtype: oci.container_engine.models.ClusterEndpointConfig
        """
        return self._endpoint_config

    @endpoint_config.setter
    def endpoint_config(self, endpoint_config):
        """
        Sets the endpoint_config of this Cluster.
        The network configuration for access to the Cluster control plane.


        :param endpoint_config: The endpoint_config of this Cluster.
        :type: oci.container_engine.models.ClusterEndpointConfig
        """
        self._endpoint_config = endpoint_config

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
    def kms_key_id(self):
        """
        Gets the kms_key_id of this Cluster.
        The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption.


        :return: The kms_key_id of this Cluster.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this Cluster.
        The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption.


        :param kms_key_id: The kms_key_id of this Cluster.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Cluster.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Cluster.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Cluster.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Cluster.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Cluster.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Cluster.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Cluster.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Cluster.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Cluster.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Cluster.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Cluster.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Cluster.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def options(self):
        """
        Gets the options of this Cluster.
        Optional attributes for the cluster.


        :return: The options of this Cluster.
        :rtype: oci.container_engine.models.ClusterCreateOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this Cluster.
        Optional attributes for the cluster.


        :param options: The options of this Cluster.
        :type: oci.container_engine.models.ClusterCreateOptions
        """
        self._options = options

    @property
    def metadata(self):
        """
        Gets the metadata of this Cluster.
        Metadata about the cluster.


        :return: The metadata of this Cluster.
        :rtype: oci.container_engine.models.ClusterMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Cluster.
        Metadata about the cluster.


        :param metadata: The metadata of this Cluster.
        :type: oci.container_engine.models.ClusterMetadata
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
        :rtype: oci.container_engine.models.ClusterEndpoints
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this Cluster.
        Endpoints served up by the cluster masters.


        :param endpoints: The endpoints of this Cluster.
        :type: oci.container_engine.models.ClusterEndpoints
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

    @property
    def image_policy_config(self):
        """
        Gets the image_policy_config of this Cluster.
        The image verification policy for signature validation.


        :return: The image_policy_config of this Cluster.
        :rtype: oci.container_engine.models.ImagePolicyConfig
        """
        return self._image_policy_config

    @image_policy_config.setter
    def image_policy_config(self, image_policy_config):
        """
        Sets the image_policy_config of this Cluster.
        The image verification policy for signature validation.


        :param image_policy_config: The image_policy_config of this Cluster.
        :type: oci.container_engine.models.ImagePolicyConfig
        """
        self._image_policy_config = image_policy_config

    @property
    def cluster_pod_network_options(self):
        """
        Gets the cluster_pod_network_options of this Cluster.
        Available CNIs and network options for existing and new node pools of the cluster


        :return: The cluster_pod_network_options of this Cluster.
        :rtype: list[oci.container_engine.models.ClusterPodNetworkOptionDetails]
        """
        return self._cluster_pod_network_options

    @cluster_pod_network_options.setter
    def cluster_pod_network_options(self, cluster_pod_network_options):
        """
        Sets the cluster_pod_network_options of this Cluster.
        Available CNIs and network options for existing and new node pools of the cluster


        :param cluster_pod_network_options: The cluster_pod_network_options of this Cluster.
        :type: list[oci.container_engine.models.ClusterPodNetworkOptionDetails]
        """
        self._cluster_pod_network_options = cluster_pod_network_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
