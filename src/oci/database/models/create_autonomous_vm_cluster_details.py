# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousVmClusterDetails(object):
    """
    Details for the create Autonomous VM cluster operation.
    """

    #: A constant which can be used with the license_model property of a CreateAutonomousVmClusterDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateAutonomousVmClusterDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousVmClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutonomousVmClusterDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousVmClusterDetails.
        :type display_name: str

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this CreateAutonomousVmClusterDetails.
        :type exadata_infrastructure_id: str

        :param vm_cluster_network_id:
            The value to assign to the vm_cluster_network_id property of this CreateAutonomousVmClusterDetails.
        :type vm_cluster_network_id: str

        :param time_zone:
            The value to assign to the time_zone property of this CreateAutonomousVmClusterDetails.
        :type time_zone: str

        :param is_local_backup_enabled:
            The value to assign to the is_local_backup_enabled property of this CreateAutonomousVmClusterDetails.
        :type is_local_backup_enabled: bool

        :param license_model:
            The value to assign to the license_model property of this CreateAutonomousVmClusterDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param total_container_databases:
            The value to assign to the total_container_databases property of this CreateAutonomousVmClusterDetails.
        :type total_container_databases: int

        :param cpu_core_count_per_node:
            The value to assign to the cpu_core_count_per_node property of this CreateAutonomousVmClusterDetails.
        :type cpu_core_count_per_node: int

        :param memory_per_oracle_compute_unit_in_gbs:
            The value to assign to the memory_per_oracle_compute_unit_in_gbs property of this CreateAutonomousVmClusterDetails.
        :type memory_per_oracle_compute_unit_in_gbs: int

        :param autonomous_data_storage_size_in_tbs:
            The value to assign to the autonomous_data_storage_size_in_tbs property of this CreateAutonomousVmClusterDetails.
        :type autonomous_data_storage_size_in_tbs: float

        :param maintenance_window_details:
            The value to assign to the maintenance_window_details property of this CreateAutonomousVmClusterDetails.
        :type maintenance_window_details: oci.database.models.MaintenanceWindow

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousVmClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousVmClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param scan_listener_port_tls:
            The value to assign to the scan_listener_port_tls property of this CreateAutonomousVmClusterDetails.
        :type scan_listener_port_tls: int

        :param scan_listener_port_non_tls:
            The value to assign to the scan_listener_port_non_tls property of this CreateAutonomousVmClusterDetails.
        :type scan_listener_port_non_tls: int

        :param is_mtls_enabled:
            The value to assign to the is_mtls_enabled property of this CreateAutonomousVmClusterDetails.
        :type is_mtls_enabled: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'exadata_infrastructure_id': 'str',
            'vm_cluster_network_id': 'str',
            'time_zone': 'str',
            'is_local_backup_enabled': 'bool',
            'license_model': 'str',
            'total_container_databases': 'int',
            'cpu_core_count_per_node': 'int',
            'memory_per_oracle_compute_unit_in_gbs': 'int',
            'autonomous_data_storage_size_in_tbs': 'float',
            'maintenance_window_details': 'MaintenanceWindow',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'scan_listener_port_tls': 'int',
            'scan_listener_port_non_tls': 'int',
            'is_mtls_enabled': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'exadata_infrastructure_id': 'exadataInfrastructureId',
            'vm_cluster_network_id': 'vmClusterNetworkId',
            'time_zone': 'timeZone',
            'is_local_backup_enabled': 'isLocalBackupEnabled',
            'license_model': 'licenseModel',
            'total_container_databases': 'totalContainerDatabases',
            'cpu_core_count_per_node': 'cpuCoreCountPerNode',
            'memory_per_oracle_compute_unit_in_gbs': 'memoryPerOracleComputeUnitInGBs',
            'autonomous_data_storage_size_in_tbs': 'autonomousDataStorageSizeInTBs',
            'maintenance_window_details': 'maintenanceWindowDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'scan_listener_port_tls': 'scanListenerPortTls',
            'scan_listener_port_non_tls': 'scanListenerPortNonTls',
            'is_mtls_enabled': 'isMtlsEnabled'
        }

        self._compartment_id = None
        self._display_name = None
        self._exadata_infrastructure_id = None
        self._vm_cluster_network_id = None
        self._time_zone = None
        self._is_local_backup_enabled = None
        self._license_model = None
        self._total_container_databases = None
        self._cpu_core_count_per_node = None
        self._memory_per_oracle_compute_unit_in_gbs = None
        self._autonomous_data_storage_size_in_tbs = None
        self._maintenance_window_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._scan_listener_port_tls = None
        self._scan_listener_port_non_tls = None
        self._is_mtls_enabled = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAutonomousVmClusterDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAutonomousVmClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAutonomousVmClusterDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAutonomousVmClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateAutonomousVmClusterDetails.
        The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.


        :return: The display_name of this CreateAutonomousVmClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutonomousVmClusterDetails.
        The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.


        :param display_name: The display_name of this CreateAutonomousVmClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def exadata_infrastructure_id(self):
        """
        **[Required]** Gets the exadata_infrastructure_id of this CreateAutonomousVmClusterDetails.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this CreateAutonomousVmClusterDetails.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this CreateAutonomousVmClusterDetails.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this CreateAutonomousVmClusterDetails.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    @property
    def vm_cluster_network_id(self):
        """
        **[Required]** Gets the vm_cluster_network_id of this CreateAutonomousVmClusterDetails.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vm_cluster_network_id of this CreateAutonomousVmClusterDetails.
        :rtype: str
        """
        return self._vm_cluster_network_id

    @vm_cluster_network_id.setter
    def vm_cluster_network_id(self, vm_cluster_network_id):
        """
        Sets the vm_cluster_network_id of this CreateAutonomousVmClusterDetails.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vm_cluster_network_id: The vm_cluster_network_id of this CreateAutonomousVmClusterDetails.
        :type: str
        """
        self._vm_cluster_network_id = vm_cluster_network_id

    @property
    def time_zone(self):
        """
        Gets the time_zone of this CreateAutonomousVmClusterDetails.
        The time zone to use for the Autonomous VM cluster. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this CreateAutonomousVmClusterDetails.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this CreateAutonomousVmClusterDetails.
        The time zone to use for the Autonomous VM cluster. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this CreateAutonomousVmClusterDetails.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def is_local_backup_enabled(self):
        """
        Gets the is_local_backup_enabled of this CreateAutonomousVmClusterDetails.
        If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata storage is not available in the Autonomous VM cluster.


        :return: The is_local_backup_enabled of this CreateAutonomousVmClusterDetails.
        :rtype: bool
        """
        return self._is_local_backup_enabled

    @is_local_backup_enabled.setter
    def is_local_backup_enabled(self, is_local_backup_enabled):
        """
        Sets the is_local_backup_enabled of this CreateAutonomousVmClusterDetails.
        If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata storage is not available in the Autonomous VM cluster.


        :param is_local_backup_enabled: The is_local_backup_enabled of this CreateAutonomousVmClusterDetails.
        :type: bool
        """
        self._is_local_backup_enabled = is_local_backup_enabled

    @property
    def license_model(self):
        """
        Gets the license_model of this CreateAutonomousVmClusterDetails.
        The Oracle license model that applies to the Autonomous VM cluster. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateAutonomousVmClusterDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateAutonomousVmClusterDetails.
        The Oracle license model that applies to the Autonomous VM cluster. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this CreateAutonomousVmClusterDetails.
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
    def total_container_databases(self):
        """
        Gets the total_container_databases of this CreateAutonomousVmClusterDetails.
        The total number of Autonomous Container Databases that can be created.


        :return: The total_container_databases of this CreateAutonomousVmClusterDetails.
        :rtype: int
        """
        return self._total_container_databases

    @total_container_databases.setter
    def total_container_databases(self, total_container_databases):
        """
        Sets the total_container_databases of this CreateAutonomousVmClusterDetails.
        The total number of Autonomous Container Databases that can be created.


        :param total_container_databases: The total_container_databases of this CreateAutonomousVmClusterDetails.
        :type: int
        """
        self._total_container_databases = total_container_databases

    @property
    def cpu_core_count_per_node(self):
        """
        Gets the cpu_core_count_per_node of this CreateAutonomousVmClusterDetails.
        The number of CPU cores to enable per VM cluster node.


        :return: The cpu_core_count_per_node of this CreateAutonomousVmClusterDetails.
        :rtype: int
        """
        return self._cpu_core_count_per_node

    @cpu_core_count_per_node.setter
    def cpu_core_count_per_node(self, cpu_core_count_per_node):
        """
        Sets the cpu_core_count_per_node of this CreateAutonomousVmClusterDetails.
        The number of CPU cores to enable per VM cluster node.


        :param cpu_core_count_per_node: The cpu_core_count_per_node of this CreateAutonomousVmClusterDetails.
        :type: int
        """
        self._cpu_core_count_per_node = cpu_core_count_per_node

    @property
    def memory_per_oracle_compute_unit_in_gbs(self):
        """
        Gets the memory_per_oracle_compute_unit_in_gbs of this CreateAutonomousVmClusterDetails.
        The amount of memory (in GBs) to be enabled per each OCPU core.


        :return: The memory_per_oracle_compute_unit_in_gbs of this CreateAutonomousVmClusterDetails.
        :rtype: int
        """
        return self._memory_per_oracle_compute_unit_in_gbs

    @memory_per_oracle_compute_unit_in_gbs.setter
    def memory_per_oracle_compute_unit_in_gbs(self, memory_per_oracle_compute_unit_in_gbs):
        """
        Sets the memory_per_oracle_compute_unit_in_gbs of this CreateAutonomousVmClusterDetails.
        The amount of memory (in GBs) to be enabled per each OCPU core.


        :param memory_per_oracle_compute_unit_in_gbs: The memory_per_oracle_compute_unit_in_gbs of this CreateAutonomousVmClusterDetails.
        :type: int
        """
        self._memory_per_oracle_compute_unit_in_gbs = memory_per_oracle_compute_unit_in_gbs

    @property
    def autonomous_data_storage_size_in_tbs(self):
        """
        Gets the autonomous_data_storage_size_in_tbs of this CreateAutonomousVmClusterDetails.
        The data disk group size to be allocated for Autonomous Databases, in TBs.


        :return: The autonomous_data_storage_size_in_tbs of this CreateAutonomousVmClusterDetails.
        :rtype: float
        """
        return self._autonomous_data_storage_size_in_tbs

    @autonomous_data_storage_size_in_tbs.setter
    def autonomous_data_storage_size_in_tbs(self, autonomous_data_storage_size_in_tbs):
        """
        Sets the autonomous_data_storage_size_in_tbs of this CreateAutonomousVmClusterDetails.
        The data disk group size to be allocated for Autonomous Databases, in TBs.


        :param autonomous_data_storage_size_in_tbs: The autonomous_data_storage_size_in_tbs of this CreateAutonomousVmClusterDetails.
        :type: float
        """
        self._autonomous_data_storage_size_in_tbs = autonomous_data_storage_size_in_tbs

    @property
    def maintenance_window_details(self):
        """
        Gets the maintenance_window_details of this CreateAutonomousVmClusterDetails.

        :return: The maintenance_window_details of this CreateAutonomousVmClusterDetails.
        :rtype: oci.database.models.MaintenanceWindow
        """
        return self._maintenance_window_details

    @maintenance_window_details.setter
    def maintenance_window_details(self, maintenance_window_details):
        """
        Sets the maintenance_window_details of this CreateAutonomousVmClusterDetails.

        :param maintenance_window_details: The maintenance_window_details of this CreateAutonomousVmClusterDetails.
        :type: oci.database.models.MaintenanceWindow
        """
        self._maintenance_window_details = maintenance_window_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAutonomousVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAutonomousVmClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAutonomousVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAutonomousVmClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAutonomousVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAutonomousVmClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAutonomousVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAutonomousVmClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def scan_listener_port_tls(self):
        """
        Gets the scan_listener_port_tls of this CreateAutonomousVmClusterDetails.
        The SCAN Listener TLS port number. Default value is 2484.


        :return: The scan_listener_port_tls of this CreateAutonomousVmClusterDetails.
        :rtype: int
        """
        return self._scan_listener_port_tls

    @scan_listener_port_tls.setter
    def scan_listener_port_tls(self, scan_listener_port_tls):
        """
        Sets the scan_listener_port_tls of this CreateAutonomousVmClusterDetails.
        The SCAN Listener TLS port number. Default value is 2484.


        :param scan_listener_port_tls: The scan_listener_port_tls of this CreateAutonomousVmClusterDetails.
        :type: int
        """
        self._scan_listener_port_tls = scan_listener_port_tls

    @property
    def scan_listener_port_non_tls(self):
        """
        Gets the scan_listener_port_non_tls of this CreateAutonomousVmClusterDetails.
        The SCAN Listener Non TLS port number. Default value is 1521.


        :return: The scan_listener_port_non_tls of this CreateAutonomousVmClusterDetails.
        :rtype: int
        """
        return self._scan_listener_port_non_tls

    @scan_listener_port_non_tls.setter
    def scan_listener_port_non_tls(self, scan_listener_port_non_tls):
        """
        Sets the scan_listener_port_non_tls of this CreateAutonomousVmClusterDetails.
        The SCAN Listener Non TLS port number. Default value is 1521.


        :param scan_listener_port_non_tls: The scan_listener_port_non_tls of this CreateAutonomousVmClusterDetails.
        :type: int
        """
        self._scan_listener_port_non_tls = scan_listener_port_non_tls

    @property
    def is_mtls_enabled(self):
        """
        Gets the is_mtls_enabled of this CreateAutonomousVmClusterDetails.
        Enable mutual TLS(mTLS) authentication for database at time of provisioning a VMCluster.Default is TLS.


        :return: The is_mtls_enabled of this CreateAutonomousVmClusterDetails.
        :rtype: bool
        """
        return self._is_mtls_enabled

    @is_mtls_enabled.setter
    def is_mtls_enabled(self, is_mtls_enabled):
        """
        Sets the is_mtls_enabled of this CreateAutonomousVmClusterDetails.
        Enable mutual TLS(mTLS) authentication for database at time of provisioning a VMCluster.Default is TLS.


        :param is_mtls_enabled: The is_mtls_enabled of this CreateAutonomousVmClusterDetails.
        :type: bool
        """
        self._is_mtls_enabled = is_mtls_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
