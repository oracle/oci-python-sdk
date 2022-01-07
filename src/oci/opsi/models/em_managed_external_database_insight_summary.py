# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_insight_summary import DatabaseInsightSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmManagedExternalDatabaseInsightSummary(DatabaseInsightSummary):
    """
    Summary of a database insight resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmManagedExternalDatabaseInsightSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EmManagedExternalDatabaseInsightSummary.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EmManagedExternalDatabaseInsightSummary.
        :type id: str

        :param database_id:
            The value to assign to the database_id property of this EmManagedExternalDatabaseInsightSummary.
        :type database_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EmManagedExternalDatabaseInsightSummary.
        :type compartment_id: str

        :param database_name:
            The value to assign to the database_name property of this EmManagedExternalDatabaseInsightSummary.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this EmManagedExternalDatabaseInsightSummary.
        :type database_display_name: str

        :param database_type:
            The value to assign to the database_type property of this EmManagedExternalDatabaseInsightSummary.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this EmManagedExternalDatabaseInsightSummary.
        :type database_version: str

        :param database_host_names:
            The value to assign to the database_host_names property of this EmManagedExternalDatabaseInsightSummary.
        :type database_host_names: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EmManagedExternalDatabaseInsightSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EmManagedExternalDatabaseInsightSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EmManagedExternalDatabaseInsightSummary.
        :type system_tags: dict(str, dict(str, object))

        :param entity_source:
            The value to assign to the entity_source property of this EmManagedExternalDatabaseInsightSummary.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE"
        :type entity_source: str

        :param processor_count:
            The value to assign to the processor_count property of this EmManagedExternalDatabaseInsightSummary.
        :type processor_count: int

        :param status:
            The value to assign to the status property of this EmManagedExternalDatabaseInsightSummary.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this EmManagedExternalDatabaseInsightSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EmManagedExternalDatabaseInsightSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EmManagedExternalDatabaseInsightSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this EmManagedExternalDatabaseInsightSummary.
        :type lifecycle_details: str

        :param enterprise_manager_identifier:
            The value to assign to the enterprise_manager_identifier property of this EmManagedExternalDatabaseInsightSummary.
        :type enterprise_manager_identifier: str

        :param enterprise_manager_entity_name:
            The value to assign to the enterprise_manager_entity_name property of this EmManagedExternalDatabaseInsightSummary.
        :type enterprise_manager_entity_name: str

        :param enterprise_manager_entity_type:
            The value to assign to the enterprise_manager_entity_type property of this EmManagedExternalDatabaseInsightSummary.
        :type enterprise_manager_entity_type: str

        :param enterprise_manager_entity_identifier:
            The value to assign to the enterprise_manager_entity_identifier property of this EmManagedExternalDatabaseInsightSummary.
        :type enterprise_manager_entity_identifier: str

        :param enterprise_manager_entity_display_name:
            The value to assign to the enterprise_manager_entity_display_name property of this EmManagedExternalDatabaseInsightSummary.
        :type enterprise_manager_entity_display_name: str

        :param enterprise_manager_bridge_id:
            The value to assign to the enterprise_manager_bridge_id property of this EmManagedExternalDatabaseInsightSummary.
        :type enterprise_manager_bridge_id: str

        :param exadata_insight_id:
            The value to assign to the exadata_insight_id property of this EmManagedExternalDatabaseInsightSummary.
        :type exadata_insight_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'database_id': 'str',
            'compartment_id': 'str',
            'database_name': 'str',
            'database_display_name': 'str',
            'database_type': 'str',
            'database_version': 'str',
            'database_host_names': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'entity_source': 'str',
            'processor_count': 'int',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'enterprise_manager_identifier': 'str',
            'enterprise_manager_entity_name': 'str',
            'enterprise_manager_entity_type': 'str',
            'enterprise_manager_entity_identifier': 'str',
            'enterprise_manager_entity_display_name': 'str',
            'enterprise_manager_bridge_id': 'str',
            'exadata_insight_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'database_id': 'databaseId',
            'compartment_id': 'compartmentId',
            'database_name': 'databaseName',
            'database_display_name': 'databaseDisplayName',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion',
            'database_host_names': 'databaseHostNames',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'entity_source': 'entitySource',
            'processor_count': 'processorCount',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'enterprise_manager_identifier': 'enterpriseManagerIdentifier',
            'enterprise_manager_entity_name': 'enterpriseManagerEntityName',
            'enterprise_manager_entity_type': 'enterpriseManagerEntityType',
            'enterprise_manager_entity_identifier': 'enterpriseManagerEntityIdentifier',
            'enterprise_manager_entity_display_name': 'enterpriseManagerEntityDisplayName',
            'enterprise_manager_bridge_id': 'enterpriseManagerBridgeId',
            'exadata_insight_id': 'exadataInsightId'
        }

        self._id = None
        self._database_id = None
        self._compartment_id = None
        self._database_name = None
        self._database_display_name = None
        self._database_type = None
        self._database_version = None
        self._database_host_names = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._entity_source = None
        self._processor_count = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._enterprise_manager_identifier = None
        self._enterprise_manager_entity_name = None
        self._enterprise_manager_entity_type = None
        self._enterprise_manager_entity_identifier = None
        self._enterprise_manager_entity_display_name = None
        self._enterprise_manager_bridge_id = None
        self._exadata_insight_id = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_DATABASE'

    @property
    def enterprise_manager_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_identifier of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Unique Identifier


        :return: The enterprise_manager_identifier of this EmManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_identifier

    @enterprise_manager_identifier.setter
    def enterprise_manager_identifier(self, enterprise_manager_identifier):
        """
        Sets the enterprise_manager_identifier of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Unique Identifier


        :param enterprise_manager_identifier: The enterprise_manager_identifier of this EmManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._enterprise_manager_identifier = enterprise_manager_identifier

    @property
    def enterprise_manager_entity_name(self):
        """
        **[Required]** Gets the enterprise_manager_entity_name of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Entity Name


        :return: The enterprise_manager_entity_name of this EmManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_entity_name

    @enterprise_manager_entity_name.setter
    def enterprise_manager_entity_name(self, enterprise_manager_entity_name):
        """
        Sets the enterprise_manager_entity_name of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Entity Name


        :param enterprise_manager_entity_name: The enterprise_manager_entity_name of this EmManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._enterprise_manager_entity_name = enterprise_manager_entity_name

    @property
    def enterprise_manager_entity_type(self):
        """
        **[Required]** Gets the enterprise_manager_entity_type of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Entity Type


        :return: The enterprise_manager_entity_type of this EmManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_entity_type

    @enterprise_manager_entity_type.setter
    def enterprise_manager_entity_type(self, enterprise_manager_entity_type):
        """
        Sets the enterprise_manager_entity_type of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Entity Type


        :param enterprise_manager_entity_type: The enterprise_manager_entity_type of this EmManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._enterprise_manager_entity_type = enterprise_manager_entity_type

    @property
    def enterprise_manager_entity_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_entity_identifier of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Entity Unique Identifier


        :return: The enterprise_manager_entity_identifier of this EmManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_entity_identifier

    @enterprise_manager_entity_identifier.setter
    def enterprise_manager_entity_identifier(self, enterprise_manager_entity_identifier):
        """
        Sets the enterprise_manager_entity_identifier of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Entity Unique Identifier


        :param enterprise_manager_entity_identifier: The enterprise_manager_entity_identifier of this EmManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._enterprise_manager_entity_identifier = enterprise_manager_entity_identifier

    @property
    def enterprise_manager_entity_display_name(self):
        """
        Gets the enterprise_manager_entity_display_name of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Entity Display Name


        :return: The enterprise_manager_entity_display_name of this EmManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_entity_display_name

    @enterprise_manager_entity_display_name.setter
    def enterprise_manager_entity_display_name(self, enterprise_manager_entity_display_name):
        """
        Sets the enterprise_manager_entity_display_name of this EmManagedExternalDatabaseInsightSummary.
        Enterprise Manager Entity Display Name


        :param enterprise_manager_entity_display_name: The enterprise_manager_entity_display_name of this EmManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._enterprise_manager_entity_display_name = enterprise_manager_entity_display_name

    @property
    def enterprise_manager_bridge_id(self):
        """
        **[Required]** Gets the enterprise_manager_bridge_id of this EmManagedExternalDatabaseInsightSummary.
        OPSI Enterprise Manager Bridge OCID


        :return: The enterprise_manager_bridge_id of this EmManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_bridge_id

    @enterprise_manager_bridge_id.setter
    def enterprise_manager_bridge_id(self, enterprise_manager_bridge_id):
        """
        Sets the enterprise_manager_bridge_id of this EmManagedExternalDatabaseInsightSummary.
        OPSI Enterprise Manager Bridge OCID


        :param enterprise_manager_bridge_id: The enterprise_manager_bridge_id of this EmManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._enterprise_manager_bridge_id = enterprise_manager_bridge_id

    @property
    def exadata_insight_id(self):
        """
        Gets the exadata_insight_id of this EmManagedExternalDatabaseInsightSummary.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The exadata_insight_id of this EmManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._exadata_insight_id

    @exadata_insight_id.setter
    def exadata_insight_id(self, exadata_insight_id):
        """
        Sets the exadata_insight_id of this EmManagedExternalDatabaseInsightSummary.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param exadata_insight_id: The exadata_insight_id of this EmManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._exadata_insight_id = exadata_insight_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
