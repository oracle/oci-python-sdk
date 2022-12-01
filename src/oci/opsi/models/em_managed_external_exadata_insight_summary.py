# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .exadata_insight_summary import ExadataInsightSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmManagedExternalExadataInsightSummary(ExadataInsightSummary):
    """
    Summary of an Exadata insight resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmManagedExternalExadataInsightSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EmManagedExternalExadataInsightSummary.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_EXADATA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EmManagedExternalExadataInsightSummary.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA", "PE_COMANAGED_EXADATA"
        :type entity_source: str

        :param id:
            The value to assign to the id property of this EmManagedExternalExadataInsightSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EmManagedExternalExadataInsightSummary.
        :type compartment_id: str

        :param exadata_name:
            The value to assign to the exadata_name property of this EmManagedExternalExadataInsightSummary.
        :type exadata_name: str

        :param exadata_display_name:
            The value to assign to the exadata_display_name property of this EmManagedExternalExadataInsightSummary.
        :type exadata_display_name: str

        :param exadata_type:
            The value to assign to the exadata_type property of this EmManagedExternalExadataInsightSummary.
            Allowed values for this property are: "DBMACHINE", "EXACS", "EXACC"
        :type exadata_type: str

        :param exadata_rack_type:
            The value to assign to the exadata_rack_type property of this EmManagedExternalExadataInsightSummary.
            Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", "FLEX"
        :type exadata_rack_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EmManagedExternalExadataInsightSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EmManagedExternalExadataInsightSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EmManagedExternalExadataInsightSummary.
        :type system_tags: dict(str, dict(str, object))

        :param status:
            The value to assign to the status property of this EmManagedExternalExadataInsightSummary.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this EmManagedExternalExadataInsightSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EmManagedExternalExadataInsightSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EmManagedExternalExadataInsightSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this EmManagedExternalExadataInsightSummary.
        :type lifecycle_details: str

        :param enterprise_manager_identifier:
            The value to assign to the enterprise_manager_identifier property of this EmManagedExternalExadataInsightSummary.
        :type enterprise_manager_identifier: str

        :param enterprise_manager_entity_name:
            The value to assign to the enterprise_manager_entity_name property of this EmManagedExternalExadataInsightSummary.
        :type enterprise_manager_entity_name: str

        :param enterprise_manager_entity_type:
            The value to assign to the enterprise_manager_entity_type property of this EmManagedExternalExadataInsightSummary.
        :type enterprise_manager_entity_type: str

        :param enterprise_manager_entity_identifier:
            The value to assign to the enterprise_manager_entity_identifier property of this EmManagedExternalExadataInsightSummary.
        :type enterprise_manager_entity_identifier: str

        :param enterprise_manager_entity_display_name:
            The value to assign to the enterprise_manager_entity_display_name property of this EmManagedExternalExadataInsightSummary.
        :type enterprise_manager_entity_display_name: str

        :param enterprise_manager_bridge_id:
            The value to assign to the enterprise_manager_bridge_id property of this EmManagedExternalExadataInsightSummary.
        :type enterprise_manager_bridge_id: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'exadata_name': 'str',
            'exadata_display_name': 'str',
            'exadata_type': 'str',
            'exadata_rack_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
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
            'enterprise_manager_bridge_id': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'exadata_name': 'exadataName',
            'exadata_display_name': 'exadataDisplayName',
            'exadata_type': 'exadataType',
            'exadata_rack_type': 'exadataRackType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
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
            'enterprise_manager_bridge_id': 'enterpriseManagerBridgeId'
        }

        self._entity_source = None
        self._id = None
        self._compartment_id = None
        self._exadata_name = None
        self._exadata_display_name = None
        self._exadata_type = None
        self._exadata_rack_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
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
        self._entity_source = 'EM_MANAGED_EXTERNAL_EXADATA'

    @property
    def enterprise_manager_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_identifier of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Unique Identifier


        :return: The enterprise_manager_identifier of this EmManagedExternalExadataInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_identifier

    @enterprise_manager_identifier.setter
    def enterprise_manager_identifier(self, enterprise_manager_identifier):
        """
        Sets the enterprise_manager_identifier of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Unique Identifier


        :param enterprise_manager_identifier: The enterprise_manager_identifier of this EmManagedExternalExadataInsightSummary.
        :type: str
        """
        self._enterprise_manager_identifier = enterprise_manager_identifier

    @property
    def enterprise_manager_entity_name(self):
        """
        **[Required]** Gets the enterprise_manager_entity_name of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Entity Name


        :return: The enterprise_manager_entity_name of this EmManagedExternalExadataInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_entity_name

    @enterprise_manager_entity_name.setter
    def enterprise_manager_entity_name(self, enterprise_manager_entity_name):
        """
        Sets the enterprise_manager_entity_name of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Entity Name


        :param enterprise_manager_entity_name: The enterprise_manager_entity_name of this EmManagedExternalExadataInsightSummary.
        :type: str
        """
        self._enterprise_manager_entity_name = enterprise_manager_entity_name

    @property
    def enterprise_manager_entity_type(self):
        """
        **[Required]** Gets the enterprise_manager_entity_type of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Entity Type


        :return: The enterprise_manager_entity_type of this EmManagedExternalExadataInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_entity_type

    @enterprise_manager_entity_type.setter
    def enterprise_manager_entity_type(self, enterprise_manager_entity_type):
        """
        Sets the enterprise_manager_entity_type of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Entity Type


        :param enterprise_manager_entity_type: The enterprise_manager_entity_type of this EmManagedExternalExadataInsightSummary.
        :type: str
        """
        self._enterprise_manager_entity_type = enterprise_manager_entity_type

    @property
    def enterprise_manager_entity_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_entity_identifier of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Entity Unique Identifier


        :return: The enterprise_manager_entity_identifier of this EmManagedExternalExadataInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_entity_identifier

    @enterprise_manager_entity_identifier.setter
    def enterprise_manager_entity_identifier(self, enterprise_manager_entity_identifier):
        """
        Sets the enterprise_manager_entity_identifier of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Entity Unique Identifier


        :param enterprise_manager_entity_identifier: The enterprise_manager_entity_identifier of this EmManagedExternalExadataInsightSummary.
        :type: str
        """
        self._enterprise_manager_entity_identifier = enterprise_manager_entity_identifier

    @property
    def enterprise_manager_entity_display_name(self):
        """
        Gets the enterprise_manager_entity_display_name of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Entity Display Name


        :return: The enterprise_manager_entity_display_name of this EmManagedExternalExadataInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_entity_display_name

    @enterprise_manager_entity_display_name.setter
    def enterprise_manager_entity_display_name(self, enterprise_manager_entity_display_name):
        """
        Sets the enterprise_manager_entity_display_name of this EmManagedExternalExadataInsightSummary.
        Enterprise Manager Entity Display Name


        :param enterprise_manager_entity_display_name: The enterprise_manager_entity_display_name of this EmManagedExternalExadataInsightSummary.
        :type: str
        """
        self._enterprise_manager_entity_display_name = enterprise_manager_entity_display_name

    @property
    def enterprise_manager_bridge_id(self):
        """
        **[Required]** Gets the enterprise_manager_bridge_id of this EmManagedExternalExadataInsightSummary.
        OPSI Enterprise Manager Bridge OCID


        :return: The enterprise_manager_bridge_id of this EmManagedExternalExadataInsightSummary.
        :rtype: str
        """
        return self._enterprise_manager_bridge_id

    @enterprise_manager_bridge_id.setter
    def enterprise_manager_bridge_id(self, enterprise_manager_bridge_id):
        """
        Sets the enterprise_manager_bridge_id of this EmManagedExternalExadataInsightSummary.
        OPSI Enterprise Manager Bridge OCID


        :param enterprise_manager_bridge_id: The enterprise_manager_bridge_id of this EmManagedExternalExadataInsightSummary.
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
