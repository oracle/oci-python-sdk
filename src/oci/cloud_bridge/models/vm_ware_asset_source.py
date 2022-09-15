# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .asset_source import AssetSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmWareAssetSource(AssetSource):
    """
    Description of an asset source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmWareAssetSource object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_bridge.models.VmWareAssetSource.type` attribute
        of this class is ``VMWARE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VmWareAssetSource.
            Allowed values for this property are: "VMWARE"
        :type type: str

        :param id:
            The value to assign to the id property of this VmWareAssetSource.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VmWareAssetSource.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this VmWareAssetSource.
        :type display_name: str

        :param environment_id:
            The value to assign to the environment_id property of this VmWareAssetSource.
        :type environment_id: str

        :param inventory_id:
            The value to assign to the inventory_id property of this VmWareAssetSource.
        :type inventory_id: str

        :param assets_compartment_id:
            The value to assign to the assets_compartment_id property of this VmWareAssetSource.
        :type assets_compartment_id: str

        :param discovery_schedule_id:
            The value to assign to the discovery_schedule_id property of this VmWareAssetSource.
        :type discovery_schedule_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VmWareAssetSource.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this VmWareAssetSource.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this VmWareAssetSource.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this VmWareAssetSource.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VmWareAssetSource.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VmWareAssetSource.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VmWareAssetSource.
        :type system_tags: dict(str, dict(str, object))

        :param vcenter_endpoint:
            The value to assign to the vcenter_endpoint property of this VmWareAssetSource.
        :type vcenter_endpoint: str

        :param discovery_credentials:
            The value to assign to the discovery_credentials property of this VmWareAssetSource.
        :type discovery_credentials: oci.cloud_bridge.models.AssetSourceCredentials

        :param replication_credentials:
            The value to assign to the replication_credentials property of this VmWareAssetSource.
        :type replication_credentials: oci.cloud_bridge.models.AssetSourceCredentials

        :param are_historical_metrics_collected:
            The value to assign to the are_historical_metrics_collected property of this VmWareAssetSource.
        :type are_historical_metrics_collected: bool

        :param are_realtime_metrics_collected:
            The value to assign to the are_realtime_metrics_collected property of this VmWareAssetSource.
        :type are_realtime_metrics_collected: bool

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'environment_id': 'str',
            'inventory_id': 'str',
            'assets_compartment_id': 'str',
            'discovery_schedule_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'vcenter_endpoint': 'str',
            'discovery_credentials': 'AssetSourceCredentials',
            'replication_credentials': 'AssetSourceCredentials',
            'are_historical_metrics_collected': 'bool',
            'are_realtime_metrics_collected': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'environment_id': 'environmentId',
            'inventory_id': 'inventoryId',
            'assets_compartment_id': 'assetsCompartmentId',
            'discovery_schedule_id': 'discoveryScheduleId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'vcenter_endpoint': 'vcenterEndpoint',
            'discovery_credentials': 'discoveryCredentials',
            'replication_credentials': 'replicationCredentials',
            'are_historical_metrics_collected': 'areHistoricalMetricsCollected',
            'are_realtime_metrics_collected': 'areRealtimeMetricsCollected'
        }

        self._type = None
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._environment_id = None
        self._inventory_id = None
        self._assets_compartment_id = None
        self._discovery_schedule_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._vcenter_endpoint = None
        self._discovery_credentials = None
        self._replication_credentials = None
        self._are_historical_metrics_collected = None
        self._are_realtime_metrics_collected = None
        self._type = 'VMWARE'

    @property
    def vcenter_endpoint(self):
        """
        **[Required]** Gets the vcenter_endpoint of this VmWareAssetSource.
        Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```


        :return: The vcenter_endpoint of this VmWareAssetSource.
        :rtype: str
        """
        return self._vcenter_endpoint

    @vcenter_endpoint.setter
    def vcenter_endpoint(self, vcenter_endpoint):
        """
        Sets the vcenter_endpoint of this VmWareAssetSource.
        Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```


        :param vcenter_endpoint: The vcenter_endpoint of this VmWareAssetSource.
        :type: str
        """
        self._vcenter_endpoint = vcenter_endpoint

    @property
    def discovery_credentials(self):
        """
        **[Required]** Gets the discovery_credentials of this VmWareAssetSource.

        :return: The discovery_credentials of this VmWareAssetSource.
        :rtype: oci.cloud_bridge.models.AssetSourceCredentials
        """
        return self._discovery_credentials

    @discovery_credentials.setter
    def discovery_credentials(self, discovery_credentials):
        """
        Sets the discovery_credentials of this VmWareAssetSource.

        :param discovery_credentials: The discovery_credentials of this VmWareAssetSource.
        :type: oci.cloud_bridge.models.AssetSourceCredentials
        """
        self._discovery_credentials = discovery_credentials

    @property
    def replication_credentials(self):
        """
        Gets the replication_credentials of this VmWareAssetSource.

        :return: The replication_credentials of this VmWareAssetSource.
        :rtype: oci.cloud_bridge.models.AssetSourceCredentials
        """
        return self._replication_credentials

    @replication_credentials.setter
    def replication_credentials(self, replication_credentials):
        """
        Sets the replication_credentials of this VmWareAssetSource.

        :param replication_credentials: The replication_credentials of this VmWareAssetSource.
        :type: oci.cloud_bridge.models.AssetSourceCredentials
        """
        self._replication_credentials = replication_credentials

    @property
    def are_historical_metrics_collected(self):
        """
        Gets the are_historical_metrics_collected of this VmWareAssetSource.
        Flag indicating whether historical metrics are collected for assets, originating from this asset source.


        :return: The are_historical_metrics_collected of this VmWareAssetSource.
        :rtype: bool
        """
        return self._are_historical_metrics_collected

    @are_historical_metrics_collected.setter
    def are_historical_metrics_collected(self, are_historical_metrics_collected):
        """
        Sets the are_historical_metrics_collected of this VmWareAssetSource.
        Flag indicating whether historical metrics are collected for assets, originating from this asset source.


        :param are_historical_metrics_collected: The are_historical_metrics_collected of this VmWareAssetSource.
        :type: bool
        """
        self._are_historical_metrics_collected = are_historical_metrics_collected

    @property
    def are_realtime_metrics_collected(self):
        """
        Gets the are_realtime_metrics_collected of this VmWareAssetSource.
        Flag indicating whether real-time metrics are collected for assets, originating from this asset source.


        :return: The are_realtime_metrics_collected of this VmWareAssetSource.
        :rtype: bool
        """
        return self._are_realtime_metrics_collected

    @are_realtime_metrics_collected.setter
    def are_realtime_metrics_collected(self, are_realtime_metrics_collected):
        """
        Sets the are_realtime_metrics_collected of this VmWareAssetSource.
        Flag indicating whether real-time metrics are collected for assets, originating from this asset source.


        :param are_realtime_metrics_collected: The are_realtime_metrics_collected of this VmWareAssetSource.
        :type: bool
        """
        self._are_realtime_metrics_collected = are_realtime_metrics_collected

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
