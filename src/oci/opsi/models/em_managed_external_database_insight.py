# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_insight import DatabaseInsight
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmManagedExternalDatabaseInsight(DatabaseInsight):
    """
    Database insight resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmManagedExternalDatabaseInsight object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EmManagedExternalDatabaseInsight.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EmManagedExternalDatabaseInsight.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE"
        :type entity_source: str

        :param id:
            The value to assign to the id property of this EmManagedExternalDatabaseInsight.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EmManagedExternalDatabaseInsight.
        :type compartment_id: str

        :param status:
            The value to assign to the status property of this EmManagedExternalDatabaseInsight.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"
        :type status: str

        :param database_type:
            The value to assign to the database_type property of this EmManagedExternalDatabaseInsight.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this EmManagedExternalDatabaseInsight.
        :type database_version: str

        :param processor_count:
            The value to assign to the processor_count property of this EmManagedExternalDatabaseInsight.
        :type processor_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EmManagedExternalDatabaseInsight.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EmManagedExternalDatabaseInsight.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EmManagedExternalDatabaseInsight.
        :type system_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this EmManagedExternalDatabaseInsight.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EmManagedExternalDatabaseInsight.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EmManagedExternalDatabaseInsight.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this EmManagedExternalDatabaseInsight.
        :type lifecycle_details: str

        :param enterprise_manager_identifier:
            The value to assign to the enterprise_manager_identifier property of this EmManagedExternalDatabaseInsight.
        :type enterprise_manager_identifier: str

        :param enterprise_manager_entity_name:
            The value to assign to the enterprise_manager_entity_name property of this EmManagedExternalDatabaseInsight.
        :type enterprise_manager_entity_name: str

        :param enterprise_manager_entity_type:
            The value to assign to the enterprise_manager_entity_type property of this EmManagedExternalDatabaseInsight.
        :type enterprise_manager_entity_type: str

        :param enterprise_manager_entity_identifier:
            The value to assign to the enterprise_manager_entity_identifier property of this EmManagedExternalDatabaseInsight.
        :type enterprise_manager_entity_identifier: str

        :param enterprise_manager_entity_display_name:
            The value to assign to the enterprise_manager_entity_display_name property of this EmManagedExternalDatabaseInsight.
        :type enterprise_manager_entity_display_name: str

        :param enterprise_manager_bridge_id:
            The value to assign to the enterprise_manager_bridge_id property of this EmManagedExternalDatabaseInsight.
        :type enterprise_manager_bridge_id: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'status': 'str',
            'database_type': 'str',
            'database_version': 'str',
            'processor_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'enterprise_manager_identifier': 'str',
            'enterprise_manager_entity_name': 'str',
            'enterprise_manager_entity_type': 'str',
            'enterprise_manager_entity_identifier': 'str',
            'enterprise_manager_entity_display_name': 'str',
            'enterprise_manager_bridge_id': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'status': 'status',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion',
            'processor_count': 'processorCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'enterprise_manager_identifier': 'enterpriseManagerIdentifier',
            'enterprise_manager_entity_name': 'enterpriseManagerEntityName',
            'enterprise_manager_entity_type': 'enterpriseManagerEntityType',
            'enterprise_manager_entity_identifier': 'enterpriseManagerEntityIdentifier',
            'enterprise_manager_entity_display_name': 'enterpriseManagerEntityDisplayName',
            'enterprise_manager_bridge_id': 'enterpriseManagerBridgeId'
        }

        self._entity_source = None
        self._id = None
        self._compartment_id = None
        self._status = None
        self._database_type = None
        self._database_version = None
        self._processor_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
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
        self._entity_source = 'EM_MANAGED_EXTERNAL_DATABASE'

    @property
    def enterprise_manager_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_identifier of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Unique Identifier


        :return: The enterprise_manager_identifier of this EmManagedExternalDatabaseInsight.
        :rtype: str
        """
        return self._enterprise_manager_identifier

    @enterprise_manager_identifier.setter
    def enterprise_manager_identifier(self, enterprise_manager_identifier):
        """
        Sets the enterprise_manager_identifier of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Unique Identifier


        :param enterprise_manager_identifier: The enterprise_manager_identifier of this EmManagedExternalDatabaseInsight.
        :type: str
        """
        self._enterprise_manager_identifier = enterprise_manager_identifier

    @property
    def enterprise_manager_entity_name(self):
        """
        **[Required]** Gets the enterprise_manager_entity_name of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Entity Name


        :return: The enterprise_manager_entity_name of this EmManagedExternalDatabaseInsight.
        :rtype: str
        """
        return self._enterprise_manager_entity_name

    @enterprise_manager_entity_name.setter
    def enterprise_manager_entity_name(self, enterprise_manager_entity_name):
        """
        Sets the enterprise_manager_entity_name of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Entity Name


        :param enterprise_manager_entity_name: The enterprise_manager_entity_name of this EmManagedExternalDatabaseInsight.
        :type: str
        """
        self._enterprise_manager_entity_name = enterprise_manager_entity_name

    @property
    def enterprise_manager_entity_type(self):
        """
        **[Required]** Gets the enterprise_manager_entity_type of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Entity Type


        :return: The enterprise_manager_entity_type of this EmManagedExternalDatabaseInsight.
        :rtype: str
        """
        return self._enterprise_manager_entity_type

    @enterprise_manager_entity_type.setter
    def enterprise_manager_entity_type(self, enterprise_manager_entity_type):
        """
        Sets the enterprise_manager_entity_type of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Entity Type


        :param enterprise_manager_entity_type: The enterprise_manager_entity_type of this EmManagedExternalDatabaseInsight.
        :type: str
        """
        self._enterprise_manager_entity_type = enterprise_manager_entity_type

    @property
    def enterprise_manager_entity_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_entity_identifier of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Entity Unique Identifier


        :return: The enterprise_manager_entity_identifier of this EmManagedExternalDatabaseInsight.
        :rtype: str
        """
        return self._enterprise_manager_entity_identifier

    @enterprise_manager_entity_identifier.setter
    def enterprise_manager_entity_identifier(self, enterprise_manager_entity_identifier):
        """
        Sets the enterprise_manager_entity_identifier of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Entity Unique Identifier


        :param enterprise_manager_entity_identifier: The enterprise_manager_entity_identifier of this EmManagedExternalDatabaseInsight.
        :type: str
        """
        self._enterprise_manager_entity_identifier = enterprise_manager_entity_identifier

    @property
    def enterprise_manager_entity_display_name(self):
        """
        Gets the enterprise_manager_entity_display_name of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Entity Display Name


        :return: The enterprise_manager_entity_display_name of this EmManagedExternalDatabaseInsight.
        :rtype: str
        """
        return self._enterprise_manager_entity_display_name

    @enterprise_manager_entity_display_name.setter
    def enterprise_manager_entity_display_name(self, enterprise_manager_entity_display_name):
        """
        Sets the enterprise_manager_entity_display_name of this EmManagedExternalDatabaseInsight.
        Enterprise Manager Entity Display Name


        :param enterprise_manager_entity_display_name: The enterprise_manager_entity_display_name of this EmManagedExternalDatabaseInsight.
        :type: str
        """
        self._enterprise_manager_entity_display_name = enterprise_manager_entity_display_name

    @property
    def enterprise_manager_bridge_id(self):
        """
        **[Required]** Gets the enterprise_manager_bridge_id of this EmManagedExternalDatabaseInsight.
        OPSI Enterprise Manager Bridge OCID


        :return: The enterprise_manager_bridge_id of this EmManagedExternalDatabaseInsight.
        :rtype: str
        """
        return self._enterprise_manager_bridge_id

    @enterprise_manager_bridge_id.setter
    def enterprise_manager_bridge_id(self, enterprise_manager_bridge_id):
        """
        Sets the enterprise_manager_bridge_id of this EmManagedExternalDatabaseInsight.
        OPSI Enterprise Manager Bridge OCID


        :param enterprise_manager_bridge_id: The enterprise_manager_bridge_id of this EmManagedExternalDatabaseInsight.
        :type: str
        """
        self._enterprise_manager_bridge_id = enterprise_manager_bridge_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
