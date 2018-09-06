# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystem(object):
    """
    The Database Service supports several types of DB systems, ranging in size, price, and performance. For details about each type of system, see:

    - `Exadata DB Systems`__
    - `Bare Metal and Virtual Machine DB Systems`__

    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    For information about access control and compartments, see
    `Overview of the Identity Service`__.

    For information about availability domains, see
    `Regions and Availability Domains`__.

    To get a list of availability domains, use the `ListAvailabilityDomains` operation
    in the Identity Service API.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Database/Concepts/exaoverview.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Database/Concepts/overview.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm
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

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this DbSystem.
        :type availability_domain: str

        :param backup_subnet_id:
            The value to assign to the backup_subnet_id property of this DbSystem.
        :type backup_subnet_id: str

        :param cluster_name:
            The value to assign to the cluster_name property of this DbSystem.
        :type cluster_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DbSystem.
        :type compartment_id: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this DbSystem.
        :type cpu_core_count: int

        :param data_storage_percentage:
            The value to assign to the data_storage_percentage property of this DbSystem.
        :type data_storage_percentage: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this DbSystem.
        :type data_storage_size_in_gbs: int

        :param database_edition:
            The value to assign to the database_edition property of this DbSystem.
            Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_edition: str

        :param defined_tags:
            The value to assign to the defined_tags property of this DbSystem.
        :type defined_tags: dict(str, dict(str, object))

        :param disk_redundancy:
            The value to assign to the disk_redundancy property of this DbSystem.
            Allowed values for this property are: "HIGH", "NORMAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type disk_redundancy: str

        :param display_name:
            The value to assign to the display_name property of this DbSystem.
        :type display_name: str

        :param domain:
            The value to assign to the domain property of this DbSystem.
        :type domain: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DbSystem.
        :type freeform_tags: dict(str, str)

        :param hostname:
            The value to assign to the hostname property of this DbSystem.
        :type hostname: str

        :param id:
            The value to assign to the id property of this DbSystem.
        :type id: str

        :param last_patch_history_entry_id:
            The value to assign to the last_patch_history_entry_id property of this DbSystem.
        :type last_patch_history_entry_id: str

        :param license_model:
            The value to assign to the license_model property of this DbSystem.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DbSystem.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbSystem.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param listener_port:
            The value to assign to the listener_port property of this DbSystem.
        :type listener_port: int

        :param node_count:
            The value to assign to the node_count property of this DbSystem.
        :type node_count: int

        :param reco_storage_size_in_gb:
            The value to assign to the reco_storage_size_in_gb property of this DbSystem.
        :type reco_storage_size_in_gb: int

        :param scan_dns_record_id:
            The value to assign to the scan_dns_record_id property of this DbSystem.
        :type scan_dns_record_id: str

        :param scan_ip_ids:
            The value to assign to the scan_ip_ids property of this DbSystem.
        :type scan_ip_ids: list[str]

        :param shape:
            The value to assign to the shape property of this DbSystem.
        :type shape: str

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this DbSystem.
        :type ssh_public_keys: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this DbSystem.
        :type subnet_id: str

        :param time_created:
            The value to assign to the time_created property of this DbSystem.
        :type time_created: datetime

        :param version:
            The value to assign to the version property of this DbSystem.
        :type version: str

        :param vip_ids:
            The value to assign to the vip_ids property of this DbSystem.
        :type vip_ids: list[str]

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'backup_subnet_id': 'str',
            'cluster_name': 'str',
            'compartment_id': 'str',
            'cpu_core_count': 'int',
            'data_storage_percentage': 'int',
            'data_storage_size_in_gbs': 'int',
            'database_edition': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'disk_redundancy': 'str',
            'display_name': 'str',
            'domain': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostname': 'str',
            'id': 'str',
            'last_patch_history_entry_id': 'str',
            'license_model': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'listener_port': 'int',
            'node_count': 'int',
            'reco_storage_size_in_gb': 'int',
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
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'database_edition': 'databaseEdition',
            'defined_tags': 'definedTags',
            'disk_redundancy': 'diskRedundancy',
            'display_name': 'displayName',
            'domain': 'domain',
            'freeform_tags': 'freeformTags',
            'hostname': 'hostname',
            'id': 'id',
            'last_patch_history_entry_id': 'lastPatchHistoryEntryId',
            'license_model': 'licenseModel',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'listener_port': 'listenerPort',
            'node_count': 'nodeCount',
            'reco_storage_size_in_gb': 'recoStorageSizeInGB',
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
        self._data_storage_size_in_gbs = None
        self._database_edition = None
        self._defined_tags = None
        self._disk_redundancy = None
        self._display_name = None
        self._domain = None
        self._freeform_tags = None
        self._hostname = None
        self._id = None
        self._last_patch_history_entry_id = None
        self._license_model = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._listener_port = None
        self._node_count = None
        self._reco_storage_size_in_gb = None
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
    def backup_subnet_id(self):
        """
        Gets the backup_subnet_id of this DbSystem.
        The `OCID`__ of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

        **Subnet Restriction:** See the subnet restrictions information for **subnetId**.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param backup_subnet_id: The backup_subnet_id of this DbSystem.
        :type: str
        """
        self._backup_subnet_id = backup_subnet_id

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
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DbSystem.
        The `OCID`__ of the compartment.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DbSystem.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbSystem.
        The `OCID`__ of the compartment.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DbSystem.
        :type: str
        """
        self._compartment_id = compartment_id

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
    def defined_tags(self):
        """
        Gets the defined_tags of this DbSystem.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


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

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DbSystem.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

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
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DbSystem.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DbSystem.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

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
    def id(self):
        """
        **[Required]** Gets the id of this DbSystem.
        The `OCID`__ of the DB system.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DbSystem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbSystem.
        The `OCID`__ of the DB system.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DbSystem.
        :type: str
        """
        self._id = id

    @property
    def last_patch_history_entry_id(self):
        """
        Gets the last_patch_history_entry_id of this DbSystem.
        The `OCID`__ of the last patch history. This value is updated as soon as a patch operation starts.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The last_patch_history_entry_id of this DbSystem.
        :rtype: str
        """
        return self._last_patch_history_entry_id

    @last_patch_history_entry_id.setter
    def last_patch_history_entry_id(self, last_patch_history_entry_id):
        """
        Sets the last_patch_history_entry_id of this DbSystem.
        The `OCID`__ of the last patch history. This value is updated as soon as a patch operation starts.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param last_patch_history_entry_id: The last_patch_history_entry_id of this DbSystem.
        :type: str
        """
        self._last_patch_history_entry_id = last_patch_history_entry_id

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
    def scan_dns_record_id(self):
        """
        Gets the scan_dns_record_id of this DbSystem.
        The `OCID`__ of the DNS record for the SCAN IP addresses that are associated with the DB system.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The scan_dns_record_id of this DbSystem.
        :rtype: str
        """
        return self._scan_dns_record_id

    @scan_dns_record_id.setter
    def scan_dns_record_id(self, scan_dns_record_id):
        """
        Sets the scan_dns_record_id of this DbSystem.
        The `OCID`__ of the DNS record for the SCAN IP addresses that are associated with the DB system.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param scan_dns_record_id: The scan_dns_record_id of this DbSystem.
        :type: str
        """
        self._scan_dns_record_id = scan_dns_record_id

    @property
    def scan_ip_ids(self):
        """
        Gets the scan_ip_ids of this DbSystem.
        The `OCID`__ of the Single Client Access Name (SCAN) IP addresses associated with the DB system.
        SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
        Oracle Clusterware directs the requests to the appropriate nodes in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param scan_ip_ids: The scan_ip_ids of this DbSystem.
        :type: list[str]
        """
        self._scan_ip_ids = scan_ip_ids

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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this DbSystem.
        :type: str
        """
        self._subnet_id = subnet_id

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
    def vip_ids(self):
        """
        Gets the vip_ids of this DbSystem.
        The `OCID`__ of the virtual IP (VIP) addresses associated with the DB system.
        The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB system to
        enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.

        **Note:** For a single-node DB system, this list is empty.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


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
