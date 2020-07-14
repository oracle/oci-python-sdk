# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousContainerDatabaseDetails(object):
    """
    Describes the required parameters for the creation of an Autonomous Container Database.
    """

    #: A constant which can be used with the service_level_agreement_type property of a CreateAutonomousContainerDatabaseDetails.
    #: This constant has a value of "STANDARD"
    SERVICE_LEVEL_AGREEMENT_TYPE_STANDARD = "STANDARD"

    #: A constant which can be used with the patch_model property of a CreateAutonomousContainerDatabaseDetails.
    #: This constant has a value of "RELEASE_UPDATES"
    PATCH_MODEL_RELEASE_UPDATES = "RELEASE_UPDATES"

    #: A constant which can be used with the patch_model property of a CreateAutonomousContainerDatabaseDetails.
    #: This constant has a value of "RELEASE_UPDATE_REVISIONS"
    PATCH_MODEL_RELEASE_UPDATE_REVISIONS = "RELEASE_UPDATE_REVISIONS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousContainerDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousContainerDatabaseDetails.
        :type display_name: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this CreateAutonomousContainerDatabaseDetails.
        :type db_unique_name: str

        :param service_level_agreement_type:
            The value to assign to the service_level_agreement_type property of this CreateAutonomousContainerDatabaseDetails.
            Allowed values for this property are: "STANDARD"
        :type service_level_agreement_type: str

        :param autonomous_exadata_infrastructure_id:
            The value to assign to the autonomous_exadata_infrastructure_id property of this CreateAutonomousContainerDatabaseDetails.
        :type autonomous_exadata_infrastructure_id: str

        :param autonomous_vm_cluster_id:
            The value to assign to the autonomous_vm_cluster_id property of this CreateAutonomousContainerDatabaseDetails.
        :type autonomous_vm_cluster_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutonomousContainerDatabaseDetails.
        :type compartment_id: str

        :param patch_model:
            The value to assign to the patch_model property of this CreateAutonomousContainerDatabaseDetails.
            Allowed values for this property are: "RELEASE_UPDATES", "RELEASE_UPDATE_REVISIONS"
        :type patch_model: str

        :param maintenance_window_details:
            The value to assign to the maintenance_window_details property of this CreateAutonomousContainerDatabaseDetails.
        :type maintenance_window_details: MaintenanceWindow

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousContainerDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousContainerDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param backup_config:
            The value to assign to the backup_config property of this CreateAutonomousContainerDatabaseDetails.
        :type backup_config: AutonomousContainerDatabaseBackupConfig

        """
        self.swagger_types = {
            'display_name': 'str',
            'db_unique_name': 'str',
            'service_level_agreement_type': 'str',
            'autonomous_exadata_infrastructure_id': 'str',
            'autonomous_vm_cluster_id': 'str',
            'compartment_id': 'str',
            'patch_model': 'str',
            'maintenance_window_details': 'MaintenanceWindow',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'backup_config': 'AutonomousContainerDatabaseBackupConfig'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'db_unique_name': 'dbUniqueName',
            'service_level_agreement_type': 'serviceLevelAgreementType',
            'autonomous_exadata_infrastructure_id': 'autonomousExadataInfrastructureId',
            'autonomous_vm_cluster_id': 'autonomousVmClusterId',
            'compartment_id': 'compartmentId',
            'patch_model': 'patchModel',
            'maintenance_window_details': 'maintenanceWindowDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'backup_config': 'backupConfig'
        }

        self._display_name = None
        self._db_unique_name = None
        self._service_level_agreement_type = None
        self._autonomous_exadata_infrastructure_id = None
        self._autonomous_vm_cluster_id = None
        self._compartment_id = None
        self._patch_model = None
        self._maintenance_window_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._backup_config = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateAutonomousContainerDatabaseDetails.
        The display name for the Autonomous Container Database.


        :return: The display_name of this CreateAutonomousContainerDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutonomousContainerDatabaseDetails.
        The display name for the Autonomous Container Database.


        :param display_name: The display_name of this CreateAutonomousContainerDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def db_unique_name(self):
        """
        Gets the db_unique_name of this CreateAutonomousContainerDatabaseDetails.
        The `DB_UNIQUE_NAME` of the Oracle Database being backed up.


        :return: The db_unique_name of this CreateAutonomousContainerDatabaseDetails.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this CreateAutonomousContainerDatabaseDetails.
        The `DB_UNIQUE_NAME` of the Oracle Database being backed up.


        :param db_unique_name: The db_unique_name of this CreateAutonomousContainerDatabaseDetails.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def service_level_agreement_type(self):
        """
        Gets the service_level_agreement_type of this CreateAutonomousContainerDatabaseDetails.
        The service level agreement type of the Autonomous Container Database. The default is STANDARD. For an autonomous dataguard Autonomous Container Database, the specified Autonomous Exadata Infrastructure must be associated with a remote Autonomous Exadata Infrastructure.

        Allowed values for this property are: "STANDARD"


        :return: The service_level_agreement_type of this CreateAutonomousContainerDatabaseDetails.
        :rtype: str
        """
        return self._service_level_agreement_type

    @service_level_agreement_type.setter
    def service_level_agreement_type(self, service_level_agreement_type):
        """
        Sets the service_level_agreement_type of this CreateAutonomousContainerDatabaseDetails.
        The service level agreement type of the Autonomous Container Database. The default is STANDARD. For an autonomous dataguard Autonomous Container Database, the specified Autonomous Exadata Infrastructure must be associated with a remote Autonomous Exadata Infrastructure.


        :param service_level_agreement_type: The service_level_agreement_type of this CreateAutonomousContainerDatabaseDetails.
        :type: str
        """
        allowed_values = ["STANDARD"]
        if not value_allowed_none_or_none_sentinel(service_level_agreement_type, allowed_values):
            raise ValueError(
                "Invalid value for `service_level_agreement_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._service_level_agreement_type = service_level_agreement_type

    @property
    def autonomous_exadata_infrastructure_id(self):
        """
        Gets the autonomous_exadata_infrastructure_id of this CreateAutonomousContainerDatabaseDetails.
        The OCID of the Autonomous Exadata Infrastructure.


        :return: The autonomous_exadata_infrastructure_id of this CreateAutonomousContainerDatabaseDetails.
        :rtype: str
        """
        return self._autonomous_exadata_infrastructure_id

    @autonomous_exadata_infrastructure_id.setter
    def autonomous_exadata_infrastructure_id(self, autonomous_exadata_infrastructure_id):
        """
        Sets the autonomous_exadata_infrastructure_id of this CreateAutonomousContainerDatabaseDetails.
        The OCID of the Autonomous Exadata Infrastructure.


        :param autonomous_exadata_infrastructure_id: The autonomous_exadata_infrastructure_id of this CreateAutonomousContainerDatabaseDetails.
        :type: str
        """
        self._autonomous_exadata_infrastructure_id = autonomous_exadata_infrastructure_id

    @property
    def autonomous_vm_cluster_id(self):
        """
        Gets the autonomous_vm_cluster_id of this CreateAutonomousContainerDatabaseDetails.
        The OCID of the Autonomous VM Cluster.


        :return: The autonomous_vm_cluster_id of this CreateAutonomousContainerDatabaseDetails.
        :rtype: str
        """
        return self._autonomous_vm_cluster_id

    @autonomous_vm_cluster_id.setter
    def autonomous_vm_cluster_id(self, autonomous_vm_cluster_id):
        """
        Sets the autonomous_vm_cluster_id of this CreateAutonomousContainerDatabaseDetails.
        The OCID of the Autonomous VM Cluster.


        :param autonomous_vm_cluster_id: The autonomous_vm_cluster_id of this CreateAutonomousContainerDatabaseDetails.
        :type: str
        """
        self._autonomous_vm_cluster_id = autonomous_vm_cluster_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateAutonomousContainerDatabaseDetails.
        The `OCID`__ of the compartment containing the Autonomous Container Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAutonomousContainerDatabaseDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAutonomousContainerDatabaseDetails.
        The `OCID`__ of the compartment containing the Autonomous Container Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAutonomousContainerDatabaseDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def patch_model(self):
        """
        **[Required]** Gets the patch_model of this CreateAutonomousContainerDatabaseDetails.
        Database Patch model preference.

        Allowed values for this property are: "RELEASE_UPDATES", "RELEASE_UPDATE_REVISIONS"


        :return: The patch_model of this CreateAutonomousContainerDatabaseDetails.
        :rtype: str
        """
        return self._patch_model

    @patch_model.setter
    def patch_model(self, patch_model):
        """
        Sets the patch_model of this CreateAutonomousContainerDatabaseDetails.
        Database Patch model preference.


        :param patch_model: The patch_model of this CreateAutonomousContainerDatabaseDetails.
        :type: str
        """
        allowed_values = ["RELEASE_UPDATES", "RELEASE_UPDATE_REVISIONS"]
        if not value_allowed_none_or_none_sentinel(patch_model, allowed_values):
            raise ValueError(
                "Invalid value for `patch_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._patch_model = patch_model

    @property
    def maintenance_window_details(self):
        """
        Gets the maintenance_window_details of this CreateAutonomousContainerDatabaseDetails.

        :return: The maintenance_window_details of this CreateAutonomousContainerDatabaseDetails.
        :rtype: MaintenanceWindow
        """
        return self._maintenance_window_details

    @maintenance_window_details.setter
    def maintenance_window_details(self, maintenance_window_details):
        """
        Sets the maintenance_window_details of this CreateAutonomousContainerDatabaseDetails.

        :param maintenance_window_details: The maintenance_window_details of this CreateAutonomousContainerDatabaseDetails.
        :type: MaintenanceWindow
        """
        self._maintenance_window_details = maintenance_window_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAutonomousContainerDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAutonomousContainerDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAutonomousContainerDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAutonomousContainerDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAutonomousContainerDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAutonomousContainerDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAutonomousContainerDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAutonomousContainerDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def backup_config(self):
        """
        Gets the backup_config of this CreateAutonomousContainerDatabaseDetails.

        :return: The backup_config of this CreateAutonomousContainerDatabaseDetails.
        :rtype: AutonomousContainerDatabaseBackupConfig
        """
        return self._backup_config

    @backup_config.setter
    def backup_config(self, backup_config):
        """
        Sets the backup_config of this CreateAutonomousContainerDatabaseDetails.

        :param backup_config: The backup_config of this CreateAutonomousContainerDatabaseDetails.
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
