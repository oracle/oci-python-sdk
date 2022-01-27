# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNodePoolNodeConfigDetails(object):
    """
    The size and placement configuration of nodes in the node pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNodePoolNodeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param size:
            The value to assign to the size property of this CreateNodePoolNodeConfigDetails.
        :type size: int

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateNodePoolNodeConfigDetails.
        :type nsg_ids: list[str]

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateNodePoolNodeConfigDetails.
        :type kms_key_id: str

        :param is_pv_encryption_in_transit_enabled:
            The value to assign to the is_pv_encryption_in_transit_enabled property of this CreateNodePoolNodeConfigDetails.
        :type is_pv_encryption_in_transit_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateNodePoolNodeConfigDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateNodePoolNodeConfigDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param placement_configs:
            The value to assign to the placement_configs property of this CreateNodePoolNodeConfigDetails.
        :type placement_configs: list[oci.container_engine.models.NodePoolPlacementConfigDetails]

        """
        self.swagger_types = {
            'size': 'int',
            'nsg_ids': 'list[str]',
            'kms_key_id': 'str',
            'is_pv_encryption_in_transit_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'placement_configs': 'list[NodePoolPlacementConfigDetails]'
        }

        self.attribute_map = {
            'size': 'size',
            'nsg_ids': 'nsgIds',
            'kms_key_id': 'kmsKeyId',
            'is_pv_encryption_in_transit_enabled': 'isPvEncryptionInTransitEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'placement_configs': 'placementConfigs'
        }

        self._size = None
        self._nsg_ids = None
        self._kms_key_id = None
        self._is_pv_encryption_in_transit_enabled = None
        self._freeform_tags = None
        self._defined_tags = None
        self._placement_configs = None

    @property
    def size(self):
        """
        **[Required]** Gets the size of this CreateNodePoolNodeConfigDetails.
        The number of nodes that should be in the node pool.


        :return: The size of this CreateNodePoolNodeConfigDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this CreateNodePoolNodeConfigDetails.
        The number of nodes that should be in the node pool.


        :param size: The size of this CreateNodePoolNodeConfigDetails.
        :type: int
        """
        self._size = size

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateNodePoolNodeConfigDetails.
        The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this CreateNodePoolNodeConfigDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateNodePoolNodeConfigDetails.
        The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this CreateNodePoolNodeConfigDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CreateNodePoolNodeConfigDetails.
        The OCID of the Key Management Service key assigned to the boot volume.


        :return: The kms_key_id of this CreateNodePoolNodeConfigDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CreateNodePoolNodeConfigDetails.
        The OCID of the Key Management Service key assigned to the boot volume.


        :param kms_key_id: The kms_key_id of this CreateNodePoolNodeConfigDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def is_pv_encryption_in_transit_enabled(self):
        """
        Gets the is_pv_encryption_in_transit_enabled of this CreateNodePoolNodeConfigDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.


        :return: The is_pv_encryption_in_transit_enabled of this CreateNodePoolNodeConfigDetails.
        :rtype: bool
        """
        return self._is_pv_encryption_in_transit_enabled

    @is_pv_encryption_in_transit_enabled.setter
    def is_pv_encryption_in_transit_enabled(self, is_pv_encryption_in_transit_enabled):
        """
        Sets the is_pv_encryption_in_transit_enabled of this CreateNodePoolNodeConfigDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.


        :param is_pv_encryption_in_transit_enabled: The is_pv_encryption_in_transit_enabled of this CreateNodePoolNodeConfigDetails.
        :type: bool
        """
        self._is_pv_encryption_in_transit_enabled = is_pv_encryption_in_transit_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateNodePoolNodeConfigDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateNodePoolNodeConfigDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateNodePoolNodeConfigDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateNodePoolNodeConfigDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateNodePoolNodeConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateNodePoolNodeConfigDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateNodePoolNodeConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateNodePoolNodeConfigDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def placement_configs(self):
        """
        **[Required]** Gets the placement_configs of this CreateNodePoolNodeConfigDetails.
        The placement configurations for the node pool. Provide one placement
        configuration for each availability domain in which you intend to launch a node.

        To use the node pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :return: The placement_configs of this CreateNodePoolNodeConfigDetails.
        :rtype: list[oci.container_engine.models.NodePoolPlacementConfigDetails]
        """
        return self._placement_configs

    @placement_configs.setter
    def placement_configs(self, placement_configs):
        """
        Sets the placement_configs of this CreateNodePoolNodeConfigDetails.
        The placement configurations for the node pool. Provide one placement
        configuration for each availability domain in which you intend to launch a node.

        To use the node pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :param placement_configs: The placement_configs of this CreateNodePoolNodeConfigDetails.
        :type: list[oci.container_engine.models.NodePoolPlacementConfigDetails]
        """
        self._placement_configs = placement_configs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
