# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_exadata_insight_details import CreateExadataInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEmManagedExternalExadataInsightDetails(CreateExadataInsightDetails):
    """
    The information about the Exadata system to be analyzed. If memberEntityDetails is not specified, the the Enterprise Manager entity (e.g. databases and hosts) associated with an Exadata system will be placed in the same compartment as the Exadata system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEmManagedExternalExadataInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.CreateEmManagedExternalExadataInsightDetails.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_EXADATA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this CreateEmManagedExternalExadataInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA", "PE_COMANAGED_EXADATA"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateEmManagedExternalExadataInsightDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateEmManagedExternalExadataInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateEmManagedExternalExadataInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param enterprise_manager_identifier:
            The value to assign to the enterprise_manager_identifier property of this CreateEmManagedExternalExadataInsightDetails.
        :type enterprise_manager_identifier: str

        :param enterprise_manager_bridge_id:
            The value to assign to the enterprise_manager_bridge_id property of this CreateEmManagedExternalExadataInsightDetails.
        :type enterprise_manager_bridge_id: str

        :param enterprise_manager_entity_identifier:
            The value to assign to the enterprise_manager_entity_identifier property of this CreateEmManagedExternalExadataInsightDetails.
        :type enterprise_manager_entity_identifier: str

        :param member_entity_details:
            The value to assign to the member_entity_details property of this CreateEmManagedExternalExadataInsightDetails.
        :type member_entity_details: list[oci.opsi.models.CreateEmManagedExternalExadataMemberEntityDetails]

        :param is_auto_sync_enabled:
            The value to assign to the is_auto_sync_enabled property of this CreateEmManagedExternalExadataInsightDetails.
        :type is_auto_sync_enabled: bool

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'enterprise_manager_identifier': 'str',
            'enterprise_manager_bridge_id': 'str',
            'enterprise_manager_entity_identifier': 'str',
            'member_entity_details': 'list[CreateEmManagedExternalExadataMemberEntityDetails]',
            'is_auto_sync_enabled': 'bool'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'enterprise_manager_identifier': 'enterpriseManagerIdentifier',
            'enterprise_manager_bridge_id': 'enterpriseManagerBridgeId',
            'enterprise_manager_entity_identifier': 'enterpriseManagerEntityIdentifier',
            'member_entity_details': 'memberEntityDetails',
            'is_auto_sync_enabled': 'isAutoSyncEnabled'
        }

        self._entity_source = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._enterprise_manager_identifier = None
        self._enterprise_manager_bridge_id = None
        self._enterprise_manager_entity_identifier = None
        self._member_entity_details = None
        self._is_auto_sync_enabled = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_EXADATA'

    @property
    def enterprise_manager_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_identifier of this CreateEmManagedExternalExadataInsightDetails.
        Enterprise Manager Unique Identifier


        :return: The enterprise_manager_identifier of this CreateEmManagedExternalExadataInsightDetails.
        :rtype: str
        """
        return self._enterprise_manager_identifier

    @enterprise_manager_identifier.setter
    def enterprise_manager_identifier(self, enterprise_manager_identifier):
        """
        Sets the enterprise_manager_identifier of this CreateEmManagedExternalExadataInsightDetails.
        Enterprise Manager Unique Identifier


        :param enterprise_manager_identifier: The enterprise_manager_identifier of this CreateEmManagedExternalExadataInsightDetails.
        :type: str
        """
        self._enterprise_manager_identifier = enterprise_manager_identifier

    @property
    def enterprise_manager_bridge_id(self):
        """
        **[Required]** Gets the enterprise_manager_bridge_id of this CreateEmManagedExternalExadataInsightDetails.
        OPSI Enterprise Manager Bridge OCID


        :return: The enterprise_manager_bridge_id of this CreateEmManagedExternalExadataInsightDetails.
        :rtype: str
        """
        return self._enterprise_manager_bridge_id

    @enterprise_manager_bridge_id.setter
    def enterprise_manager_bridge_id(self, enterprise_manager_bridge_id):
        """
        Sets the enterprise_manager_bridge_id of this CreateEmManagedExternalExadataInsightDetails.
        OPSI Enterprise Manager Bridge OCID


        :param enterprise_manager_bridge_id: The enterprise_manager_bridge_id of this CreateEmManagedExternalExadataInsightDetails.
        :type: str
        """
        self._enterprise_manager_bridge_id = enterprise_manager_bridge_id

    @property
    def enterprise_manager_entity_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_entity_identifier of this CreateEmManagedExternalExadataInsightDetails.
        Enterprise Manager Entity Unique Identifier


        :return: The enterprise_manager_entity_identifier of this CreateEmManagedExternalExadataInsightDetails.
        :rtype: str
        """
        return self._enterprise_manager_entity_identifier

    @enterprise_manager_entity_identifier.setter
    def enterprise_manager_entity_identifier(self, enterprise_manager_entity_identifier):
        """
        Sets the enterprise_manager_entity_identifier of this CreateEmManagedExternalExadataInsightDetails.
        Enterprise Manager Entity Unique Identifier


        :param enterprise_manager_entity_identifier: The enterprise_manager_entity_identifier of this CreateEmManagedExternalExadataInsightDetails.
        :type: str
        """
        self._enterprise_manager_entity_identifier = enterprise_manager_entity_identifier

    @property
    def member_entity_details(self):
        """
        Gets the member_entity_details of this CreateEmManagedExternalExadataInsightDetails.

        :return: The member_entity_details of this CreateEmManagedExternalExadataInsightDetails.
        :rtype: list[oci.opsi.models.CreateEmManagedExternalExadataMemberEntityDetails]
        """
        return self._member_entity_details

    @member_entity_details.setter
    def member_entity_details(self, member_entity_details):
        """
        Sets the member_entity_details of this CreateEmManagedExternalExadataInsightDetails.

        :param member_entity_details: The member_entity_details of this CreateEmManagedExternalExadataInsightDetails.
        :type: list[oci.opsi.models.CreateEmManagedExternalExadataMemberEntityDetails]
        """
        self._member_entity_details = member_entity_details

    @property
    def is_auto_sync_enabled(self):
        """
        Gets the is_auto_sync_enabled of this CreateEmManagedExternalExadataInsightDetails.
        Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will be placed in the same compartment as the related Exadata Insight.


        :return: The is_auto_sync_enabled of this CreateEmManagedExternalExadataInsightDetails.
        :rtype: bool
        """
        return self._is_auto_sync_enabled

    @is_auto_sync_enabled.setter
    def is_auto_sync_enabled(self, is_auto_sync_enabled):
        """
        Sets the is_auto_sync_enabled of this CreateEmManagedExternalExadataInsightDetails.
        Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will be placed in the same compartment as the related Exadata Insight.


        :param is_auto_sync_enabled: The is_auto_sync_enabled of this CreateEmManagedExternalExadataInsightDetails.
        :type: bool
        """
        self._is_auto_sync_enabled = is_auto_sync_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
