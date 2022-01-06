# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_configuration_summary import DatabaseConfigurationSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MacsManagedExternalDatabaseConfigurationSummary(DatabaseConfigurationSummary):
    """
    Configuration Summary of a Macs Managed External database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MacsManagedExternalDatabaseConfigurationSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.MacsManagedExternalDatabaseConfigurationSummary.entity_source` attribute
        of this class is ``MACS_MANAGED_EXTERNAL_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_insight_id:
            The value to assign to the database_insight_id property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type database_insight_id: str

        :param entity_source:
            The value to assign to the entity_source property of this MacsManagedExternalDatabaseConfigurationSummary.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type compartment_id: str

        :param database_name:
            The value to assign to the database_name property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type database_display_name: str

        :param database_type:
            The value to assign to the database_type property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type database_version: str

        :param cdb_name:
            The value to assign to the cdb_name property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type cdb_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type freeform_tags: dict(str, str)

        :param processor_count:
            The value to assign to the processor_count property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type processor_count: int

        :param database_id:
            The value to assign to the database_id property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type database_id: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type management_agent_id: str

        :param connector_id:
            The value to assign to the connector_id property of this MacsManagedExternalDatabaseConfigurationSummary.
        :type connector_id: str

        :param instances:
            The value to assign to the instances property of this MacsManagedExternalDatabaseConfigurationSummary.
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
            'cdb_name': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'processor_count': 'int',
            'database_id': 'str',
            'management_agent_id': 'str',
            'connector_id': 'str',
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
            'cdb_name': 'cdbName',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'processor_count': 'processorCount',
            'database_id': 'databaseId',
            'management_agent_id': 'managementAgentId',
            'connector_id': 'connectorId',
            'instances': 'instances'
        }

        self._database_insight_id = None
        self._entity_source = None
        self._compartment_id = None
        self._database_name = None
        self._database_display_name = None
        self._database_type = None
        self._database_version = None
        self._cdb_name = None
        self._defined_tags = None
        self._freeform_tags = None
        self._processor_count = None
        self._database_id = None
        self._management_agent_id = None
        self._connector_id = None
        self._instances = None
        self._entity_source = 'MACS_MANAGED_EXTERNAL_DATABASE'

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this MacsManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The database_id of this MacsManagedExternalDatabaseConfigurationSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this MacsManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this MacsManagedExternalDatabaseConfigurationSummary.
        :type: str
        """
        self._database_id = database_id

    @property
    def management_agent_id(self):
        """
        **[Required]** Gets the management_agent_id of this MacsManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this MacsManagedExternalDatabaseConfigurationSummary.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this MacsManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this MacsManagedExternalDatabaseConfigurationSummary.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def connector_id(self):
        """
        **[Required]** Gets the connector_id of this MacsManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of External Database Connector

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The connector_id of this MacsManagedExternalDatabaseConfigurationSummary.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this MacsManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of External Database Connector

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param connector_id: The connector_id of this MacsManagedExternalDatabaseConfigurationSummary.
        :type: str
        """
        self._connector_id = connector_id

    @property
    def instances(self):
        """
        **[Required]** Gets the instances of this MacsManagedExternalDatabaseConfigurationSummary.
        Array of hostname and instance name.


        :return: The instances of this MacsManagedExternalDatabaseConfigurationSummary.
        :rtype: list[oci.opsi.models.HostInstanceMap]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """
        Sets the instances of this MacsManagedExternalDatabaseConfigurationSummary.
        Array of hostname and instance name.


        :param instances: The instances of this MacsManagedExternalDatabaseConfigurationSummary.
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
