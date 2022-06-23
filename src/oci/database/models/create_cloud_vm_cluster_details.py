# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCloudVmClusterDetails(object):
    """
    Details for the create cloud VM cluster operation. Applies to Exadata Cloud Service instances only.
    """

    #: A constant which can be used with the license_model property of a CreateCloudVmClusterDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateCloudVmClusterDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCloudVmClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCloudVmClusterDetails.
        :type compartment_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateCloudVmClusterDetails.
        :type subnet_id: str

        :param backup_subnet_id:
            The value to assign to the backup_subnet_id property of this CreateCloudVmClusterDetails.
        :type backup_subnet_id: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateCloudVmClusterDetails.
        :type cpu_core_count: int

        :param ocpu_count:
            The value to assign to the ocpu_count property of this CreateCloudVmClusterDetails.
        :type ocpu_count: float

        :param cluster_name:
            The value to assign to the cluster_name property of this CreateCloudVmClusterDetails.
        :type cluster_name: str

        :param data_storage_percentage:
            The value to assign to the data_storage_percentage property of this CreateCloudVmClusterDetails.
        :type data_storage_percentage: int

        :param display_name:
            The value to assign to the display_name property of this CreateCloudVmClusterDetails.
        :type display_name: str

        :param cloud_exadata_infrastructure_id:
            The value to assign to the cloud_exadata_infrastructure_id property of this CreateCloudVmClusterDetails.
        :type cloud_exadata_infrastructure_id: str

        :param hostname:
            The value to assign to the hostname property of this CreateCloudVmClusterDetails.
        :type hostname: str

        :param domain:
            The value to assign to the domain property of this CreateCloudVmClusterDetails.
        :type domain: str

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this CreateCloudVmClusterDetails.
        :type ssh_public_keys: list[str]

        :param license_model:
            The value to assign to the license_model property of this CreateCloudVmClusterDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param is_sparse_diskgroup_enabled:
            The value to assign to the is_sparse_diskgroup_enabled property of this CreateCloudVmClusterDetails.
        :type is_sparse_diskgroup_enabled: bool

        :param is_local_backup_enabled:
            The value to assign to the is_local_backup_enabled property of this CreateCloudVmClusterDetails.
        :type is_local_backup_enabled: bool

        :param time_zone:
            The value to assign to the time_zone property of this CreateCloudVmClusterDetails.
        :type time_zone: str

        :param scan_listener_port_tcp:
            The value to assign to the scan_listener_port_tcp property of this CreateCloudVmClusterDetails.
        :type scan_listener_port_tcp: int

        :param scan_listener_port_tcp_ssl:
            The value to assign to the scan_listener_port_tcp_ssl property of this CreateCloudVmClusterDetails.
        :type scan_listener_port_tcp_ssl: int

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateCloudVmClusterDetails.
        :type nsg_ids: list[str]

        :param backup_network_nsg_ids:
            The value to assign to the backup_network_nsg_ids property of this CreateCloudVmClusterDetails.
        :type backup_network_nsg_ids: list[str]

        :param gi_version:
            The value to assign to the gi_version property of this CreateCloudVmClusterDetails.
        :type gi_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCloudVmClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCloudVmClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param data_collection_options:
            The value to assign to the data_collection_options property of this CreateCloudVmClusterDetails.
        :type data_collection_options: oci.database.models.DataCollectionOptions

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'subnet_id': 'str',
            'backup_subnet_id': 'str',
            'cpu_core_count': 'int',
            'ocpu_count': 'float',
            'cluster_name': 'str',
            'data_storage_percentage': 'int',
            'display_name': 'str',
            'cloud_exadata_infrastructure_id': 'str',
            'hostname': 'str',
            'domain': 'str',
            'ssh_public_keys': 'list[str]',
            'license_model': 'str',
            'is_sparse_diskgroup_enabled': 'bool',
            'is_local_backup_enabled': 'bool',
            'time_zone': 'str',
            'scan_listener_port_tcp': 'int',
            'scan_listener_port_tcp_ssl': 'int',
            'nsg_ids': 'list[str]',
            'backup_network_nsg_ids': 'list[str]',
            'gi_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'data_collection_options': 'DataCollectionOptions'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'subnet_id': 'subnetId',
            'backup_subnet_id': 'backupSubnetId',
            'cpu_core_count': 'cpuCoreCount',
            'ocpu_count': 'ocpuCount',
            'cluster_name': 'clusterName',
            'data_storage_percentage': 'dataStoragePercentage',
            'display_name': 'displayName',
            'cloud_exadata_infrastructure_id': 'cloudExadataInfrastructureId',
            'hostname': 'hostname',
            'domain': 'domain',
            'ssh_public_keys': 'sshPublicKeys',
            'license_model': 'licenseModel',
            'is_sparse_diskgroup_enabled': 'isSparseDiskgroupEnabled',
            'is_local_backup_enabled': 'isLocalBackupEnabled',
            'time_zone': 'timeZone',
            'scan_listener_port_tcp': 'scanListenerPortTcp',
            'scan_listener_port_tcp_ssl': 'scanListenerPortTcpSsl',
            'nsg_ids': 'nsgIds',
            'backup_network_nsg_ids': 'backupNetworkNsgIds',
            'gi_version': 'giVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'data_collection_options': 'dataCollectionOptions'
        }

        self._compartment_id = None
        self._subnet_id = None
        self._backup_subnet_id = None
        self._cpu_core_count = None
        self._ocpu_count = None
        self._cluster_name = None
        self._data_storage_percentage = None
        self._display_name = None
        self._cloud_exadata_infrastructure_id = None
        self._hostname = None
        self._domain = None
        self._ssh_public_keys = None
        self._license_model = None
        self._is_sparse_diskgroup_enabled = None
        self._is_local_backup_enabled = None
        self._time_zone = None
        self._scan_listener_port_tcp = None
        self._scan_listener_port_tcp_ssl = None
        self._nsg_ids = None
        self._backup_network_nsg_ids = None
        self._gi_version = None
        self._freeform_tags = None
        self._defined_tags = None
        self._data_collection_options = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCloudVmClusterDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCloudVmClusterDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateCloudVmClusterDetails.
        The `OCID`__ of the subnet associated with the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateCloudVmClusterDetails.
        The `OCID`__ of the subnet associated with the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def backup_subnet_id(self):
        """
        **[Required]** Gets the backup_subnet_id of this CreateCloudVmClusterDetails.
        The `OCID`__ of the backup network subnet associated with the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The backup_subnet_id of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._backup_subnet_id

    @backup_subnet_id.setter
    def backup_subnet_id(self, backup_subnet_id):
        """
        Sets the backup_subnet_id of this CreateCloudVmClusterDetails.
        The `OCID`__ of the backup network subnet associated with the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param backup_subnet_id: The backup_subnet_id of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._backup_subnet_id = backup_subnet_id

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this CreateCloudVmClusterDetails.
        The number of CPU cores to enable for a cloud VM cluster. Valid values depend on the specified shape:

        - Exadata.Base.48 - Specify a multiple of 2, from 0 to 48.
        - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84.
        - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168.
        - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.
        - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92.
        - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184.
        - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.


        :return: The cpu_core_count of this CreateCloudVmClusterDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CreateCloudVmClusterDetails.
        The number of CPU cores to enable for a cloud VM cluster. Valid values depend on the specified shape:

        - Exadata.Base.48 - Specify a multiple of 2, from 0 to 48.
        - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84.
        - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168.
        - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.
        - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92.
        - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184.
        - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.


        :param cpu_core_count: The cpu_core_count of this CreateCloudVmClusterDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def ocpu_count(self):
        """
        Gets the ocpu_count of this CreateCloudVmClusterDetails.
        The number of OCPU cores to enable for a cloud VM cluster. Only 1 decimal place is allowed for the fractional part.


        :return: The ocpu_count of this CreateCloudVmClusterDetails.
        :rtype: float
        """
        return self._ocpu_count

    @ocpu_count.setter
    def ocpu_count(self, ocpu_count):
        """
        Sets the ocpu_count of this CreateCloudVmClusterDetails.
        The number of OCPU cores to enable for a cloud VM cluster. Only 1 decimal place is allowed for the fractional part.


        :param ocpu_count: The ocpu_count of this CreateCloudVmClusterDetails.
        :type: float
        """
        self._ocpu_count = ocpu_count

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this CreateCloudVmClusterDetails.
        The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :return: The cluster_name of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this CreateCloudVmClusterDetails.
        The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :param cluster_name: The cluster_name of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def data_storage_percentage(self):
        """
        Gets the data_storage_percentage of this CreateCloudVmClusterDetails.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See `Storage Configuration`__ in the Exadata documentation for details on the impact of the configuration settings on storage.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/exaoverview.htm#Exadata


        :return: The data_storage_percentage of this CreateCloudVmClusterDetails.
        :rtype: int
        """
        return self._data_storage_percentage

    @data_storage_percentage.setter
    def data_storage_percentage(self, data_storage_percentage):
        """
        Sets the data_storage_percentage of this CreateCloudVmClusterDetails.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See `Storage Configuration`__ in the Exadata documentation for details on the impact of the configuration settings on storage.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/exaoverview.htm#Exadata


        :param data_storage_percentage: The data_storage_percentage of this CreateCloudVmClusterDetails.
        :type: int
        """
        self._data_storage_percentage = data_storage_percentage

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateCloudVmClusterDetails.
        The user-friendly name for the cloud VM cluster. The name does not need to be unique.


        :return: The display_name of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCloudVmClusterDetails.
        The user-friendly name for the cloud VM cluster. The name does not need to be unique.


        :param display_name: The display_name of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def cloud_exadata_infrastructure_id(self):
        """
        **[Required]** Gets the cloud_exadata_infrastructure_id of this CreateCloudVmClusterDetails.
        The `OCID`__ of the cloud Exadata infrastructure resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_exadata_infrastructure_id of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._cloud_exadata_infrastructure_id

    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(self, cloud_exadata_infrastructure_id):
        """
        Sets the cloud_exadata_infrastructure_id of this CreateCloudVmClusterDetails.
        The `OCID`__ of the cloud Exadata infrastructure resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_exadata_infrastructure_id: The cloud_exadata_infrastructure_id of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._cloud_exadata_infrastructure_id = cloud_exadata_infrastructure_id

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this CreateCloudVmClusterDetails.
        The hostname for the cloud VM cluster. The hostname must begin with an alphabetic character, and
        can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB systems, and 12 characters for Exadata systems.

        The maximum length of the combined hostname and domain is 63 characters.

        **Note:** The hostname must be unique within the subnet. If it is not unique,
        the cloud VM Cluster will fail to provision.


        :return: The hostname of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CreateCloudVmClusterDetails.
        The hostname for the cloud VM cluster. The hostname must begin with an alphabetic character, and
        can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB systems, and 12 characters for Exadata systems.

        The maximum length of the combined hostname and domain is 63 characters.

        **Note:** The hostname must be unique within the subnet. If it is not unique,
        the cloud VM Cluster will fail to provision.


        :param hostname: The hostname of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def domain(self):
        """
        Gets the domain of this CreateCloudVmClusterDetails.
        A domain name used for the cloud VM cluster. If the Oracle-provided internet and VCN
        resolver is enabled for the specified subnet, the domain name for the subnet is used
        (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.
        Applies to Exadata Cloud Service instances only.


        :return: The domain of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this CreateCloudVmClusterDetails.
        A domain name used for the cloud VM cluster. If the Oracle-provided internet and VCN
        resolver is enabled for the specified subnet, the domain name for the subnet is used
        (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.
        Applies to Exadata Cloud Service instances only.


        :param domain: The domain of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._domain = domain

    @property
    def ssh_public_keys(self):
        """
        **[Required]** Gets the ssh_public_keys of this CreateCloudVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.


        :return: The ssh_public_keys of this CreateCloudVmClusterDetails.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this CreateCloudVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.


        :param ssh_public_keys: The ssh_public_keys of this CreateCloudVmClusterDetails.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def license_model(self):
        """
        Gets the license_model of this CreateCloudVmClusterDetails.
        The Oracle license model that applies to the cloud VM cluster. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateCloudVmClusterDetails.
        The Oracle license model that applies to the cloud VM cluster. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this CreateCloudVmClusterDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                "Invalid value for `license_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._license_model = license_model

    @property
    def is_sparse_diskgroup_enabled(self):
        """
        Gets the is_sparse_diskgroup_enabled of this CreateCloudVmClusterDetails.
        If true, the sparse disk group is configured for the cloud VM cluster. If false, the sparse disk group is not created.


        :return: The is_sparse_diskgroup_enabled of this CreateCloudVmClusterDetails.
        :rtype: bool
        """
        return self._is_sparse_diskgroup_enabled

    @is_sparse_diskgroup_enabled.setter
    def is_sparse_diskgroup_enabled(self, is_sparse_diskgroup_enabled):
        """
        Sets the is_sparse_diskgroup_enabled of this CreateCloudVmClusterDetails.
        If true, the sparse disk group is configured for the cloud VM cluster. If false, the sparse disk group is not created.


        :param is_sparse_diskgroup_enabled: The is_sparse_diskgroup_enabled of this CreateCloudVmClusterDetails.
        :type: bool
        """
        self._is_sparse_diskgroup_enabled = is_sparse_diskgroup_enabled

    @property
    def is_local_backup_enabled(self):
        """
        Gets the is_local_backup_enabled of this CreateCloudVmClusterDetails.
        If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.


        :return: The is_local_backup_enabled of this CreateCloudVmClusterDetails.
        :rtype: bool
        """
        return self._is_local_backup_enabled

    @is_local_backup_enabled.setter
    def is_local_backup_enabled(self, is_local_backup_enabled):
        """
        Sets the is_local_backup_enabled of this CreateCloudVmClusterDetails.
        If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.


        :param is_local_backup_enabled: The is_local_backup_enabled of this CreateCloudVmClusterDetails.
        :type: bool
        """
        self._is_local_backup_enabled = is_local_backup_enabled

    @property
    def time_zone(self):
        """
        Gets the time_zone of this CreateCloudVmClusterDetails.
        The time zone to use for the cloud VM cluster. For details, see `Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this CreateCloudVmClusterDetails.
        The time zone to use for the cloud VM cluster. For details, see `Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def scan_listener_port_tcp(self):
        """
        Gets the scan_listener_port_tcp of this CreateCloudVmClusterDetails.
        The TCP Single Client Access Name (SCAN) port. The default port is 1521.


        :return: The scan_listener_port_tcp of this CreateCloudVmClusterDetails.
        :rtype: int
        """
        return self._scan_listener_port_tcp

    @scan_listener_port_tcp.setter
    def scan_listener_port_tcp(self, scan_listener_port_tcp):
        """
        Sets the scan_listener_port_tcp of this CreateCloudVmClusterDetails.
        The TCP Single Client Access Name (SCAN) port. The default port is 1521.


        :param scan_listener_port_tcp: The scan_listener_port_tcp of this CreateCloudVmClusterDetails.
        :type: int
        """
        self._scan_listener_port_tcp = scan_listener_port_tcp

    @property
    def scan_listener_port_tcp_ssl(self):
        """
        Gets the scan_listener_port_tcp_ssl of this CreateCloudVmClusterDetails.
        The TCPS Single Client Access Name (SCAN) port. The default port is 2484.


        :return: The scan_listener_port_tcp_ssl of this CreateCloudVmClusterDetails.
        :rtype: int
        """
        return self._scan_listener_port_tcp_ssl

    @scan_listener_port_tcp_ssl.setter
    def scan_listener_port_tcp_ssl(self, scan_listener_port_tcp_ssl):
        """
        Sets the scan_listener_port_tcp_ssl of this CreateCloudVmClusterDetails.
        The TCPS Single Client Access Name (SCAN) port. The default port is 2484.


        :param scan_listener_port_tcp_ssl: The scan_listener_port_tcp_ssl of this CreateCloudVmClusterDetails.
        :type: int
        """
        self._scan_listener_port_tcp_ssl = scan_listener_port_tcp_ssl

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateCloudVmClusterDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this CreateCloudVmClusterDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateCloudVmClusterDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this CreateCloudVmClusterDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def backup_network_nsg_ids(self):
        """
        Gets the backup_network_nsg_ids of this CreateCloudVmClusterDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The backup_network_nsg_ids of this CreateCloudVmClusterDetails.
        :rtype: list[str]
        """
        return self._backup_network_nsg_ids

    @backup_network_nsg_ids.setter
    def backup_network_nsg_ids(self, backup_network_nsg_ids):
        """
        Sets the backup_network_nsg_ids of this CreateCloudVmClusterDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param backup_network_nsg_ids: The backup_network_nsg_ids of this CreateCloudVmClusterDetails.
        :type: list[str]
        """
        self._backup_network_nsg_ids = backup_network_nsg_ids

    @property
    def gi_version(self):
        """
        **[Required]** Gets the gi_version of this CreateCloudVmClusterDetails.
        A valid Oracle Grid Infrastructure (GI) software version.


        :return: The gi_version of this CreateCloudVmClusterDetails.
        :rtype: str
        """
        return self._gi_version

    @gi_version.setter
    def gi_version(self, gi_version):
        """
        Sets the gi_version of this CreateCloudVmClusterDetails.
        A valid Oracle Grid Infrastructure (GI) software version.


        :param gi_version: The gi_version of this CreateCloudVmClusterDetails.
        :type: str
        """
        self._gi_version = gi_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCloudVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateCloudVmClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCloudVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateCloudVmClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCloudVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateCloudVmClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCloudVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateCloudVmClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def data_collection_options(self):
        """
        Gets the data_collection_options of this CreateCloudVmClusterDetails.

        :return: The data_collection_options of this CreateCloudVmClusterDetails.
        :rtype: oci.database.models.DataCollectionOptions
        """
        return self._data_collection_options

    @data_collection_options.setter
    def data_collection_options(self, data_collection_options):
        """
        Sets the data_collection_options of this CreateCloudVmClusterDetails.

        :param data_collection_options: The data_collection_options of this CreateCloudVmClusterDetails.
        :type: oci.database.models.DataCollectionOptions
        """
        self._data_collection_options = data_collection_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
