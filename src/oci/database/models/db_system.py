# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class DbSystem(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'backup_subnet_id': 'str',
            'cluster_name': 'str',
            'compartment_id': 'str',
            'cpu_core_count': 'int',
            'data_storage_percentage': 'int',
            'database_edition': 'str',
            'disk_redundancy': 'str',
            'display_name': 'str',
            'domain': 'str',
            'hostname': 'str',
            'id': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'listener_port': 'int',
            'scan_dns_record_id': 'str',
            'scan_ip_ids': 'list[str]',
            'shape': 'str',
            'ssh_public_keys': 'list[str]',
            'subnet_id': 'str',
            'time_created': 'datetime',
            'version': 'str',
            'vip_ids': 'list[str]'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'backup_subnet_id': 'backupSubnetId',
            'cluster_name': 'clusterName',
            'compartment_id': 'compartmentId',
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_percentage': 'dataStoragePercentage',
            'database_edition': 'databaseEdition',
            'disk_redundancy': 'diskRedundancy',
            'display_name': 'displayName',
            'domain': 'domain',
            'hostname': 'hostname',
            'id': 'id',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'listener_port': 'listenerPort',
            'scan_dns_record_id': 'scanDnsRecordId',
            'scan_ip_ids': 'scanIpIds',
            'shape': 'shape',
            'ssh_public_keys': 'sshPublicKeys',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated',
            'version': 'version',
            'vip_ids': 'vipIds'
        }

        self._availability_domain = None
        self._backup_subnet_id = None
        self._cluster_name = None
        self._compartment_id = None
        self._cpu_core_count = None
        self._data_storage_percentage = None
        self._database_edition = None
        self._disk_redundancy = None
        self._display_name = None
        self._domain = None
        self._hostname = None
        self._id = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._listener_port = None
        self._scan_dns_record_id = None
        self._scan_ip_ids = None
        self._shape = None
        self._ssh_public_keys = None
        self._subnet_id = None
        self._time_created = None
        self._version = None
        self._vip_ids = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this DbSystem.
        The name of the Availability Domain that the DB System is located in.


        :return: The availability_domain of this DbSystem.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DbSystem.
        The name of the Availability Domain that the DB System is located in.


        :param availability_domain: The availability_domain of this DbSystem.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def backup_subnet_id(self):
        """
        Gets the backup_subnet_id of this DbSystem.
        The OCID of the backup network subnet the DB System is associated with. Applicable only to Exadata.

        **Subnet Restriction:** See above subnetId's 'Subnet Restriction'.
        to malfunction.


        :return: The backup_subnet_id of this DbSystem.
        :rtype: str
        """
        return self._backup_subnet_id

    @backup_subnet_id.setter
    def backup_subnet_id(self, backup_subnet_id):
        """
        Sets the backup_subnet_id of this DbSystem.
        The OCID of the backup network subnet the DB System is associated with. Applicable only to Exadata.

        **Subnet Restriction:** See above subnetId's 'Subnet Restriction'.
        to malfunction.


        :param backup_subnet_id: The backup_subnet_id of this DbSystem.
        :type: str
        """
        self._backup_subnet_id = backup_subnet_id

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this DbSystem.
        Cluster name for Exadata and 2-node RAC DB Systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :return: The cluster_name of this DbSystem.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this DbSystem.
        Cluster name for Exadata and 2-node RAC DB Systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :param cluster_name: The cluster_name of this DbSystem.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DbSystem.
        The OCID of the compartment.


        :return: The compartment_id of this DbSystem.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbSystem.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this DbSystem.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this DbSystem.
        The number of CPU cores enabled on the DB System.


        :return: The cpu_core_count of this DbSystem.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this DbSystem.
        The number of CPU cores enabled on the DB System.


        :param cpu_core_count: The cpu_core_count of this DbSystem.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def data_storage_percentage(self):
        """
        Gets the data_storage_percentage of this DbSystem.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 40 and 80.


        :return: The data_storage_percentage of this DbSystem.
        :rtype: int
        """
        return self._data_storage_percentage

    @data_storage_percentage.setter
    def data_storage_percentage(self, data_storage_percentage):
        """
        Sets the data_storage_percentage of this DbSystem.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 40 and 80.


        :param data_storage_percentage: The data_storage_percentage of this DbSystem.
        :type: int
        """
        self._data_storage_percentage = data_storage_percentage

    @property
    def database_edition(self):
        """
        Gets the database_edition of this DbSystem.
        The Oracle Database Edition that applies to all the databases on the DB System.

        Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_edition of this DbSystem.
        :rtype: str
        """
        return self._database_edition

    @database_edition.setter
    def database_edition(self, database_edition):
        """
        Sets the database_edition of this DbSystem.
        The Oracle Database Edition that applies to all the databases on the DB System.


        :param database_edition: The database_edition of this DbSystem.
        :type: str
        """
        allowed_values = ["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE", "ENTERPRISE_EDITION_HIGH_PERFORMANCE"]
        if database_edition not in allowed_values:
            database_edition = 'UNKNOWN_ENUM_VALUE'
        self._database_edition = database_edition

    @property
    def disk_redundancy(self):
        """
        Gets the disk_redundancy of this DbSystem.
        The type of redundancy configured for the DB System.
        Normal is 2-way redundancy.
        High is 3-way redundancy.

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
        The type of redundancy configured for the DB System.
        Normal is 2-way redundancy.
        High is 3-way redundancy.


        :param disk_redundancy: The disk_redundancy of this DbSystem.
        :type: str
        """
        allowed_values = ["HIGH", "NORMAL"]
        if disk_redundancy not in allowed_values:
            disk_redundancy = 'UNKNOWN_ENUM_VALUE'
        self._disk_redundancy = disk_redundancy

    @property
    def display_name(self):
        """
        Gets the display_name of this DbSystem.
        The user-friendly name for the DB System. It does not have to be unique.


        :return: The display_name of this DbSystem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DbSystem.
        The user-friendly name for the DB System. It does not have to be unique.


        :param display_name: The display_name of this DbSystem.
        :type: str
        """
        self._display_name = display_name

    @property
    def domain(self):
        """
        Gets the domain of this DbSystem.
        The domain name for the DB System.


        :return: The domain of this DbSystem.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this DbSystem.
        The domain name for the DB System.


        :param domain: The domain of this DbSystem.
        :type: str
        """
        self._domain = domain

    @property
    def hostname(self):
        """
        Gets the hostname of this DbSystem.
        The host name for the DB Node.


        :return: The hostname of this DbSystem.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this DbSystem.
        The host name for the DB Node.


        :param hostname: The hostname of this DbSystem.
        :type: str
        """
        self._hostname = hostname

    @property
    def id(self):
        """
        Gets the id of this DbSystem.
        The OCID of the DB System.


        :return: The id of this DbSystem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbSystem.
        The OCID of the DB System.


        :param id: The id of this DbSystem.
        :type: str
        """
        self._id = id

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
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DbSystem.
        The current state of the DB System.

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
        The current state of the DB System.


        :param lifecycle_state: The lifecycle_state of this DbSystem.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def listener_port(self):
        """
        Gets the listener_port of this DbSystem.
        The port number configured for the listener on the DB System.


        :return: The listener_port of this DbSystem.
        :rtype: int
        """
        return self._listener_port

    @listener_port.setter
    def listener_port(self, listener_port):
        """
        Sets the listener_port of this DbSystem.
        The port number configured for the listener on the DB System.


        :param listener_port: The listener_port of this DbSystem.
        :type: int
        """
        self._listener_port = listener_port

    @property
    def scan_dns_record_id(self):
        """
        Gets the scan_dns_record_id of this DbSystem.
        The OCID of the DNS record for the SCAN IP addresses that are associated with the DB System.


        :return: The scan_dns_record_id of this DbSystem.
        :rtype: str
        """
        return self._scan_dns_record_id

    @scan_dns_record_id.setter
    def scan_dns_record_id(self, scan_dns_record_id):
        """
        Sets the scan_dns_record_id of this DbSystem.
        The OCID of the DNS record for the SCAN IP addresses that are associated with the DB System.


        :param scan_dns_record_id: The scan_dns_record_id of this DbSystem.
        :type: str
        """
        self._scan_dns_record_id = scan_dns_record_id

    @property
    def scan_ip_ids(self):
        """
        Gets the scan_ip_ids of this DbSystem.
        The OCID of the Single Client Access Name (SCAN) IP addresses associated with the DB System.
        SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
        Clusterware directs the requests to the appropriate nodes in the cluster.

        - For a single-node DB System, this list is empty.


        :return: The scan_ip_ids of this DbSystem.
        :rtype: list[str]
        """
        return self._scan_ip_ids

    @scan_ip_ids.setter
    def scan_ip_ids(self, scan_ip_ids):
        """
        Sets the scan_ip_ids of this DbSystem.
        The OCID of the Single Client Access Name (SCAN) IP addresses associated with the DB System.
        SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
        Clusterware directs the requests to the appropriate nodes in the cluster.

        - For a single-node DB System, this list is empty.


        :param scan_ip_ids: The scan_ip_ids of this DbSystem.
        :type: list[str]
        """
        self._scan_ip_ids = scan_ip_ids

    @property
    def shape(self):
        """
        Gets the shape of this DbSystem.
        The shape of the DB System. The shape determines the CPU cores, storage, and memory allocated to the DB System.


        :return: The shape of this DbSystem.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DbSystem.
        The shape of the DB System. The shape determines the CPU cores, storage, and memory allocated to the DB System.


        :param shape: The shape of this DbSystem.
        :type: str
        """
        self._shape = shape

    @property
    def ssh_public_keys(self):
        """
        Gets the ssh_public_keys of this DbSystem.
        The public key portion of one or more key pairs used for SSH access to the DB System.


        :return: The ssh_public_keys of this DbSystem.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this DbSystem.
        The public key portion of one or more key pairs used for SSH access to the DB System.


        :param ssh_public_keys: The ssh_public_keys of this DbSystem.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this DbSystem.
        The OCID of the subnet the DB System is associated with.

        **Subnet Restrictions:**
        - For 1- and 2-node RAC DB Systems, do not use a subnet that overlaps with 192.168.16.16/28
        - For Exadata DB Systems, do not use a subnet that overlaps with 192.168.128.0/20

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.


        :return: The subnet_id of this DbSystem.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DbSystem.
        The OCID of the subnet the DB System is associated with.

        **Subnet Restrictions:**
        - For 1- and 2-node RAC DB Systems, do not use a subnet that overlaps with 192.168.16.16/28
        - For Exadata DB Systems, do not use a subnet that overlaps with 192.168.128.0/20

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.


        :param subnet_id: The subnet_id of this DbSystem.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        Gets the time_created of this DbSystem.
        The date and time the DB System was created.


        :return: The time_created of this DbSystem.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbSystem.
        The date and time the DB System was created.


        :param time_created: The time_created of this DbSystem.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def version(self):
        """
        Gets the version of this DbSystem.
        The version of the DB System.


        :return: The version of this DbSystem.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DbSystem.
        The version of the DB System.


        :param version: The version of this DbSystem.
        :type: str
        """
        self._version = version

    @property
    def vip_ids(self):
        """
        Gets the vip_ids of this DbSystem.
        The OCID of the virtual IP (VIP) addresses associated with the DB System.
        The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB System to
        enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.

        - For a single-node DB System, this list is empty.


        :return: The vip_ids of this DbSystem.
        :rtype: list[str]
        """
        return self._vip_ids

    @vip_ids.setter
    def vip_ids(self, vip_ids):
        """
        Sets the vip_ids of this DbSystem.
        The OCID of the virtual IP (VIP) addresses associated with the DB System.
        The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB System to
        enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.

        - For a single-node DB System, this list is empty.


        :param vip_ids: The vip_ids of this DbSystem.
        :type: list[str]
        """
        self._vip_ids = vip_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
