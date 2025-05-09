# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateClusterPlacementGroupDetails(object):
    """
    Detailed information about the new cluster placement group.
    """

    #: A constant which can be used with the cluster_placement_group_type property of a CreateClusterPlacementGroupDetails.
    #: This constant has a value of "STANDARD"
    CLUSTER_PLACEMENT_GROUP_TYPE_STANDARD = "STANDARD"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateClusterPlacementGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateClusterPlacementGroupDetails.
        :type name: str

        :param cluster_placement_group_type:
            The value to assign to the cluster_placement_group_type property of this CreateClusterPlacementGroupDetails.
            Allowed values for this property are: "STANDARD"
        :type cluster_placement_group_type: str

        :param description:
            The value to assign to the description property of this CreateClusterPlacementGroupDetails.
        :type description: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateClusterPlacementGroupDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateClusterPlacementGroupDetails.
        :type compartment_id: str

        :param placement_instruction:
            The value to assign to the placement_instruction property of this CreateClusterPlacementGroupDetails.
        :type placement_instruction: oci.cluster_placement_groups.models.PlacementInstructionDetails

        :param capabilities:
            The value to assign to the capabilities property of this CreateClusterPlacementGroupDetails.
        :type capabilities: oci.cluster_placement_groups.models.CapabilitiesCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateClusterPlacementGroupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateClusterPlacementGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'cluster_placement_group_type': 'str',
            'description': 'str',
            'availability_domain': 'str',
            'compartment_id': 'str',
            'placement_instruction': 'PlacementInstructionDetails',
            'capabilities': 'CapabilitiesCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'name': 'name',
            'cluster_placement_group_type': 'clusterPlacementGroupType',
            'description': 'description',
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'placement_instruction': 'placementInstruction',
            'capabilities': 'capabilities',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._name = None
        self._cluster_placement_group_type = None
        self._description = None
        self._availability_domain = None
        self._compartment_id = None
        self._placement_instruction = None
        self._capabilities = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateClusterPlacementGroupDetails.
        The friendly name of the cluster placement group.


        :return: The name of this CreateClusterPlacementGroupDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateClusterPlacementGroupDetails.
        The friendly name of the cluster placement group.


        :param name: The name of this CreateClusterPlacementGroupDetails.
        :type: str
        """
        self._name = name

    @property
    def cluster_placement_group_type(self):
        """
        **[Required]** Gets the cluster_placement_group_type of this CreateClusterPlacementGroupDetails.
        ClusterPlacementGroup Identifier.

        Allowed values for this property are: "STANDARD"


        :return: The cluster_placement_group_type of this CreateClusterPlacementGroupDetails.
        :rtype: str
        """
        return self._cluster_placement_group_type

    @cluster_placement_group_type.setter
    def cluster_placement_group_type(self, cluster_placement_group_type):
        """
        Sets the cluster_placement_group_type of this CreateClusterPlacementGroupDetails.
        ClusterPlacementGroup Identifier.


        :param cluster_placement_group_type: The cluster_placement_group_type of this CreateClusterPlacementGroupDetails.
        :type: str
        """
        allowed_values = ["STANDARD"]
        if not value_allowed_none_or_none_sentinel(cluster_placement_group_type, allowed_values):
            raise ValueError(
                f"Invalid value for `cluster_placement_group_type`, must be None or one of {allowed_values}"
            )
        self._cluster_placement_group_type = cluster_placement_group_type

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateClusterPlacementGroupDetails.
        A description of the cluster placement group.


        :return: The description of this CreateClusterPlacementGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateClusterPlacementGroupDetails.
        A description of the cluster placement group.


        :param description: The description of this CreateClusterPlacementGroupDetails.
        :type: str
        """
        self._description = description

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateClusterPlacementGroupDetails.
        The availability domain where you want to create the cluster placement group.


        :return: The availability_domain of this CreateClusterPlacementGroupDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateClusterPlacementGroupDetails.
        The availability domain where you want to create the cluster placement group.


        :param availability_domain: The availability_domain of this CreateClusterPlacementGroupDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateClusterPlacementGroupDetails.
        The `OCID`__ of the compartment where you want to create the cluster placement group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateClusterPlacementGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateClusterPlacementGroupDetails.
        The `OCID`__ of the compartment where you want to create the cluster placement group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateClusterPlacementGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def placement_instruction(self):
        """
        Gets the placement_instruction of this CreateClusterPlacementGroupDetails.

        :return: The placement_instruction of this CreateClusterPlacementGroupDetails.
        :rtype: oci.cluster_placement_groups.models.PlacementInstructionDetails
        """
        return self._placement_instruction

    @placement_instruction.setter
    def placement_instruction(self, placement_instruction):
        """
        Sets the placement_instruction of this CreateClusterPlacementGroupDetails.

        :param placement_instruction: The placement_instruction of this CreateClusterPlacementGroupDetails.
        :type: oci.cluster_placement_groups.models.PlacementInstructionDetails
        """
        self._placement_instruction = placement_instruction

    @property
    def capabilities(self):
        """
        Gets the capabilities of this CreateClusterPlacementGroupDetails.

        :return: The capabilities of this CreateClusterPlacementGroupDetails.
        :rtype: oci.cluster_placement_groups.models.CapabilitiesCollection
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """
        Sets the capabilities of this CreateClusterPlacementGroupDetails.

        :param capabilities: The capabilities of this CreateClusterPlacementGroupDetails.
        :type: oci.cluster_placement_groups.models.CapabilitiesCollection
        """
        self._capabilities = capabilities

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateClusterPlacementGroupDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateClusterPlacementGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateClusterPlacementGroupDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateClusterPlacementGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateClusterPlacementGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateClusterPlacementGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateClusterPlacementGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateClusterPlacementGroupDetails.
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
