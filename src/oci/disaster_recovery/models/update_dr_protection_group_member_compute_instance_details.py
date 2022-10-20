# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_dr_protection_group_member_details import UpdateDrProtectionGroupMemberDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrProtectionGroupMemberComputeInstanceDetails(UpdateDrProtectionGroupMemberDetails):
    """
    Update properties for a Compute Instance member.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrProtectionGroupMemberComputeInstanceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.UpdateDrProtectionGroupMemberComputeInstanceDetails.member_type` attribute
        of this class is ``COMPUTE_INSTANCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
            Allowed values for this property are: "COMPUTE_INSTANCE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE"
        :type member_type: str

        :param is_movable:
            The value to assign to the is_movable property of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :type is_movable: bool

        :param vnic_mapping:
            The value to assign to the vnic_mapping property of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :type vnic_mapping: list[oci.disaster_recovery.models.ComputeInstanceVnicMappingDetails]

        :param destination_compartment_id:
            The value to assign to the destination_compartment_id property of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :type destination_compartment_id: str

        :param destination_dedicated_vm_host_id:
            The value to assign to the destination_dedicated_vm_host_id property of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :type destination_dedicated_vm_host_id: str

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str',
            'is_movable': 'bool',
            'vnic_mapping': 'list[ComputeInstanceVnicMappingDetails]',
            'destination_compartment_id': 'str',
            'destination_dedicated_vm_host_id': 'str'
        }

        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType',
            'is_movable': 'isMovable',
            'vnic_mapping': 'vnicMapping',
            'destination_compartment_id': 'destinationCompartmentId',
            'destination_dedicated_vm_host_id': 'destinationDedicatedVmHostId'
        }

        self._member_id = None
        self._member_type = None
        self._is_movable = None
        self._vnic_mapping = None
        self._destination_compartment_id = None
        self._destination_dedicated_vm_host_id = None
        self._member_type = 'COMPUTE_INSTANCE'

    @property
    def is_movable(self):
        """
        Gets the is_movable of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        A flag indicating if this compute instance should be moved during DR operations.

        Example: `false`


        :return: The is_movable of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :rtype: bool
        """
        return self._is_movable

    @is_movable.setter
    def is_movable(self, is_movable):
        """
        Sets the is_movable of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        A flag indicating if this compute instance should be moved during DR operations.

        Example: `false`


        :param is_movable: The is_movable of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :type: bool
        """
        self._is_movable = is_movable

    @property
    def vnic_mapping(self):
        """
        Gets the vnic_mapping of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        A list of Compute Instance VNIC mappings.


        :return: The vnic_mapping of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :rtype: list[oci.disaster_recovery.models.ComputeInstanceVnicMappingDetails]
        """
        return self._vnic_mapping

    @vnic_mapping.setter
    def vnic_mapping(self, vnic_mapping):
        """
        Sets the vnic_mapping of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        A list of Compute Instance VNIC mappings.


        :param vnic_mapping: The vnic_mapping of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :type: list[oci.disaster_recovery.models.ComputeInstanceVnicMappingDetails]
        """
        self._vnic_mapping = vnic_mapping

    @property
    def destination_compartment_id(self):
        """
        Gets the destination_compartment_id of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        The OCID of the compartment for this compute instance in the destination region.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :return: The destination_compartment_id of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :rtype: str
        """
        return self._destination_compartment_id

    @destination_compartment_id.setter
    def destination_compartment_id(self, destination_compartment_id):
        """
        Sets the destination_compartment_id of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        The OCID of the compartment for this compute instance in the destination region.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :param destination_compartment_id: The destination_compartment_id of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :type: str
        """
        self._destination_compartment_id = destination_compartment_id

    @property
    def destination_dedicated_vm_host_id(self):
        """
        Gets the destination_dedicated_vm_host_id of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        The OCID of the dedicated VM Host in the destination region where this compute instance
        should be launched

        Example: `ocid1.dedicatedvmhost.oc1.iad.exampleocid2`


        :return: The destination_dedicated_vm_host_id of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :rtype: str
        """
        return self._destination_dedicated_vm_host_id

    @destination_dedicated_vm_host_id.setter
    def destination_dedicated_vm_host_id(self, destination_dedicated_vm_host_id):
        """
        Sets the destination_dedicated_vm_host_id of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        The OCID of the dedicated VM Host in the destination region where this compute instance
        should be launched

        Example: `ocid1.dedicatedvmhost.oc1.iad.exampleocid2`


        :param destination_dedicated_vm_host_id: The destination_dedicated_vm_host_id of this UpdateDrProtectionGroupMemberComputeInstanceDetails.
        :type: str
        """
        self._destination_dedicated_vm_host_id = destination_dedicated_vm_host_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
