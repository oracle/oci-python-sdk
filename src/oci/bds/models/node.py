# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Node(object):
    """
    Details about a node.
    """

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

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
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a Node.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the node_type property of a Node.
    #: This constant has a value of "MASTER"
    NODE_TYPE_MASTER = "MASTER"

    #: A constant which can be used with the node_type property of a Node.
    #: This constant has a value of "EDGE"
    NODE_TYPE_EDGE = "EDGE"

    #: A constant which can be used with the node_type property of a Node.
    #: This constant has a value of "UTILITY"
    NODE_TYPE_UTILITY = "UTILITY"

    #: A constant which can be used with the node_type property of a Node.
    #: This constant has a value of "WORKER"
    NODE_TYPE_WORKER = "WORKER"

    #: A constant which can be used with the node_type property of a Node.
    #: This constant has a value of "COMPUTE_ONLY_WORKER"
    NODE_TYPE_COMPUTE_ONLY_WORKER = "COMPUTE_ONLY_WORKER"

    #: A constant which can be used with the node_type property of a Node.
    #: This constant has a value of "BURSTING"
    NODE_TYPE_BURSTING = "BURSTING"

    #: A constant which can be used with the node_type property of a Node.
    #: This constant has a value of "CLOUD_SQL"
    NODE_TYPE_CLOUD_SQL = "CLOUD_SQL"

    def __init__(self, **kwargs):
        """
        Initializes a new Node object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_id:
            The value to assign to the instance_id property of this Node.
        :type instance_id: str

        :param display_name:
            The value to assign to the display_name property of this Node.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Node.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STOPPED", "STOPPING", "STARTING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param node_type:
            The value to assign to the node_type property of this Node.
            Allowed values for this property are: "MASTER", "EDGE", "UTILITY", "WORKER", "COMPUTE_ONLY_WORKER", "BURSTING", "CLOUD_SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type node_type: str

        :param shape:
            The value to assign to the shape property of this Node.
        :type shape: str

        :param attached_block_volumes:
            The value to assign to the attached_block_volumes property of this Node.
        :type attached_block_volumes: list[oci.bds.models.VolumeAttachmentDetail]

        :param subnet_id:
            The value to assign to the subnet_id property of this Node.
        :type subnet_id: str

        :param ip_address:
            The value to assign to the ip_address property of this Node.
        :type ip_address: str

        :param hostname:
            The value to assign to the hostname property of this Node.
        :type hostname: str

        :param image_id:
            The value to assign to the image_id property of this Node.
        :type image_id: str

        :param ssh_fingerprint:
            The value to assign to the ssh_fingerprint property of this Node.
        :type ssh_fingerprint: str

        :param availability_domain:
            The value to assign to the availability_domain property of this Node.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this Node.
        :type fault_domain: str

        :param time_created:
            The value to assign to the time_created property of this Node.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Node.
        :type time_updated: datetime

        :param ocpus:
            The value to assign to the ocpus property of this Node.
        :type ocpus: int

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this Node.
        :type memory_in_gbs: int

        :param nvmes:
            The value to assign to the nvmes property of this Node.
        :type nvmes: int

        :param local_disks_total_size_in_gbs:
            The value to assign to the local_disks_total_size_in_gbs property of this Node.
        :type local_disks_total_size_in_gbs: float

        """
        self.swagger_types = {
            'instance_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'node_type': 'str',
            'shape': 'str',
            'attached_block_volumes': 'list[VolumeAttachmentDetail]',
            'subnet_id': 'str',
            'ip_address': 'str',
            'hostname': 'str',
            'image_id': 'str',
            'ssh_fingerprint': 'str',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'ocpus': 'int',
            'memory_in_gbs': 'int',
            'nvmes': 'int',
            'local_disks_total_size_in_gbs': 'float'
        }

        self.attribute_map = {
            'instance_id': 'instanceId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'node_type': 'nodeType',
            'shape': 'shape',
            'attached_block_volumes': 'attachedBlockVolumes',
            'subnet_id': 'subnetId',
            'ip_address': 'ipAddress',
            'hostname': 'hostname',
            'image_id': 'imageId',
            'ssh_fingerprint': 'sshFingerprint',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs',
            'nvmes': 'nvmes',
            'local_disks_total_size_in_gbs': 'localDisksTotalSizeInGBs'
        }

        self._instance_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._node_type = None
        self._shape = None
        self._attached_block_volumes = None
        self._subnet_id = None
        self._ip_address = None
        self._hostname = None
        self._image_id = None
        self._ssh_fingerprint = None
        self._availability_domain = None
        self._fault_domain = None
        self._time_created = None
        self._time_updated = None
        self._ocpus = None
        self._memory_in_gbs = None
        self._nvmes = None
        self._local_disks_total_size_in_gbs = None

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this Node.
        The OCID of the underlying Oracle Cloud Infrastructure Compute instance.


        :return: The instance_id of this Node.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this Node.
        The OCID of the underlying Oracle Cloud Infrastructure Compute instance.


        :param instance_id: The instance_id of this Node.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Node.
        The name of the node.


        :return: The display_name of this Node.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Node.
        The name of the node.


        :param display_name: The display_name of this Node.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Node.
        The state of the node.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STOPPED", "STOPPING", "STARTING", 'UNKNOWN_ENUM_VALUE'.
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
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STOPPED", "STOPPING", "STARTING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def node_type(self):
        """
        **[Required]** Gets the node_type of this Node.
        Cluster node type.

        Allowed values for this property are: "MASTER", "EDGE", "UTILITY", "WORKER", "COMPUTE_ONLY_WORKER", "BURSTING", "CLOUD_SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The node_type of this Node.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this Node.
        Cluster node type.


        :param node_type: The node_type of this Node.
        :type: str
        """
        allowed_values = ["MASTER", "EDGE", "UTILITY", "WORKER", "COMPUTE_ONLY_WORKER", "BURSTING", "CLOUD_SQL"]
        if not value_allowed_none_or_none_sentinel(node_type, allowed_values):
            node_type = 'UNKNOWN_ENUM_VALUE'
        self._node_type = node_type

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this Node.
        Shape of the node.


        :return: The shape of this Node.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this Node.
        Shape of the node.


        :param shape: The shape of this Node.
        :type: str
        """
        self._shape = shape

    @property
    def attached_block_volumes(self):
        """
        Gets the attached_block_volumes of this Node.
        The list of block volumes attached to a given node.


        :return: The attached_block_volumes of this Node.
        :rtype: list[oci.bds.models.VolumeAttachmentDetail]
        """
        return self._attached_block_volumes

    @attached_block_volumes.setter
    def attached_block_volumes(self, attached_block_volumes):
        """
        Sets the attached_block_volumes of this Node.
        The list of block volumes attached to a given node.


        :param attached_block_volumes: The attached_block_volumes of this Node.
        :type: list[oci.bds.models.VolumeAttachmentDetail]
        """
        self._attached_block_volumes = attached_block_volumes

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this Node.
        The OCID of the subnet in which the node is to be created.


        :return: The subnet_id of this Node.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Node.
        The OCID of the subnet in which the node is to be created.


        :param subnet_id: The subnet_id of this Node.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this Node.
        IP address of the node.


        :return: The ip_address of this Node.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Node.
        IP address of the node.


        :param ip_address: The ip_address of this Node.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def hostname(self):
        """
        Gets the hostname of this Node.
        The fully-qualified hostname (FQDN) of the node.


        :return: The hostname of this Node.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this Node.
        The fully-qualified hostname (FQDN) of the node.


        :param hostname: The hostname of this Node.
        :type: str
        """
        self._hostname = hostname

    @property
    def image_id(self):
        """
        Gets the image_id of this Node.
        The OCID of the image from which the node was created.


        :return: The image_id of this Node.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this Node.
        The OCID of the image from which the node was created.


        :param image_id: The image_id of this Node.
        :type: str
        """
        self._image_id = image_id

    @property
    def ssh_fingerprint(self):
        """
        **[Required]** Gets the ssh_fingerprint of this Node.
        The fingerprint of the SSH key used for node access.


        :return: The ssh_fingerprint of this Node.
        :rtype: str
        """
        return self._ssh_fingerprint

    @ssh_fingerprint.setter
    def ssh_fingerprint(self, ssh_fingerprint):
        """
        Sets the ssh_fingerprint of this Node.
        The fingerprint of the SSH key used for node access.


        :param ssh_fingerprint: The ssh_fingerprint of this Node.
        :type: str
        """
        self._ssh_fingerprint = ssh_fingerprint

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this Node.
        The name of the availability domain in which the node is running.


        :return: The availability_domain of this Node.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Node.
        The name of the availability domain in which the node is running.


        :param availability_domain: The availability_domain of this Node.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        **[Required]** Gets the fault_domain of this Node.
        The name of the fault domain in which the node is running.


        :return: The fault_domain of this Node.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this Node.
        The name of the fault domain in which the node is running.


        :param fault_domain: The fault_domain of this Node.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Node.
        The time the node was created, shown as an RFC 3339 formatted datetime string.


        :return: The time_created of this Node.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Node.
        The time the node was created, shown as an RFC 3339 formatted datetime string.


        :param time_created: The time_created of this Node.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Node.
        The time the cluster was updated, shown as an RFC 3339 formatted datetime string.


        :return: The time_updated of this Node.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Node.
        The time the cluster was updated, shown as an RFC 3339 formatted datetime string.


        :param time_updated: The time_updated of this Node.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def ocpus(self):
        """
        Gets the ocpus of this Node.
        The total number of OCPUs available to the node.


        :return: The ocpus of this Node.
        :rtype: int
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this Node.
        The total number of OCPUs available to the node.


        :param ocpus: The ocpus of this Node.
        :type: int
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this Node.
        The total amount of memory available to the node, in gigabytes.


        :return: The memory_in_gbs of this Node.
        :rtype: int
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this Node.
        The total amount of memory available to the node, in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this Node.
        :type: int
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def nvmes(self):
        """
        Gets the nvmes of this Node.
        The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.


        :return: The nvmes of this Node.
        :rtype: int
        """
        return self._nvmes

    @nvmes.setter
    def nvmes(self, nvmes):
        """
        Sets the nvmes of this Node.
        The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.


        :param nvmes: The nvmes of this Node.
        :type: int
        """
        self._nvmes = nvmes

    @property
    def local_disks_total_size_in_gbs(self):
        """
        Gets the local_disks_total_size_in_gbs of this Node.
        The aggregate size of all local disks, in gigabytes. If the instance does not have any local disks, this field is null.


        :return: The local_disks_total_size_in_gbs of this Node.
        :rtype: float
        """
        return self._local_disks_total_size_in_gbs

    @local_disks_total_size_in_gbs.setter
    def local_disks_total_size_in_gbs(self, local_disks_total_size_in_gbs):
        """
        Sets the local_disks_total_size_in_gbs of this Node.
        The aggregate size of all local disks, in gigabytes. If the instance does not have any local disks, this field is null.


        :param local_disks_total_size_in_gbs: The local_disks_total_size_in_gbs of this Node.
        :type: float
        """
        self._local_disks_total_size_in_gbs = local_disks_total_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
