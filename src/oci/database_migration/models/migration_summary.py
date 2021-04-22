# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationSummary(object):
    """
    Migration resource
    """

    #: A constant which can be used with the type property of a MigrationSummary.
    #: This constant has a value of "ONLINE"
    TYPE_ONLINE = "ONLINE"

    #: A constant which can be used with the type property of a MigrationSummary.
    #: This constant has a value of "OFFLINE"
    TYPE_OFFLINE = "OFFLINE"

    #: A constant which can be used with the lifecycle_state property of a MigrationSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MigrationSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MigrationSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MigrationSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MigrationSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MigrationSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MigrationSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_details property of a MigrationSummary.
    #: This constant has a value of "READY"
    LIFECYCLE_DETAILS_READY = "READY"

    #: A constant which can be used with the lifecycle_details property of a MigrationSummary.
    #: This constant has a value of "ABORTING"
    LIFECYCLE_DETAILS_ABORTING = "ABORTING"

    #: A constant which can be used with the lifecycle_details property of a MigrationSummary.
    #: This constant has a value of "VALIDATING"
    LIFECYCLE_DETAILS_VALIDATING = "VALIDATING"

    #: A constant which can be used with the lifecycle_details property of a MigrationSummary.
    #: This constant has a value of "VALIDATED"
    LIFECYCLE_DETAILS_VALIDATED = "VALIDATED"

    #: A constant which can be used with the lifecycle_details property of a MigrationSummary.
    #: This constant has a value of "WAITING"
    LIFECYCLE_DETAILS_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_details property of a MigrationSummary.
    #: This constant has a value of "MIGRATING"
    LIFECYCLE_DETAILS_MIGRATING = "MIGRATING"

    #: A constant which can be used with the lifecycle_details property of a MigrationSummary.
    #: This constant has a value of "DONE"
    LIFECYCLE_DETAILS_DONE = "DONE"

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MigrationSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this MigrationSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MigrationSummary.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this MigrationSummary.
            Allowed values for this property are: "ONLINE", "OFFLINE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this MigrationSummary.
        :type source_database_connection_id: str

        :param source_container_database_connection_id:
            The value to assign to the source_container_database_connection_id property of this MigrationSummary.
        :type source_container_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this MigrationSummary.
        :type target_database_connection_id: str

        :param executing_job_id:
            The value to assign to the executing_job_id property of this MigrationSummary.
        :type executing_job_id: str

        :param agent_id:
            The value to assign to the agent_id property of this MigrationSummary.
        :type agent_id: str

        :param vault_details:
            The value to assign to the vault_details property of this MigrationSummary.
        :type vault_details: oci.database_migration.models.VaultDetails

        :param time_created:
            The value to assign to the time_created property of this MigrationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MigrationSummary.
        :type time_updated: datetime

        :param time_last_migration:
            The value to assign to the time_last_migration property of this MigrationSummary.
        :type time_last_migration: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MigrationSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MigrationSummary.
            Allowed values for this property are: "READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MigrationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MigrationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MigrationSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'source_database_connection_id': 'str',
            'source_container_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'executing_job_id': 'str',
            'agent_id': 'str',
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
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'source_container_database_connection_id': 'sourceContainerDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'executing_job_id': 'executingJobId',
            'agent_id': 'agentId',
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
        self._source_database_connection_id = None
        self._source_container_database_connection_id = None
        self._target_database_connection_id = None
        self._executing_job_id = None
        self._agent_id = None
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
        **[Required]** Gets the id of this MigrationSummary.
        The OCID of the resource


        :return: The id of this MigrationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MigrationSummary.
        The OCID of the resource


        :param id: The id of this MigrationSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MigrationSummary.
        Migration Display Name


        :return: The display_name of this MigrationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MigrationSummary.
        Migration Display Name


        :param display_name: The display_name of this MigrationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MigrationSummary.
        OCID of the compartment


        :return: The compartment_id of this MigrationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MigrationSummary.
        OCID of the compartment


        :param compartment_id: The compartment_id of this MigrationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MigrationSummary.
        Migration type.

        Allowed values for this property are: "ONLINE", "OFFLINE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this MigrationSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MigrationSummary.
        Migration type.


        :param type: The type of this MigrationSummary.
        :type: str
        """
        allowed_values = ["ONLINE", "OFFLINE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def source_database_connection_id(self):
        """
        **[Required]** Gets the source_database_connection_id of this MigrationSummary.
        The OCID of the Source Database Connection.


        :return: The source_database_connection_id of this MigrationSummary.
        :rtype: str
        """
        return self._source_database_connection_id

    @source_database_connection_id.setter
    def source_database_connection_id(self, source_database_connection_id):
        """
        Sets the source_database_connection_id of this MigrationSummary.
        The OCID of the Source Database Connection.


        :param source_database_connection_id: The source_database_connection_id of this MigrationSummary.
        :type: str
        """
        self._source_database_connection_id = source_database_connection_id

    @property
    def source_container_database_connection_id(self):
        """
        Gets the source_container_database_connection_id of this MigrationSummary.
        The OCID of the Source Container Database Connection.


        :return: The source_container_database_connection_id of this MigrationSummary.
        :rtype: str
        """
        return self._source_container_database_connection_id

    @source_container_database_connection_id.setter
    def source_container_database_connection_id(self, source_container_database_connection_id):
        """
        Sets the source_container_database_connection_id of this MigrationSummary.
        The OCID of the Source Container Database Connection.


        :param source_container_database_connection_id: The source_container_database_connection_id of this MigrationSummary.
        :type: str
        """
        self._source_container_database_connection_id = source_container_database_connection_id

    @property
    def target_database_connection_id(self):
        """
        **[Required]** Gets the target_database_connection_id of this MigrationSummary.
        The OCID of the Target Database Connection.


        :return: The target_database_connection_id of this MigrationSummary.
        :rtype: str
        """
        return self._target_database_connection_id

    @target_database_connection_id.setter
    def target_database_connection_id(self, target_database_connection_id):
        """
        Sets the target_database_connection_id of this MigrationSummary.
        The OCID of the Target Database Connection.


        :param target_database_connection_id: The target_database_connection_id of this MigrationSummary.
        :type: str
        """
        self._target_database_connection_id = target_database_connection_id

    @property
    def executing_job_id(self):
        """
        Gets the executing_job_id of this MigrationSummary.
        OCID of the current ODMS Job in execution for the Migration, if any.


        :return: The executing_job_id of this MigrationSummary.
        :rtype: str
        """
        return self._executing_job_id

    @executing_job_id.setter
    def executing_job_id(self, executing_job_id):
        """
        Sets the executing_job_id of this MigrationSummary.
        OCID of the current ODMS Job in execution for the Migration, if any.


        :param executing_job_id: The executing_job_id of this MigrationSummary.
        :type: str
        """
        self._executing_job_id = executing_job_id

    @property
    def agent_id(self):
        """
        Gets the agent_id of this MigrationSummary.
        The OCID of the registered on-premises ODMS Agent. Only valid for Offline Migrations.


        :return: The agent_id of this MigrationSummary.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this MigrationSummary.
        The OCID of the registered on-premises ODMS Agent. Only valid for Offline Migrations.


        :param agent_id: The agent_id of this MigrationSummary.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def vault_details(self):
        """
        Gets the vault_details of this MigrationSummary.

        :return: The vault_details of this MigrationSummary.
        :rtype: oci.database_migration.models.VaultDetails
        """
        return self._vault_details

    @vault_details.setter
    def vault_details(self, vault_details):
        """
        Sets the vault_details of this MigrationSummary.

        :param vault_details: The vault_details of this MigrationSummary.
        :type: oci.database_migration.models.VaultDetails
        """
        self._vault_details = vault_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MigrationSummary.
        The time the Migration was created. An RFC3339 formatted datetime string.


        :return: The time_created of this MigrationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MigrationSummary.
        The time the Migration was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this MigrationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MigrationSummary.
        The time of the last Migration details update. An RFC3339 formatted datetime string.


        :return: The time_updated of this MigrationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MigrationSummary.
        The time of the last Migration details update. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MigrationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_migration(self):
        """
        Gets the time_last_migration of this MigrationSummary.
        The time of last Migration. An RFC3339 formatted datetime string.


        :return: The time_last_migration of this MigrationSummary.
        :rtype: datetime
        """
        return self._time_last_migration

    @time_last_migration.setter
    def time_last_migration(self, time_last_migration):
        """
        Sets the time_last_migration of this MigrationSummary.
        The time of last Migration. An RFC3339 formatted datetime string.


        :param time_last_migration: The time_last_migration of this MigrationSummary.
        :type: datetime
        """
        self._time_last_migration = time_last_migration

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MigrationSummary.
        The current state of the Migration.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MigrationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MigrationSummary.
        The current state of the Migration.


        :param lifecycle_state: The lifecycle_state of this MigrationSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MigrationSummary.
        Additional status related to the execution and current state of the Migration.

        Allowed values for this property are: "READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this MigrationSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MigrationSummary.
        Additional status related to the execution and current state of the Migration.


        :param lifecycle_details: The lifecycle_details of this MigrationSummary.
        :type: str
        """
        allowed_values = ["READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MigrationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MigrationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MigrationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MigrationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MigrationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MigrationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MigrationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MigrationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MigrationSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MigrationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MigrationSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MigrationSummary.
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
