# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlockchainPlatform(object):
    """
    Blockchain Platform Instance Description.
    """

    #: A constant which can be used with the platform_role property of a BlockchainPlatform.
    #: This constant has a value of "FOUNDER"
    PLATFORM_ROLE_FOUNDER = "FOUNDER"

    #: A constant which can be used with the platform_role property of a BlockchainPlatform.
    #: This constant has a value of "PARTICIPANT"
    PLATFORM_ROLE_PARTICIPANT = "PARTICIPANT"

    #: A constant which can be used with the compute_shape property of a BlockchainPlatform.
    #: This constant has a value of "STANDARD"
    COMPUTE_SHAPE_STANDARD = "STANDARD"

    #: A constant which can be used with the compute_shape property of a BlockchainPlatform.
    #: This constant has a value of "ENTERPRISE_SMALL"
    COMPUTE_SHAPE_ENTERPRISE_SMALL = "ENTERPRISE_SMALL"

    #: A constant which can be used with the compute_shape property of a BlockchainPlatform.
    #: This constant has a value of "ENTERPRISE_MEDIUM"
    COMPUTE_SHAPE_ENTERPRISE_MEDIUM = "ENTERPRISE_MEDIUM"

    #: A constant which can be used with the compute_shape property of a BlockchainPlatform.
    #: This constant has a value of "ENTERPRISE_LARGE"
    COMPUTE_SHAPE_ENTERPRISE_LARGE = "ENTERPRISE_LARGE"

    #: A constant which can be used with the compute_shape property of a BlockchainPlatform.
    #: This constant has a value of "ENTERPRISE_EXTRA_LARGE"
    COMPUTE_SHAPE_ENTERPRISE_EXTRA_LARGE = "ENTERPRISE_EXTRA_LARGE"

    #: A constant which can be used with the compute_shape property of a BlockchainPlatform.
    #: This constant has a value of "ENTERPRISE_CUSTOM"
    COMPUTE_SHAPE_ENTERPRISE_CUSTOM = "ENTERPRISE_CUSTOM"

    #: A constant which can be used with the platform_shape_type property of a BlockchainPlatform.
    #: This constant has a value of "DEFAULT"
    PLATFORM_SHAPE_TYPE_DEFAULT = "DEFAULT"

    #: A constant which can be used with the platform_shape_type property of a BlockchainPlatform.
    #: This constant has a value of "CUSTOM"
    PLATFORM_SHAPE_TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the load_balancer_shape property of a BlockchainPlatform.
    #: This constant has a value of "LB_100_MBPS"
    LOAD_BALANCER_SHAPE_LB_100_MBPS = "LB_100_MBPS"

    #: A constant which can be used with the load_balancer_shape property of a BlockchainPlatform.
    #: This constant has a value of "LB_400_MBPS"
    LOAD_BALANCER_SHAPE_LB_400_MBPS = "LB_400_MBPS"

    #: A constant which can be used with the lifecycle_state property of a BlockchainPlatform.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a BlockchainPlatform.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a BlockchainPlatform.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BlockchainPlatform.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a BlockchainPlatform.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a BlockchainPlatform.
    #: This constant has a value of "SCALING"
    LIFECYCLE_STATE_SCALING = "SCALING"

    #: A constant which can be used with the lifecycle_state property of a BlockchainPlatform.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BlockchainPlatform.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new BlockchainPlatform object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BlockchainPlatform.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this BlockchainPlatform.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BlockchainPlatform.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this BlockchainPlatform.
        :type description: str

        :param is_byol:
            The value to assign to the is_byol property of this BlockchainPlatform.
        :type is_byol: bool

        :param time_created:
            The value to assign to the time_created property of this BlockchainPlatform.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BlockchainPlatform.
        :type time_updated: datetime

        :param service_version:
            The value to assign to the service_version property of this BlockchainPlatform.
        :type service_version: str

        :param platform_role:
            The value to assign to the platform_role property of this BlockchainPlatform.
            Allowed values for this property are: "FOUNDER", "PARTICIPANT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_role: str

        :param compute_shape:
            The value to assign to the compute_shape property of this BlockchainPlatform.
            Allowed values for this property are: "STANDARD", "ENTERPRISE_SMALL", "ENTERPRISE_MEDIUM", "ENTERPRISE_LARGE", "ENTERPRISE_EXTRA_LARGE", "ENTERPRISE_CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type compute_shape: str

        :param platform_shape_type:
            The value to assign to the platform_shape_type property of this BlockchainPlatform.
            Allowed values for this property are: "DEFAULT", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_shape_type: str

        :param load_balancer_shape:
            The value to assign to the load_balancer_shape property of this BlockchainPlatform.
            Allowed values for this property are: "LB_100_MBPS", "LB_400_MBPS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type load_balancer_shape: str

        :param service_endpoint:
            The value to assign to the service_endpoint property of this BlockchainPlatform.
        :type service_endpoint: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BlockchainPlatform.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "SCALING", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this BlockchainPlatform.
        :type lifecycle_details: str

        :param storage_size_in_tbs:
            The value to assign to the storage_size_in_tbs property of this BlockchainPlatform.
        :type storage_size_in_tbs: float

        :param storage_used_in_t_bs:
            The value to assign to the storage_used_in_t_bs property of this BlockchainPlatform.
        :type storage_used_in_t_bs: float

        :param is_multi_ad:
            The value to assign to the is_multi_ad property of this BlockchainPlatform.
        :type is_multi_ad: bool

        :param total_ocpu_capacity:
            The value to assign to the total_ocpu_capacity property of this BlockchainPlatform.
        :type total_ocpu_capacity: int

        :param component_details:
            The value to assign to the component_details property of this BlockchainPlatform.
        :type component_details: oci.blockchain.models.BlockchainPlatformComponentDetails

        :param replicas:
            The value to assign to the replicas property of this BlockchainPlatform.
        :type replicas: oci.blockchain.models.ReplicaDetails

        :param host_ocpu_utilization_info:
            The value to assign to the host_ocpu_utilization_info property of this BlockchainPlatform.
        :type host_ocpu_utilization_info: list[oci.blockchain.models.OcpuUtilizationInfo]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BlockchainPlatform.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BlockchainPlatform.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'is_byol': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'service_version': 'str',
            'platform_role': 'str',
            'compute_shape': 'str',
            'platform_shape_type': 'str',
            'load_balancer_shape': 'str',
            'service_endpoint': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'storage_size_in_tbs': 'float',
            'storage_used_in_t_bs': 'float',
            'is_multi_ad': 'bool',
            'total_ocpu_capacity': 'int',
            'component_details': 'BlockchainPlatformComponentDetails',
            'replicas': 'ReplicaDetails',
            'host_ocpu_utilization_info': 'list[OcpuUtilizationInfo]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'is_byol': 'isByol',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'service_version': 'serviceVersion',
            'platform_role': 'platformRole',
            'compute_shape': 'computeShape',
            'platform_shape_type': 'platformShapeType',
            'load_balancer_shape': 'loadBalancerShape',
            'service_endpoint': 'serviceEndpoint',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'storage_size_in_tbs': 'storageSizeInTBs',
            'storage_used_in_t_bs': 'storageUsedInTBs',
            'is_multi_ad': 'isMultiAD',
            'total_ocpu_capacity': 'totalOcpuCapacity',
            'component_details': 'componentDetails',
            'replicas': 'replicas',
            'host_ocpu_utilization_info': 'hostOcpuUtilizationInfo',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._is_byol = None
        self._time_created = None
        self._time_updated = None
        self._service_version = None
        self._platform_role = None
        self._compute_shape = None
        self._platform_shape_type = None
        self._load_balancer_shape = None
        self._service_endpoint = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._storage_size_in_tbs = None
        self._storage_used_in_t_bs = None
        self._is_multi_ad = None
        self._total_ocpu_capacity = None
        self._component_details = None
        self._replicas = None
        self._host_ocpu_utilization_info = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BlockchainPlatform.
        unique identifier that is immutable on creation


        :return: The id of this BlockchainPlatform.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BlockchainPlatform.
        unique identifier that is immutable on creation


        :param id: The id of this BlockchainPlatform.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BlockchainPlatform.
        Platform Instance Display name, can be renamed


        :return: The display_name of this BlockchainPlatform.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BlockchainPlatform.
        Platform Instance Display name, can be renamed


        :param display_name: The display_name of this BlockchainPlatform.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BlockchainPlatform.
        Compartment Identifier


        :return: The compartment_id of this BlockchainPlatform.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BlockchainPlatform.
        Compartment Identifier


        :param compartment_id: The compartment_id of this BlockchainPlatform.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this BlockchainPlatform.
        Platform Instance Description


        :return: The description of this BlockchainPlatform.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BlockchainPlatform.
        Platform Instance Description


        :param description: The description of this BlockchainPlatform.
        :type: str
        """
        self._description = description

    @property
    def is_byol(self):
        """
        Gets the is_byol of this BlockchainPlatform.
        Bring your own license


        :return: The is_byol of this BlockchainPlatform.
        :rtype: bool
        """
        return self._is_byol

    @is_byol.setter
    def is_byol(self, is_byol):
        """
        Sets the is_byol of this BlockchainPlatform.
        Bring your own license


        :param is_byol: The is_byol of this BlockchainPlatform.
        :type: bool
        """
        self._is_byol = is_byol

    @property
    def time_created(self):
        """
        Gets the time_created of this BlockchainPlatform.
        The time the the Platform Instance was created. An RFC3339 formatted datetime string


        :return: The time_created of this BlockchainPlatform.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BlockchainPlatform.
        The time the the Platform Instance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this BlockchainPlatform.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BlockchainPlatform.
        The time the Platform Instance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this BlockchainPlatform.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BlockchainPlatform.
        The time the Platform Instance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this BlockchainPlatform.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def service_version(self):
        """
        Gets the service_version of this BlockchainPlatform.
        The version of the Platform Instance.


        :return: The service_version of this BlockchainPlatform.
        :rtype: str
        """
        return self._service_version

    @service_version.setter
    def service_version(self, service_version):
        """
        Sets the service_version of this BlockchainPlatform.
        The version of the Platform Instance.


        :param service_version: The service_version of this BlockchainPlatform.
        :type: str
        """
        self._service_version = service_version

    @property
    def platform_role(self):
        """
        **[Required]** Gets the platform_role of this BlockchainPlatform.
        Role of platform - FOUNDER or PARTICIPANT

        Allowed values for this property are: "FOUNDER", "PARTICIPANT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_role of this BlockchainPlatform.
        :rtype: str
        """
        return self._platform_role

    @platform_role.setter
    def platform_role(self, platform_role):
        """
        Sets the platform_role of this BlockchainPlatform.
        Role of platform - FOUNDER or PARTICIPANT


        :param platform_role: The platform_role of this BlockchainPlatform.
        :type: str
        """
        allowed_values = ["FOUNDER", "PARTICIPANT"]
        if not value_allowed_none_or_none_sentinel(platform_role, allowed_values):
            platform_role = 'UNKNOWN_ENUM_VALUE'
        self._platform_role = platform_role

    @property
    def compute_shape(self):
        """
        **[Required]** Gets the compute_shape of this BlockchainPlatform.
        Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM

        Allowed values for this property are: "STANDARD", "ENTERPRISE_SMALL", "ENTERPRISE_MEDIUM", "ENTERPRISE_LARGE", "ENTERPRISE_EXTRA_LARGE", "ENTERPRISE_CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The compute_shape of this BlockchainPlatform.
        :rtype: str
        """
        return self._compute_shape

    @compute_shape.setter
    def compute_shape(self, compute_shape):
        """
        Sets the compute_shape of this BlockchainPlatform.
        Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM


        :param compute_shape: The compute_shape of this BlockchainPlatform.
        :type: str
        """
        allowed_values = ["STANDARD", "ENTERPRISE_SMALL", "ENTERPRISE_MEDIUM", "ENTERPRISE_LARGE", "ENTERPRISE_EXTRA_LARGE", "ENTERPRISE_CUSTOM"]
        if not value_allowed_none_or_none_sentinel(compute_shape, allowed_values):
            compute_shape = 'UNKNOWN_ENUM_VALUE'
        self._compute_shape = compute_shape

    @property
    def platform_shape_type(self):
        """
        Gets the platform_shape_type of this BlockchainPlatform.
        Type of Platform shape - DEFAULT or CUSTOM

        Allowed values for this property are: "DEFAULT", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_shape_type of this BlockchainPlatform.
        :rtype: str
        """
        return self._platform_shape_type

    @platform_shape_type.setter
    def platform_shape_type(self, platform_shape_type):
        """
        Sets the platform_shape_type of this BlockchainPlatform.
        Type of Platform shape - DEFAULT or CUSTOM


        :param platform_shape_type: The platform_shape_type of this BlockchainPlatform.
        :type: str
        """
        allowed_values = ["DEFAULT", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(platform_shape_type, allowed_values):
            platform_shape_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_shape_type = platform_shape_type

    @property
    def load_balancer_shape(self):
        """
        Gets the load_balancer_shape of this BlockchainPlatform.
        Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS.

        Allowed values for this property are: "LB_100_MBPS", "LB_400_MBPS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The load_balancer_shape of this BlockchainPlatform.
        :rtype: str
        """
        return self._load_balancer_shape

    @load_balancer_shape.setter
    def load_balancer_shape(self, load_balancer_shape):
        """
        Sets the load_balancer_shape of this BlockchainPlatform.
        Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS.


        :param load_balancer_shape: The load_balancer_shape of this BlockchainPlatform.
        :type: str
        """
        allowed_values = ["LB_100_MBPS", "LB_400_MBPS"]
        if not value_allowed_none_or_none_sentinel(load_balancer_shape, allowed_values):
            load_balancer_shape = 'UNKNOWN_ENUM_VALUE'
        self._load_balancer_shape = load_balancer_shape

    @property
    def service_endpoint(self):
        """
        Gets the service_endpoint of this BlockchainPlatform.
        Service endpoint URL, valid post-provisioning


        :return: The service_endpoint of this BlockchainPlatform.
        :rtype: str
        """
        return self._service_endpoint

    @service_endpoint.setter
    def service_endpoint(self, service_endpoint):
        """
        Sets the service_endpoint of this BlockchainPlatform.
        Service endpoint URL, valid post-provisioning


        :param service_endpoint: The service_endpoint of this BlockchainPlatform.
        :type: str
        """
        self._service_endpoint = service_endpoint

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BlockchainPlatform.
        The current state of the Platform Instance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "SCALING", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BlockchainPlatform.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BlockchainPlatform.
        The current state of the Platform Instance.


        :param lifecycle_state: The lifecycle_state of this BlockchainPlatform.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "SCALING", "INACTIVE", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this BlockchainPlatform.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this BlockchainPlatform.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this BlockchainPlatform.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this BlockchainPlatform.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def storage_size_in_tbs(self):
        """
        Gets the storage_size_in_tbs of this BlockchainPlatform.
        Storage size in TBs


        :return: The storage_size_in_tbs of this BlockchainPlatform.
        :rtype: float
        """
        return self._storage_size_in_tbs

    @storage_size_in_tbs.setter
    def storage_size_in_tbs(self, storage_size_in_tbs):
        """
        Sets the storage_size_in_tbs of this BlockchainPlatform.
        Storage size in TBs


        :param storage_size_in_tbs: The storage_size_in_tbs of this BlockchainPlatform.
        :type: float
        """
        self._storage_size_in_tbs = storage_size_in_tbs

    @property
    def storage_used_in_t_bs(self):
        """
        Gets the storage_used_in_t_bs of this BlockchainPlatform.
        Storage used in TBs


        :return: The storage_used_in_t_bs of this BlockchainPlatform.
        :rtype: float
        """
        return self._storage_used_in_t_bs

    @storage_used_in_t_bs.setter
    def storage_used_in_t_bs(self, storage_used_in_t_bs):
        """
        Sets the storage_used_in_t_bs of this BlockchainPlatform.
        Storage used in TBs


        :param storage_used_in_t_bs: The storage_used_in_t_bs of this BlockchainPlatform.
        :type: float
        """
        self._storage_used_in_t_bs = storage_used_in_t_bs

    @property
    def is_multi_ad(self):
        """
        Gets the is_multi_ad of this BlockchainPlatform.
        True for multi-AD blockchain plaforms, false for single-AD


        :return: The is_multi_ad of this BlockchainPlatform.
        :rtype: bool
        """
        return self._is_multi_ad

    @is_multi_ad.setter
    def is_multi_ad(self, is_multi_ad):
        """
        Sets the is_multi_ad of this BlockchainPlatform.
        True for multi-AD blockchain plaforms, false for single-AD


        :param is_multi_ad: The is_multi_ad of this BlockchainPlatform.
        :type: bool
        """
        self._is_multi_ad = is_multi_ad

    @property
    def total_ocpu_capacity(self):
        """
        Gets the total_ocpu_capacity of this BlockchainPlatform.
        Number of total OCPUs allocated to the platform cluster


        :return: The total_ocpu_capacity of this BlockchainPlatform.
        :rtype: int
        """
        return self._total_ocpu_capacity

    @total_ocpu_capacity.setter
    def total_ocpu_capacity(self, total_ocpu_capacity):
        """
        Sets the total_ocpu_capacity of this BlockchainPlatform.
        Number of total OCPUs allocated to the platform cluster


        :param total_ocpu_capacity: The total_ocpu_capacity of this BlockchainPlatform.
        :type: int
        """
        self._total_ocpu_capacity = total_ocpu_capacity

    @property
    def component_details(self):
        """
        Gets the component_details of this BlockchainPlatform.

        :return: The component_details of this BlockchainPlatform.
        :rtype: oci.blockchain.models.BlockchainPlatformComponentDetails
        """
        return self._component_details

    @component_details.setter
    def component_details(self, component_details):
        """
        Sets the component_details of this BlockchainPlatform.

        :param component_details: The component_details of this BlockchainPlatform.
        :type: oci.blockchain.models.BlockchainPlatformComponentDetails
        """
        self._component_details = component_details

    @property
    def replicas(self):
        """
        Gets the replicas of this BlockchainPlatform.

        :return: The replicas of this BlockchainPlatform.
        :rtype: oci.blockchain.models.ReplicaDetails
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this BlockchainPlatform.

        :param replicas: The replicas of this BlockchainPlatform.
        :type: oci.blockchain.models.ReplicaDetails
        """
        self._replicas = replicas

    @property
    def host_ocpu_utilization_info(self):
        """
        Gets the host_ocpu_utilization_info of this BlockchainPlatform.
        List of OcpuUtilization for all hosts


        :return: The host_ocpu_utilization_info of this BlockchainPlatform.
        :rtype: list[oci.blockchain.models.OcpuUtilizationInfo]
        """
        return self._host_ocpu_utilization_info

    @host_ocpu_utilization_info.setter
    def host_ocpu_utilization_info(self, host_ocpu_utilization_info):
        """
        Sets the host_ocpu_utilization_info of this BlockchainPlatform.
        List of OcpuUtilization for all hosts


        :param host_ocpu_utilization_info: The host_ocpu_utilization_info of this BlockchainPlatform.
        :type: list[oci.blockchain.models.OcpuUtilizationInfo]
        """
        self._host_ocpu_utilization_info = host_ocpu_utilization_info

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BlockchainPlatform.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this BlockchainPlatform.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BlockchainPlatform.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this BlockchainPlatform.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BlockchainPlatform.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this BlockchainPlatform.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BlockchainPlatform.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this BlockchainPlatform.
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
