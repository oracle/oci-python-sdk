# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMigrationDetails(object):
    """
    Update Migration resource parameters.
    """

    #: A constant which can be used with the type property of a UpdateMigrationDetails.
    #: This constant has a value of "ONLINE"
    TYPE_ONLINE = "ONLINE"

    #: A constant which can be used with the type property of a UpdateMigrationDetails.
    #: This constant has a value of "OFFLINE"
    TYPE_OFFLINE = "OFFLINE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMigrationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateMigrationDetails.
            Allowed values for this property are: "ONLINE", "OFFLINE"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateMigrationDetails.
        :type display_name: str

        :param agent_id:
            The value to assign to the agent_id property of this UpdateMigrationDetails.
        :type agent_id: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this UpdateMigrationDetails.
        :type source_database_connection_id: str

        :param source_container_database_connection_id:
            The value to assign to the source_container_database_connection_id property of this UpdateMigrationDetails.
        :type source_container_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this UpdateMigrationDetails.
        :type target_database_connection_id: str

        :param data_transfer_medium_details:
            The value to assign to the data_transfer_medium_details property of this UpdateMigrationDetails.
        :type data_transfer_medium_details: oci.database_migration.models.UpdateDataTransferMediumDetails

        :param dump_transfer_details:
            The value to assign to the dump_transfer_details property of this UpdateMigrationDetails.
        :type dump_transfer_details: oci.database_migration.models.UpdateDumpTransferDetails

        :param datapump_settings:
            The value to assign to the datapump_settings property of this UpdateMigrationDetails.
        :type datapump_settings: oci.database_migration.models.UpdateDataPumpSettings

        :param advisor_settings:
            The value to assign to the advisor_settings property of this UpdateMigrationDetails.
        :type advisor_settings: oci.database_migration.models.UpdateAdvisorSettings

        :param exclude_objects:
            The value to assign to the exclude_objects property of this UpdateMigrationDetails.
        :type exclude_objects: list[oci.database_migration.models.DatabaseObject]

        :param include_objects:
            The value to assign to the include_objects property of this UpdateMigrationDetails.
        :type include_objects: list[oci.database_migration.models.DatabaseObject]

        :param golden_gate_details:
            The value to assign to the golden_gate_details property of this UpdateMigrationDetails.
        :type golden_gate_details: oci.database_migration.models.UpdateGoldenGateDetails

        :param vault_details:
            The value to assign to the vault_details property of this UpdateMigrationDetails.
        :type vault_details: oci.database_migration.models.UpdateVaultDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMigrationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMigrationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'agent_id': 'str',
            'source_database_connection_id': 'str',
            'source_container_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'data_transfer_medium_details': 'UpdateDataTransferMediumDetails',
            'dump_transfer_details': 'UpdateDumpTransferDetails',
            'datapump_settings': 'UpdateDataPumpSettings',
            'advisor_settings': 'UpdateAdvisorSettings',
            'exclude_objects': 'list[DatabaseObject]',
            'include_objects': 'list[DatabaseObject]',
            'golden_gate_details': 'UpdateGoldenGateDetails',
            'vault_details': 'UpdateVaultDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'agent_id': 'agentId',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'source_container_database_connection_id': 'sourceContainerDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'data_transfer_medium_details': 'dataTransferMediumDetails',
            'dump_transfer_details': 'dumpTransferDetails',
            'datapump_settings': 'datapumpSettings',
            'advisor_settings': 'advisorSettings',
            'exclude_objects': 'excludeObjects',
            'include_objects': 'includeObjects',
            'golden_gate_details': 'goldenGateDetails',
            'vault_details': 'vaultDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._type = None
        self._display_name = None
        self._agent_id = None
        self._source_database_connection_id = None
        self._source_container_database_connection_id = None
        self._target_database_connection_id = None
        self._data_transfer_medium_details = None
        self._dump_transfer_details = None
        self._datapump_settings = None
        self._advisor_settings = None
        self._exclude_objects = None
        self._include_objects = None
        self._golden_gate_details = None
        self._vault_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def type(self):
        """
        Gets the type of this UpdateMigrationDetails.
        Migration type.

        Allowed values for this property are: "ONLINE", "OFFLINE"


        :return: The type of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateMigrationDetails.
        Migration type.


        :param type: The type of this UpdateMigrationDetails.
        :type: str
        """
        allowed_values = ["ONLINE", "OFFLINE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMigrationDetails.
        Migration Display Name


        :return: The display_name of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMigrationDetails.
        Migration Display Name


        :param display_name: The display_name of this UpdateMigrationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def agent_id(self):
        """
        Gets the agent_id of this UpdateMigrationDetails.
        The OCID of the registered ODMS Agent.


        :return: The agent_id of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this UpdateMigrationDetails.
        The OCID of the registered ODMS Agent.


        :param agent_id: The agent_id of this UpdateMigrationDetails.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def source_database_connection_id(self):
        """
        Gets the source_database_connection_id of this UpdateMigrationDetails.
        The OCID of the Source Database Connection.


        :return: The source_database_connection_id of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._source_database_connection_id

    @source_database_connection_id.setter
    def source_database_connection_id(self, source_database_connection_id):
        """
        Sets the source_database_connection_id of this UpdateMigrationDetails.
        The OCID of the Source Database Connection.


        :param source_database_connection_id: The source_database_connection_id of this UpdateMigrationDetails.
        :type: str
        """
        self._source_database_connection_id = source_database_connection_id

    @property
    def source_container_database_connection_id(self):
        """
        Gets the source_container_database_connection_id of this UpdateMigrationDetails.
        The OCID of the Source Container Database Connection. Only used for Online migrations.
        Only Connections of type Non-Autonomous can be used as source container databases.
        An empty value would remove the stored Connection ID.


        :return: The source_container_database_connection_id of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._source_container_database_connection_id

    @source_container_database_connection_id.setter
    def source_container_database_connection_id(self, source_container_database_connection_id):
        """
        Sets the source_container_database_connection_id of this UpdateMigrationDetails.
        The OCID of the Source Container Database Connection. Only used for Online migrations.
        Only Connections of type Non-Autonomous can be used as source container databases.
        An empty value would remove the stored Connection ID.


        :param source_container_database_connection_id: The source_container_database_connection_id of this UpdateMigrationDetails.
        :type: str
        """
        self._source_container_database_connection_id = source_container_database_connection_id

    @property
    def target_database_connection_id(self):
        """
        Gets the target_database_connection_id of this UpdateMigrationDetails.
        The OCID of the Target Database Connection.


        :return: The target_database_connection_id of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._target_database_connection_id

    @target_database_connection_id.setter
    def target_database_connection_id(self, target_database_connection_id):
        """
        Sets the target_database_connection_id of this UpdateMigrationDetails.
        The OCID of the Target Database Connection.


        :param target_database_connection_id: The target_database_connection_id of this UpdateMigrationDetails.
        :type: str
        """
        self._target_database_connection_id = target_database_connection_id

    @property
    def data_transfer_medium_details(self):
        """
        Gets the data_transfer_medium_details of this UpdateMigrationDetails.

        :return: The data_transfer_medium_details of this UpdateMigrationDetails.
        :rtype: oci.database_migration.models.UpdateDataTransferMediumDetails
        """
        return self._data_transfer_medium_details

    @data_transfer_medium_details.setter
    def data_transfer_medium_details(self, data_transfer_medium_details):
        """
        Sets the data_transfer_medium_details of this UpdateMigrationDetails.

        :param data_transfer_medium_details: The data_transfer_medium_details of this UpdateMigrationDetails.
        :type: oci.database_migration.models.UpdateDataTransferMediumDetails
        """
        self._data_transfer_medium_details = data_transfer_medium_details

    @property
    def dump_transfer_details(self):
        """
        Gets the dump_transfer_details of this UpdateMigrationDetails.

        :return: The dump_transfer_details of this UpdateMigrationDetails.
        :rtype: oci.database_migration.models.UpdateDumpTransferDetails
        """
        return self._dump_transfer_details

    @dump_transfer_details.setter
    def dump_transfer_details(self, dump_transfer_details):
        """
        Sets the dump_transfer_details of this UpdateMigrationDetails.

        :param dump_transfer_details: The dump_transfer_details of this UpdateMigrationDetails.
        :type: oci.database_migration.models.UpdateDumpTransferDetails
        """
        self._dump_transfer_details = dump_transfer_details

    @property
    def datapump_settings(self):
        """
        Gets the datapump_settings of this UpdateMigrationDetails.

        :return: The datapump_settings of this UpdateMigrationDetails.
        :rtype: oci.database_migration.models.UpdateDataPumpSettings
        """
        return self._datapump_settings

    @datapump_settings.setter
    def datapump_settings(self, datapump_settings):
        """
        Sets the datapump_settings of this UpdateMigrationDetails.

        :param datapump_settings: The datapump_settings of this UpdateMigrationDetails.
        :type: oci.database_migration.models.UpdateDataPumpSettings
        """
        self._datapump_settings = datapump_settings

    @property
    def advisor_settings(self):
        """
        Gets the advisor_settings of this UpdateMigrationDetails.

        :return: The advisor_settings of this UpdateMigrationDetails.
        :rtype: oci.database_migration.models.UpdateAdvisorSettings
        """
        return self._advisor_settings

    @advisor_settings.setter
    def advisor_settings(self, advisor_settings):
        """
        Sets the advisor_settings of this UpdateMigrationDetails.

        :param advisor_settings: The advisor_settings of this UpdateMigrationDetails.
        :type: oci.database_migration.models.UpdateAdvisorSettings
        """
        self._advisor_settings = advisor_settings

    @property
    def exclude_objects(self):
        """
        Gets the exclude_objects of this UpdateMigrationDetails.
        Database objects to exclude from migration, cannot be specified alongside 'includeObjects'.
        If specified, the list will be replaced entirely. Empty list will remove stored excludeObjects details.


        :return: The exclude_objects of this UpdateMigrationDetails.
        :rtype: list[oci.database_migration.models.DatabaseObject]
        """
        return self._exclude_objects

    @exclude_objects.setter
    def exclude_objects(self, exclude_objects):
        """
        Sets the exclude_objects of this UpdateMigrationDetails.
        Database objects to exclude from migration, cannot be specified alongside 'includeObjects'.
        If specified, the list will be replaced entirely. Empty list will remove stored excludeObjects details.


        :param exclude_objects: The exclude_objects of this UpdateMigrationDetails.
        :type: list[oci.database_migration.models.DatabaseObject]
        """
        self._exclude_objects = exclude_objects

    @property
    def include_objects(self):
        """
        Gets the include_objects of this UpdateMigrationDetails.
        Database objects to include from migration, cannot be specified alongside 'excludeObjects'.
        If specified, the list will be replaced entirely. Empty list will remove stored includeObjects details.


        :return: The include_objects of this UpdateMigrationDetails.
        :rtype: list[oci.database_migration.models.DatabaseObject]
        """
        return self._include_objects

    @include_objects.setter
    def include_objects(self, include_objects):
        """
        Sets the include_objects of this UpdateMigrationDetails.
        Database objects to include from migration, cannot be specified alongside 'excludeObjects'.
        If specified, the list will be replaced entirely. Empty list will remove stored includeObjects details.


        :param include_objects: The include_objects of this UpdateMigrationDetails.
        :type: list[oci.database_migration.models.DatabaseObject]
        """
        self._include_objects = include_objects

    @property
    def golden_gate_details(self):
        """
        Gets the golden_gate_details of this UpdateMigrationDetails.

        :return: The golden_gate_details of this UpdateMigrationDetails.
        :rtype: oci.database_migration.models.UpdateGoldenGateDetails
        """
        return self._golden_gate_details

    @golden_gate_details.setter
    def golden_gate_details(self, golden_gate_details):
        """
        Sets the golden_gate_details of this UpdateMigrationDetails.

        :param golden_gate_details: The golden_gate_details of this UpdateMigrationDetails.
        :type: oci.database_migration.models.UpdateGoldenGateDetails
        """
        self._golden_gate_details = golden_gate_details

    @property
    def vault_details(self):
        """
        Gets the vault_details of this UpdateMigrationDetails.

        :return: The vault_details of this UpdateMigrationDetails.
        :rtype: oci.database_migration.models.UpdateVaultDetails
        """
        return self._vault_details

    @vault_details.setter
    def vault_details(self, vault_details):
        """
        Sets the vault_details of this UpdateMigrationDetails.

        :param vault_details: The vault_details of this UpdateMigrationDetails.
        :type: oci.database_migration.models.UpdateVaultDetails
        """
        self._vault_details = vault_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateMigrationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateMigrationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateMigrationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateMigrationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
