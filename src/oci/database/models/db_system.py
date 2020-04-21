# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystem(object):
    """
    DbSystem model.
    """

    #: A constant which can be used with the database_edition property of a DbSystem.
    #: This constant has a value of "STANDARD_EDITION"
    DATABASE_EDITION_STANDARD_EDITION = "STANDARD_EDITION"

    #: A constant which can be used with the database_edition property of a DbSystem.
    #: This constant has a value of "ENTERPRISE_EDITION"
    DATABASE_EDITION_ENTERPRISE_EDITION = "ENTERPRISE_EDITION"

    #: A constant which can be used with the database_edition property of a DbSystem.
    #: This constant has a value of "ENTERPRISE_EDITION_HIGH_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_HIGH_PERFORMANCE = "ENTERPRISE_EDITION_HIGH_PERFORMANCE"

    #: A constant which can be used with the database_edition property of a DbSystem.
    #: This constant has a value of "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_EXTREME_PERFORMANCE = "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the disk_redundancy property of a DbSystem.
    #: This constant has a value of "HIGH"
    DISK_REDUNDANCY_HIGH = "HIGH"

    #: A constant which can be used with the disk_redundancy property of a DbSystem.
    #: This constant has a value of "NORMAL"
    DISK_REDUNDANCY_NORMAL = "NORMAL"

    #: A constant which can be used with the license_model property of a DbSystem.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a DbSystem.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param iorm_config_cache:
            The value to assign to the iorm_config_cache property of this DbSystem.
        :type iorm_config_cache: ExadataIormConfig

        :param id:
            The value to assign to the id property of this DbSystem.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DbSystem.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DbSystem.
        :type display_name: str

        :param availability_domain:
            The value to assign to the availability_domain property of this DbSystem.
        :type availability_domain: str

        :param fault_domains:
            The value to assign to the fault_domains property of this DbSystem.
        :type fault_domains: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this DbSystem.
        :type subnet_id: str

        :param backup_subnet_id:
            The value to assign to the backup_subnet_id property of this DbSystem.
        :type backup_subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this DbSystem.
        :type nsg_ids: list[str]

        :param backup_network_nsg_ids:
            The value to assign to the backup_network_nsg_ids property of this DbSystem.
        :type backup_network_nsg_ids: list[str]

        :param shape:
            The value to assign to the shape property of this DbSystem.
        :type shape: str

        :param db_system_options:
            The value to assign to the db_system_options property of this DbSystem.
        :type db_system_options: DbSystemOptions

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this DbSystem.
        :type ssh_public_keys: list[str]

        :param time_zone:
            The value to assign to the time_zone property of this DbSystem.
        :type time_zone: str

        :param hostname:
            The value to assign to the hostname property of this DbSystem.
        :type hostname: str

        :param domain:
            The value to assign to the domain property of this DbSystem.
        :type domain: str

        :param version:
            The value to assign to the version property of this DbSystem.
        :type version: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this DbSystem.
        :type cpu_core_count: int

        :param cluster_name:
            The value to assign to the cluster_name property of this DbSystem.
        :type cluster_name: str

        :param data_storage_percentage:
            The value to assign to the data_storage_percentage property of this DbSystem.
        :type data_storage_percentage: int

        :param database_edition:
            The value to assign to the database_edition property of this DbSystem.
            Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_edition: str

        :param last_patch_history_entry_id:
            The value to assign to the last_patch_history_entry_id property of this DbSystem.
        :type last_patch_history_entry_id: str

        :param listener_port:
            The value to assign to the listener_port property of this DbSystem.
        :type listener_port: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbSystem.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this DbSystem.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DbSystem.
        :type lifecycle_details: str

        :param disk_redundancy:
            The value to assign to the disk_redundancy property of this DbSystem.
            Allowed values for this property are: "HIGH", "NORMAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type disk_redundancy: str

        :param sparse_diskgroup:
            The value to assign to the sparse_diskgroup property of this DbSystem.
        :type sparse_diskgroup: bool

        :param scan_ip_ids:
            The value to assign to the scan_ip_ids property of this DbSystem.
        :type scan_ip_ids: list[str]

        :param vip_ids:
            The value to assign to the vip_ids property of this DbSystem.
        :type vip_ids: list[str]

        :param scan_dns_record_id:
            The value to assign to the scan_dns_record_id property of this DbSystem.
        :type scan_dns_record_id: str

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this DbSystem.
        :type data_storage_size_in_gbs: int

        :param reco_storage_size_in_gb:
            The value to assign to the reco_storage_size_in_gb property of this DbSystem.
        :type reco_storage_size_in_gb: int

        :param node_count:
            The value to assign to the node_count property of this DbSystem.
        :type node_count: int

        :param license_model:
            The value to assign to the license_model property of this DbSystem.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param maintenance_window:
            The value to assign to the maintenance_window property of this DbSystem.
        :type maintenance_window: MaintenanceWindow

        :param last_maintenance_run_id:
            The value to assign to the last_maintenance_run_id property of this DbSystem.
        :type last_maintenance_run_id: str

        :param next_maintenance_run_id:
            The value to assign to the next_maintenance_run_id property of this DbSystem.
        :type next_maintenance_run_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DbSystem.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DbSystem.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'iorm_config_cache': 'ExadataIormConfig',
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'availability_domain': 'str',
            'fault_domains': 'list[str]',
            'subnet_id': 'str',
            'backup_subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'backup_network_nsg_ids': 'list[str]',
            'shape': 'str',
            'db_system_options': 'DbSystemOptions',
            'ssh_public_keys': 'list[str]',
            'time_zone': 'str',
            'hostname': 'str',
            'domain': 'str',
            'version': 'str',
            'cpu_core_count': 'int',
            'cluster_name': 'str',
            'data_storage_percentage': 'int',
            'database_edition': 'str',
            'last_patch_history_entry_id': 'str',
            'listener_port': 'int',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'disk_redundancy': 'str',
            'sparse_diskgroup': 'bool',
            'scan_ip_ids': 'list[str]',
            'vip_ids': 'list[str]',
            'scan_dns_record_id': 'str',
            'data_storage_size_in_gbs': 'int',
            'reco_storage_size_in_gb': 'int',
            'node_count': 'int',
            'license_model': 'str',
            'maintenance_window': 'MaintenanceWindow',
            'last_maintenance_run_id': 'str',
            'next_maintenance_run_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'iorm_config_cache': 'iormConfigCache',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'availability_domain': 'availabilityDomain',
            'fault_domains': 'faultDomains',
            'subnet_id': 'subnetId',
            'backup_subnet_id': 'backupSubnetId',
            'nsg_ids': 'nsgIds',
            'backup_network_nsg_ids': 'backupNetworkNsgIds',
            'shape': 'shape',
            'db_system_options': 'dbSystemOptions',
            'ssh_public_keys': 'sshPublicKeys',
            'time_zone': 'timeZone',
            'hostname': 'hostname',
            'domain': 'domain',
            'version': 'version',
            'cpu_core_count': 'cpuCoreCount',
            'cluster_name': 'clusterName',
            'data_storage_percentage': 'dataStoragePercentage',
            'database_edition': 'databaseEdition',
            'last_patch_history_entry_id': 'lastPatchHistoryEntryId',
            'listener_port': 'listenerPort',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'disk_redundancy': 'diskRedundancy',
            'sparse_diskgroup': 'sparseDiskgroup',
            'scan_ip_ids': 'scanIpIds',
            'vip_ids': 'vipIds',
            'scan_dns_record_id': 'scanDnsRecordId',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'reco_storage_size_in_gb': 'recoStorageSizeInGB',
            'node_count': 'nodeCount',
            'license_model': 'licenseModel',
            'maintenance_window': 'maintenanceWindow',
            'last_maintenance_run_id': 'lastMaintenanceRunId',
            'next_maintenance_run_id': 'nextMaintenanceRunId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._iorm_config_cache = None
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._availability_domain = None
        self._fault_domains = None
        self._subnet_id = None
        self._backup_subnet_id = None
        self._nsg_ids = None
        self._backup_network_nsg_ids = None
        self._shape = None
        self._db_system_options = None
        self._ssh_public_keys = None
        self._time_zone = None
        self._hostname = None
        self._domain = None
        self._version = None
        self._cpu_core_count = None
        self._cluster_name = None
        self._data_storage_percentage = None
        self._database_edition = None
        self._last_patch_history_entry_id = None
        self._listener_port = None
        self._lifecycle_state = None
        self._time_created = None
        self._lifecycle_details = None
        self._disk_redundancy = None
        self._sparse_diskgroup = None
        self._scan_ip_ids = None
        self._vip_ids = None
        self._scan_dns_record_id = None
        self._data_storage_size_in_gbs = None
        self._reco_storage_size_in_gb = None
        self._node_count = None
        self._license_model = None
        self._maintenance_window = None
        self._last_maintenance_run_id = None
        self._next_maintenance_run_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def iorm_config_cache(self):
        """
        Gets the iorm_config_cache of this DbSystem.

        :return: The iorm_config_cache of this DbSystem.
        :rtype: ExadataIormConfig
        """
        return self._iorm_config_cache

    @iorm_config_cache.setter
    def iorm_config_cache(self, iorm_config_cache):
        """
        Sets the iorm_config_cache of this DbSystem.

        :param iorm_config_cache: The iorm_config_cache of this DbSystem.
        :type: ExadataIormConfig
        """
        self._iorm_config_cache = iorm_config_cache

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbSystem.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DbSystem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbSystem.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DbSystem.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DbSystem.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DbSystem.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbSystem.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DbSystem.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DbSystem.
        The user-friendly name for the DB system. The name does not have to be unique.


        :return: The display_name of this DbSystem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DbSystem.
        The user-friendly name for the DB system. The name does not have to be unique.


        :param display_name: The display_name of this DbSystem.
        :type: str
        """
        self._display_name = display_name

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this DbSystem.
        The name of the availability domain that the DB system is located in.


        :return: The availability_domain of this DbSystem.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DbSystem.
        The name of the availability domain that the DB system is located in.


        :param availability_domain: The availability_domain of this DbSystem.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domains(self):
        """
        Gets the fault_domains of this DbSystem.
        List of the Fault Domains in which this DB system is provisioned.


        :return: The fault_domains of this DbSystem.
        :rtype: list[str]
        """
        return self._fault_domains

    @fault_domains.setter
    def fault_domains(self, fault_domains):
        """
        Sets the fault_domains of this DbSystem.
        List of the Fault Domains in which this DB system is provisioned.


        :param fault_domains: The fault_domains of this DbSystem.
        :type: list[str]
        """
        self._fault_domains = fault_domains

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DbSystem.
        The `OCID`__ of the subnet the DB system is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this DbSystem.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DbSystem.
        The `OCID`__ of the subnet the DB system is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this DbSystem.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def backup_subnet_id(self):
        """
        Gets the backup_subnet_id of this DbSystem.
        The `OCID`__ of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

        **Subnet Restriction:** See the subnet restrictions information for **subnetId**.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The backup_subnet_id of this DbSystem.
        :rtype: str
        """
        return self._backup_subnet_id

    @backup_subnet_id.setter
    def backup_subnet_id(self, backup_subnet_id):
        """
        Sets the backup_subnet_id of this DbSystem.
        The `OCID`__ of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

        **Subnet Restriction:** See the subnet restrictions information for **subnetId**.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param backup_subnet_id: The backup_subnet_id of this DbSystem.
        :type: str
        """
        self._backup_subnet_id = backup_subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this DbSystem.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this DbSystem.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this DbSystem.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this DbSystem.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def backup_network_nsg_ids(self):
        """
        Gets the backup_network_nsg_ids of this DbSystem.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata DB systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The backup_network_nsg_ids of this DbSystem.
        :rtype: list[str]
        """
        return self._backup_network_nsg_ids

    @backup_network_nsg_ids.setter
    def backup_network_nsg_ids(self, backup_network_nsg_ids):
        """
        Sets the backup_network_nsg_ids of this DbSystem.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata DB systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param backup_network_nsg_ids: The backup_network_nsg_ids of this DbSystem.
        :type: list[str]
        """
        self._backup_network_nsg_ids = backup_network_nsg_ids

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this DbSystem.
        The shape of the DB system. The shape determines resources to allocate to the DB system.
        - For virtual machine shapes, the number of CPU cores and memory
        - For bare metal and Exadata shapes, the number of CPU cores, storage, and memory


        :return: The shape of this DbSystem.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DbSystem.
        The shape of the DB system. The shape determines resources to allocate to the DB system.
        - For virtual machine shapes, the number of CPU cores and memory
        - For bare metal and Exadata shapes, the number of CPU cores, storage, and memory


        :param shape: The shape of this DbSystem.
        :type: str
        """
        self._shape = shape

    @property
    def db_system_options(self):
        """
        Gets the db_system_options of this DbSystem.

        :return: The db_system_options of this DbSystem.
        :rtype: DbSystemOptions
        """
        return self._db_system_options

    @db_system_options.setter
    def db_system_options(self, db_system_options):
        """
        Sets the db_system_options of this DbSystem.

        :param db_system_options: The db_system_options of this DbSystem.
        :type: DbSystemOptions
        """
        self._db_system_options = db_system_options

    @property
    def ssh_public_keys(self):
        """
        **[Required]** Gets the ssh_public_keys of this DbSystem.
        The public key portion of one or more key pairs used for SSH access to the DB system.


        :return: The ssh_public_keys of this DbSystem.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this DbSystem.
        The public key portion of one or more key pairs used for SSH access to the DB system.


        :param ssh_public_keys: The ssh_public_keys of this DbSystem.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def time_zone(self):
        """
        Gets the time_zone of this DbSystem.
        The time zone of the DB system. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this DbSystem.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this DbSystem.
        The time zone of the DB system. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this DbSystem.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this DbSystem.
        The hostname for the DB system.


        :return: The hostname of this DbSystem.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this DbSystem.
        The hostname for the DB system.


        :param hostname: The hostname of this DbSystem.
        :type: str
        """
        self._hostname = hostname

    @property
    def domain(self):
        """
        **[Required]** Gets the domain of this DbSystem.
        The domain name for the DB system.


        :return: The domain of this DbSystem.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this DbSystem.
        The domain name for the DB system.


        :param domain: The domain of this DbSystem.
        :type: str
        """
        self._domain = domain

    @property
    def version(self):
        """
        Gets the version of this DbSystem.
        The Oracle Database version of the DB system.


        :return: The version of this DbSystem.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DbSystem.
        The Oracle Database version of the DB system.


        :param version: The version of this DbSystem.
        :type: str
        """
        self._version = version

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this DbSystem.
        The number of CPU cores enabled on the DB system.


        :return: The cpu_core_count of this DbSystem.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this DbSystem.
        The number of CPU cores enabled on the DB system.


        :param cpu_core_count: The cpu_core_count of this DbSystem.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this DbSystem.
        The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :return: The cluster_name of this DbSystem.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this DbSystem.
        The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :param cluster_name: The cluster_name of this DbSystem.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def data_storage_percentage(self):
        """
        Gets the data_storage_percentage of this DbSystem.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 40 and 80. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.


        :return: The data_storage_percentage of this DbSystem.
        :rtype: int
        """
        return self._data_storage_percentage

    @data_storage_percentage.setter
    def data_storage_percentage(self, data_storage_percentage):
        """
        Sets the data_storage_percentage of this DbSystem.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 40 and 80. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.


        :param data_storage_percentage: The data_storage_percentage of this DbSystem.
        :type: int
        """
        self._data_storage_percentage = data_storage_percentage

    @property
    def database_edition(self):
        """
        **[Required]** Gets the database_edition of this DbSystem.
        The Oracle Database edition that applies to all the databases on the DB system.

        Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_edition of this DbSystem.
        :rtype: str
        """
        return self._database_edition

    @database_edition.setter
    def database_edition(self, database_edition):
        """
        Sets the database_edition of this DbSystem.
        The Oracle Database edition that applies to all the databases on the DB system.


        :param database_edition: The database_edition of this DbSystem.
        :type: str
        """
        allowed_values = ["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]
        if not value_allowed_none_or_none_sentinel(database_edition, allowed_values):
            database_edition = 'UNKNOWN_ENUM_VALUE'
        self._database_edition = database_edition

    @property
    def last_patch_history_entry_id(self):
        """
        Gets the last_patch_history_entry_id of this DbSystem.
        The `OCID`__ of the last patch history. This value is updated as soon as a patch operation starts.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_patch_history_entry_id of this DbSystem.
        :rtype: str
        """
        return self._last_patch_history_entry_id

    @last_patch_history_entry_id.setter
    def last_patch_history_entry_id(self, last_patch_history_entry_id):
        """
        Sets the last_patch_history_entry_id of this DbSystem.
        The `OCID`__ of the last patch history. This value is updated as soon as a patch operation starts.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_patch_history_entry_id: The last_patch_history_entry_id of this DbSystem.
        :type: str
        """
        self._last_patch_history_entry_id = last_patch_history_entry_id

    @property
    def listener_port(self):
        """
        Gets the listener_port of this DbSystem.
        The port number configured for the listener on the DB system.


        :return: The listener_port of this DbSystem.
        :rtype: int
        """
        return self._listener_port

    @listener_port.setter
    def listener_port(self, listener_port):
        """
        Sets the listener_port of this DbSystem.
        The port number configured for the listener on the DB system.


        :param listener_port: The listener_port of this DbSystem.
        :type: int
        """
        self._listener_port = listener_port

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DbSystem.
        The current state of the DB system.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbSystem.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbSystem.
        The current state of the DB system.


        :param lifecycle_state: The lifecycle_state of this DbSystem.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this DbSystem.
        The date and time the DB system was created.


        :return: The time_created of this DbSystem.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbSystem.
        The date and time the DB system was created.


        :param time_created: The time_created of this DbSystem.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DbSystem.
        Additional information about the current lifecycleState.


        :return: The lifecycle_details of this DbSystem.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DbSystem.
        Additional information about the current lifecycleState.


        :param lifecycle_details: The lifecycle_details of this DbSystem.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def disk_redundancy(self):
        """
        Gets the disk_redundancy of this DbSystem.
        The type of redundancy configured for the DB system.
        NORMAL is 2-way redundancy.
        HIGH is 3-way redundancy.

        Allowed values for this property are: "HIGH", "NORMAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The disk_redundancy of this DbSystem.
        :rtype: str
        """
        return self._disk_redundancy

    @disk_redundancy.setter
    def disk_redundancy(self, disk_redundancy):
        """
        Sets the disk_redundancy of this DbSystem.
        The type of redundancy configured for the DB system.
        NORMAL is 2-way redundancy.
        HIGH is 3-way redundancy.


        :param disk_redundancy: The disk_redundancy of this DbSystem.
        :type: str
        """
        allowed_values = ["HIGH", "NORMAL"]
        if not value_allowed_none_or_none_sentinel(disk_redundancy, allowed_values):
            disk_redundancy = 'UNKNOWN_ENUM_VALUE'
        self._disk_redundancy = disk_redundancy

    @property
    def sparse_diskgroup(self):
        """
        Gets the sparse_diskgroup of this DbSystem.
        True, if Sparse Diskgroup is configured for Exadata dbsystem, False, if Sparse diskgroup was not configured.


        :return: The sparse_diskgroup of this DbSystem.
        :rtype: bool
        """
        return self._sparse_diskgroup

    @sparse_diskgroup.setter
    def sparse_diskgroup(self, sparse_diskgroup):
        """
        Sets the sparse_diskgroup of this DbSystem.
        True, if Sparse Diskgroup is configured for Exadata dbsystem, False, if Sparse diskgroup was not configured.


        :param sparse_diskgroup: The sparse_diskgroup of this DbSystem.
        :type: bool
        """
        self._sparse_diskgroup = sparse_diskgroup

    @property
    def scan_ip_ids(self):
        """
        Gets the scan_ip_ids of this DbSystem.
        The `OCID`__ of the Single Client Access Name (SCAN) IP addresses associated with the DB system.
        SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
        Oracle Clusterware directs the requests to the appropriate nodes in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The scan_ip_ids of this DbSystem.
        :rtype: list[str]
        """
        return self._scan_ip_ids

    @scan_ip_ids.setter
    def scan_ip_ids(self, scan_ip_ids):
        """
        Sets the scan_ip_ids of this DbSystem.
        The `OCID`__ of the Single Client Access Name (SCAN) IP addresses associated with the DB system.
        SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
        Oracle Clusterware directs the requests to the appropriate nodes in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param scan_ip_ids: The scan_ip_ids of this DbSystem.
        :type: list[str]
        """
        self._scan_ip_ids = scan_ip_ids

    @property
    def vip_ids(self):
        """
        Gets the vip_ids of this DbSystem.
        The `OCID`__ of the virtual IP (VIP) addresses associated with the DB system.
        The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB system to
        enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vip_ids of this DbSystem.
        :rtype: list[str]
        """
        return self._vip_ids

    @vip_ids.setter
    def vip_ids(self, vip_ids):
        """
        Sets the vip_ids of this DbSystem.
        The `OCID`__ of the virtual IP (VIP) addresses associated with the DB system.
        The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB system to
        enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vip_ids: The vip_ids of this DbSystem.
        :type: list[str]
        """
        self._vip_ids = vip_ids

    @property
    def scan_dns_record_id(self):
        """
        Gets the scan_dns_record_id of this DbSystem.
        The `OCID`__ of the DNS record for the SCAN IP addresses that are associated with the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The scan_dns_record_id of this DbSystem.
        :rtype: str
        """
        return self._scan_dns_record_id

    @scan_dns_record_id.setter
    def scan_dns_record_id(self, scan_dns_record_id):
        """
        Sets the scan_dns_record_id of this DbSystem.
        The `OCID`__ of the DNS record for the SCAN IP addresses that are associated with the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param scan_dns_record_id: The scan_dns_record_id of this DbSystem.
        :type: str
        """
        self._scan_dns_record_id = scan_dns_record_id

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this DbSystem.
        The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.


        :return: The data_storage_size_in_gbs of this DbSystem.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this DbSystem.
        The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this DbSystem.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def reco_storage_size_in_gb(self):
        """
        Gets the reco_storage_size_in_gb of this DbSystem.
        The RECO/REDO storage size, in gigabytes, that is currently allocated to the DB system. Applies only for virtual machine DB systems.


        :return: The reco_storage_size_in_gb of this DbSystem.
        :rtype: int
        """
        return self._reco_storage_size_in_gb

    @reco_storage_size_in_gb.setter
    def reco_storage_size_in_gb(self, reco_storage_size_in_gb):
        """
        Sets the reco_storage_size_in_gb of this DbSystem.
        The RECO/REDO storage size, in gigabytes, that is currently allocated to the DB system. Applies only for virtual machine DB systems.


        :param reco_storage_size_in_gb: The reco_storage_size_in_gb of this DbSystem.
        :type: int
        """
        self._reco_storage_size_in_gb = reco_storage_size_in_gb

    @property
    def node_count(self):
        """
        Gets the node_count of this DbSystem.
        The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.


        :return: The node_count of this DbSystem.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this DbSystem.
        The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.


        :param node_count: The node_count of this DbSystem.
        :type: int
        """
        self._node_count = node_count

    @property
    def license_model(self):
        """
        Gets the license_model of this DbSystem.
        The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this DbSystem.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this DbSystem.
        The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.


        :param license_model: The license_model of this DbSystem.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def maintenance_window(self):
        """
        Gets the maintenance_window of this DbSystem.

        :return: The maintenance_window of this DbSystem.
        :rtype: MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """
        Sets the maintenance_window of this DbSystem.

        :param maintenance_window: The maintenance_window of this DbSystem.
        :type: MaintenanceWindow
        """
        self._maintenance_window = maintenance_window

    @property
    def last_maintenance_run_id(self):
        """
        Gets the last_maintenance_run_id of this DbSystem.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_maintenance_run_id of this DbSystem.
        :rtype: str
        """
        return self._last_maintenance_run_id

    @last_maintenance_run_id.setter
    def last_maintenance_run_id(self, last_maintenance_run_id):
        """
        Sets the last_maintenance_run_id of this DbSystem.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_maintenance_run_id: The last_maintenance_run_id of this DbSystem.
        :type: str
        """
        self._last_maintenance_run_id = last_maintenance_run_id

    @property
    def next_maintenance_run_id(self):
        """
        Gets the next_maintenance_run_id of this DbSystem.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The next_maintenance_run_id of this DbSystem.
        :rtype: str
        """
        return self._next_maintenance_run_id

    @next_maintenance_run_id.setter
    def next_maintenance_run_id(self, next_maintenance_run_id):
        """
        Sets the next_maintenance_run_id of this DbSystem.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param next_maintenance_run_id: The next_maintenance_run_id of this DbSystem.
        :type: str
        """
        self._next_maintenance_run_id = next_maintenance_run_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DbSystem.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DbSystem.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DbSystem.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DbSystem.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DbSystem.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DbSystem.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DbSystem.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DbSystem.
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
