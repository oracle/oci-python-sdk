# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .exadata_configuration_summary import ExadataConfigurationSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataDatabaseMachineConfigurationSummary(ExadataConfigurationSummary):
    """
    Configuration summary of a database machine.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataDatabaseMachineConfigurationSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.ExadataDatabaseMachineConfigurationSummary.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_EXADATA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exadata_insight_id:
            The value to assign to the exadata_insight_id property of this ExadataDatabaseMachineConfigurationSummary.
        :type exadata_insight_id: str

        :param entity_source:
            The value to assign to the entity_source property of this ExadataDatabaseMachineConfigurationSummary.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA", "PE_COMANAGED_EXADATA"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExadataDatabaseMachineConfigurationSummary.
        :type compartment_id: str

        :param exadata_name:
            The value to assign to the exadata_name property of this ExadataDatabaseMachineConfigurationSummary.
        :type exadata_name: str

        :param exadata_display_name:
            The value to assign to the exadata_display_name property of this ExadataDatabaseMachineConfigurationSummary.
        :type exadata_display_name: str

        :param exadata_type:
            The value to assign to the exadata_type property of this ExadataDatabaseMachineConfigurationSummary.
            Allowed values for this property are: "DBMACHINE", "EXACS", "EXACC"
        :type exadata_type: str

        :param exadata_rack_type:
            The value to assign to the exadata_rack_type property of this ExadataDatabaseMachineConfigurationSummary.
            Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", "FLEX"
        :type exadata_rack_type: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ExadataDatabaseMachineConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExadataDatabaseMachineConfigurationSummary.
        :type freeform_tags: dict(str, str)

        :param vmcluster_details:
            The value to assign to the vmcluster_details property of this ExadataDatabaseMachineConfigurationSummary.
        :type vmcluster_details: list[oci.opsi.models.VmClusterSummary]

        :param enterprise_manager_identifier:
            The value to assign to the enterprise_manager_identifier property of this ExadataDatabaseMachineConfigurationSummary.
        :type enterprise_manager_identifier: str

        :param enterprise_manager_bridge_id:
            The value to assign to the enterprise_manager_bridge_id property of this ExadataDatabaseMachineConfigurationSummary.
        :type enterprise_manager_bridge_id: str

        """
        self.swagger_types = {
            'exadata_insight_id': 'str',
            'entity_source': 'str',
            'compartment_id': 'str',
            'exadata_name': 'str',
            'exadata_display_name': 'str',
            'exadata_type': 'str',
            'exadata_rack_type': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'vmcluster_details': 'list[VmClusterSummary]',
            'enterprise_manager_identifier': 'str',
            'enterprise_manager_bridge_id': 'str'
        }

        self.attribute_map = {
            'exadata_insight_id': 'exadataInsightId',
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'exadata_name': 'exadataName',
            'exadata_display_name': 'exadataDisplayName',
            'exadata_type': 'exadataType',
            'exadata_rack_type': 'exadataRackType',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'vmcluster_details': 'vmclusterDetails',
            'enterprise_manager_identifier': 'enterpriseManagerIdentifier',
            'enterprise_manager_bridge_id': 'enterpriseManagerBridgeId'
        }

        self._exadata_insight_id = None
        self._entity_source = None
        self._compartment_id = None
        self._exadata_name = None
        self._exadata_display_name = None
        self._exadata_type = None
        self._exadata_rack_type = None
        self._defined_tags = None
        self._freeform_tags = None
        self._vmcluster_details = None
        self._enterprise_manager_identifier = None
        self._enterprise_manager_bridge_id = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_EXADATA'

    @property
    def enterprise_manager_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_identifier of this ExadataDatabaseMachineConfigurationSummary.
        Enterprise Manager Unique Identifier


        :return: The enterprise_manager_identifier of this ExadataDatabaseMachineConfigurationSummary.
        :rtype: str
        """
        return self._enterprise_manager_identifier

    @enterprise_manager_identifier.setter
    def enterprise_manager_identifier(self, enterprise_manager_identifier):
        """
        Sets the enterprise_manager_identifier of this ExadataDatabaseMachineConfigurationSummary.
        Enterprise Manager Unique Identifier


        :param enterprise_manager_identifier: The enterprise_manager_identifier of this ExadataDatabaseMachineConfigurationSummary.
        :type: str
        """
        self._enterprise_manager_identifier = enterprise_manager_identifier

    @property
    def enterprise_manager_bridge_id(self):
        """
        **[Required]** Gets the enterprise_manager_bridge_id of this ExadataDatabaseMachineConfigurationSummary.
        OPSI Enterprise Manager Bridge OCID


        :return: The enterprise_manager_bridge_id of this ExadataDatabaseMachineConfigurationSummary.
        :rtype: str
        """
        return self._enterprise_manager_bridge_id

    @enterprise_manager_bridge_id.setter
    def enterprise_manager_bridge_id(self, enterprise_manager_bridge_id):
        """
        Sets the enterprise_manager_bridge_id of this ExadataDatabaseMachineConfigurationSummary.
        OPSI Enterprise Manager Bridge OCID


        :param enterprise_manager_bridge_id: The enterprise_manager_bridge_id of this ExadataDatabaseMachineConfigurationSummary.
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
