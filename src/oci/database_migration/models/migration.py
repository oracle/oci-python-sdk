# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Migration(object):
    """
    Migration resource
    """

    #: A constant which can be used with the type property of a Migration.
    #: This constant has a value of "ONLINE"
    TYPE_ONLINE = "ONLINE"

    #: A constant which can be used with the type property of a Migration.
    #: This constant has a value of "OFFLINE"
    TYPE_OFFLINE = "OFFLINE"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_TGT"
    WAIT_AFTER_ODMS_VALIDATE_TGT = "ODMS_VALIDATE_TGT"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_SRC"
    WAIT_AFTER_ODMS_VALIDATE_SRC = "ODMS_VALIDATE_SRC"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_PREMIGRATION_ADVISOR"
    WAIT_AFTER_ODMS_VALIDATE_PREMIGRATION_ADVISOR = "ODMS_VALIDATE_PREMIGRATION_ADVISOR"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_GG_HUB"
    WAIT_AFTER_ODMS_VALIDATE_GG_HUB = "ODMS_VALIDATE_GG_HUB"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SETTINGS = "ODMS_VALIDATE_DATAPUMP_SETTINGS"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC = "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT = "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SRC"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SRC = "ODMS_VALIDATE_DATAPUMP_SRC"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC = "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE"
    WAIT_AFTER_ODMS_VALIDATE = "ODMS_VALIDATE"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_PREPARE"
    WAIT_AFTER_ODMS_PREPARE = "ODMS_PREPARE"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_INITIAL_LOAD_EXPORT"
    WAIT_AFTER_ODMS_INITIAL_LOAD_EXPORT = "ODMS_INITIAL_LOAD_EXPORT"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_DATA_UPLOAD"
    WAIT_AFTER_ODMS_DATA_UPLOAD = "ODMS_DATA_UPLOAD"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_INITIAL_LOAD_IMPORT"
    WAIT_AFTER_ODMS_INITIAL_LOAD_IMPORT = "ODMS_INITIAL_LOAD_IMPORT"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_POST_INITIAL_LOAD"
    WAIT_AFTER_ODMS_POST_INITIAL_LOAD = "ODMS_POST_INITIAL_LOAD"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_PREPARE_REPLICATION_TARGET"
    WAIT_AFTER_ODMS_PREPARE_REPLICATION_TARGET = "ODMS_PREPARE_REPLICATION_TARGET"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_MONITOR_REPLICATION_LAG"
    WAIT_AFTER_ODMS_MONITOR_REPLICATION_LAG = "ODMS_MONITOR_REPLICATION_LAG"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_SWITCHOVER"
    WAIT_AFTER_ODMS_SWITCHOVER = "ODMS_SWITCHOVER"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_CLEANUP"
    WAIT_AFTER_ODMS_CLEANUP = "ODMS_CLEANUP"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "READY"
    LIFECYCLE_DETAILS_READY = "READY"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "ABORTING"
    LIFECYCLE_DETAILS_ABORTING = "ABORTING"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "VALIDATING"
    LIFECYCLE_DETAILS_VALIDATING = "VALIDATING"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "VALIDATED"
    LIFECYCLE_DETAILS_VALIDATED = "VALIDATED"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "WAITING"
    LIFECYCLE_DETAILS_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "MIGRATING"
    LIFECYCLE_DETAILS_MIGRATING = "MIGRATING"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "DONE"
    LIFECYCLE_DETAILS_DONE = "DONE"

    def __init__(self, **kwargs):
        """
        Initializes a new Migration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Migration.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Migration.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Migration.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this Migration.
            Allowed values for this property are: "ONLINE", "OFFLINE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param wait_after:
            The value to assign to the wait_after property of this Migration.
            Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type wait_after: str

        :param agent_id:
            The value to assign to the agent_id property of this Migration.
        :type agent_id: str

        :param credentials_secret_id:
            The value to assign to the credentials_secret_id property of this Migration.
        :type credentials_secret_id: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this Migration.
        :type source_database_connection_id: str

        :param source_container_database_connection_id:
            The value to assign to the source_container_database_connection_id property of this Migration.
        :type source_container_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this Migration.
        :type target_database_connection_id: str

        :param executing_job_id:
            The value to assign to the executing_job_id property of this Migration.
        :type executing_job_id: str

        :param data_transfer_medium_details:
            The value to assign to the data_transfer_medium_details property of this Migration.
        :type data_transfer_medium_details: oci.database_migration.models.DataTransferMediumDetails

        :param dump_transfer_details:
            The value to assign to the dump_transfer_details property of this Migration.
        :type dump_transfer_details: oci.database_migration.models.DumpTransferDetails

        :param datapump_settings:
            The value to assign to the datapump_settings property of this Migration.
        :type datapump_settings: oci.database_migration.models.DataPumpSettings

        :param advisor_settings:
            The value to assign to the advisor_settings property of this Migration.
        :type advisor_settings: oci.database_migration.models.AdvisorSettings

        :param exclude_objects:
            The value to assign to the exclude_objects property of this Migration.
        :type exclude_objects: list[oci.database_migration.models.DatabaseObject]

        :param include_objects:
            The value to assign to the include_objects property of this Migration.
        :type include_objects: list[oci.database_migration.models.DatabaseObject]

        :param golden_gate_details:
            The value to assign to the golden_gate_details property of this Migration.
        :type golden_gate_details: oci.database_migration.models.GoldenGateDetails

        :param vault_details:
            The value to assign to the vault_details property of this Migration.
        :type vault_details: oci.database_migration.models.VaultDetails

        :param time_created:
            The value to assign to the time_created property of this Migration.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Migration.
        :type time_updated: datetime

        :param time_last_migration:
            The value to assign to the time_last_migration property of this Migration.
        :type time_last_migration: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Migration.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "IN_PROGRESS", "ACCEPTED", "SUCCEEDED", "CANCELED", "WAITING", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Migration.
            Allowed values for this property are: "READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Migration.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Migration.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Migration.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'wait_after': 'str',
            'agent_id': 'str',
            'credentials_secret_id': 'str',
            'source_database_connection_id': 'str',
            'source_container_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'executing_job_id': 'str',
            'data_transfer_medium_details': 'DataTransferMediumDetails',
            'dump_transfer_details': 'DumpTransferDetails',
            'datapump_settings': 'DataPumpSettings',
            'advisor_settings': 'AdvisorSettings',
            'exclude_objects': 'list[DatabaseObject]',
            'include_objects': 'list[DatabaseObject]',
            'golden_gate_details': 'GoldenGateDetails',
            'vault_details': 'VaultDetails',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_migration': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'wait_after': 'waitAfter',
            'agent_id': 'agentId',
            'credentials_secret_id': 'credentialsSecretId',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'source_container_database_connection_id': 'sourceContainerDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'executing_job_id': 'executingJobId',
            'data_transfer_medium_details': 'dataTransferMediumDetails',
            'dump_transfer_details': 'dumpTransferDetails',
            'datapump_settings': 'datapumpSettings',
            'advisor_settings': 'advisorSettings',
            'exclude_objects': 'excludeObjects',
            'include_objects': 'includeObjects',
            'golden_gate_details': 'goldenGateDetails',
            'vault_details': 'vaultDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_migration': 'timeLastMigration',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._wait_after = None
        self._agent_id = None
        self._credentials_secret_id = None
        self._source_database_connection_id = None
        self._source_container_database_connection_id = None
        self._target_database_connection_id = None
        self._executing_job_id = None
        self._data_transfer_medium_details = None
        self._dump_transfer_details = None
        self._datapump_settings = None
        self._advisor_settings = None
        self._exclude_objects = None
        self._include_objects = None
        self._golden_gate_details = None
        self._vault_details = None
        self._time_created = None
        self._time_updated = None
        self._time_last_migration = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Migration.
        The OCID of the resource


        :return: The id of this Migration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Migration.
        The OCID of the resource


        :param id: The id of this Migration.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Migration.
        Migration Display Name


        :return: The display_name of this Migration.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Migration.
        Migration Display Name


        :param display_name: The display_name of this Migration.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Migration.
        OCID of the compartment


        :return: The compartment_id of this Migration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Migration.
        OCID of the compartment


        :param compartment_id: The compartment_id of this Migration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Migration.
        Migration type.

        Allowed values for this property are: "ONLINE", "OFFLINE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Migration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Migration.
        Migration type.


        :param type: The type of this Migration.
        :type: str
        """
        allowed_values = ["ONLINE", "OFFLINE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def wait_after(self):
        """
        Gets the wait_after of this Migration.
        Name of a migration phase. The Job will wait after executing this
        phase until the Resume Job endpoint is called.

        Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The wait_after of this Migration.
        :rtype: str
        """
        return self._wait_after

    @wait_after.setter
    def wait_after(self, wait_after):
        """
        Sets the wait_after of this Migration.
        Name of a migration phase. The Job will wait after executing this
        phase until the Resume Job endpoint is called.


        :param wait_after: The wait_after of this Migration.
        :type: str
        """
        allowed_values = ["ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"]
        if not value_allowed_none_or_none_sentinel(wait_after, allowed_values):
            wait_after = 'UNKNOWN_ENUM_VALUE'
        self._wait_after = wait_after

    @property
    def agent_id(self):
        """
        Gets the agent_id of this Migration.
        The OCID of the registered on-premises ODMS Agent. Only valid for Offline Migrations.


        :return: The agent_id of this Migration.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this Migration.
        The OCID of the registered on-premises ODMS Agent. Only valid for Offline Migrations.


        :param agent_id: The agent_id of this Migration.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def credentials_secret_id(self):
        """
        Gets the credentials_secret_id of this Migration.
        OCID of the Secret in the OCI vault containing the Migration credentials. Used to store GoldenGate administrator user credentials.


        :return: The credentials_secret_id of this Migration.
        :rtype: str
        """
        return self._credentials_secret_id

    @credentials_secret_id.setter
    def credentials_secret_id(self, credentials_secret_id):
        """
        Sets the credentials_secret_id of this Migration.
        OCID of the Secret in the OCI vault containing the Migration credentials. Used to store GoldenGate administrator user credentials.


        :param credentials_secret_id: The credentials_secret_id of this Migration.
        :type: str
        """
        self._credentials_secret_id = credentials_secret_id

    @property
    def source_database_connection_id(self):
        """
        **[Required]** Gets the source_database_connection_id of this Migration.
        The OCID of the Source Database Connection.


        :return: The source_database_connection_id of this Migration.
        :rtype: str
        """
        return self._source_database_connection_id

    @source_database_connection_id.setter
    def source_database_connection_id(self, source_database_connection_id):
        """
        Sets the source_database_connection_id of this Migration.
        The OCID of the Source Database Connection.


        :param source_database_connection_id: The source_database_connection_id of this Migration.
        :type: str
        """
        self._source_database_connection_id = source_database_connection_id

    @property
    def source_container_database_connection_id(self):
        """
        Gets the source_container_database_connection_id of this Migration.
        The OCID of the Source Container Database Connection.


        :return: The source_container_database_connection_id of this Migration.
        :rtype: str
        """
        return self._source_container_database_connection_id

    @source_container_database_connection_id.setter
    def source_container_database_connection_id(self, source_container_database_connection_id):
        """
        Sets the source_container_database_connection_id of this Migration.
        The OCID of the Source Container Database Connection.


        :param source_container_database_connection_id: The source_container_database_connection_id of this Migration.
        :type: str
        """
        self._source_container_database_connection_id = source_container_database_connection_id

    @property
    def target_database_connection_id(self):
        """
        **[Required]** Gets the target_database_connection_id of this Migration.
        The OCID of the Target Database Connection.


        :return: The target_database_connection_id of this Migration.
        :rtype: str
        """
        return self._target_database_connection_id

    @target_database_connection_id.setter
    def target_database_connection_id(self, target_database_connection_id):
        """
        Sets the target_database_connection_id of this Migration.
        The OCID of the Target Database Connection.


        :param target_database_connection_id: The target_database_connection_id of this Migration.
        :type: str
        """
        self._target_database_connection_id = target_database_connection_id

    @property
    def executing_job_id(self):
        """
        Gets the executing_job_id of this Migration.
        OCID of the current ODMS Job in execution for the Migration, if any.


        :return: The executing_job_id of this Migration.
        :rtype: str
        """
        return self._executing_job_id

    @executing_job_id.setter
    def executing_job_id(self, executing_job_id):
        """
        Sets the executing_job_id of this Migration.
        OCID of the current ODMS Job in execution for the Migration, if any.


        :param executing_job_id: The executing_job_id of this Migration.
        :type: str
        """
        self._executing_job_id = executing_job_id

    @property
    def data_transfer_medium_details(self):
        """
        Gets the data_transfer_medium_details of this Migration.

        :return: The data_transfer_medium_details of this Migration.
        :rtype: oci.database_migration.models.DataTransferMediumDetails
        """
        return self._data_transfer_medium_details

    @data_transfer_medium_details.setter
    def data_transfer_medium_details(self, data_transfer_medium_details):
        """
        Sets the data_transfer_medium_details of this Migration.

        :param data_transfer_medium_details: The data_transfer_medium_details of this Migration.
        :type: oci.database_migration.models.DataTransferMediumDetails
        """
        self._data_transfer_medium_details = data_transfer_medium_details

    @property
    def dump_transfer_details(self):
        """
        Gets the dump_transfer_details of this Migration.

        :return: The dump_transfer_details of this Migration.
        :rtype: oci.database_migration.models.DumpTransferDetails
        """
        return self._dump_transfer_details

    @dump_transfer_details.setter
    def dump_transfer_details(self, dump_transfer_details):
        """
        Sets the dump_transfer_details of this Migration.

        :param dump_transfer_details: The dump_transfer_details of this Migration.
        :type: oci.database_migration.models.DumpTransferDetails
        """
        self._dump_transfer_details = dump_transfer_details

    @property
    def datapump_settings(self):
        """
        Gets the datapump_settings of this Migration.

        :return: The datapump_settings of this Migration.
        :rtype: oci.database_migration.models.DataPumpSettings
        """
        return self._datapump_settings

    @datapump_settings.setter
    def datapump_settings(self, datapump_settings):
        """
        Sets the datapump_settings of this Migration.

        :param datapump_settings: The datapump_settings of this Migration.
        :type: oci.database_migration.models.DataPumpSettings
        """
        self._datapump_settings = datapump_settings

    @property
    def advisor_settings(self):
        """
        Gets the advisor_settings of this Migration.

        :return: The advisor_settings of this Migration.
        :rtype: oci.database_migration.models.AdvisorSettings
        """
        return self._advisor_settings

    @advisor_settings.setter
    def advisor_settings(self, advisor_settings):
        """
        Sets the advisor_settings of this Migration.

        :param advisor_settings: The advisor_settings of this Migration.
        :type: oci.database_migration.models.AdvisorSettings
        """
        self._advisor_settings = advisor_settings

    @property
    def exclude_objects(self):
        """
        Gets the exclude_objects of this Migration.
        Database objects to exclude from migration.
        If 'includeObjects' are specified, only exclude object types can be specified with general wildcards (.*) for owner and objectName.


        :return: The exclude_objects of this Migration.
        :rtype: list[oci.database_migration.models.DatabaseObject]
        """
        return self._exclude_objects

    @exclude_objects.setter
    def exclude_objects(self, exclude_objects):
        """
        Sets the exclude_objects of this Migration.
        Database objects to exclude from migration.
        If 'includeObjects' are specified, only exclude object types can be specified with general wildcards (.*) for owner and objectName.


        :param exclude_objects: The exclude_objects of this Migration.
        :type: list[oci.database_migration.models.DatabaseObject]
        """
        self._exclude_objects = exclude_objects

    @property
    def include_objects(self):
        """
        Gets the include_objects of this Migration.
        Database objects to include from migration.


        :return: The include_objects of this Migration.
        :rtype: list[oci.database_migration.models.DatabaseObject]
        """
        return self._include_objects

    @include_objects.setter
    def include_objects(self, include_objects):
        """
        Sets the include_objects of this Migration.
        Database objects to include from migration.


        :param include_objects: The include_objects of this Migration.
        :type: list[oci.database_migration.models.DatabaseObject]
        """
        self._include_objects = include_objects

    @property
    def golden_gate_details(self):
        """
        Gets the golden_gate_details of this Migration.

        :return: The golden_gate_details of this Migration.
        :rtype: oci.database_migration.models.GoldenGateDetails
        """
        return self._golden_gate_details

    @golden_gate_details.setter
    def golden_gate_details(self, golden_gate_details):
        """
        Sets the golden_gate_details of this Migration.

        :param golden_gate_details: The golden_gate_details of this Migration.
        :type: oci.database_migration.models.GoldenGateDetails
        """
        self._golden_gate_details = golden_gate_details

    @property
    def vault_details(self):
        """
        Gets the vault_details of this Migration.

        :return: The vault_details of this Migration.
        :rtype: oci.database_migration.models.VaultDetails
        """
        return self._vault_details

    @vault_details.setter
    def vault_details(self, vault_details):
        """
        Sets the vault_details of this Migration.

        :param vault_details: The vault_details of this Migration.
        :type: oci.database_migration.models.VaultDetails
        """
        self._vault_details = vault_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Migration.
        The time the Migration was created. An RFC3339 formatted datetime string.


        :return: The time_created of this Migration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Migration.
        The time the Migration was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this Migration.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Migration.
        The time of the last Migration details update. An RFC3339 formatted datetime string.


        :return: The time_updated of this Migration.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Migration.
        The time of the last Migration details update. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this Migration.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_migration(self):
        """
        Gets the time_last_migration of this Migration.
        The time of last Migration. An RFC3339 formatted datetime string.


        :return: The time_last_migration of this Migration.
        :rtype: datetime
        """
        return self._time_last_migration

    @time_last_migration.setter
    def time_last_migration(self, time_last_migration):
        """
        Sets the time_last_migration of this Migration.
        The time of last Migration. An RFC3339 formatted datetime string.


        :param time_last_migration: The time_last_migration of this Migration.
        :type: datetime
        """
        self._time_last_migration = time_last_migration

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Migration.
        The current state of the Migration resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "IN_PROGRESS", "ACCEPTED", "SUCCEEDED", "CANCELED", "WAITING", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Migration.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Migration.
        The current state of the Migration resource.


        :param lifecycle_state: The lifecycle_state of this Migration.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "IN_PROGRESS", "ACCEPTED", "SUCCEEDED", "CANCELED", "WAITING", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Migration.
        Additional status related to the execution and current state of the Migration.

        Allowed values for this property are: "READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this Migration.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Migration.
        Additional status related to the execution and current state of the Migration.


        :param lifecycle_details: The lifecycle_details of this Migration.
        :type: str
        """
        allowed_values = ["READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Migration.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Migration.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Migration.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Migration.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Migration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Migration.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Migration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Migration.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Migration.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Migration.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Migration.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Migration.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
