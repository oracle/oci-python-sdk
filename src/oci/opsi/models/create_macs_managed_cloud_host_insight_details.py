# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_host_insight_details import CreateHostInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMacsManagedCloudHostInsightDetails(CreateHostInsightDetails):
    """
    The information about the Compute Instance host to be analyzed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMacsManagedCloudHostInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.CreateMacsManagedCloudHostInsightDetails.entity_source` attribute
        of this class is ``MACS_MANAGED_CLOUD_HOST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this CreateMacsManagedCloudHostInsightDetails.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST", "MACS_MANAGED_CLOUD_HOST", "PE_COMANAGED_HOST"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMacsManagedCloudHostInsightDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMacsManagedCloudHostInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMacsManagedCloudHostInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param compute_id:
            The value to assign to the compute_id property of this CreateMacsManagedCloudHostInsightDetails.
        :type compute_id: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'compute_id': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'compute_id': 'computeId'
        }

        self._entity_source = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._compute_id = None
        self._entity_source = 'MACS_MANAGED_CLOUD_HOST'

    @property
    def compute_id(self):
        """
        **[Required]** Gets the compute_id of this CreateMacsManagedCloudHostInsightDetails.
        The `OCID`__ of the Compute Instance

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compute_id of this CreateMacsManagedCloudHostInsightDetails.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        """
        Sets the compute_id of this CreateMacsManagedCloudHostInsightDetails.
        The `OCID`__ of the Compute Instance

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compute_id: The compute_id of this CreateMacsManagedCloudHostInsightDetails.
        :type: str
        """
        self._compute_id = compute_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
