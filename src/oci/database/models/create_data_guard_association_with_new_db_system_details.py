# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataGuardAssociationWithNewDbSystemDetails(CreateDataGuardAssociationDetails):
    """
    The configuration details for creating a Data Guard association for a virtual machine DB system database. For this type of DB system database, the `creationType` should be `NewDbSystem`. A new DB system will be launched to create the standby database.

    To create a Data Guard association for a database in a bare metal or Exadata DB system, use the :func:`create_data_guard_association_to_existing_db_system_details` subtype instead.
    """

    #: A constant which can be used with the storage_volume_performance_mode property of a CreateDataGuardAssociationWithNewDbSystemDetails.
    #: This constant has a value of "BALANCED"
    STORAGE_VOLUME_PERFORMANCE_MODE_BALANCED = "BALANCED"

    #: A constant which can be used with the storage_volume_performance_mode property of a CreateDataGuardAssociationWithNewDbSystemDetails.
    #: This constant has a value of "HIGH_PERFORMANCE"
    STORAGE_VOLUME_PERFORMANCE_MODE_HIGH_PERFORMANCE = "HIGH_PERFORMANCE"

    #: A constant which can be used with the license_model property of a CreateDataGuardAssociationWithNewDbSystemDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateDataGuardAssociationWithNewDbSystemDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataGuardAssociationWithNewDbSystemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDataGuardAssociationWithNewDbSystemDetails.creation_type` attribute
        of this class is ``NewDbSystem`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_software_image_id:
            The value to assign to the database_software_image_id property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type database_software_image_id: str

        :param database_admin_password:
            The value to assign to the database_admin_password property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type database_admin_password: str

        :param protection_mode:
            The value to assign to the protection_mode property of this CreateDataGuardAssociationWithNewDbSystemDetails.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"
        :type protection_mode: str

        :param transport_type:
            The value to assign to the transport_type property of this CreateDataGuardAssociationWithNewDbSystemDetails.
            Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC"
        :type transport_type: str

        :param creation_type:
            The value to assign to the creation_type property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type creation_type: str

        :param is_active_data_guard_enabled:
            The value to assign to the is_active_data_guard_enabled property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type is_active_data_guard_enabled: bool

        :param peer_db_unique_name:
            The value to assign to the peer_db_unique_name property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type peer_db_unique_name: str

        :param peer_sid_prefix:
            The value to assign to the peer_sid_prefix property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type peer_sid_prefix: str

        :param display_name:
            The value to assign to the display_name property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type display_name: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type availability_domain: str

        :param shape:
            The value to assign to the shape property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type shape: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type cpu_core_count: int

        :param storage_volume_performance_mode:
            The value to assign to the storage_volume_performance_mode property of this CreateDataGuardAssociationWithNewDbSystemDetails.
            Allowed values for this property are: "BALANCED", "HIGH_PERFORMANCE"
        :type storage_volume_performance_mode: str

        :param node_count:
            The value to assign to the node_count property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type node_count: int

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type nsg_ids: list[str]

        :param backup_network_nsg_ids:
            The value to assign to the backup_network_nsg_ids property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type backup_network_nsg_ids: list[str]

        :param hostname:
            The value to assign to the hostname property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type hostname: str

        :param time_zone:
            The value to assign to the time_zone property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type time_zone: str

        :param fault_domains:
            The value to assign to the fault_domains property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type fault_domains: list[str]

        :param private_ip:
            The value to assign to the private_ip property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type private_ip: str

        :param license_model:
            The value to assign to the license_model property of this CreateDataGuardAssociationWithNewDbSystemDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param db_system_freeform_tags:
            The value to assign to the db_system_freeform_tags property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type db_system_freeform_tags: dict(str, str)

        :param db_system_defined_tags:
            The value to assign to the db_system_defined_tags property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type db_system_defined_tags: dict(str, dict(str, object))

        :param database_freeform_tags:
            The value to assign to the database_freeform_tags property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type database_freeform_tags: dict(str, str)

        :param database_defined_tags:
            The value to assign to the database_defined_tags property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type database_defined_tags: dict(str, dict(str, object))

        :param data_collection_options:
            The value to assign to the data_collection_options property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type data_collection_options: oci.database.models.DataCollectionOptions

        """
        self.swagger_types = {
            'database_software_image_id': 'str',
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str',
            'creation_type': 'str',
            'is_active_data_guard_enabled': 'bool',
            'peer_db_unique_name': 'str',
            'peer_sid_prefix': 'str',
            'display_name': 'str',
            'availability_domain': 'str',
            'shape': 'str',
            'cpu_core_count': 'int',
            'storage_volume_performance_mode': 'str',
            'node_count': 'int',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'backup_network_nsg_ids': 'list[str]',
            'hostname': 'str',
            'time_zone': 'str',
            'fault_domains': 'list[str]',
            'private_ip': 'str',
            'license_model': 'str',
            'db_system_freeform_tags': 'dict(str, str)',
            'db_system_defined_tags': 'dict(str, dict(str, object))',
            'database_freeform_tags': 'dict(str, str)',
            'database_defined_tags': 'dict(str, dict(str, object))',
            'data_collection_options': 'DataCollectionOptions'
        }

        self.attribute_map = {
            'database_software_image_id': 'databaseSoftwareImageId',
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType',
            'creation_type': 'creationType',
            'is_active_data_guard_enabled': 'isActiveDataGuardEnabled',
            'peer_db_unique_name': 'peerDbUniqueName',
            'peer_sid_prefix': 'peerSidPrefix',
            'display_name': 'displayName',
            'availability_domain': 'availabilityDomain',
            'shape': 'shape',
            'cpu_core_count': 'cpuCoreCount',
            'storage_volume_performance_mode': 'storageVolumePerformanceMode',
            'node_count': 'nodeCount',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'backup_network_nsg_ids': 'backupNetworkNsgIds',
            'hostname': 'hostname',
            'time_zone': 'timeZone',
            'fault_domains': 'faultDomains',
            'private_ip': 'privateIp',
            'license_model': 'licenseModel',
            'db_system_freeform_tags': 'dbSystemFreeformTags',
            'db_system_defined_tags': 'dbSystemDefinedTags',
            'database_freeform_tags': 'databaseFreeformTags',
            'database_defined_tags': 'databaseDefinedTags',
            'data_collection_options': 'dataCollectionOptions'
        }

        self._database_software_image_id = None
        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None
        self._creation_type = None
        self._is_active_data_guard_enabled = None
        self._peer_db_unique_name = None
        self._peer_sid_prefix = None
        self._display_name = None
        self._availability_domain = None
        self._shape = None
        self._cpu_core_count = None
        self._storage_volume_performance_mode = None
        self._node_count = None
        self._subnet_id = None
        self._nsg_ids = None
        self._backup_network_nsg_ids = None
        self._hostname = None
        self._time_zone = None
        self._fault_domains = None
        self._private_ip = None
        self._license_model = None
        self._db_system_freeform_tags = None
        self._db_system_defined_tags = None
        self._database_freeform_tags = None
        self._database_defined_tags = None
        self._data_collection_options = None
        self._creation_type = 'NewDbSystem'

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The user-friendly name of the DB system that will contain the the standby database. The display name does not have to be unique.


        :return: The display_name of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The user-friendly name of the DB system that will contain the the standby database. The display name does not have to be unique.


        :param display_name: The display_name of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The name of the availability domain that the standby database DB system will be located in. For example- \"Uocm:PHX-AD-1\".


        :return: The availability_domain of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The name of the availability domain that the standby database DB system will be located in. For example- \"Uocm:PHX-AD-1\".


        :param availability_domain: The availability_domain of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def shape(self):
        """
        Gets the shape of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The virtual machine DB system shape to launch for the standby database in the Data Guard association. The shape determines the number of CPU cores and the amount of memory available for the DB system.
        Only virtual machine shapes are valid options. If you do not supply this parameter, the default shape is the shape of the primary DB system.

        To get a list of all shapes, use the :func:`list_db_system_shapes` operation.


        :return: The shape of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The virtual machine DB system shape to launch for the standby database in the Data Guard association. The shape determines the number of CPU cores and the amount of memory available for the DB system.
        Only virtual machine shapes are valid options. If you do not supply this parameter, the default shape is the shape of the primary DB system.

        To get a list of all shapes, use the :func:`list_db_system_shapes` operation.


        :param shape: The shape of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._shape = shape

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The number of OCPU cores available for AMD-based virtual machine DB systems.


        :return: The cpu_core_count of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The number of OCPU cores available for AMD-based virtual machine DB systems.


        :param cpu_core_count: The cpu_core_count of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def storage_volume_performance_mode(self):
        """
        Gets the storage_volume_performance_mode of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See `Block Volume Performance`__ for more information.

        __ https://docs.cloud.oracle.com/Content/Block/Concepts/blockvolumeperformance.htm

        Allowed values for this property are: "BALANCED", "HIGH_PERFORMANCE"


        :return: The storage_volume_performance_mode of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._storage_volume_performance_mode

    @storage_volume_performance_mode.setter
    def storage_volume_performance_mode(self, storage_volume_performance_mode):
        """
        Sets the storage_volume_performance_mode of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See `Block Volume Performance`__ for more information.

        __ https://docs.cloud.oracle.com/Content/Block/Concepts/blockvolumeperformance.htm


        :param storage_volume_performance_mode: The storage_volume_performance_mode of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        allowed_values = ["BALANCED", "HIGH_PERFORMANCE"]
        if not value_allowed_none_or_none_sentinel(storage_volume_performance_mode, allowed_values):
            raise ValueError(
                "Invalid value for `storage_volume_performance_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._storage_volume_performance_mode = storage_volume_performance_mode

    @property
    def node_count(self):
        """
        Gets the node_count of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The number of nodes to launch for the DB system of the standby in the Data Guard association. For a 2-node RAC virtual machine DB system, specify either 1 or 2. If you do not supply this parameter, the default is the node count of the primary DB system.


        :return: The node_count of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The number of nodes to launch for the DB system of the standby in the Data Guard association. For a 2-node RAC virtual machine DB system, specify either 1 or 2. If you do not supply this parameter, the default is the node count of the primary DB system.


        :param node_count: The node_count of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: int
        """
        self._node_count = node_count

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The OCID of the subnet the DB system is associated with.
        **Subnet Restrictions:**
        - For 1- and 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.16.16/28

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.


        :return: The subnet_id of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The OCID of the subnet the DB system is associated with.
        **Subnet Restrictions:**
        - For 1- and 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.16.16/28

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.


        :param subnet_id: The subnet_id of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def backup_network_nsg_ids(self):
        """
        Gets the backup_network_nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The backup_network_nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: list[str]
        """
        return self._backup_network_nsg_ids

    @backup_network_nsg_ids.setter
    def backup_network_nsg_ids(self, backup_network_nsg_ids):
        """
        Sets the backup_network_nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param backup_network_nsg_ids: The backup_network_nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: list[str]
        """
        self._backup_network_nsg_ids = backup_network_nsg_ids

    @property
    def hostname(self):
        """
        Gets the hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The hostname for the DB node.


        :return: The hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The hostname for the DB node.


        :param hostname: The hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def time_zone(self):
        """
        Gets the time_zone of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The time zone of the dataguard standby DB system. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The time zone of the dataguard standby DB system. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def fault_domains(self):
        """
        Gets the fault_domains of this CreateDataGuardAssociationWithNewDbSystemDetails.
        A Fault Domain is a grouping of hardware and infrastructure within an availability domain.
        Fault Domains let you distribute your instances so that they are not on the same physical
        hardware within a single availability domain. A hardware failure or maintenance
        that affects one Fault Domain does not affect DB systems in other Fault Domains.

        If you do not specify the Fault Domain, the system selects one for you. To change the Fault
        Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain.

        If the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into.
        The system assigns your nodes automatically to the Fault Domains you specify so that
        no Fault Domain contains more than one node.

        To get a list of Fault Domains, use the
        :func:`list_fault_domains` operation in the
        Identity and Access Management Service API.

        Example: `FAULT-DOMAIN-1`


        :return: The fault_domains of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: list[str]
        """
        return self._fault_domains

    @fault_domains.setter
    def fault_domains(self, fault_domains):
        """
        Sets the fault_domains of this CreateDataGuardAssociationWithNewDbSystemDetails.
        A Fault Domain is a grouping of hardware and infrastructure within an availability domain.
        Fault Domains let you distribute your instances so that they are not on the same physical
        hardware within a single availability domain. A hardware failure or maintenance
        that affects one Fault Domain does not affect DB systems in other Fault Domains.

        If you do not specify the Fault Domain, the system selects one for you. To change the Fault
        Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain.

        If the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into.
        The system assigns your nodes automatically to the Fault Domains you specify so that
        no Fault Domain contains more than one node.

        To get a list of Fault Domains, use the
        :func:`list_fault_domains` operation in the
        Identity and Access Management Service API.

        Example: `FAULT-DOMAIN-1`


        :param fault_domains: The fault_domains of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: list[str]
        """
        self._fault_domains = fault_domains

    @property
    def private_ip(self):
        """
        Gets the private_ip of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The IPv4 address from the provided OCI subnet which needs to be assigned to the VNIC. If not provided, it will
        be auto-assigned with an available IPv4 address from the subnet.


        :return: The private_ip of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The IPv4 address from the provided OCI subnet which needs to be assigned to the VNIC. If not provided, it will
        be auto-assigned with an available IPv4 address from the subnet.


        :param private_ip: The private_ip of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def license_model(self):
        """
        Gets the license_model of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The Oracle license model that applies to all the databases on the dataguard standby DB system. The default is LICENSE_INCLUDED.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The Oracle license model that applies to all the databases on the dataguard standby DB system. The default is LICENSE_INCLUDED.


        :param license_model: The license_model of this CreateDataGuardAssociationWithNewDbSystemDetails.
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
    def db_system_freeform_tags(self):
        """
        Gets the db_system_freeform_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The db_system_freeform_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: dict(str, str)
        """
        return self._db_system_freeform_tags

    @db_system_freeform_tags.setter
    def db_system_freeform_tags(self, db_system_freeform_tags):
        """
        Sets the db_system_freeform_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param db_system_freeform_tags: The db_system_freeform_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: dict(str, str)
        """
        self._db_system_freeform_tags = db_system_freeform_tags

    @property
    def db_system_defined_tags(self):
        """
        Gets the db_system_defined_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The db_system_defined_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._db_system_defined_tags

    @db_system_defined_tags.setter
    def db_system_defined_tags(self, db_system_defined_tags):
        """
        Sets the db_system_defined_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param db_system_defined_tags: The db_system_defined_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: dict(str, dict(str, object))
        """
        self._db_system_defined_tags = db_system_defined_tags

    @property
    def database_freeform_tags(self):
        """
        Gets the database_freeform_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The database_freeform_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: dict(str, str)
        """
        return self._database_freeform_tags

    @database_freeform_tags.setter
    def database_freeform_tags(self, database_freeform_tags):
        """
        Sets the database_freeform_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param database_freeform_tags: The database_freeform_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: dict(str, str)
        """
        self._database_freeform_tags = database_freeform_tags

    @property
    def database_defined_tags(self):
        """
        Gets the database_defined_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The database_defined_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._database_defined_tags

    @database_defined_tags.setter
    def database_defined_tags(self, database_defined_tags):
        """
        Sets the database_defined_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param database_defined_tags: The database_defined_tags of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: dict(str, dict(str, object))
        """
        self._database_defined_tags = database_defined_tags

    @property
    def data_collection_options(self):
        """
        Gets the data_collection_options of this CreateDataGuardAssociationWithNewDbSystemDetails.

        :return: The data_collection_options of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: oci.database.models.DataCollectionOptions
        """
        return self._data_collection_options

    @data_collection_options.setter
    def data_collection_options(self, data_collection_options):
        """
        Sets the data_collection_options of this CreateDataGuardAssociationWithNewDbSystemDetails.

        :param data_collection_options: The data_collection_options of this CreateDataGuardAssociationWithNewDbSystemDetails.
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
