# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .asset_source_summary import AssetSourceSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmWareAssetSourceSummary(AssetSourceSummary):
    """
    Description of an asset source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmWareAssetSourceSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_migrations.models.VmWareAssetSourceSummary.type` attribute
        of this class is ``VMWARE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VmWareAssetSourceSummary.
            Allowed values for this property are: "VMWARE"
        :type type: str

        :param id:
            The value to assign to the id property of this VmWareAssetSourceSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VmWareAssetSourceSummary.
        :type compartment_id: str

        :param environment_id:
            The value to assign to the environment_id property of this VmWareAssetSourceSummary.
        :type environment_id: str

        :param display_name:
            The value to assign to the display_name property of this VmWareAssetSourceSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VmWareAssetSourceSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this VmWareAssetSourceSummary.
        :type lifecycle_details: str

        :param inventory_id:
            The value to assign to the inventory_id property of this VmWareAssetSourceSummary.
        :type inventory_id: str

        :param assets_compartment_id:
            The value to assign to the assets_compartment_id property of this VmWareAssetSourceSummary.
        :type assets_compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this VmWareAssetSourceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this VmWareAssetSourceSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VmWareAssetSourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VmWareAssetSourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VmWareAssetSourceSummary.
        :type system_tags: dict(str, dict(str, object))

        :param vcenter_endpoint:
            The value to assign to the vcenter_endpoint property of this VmWareAssetSourceSummary.
        :type vcenter_endpoint: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'environment_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'inventory_id': 'str',
            'assets_compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'vcenter_endpoint': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'environment_id': 'environmentId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'inventory_id': 'inventoryId',
            'assets_compartment_id': 'assetsCompartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'vcenter_endpoint': 'vcenterEndpoint'
        }

        self._type = None
        self._id = None
        self._compartment_id = None
        self._environment_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._inventory_id = None
        self._assets_compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._vcenter_endpoint = None
        self._type = 'VMWARE'

    @property
    def vcenter_endpoint(self):
        """
        **[Required]** Gets the vcenter_endpoint of this VmWareAssetSourceSummary.
        Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```


        :return: The vcenter_endpoint of this VmWareAssetSourceSummary.
        :rtype: str
        """
        return self._vcenter_endpoint

    @vcenter_endpoint.setter
    def vcenter_endpoint(self, vcenter_endpoint):
        """
        Sets the vcenter_endpoint of this VmWareAssetSourceSummary.
        Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```


        :param vcenter_endpoint: The vcenter_endpoint of this VmWareAssetSourceSummary.
        :type: str
        """
        self._vcenter_endpoint = vcenter_endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
