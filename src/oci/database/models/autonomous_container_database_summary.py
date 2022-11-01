# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousContainerDatabaseSummary(object):
    """
    An Autonomous Container Database is a container database service that enables the customer to host one or more databases within the container database. A basic container database runs on a single Autonomous Exadata Infrastructure from an availability domain without the Extreme Availability features enabled.
    """

    #: A constant which can be used with the service_level_agreement_type property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "STANDARD"
    SERVICE_LEVEL_AGREEMENT_TYPE_STANDARD = "STANDARD"

    #: A constant which can be used with the service_level_agreement_type property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "MISSION_CRITICAL"
    SERVICE_LEVEL_AGREEMENT_TYPE_MISSION_CRITICAL = "MISSION_CRITICAL"

    #: A constant which can be used with the service_level_agreement_type property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "AUTONOMOUS_DATAGUARD"
    SERVICE_LEVEL_AGREEMENT_TYPE_AUTONOMOUS_DATAGUARD = "AUTONOMOUS_DATAGUARD"

    #: A constant which can be used with the infrastructure_type property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "CLOUD"
    INFRASTRUCTURE_TYPE_CLOUD = "CLOUD"

    #: A constant which can be used with the infrastructure_type property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "CLOUD_AT_CUSTOMER"
    INFRASTRUCTURE_TYPE_CLOUD_AT_CUSTOMER = "CLOUD_AT_CUSTOMER"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "RESTORING"
    LIFECYCLE_STATE_RESTORING = "RESTORING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "RESTORE_FAILED"
    LIFECYCLE_STATE_RESTORE_FAILED = "RESTORE_FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "RESTARTING"
    LIFECYCLE_STATE_RESTARTING = "RESTARTING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "ROLE_CHANGE_IN_PROGRESS"
    LIFECYCLE_STATE_ROLE_CHANGE_IN_PROGRESS = "ROLE_CHANGE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "UNAVAILABLE"
    LIFECYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the patch_model property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "RELEASE_UPDATES"
    PATCH_MODEL_RELEASE_UPDATES = "RELEASE_UPDATES"

    #: A constant which can be used with the patch_model property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "RELEASE_UPDATE_REVISIONS"
    PATCH_MODEL_RELEASE_UPDATE_REVISIONS = "RELEASE_UPDATE_REVISIONS"

    #: A constant which can be used with the role property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "STANDBY"
    ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the role property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "DISABLED_STANDBY"
    ROLE_DISABLED_STANDBY = "DISABLED_STANDBY"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousContainerDatabaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousContainerDatabaseSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousContainerDatabaseSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AutonomousContainerDatabaseSummary.
        :type display_name: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this AutonomousContainerDatabaseSummary.
        :type db_unique_name: str

        :param service_level_agreement_type:
            The value to assign to the service_level_agreement_type property of this AutonomousContainerDatabaseSummary.
            Allowed values for this property are: "STANDARD", "MISSION_CRITICAL", "AUTONOMOUS_DATAGUARD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_level_agreement_type: str

        :param autonomous_exadata_infrastructure_id:
            The value to assign to the autonomous_exadata_infrastructure_id property of this AutonomousContainerDatabaseSummary.
        :type autonomous_exadata_infrastructure_id: str

        :param autonomous_vm_cluster_id:
            The value to assign to the autonomous_vm_cluster_id property of this AutonomousContainerDatabaseSummary.
        :type autonomous_vm_cluster_id: str

        :param infrastructure_type:
            The value to assign to the infrastructure_type property of this AutonomousContainerDatabaseSummary.
            Allowed values for this property are: "CLOUD", "CLOUD_AT_CUSTOMER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type infrastructure_type: str

        :param cloud_autonomous_vm_cluster_id:
            The value to assign to the cloud_autonomous_vm_cluster_id property of this AutonomousContainerDatabaseSummary.
        :type cloud_autonomous_vm_cluster_id: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this AutonomousContainerDatabaseSummary.
        :type kms_key_id: str

        :param vault_id:
            The value to assign to the vault_id property of this AutonomousContainerDatabaseSummary.
        :type vault_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this AutonomousContainerDatabaseSummary.
        :type kms_key_version_id: str

        :param key_history_entry:
            The value to assign to the key_history_entry property of this AutonomousContainerDatabaseSummary.
        :type key_history_entry: list[oci.database.models.AutonomousDatabaseKeyHistoryEntry]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousContainerDatabaseSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS", "ROLE_CHANGE_IN_PROGRESS", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousContainerDatabaseSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this AutonomousContainerDatabaseSummary.
        :type time_created: datetime

        :param patch_model:
            The value to assign to the patch_model property of this AutonomousContainerDatabaseSummary.
            Allowed values for this property are: "RELEASE_UPDATES", "RELEASE_UPDATE_REVISIONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type patch_model: str

        :param patch_id:
            The value to assign to the patch_id property of this AutonomousContainerDatabaseSummary.
        :type patch_id: str

        :param last_maintenance_run_id:
            The value to assign to the last_maintenance_run_id property of this AutonomousContainerDatabaseSummary.
        :type last_maintenance_run_id: str

        :param next_maintenance_run_id:
            The value to assign to the next_maintenance_run_id property of this AutonomousContainerDatabaseSummary.
        :type next_maintenance_run_id: str

        :param maintenance_window:
            The value to assign to the maintenance_window property of this AutonomousContainerDatabaseSummary.
        :type maintenance_window: oci.database.models.MaintenanceWindow

        :param standby_maintenance_buffer_in_days:
            The value to assign to the standby_maintenance_buffer_in_days property of this AutonomousContainerDatabaseSummary.
        :type standby_maintenance_buffer_in_days: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousContainerDatabaseSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousContainerDatabaseSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param role:
            The value to assign to the role property of this AutonomousContainerDatabaseSummary.
            Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param availability_domain:
            The value to assign to the availability_domain property of this AutonomousContainerDatabaseSummary.
        :type availability_domain: str

        :param db_version:
            The value to assign to the db_version property of this AutonomousContainerDatabaseSummary.
        :type db_version: str

        :param backup_config:
            The value to assign to the backup_config property of this AutonomousContainerDatabaseSummary.
        :type backup_config: oci.database.models.AutonomousContainerDatabaseBackupConfig

        :param key_store_id:
            The value to assign to the key_store_id property of this AutonomousContainerDatabaseSummary.
        :type key_store_id: str

        :param key_store_wallet_name:
            The value to assign to the key_store_wallet_name property of this AutonomousContainerDatabaseSummary.
        :type key_store_wallet_name: str

        :param memory_per_oracle_compute_unit_in_gbs:
            The value to assign to the memory_per_oracle_compute_unit_in_gbs property of this AutonomousContainerDatabaseSummary.
        :type memory_per_oracle_compute_unit_in_gbs: int

        :param available_cpus:
            The value to assign to the available_cpus property of this AutonomousContainerDatabaseSummary.
        :type available_cpus: float

        :param total_cpus:
            The value to assign to the total_cpus property of this AutonomousContainerDatabaseSummary.
        :type total_cpus: int

        :param reclaimable_cpus:
            The value to assign to the reclaimable_cpus property of this AutonomousContainerDatabaseSummary.
        :type reclaimable_cpus: float

        :param provisionable_cpus:
            The value to assign to the provisionable_cpus property of this AutonomousContainerDatabaseSummary.
        :type provisionable_cpus: list[float]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'db_unique_name': 'str',
            'service_level_agreement_type': 'str',
            'autonomous_exadata_infrastructure_id': 'str',
            'autonomous_vm_cluster_id': 'str',
            'infrastructure_type': 'str',
            'cloud_autonomous_vm_cluster_id': 'str',
            'kms_key_id': 'str',
            'vault_id': 'str',
            'kms_key_version_id': 'str',
            'key_history_entry': 'list[AutonomousDatabaseKeyHistoryEntry]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'patch_model': 'str',
            'patch_id': 'str',
            'last_maintenance_run_id': 'str',
            'next_maintenance_run_id': 'str',
            'maintenance_window': 'MaintenanceWindow',
            'standby_maintenance_buffer_in_days': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'role': 'str',
            'availability_domain': 'str',
            'db_version': 'str',
            'backup_config': 'AutonomousContainerDatabaseBackupConfig',
            'key_store_id': 'str',
            'key_store_wallet_name': 'str',
            'memory_per_oracle_compute_unit_in_gbs': 'int',
            'available_cpus': 'float',
            'total_cpus': 'int',
            'reclaimable_cpus': 'float',
            'provisionable_cpus': 'list[float]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'db_unique_name': 'dbUniqueName',
            'service_level_agreement_type': 'serviceLevelAgreementType',
            'autonomous_exadata_infrastructure_id': 'autonomousExadataInfrastructureId',
            'autonomous_vm_cluster_id': 'autonomousVmClusterId',
            'infrastructure_type': 'infrastructureType',
            'cloud_autonomous_vm_cluster_id': 'cloudAutonomousVmClusterId',
            'kms_key_id': 'kmsKeyId',
            'vault_id': 'vaultId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'key_history_entry': 'keyHistoryEntry',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'patch_model': 'patchModel',
            'patch_id': 'patchId',
            'last_maintenance_run_id': 'lastMaintenanceRunId',
            'next_maintenance_run_id': 'nextMaintenanceRunId',
            'maintenance_window': 'maintenanceWindow',
            'standby_maintenance_buffer_in_days': 'standbyMaintenanceBufferInDays',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'role': 'role',
            'availability_domain': 'availabilityDomain',
            'db_version': 'dbVersion',
            'backup_config': 'backupConfig',
            'key_store_id': 'keyStoreId',
            'key_store_wallet_name': 'keyStoreWalletName',
            'memory_per_oracle_compute_unit_in_gbs': 'memoryPerOracleComputeUnitInGBs',
            'available_cpus': 'availableCpus',
            'total_cpus': 'totalCpus',
            'reclaimable_cpus': 'reclaimableCpus',
            'provisionable_cpus': 'provisionableCpus'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._db_unique_name = None
        self._service_level_agreement_type = None
        self._autonomous_exadata_infrastructure_id = None
        self._autonomous_vm_cluster_id = None
        self._infrastructure_type = None
        self._cloud_autonomous_vm_cluster_id = None
        self._kms_key_id = None
        self._vault_id = None
        self._kms_key_version_id = None
        self._key_history_entry = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._patch_model = None
        self._patch_id = None
        self._last_maintenance_run_id = None
        self._next_maintenance_run_id = None
        self._maintenance_window = None
        self._standby_maintenance_buffer_in_days = None
        self._freeform_tags = None
        self._defined_tags = None
        self._role = None
        self._availability_domain = None
        self._db_version = None
        self._backup_config = None
        self._key_store_id = None
        self._key_store_wallet_name = None
        self._memory_per_oracle_compute_unit_in_gbs = None
        self._available_cpus = None
        self._total_cpus = None
        self._reclaimable_cpus = None
        self._provisionable_cpus = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousContainerDatabaseSummary.
        The OCID of the Autonomous Container Database.


        :return: The id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousContainerDatabaseSummary.
        The OCID of the Autonomous Container Database.


        :param id: The id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AutonomousContainerDatabaseSummary.
        The OCID of the compartment.


        :return: The compartment_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutonomousContainerDatabaseSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AutonomousContainerDatabaseSummary.
        The user-provided name for the Autonomous Container Database.


        :return: The display_name of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutonomousContainerDatabaseSummary.
        The user-provided name for the Autonomous Container Database.


        :param display_name: The display_name of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def db_unique_name(self):
        """
        Gets the db_unique_name of this AutonomousContainerDatabaseSummary.
        **Deprecated.** The `DB_UNIQUE_NAME` value is set by Oracle Cloud Infrastructure.  Do not specify a value for this parameter. Specifying a value for this field will cause Terraform operations to fail.


        :return: The db_unique_name of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this AutonomousContainerDatabaseSummary.
        **Deprecated.** The `DB_UNIQUE_NAME` value is set by Oracle Cloud Infrastructure.  Do not specify a value for this parameter. Specifying a value for this field will cause Terraform operations to fail.


        :param db_unique_name: The db_unique_name of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def service_level_agreement_type(self):
        """
        **[Required]** Gets the service_level_agreement_type of this AutonomousContainerDatabaseSummary.
        The service level agreement type of the container database. The default is STANDARD.

        Allowed values for this property are: "STANDARD", "MISSION_CRITICAL", "AUTONOMOUS_DATAGUARD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The service_level_agreement_type of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._service_level_agreement_type

    @service_level_agreement_type.setter
    def service_level_agreement_type(self, service_level_agreement_type):
        """
        Sets the service_level_agreement_type of this AutonomousContainerDatabaseSummary.
        The service level agreement type of the container database. The default is STANDARD.


        :param service_level_agreement_type: The service_level_agreement_type of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        allowed_values = ["STANDARD", "MISSION_CRITICAL", "AUTONOMOUS_DATAGUARD"]
        if not value_allowed_none_or_none_sentinel(service_level_agreement_type, allowed_values):
            service_level_agreement_type = 'UNKNOWN_ENUM_VALUE'
        self._service_level_agreement_type = service_level_agreement_type

    @property
    def autonomous_exadata_infrastructure_id(self):
        """
        Gets the autonomous_exadata_infrastructure_id of this AutonomousContainerDatabaseSummary.
        **No longer used.** For Autonomous Database on dedicated Exadata infrastructure, the container database is created within a specified `cloudAutonomousVmCluster`.


        :return: The autonomous_exadata_infrastructure_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._autonomous_exadata_infrastructure_id

    @autonomous_exadata_infrastructure_id.setter
    def autonomous_exadata_infrastructure_id(self, autonomous_exadata_infrastructure_id):
        """
        Sets the autonomous_exadata_infrastructure_id of this AutonomousContainerDatabaseSummary.
        **No longer used.** For Autonomous Database on dedicated Exadata infrastructure, the container database is created within a specified `cloudAutonomousVmCluster`.


        :param autonomous_exadata_infrastructure_id: The autonomous_exadata_infrastructure_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._autonomous_exadata_infrastructure_id = autonomous_exadata_infrastructure_id

    @property
    def autonomous_vm_cluster_id(self):
        """
        Gets the autonomous_vm_cluster_id of this AutonomousContainerDatabaseSummary.
        The OCID of the Autonomous VM Cluster.


        :return: The autonomous_vm_cluster_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._autonomous_vm_cluster_id

    @autonomous_vm_cluster_id.setter
    def autonomous_vm_cluster_id(self, autonomous_vm_cluster_id):
        """
        Sets the autonomous_vm_cluster_id of this AutonomousContainerDatabaseSummary.
        The OCID of the Autonomous VM Cluster.


        :param autonomous_vm_cluster_id: The autonomous_vm_cluster_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._autonomous_vm_cluster_id = autonomous_vm_cluster_id

    @property
    def infrastructure_type(self):
        """
        Gets the infrastructure_type of this AutonomousContainerDatabaseSummary.
        The infrastructure type this resource belongs to.

        Allowed values for this property are: "CLOUD", "CLOUD_AT_CUSTOMER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The infrastructure_type of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._infrastructure_type

    @infrastructure_type.setter
    def infrastructure_type(self, infrastructure_type):
        """
        Sets the infrastructure_type of this AutonomousContainerDatabaseSummary.
        The infrastructure type this resource belongs to.


        :param infrastructure_type: The infrastructure_type of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        allowed_values = ["CLOUD", "CLOUD_AT_CUSTOMER"]
        if not value_allowed_none_or_none_sentinel(infrastructure_type, allowed_values):
            infrastructure_type = 'UNKNOWN_ENUM_VALUE'
        self._infrastructure_type = infrastructure_type

    @property
    def cloud_autonomous_vm_cluster_id(self):
        """
        Gets the cloud_autonomous_vm_cluster_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the cloud Autonomous Exadata VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_autonomous_vm_cluster_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._cloud_autonomous_vm_cluster_id

    @cloud_autonomous_vm_cluster_id.setter
    def cloud_autonomous_vm_cluster_id(self, cloud_autonomous_vm_cluster_id):
        """
        Sets the cloud_autonomous_vm_cluster_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the cloud Autonomous Exadata VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_autonomous_vm_cluster_id: The cloud_autonomous_vm_cluster_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._cloud_autonomous_vm_cluster_id = cloud_autonomous_vm_cluster_id

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this AutonomousContainerDatabaseSummary.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :return: The kms_key_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this AutonomousContainerDatabaseSummary.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :param kms_key_id: The kms_key_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def vault_id(self):
        """
        Gets the vault_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The vault_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param vault_id: The vault_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def kms_key_version_id(self):
        """
        Gets the kms_key_version_id of this AutonomousContainerDatabaseSummary.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :return: The kms_key_version_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._kms_key_version_id

    @kms_key_version_id.setter
    def kms_key_version_id(self, kms_key_version_id):
        """
        Sets the kms_key_version_id of this AutonomousContainerDatabaseSummary.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :param kms_key_version_id: The kms_key_version_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._kms_key_version_id = kms_key_version_id

    @property
    def key_history_entry(self):
        """
        Gets the key_history_entry of this AutonomousContainerDatabaseSummary.
        Key History Entry.


        :return: The key_history_entry of this AutonomousContainerDatabaseSummary.
        :rtype: list[oci.database.models.AutonomousDatabaseKeyHistoryEntry]
        """
        return self._key_history_entry

    @key_history_entry.setter
    def key_history_entry(self, key_history_entry):
        """
        Sets the key_history_entry of this AutonomousContainerDatabaseSummary.
        Key History Entry.


        :param key_history_entry: The key_history_entry of this AutonomousContainerDatabaseSummary.
        :type: list[oci.database.models.AutonomousDatabaseKeyHistoryEntry]
        """
        self._key_history_entry = key_history_entry

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousContainerDatabaseSummary.
        The current state of the Autonomous Container Database.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS", "ROLE_CHANGE_IN_PROGRESS", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousContainerDatabaseSummary.
        The current state of the Autonomous Container Database.


        :param lifecycle_state: The lifecycle_state of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS", "ROLE_CHANGE_IN_PROGRESS", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousContainerDatabaseSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousContainerDatabaseSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        Gets the time_created of this AutonomousContainerDatabaseSummary.
        The date and time the Autonomous Container Database was created.


        :return: The time_created of this AutonomousContainerDatabaseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutonomousContainerDatabaseSummary.
        The date and time the Autonomous Container Database was created.


        :param time_created: The time_created of this AutonomousContainerDatabaseSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def patch_model(self):
        """
        **[Required]** Gets the patch_model of this AutonomousContainerDatabaseSummary.
        Database patch model preference.

        Allowed values for this property are: "RELEASE_UPDATES", "RELEASE_UPDATE_REVISIONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The patch_model of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._patch_model

    @patch_model.setter
    def patch_model(self, patch_model):
        """
        Sets the patch_model of this AutonomousContainerDatabaseSummary.
        Database patch model preference.


        :param patch_model: The patch_model of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        allowed_values = ["RELEASE_UPDATES", "RELEASE_UPDATE_REVISIONS"]
        if not value_allowed_none_or_none_sentinel(patch_model, allowed_values):
            patch_model = 'UNKNOWN_ENUM_VALUE'
        self._patch_model = patch_model

    @property
    def patch_id(self):
        """
        Gets the patch_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the last patch applied on the system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The patch_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._patch_id

    @patch_id.setter
    def patch_id(self, patch_id):
        """
        Sets the patch_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the last patch applied on the system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param patch_id: The patch_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._patch_id = patch_id

    @property
    def last_maintenance_run_id(self):
        """
        Gets the last_maintenance_run_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_maintenance_run_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._last_maintenance_run_id

    @last_maintenance_run_id.setter
    def last_maintenance_run_id(self, last_maintenance_run_id):
        """
        Sets the last_maintenance_run_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_maintenance_run_id: The last_maintenance_run_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._last_maintenance_run_id = last_maintenance_run_id

    @property
    def next_maintenance_run_id(self):
        """
        Gets the next_maintenance_run_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The next_maintenance_run_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._next_maintenance_run_id

    @next_maintenance_run_id.setter
    def next_maintenance_run_id(self, next_maintenance_run_id):
        """
        Sets the next_maintenance_run_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param next_maintenance_run_id: The next_maintenance_run_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._next_maintenance_run_id = next_maintenance_run_id

    @property
    def maintenance_window(self):
        """
        Gets the maintenance_window of this AutonomousContainerDatabaseSummary.

        :return: The maintenance_window of this AutonomousContainerDatabaseSummary.
        :rtype: oci.database.models.MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """
        Sets the maintenance_window of this AutonomousContainerDatabaseSummary.

        :param maintenance_window: The maintenance_window of this AutonomousContainerDatabaseSummary.
        :type: oci.database.models.MaintenanceWindow
        """
        self._maintenance_window = maintenance_window

    @property
    def standby_maintenance_buffer_in_days(self):
        """
        Gets the standby_maintenance_buffer_in_days of this AutonomousContainerDatabaseSummary.
        The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database.
        This value represents the number of days before scheduled maintenance of the primary database.


        :return: The standby_maintenance_buffer_in_days of this AutonomousContainerDatabaseSummary.
        :rtype: int
        """
        return self._standby_maintenance_buffer_in_days

    @standby_maintenance_buffer_in_days.setter
    def standby_maintenance_buffer_in_days(self, standby_maintenance_buffer_in_days):
        """
        Sets the standby_maintenance_buffer_in_days of this AutonomousContainerDatabaseSummary.
        The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database.
        This value represents the number of days before scheduled maintenance of the primary database.


        :param standby_maintenance_buffer_in_days: The standby_maintenance_buffer_in_days of this AutonomousContainerDatabaseSummary.
        :type: int
        """
        self._standby_maintenance_buffer_in_days = standby_maintenance_buffer_in_days

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AutonomousContainerDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AutonomousContainerDatabaseSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AutonomousContainerDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AutonomousContainerDatabaseSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AutonomousContainerDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AutonomousContainerDatabaseSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AutonomousContainerDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AutonomousContainerDatabaseSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def role(self):
        """
        Gets the role of this AutonomousContainerDatabaseSummary.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

        Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this AutonomousContainerDatabaseSummary.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.


        :param role: The role of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "DISABLED_STANDBY"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this AutonomousContainerDatabaseSummary.
        The availability domain of the Autonomous Container Database.


        :return: The availability_domain of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this AutonomousContainerDatabaseSummary.
        The availability domain of the Autonomous Container Database.


        :param availability_domain: The availability_domain of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def db_version(self):
        """
        Gets the db_version of this AutonomousContainerDatabaseSummary.
        Oracle Database version of the Autonomous Container Database.


        :return: The db_version of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this AutonomousContainerDatabaseSummary.
        Oracle Database version of the Autonomous Container Database.


        :param db_version: The db_version of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def backup_config(self):
        """
        Gets the backup_config of this AutonomousContainerDatabaseSummary.

        :return: The backup_config of this AutonomousContainerDatabaseSummary.
        :rtype: oci.database.models.AutonomousContainerDatabaseBackupConfig
        """
        return self._backup_config

    @backup_config.setter
    def backup_config(self, backup_config):
        """
        Sets the backup_config of this AutonomousContainerDatabaseSummary.

        :param backup_config: The backup_config of this AutonomousContainerDatabaseSummary.
        :type: oci.database.models.AutonomousContainerDatabaseBackupConfig
        """
        self._backup_config = backup_config

    @property
    def key_store_id(self):
        """
        Gets the key_store_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the key store.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_store_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._key_store_id

    @key_store_id.setter
    def key_store_id(self, key_store_id):
        """
        Sets the key_store_id of this AutonomousContainerDatabaseSummary.
        The `OCID`__ of the key store.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_store_id: The key_store_id of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._key_store_id = key_store_id

    @property
    def key_store_wallet_name(self):
        """
        Gets the key_store_wallet_name of this AutonomousContainerDatabaseSummary.
        The wallet name for Oracle Key Vault.


        :return: The key_store_wallet_name of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._key_store_wallet_name

    @key_store_wallet_name.setter
    def key_store_wallet_name(self, key_store_wallet_name):
        """
        Sets the key_store_wallet_name of this AutonomousContainerDatabaseSummary.
        The wallet name for Oracle Key Vault.


        :param key_store_wallet_name: The key_store_wallet_name of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._key_store_wallet_name = key_store_wallet_name

    @property
    def memory_per_oracle_compute_unit_in_gbs(self):
        """
        Gets the memory_per_oracle_compute_unit_in_gbs of this AutonomousContainerDatabaseSummary.
        The amount of memory (in GBs) enabled per each OCPU core in Autonomous VM Cluster.


        :return: The memory_per_oracle_compute_unit_in_gbs of this AutonomousContainerDatabaseSummary.
        :rtype: int
        """
        return self._memory_per_oracle_compute_unit_in_gbs

    @memory_per_oracle_compute_unit_in_gbs.setter
    def memory_per_oracle_compute_unit_in_gbs(self, memory_per_oracle_compute_unit_in_gbs):
        """
        Sets the memory_per_oracle_compute_unit_in_gbs of this AutonomousContainerDatabaseSummary.
        The amount of memory (in GBs) enabled per each OCPU core in Autonomous VM Cluster.


        :param memory_per_oracle_compute_unit_in_gbs: The memory_per_oracle_compute_unit_in_gbs of this AutonomousContainerDatabaseSummary.
        :type: int
        """
        self._memory_per_oracle_compute_unit_in_gbs = memory_per_oracle_compute_unit_in_gbs

    @property
    def available_cpus(self):
        """
        Gets the available_cpus of this AutonomousContainerDatabaseSummary.
        Sum of OCPUs available on the Autonomous VM Cluster + Sum of reclaimable OCPUs available in the Autonomous Container Database.


        :return: The available_cpus of this AutonomousContainerDatabaseSummary.
        :rtype: float
        """
        return self._available_cpus

    @available_cpus.setter
    def available_cpus(self, available_cpus):
        """
        Sets the available_cpus of this AutonomousContainerDatabaseSummary.
        Sum of OCPUs available on the Autonomous VM Cluster + Sum of reclaimable OCPUs available in the Autonomous Container Database.


        :param available_cpus: The available_cpus of this AutonomousContainerDatabaseSummary.
        :type: float
        """
        self._available_cpus = available_cpus

    @property
    def total_cpus(self):
        """
        Gets the total_cpus of this AutonomousContainerDatabaseSummary.
        The number of CPU cores allocated to the Autonomous VM cluster.


        :return: The total_cpus of this AutonomousContainerDatabaseSummary.
        :rtype: int
        """
        return self._total_cpus

    @total_cpus.setter
    def total_cpus(self, total_cpus):
        """
        Sets the total_cpus of this AutonomousContainerDatabaseSummary.
        The number of CPU cores allocated to the Autonomous VM cluster.


        :param total_cpus: The total_cpus of this AutonomousContainerDatabaseSummary.
        :type: int
        """
        self._total_cpus = total_cpus

    @property
    def reclaimable_cpus(self):
        """
        Gets the reclaimable_cpus of this AutonomousContainerDatabaseSummary.
        CPU cores that continue to be included in the count of OCPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous Container Database.


        :return: The reclaimable_cpus of this AutonomousContainerDatabaseSummary.
        :rtype: float
        """
        return self._reclaimable_cpus

    @reclaimable_cpus.setter
    def reclaimable_cpus(self, reclaimable_cpus):
        """
        Sets the reclaimable_cpus of this AutonomousContainerDatabaseSummary.
        CPU cores that continue to be included in the count of OCPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous Container Database.


        :param reclaimable_cpus: The reclaimable_cpus of this AutonomousContainerDatabaseSummary.
        :type: float
        """
        self._reclaimable_cpus = reclaimable_cpus

    @property
    def provisionable_cpus(self):
        """
        Gets the provisionable_cpus of this AutonomousContainerDatabaseSummary.
        An array of CPU values that can be used to successfully provision a single Autonomous Database.


        :return: The provisionable_cpus of this AutonomousContainerDatabaseSummary.
        :rtype: list[float]
        """
        return self._provisionable_cpus

    @provisionable_cpus.setter
    def provisionable_cpus(self, provisionable_cpus):
        """
        Sets the provisionable_cpus of this AutonomousContainerDatabaseSummary.
        An array of CPU values that can be used to successfully provision a single Autonomous Database.


        :param provisionable_cpus: The provisionable_cpus of this AutonomousContainerDatabaseSummary.
        :type: list[float]
        """
        self._provisionable_cpus = provisionable_cpus

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
