# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_exadata_insight_details import CreateExadataInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePeComanagedExadataInsightDetails(CreateExadataInsightDetails):
    """
    The information about the Exadata system to be analyzed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePeComanagedExadataInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.CreatePeComanagedExadataInsightDetails.entity_source` attribute
        of this class is ``PE_COMANAGED_EXADATA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this CreatePeComanagedExadataInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA", "PE_COMANAGED_EXADATA"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePeComanagedExadataInsightDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePeComanagedExadataInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePeComanagedExadataInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param exadata_infra_id:
            The value to assign to the exadata_infra_id property of this CreatePeComanagedExadataInsightDetails.
        :type exadata_infra_id: str

        :param member_vm_cluster_details:
            The value to assign to the member_vm_cluster_details property of this CreatePeComanagedExadataInsightDetails.
        :type member_vm_cluster_details: list[oci.opsi.models.CreatePeComanagedExadataVmclusterDetails]

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'exadata_infra_id': 'str',
            'member_vm_cluster_details': 'list[CreatePeComanagedExadataVmclusterDetails]'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'exadata_infra_id': 'exadataInfraId',
            'member_vm_cluster_details': 'memberVmClusterDetails'
        }

        self._entity_source = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._exadata_infra_id = None
        self._member_vm_cluster_details = None
        self._entity_source = 'PE_COMANAGED_EXADATA'

    @property
    def exadata_infra_id(self):
        """
        **[Required]** Gets the exadata_infra_id of this CreatePeComanagedExadataInsightDetails.
        The `OCID`__ of the Exadata Infrastructure.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The exadata_infra_id of this CreatePeComanagedExadataInsightDetails.
        :rtype: str
        """
        return self._exadata_infra_id

    @exadata_infra_id.setter
    def exadata_infra_id(self, exadata_infra_id):
        """
        Sets the exadata_infra_id of this CreatePeComanagedExadataInsightDetails.
        The `OCID`__ of the Exadata Infrastructure.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param exadata_infra_id: The exadata_infra_id of this CreatePeComanagedExadataInsightDetails.
        :type: str
        """
        self._exadata_infra_id = exadata_infra_id

    @property
    def member_vm_cluster_details(self):
        """
        Gets the member_vm_cluster_details of this CreatePeComanagedExadataInsightDetails.

        :return: The member_vm_cluster_details of this CreatePeComanagedExadataInsightDetails.
        :rtype: list[oci.opsi.models.CreatePeComanagedExadataVmclusterDetails]
        """
        return self._member_vm_cluster_details

    @member_vm_cluster_details.setter
    def member_vm_cluster_details(self, member_vm_cluster_details):
        """
        Sets the member_vm_cluster_details of this CreatePeComanagedExadataInsightDetails.

        :param member_vm_cluster_details: The member_vm_cluster_details of this CreatePeComanagedExadataInsightDetails.
        :type: list[oci.opsi.models.CreatePeComanagedExadataVmclusterDetails]
        """
        self._member_vm_cluster_details = member_vm_cluster_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
