# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudVmCluster(object):
    """
    Details of the cloud VM cluster. Applies to Exadata Cloud Service instances only.
    """

    #: A constant which can be used with the lifecycle_state property of a CloudVmCluster.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a CloudVmCluster.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a CloudVmCluster.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CloudVmCluster.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a CloudVmCluster.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a CloudVmCluster.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a CloudVmCluster.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the license_model property of a CloudVmCluster.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CloudVmCluster.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the disk_redundancy property of a CloudVmCluster.
    #: This constant has a value of "HIGH"
    DISK_REDUNDANCY_HIGH = "HIGH"

    #: A constant which can be used with the disk_redundancy property of a CloudVmCluster.
    #: This constant has a value of "NORMAL"
    DISK_REDUNDANCY_NORMAL = "NORMAL"

    def __init__(self, **kwargs):
        """
        Initializes a new CloudVmCluster object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param iorm_config_cache:
            The value to assign to the iorm_config_cache property of this CloudVmCluster.
        :type iorm_config_cache: oci.database.models.ExadataIormConfig

        :param id:
            The value to assign to the id property of this CloudVmCluster.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CloudVmCluster.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CloudVmCluster.
        :type availability_domain: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CloudVmCluster.
        :type subnet_id: str

        :param backup_subnet_id:
            The value to assign to the backup_subnet_id property of this CloudVmCluster.
        :type backup_subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CloudVmCluster.
        :type nsg_ids: list[str]

        :param backup_network_nsg_ids:
            The value to assign to the backup_network_nsg_ids property of this CloudVmCluster.
        :type backup_network_nsg_ids: list[str]

        :param last_update_history_entry_id:
            The value to assign to the last_update_history_entry_id property of this CloudVmCluster.
        :type last_update_history_entry_id: str

        :param shape:
            The value to assign to the shape property of this CloudVmCluster.
        :type shape: str

        :param listener_port:
            The value to assign to the listener_port property of this CloudVmCluster.
        :type listener_port: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CloudVmCluster.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param node_count:
            The value to assign to the node_count property of this CloudVmCluster.
        :type node_count: int

        :param storage_size_in_gbs:
            The value to assign to the storage_size_in_gbs property of this CloudVmCluster.
        :type storage_size_in_gbs: int

        :param display_name:
            The value to assign to the display_name property of this CloudVmCluster.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this CloudVmCluster.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CloudVmCluster.
        :type lifecycle_details: str

        :param time_zone:
            The value to assign to the time_zone property of this CloudVmCluster.
        :type time_zone: str

        :param hostname:
            The value to assign to the hostname property of this CloudVmCluster.
        :type hostname: str

        :param domain:
            The value to assign to the domain property of this CloudVmCluster.
        :type domain: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CloudVmCluster.
        :type cpu_core_count: int

        :param cluster_name:
            The value to assign to the cluster_name property of this CloudVmCluster.
        :type cluster_name: str

        :param data_storage_percentage:
            The value to assign to the data_storage_percentage property of this CloudVmCluster.
        :type data_storage_percentage: int

        :param is_local_backup_enabled:
            The value to assign to the is_local_backup_enabled property of this CloudVmCluster.
        :type is_local_backup_enabled: bool

        :param cloud_exadata_infrastructure_id:
            The value to assign to the cloud_exadata_infrastructure_id property of this CloudVmCluster.
        :type cloud_exadata_infrastructure_id: str

        :param is_sparse_diskgroup_enabled:
            The value to assign to the is_sparse_diskgroup_enabled property of this CloudVmCluster.
        :type is_sparse_diskgroup_enabled: bool

        :param gi_version:
            The value to assign to the gi_version property of this CloudVmCluster.
        :type gi_version: str

        :param system_version:
            The value to assign to the system_version property of this CloudVmCluster.
        :type system_version: str

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this CloudVmCluster.
        :type ssh_public_keys: list[str]

        :param license_model:
            The value to assign to the license_model property of this CloudVmCluster.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param disk_redundancy:
            The value to assign to the disk_redundancy property of this CloudVmCluster.
            Allowed values for this property are: "HIGH", "NORMAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type disk_redundancy: str

        :param scan_ip_ids:
            The value to assign to the scan_ip_ids property of this CloudVmCluster.
        :type scan_ip_ids: list[str]

        :param vip_ids:
            The value to assign to the vip_ids property of this CloudVmCluster.
        :type vip_ids: list[str]

        :param scan_dns_record_id:
            The value to assign to the scan_dns_record_id property of this CloudVmCluster.
        :type scan_dns_record_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CloudVmCluster.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CloudVmCluster.
        :type defined_tags: dict(str, dict(str, object))

        :param scan_dns_name:
            The value to assign to the scan_dns_name property of this CloudVmCluster.
        :type scan_dns_name: str

        :param zone_id:
            The value to assign to the zone_id property of this CloudVmCluster.
        :type zone_id: str

        """
        self.swagger_types = {
            'iorm_config_cache': 'ExadataIormConfig',
            'id': 'str',
            'compartment_id': 'str',
            'availability_domain': 'str',
            'subnet_id': 'str',
            'backup_subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'backup_network_nsg_ids': 'list[str]',
            'last_update_history_entry_id': 'str',
            'shape': 'str',
            'listener_port': 'int',
            'lifecycle_state': 'str',
            'node_count': 'int',
            'storage_size_in_gbs': 'int',
            'display_name': 'str',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'time_zone': 'str',
            'hostname': 'str',
            'domain': 'str',
            'cpu_core_count': 'int',
            'cluster_name': 'str',
            'data_storage_percentage': 'int',
            'is_local_backup_enabled': 'bool',
            'cloud_exadata_infrastructure_id': 'str',
            'is_sparse_diskgroup_enabled': 'bool',
            'gi_version': 'str',
            'system_version': 'str',
            'ssh_public_keys': 'list[str]',
            'license_model': 'str',
            'disk_redundancy': 'str',
            'scan_ip_ids': 'list[str]',
            'vip_ids': 'list[str]',
            'scan_dns_record_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'scan_dns_name': 'str',
            'zone_id': 'str'
        }

        self.attribute_map = {
            'iorm_config_cache': 'iormConfigCache',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'subnet_id': 'subnetId',
            'backup_subnet_id': 'backupSubnetId',
            'nsg_ids': 'nsgIds',
            'backup_network_nsg_ids': 'backupNetworkNsgIds',
            'last_update_history_entry_id': 'lastUpdateHistoryEntryId',
            'shape': 'shape',
            'listener_port': 'listenerPort',
            'lifecycle_state': 'lifecycleState',
            'node_count': 'nodeCount',
            'storage_size_in_gbs': 'storageSizeInGBs',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'time_zone': 'timeZone',
            'hostname': 'hostname',
            'domain': 'domain',
            'cpu_core_count': 'cpuCoreCount',
            'cluster_name': 'clusterName',
            'data_storage_percentage': 'dataStoragePercentage',
            'is_local_backup_enabled': 'isLocalBackupEnabled',
            'cloud_exadata_infrastructure_id': 'cloudExadataInfrastructureId',
            'is_sparse_diskgroup_enabled': 'isSparseDiskgroupEnabled',
            'gi_version': 'giVersion',
            'system_version': 'systemVersion',
            'ssh_public_keys': 'sshPublicKeys',
            'license_model': 'licenseModel',
            'disk_redundancy': 'diskRedundancy',
            'scan_ip_ids': 'scanIpIds',
            'vip_ids': 'vipIds',
            'scan_dns_record_id': 'scanDnsRecordId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'scan_dns_name': 'scanDnsName',
            'zone_id': 'zoneId'
        }

        self._iorm_config_cache = None
        self._id = None
        self._compartment_id = None
        self._availability_domain = None
        self._subnet_id = None
        self._backup_subnet_id = None
        self._nsg_ids = None
        self._backup_network_nsg_ids = None
        self._last_update_history_entry_id = None
        self._shape = None
        self._listener_port = None
        self._lifecycle_state = None
        self._node_count = None
        self._storage_size_in_gbs = None
        self._display_name = None
        self._time_created = None
        self._lifecycle_details = None
        self._time_zone = None
        self._hostname = None
        self._domain = None
        self._cpu_core_count = None
        self._cluster_name = None
        self._data_storage_percentage = None
        self._is_local_backup_enabled = None
        self._cloud_exadata_infrastructure_id = None
        self._is_sparse_diskgroup_enabled = None
        self._gi_version = None
        self._system_version = None
        self._ssh_public_keys = None
        self._license_model = None
        self._disk_redundancy = None
        self._scan_ip_ids = None
        self._vip_ids = None
        self._scan_dns_record_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._scan_dns_name = None
        self._zone_id = None

    @property
    def iorm_config_cache(self):
        """
        Gets the iorm_config_cache of this CloudVmCluster.

        :return: The iorm_config_cache of this CloudVmCluster.
        :rtype: oci.database.models.ExadataIormConfig
        """
        return self._iorm_config_cache

    @iorm_config_cache.setter
    def iorm_config_cache(self, iorm_config_cache):
        """
        Sets the iorm_config_cache of this CloudVmCluster.

        :param iorm_config_cache: The iorm_config_cache of this CloudVmCluster.
        :type: oci.database.models.ExadataIormConfig
        """
        self._iorm_config_cache = iorm_config_cache

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CloudVmCluster.
        The `OCID`__ of the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this CloudVmCluster.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudVmCluster.
        The `OCID`__ of the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this CloudVmCluster.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CloudVmCluster.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CloudVmCluster.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CloudVmCluster.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CloudVmCluster.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CloudVmCluster.
        The name of the availability domain that the cloud Exadata infrastructure resource is located in.


        :return: The availability_domain of this CloudVmCluster.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CloudVmCluster.
        The name of the availability domain that the cloud Exadata infrastructure resource is located in.


        :param availability_domain: The availability_domain of this CloudVmCluster.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CloudVmCluster.
        The `OCID`__ of the subnet associated with the cloud VM cluster.

        **Subnet Restrictions:**
        - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CloudVmCluster.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CloudVmCluster.
        The `OCID`__ of the subnet associated with the cloud VM cluster.

        **Subnet Restrictions:**
        - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CloudVmCluster.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def backup_subnet_id(self):
        """
        Gets the backup_subnet_id of this CloudVmCluster.
        The `OCID`__ of the backup network subnet associated with the cloud VM cluster.

        **Subnet Restriction:** See the subnet restrictions information for **subnetId**.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The backup_subnet_id of this CloudVmCluster.
        :rtype: str
        """
        return self._backup_subnet_id

    @backup_subnet_id.setter
    def backup_subnet_id(self, backup_subnet_id):
        """
        Sets the backup_subnet_id of this CloudVmCluster.
        The `OCID`__ of the backup network subnet associated with the cloud VM cluster.

        **Subnet Restriction:** See the subnet restrictions information for **subnetId**.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param backup_subnet_id: The backup_subnet_id of this CloudVmCluster.
        :type: str
        """
        self._backup_subnet_id = backup_subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CloudVmCluster.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this CloudVmCluster.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CloudVmCluster.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this CloudVmCluster.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def backup_network_nsg_ids(self):
        """
        Gets the backup_network_nsg_ids of this CloudVmCluster.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The backup_network_nsg_ids of this CloudVmCluster.
        :rtype: list[str]
        """
        return self._backup_network_nsg_ids

    @backup_network_nsg_ids.setter
    def backup_network_nsg_ids(self, backup_network_nsg_ids):
        """
        Sets the backup_network_nsg_ids of this CloudVmCluster.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param backup_network_nsg_ids: The backup_network_nsg_ids of this CloudVmCluster.
        :type: list[str]
        """
        self._backup_network_nsg_ids = backup_network_nsg_ids

    @property
    def last_update_history_entry_id(self):
        """
        Gets the last_update_history_entry_id of this CloudVmCluster.
        The `OCID`__ of the last maintenance update history entry. This value is updated when a maintenance update starts.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_update_history_entry_id of this CloudVmCluster.
        :rtype: str
        """
        return self._last_update_history_entry_id

    @last_update_history_entry_id.setter
    def last_update_history_entry_id(self, last_update_history_entry_id):
        """
        Sets the last_update_history_entry_id of this CloudVmCluster.
        The `OCID`__ of the last maintenance update history entry. This value is updated when a maintenance update starts.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_update_history_entry_id: The last_update_history_entry_id of this CloudVmCluster.
        :type: str
        """
        self._last_update_history_entry_id = last_update_history_entry_id

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CloudVmCluster.
        The model name of the Exadata hardware running the cloud VM cluster.


        :return: The shape of this CloudVmCluster.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CloudVmCluster.
        The model name of the Exadata hardware running the cloud VM cluster.


        :param shape: The shape of this CloudVmCluster.
        :type: str
        """
        self._shape = shape

    @property
    def listener_port(self):
        """
        Gets the listener_port of this CloudVmCluster.
        The port number configured for the listener on the cloud VM cluster.


        :return: The listener_port of this CloudVmCluster.
        :rtype: int
        """
        return self._listener_port

    @listener_port.setter
    def listener_port(self, listener_port):
        """
        Sets the listener_port of this CloudVmCluster.
        The port number configured for the listener on the cloud VM cluster.


        :param listener_port: The listener_port of this CloudVmCluster.
        :type: int
        """
        self._listener_port = listener_port

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CloudVmCluster.
        The current state of the cloud VM cluster.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CloudVmCluster.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CloudVmCluster.
        The current state of the cloud VM cluster.


        :param lifecycle_state: The lifecycle_state of this CloudVmCluster.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def node_count(self):
        """
        Gets the node_count of this CloudVmCluster.
        The number of nodes in the cloud VM cluster.


        :return: The node_count of this CloudVmCluster.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this CloudVmCluster.
        The number of nodes in the cloud VM cluster.


        :param node_count: The node_count of this CloudVmCluster.
        :type: int
        """
        self._node_count = node_count

    @property
    def storage_size_in_gbs(self):
        """
        Gets the storage_size_in_gbs of this CloudVmCluster.
        The storage allocation for the disk group, in gigabytes (GB).


        :return: The storage_size_in_gbs of this CloudVmCluster.
        :rtype: int
        """
        return self._storage_size_in_gbs

    @storage_size_in_gbs.setter
    def storage_size_in_gbs(self, storage_size_in_gbs):
        """
        Sets the storage_size_in_gbs of this CloudVmCluster.
        The storage allocation for the disk group, in gigabytes (GB).


        :param storage_size_in_gbs: The storage_size_in_gbs of this CloudVmCluster.
        :type: int
        """
        self._storage_size_in_gbs = storage_size_in_gbs

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CloudVmCluster.
        The user-friendly name for the cloud VM cluster. The name does not need to be unique.


        :return: The display_name of this CloudVmCluster.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CloudVmCluster.
        The user-friendly name for the cloud VM cluster. The name does not need to be unique.


        :param display_name: The display_name of this CloudVmCluster.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this CloudVmCluster.
        The date and time that the cloud VM cluster was created.


        :return: The time_created of this CloudVmCluster.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CloudVmCluster.
        The date and time that the cloud VM cluster was created.


        :param time_created: The time_created of this CloudVmCluster.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CloudVmCluster.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this CloudVmCluster.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CloudVmCluster.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this CloudVmCluster.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_zone(self):
        """
        Gets the time_zone of this CloudVmCluster.
        The time zone of the cloud VM cluster. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this CloudVmCluster.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this CloudVmCluster.
        The time zone of the cloud VM cluster. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this CloudVmCluster.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this CloudVmCluster.
        The hostname for the cloud VM cluster.


        :return: The hostname of this CloudVmCluster.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CloudVmCluster.
        The hostname for the cloud VM cluster.


        :param hostname: The hostname of this CloudVmCluster.
        :type: str
        """
        self._hostname = hostname

    @property
    def domain(self):
        """
        **[Required]** Gets the domain of this CloudVmCluster.
        The domain name for the cloud VM cluster.


        :return: The domain of this CloudVmCluster.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this CloudVmCluster.
        The domain name for the cloud VM cluster.


        :param domain: The domain of this CloudVmCluster.
        :type: str
        """
        self._domain = domain

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this CloudVmCluster.
        The number of CPU cores enabled on the cloud VM cluster.


        :return: The cpu_core_count of this CloudVmCluster.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CloudVmCluster.
        The number of CPU cores enabled on the cloud VM cluster.


        :param cpu_core_count: The cpu_core_count of this CloudVmCluster.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this CloudVmCluster.
        The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :return: The cluster_name of this CloudVmCluster.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this CloudVmCluster.
        The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :param cluster_name: The cluster_name of this CloudVmCluster.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def data_storage_percentage(self):
        """
        Gets the data_storage_percentage of this CloudVmCluster.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See `Storage Configuration`__ in the Exadata documentation for details on the impact of the configuration settings on storage.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/exaoverview.htm#Exadata


        :return: The data_storage_percentage of this CloudVmCluster.
        :rtype: int
        """
        return self._data_storage_percentage

    @data_storage_percentage.setter
    def data_storage_percentage(self, data_storage_percentage):
        """
        Sets the data_storage_percentage of this CloudVmCluster.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See `Storage Configuration`__ in the Exadata documentation for details on the impact of the configuration settings on storage.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/exaoverview.htm#Exadata


        :param data_storage_percentage: The data_storage_percentage of this CloudVmCluster.
        :type: int
        """
        self._data_storage_percentage = data_storage_percentage

    @property
    def is_local_backup_enabled(self):
        """
        Gets the is_local_backup_enabled of this CloudVmCluster.
        If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.


        :return: The is_local_backup_enabled of this CloudVmCluster.
        :rtype: bool
        """
        return self._is_local_backup_enabled

    @is_local_backup_enabled.setter
    def is_local_backup_enabled(self, is_local_backup_enabled):
        """
        Sets the is_local_backup_enabled of this CloudVmCluster.
        If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.


        :param is_local_backup_enabled: The is_local_backup_enabled of this CloudVmCluster.
        :type: bool
        """
        self._is_local_backup_enabled = is_local_backup_enabled

    @property
    def cloud_exadata_infrastructure_id(self):
        """
        **[Required]** Gets the cloud_exadata_infrastructure_id of this CloudVmCluster.
        The `OCID`__ of the cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_exadata_infrastructure_id of this CloudVmCluster.
        :rtype: str
        """
        return self._cloud_exadata_infrastructure_id

    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(self, cloud_exadata_infrastructure_id):
        """
        Sets the cloud_exadata_infrastructure_id of this CloudVmCluster.
        The `OCID`__ of the cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_exadata_infrastructure_id: The cloud_exadata_infrastructure_id of this CloudVmCluster.
        :type: str
        """
        self._cloud_exadata_infrastructure_id = cloud_exadata_infrastructure_id

    @property
    def is_sparse_diskgroup_enabled(self):
        """
        Gets the is_sparse_diskgroup_enabled of this CloudVmCluster.
        If true, sparse disk group is configured for the cloud VM cluster. If false, sparse disk group is not created.


        :return: The is_sparse_diskgroup_enabled of this CloudVmCluster.
        :rtype: bool
        """
        return self._is_sparse_diskgroup_enabled

    @is_sparse_diskgroup_enabled.setter
    def is_sparse_diskgroup_enabled(self, is_sparse_diskgroup_enabled):
        """
        Sets the is_sparse_diskgroup_enabled of this CloudVmCluster.
        If true, sparse disk group is configured for the cloud VM cluster. If false, sparse disk group is not created.


        :param is_sparse_diskgroup_enabled: The is_sparse_diskgroup_enabled of this CloudVmCluster.
        :type: bool
        """
        self._is_sparse_diskgroup_enabled = is_sparse_diskgroup_enabled

    @property
    def gi_version(self):
        """
        Gets the gi_version of this CloudVmCluster.
        A valid Oracle Grid Infrastructure (GI) software version.


        :return: The gi_version of this CloudVmCluster.
        :rtype: str
        """
        return self._gi_version

    @gi_version.setter
    def gi_version(self, gi_version):
        """
        Sets the gi_version of this CloudVmCluster.
        A valid Oracle Grid Infrastructure (GI) software version.


        :param gi_version: The gi_version of this CloudVmCluster.
        :type: str
        """
        self._gi_version = gi_version

    @property
    def system_version(self):
        """
        Gets the system_version of this CloudVmCluster.
        Operating system version of the image.


        :return: The system_version of this CloudVmCluster.
        :rtype: str
        """
        return self._system_version

    @system_version.setter
    def system_version(self, system_version):
        """
        Sets the system_version of this CloudVmCluster.
        Operating system version of the image.


        :param system_version: The system_version of this CloudVmCluster.
        :type: str
        """
        self._system_version = system_version

    @property
    def ssh_public_keys(self):
        """
        **[Required]** Gets the ssh_public_keys of this CloudVmCluster.
        The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.


        :return: The ssh_public_keys of this CloudVmCluster.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this CloudVmCluster.
        The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.


        :param ssh_public_keys: The ssh_public_keys of this CloudVmCluster.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def license_model(self):
        """
        Gets the license_model of this CloudVmCluster.
        The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this CloudVmCluster.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CloudVmCluster.
        The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED.


        :param license_model: The license_model of this CloudVmCluster.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def disk_redundancy(self):
        """
        Gets the disk_redundancy of this CloudVmCluster.
        The type of redundancy configured for the cloud Vm cluster.
        NORMAL is 2-way redundancy.
        HIGH is 3-way redundancy.

        Allowed values for this property are: "HIGH", "NORMAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The disk_redundancy of this CloudVmCluster.
        :rtype: str
        """
        return self._disk_redundancy

    @disk_redundancy.setter
    def disk_redundancy(self, disk_redundancy):
        """
        Sets the disk_redundancy of this CloudVmCluster.
        The type of redundancy configured for the cloud Vm cluster.
        NORMAL is 2-way redundancy.
        HIGH is 3-way redundancy.


        :param disk_redundancy: The disk_redundancy of this CloudVmCluster.
        :type: str
        """
        allowed_values = ["HIGH", "NORMAL"]
        if not value_allowed_none_or_none_sentinel(disk_redundancy, allowed_values):
            disk_redundancy = 'UNKNOWN_ENUM_VALUE'
        self._disk_redundancy = disk_redundancy

    @property
    def scan_ip_ids(self):
        """
        Gets the scan_ip_ids of this CloudVmCluster.
        The `OCID`__ of the Single Client Access Name (SCAN) IP addresses associated with the cloud VM cluster.
        SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
        Oracle Clusterware directs the requests to the appropriate nodes in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The scan_ip_ids of this CloudVmCluster.
        :rtype: list[str]
        """
        return self._scan_ip_ids

    @scan_ip_ids.setter
    def scan_ip_ids(self, scan_ip_ids):
        """
        Sets the scan_ip_ids of this CloudVmCluster.
        The `OCID`__ of the Single Client Access Name (SCAN) IP addresses associated with the cloud VM cluster.
        SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
        Oracle Clusterware directs the requests to the appropriate nodes in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param scan_ip_ids: The scan_ip_ids of this CloudVmCluster.
        :type: list[str]
        """
        self._scan_ip_ids = scan_ip_ids

    @property
    def vip_ids(self):
        """
        Gets the vip_ids of this CloudVmCluster.
        The `OCID`__ of the virtual IP (VIP) addresses associated with the cloud VM cluster.
        The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to
        enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vip_ids of this CloudVmCluster.
        :rtype: list[str]
        """
        return self._vip_ids

    @vip_ids.setter
    def vip_ids(self, vip_ids):
        """
        Sets the vip_ids of this CloudVmCluster.
        The `OCID`__ of the virtual IP (VIP) addresses associated with the cloud VM cluster.
        The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to
        enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vip_ids: The vip_ids of this CloudVmCluster.
        :type: list[str]
        """
        self._vip_ids = vip_ids

    @property
    def scan_dns_record_id(self):
        """
        Gets the scan_dns_record_id of this CloudVmCluster.
        The `OCID`__ of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The scan_dns_record_id of this CloudVmCluster.
        :rtype: str
        """
        return self._scan_dns_record_id

    @scan_dns_record_id.setter
    def scan_dns_record_id(self, scan_dns_record_id):
        """
        Sets the scan_dns_record_id of this CloudVmCluster.
        The `OCID`__ of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param scan_dns_record_id: The scan_dns_record_id of this CloudVmCluster.
        :type: str
        """
        self._scan_dns_record_id = scan_dns_record_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CloudVmCluster.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CloudVmCluster.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CloudVmCluster.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CloudVmCluster.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CloudVmCluster.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CloudVmCluster.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CloudVmCluster.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CloudVmCluster.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def scan_dns_name(self):
        """
        Gets the scan_dns_name of this CloudVmCluster.
        The FQDN of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.


        :return: The scan_dns_name of this CloudVmCluster.
        :rtype: str
        """
        return self._scan_dns_name

    @scan_dns_name.setter
    def scan_dns_name(self, scan_dns_name):
        """
        Sets the scan_dns_name of this CloudVmCluster.
        The FQDN of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.


        :param scan_dns_name: The scan_dns_name of this CloudVmCluster.
        :type: str
        """
        self._scan_dns_name = scan_dns_name

    @property
    def zone_id(self):
        """
        Gets the zone_id of this CloudVmCluster.
        The OCID of the zone the cloud VM cluster is associated with.


        :return: The zone_id of this CloudVmCluster.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """
        Sets the zone_id of this CloudVmCluster.
        The OCID of the zone the cloud VM cluster is associated with.


        :param zone_id: The zone_id of this CloudVmCluster.
        :type: str
        """
        self._zone_id = zone_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
