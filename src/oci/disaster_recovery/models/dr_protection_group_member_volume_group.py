# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .dr_protection_group_member import DrProtectionGroupMember
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrProtectionGroupMemberVolumeGroup(DrProtectionGroupMember):
    """
    The properties for a volume group member of a DR protection group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DrProtectionGroupMemberVolumeGroup object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.DrProtectionGroupMemberVolumeGroup.member_type` attribute
        of this class is ``VOLUME_GROUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this DrProtectionGroupMemberVolumeGroup.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this DrProtectionGroupMemberVolumeGroup.
            Allowed values for this property are: "COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "AUTONOMOUS_CONTAINER_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM", "OKE_CLUSTER", "OBJECT_STORAGE_BUCKET"
        :type member_type: str

        :param destination_backup_policy_id:
            The value to assign to the destination_backup_policy_id property of this DrProtectionGroupMemberVolumeGroup.
        :type destination_backup_policy_id: str

        :param source_volume_to_destination_encryption_key_mappings:
            The value to assign to the source_volume_to_destination_encryption_key_mappings property of this DrProtectionGroupMemberVolumeGroup.
        :type source_volume_to_destination_encryption_key_mappings: list[oci.disaster_recovery.models.SourceVolumeToDestinationEncryptionKeyMapping]

        :param common_destination_key:
            The value to assign to the common_destination_key property of this DrProtectionGroupMemberVolumeGroup.
        :type common_destination_key: oci.disaster_recovery.models.VaultAndEncryptionKey

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str',
            'destination_backup_policy_id': 'str',
            'source_volume_to_destination_encryption_key_mappings': 'list[SourceVolumeToDestinationEncryptionKeyMapping]',
            'common_destination_key': 'VaultAndEncryptionKey'
        }
        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType',
            'destination_backup_policy_id': 'destinationBackupPolicyId',
            'source_volume_to_destination_encryption_key_mappings': 'sourceVolumeToDestinationEncryptionKeyMappings',
            'common_destination_key': 'commonDestinationKey'
        }
        self._member_id = None
        self._member_type = None
        self._destination_backup_policy_id = None
        self._source_volume_to_destination_encryption_key_mappings = None
        self._common_destination_key = None
        self._member_type = 'VOLUME_GROUP'

    @property
    def destination_backup_policy_id(self):
        """
        Gets the destination_backup_policy_id of this DrProtectionGroupMemberVolumeGroup.
        The OCID of the backup policy to use in the destination region. This policy will be used to create backups for this volume group after it moves the destination region.

        Example: `ocid1.volumebackuppolicy.oc1..uniqueID`


        :return: The destination_backup_policy_id of this DrProtectionGroupMemberVolumeGroup.
        :rtype: str
        """
        return self._destination_backup_policy_id

    @destination_backup_policy_id.setter
    def destination_backup_policy_id(self, destination_backup_policy_id):
        """
        Sets the destination_backup_policy_id of this DrProtectionGroupMemberVolumeGroup.
        The OCID of the backup policy to use in the destination region. This policy will be used to create backups for this volume group after it moves the destination region.

        Example: `ocid1.volumebackuppolicy.oc1..uniqueID`


        :param destination_backup_policy_id: The destination_backup_policy_id of this DrProtectionGroupMemberVolumeGroup.
        :type: str
        """
        self._destination_backup_policy_id = destination_backup_policy_id

    @property
    def source_volume_to_destination_encryption_key_mappings(self):
        """
        Gets the source_volume_to_destination_encryption_key_mappings of this DrProtectionGroupMemberVolumeGroup.
        A list of mappings between source volume IDs in the volume group and customer-managed encryption keys in the
        destination region which will be used to encrypt the volume after it moves to the destination region.

        If you add the entry for source volumes and its corresponding vault and encryption keys here, you can not use
        'commonDestinationKey' for encrypting all volumes with common encryption key. Similarly, if you specify common
        vault and encryption key using 'commonDestinationKey', you cannot specify vaults and encryption keys individually
        for each volume using 'sourceVolumeToDestinationEncryptionKeyMappings'.

        An entry for each volume in volume group should be added in this list. The encryption key will not be updated
        for the volumes that are part of volume group but missing in this list.


        :return: The source_volume_to_destination_encryption_key_mappings of this DrProtectionGroupMemberVolumeGroup.
        :rtype: list[oci.disaster_recovery.models.SourceVolumeToDestinationEncryptionKeyMapping]
        """
        return self._source_volume_to_destination_encryption_key_mappings

    @source_volume_to_destination_encryption_key_mappings.setter
    def source_volume_to_destination_encryption_key_mappings(self, source_volume_to_destination_encryption_key_mappings):
        """
        Sets the source_volume_to_destination_encryption_key_mappings of this DrProtectionGroupMemberVolumeGroup.
        A list of mappings between source volume IDs in the volume group and customer-managed encryption keys in the
        destination region which will be used to encrypt the volume after it moves to the destination region.

        If you add the entry for source volumes and its corresponding vault and encryption keys here, you can not use
        'commonDestinationKey' for encrypting all volumes with common encryption key. Similarly, if you specify common
        vault and encryption key using 'commonDestinationKey', you cannot specify vaults and encryption keys individually
        for each volume using 'sourceVolumeToDestinationEncryptionKeyMappings'.

        An entry for each volume in volume group should be added in this list. The encryption key will not be updated
        for the volumes that are part of volume group but missing in this list.


        :param source_volume_to_destination_encryption_key_mappings: The source_volume_to_destination_encryption_key_mappings of this DrProtectionGroupMemberVolumeGroup.
        :type: list[oci.disaster_recovery.models.SourceVolumeToDestinationEncryptionKeyMapping]
        """
        self._source_volume_to_destination_encryption_key_mappings = source_volume_to_destination_encryption_key_mappings

    @property
    def common_destination_key(self):
        """
        Gets the common_destination_key of this DrProtectionGroupMemberVolumeGroup.

        :return: The common_destination_key of this DrProtectionGroupMemberVolumeGroup.
        :rtype: oci.disaster_recovery.models.VaultAndEncryptionKey
        """
        return self._common_destination_key

    @common_destination_key.setter
    def common_destination_key(self, common_destination_key):
        """
        Sets the common_destination_key of this DrProtectionGroupMemberVolumeGroup.

        :param common_destination_key: The common_destination_key of this DrProtectionGroupMemberVolumeGroup.
        :type: oci.disaster_recovery.models.VaultAndEncryptionKey
        """
        self._common_destination_key = common_destination_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
