# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_asset_details import UpdateAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVmwareVmAssetDetails(UpdateAssetDetails):
    """
    The information of VMware VM asset to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVmwareVmAssetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_bridge.models.UpdateVmwareVmAssetDetails.asset_type` attribute
        of this class is ``VMWARE_VM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateVmwareVmAssetDetails.
        :type display_name: str

        :param asset_type:
            The value to assign to the asset_type property of this UpdateVmwareVmAssetDetails.
            Allowed values for this property are: "VMWARE_VM", "VM"
        :type asset_type: str

        :param asset_source_ids:
            The value to assign to the asset_source_ids property of this UpdateVmwareVmAssetDetails.
        :type asset_source_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVmwareVmAssetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVmwareVmAssetDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param compute:
            The value to assign to the compute property of this UpdateVmwareVmAssetDetails.
        :type compute: oci.cloud_bridge.models.ComputeProperties

        :param vm:
            The value to assign to the vm property of this UpdateVmwareVmAssetDetails.
        :type vm: oci.cloud_bridge.models.VmProperties

        :param vmware_vm:
            The value to assign to the vmware_vm property of this UpdateVmwareVmAssetDetails.
        :type vmware_vm: oci.cloud_bridge.models.VmwareVmProperties

        :param vmware_v_center:
            The value to assign to the vmware_v_center property of this UpdateVmwareVmAssetDetails.
        :type vmware_v_center: oci.cloud_bridge.models.VmwareVCenterProperties

        """
        self.swagger_types = {
            'display_name': 'str',
            'asset_type': 'str',
            'asset_source_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'compute': 'ComputeProperties',
            'vm': 'VmProperties',
            'vmware_vm': 'VmwareVmProperties',
            'vmware_v_center': 'VmwareVCenterProperties'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'asset_type': 'assetType',
            'asset_source_ids': 'assetSourceIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'compute': 'compute',
            'vm': 'vm',
            'vmware_vm': 'vmwareVm',
            'vmware_v_center': 'vmwareVCenter'
        }

        self._display_name = None
        self._asset_type = None
        self._asset_source_ids = None
        self._freeform_tags = None
        self._defined_tags = None
        self._compute = None
        self._vm = None
        self._vmware_vm = None
        self._vmware_v_center = None
        self._asset_type = 'VMWARE_VM'

    @property
    def compute(self):
        """
        Gets the compute of this UpdateVmwareVmAssetDetails.

        :return: The compute of this UpdateVmwareVmAssetDetails.
        :rtype: oci.cloud_bridge.models.ComputeProperties
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """
        Sets the compute of this UpdateVmwareVmAssetDetails.

        :param compute: The compute of this UpdateVmwareVmAssetDetails.
        :type: oci.cloud_bridge.models.ComputeProperties
        """
        self._compute = compute

    @property
    def vm(self):
        """
        Gets the vm of this UpdateVmwareVmAssetDetails.

        :return: The vm of this UpdateVmwareVmAssetDetails.
        :rtype: oci.cloud_bridge.models.VmProperties
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """
        Sets the vm of this UpdateVmwareVmAssetDetails.

        :param vm: The vm of this UpdateVmwareVmAssetDetails.
        :type: oci.cloud_bridge.models.VmProperties
        """
        self._vm = vm

    @property
    def vmware_vm(self):
        """
        Gets the vmware_vm of this UpdateVmwareVmAssetDetails.

        :return: The vmware_vm of this UpdateVmwareVmAssetDetails.
        :rtype: oci.cloud_bridge.models.VmwareVmProperties
        """
        return self._vmware_vm

    @vmware_vm.setter
    def vmware_vm(self, vmware_vm):
        """
        Sets the vmware_vm of this UpdateVmwareVmAssetDetails.

        :param vmware_vm: The vmware_vm of this UpdateVmwareVmAssetDetails.
        :type: oci.cloud_bridge.models.VmwareVmProperties
        """
        self._vmware_vm = vmware_vm

    @property
    def vmware_v_center(self):
        """
        Gets the vmware_v_center of this UpdateVmwareVmAssetDetails.

        :return: The vmware_v_center of this UpdateVmwareVmAssetDetails.
        :rtype: oci.cloud_bridge.models.VmwareVCenterProperties
        """
        return self._vmware_v_center

    @vmware_v_center.setter
    def vmware_v_center(self, vmware_v_center):
        """
        Sets the vmware_v_center of this UpdateVmwareVmAssetDetails.

        :param vmware_v_center: The vmware_v_center of this UpdateVmwareVmAssetDetails.
        :type: oci.cloud_bridge.models.VmwareVCenterProperties
        """
        self._vmware_v_center = vmware_v_center

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
