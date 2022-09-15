# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .asset import Asset
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmwareVmAsset(Asset):
    """
    VMware VM type of asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmwareVmAsset object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_bridge.models.VmwareVmAsset.asset_type` attribute
        of this class is ``VMWARE_VM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this VmwareVmAsset.
        :type display_name: str

        :param inventory_id:
            The value to assign to the inventory_id property of this VmwareVmAsset.
        :type inventory_id: str

        :param id:
            The value to assign to the id property of this VmwareVmAsset.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VmwareVmAsset.
        :type compartment_id: str

        :param source_key:
            The value to assign to the source_key property of this VmwareVmAsset.
        :type source_key: str

        :param external_asset_key:
            The value to assign to the external_asset_key property of this VmwareVmAsset.
        :type external_asset_key: str

        :param asset_type:
            The value to assign to the asset_type property of this VmwareVmAsset.
            Allowed values for this property are: "VMWARE_VM", "VM"
        :type asset_type: str

        :param time_created:
            The value to assign to the time_created property of this VmwareVmAsset.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this VmwareVmAsset.
        :type time_updated: datetime

        :param asset_source_ids:
            The value to assign to the asset_source_ids property of this VmwareVmAsset.
        :type asset_source_ids: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VmwareVmAsset.
            Allowed values for this property are: "ACTIVE", "DELETED"
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VmwareVmAsset.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VmwareVmAsset.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VmwareVmAsset.
        :type system_tags: dict(str, dict(str, object))

        :param compute:
            The value to assign to the compute property of this VmwareVmAsset.
        :type compute: oci.cloud_bridge.models.ComputeProperties

        :param vm:
            The value to assign to the vm property of this VmwareVmAsset.
        :type vm: oci.cloud_bridge.models.VmProperties

        :param vmware_vm:
            The value to assign to the vmware_vm property of this VmwareVmAsset.
        :type vmware_vm: oci.cloud_bridge.models.VmwareVmProperties

        :param vmware_v_center:
            The value to assign to the vmware_v_center property of this VmwareVmAsset.
        :type vmware_v_center: oci.cloud_bridge.models.VmwareVCenterProperties

        """
        self.swagger_types = {
            'display_name': 'str',
            'inventory_id': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'source_key': 'str',
            'external_asset_key': 'str',
            'asset_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'asset_source_ids': 'list[str]',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'compute': 'ComputeProperties',
            'vm': 'VmProperties',
            'vmware_vm': 'VmwareVmProperties',
            'vmware_v_center': 'VmwareVCenterProperties'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'inventory_id': 'inventoryId',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'source_key': 'sourceKey',
            'external_asset_key': 'externalAssetKey',
            'asset_type': 'assetType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'asset_source_ids': 'assetSourceIds',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'compute': 'compute',
            'vm': 'vm',
            'vmware_vm': 'vmwareVm',
            'vmware_v_center': 'vmwareVCenter'
        }

        self._display_name = None
        self._inventory_id = None
        self._id = None
        self._compartment_id = None
        self._source_key = None
        self._external_asset_key = None
        self._asset_type = None
        self._time_created = None
        self._time_updated = None
        self._asset_source_ids = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._compute = None
        self._vm = None
        self._vmware_vm = None
        self._vmware_v_center = None
        self._asset_type = 'VMWARE_VM'

    @property
    def compute(self):
        """
        Gets the compute of this VmwareVmAsset.

        :return: The compute of this VmwareVmAsset.
        :rtype: oci.cloud_bridge.models.ComputeProperties
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """
        Sets the compute of this VmwareVmAsset.

        :param compute: The compute of this VmwareVmAsset.
        :type: oci.cloud_bridge.models.ComputeProperties
        """
        self._compute = compute

    @property
    def vm(self):
        """
        Gets the vm of this VmwareVmAsset.

        :return: The vm of this VmwareVmAsset.
        :rtype: oci.cloud_bridge.models.VmProperties
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """
        Sets the vm of this VmwareVmAsset.

        :param vm: The vm of this VmwareVmAsset.
        :type: oci.cloud_bridge.models.VmProperties
        """
        self._vm = vm

    @property
    def vmware_vm(self):
        """
        Gets the vmware_vm of this VmwareVmAsset.

        :return: The vmware_vm of this VmwareVmAsset.
        :rtype: oci.cloud_bridge.models.VmwareVmProperties
        """
        return self._vmware_vm

    @vmware_vm.setter
    def vmware_vm(self, vmware_vm):
        """
        Sets the vmware_vm of this VmwareVmAsset.

        :param vmware_vm: The vmware_vm of this VmwareVmAsset.
        :type: oci.cloud_bridge.models.VmwareVmProperties
        """
        self._vmware_vm = vmware_vm

    @property
    def vmware_v_center(self):
        """
        Gets the vmware_v_center of this VmwareVmAsset.

        :return: The vmware_v_center of this VmwareVmAsset.
        :rtype: oci.cloud_bridge.models.VmwareVCenterProperties
        """
        return self._vmware_v_center

    @vmware_v_center.setter
    def vmware_v_center(self, vmware_v_center):
        """
        Sets the vmware_v_center of this VmwareVmAsset.

        :param vmware_v_center: The vmware_v_center of this VmwareVmAsset.
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
