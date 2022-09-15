# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .asset import Asset
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmAsset(Asset):
    """
    VM type of asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmAsset object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_bridge.models.VmAsset.asset_type` attribute
        of this class is ``VM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this VmAsset.
        :type display_name: str

        :param inventory_id:
            The value to assign to the inventory_id property of this VmAsset.
        :type inventory_id: str

        :param id:
            The value to assign to the id property of this VmAsset.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VmAsset.
        :type compartment_id: str

        :param source_key:
            The value to assign to the source_key property of this VmAsset.
        :type source_key: str

        :param external_asset_key:
            The value to assign to the external_asset_key property of this VmAsset.
        :type external_asset_key: str

        :param asset_type:
            The value to assign to the asset_type property of this VmAsset.
            Allowed values for this property are: "VMWARE_VM", "VM"
        :type asset_type: str

        :param time_created:
            The value to assign to the time_created property of this VmAsset.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this VmAsset.
        :type time_updated: datetime

        :param asset_source_ids:
            The value to assign to the asset_source_ids property of this VmAsset.
        :type asset_source_ids: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VmAsset.
            Allowed values for this property are: "ACTIVE", "DELETED"
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VmAsset.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VmAsset.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VmAsset.
        :type system_tags: dict(str, dict(str, object))

        :param compute:
            The value to assign to the compute property of this VmAsset.
        :type compute: oci.cloud_bridge.models.ComputeProperties

        :param vm:
            The value to assign to the vm property of this VmAsset.
        :type vm: oci.cloud_bridge.models.VmProperties

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
            'vm': 'VmProperties'
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
            'vm': 'vm'
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
        self._asset_type = 'VM'

    @property
    def compute(self):
        """
        Gets the compute of this VmAsset.

        :return: The compute of this VmAsset.
        :rtype: oci.cloud_bridge.models.ComputeProperties
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """
        Sets the compute of this VmAsset.

        :param compute: The compute of this VmAsset.
        :type: oci.cloud_bridge.models.ComputeProperties
        """
        self._compute = compute

    @property
    def vm(self):
        """
        Gets the vm of this VmAsset.

        :return: The vm of this VmAsset.
        :rtype: oci.cloud_bridge.models.VmProperties
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """
        Sets the vm of this VmAsset.

        :param vm: The vm of this VmAsset.
        :type: oci.cloud_bridge.models.VmProperties
        """
        self._vm = vm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
