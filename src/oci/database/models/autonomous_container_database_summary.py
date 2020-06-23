# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

    #: A constant which can be used with the patch_model property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "RELEASE_UPDATES"
    PATCH_MODEL_RELEASE_UPDATES = "RELEASE_UPDATES"

    #: A constant which can be used with the patch_model property of a AutonomousContainerDatabaseSummary.
    #: This constant has a value of "RELEASE_UPDATE_REVISIONS"
    PATCH_MODEL_RELEASE_UPDATE_REVISIONS = "RELEASE_UPDATE_REVISIONS"

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
            Allowed values for this property are: "STANDARD", "MISSION_CRITICAL", 'UNKNOWN_ENUM_VALUE'.
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

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousContainerDatabaseSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
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

        :param last_maintenance_run_id:
            The value to assign to the last_maintenance_run_id property of this AutonomousContainerDatabaseSummary.
        :type last_maintenance_run_id: str

        :param next_maintenance_run_id:
            The value to assign to the next_maintenance_run_id property of this AutonomousContainerDatabaseSummary.
        :type next_maintenance_run_id: str

        :param maintenance_window:
            The value to assign to the maintenance_window property of this AutonomousContainerDatabaseSummary.
        :type maintenance_window: MaintenanceWindow

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousContainerDatabaseSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousContainerDatabaseSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param availability_domain:
            The value to assign to the availability_domain property of this AutonomousContainerDatabaseSummary.
        :type availability_domain: str

        :param db_version:
            The value to assign to the db_version property of this AutonomousContainerDatabaseSummary.
        :type db_version: str

        :param backup_config:
            The value to assign to the backup_config property of this AutonomousContainerDatabaseSummary.
        :type backup_config: AutonomousContainerDatabaseBackupConfig

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
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'patch_model': 'str',
            'last_maintenance_run_id': 'str',
            'next_maintenance_run_id': 'str',
            'maintenance_window': 'MaintenanceWindow',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'availability_domain': 'str',
            'db_version': 'str',
            'backup_config': 'AutonomousContainerDatabaseBackupConfig'
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
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'patch_model': 'patchModel',
            'last_maintenance_run_id': 'lastMaintenanceRunId',
            'next_maintenance_run_id': 'nextMaintenanceRunId',
            'maintenance_window': 'maintenanceWindow',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'availability_domain': 'availabilityDomain',
            'db_version': 'dbVersion',
            'backup_config': 'backupConfig'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._db_unique_name = None
        self._service_level_agreement_type = None
        self._autonomous_exadata_infrastructure_id = None
        self._autonomous_vm_cluster_id = None
        self._infrastructure_type = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._patch_model = None
        self._last_maintenance_run_id = None
        self._next_maintenance_run_id = None
        self._maintenance_window = None
        self._freeform_tags = None
        self._defined_tags = None
        self._availability_domain = None
        self._db_version = None
        self._backup_config = None

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
        The `DB_UNIQUE_NAME` of the Oracle Database being backed up.


        :return: The db_unique_name of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this AutonomousContainerDatabaseSummary.
        The `DB_UNIQUE_NAME` of the Oracle Database being backed up.


        :param db_unique_name: The db_unique_name of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def service_level_agreement_type(self):
        """
        **[Required]** Gets the service_level_agreement_type of this AutonomousContainerDatabaseSummary.
        The service level agreement type of the container database. The default is STANDARD.

        Allowed values for this property are: "STANDARD", "MISSION_CRITICAL", 'UNKNOWN_ENUM_VALUE'.
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
        allowed_values = ["STANDARD", "MISSION_CRITICAL"]
        if not value_allowed_none_or_none_sentinel(service_level_agreement_type, allowed_values):
            service_level_agreement_type = 'UNKNOWN_ENUM_VALUE'
        self._service_level_agreement_type = service_level_agreement_type

    @property
    def autonomous_exadata_infrastructure_id(self):
        """
        Gets the autonomous_exadata_infrastructure_id of this AutonomousContainerDatabaseSummary.
        The OCID of the Autonomous Exadata Infrastructure.


        :return: The autonomous_exadata_infrastructure_id of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._autonomous_exadata_infrastructure_id

    @autonomous_exadata_infrastructure_id.setter
    def autonomous_exadata_infrastructure_id(self, autonomous_exadata_infrastructure_id):
        """
        Sets the autonomous_exadata_infrastructure_id of this AutonomousContainerDatabaseSummary.
        The OCID of the Autonomous Exadata Infrastructure.


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
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousContainerDatabaseSummary.
        The current state of the Autonomous Container Database.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
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
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousContainerDatabaseSummary.
        Additional information about the current lifecycleState.


        :return: The lifecycle_details of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousContainerDatabaseSummary.
        Additional information about the current lifecycleState.


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
        :rtype: MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """
        Sets the maintenance_window of this AutonomousContainerDatabaseSummary.

        :param maintenance_window: The maintenance_window of this AutonomousContainerDatabaseSummary.
        :type: MaintenanceWindow
        """
        self._maintenance_window = maintenance_window

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
        Oracle Database version of the Autonomous Container Database


        :return: The db_version of this AutonomousContainerDatabaseSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this AutonomousContainerDatabaseSummary.
        Oracle Database version of the Autonomous Container Database


        :param db_version: The db_version of this AutonomousContainerDatabaseSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def backup_config(self):
        """
        Gets the backup_config of this AutonomousContainerDatabaseSummary.

        :return: The backup_config of this AutonomousContainerDatabaseSummary.
        :rtype: AutonomousContainerDatabaseBackupConfig
        """
        return self._backup_config

    @backup_config.setter
    def backup_config(self, backup_config):
        """
        Sets the backup_config of this AutonomousContainerDatabaseSummary.

        :param backup_config: The backup_config of this AutonomousContainerDatabaseSummary.
        :type: AutonomousContainerDatabaseBackupConfig
        """
        self._backup_config = backup_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
