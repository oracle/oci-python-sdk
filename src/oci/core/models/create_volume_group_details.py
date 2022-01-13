# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVolumeGroupDetails(object):
    """
    CreateVolumeGroupDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVolumeGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateVolumeGroupDetails.
        :type availability_domain: str

        :param backup_policy_id:
            The value to assign to the backup_policy_id property of this CreateVolumeGroupDetails.
        :type backup_policy_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVolumeGroupDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVolumeGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateVolumeGroupDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVolumeGroupDetails.
        :type freeform_tags: dict(str, str)

        :param source_details:
            The value to assign to the source_details property of this CreateVolumeGroupDetails.
        :type source_details: oci.core.models.VolumeGroupSourceDetails

        :param volume_group_replicas:
            The value to assign to the volume_group_replicas property of this CreateVolumeGroupDetails.
        :type volume_group_replicas: list[oci.core.models.VolumeGroupReplicaDetails]

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'backup_policy_id': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'source_details': 'VolumeGroupSourceDetails',
            'volume_group_replicas': 'list[VolumeGroupReplicaDetails]'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'backup_policy_id': 'backupPolicyId',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'source_details': 'sourceDetails',
            'volume_group_replicas': 'volumeGroupReplicas'
        }

        self._availability_domain = None
        self._backup_policy_id = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._source_details = None
        self._volume_group_replicas = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateVolumeGroupDetails.
        The availability domain of the volume group.


        :return: The availability_domain of this CreateVolumeGroupDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateVolumeGroupDetails.
        The availability domain of the volume group.


        :param availability_domain: The availability_domain of this CreateVolumeGroupDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def backup_policy_id(self):
        """
        Gets the backup_policy_id of this CreateVolumeGroupDetails.
        If provided, specifies the ID of the volume backup policy to assign to the newly
        created volume group. If omitted, no policy will be assigned.


        :return: The backup_policy_id of this CreateVolumeGroupDetails.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        """
        Sets the backup_policy_id of this CreateVolumeGroupDetails.
        If provided, specifies the ID of the volume backup policy to assign to the newly
        created volume group. If omitted, no policy will be assigned.


        :param backup_policy_id: The backup_policy_id of this CreateVolumeGroupDetails.
        :type: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVolumeGroupDetails.
        The OCID of the compartment that contains the volume group.


        :return: The compartment_id of this CreateVolumeGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVolumeGroupDetails.
        The OCID of the compartment that contains the volume group.


        :param compartment_id: The compartment_id of this CreateVolumeGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVolumeGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVolumeGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVolumeGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVolumeGroupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVolumeGroupDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateVolumeGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVolumeGroupDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateVolumeGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVolumeGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVolumeGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVolumeGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVolumeGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def source_details(self):
        """
        **[Required]** Gets the source_details of this CreateVolumeGroupDetails.

        :return: The source_details of this CreateVolumeGroupDetails.
        :rtype: oci.core.models.VolumeGroupSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this CreateVolumeGroupDetails.

        :param source_details: The source_details of this CreateVolumeGroupDetails.
        :type: oci.core.models.VolumeGroupSourceDetails
        """
        self._source_details = source_details

    @property
    def volume_group_replicas(self):
        """
        Gets the volume_group_replicas of this CreateVolumeGroupDetails.
        The list of volume group replicas that this volume group will be enabled to have
        in the specified destination availability domains.


        :return: The volume_group_replicas of this CreateVolumeGroupDetails.
        :rtype: list[oci.core.models.VolumeGroupReplicaDetails]
        """
        return self._volume_group_replicas

    @volume_group_replicas.setter
    def volume_group_replicas(self, volume_group_replicas):
        """
        Sets the volume_group_replicas of this CreateVolumeGroupDetails.
        The list of volume group replicas that this volume group will be enabled to have
        in the specified destination availability domains.


        :param volume_group_replicas: The volume_group_replicas of this CreateVolumeGroupDetails.
        :type: list[oci.core.models.VolumeGroupReplicaDetails]
        """
        self._volume_group_replicas = volume_group_replicas

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
