# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_configuration_summary import DatabaseConfigurationSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmManagedExternalDatabaseConfigurationSummary(DatabaseConfigurationSummary):
    """
    Configuration summary of a EM Managed External database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmManagedExternalDatabaseConfigurationSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EmManagedExternalDatabaseConfigurationSummary.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_insight_id:
            The value to assign to the database_insight_id property of this EmManagedExternalDatabaseConfigurationSummary.
        :type database_insight_id: str

        :param entity_source:
            The value to assign to the entity_source property of this EmManagedExternalDatabaseConfigurationSummary.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EmManagedExternalDatabaseConfigurationSummary.
        :type compartment_id: str

        :param database_name:
            The value to assign to the database_name property of this EmManagedExternalDatabaseConfigurationSummary.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this EmManagedExternalDatabaseConfigurationSummary.
        :type database_display_name: str

        :param database_type:
            The value to assign to the database_type property of this EmManagedExternalDatabaseConfigurationSummary.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this EmManagedExternalDatabaseConfigurationSummary.
        :type database_version: str

        :param defined_tags:
            The value to assign to the defined_tags property of this EmManagedExternalDatabaseConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EmManagedExternalDatabaseConfigurationSummary.
        :type freeform_tags: dict(str, str)

        :param processor_count:
            The value to assign to the processor_count property of this EmManagedExternalDatabaseConfigurationSummary.
        :type processor_count: int

        :param enterprise_manager_identifier:
            The value to assign to the enterprise_manager_identifier property of this EmManagedExternalDatabaseConfigurationSummary.
        :type enterprise_manager_identifier: str

        :param enterprise_manager_bridge_id:
            The value to assign to the enterprise_manager_bridge_id property of this EmManagedExternalDatabaseConfigurationSummary.
        :type enterprise_manager_bridge_id: str

        :param instances:
            The value to assign to the instances property of this EmManagedExternalDatabaseConfigurationSummary.
        :type instances: list[oci.opsi.models.HostInstanceMap]

        """
        self.swagger_types = {
            'database_insight_id': 'str',
            'entity_source': 'str',
            'compartment_id': 'str',
            'database_name': 'str',
            'database_display_name': 'str',
            'database_type': 'str',
            'database_version': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'processor_count': 'int',
            'enterprise_manager_identifier': 'str',
            'enterprise_manager_bridge_id': 'str',
            'instances': 'list[HostInstanceMap]'
        }

        self.attribute_map = {
            'database_insight_id': 'databaseInsightId',
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'database_name': 'databaseName',
            'database_display_name': 'databaseDisplayName',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'processor_count': 'processorCount',
            'enterprise_manager_identifier': 'enterpriseManagerIdentifier',
            'enterprise_manager_bridge_id': 'enterpriseManagerBridgeId',
            'instances': 'instances'
        }

        self._database_insight_id = None
        self._entity_source = None
        self._compartment_id = None
        self._database_name = None
        self._database_display_name = None
        self._database_type = None
        self._database_version = None
        self._defined_tags = None
        self._freeform_tags = None
        self._processor_count = None
        self._enterprise_manager_identifier = None
        self._enterprise_manager_bridge_id = None
        self._instances = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_DATABASE'

    @property
    def enterprise_manager_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_identifier of this EmManagedExternalDatabaseConfigurationSummary.
        Enterprise Manager Unique Identifier


        :return: The enterprise_manager_identifier of this EmManagedExternalDatabaseConfigurationSummary.
        :rtype: str
        """
        return self._enterprise_manager_identifier

    @enterprise_manager_identifier.setter
    def enterprise_manager_identifier(self, enterprise_manager_identifier):
        """
        Sets the enterprise_manager_identifier of this EmManagedExternalDatabaseConfigurationSummary.
        Enterprise Manager Unique Identifier


        :param enterprise_manager_identifier: The enterprise_manager_identifier of this EmManagedExternalDatabaseConfigurationSummary.
        :type: str
        """
        self._enterprise_manager_identifier = enterprise_manager_identifier

    @property
    def enterprise_manager_bridge_id(self):
        """
        **[Required]** Gets the enterprise_manager_bridge_id of this EmManagedExternalDatabaseConfigurationSummary.
        OPSI Enterprise Manager Bridge OCID


        :return: The enterprise_manager_bridge_id of this EmManagedExternalDatabaseConfigurationSummary.
        :rtype: str
        """
        return self._enterprise_manager_bridge_id

    @enterprise_manager_bridge_id.setter
    def enterprise_manager_bridge_id(self, enterprise_manager_bridge_id):
        """
        Sets the enterprise_manager_bridge_id of this EmManagedExternalDatabaseConfigurationSummary.
        OPSI Enterprise Manager Bridge OCID


        :param enterprise_manager_bridge_id: The enterprise_manager_bridge_id of this EmManagedExternalDatabaseConfigurationSummary.
        :type: str
        """
        self._enterprise_manager_bridge_id = enterprise_manager_bridge_id

    @property
    def instances(self):
        """
        **[Required]** Gets the instances of this EmManagedExternalDatabaseConfigurationSummary.
        Array of hostname and instance name.


        :return: The instances of this EmManagedExternalDatabaseConfigurationSummary.
        :rtype: list[oci.opsi.models.HostInstanceMap]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """
        Sets the instances of this EmManagedExternalDatabaseConfigurationSummary.
        Array of hostname and instance name.


        :param instances: The instances of this EmManagedExternalDatabaseConfigurationSummary.
        :type: list[oci.opsi.models.HostInstanceMap]
        """
        self._instances = instances

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
