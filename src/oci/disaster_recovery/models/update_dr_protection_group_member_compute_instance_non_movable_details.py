# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .update_dr_protection_group_member_details import UpdateDrProtectionGroupMemberDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails(UpdateDrProtectionGroupMemberDetails):
    """
    Update properties for a non-movable compute instance member.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.member_type` attribute
        of this class is ``COMPUTE_INSTANCE_NON_MOVABLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
            Allowed values for this property are: "COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM"
        :type member_type: str

        :param is_start_stop_enabled:
            The value to assign to the is_start_stop_enabled property of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :type is_start_stop_enabled: bool

        :param file_system_operations:
            The value to assign to the file_system_operations property of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :type file_system_operations: list[oci.disaster_recovery.models.UpdateComputeInstanceNonMovableFileSystemOperationDetails]

        :param block_volume_operations:
            The value to assign to the block_volume_operations property of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :type block_volume_operations: list[oci.disaster_recovery.models.UpdateComputeInstanceNonMovableBlockVolumeOperationDetails]

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str',
            'is_start_stop_enabled': 'bool',
            'file_system_operations': 'list[UpdateComputeInstanceNonMovableFileSystemOperationDetails]',
            'block_volume_operations': 'list[UpdateComputeInstanceNonMovableBlockVolumeOperationDetails]'
        }

        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType',
            'is_start_stop_enabled': 'isStartStopEnabled',
            'file_system_operations': 'fileSystemOperations',
            'block_volume_operations': 'blockVolumeOperations'
        }

        self._member_id = None
        self._member_type = None
        self._is_start_stop_enabled = None
        self._file_system_operations = None
        self._block_volume_operations = None
        self._member_type = 'COMPUTE_INSTANCE_NON_MOVABLE'

    @property
    def is_start_stop_enabled(self):
        """
        Gets the is_start_stop_enabled of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        A flag indicating whether the non-movable compute instance should be started and stopped during DR operations.
        *Prechecks cannot be executed on stopped instances that are configured to be started.*


        :return: The is_start_stop_enabled of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :rtype: bool
        """
        return self._is_start_stop_enabled

    @is_start_stop_enabled.setter
    def is_start_stop_enabled(self, is_start_stop_enabled):
        """
        Sets the is_start_stop_enabled of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        A flag indicating whether the non-movable compute instance should be started and stopped during DR operations.
        *Prechecks cannot be executed on stopped instances that are configured to be started.*


        :param is_start_stop_enabled: The is_start_stop_enabled of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :type: bool
        """
        self._is_start_stop_enabled = is_start_stop_enabled

    @property
    def file_system_operations(self):
        """
        Gets the file_system_operations of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        A list of operations performed on file systems used by the compute instance.


        :return: The file_system_operations of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :rtype: list[oci.disaster_recovery.models.UpdateComputeInstanceNonMovableFileSystemOperationDetails]
        """
        return self._file_system_operations

    @file_system_operations.setter
    def file_system_operations(self, file_system_operations):
        """
        Sets the file_system_operations of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        A list of operations performed on file systems used by the compute instance.


        :param file_system_operations: The file_system_operations of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :type: list[oci.disaster_recovery.models.UpdateComputeInstanceNonMovableFileSystemOperationDetails]
        """
        self._file_system_operations = file_system_operations

    @property
    def block_volume_operations(self):
        """
        Gets the block_volume_operations of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        A list of operations performed on block volumes used by the compute instance.


        :return: The block_volume_operations of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :rtype: list[oci.disaster_recovery.models.UpdateComputeInstanceNonMovableBlockVolumeOperationDetails]
        """
        return self._block_volume_operations

    @block_volume_operations.setter
    def block_volume_operations(self, block_volume_operations):
        """
        Sets the block_volume_operations of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        A list of operations performed on block volumes used by the compute instance.


        :param block_volume_operations: The block_volume_operations of this UpdateDrProtectionGroupMemberComputeInstanceNonMovableDetails.
        :type: list[oci.disaster_recovery.models.UpdateComputeInstanceNonMovableBlockVolumeOperationDetails]
        """
        self._block_volume_operations = block_volume_operations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
