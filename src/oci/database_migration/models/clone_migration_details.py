# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloneMigrationDetails(object):
    """
    Details that will override an existing Migration configuration that will be cloned.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloneMigrationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CloneMigrationDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CloneMigrationDetails.
        :type compartment_id: str

        :param agent_id:
            The value to assign to the agent_id property of this CloneMigrationDetails.
        :type agent_id: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this CloneMigrationDetails.
        :type source_database_connection_id: str

        :param source_container_database_connection_id:
            The value to assign to the source_container_database_connection_id property of this CloneMigrationDetails.
        :type source_container_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this CloneMigrationDetails.
        :type target_database_connection_id: str

        :param exclude_objects:
            The value to assign to the exclude_objects property of this CloneMigrationDetails.
        :type exclude_objects: list[oci.database_migration.models.DatabaseObject]

        :param vault_details:
            The value to assign to the vault_details property of this CloneMigrationDetails.
        :type vault_details: oci.database_migration.models.CreateVaultDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CloneMigrationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CloneMigrationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'agent_id': 'str',
            'source_database_connection_id': 'str',
            'source_container_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'exclude_objects': 'list[DatabaseObject]',
            'vault_details': 'CreateVaultDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'agent_id': 'agentId',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'source_container_database_connection_id': 'sourceContainerDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'exclude_objects': 'excludeObjects',
            'vault_details': 'vaultDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._agent_id = None
        self._source_database_connection_id = None
        self._source_container_database_connection_id = None
        self._target_database_connection_id = None
        self._exclude_objects = None
        self._vault_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CloneMigrationDetails.
        Migration Display Name


        :return: The display_name of this CloneMigrationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CloneMigrationDetails.
        Migration Display Name


        :param display_name: The display_name of this CloneMigrationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CloneMigrationDetails.
        OCID of the compartment


        :return: The compartment_id of this CloneMigrationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CloneMigrationDetails.
        OCID of the compartment


        :param compartment_id: The compartment_id of this CloneMigrationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def agent_id(self):
        """
        Gets the agent_id of this CloneMigrationDetails.
        The OCID of the registered on-premises ODMS Agent. Only valid for Offline Logical Migrations.


        :return: The agent_id of this CloneMigrationDetails.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this CloneMigrationDetails.
        The OCID of the registered on-premises ODMS Agent. Only valid for Offline Logical Migrations.


        :param agent_id: The agent_id of this CloneMigrationDetails.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def source_database_connection_id(self):
        """
        **[Required]** Gets the source_database_connection_id of this CloneMigrationDetails.
        The OCID of the Source Database Connection.


        :return: The source_database_connection_id of this CloneMigrationDetails.
        :rtype: str
        """
        return self._source_database_connection_id

    @source_database_connection_id.setter
    def source_database_connection_id(self, source_database_connection_id):
        """
        Sets the source_database_connection_id of this CloneMigrationDetails.
        The OCID of the Source Database Connection.


        :param source_database_connection_id: The source_database_connection_id of this CloneMigrationDetails.
        :type: str
        """
        self._source_database_connection_id = source_database_connection_id

    @property
    def source_container_database_connection_id(self):
        """
        Gets the source_container_database_connection_id of this CloneMigrationDetails.
        The OCID of the Source Container Database Connection. Only used for Online migrations.
        Only Connections of type Non-Autonomous can be used as source container databases.


        :return: The source_container_database_connection_id of this CloneMigrationDetails.
        :rtype: str
        """
        return self._source_container_database_connection_id

    @source_container_database_connection_id.setter
    def source_container_database_connection_id(self, source_container_database_connection_id):
        """
        Sets the source_container_database_connection_id of this CloneMigrationDetails.
        The OCID of the Source Container Database Connection. Only used for Online migrations.
        Only Connections of type Non-Autonomous can be used as source container databases.


        :param source_container_database_connection_id: The source_container_database_connection_id of this CloneMigrationDetails.
        :type: str
        """
        self._source_container_database_connection_id = source_container_database_connection_id

    @property
    def target_database_connection_id(self):
        """
        **[Required]** Gets the target_database_connection_id of this CloneMigrationDetails.
        The OCID of the Target Database Connection.


        :return: The target_database_connection_id of this CloneMigrationDetails.
        :rtype: str
        """
        return self._target_database_connection_id

    @target_database_connection_id.setter
    def target_database_connection_id(self, target_database_connection_id):
        """
        Sets the target_database_connection_id of this CloneMigrationDetails.
        The OCID of the Target Database Connection.


        :param target_database_connection_id: The target_database_connection_id of this CloneMigrationDetails.
        :type: str
        """
        self._target_database_connection_id = target_database_connection_id

    @property
    def exclude_objects(self):
        """
        Gets the exclude_objects of this CloneMigrationDetails.
        Database objects to exclude from migration.


        :return: The exclude_objects of this CloneMigrationDetails.
        :rtype: list[oci.database_migration.models.DatabaseObject]
        """
        return self._exclude_objects

    @exclude_objects.setter
    def exclude_objects(self, exclude_objects):
        """
        Sets the exclude_objects of this CloneMigrationDetails.
        Database objects to exclude from migration.


        :param exclude_objects: The exclude_objects of this CloneMigrationDetails.
        :type: list[oci.database_migration.models.DatabaseObject]
        """
        self._exclude_objects = exclude_objects

    @property
    def vault_details(self):
        """
        Gets the vault_details of this CloneMigrationDetails.

        :return: The vault_details of this CloneMigrationDetails.
        :rtype: oci.database_migration.models.CreateVaultDetails
        """
        return self._vault_details

    @vault_details.setter
    def vault_details(self, vault_details):
        """
        Sets the vault_details of this CloneMigrationDetails.

        :param vault_details: The vault_details of this CloneMigrationDetails.
        :type: oci.database_migration.models.CreateVaultDetails
        """
        self._vault_details = vault_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CloneMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CloneMigrationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CloneMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CloneMigrationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CloneMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CloneMigrationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CloneMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CloneMigrationDetails.
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
