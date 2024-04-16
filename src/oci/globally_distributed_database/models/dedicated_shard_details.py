# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedShardDetails(object):
    """
    Details of ATP-D based shard.
    """

    #: A constant which can be used with the status property of a DedicatedShardDetails.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a DedicatedShardDetails.
    #: This constant has a value of "DELETING"
    STATUS_DELETING = "DELETING"

    #: A constant which can be used with the status property of a DedicatedShardDetails.
    #: This constant has a value of "DELETED"
    STATUS_DELETED = "DELETED"

    #: A constant which can be used with the status property of a DedicatedShardDetails.
    #: This constant has a value of "UPDATING"
    STATUS_UPDATING = "UPDATING"

    #: A constant which can be used with the status property of a DedicatedShardDetails.
    #: This constant has a value of "CREATING"
    STATUS_CREATING = "CREATING"

    #: A constant which can be used with the status property of a DedicatedShardDetails.
    #: This constant has a value of "CREATED"
    STATUS_CREATED = "CREATED"

    #: A constant which can be used with the status property of a DedicatedShardDetails.
    #: This constant has a value of "READY_FOR_CONFIGURATION"
    STATUS_READY_FOR_CONFIGURATION = "READY_FOR_CONFIGURATION"

    #: A constant which can be used with the status property of a DedicatedShardDetails.
    #: This constant has a value of "CONFIGURED"
    STATUS_CONFIGURED = "CONFIGURED"

    #: A constant which can be used with the status property of a DedicatedShardDetails.
    #: This constant has a value of "NEEDS_ATTENTION"
    STATUS_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedShardDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param encryption_key_details:
            The value to assign to the encryption_key_details property of this DedicatedShardDetails.
        :type encryption_key_details: oci.globally_distributed_database.models.DedicatedShardOrCatalogEncryptionKeyDetails

        :param name:
            The value to assign to the name property of this DedicatedShardDetails.
        :type name: str

        :param compute_count:
            The value to assign to the compute_count property of this DedicatedShardDetails.
        :type compute_count: float

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this DedicatedShardDetails.
        :type data_storage_size_in_gbs: float

        :param shard_group:
            The value to assign to the shard_group property of this DedicatedShardDetails.
        :type shard_group: str

        :param time_created:
            The value to assign to the time_created property of this DedicatedShardDetails.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DedicatedShardDetails.
        :type time_updated: datetime

        :param time_ssl_certificate_expires:
            The value to assign to the time_ssl_certificate_expires property of this DedicatedShardDetails.
        :type time_ssl_certificate_expires: datetime

        :param status:
            The value to assign to the status property of this DedicatedShardDetails.
            Allowed values for this property are: "FAILED", "DELETING", "DELETED", "UPDATING", "CREATING", "CREATED", "READY_FOR_CONFIGURATION", "CONFIGURED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param shard_space:
            The value to assign to the shard_space property of this DedicatedShardDetails.
        :type shard_space: str

        :param supporting_resource_id:
            The value to assign to the supporting_resource_id property of this DedicatedShardDetails.
        :type supporting_resource_id: str

        :param container_database_id:
            The value to assign to the container_database_id property of this DedicatedShardDetails.
        :type container_database_id: str

        :param container_database_parent_id:
            The value to assign to the container_database_parent_id property of this DedicatedShardDetails.
        :type container_database_parent_id: str

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this DedicatedShardDetails.
        :type is_auto_scaling_enabled: bool

        :param cloud_autonomous_vm_cluster_id:
            The value to assign to the cloud_autonomous_vm_cluster_id property of this DedicatedShardDetails.
        :type cloud_autonomous_vm_cluster_id: str

        :param peer_cloud_autonomous_vm_cluster_id:
            The value to assign to the peer_cloud_autonomous_vm_cluster_id property of this DedicatedShardDetails.
        :type peer_cloud_autonomous_vm_cluster_id: str

        :param metadata:
            The value to assign to the metadata property of this DedicatedShardDetails.
        :type metadata: dict(str, object)

        """
        self.swagger_types = {
            'encryption_key_details': 'DedicatedShardOrCatalogEncryptionKeyDetails',
            'name': 'str',
            'compute_count': 'float',
            'data_storage_size_in_gbs': 'float',
            'shard_group': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_ssl_certificate_expires': 'datetime',
            'status': 'str',
            'shard_space': 'str',
            'supporting_resource_id': 'str',
            'container_database_id': 'str',
            'container_database_parent_id': 'str',
            'is_auto_scaling_enabled': 'bool',
            'cloud_autonomous_vm_cluster_id': 'str',
            'peer_cloud_autonomous_vm_cluster_id': 'str',
            'metadata': 'dict(str, object)'
        }

        self.attribute_map = {
            'encryption_key_details': 'encryptionKeyDetails',
            'name': 'name',
            'compute_count': 'computeCount',
            'data_storage_size_in_gbs': 'dataStorageSizeInGbs',
            'shard_group': 'shardGroup',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_ssl_certificate_expires': 'timeSslCertificateExpires',
            'status': 'status',
            'shard_space': 'shardSpace',
            'supporting_resource_id': 'supportingResourceId',
            'container_database_id': 'containerDatabaseId',
            'container_database_parent_id': 'containerDatabaseParentId',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'cloud_autonomous_vm_cluster_id': 'cloudAutonomousVmClusterId',
            'peer_cloud_autonomous_vm_cluster_id': 'peerCloudAutonomousVmClusterId',
            'metadata': 'metadata'
        }

        self._encryption_key_details = None
        self._name = None
        self._compute_count = None
        self._data_storage_size_in_gbs = None
        self._shard_group = None
        self._time_created = None
        self._time_updated = None
        self._time_ssl_certificate_expires = None
        self._status = None
        self._shard_space = None
        self._supporting_resource_id = None
        self._container_database_id = None
        self._container_database_parent_id = None
        self._is_auto_scaling_enabled = None
        self._cloud_autonomous_vm_cluster_id = None
        self._peer_cloud_autonomous_vm_cluster_id = None
        self._metadata = None

    @property
    def encryption_key_details(self):
        """
        Gets the encryption_key_details of this DedicatedShardDetails.

        :return: The encryption_key_details of this DedicatedShardDetails.
        :rtype: oci.globally_distributed_database.models.DedicatedShardOrCatalogEncryptionKeyDetails
        """
        return self._encryption_key_details

    @encryption_key_details.setter
    def encryption_key_details(self, encryption_key_details):
        """
        Sets the encryption_key_details of this DedicatedShardDetails.

        :param encryption_key_details: The encryption_key_details of this DedicatedShardDetails.
        :type: oci.globally_distributed_database.models.DedicatedShardOrCatalogEncryptionKeyDetails
        """
        self._encryption_key_details = encryption_key_details

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DedicatedShardDetails.
        Name of the shard.


        :return: The name of this DedicatedShardDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DedicatedShardDetails.
        Name of the shard.


        :param name: The name of this DedicatedShardDetails.
        :type: str
        """
        self._name = name

    @property
    def compute_count(self):
        """
        **[Required]** Gets the compute_count of this DedicatedShardDetails.
        The compute amount available to the underlying autonomous database associated with shard.


        :return: The compute_count of this DedicatedShardDetails.
        :rtype: float
        """
        return self._compute_count

    @compute_count.setter
    def compute_count(self, compute_count):
        """
        Sets the compute_count of this DedicatedShardDetails.
        The compute amount available to the underlying autonomous database associated with shard.


        :param compute_count: The compute_count of this DedicatedShardDetails.
        :type: float
        """
        self._compute_count = compute_count

    @property
    def data_storage_size_in_gbs(self):
        """
        **[Required]** Gets the data_storage_size_in_gbs of this DedicatedShardDetails.
        The data disk group size to be allocated in GBs.


        :return: The data_storage_size_in_gbs of this DedicatedShardDetails.
        :rtype: float
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this DedicatedShardDetails.
        The data disk group size to be allocated in GBs.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this DedicatedShardDetails.
        :type: float
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def shard_group(self):
        """
        **[Required]** Gets the shard_group of this DedicatedShardDetails.
        Name of the shard-group to which the shard belongs.


        :return: The shard_group of this DedicatedShardDetails.
        :rtype: str
        """
        return self._shard_group

    @shard_group.setter
    def shard_group(self, shard_group):
        """
        Sets the shard_group of this DedicatedShardDetails.
        Name of the shard-group to which the shard belongs.


        :param shard_group: The shard_group of this DedicatedShardDetails.
        :type: str
        """
        self._shard_group = shard_group

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DedicatedShardDetails.
        The time the the shard was created. An RFC3339 formatted datetime string


        :return: The time_created of this DedicatedShardDetails.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DedicatedShardDetails.
        The time the the shard was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this DedicatedShardDetails.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this DedicatedShardDetails.
        The time the shard was last updated. An RFC3339 formatted datetime string


        :return: The time_updated of this DedicatedShardDetails.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DedicatedShardDetails.
        The time the shard was last updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this DedicatedShardDetails.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_ssl_certificate_expires(self):
        """
        Gets the time_ssl_certificate_expires of this DedicatedShardDetails.
        The time the ssl certificate associated with shard expires. An RFC3339 formatted datetime string


        :return: The time_ssl_certificate_expires of this DedicatedShardDetails.
        :rtype: datetime
        """
        return self._time_ssl_certificate_expires

    @time_ssl_certificate_expires.setter
    def time_ssl_certificate_expires(self, time_ssl_certificate_expires):
        """
        Sets the time_ssl_certificate_expires of this DedicatedShardDetails.
        The time the ssl certificate associated with shard expires. An RFC3339 formatted datetime string


        :param time_ssl_certificate_expires: The time_ssl_certificate_expires of this DedicatedShardDetails.
        :type: datetime
        """
        self._time_ssl_certificate_expires = time_ssl_certificate_expires

    @property
    def status(self):
        """
        **[Required]** Gets the status of this DedicatedShardDetails.
        Status of shard or catalog or gsm for the sharded database.

        Allowed values for this property are: "FAILED", "DELETING", "DELETED", "UPDATING", "CREATING", "CREATED", "READY_FOR_CONFIGURATION", "CONFIGURED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DedicatedShardDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DedicatedShardDetails.
        Status of shard or catalog or gsm for the sharded database.


        :param status: The status of this DedicatedShardDetails.
        :type: str
        """
        allowed_values = ["FAILED", "DELETING", "DELETED", "UPDATING", "CREATING", "CREATED", "READY_FOR_CONFIGURATION", "CONFIGURED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def shard_space(self):
        """
        Gets the shard_space of this DedicatedShardDetails.
        Shard space name.


        :return: The shard_space of this DedicatedShardDetails.
        :rtype: str
        """
        return self._shard_space

    @shard_space.setter
    def shard_space(self, shard_space):
        """
        Sets the shard_space of this DedicatedShardDetails.
        Shard space name.


        :param shard_space: The shard_space of this DedicatedShardDetails.
        :type: str
        """
        self._shard_space = shard_space

    @property
    def supporting_resource_id(self):
        """
        Gets the supporting_resource_id of this DedicatedShardDetails.
        Identifier of the underlying supporting resource.


        :return: The supporting_resource_id of this DedicatedShardDetails.
        :rtype: str
        """
        return self._supporting_resource_id

    @supporting_resource_id.setter
    def supporting_resource_id(self, supporting_resource_id):
        """
        Sets the supporting_resource_id of this DedicatedShardDetails.
        Identifier of the underlying supporting resource.


        :param supporting_resource_id: The supporting_resource_id of this DedicatedShardDetails.
        :type: str
        """
        self._supporting_resource_id = supporting_resource_id

    @property
    def container_database_id(self):
        """
        Gets the container_database_id of this DedicatedShardDetails.
        Identifier of the underlying container database.


        :return: The container_database_id of this DedicatedShardDetails.
        :rtype: str
        """
        return self._container_database_id

    @container_database_id.setter
    def container_database_id(self, container_database_id):
        """
        Sets the container_database_id of this DedicatedShardDetails.
        Identifier of the underlying container database.


        :param container_database_id: The container_database_id of this DedicatedShardDetails.
        :type: str
        """
        self._container_database_id = container_database_id

    @property
    def container_database_parent_id(self):
        """
        Gets the container_database_parent_id of this DedicatedShardDetails.
        Identifier of the underlying container database parent.


        :return: The container_database_parent_id of this DedicatedShardDetails.
        :rtype: str
        """
        return self._container_database_parent_id

    @container_database_parent_id.setter
    def container_database_parent_id(self, container_database_parent_id):
        """
        Sets the container_database_parent_id of this DedicatedShardDetails.
        Identifier of the underlying container database parent.


        :param container_database_parent_id: The container_database_parent_id of this DedicatedShardDetails.
        :type: str
        """
        self._container_database_parent_id = container_database_parent_id

    @property
    def is_auto_scaling_enabled(self):
        """
        **[Required]** Gets the is_auto_scaling_enabled of this DedicatedShardDetails.
        Determines the auto-scaling mode.


        :return: The is_auto_scaling_enabled of this DedicatedShardDetails.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this DedicatedShardDetails.
        Determines the auto-scaling mode.


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this DedicatedShardDetails.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def cloud_autonomous_vm_cluster_id(self):
        """
        **[Required]** Gets the cloud_autonomous_vm_cluster_id of this DedicatedShardDetails.
        Identifier of the primary cloudAutonomousVmCluster for the shard.


        :return: The cloud_autonomous_vm_cluster_id of this DedicatedShardDetails.
        :rtype: str
        """
        return self._cloud_autonomous_vm_cluster_id

    @cloud_autonomous_vm_cluster_id.setter
    def cloud_autonomous_vm_cluster_id(self, cloud_autonomous_vm_cluster_id):
        """
        Sets the cloud_autonomous_vm_cluster_id of this DedicatedShardDetails.
        Identifier of the primary cloudAutonomousVmCluster for the shard.


        :param cloud_autonomous_vm_cluster_id: The cloud_autonomous_vm_cluster_id of this DedicatedShardDetails.
        :type: str
        """
        self._cloud_autonomous_vm_cluster_id = cloud_autonomous_vm_cluster_id

    @property
    def peer_cloud_autonomous_vm_cluster_id(self):
        """
        Gets the peer_cloud_autonomous_vm_cluster_id of this DedicatedShardDetails.
        Identifier of the peer cloudAutonomousVmCluster for the shard.


        :return: The peer_cloud_autonomous_vm_cluster_id of this DedicatedShardDetails.
        :rtype: str
        """
        return self._peer_cloud_autonomous_vm_cluster_id

    @peer_cloud_autonomous_vm_cluster_id.setter
    def peer_cloud_autonomous_vm_cluster_id(self, peer_cloud_autonomous_vm_cluster_id):
        """
        Sets the peer_cloud_autonomous_vm_cluster_id of this DedicatedShardDetails.
        Identifier of the peer cloudAutonomousVmCluster for the shard.


        :param peer_cloud_autonomous_vm_cluster_id: The peer_cloud_autonomous_vm_cluster_id of this DedicatedShardDetails.
        :type: str
        """
        self._peer_cloud_autonomous_vm_cluster_id = peer_cloud_autonomous_vm_cluster_id

    @property
    def metadata(self):
        """
        Gets the metadata of this DedicatedShardDetails.
        Additional metadata related to shard's underlying supporting resource.


        :return: The metadata of this DedicatedShardDetails.
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this DedicatedShardDetails.
        Additional metadata related to shard's underlying supporting resource.


        :param metadata: The metadata of this DedicatedShardDetails.
        :type: dict(str, object)
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other