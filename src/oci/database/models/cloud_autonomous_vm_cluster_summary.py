# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudAutonomousVmClusterSummary(object):
    """
    Details of the cloud Autonomous VM cluster.
    """

    #: A constant which can be used with the lifecycle_state property of a CloudAutonomousVmClusterSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a CloudAutonomousVmClusterSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a CloudAutonomousVmClusterSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CloudAutonomousVmClusterSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a CloudAutonomousVmClusterSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a CloudAutonomousVmClusterSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a CloudAutonomousVmClusterSummary.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the license_model property of a CloudAutonomousVmClusterSummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CloudAutonomousVmClusterSummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new CloudAutonomousVmClusterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CloudAutonomousVmClusterSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CloudAutonomousVmClusterSummary.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CloudAutonomousVmClusterSummary.
        :type description: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CloudAutonomousVmClusterSummary.
        :type availability_domain: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CloudAutonomousVmClusterSummary.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CloudAutonomousVmClusterSummary.
        :type nsg_ids: list[str]

        :param last_update_history_entry_id:
            The value to assign to the last_update_history_entry_id property of this CloudAutonomousVmClusterSummary.
        :type last_update_history_entry_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CloudAutonomousVmClusterSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this CloudAutonomousVmClusterSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this CloudAutonomousVmClusterSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CloudAutonomousVmClusterSummary.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CloudAutonomousVmClusterSummary.
        :type lifecycle_details: str

        :param hostname:
            The value to assign to the hostname property of this CloudAutonomousVmClusterSummary.
        :type hostname: str

        :param domain:
            The value to assign to the domain property of this CloudAutonomousVmClusterSummary.
        :type domain: str

        :param cloud_exadata_infrastructure_id:
            The value to assign to the cloud_exadata_infrastructure_id property of this CloudAutonomousVmClusterSummary.
        :type cloud_exadata_infrastructure_id: str

        :param shape:
            The value to assign to the shape property of this CloudAutonomousVmClusterSummary.
        :type shape: str

        :param node_count:
            The value to assign to the node_count property of this CloudAutonomousVmClusterSummary.
        :type node_count: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CloudAutonomousVmClusterSummary.
        :type data_storage_size_in_tbs: float

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this CloudAutonomousVmClusterSummary.
        :type data_storage_size_in_gbs: float

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CloudAutonomousVmClusterSummary.
        :type cpu_core_count: int

        :param ocpu_count:
            The value to assign to the ocpu_count property of this CloudAutonomousVmClusterSummary.
        :type ocpu_count: float

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this CloudAutonomousVmClusterSummary.
        :type memory_size_in_gbs: int

        :param license_model:
            The value to assign to the license_model property of this CloudAutonomousVmClusterSummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param last_maintenance_run_id:
            The value to assign to the last_maintenance_run_id property of this CloudAutonomousVmClusterSummary.
        :type last_maintenance_run_id: str

        :param next_maintenance_run_id:
            The value to assign to the next_maintenance_run_id property of this CloudAutonomousVmClusterSummary.
        :type next_maintenance_run_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CloudAutonomousVmClusterSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CloudAutonomousVmClusterSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param available_cpus:
            The value to assign to the available_cpus property of this CloudAutonomousVmClusterSummary.
        :type available_cpus: float

        :param reclaimable_cpus:
            The value to assign to the reclaimable_cpus property of this CloudAutonomousVmClusterSummary.
        :type reclaimable_cpus: float

        :param available_container_databases:
            The value to assign to the available_container_databases property of this CloudAutonomousVmClusterSummary.
        :type available_container_databases: int

        :param total_container_databases:
            The value to assign to the total_container_databases property of this CloudAutonomousVmClusterSummary.
        :type total_container_databases: int

        :param available_autonomous_data_storage_size_in_tbs:
            The value to assign to the available_autonomous_data_storage_size_in_tbs property of this CloudAutonomousVmClusterSummary.
        :type available_autonomous_data_storage_size_in_tbs: float

        :param autonomous_data_storage_size_in_tbs:
            The value to assign to the autonomous_data_storage_size_in_tbs property of this CloudAutonomousVmClusterSummary.
        :type autonomous_data_storage_size_in_tbs: float

        :param db_node_storage_size_in_gbs:
            The value to assign to the db_node_storage_size_in_gbs property of this CloudAutonomousVmClusterSummary.
        :type db_node_storage_size_in_gbs: int

        :param memory_per_oracle_compute_unit_in_gbs:
            The value to assign to the memory_per_oracle_compute_unit_in_gbs property of this CloudAutonomousVmClusterSummary.
        :type memory_per_oracle_compute_unit_in_gbs: int

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'availability_domain': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'last_update_history_entry_id': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'hostname': 'str',
            'domain': 'str',
            'cloud_exadata_infrastructure_id': 'str',
            'shape': 'str',
            'node_count': 'int',
            'data_storage_size_in_tbs': 'float',
            'data_storage_size_in_gbs': 'float',
            'cpu_core_count': 'int',
            'ocpu_count': 'float',
            'memory_size_in_gbs': 'int',
            'license_model': 'str',
            'last_maintenance_run_id': 'str',
            'next_maintenance_run_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'available_cpus': 'float',
            'reclaimable_cpus': 'float',
            'available_container_databases': 'int',
            'total_container_databases': 'int',
            'available_autonomous_data_storage_size_in_tbs': 'float',
            'autonomous_data_storage_size_in_tbs': 'float',
            'db_node_storage_size_in_gbs': 'int',
            'memory_per_oracle_compute_unit_in_gbs': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'availability_domain': 'availabilityDomain',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'last_update_history_entry_id': 'lastUpdateHistoryEntryId',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'hostname': 'hostname',
            'domain': 'domain',
            'cloud_exadata_infrastructure_id': 'cloudExadataInfrastructureId',
            'shape': 'shape',
            'node_count': 'nodeCount',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'cpu_core_count': 'cpuCoreCount',
            'ocpu_count': 'ocpuCount',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'license_model': 'licenseModel',
            'last_maintenance_run_id': 'lastMaintenanceRunId',
            'next_maintenance_run_id': 'nextMaintenanceRunId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'available_cpus': 'availableCpus',
            'reclaimable_cpus': 'reclaimableCpus',
            'available_container_databases': 'availableContainerDatabases',
            'total_container_databases': 'totalContainerDatabases',
            'available_autonomous_data_storage_size_in_tbs': 'availableAutonomousDataStorageSizeInTBs',
            'autonomous_data_storage_size_in_tbs': 'autonomousDataStorageSizeInTBs',
            'db_node_storage_size_in_gbs': 'dbNodeStorageSizeInGBs',
            'memory_per_oracle_compute_unit_in_gbs': 'memoryPerOracleComputeUnitInGBs'
        }

        self._id = None
        self._compartment_id = None
        self._description = None
        self._availability_domain = None
        self._subnet_id = None
        self._nsg_ids = None
        self._last_update_history_entry_id = None
        self._lifecycle_state = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_details = None
        self._hostname = None
        self._domain = None
        self._cloud_exadata_infrastructure_id = None
        self._shape = None
        self._node_count = None
        self._data_storage_size_in_tbs = None
        self._data_storage_size_in_gbs = None
        self._cpu_core_count = None
        self._ocpu_count = None
        self._memory_size_in_gbs = None
        self._license_model = None
        self._last_maintenance_run_id = None
        self._next_maintenance_run_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._available_cpus = None
        self._reclaimable_cpus = None
        self._available_container_databases = None
        self._total_container_databases = None
        self._available_autonomous_data_storage_size_in_tbs = None
        self._autonomous_data_storage_size_in_tbs = None
        self._db_node_storage_size_in_gbs = None
        self._memory_per_oracle_compute_unit_in_gbs = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the Cloud Autonomous VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the Cloud Autonomous VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this CloudAutonomousVmClusterSummary.
        User defined description of the cloud Autonomous VM cluster.


        :return: The description of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CloudAutonomousVmClusterSummary.
        User defined description of the cloud Autonomous VM cluster.


        :param description: The description of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._description = description

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CloudAutonomousVmClusterSummary.
        The name of the availability domain that the cloud Autonomous VM cluster is located in.


        :return: The availability_domain of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CloudAutonomousVmClusterSummary.
        The name of the availability domain that the cloud Autonomous VM cluster is located in.


        :param availability_domain: The availability_domain of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the subnet the cloud Autonomous VM Cluster is associated with.

        **Subnet Restrictions:**
        - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the subnet the cloud Autonomous VM Cluster is associated with.

        **Subnet Restrictions:**
        - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CloudAutonomousVmClusterSummary.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds list cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this CloudAutonomousVmClusterSummary.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CloudAutonomousVmClusterSummary.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds list cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this CloudAutonomousVmClusterSummary.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def last_update_history_entry_id(self):
        """
        Gets the last_update_history_entry_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the last maintenance update history. This value is updated when a maintenance update starts.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_update_history_entry_id of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._last_update_history_entry_id

    @last_update_history_entry_id.setter
    def last_update_history_entry_id(self, last_update_history_entry_id):
        """
        Sets the last_update_history_entry_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the last maintenance update history. This value is updated when a maintenance update starts.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_update_history_entry_id: The last_update_history_entry_id of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._last_update_history_entry_id = last_update_history_entry_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CloudAutonomousVmClusterSummary.
        The current state of the cloud Autonomous VM cluster.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CloudAutonomousVmClusterSummary.
        The current state of the cloud Autonomous VM cluster.


        :param lifecycle_state: The lifecycle_state of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CloudAutonomousVmClusterSummary.
        The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.


        :return: The display_name of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CloudAutonomousVmClusterSummary.
        The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.


        :param display_name: The display_name of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this CloudAutonomousVmClusterSummary.
        The date and time that the cloud Autonomous VM cluster was created.


        :return: The time_created of this CloudAutonomousVmClusterSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CloudAutonomousVmClusterSummary.
        The date and time that the cloud Autonomous VM cluster was created.


        :param time_created: The time_created of this CloudAutonomousVmClusterSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this CloudAutonomousVmClusterSummary.
        The last date and time that the cloud Autonomous VM cluster was updated.


        :return: The time_updated of this CloudAutonomousVmClusterSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this CloudAutonomousVmClusterSummary.
        The last date and time that the cloud Autonomous VM cluster was updated.


        :param time_updated: The time_updated of this CloudAutonomousVmClusterSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CloudAutonomousVmClusterSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CloudAutonomousVmClusterSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def hostname(self):
        """
        Gets the hostname of this CloudAutonomousVmClusterSummary.
        The hostname for the cloud Autonomous VM cluster.


        :return: The hostname of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CloudAutonomousVmClusterSummary.
        The hostname for the cloud Autonomous VM cluster.


        :param hostname: The hostname of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._hostname = hostname

    @property
    def domain(self):
        """
        Gets the domain of this CloudAutonomousVmClusterSummary.
        The domain name for the cloud Autonomous VM cluster.


        :return: The domain of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this CloudAutonomousVmClusterSummary.
        The domain name for the cloud Autonomous VM cluster.


        :param domain: The domain of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._domain = domain

    @property
    def cloud_exadata_infrastructure_id(self):
        """
        **[Required]** Gets the cloud_exadata_infrastructure_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_exadata_infrastructure_id of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._cloud_exadata_infrastructure_id

    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(self, cloud_exadata_infrastructure_id):
        """
        Sets the cloud_exadata_infrastructure_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_exadata_infrastructure_id: The cloud_exadata_infrastructure_id of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._cloud_exadata_infrastructure_id = cloud_exadata_infrastructure_id

    @property
    def shape(self):
        """
        Gets the shape of this CloudAutonomousVmClusterSummary.
        The model name of the Exadata hardware running the cloud Autonomous VM cluster.


        :return: The shape of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CloudAutonomousVmClusterSummary.
        The model name of the Exadata hardware running the cloud Autonomous VM cluster.


        :param shape: The shape of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._shape = shape

    @property
    def node_count(self):
        """
        Gets the node_count of this CloudAutonomousVmClusterSummary.
        The number of database servers in the cloud VM cluster.


        :return: The node_count of this CloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this CloudAutonomousVmClusterSummary.
        The number of database servers in the cloud VM cluster.


        :param node_count: The node_count of this CloudAutonomousVmClusterSummary.
        :type: int
        """
        self._node_count = node_count

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        The total data storage allocated, in terabytes (TB).


        :return: The data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        The total data storage allocated, in terabytes (TB).


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        :type: float
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this CloudAutonomousVmClusterSummary.
        The total data storage allocated, in gigabytes (GB).


        :return: The data_storage_size_in_gbs of this CloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this CloudAutonomousVmClusterSummary.
        The total data storage allocated, in gigabytes (GB).


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this CloudAutonomousVmClusterSummary.
        :type: float
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this CloudAutonomousVmClusterSummary.
        The number of CPU cores enabled on the cloud Autonomous VM cluster.


        :return: The cpu_core_count of this CloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CloudAutonomousVmClusterSummary.
        The number of CPU cores enabled on the cloud Autonomous VM cluster.


        :param cpu_core_count: The cpu_core_count of this CloudAutonomousVmClusterSummary.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def ocpu_count(self):
        """
        Gets the ocpu_count of this CloudAutonomousVmClusterSummary.
        The number of CPU cores enabled on the cloud Autonomous VM cluster. Only 1 decimal place is allowed for the fractional part.


        :return: The ocpu_count of this CloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._ocpu_count

    @ocpu_count.setter
    def ocpu_count(self, ocpu_count):
        """
        Sets the ocpu_count of this CloudAutonomousVmClusterSummary.
        The number of CPU cores enabled on the cloud Autonomous VM cluster. Only 1 decimal place is allowed for the fractional part.


        :param ocpu_count: The ocpu_count of this CloudAutonomousVmClusterSummary.
        :type: float
        """
        self._ocpu_count = ocpu_count

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this CloudAutonomousVmClusterSummary.
        The memory allocated in GBs.


        :return: The memory_size_in_gbs of this CloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this CloudAutonomousVmClusterSummary.
        The memory allocated in GBs.


        :param memory_size_in_gbs: The memory_size_in_gbs of this CloudAutonomousVmClusterSummary.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def license_model(self):
        """
        Gets the license_model of this CloudAutonomousVmClusterSummary.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CloudAutonomousVmClusterSummary.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param license_model: The license_model of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def last_maintenance_run_id(self):
        """
        Gets the last_maintenance_run_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_maintenance_run_id of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._last_maintenance_run_id

    @last_maintenance_run_id.setter
    def last_maintenance_run_id(self, last_maintenance_run_id):
        """
        Sets the last_maintenance_run_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_maintenance_run_id: The last_maintenance_run_id of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._last_maintenance_run_id = last_maintenance_run_id

    @property
    def next_maintenance_run_id(self):
        """
        Gets the next_maintenance_run_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The next_maintenance_run_id of this CloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._next_maintenance_run_id

    @next_maintenance_run_id.setter
    def next_maintenance_run_id(self, next_maintenance_run_id):
        """
        Sets the next_maintenance_run_id of this CloudAutonomousVmClusterSummary.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param next_maintenance_run_id: The next_maintenance_run_id of this CloudAutonomousVmClusterSummary.
        :type: str
        """
        self._next_maintenance_run_id = next_maintenance_run_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CloudAutonomousVmClusterSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CloudAutonomousVmClusterSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CloudAutonomousVmClusterSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CloudAutonomousVmClusterSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CloudAutonomousVmClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CloudAutonomousVmClusterSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CloudAutonomousVmClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CloudAutonomousVmClusterSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def available_cpus(self):
        """
        Gets the available_cpus of this CloudAutonomousVmClusterSummary.
        CPU cores available for allocation to Autonomous Databases.


        :return: The available_cpus of this CloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._available_cpus

    @available_cpus.setter
    def available_cpus(self, available_cpus):
        """
        Sets the available_cpus of this CloudAutonomousVmClusterSummary.
        CPU cores available for allocation to Autonomous Databases.


        :param available_cpus: The available_cpus of this CloudAutonomousVmClusterSummary.
        :type: float
        """
        self._available_cpus = available_cpus

    @property
    def reclaimable_cpus(self):
        """
        Gets the reclaimable_cpus of this CloudAutonomousVmClusterSummary.
        CPU cores that are not released to available pool after an Autonomous Database is terminated (Requires Autonomous Container Database restart).


        :return: The reclaimable_cpus of this CloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._reclaimable_cpus

    @reclaimable_cpus.setter
    def reclaimable_cpus(self, reclaimable_cpus):
        """
        Sets the reclaimable_cpus of this CloudAutonomousVmClusterSummary.
        CPU cores that are not released to available pool after an Autonomous Database is terminated (Requires Autonomous Container Database restart).


        :param reclaimable_cpus: The reclaimable_cpus of this CloudAutonomousVmClusterSummary.
        :type: float
        """
        self._reclaimable_cpus = reclaimable_cpus

    @property
    def available_container_databases(self):
        """
        Gets the available_container_databases of this CloudAutonomousVmClusterSummary.
        The number of Autonomous Container Databases that can be created with the currently available local storage.


        :return: The available_container_databases of this CloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._available_container_databases

    @available_container_databases.setter
    def available_container_databases(self, available_container_databases):
        """
        Sets the available_container_databases of this CloudAutonomousVmClusterSummary.
        The number of Autonomous Container Databases that can be created with the currently available local storage.


        :param available_container_databases: The available_container_databases of this CloudAutonomousVmClusterSummary.
        :type: int
        """
        self._available_container_databases = available_container_databases

    @property
    def total_container_databases(self):
        """
        Gets the total_container_databases of this CloudAutonomousVmClusterSummary.
        The total number of Autonomous Container Databases that can be created with the allocated local storage.


        :return: The total_container_databases of this CloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._total_container_databases

    @total_container_databases.setter
    def total_container_databases(self, total_container_databases):
        """
        Sets the total_container_databases of this CloudAutonomousVmClusterSummary.
        The total number of Autonomous Container Databases that can be created with the allocated local storage.


        :param total_container_databases: The total_container_databases of this CloudAutonomousVmClusterSummary.
        :type: int
        """
        self._total_container_databases = total_container_databases

    @property
    def available_autonomous_data_storage_size_in_tbs(self):
        """
        Gets the available_autonomous_data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        The data disk group size available for Autonomous Databases, in TBs.


        :return: The available_autonomous_data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._available_autonomous_data_storage_size_in_tbs

    @available_autonomous_data_storage_size_in_tbs.setter
    def available_autonomous_data_storage_size_in_tbs(self, available_autonomous_data_storage_size_in_tbs):
        """
        Sets the available_autonomous_data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        The data disk group size available for Autonomous Databases, in TBs.


        :param available_autonomous_data_storage_size_in_tbs: The available_autonomous_data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        :type: float
        """
        self._available_autonomous_data_storage_size_in_tbs = available_autonomous_data_storage_size_in_tbs

    @property
    def autonomous_data_storage_size_in_tbs(self):
        """
        Gets the autonomous_data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        The data disk group size allocated for Autonomous Databases, in TBs.


        :return: The autonomous_data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._autonomous_data_storage_size_in_tbs

    @autonomous_data_storage_size_in_tbs.setter
    def autonomous_data_storage_size_in_tbs(self, autonomous_data_storage_size_in_tbs):
        """
        Sets the autonomous_data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        The data disk group size allocated for Autonomous Databases, in TBs.


        :param autonomous_data_storage_size_in_tbs: The autonomous_data_storage_size_in_tbs of this CloudAutonomousVmClusterSummary.
        :type: float
        """
        self._autonomous_data_storage_size_in_tbs = autonomous_data_storage_size_in_tbs

    @property
    def db_node_storage_size_in_gbs(self):
        """
        Gets the db_node_storage_size_in_gbs of this CloudAutonomousVmClusterSummary.
        The local node storage allocated in GBs.


        :return: The db_node_storage_size_in_gbs of this CloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._db_node_storage_size_in_gbs

    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, db_node_storage_size_in_gbs):
        """
        Sets the db_node_storage_size_in_gbs of this CloudAutonomousVmClusterSummary.
        The local node storage allocated in GBs.


        :param db_node_storage_size_in_gbs: The db_node_storage_size_in_gbs of this CloudAutonomousVmClusterSummary.
        :type: int
        """
        self._db_node_storage_size_in_gbs = db_node_storage_size_in_gbs

    @property
    def memory_per_oracle_compute_unit_in_gbs(self):
        """
        Gets the memory_per_oracle_compute_unit_in_gbs of this CloudAutonomousVmClusterSummary.
        The amount of memory (in GBs) enabled per each OCPU core.


        :return: The memory_per_oracle_compute_unit_in_gbs of this CloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._memory_per_oracle_compute_unit_in_gbs

    @memory_per_oracle_compute_unit_in_gbs.setter
    def memory_per_oracle_compute_unit_in_gbs(self, memory_per_oracle_compute_unit_in_gbs):
        """
        Sets the memory_per_oracle_compute_unit_in_gbs of this CloudAutonomousVmClusterSummary.
        The amount of memory (in GBs) enabled per each OCPU core.


        :param memory_per_oracle_compute_unit_in_gbs: The memory_per_oracle_compute_unit_in_gbs of this CloudAutonomousVmClusterSummary.
        :type: int
        """
        self._memory_per_oracle_compute_unit_in_gbs = memory_per_oracle_compute_unit_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
