# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationAssetSummary(object):
    """
    Summary of the migration asset.
    """

    #: A constant which can be used with the notifications property of a MigrationAssetSummary.
    #: This constant has a value of "OUT_OF_DATE"
    NOTIFICATIONS_OUT_OF_DATE = "OUT_OF_DATE"

    #: A constant which can be used with the notifications property of a MigrationAssetSummary.
    #: This constant has a value of "SOURCE_REMOVED"
    NOTIFICATIONS_SOURCE_REMOVED = "SOURCE_REMOVED"

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationAssetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MigrationAssetSummary.
        :type id: str

        :param type:
            The value to assign to the type property of this MigrationAssetSummary.
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this MigrationAssetSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MigrationAssetSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MigrationAssetSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MigrationAssetSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this MigrationAssetSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MigrationAssetSummary.
        :type time_updated: datetime

        :param migration_id:
            The value to assign to the migration_id property of this MigrationAssetSummary.
        :type migration_id: str

        :param snapshots:
            The value to assign to the snapshots property of this MigrationAssetSummary.
        :type snapshots: dict(str, HydratedVolume)

        :param parent_snapshot:
            The value to assign to the parent_snapshot property of this MigrationAssetSummary.
        :type parent_snapshot: str

        :param snapshot_info:
            The value to assign to the snapshot_info property of this MigrationAssetSummary.
        :type snapshot_info: str

        :param source_asset_data:
            The value to assign to the source_asset_data property of this MigrationAssetSummary.
        :type source_asset_data: dict(str, object)

        :param notifications:
            The value to assign to the notifications property of this MigrationAssetSummary.
            Allowed values for items in this list are: "OUT_OF_DATE", "SOURCE_REMOVED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type notifications: list[str]

        :param source_asset_id:
            The value to assign to the source_asset_id property of this MigrationAssetSummary.
        :type source_asset_id: str

        :param depended_on_by:
            The value to assign to the depended_on_by property of this MigrationAssetSummary.
        :type depended_on_by: list[str]

        :param depends_on:
            The value to assign to the depends_on property of this MigrationAssetSummary.
        :type depends_on: list[str]

        :param replication_schedule_id:
            The value to assign to the replication_schedule_id property of this MigrationAssetSummary.
        :type replication_schedule_id: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this MigrationAssetSummary.
        :type tenancy_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'migration_id': 'str',
            'snapshots': 'dict(str, HydratedVolume)',
            'parent_snapshot': 'str',
            'snapshot_info': 'str',
            'source_asset_data': 'dict(str, object)',
            'notifications': 'list[str]',
            'source_asset_id': 'str',
            'depended_on_by': 'list[str]',
            'depends_on': 'list[str]',
            'replication_schedule_id': 'str',
            'tenancy_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'migration_id': 'migrationId',
            'snapshots': 'snapshots',
            'parent_snapshot': 'parentSnapshot',
            'snapshot_info': 'snapshotInfo',
            'source_asset_data': 'sourceAssetData',
            'notifications': 'notifications',
            'source_asset_id': 'sourceAssetId',
            'depended_on_by': 'dependedOnBy',
            'depends_on': 'dependsOn',
            'replication_schedule_id': 'replicationScheduleId',
            'tenancy_id': 'tenancyId'
        }

        self._id = None
        self._type = None
        self._display_name = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._migration_id = None
        self._snapshots = None
        self._parent_snapshot = None
        self._snapshot_info = None
        self._source_asset_data = None
        self._notifications = None
        self._source_asset_id = None
        self._depended_on_by = None
        self._depends_on = None
        self._replication_schedule_id = None
        self._tenancy_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MigrationAssetSummary.
        The asset ID generated by the mirgration service. It is used in the migration service pipeline.


        :return: The id of this MigrationAssetSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MigrationAssetSummary.
        The asset ID generated by the mirgration service. It is used in the migration service pipeline.


        :param id: The id of this MigrationAssetSummary.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MigrationAssetSummary.
        The type of asset referenced for an inventory.


        :return: The type of this MigrationAssetSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MigrationAssetSummary.
        The type of asset referenced for an inventory.


        :param type: The type of this MigrationAssetSummary.
        :type: str
        """
        self._type = type

    @property
    def display_name(self):
        """
        Gets the display_name of this MigrationAssetSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this MigrationAssetSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MigrationAssetSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this MigrationAssetSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this MigrationAssetSummary.
        Compartment identifier


        :return: The compartment_id of this MigrationAssetSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MigrationAssetSummary.
        Compartment identifier


        :param compartment_id: The compartment_id of this MigrationAssetSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MigrationAssetSummary.
        The current state of the migration asset.


        :return: The lifecycle_state of this MigrationAssetSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MigrationAssetSummary.
        The current state of the migration asset.


        :param lifecycle_state: The lifecycle_state of this MigrationAssetSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MigrationAssetSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this MigrationAssetSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MigrationAssetSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this MigrationAssetSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MigrationAssetSummary.
        The time when the migration asset was created. An RFC3339 formatted datetime string.


        :return: The time_created of this MigrationAssetSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MigrationAssetSummary.
        The time when the migration asset was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this MigrationAssetSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MigrationAssetSummary.
        The time when the migration asset was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this MigrationAssetSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MigrationAssetSummary.
        The time when the migration asset was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MigrationAssetSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def migration_id(self):
        """
        **[Required]** Gets the migration_id of this MigrationAssetSummary.
        OCID of the associated migration.


        :return: The migration_id of this MigrationAssetSummary.
        :rtype: str
        """
        return self._migration_id

    @migration_id.setter
    def migration_id(self, migration_id):
        """
        Sets the migration_id of this MigrationAssetSummary.
        OCID of the associated migration.


        :param migration_id: The migration_id of this MigrationAssetSummary.
        :type: str
        """
        self._migration_id = migration_id

    @property
    def snapshots(self):
        """
        Gets the snapshots of this MigrationAssetSummary.
        Key-value pair representing disk's ID that is mapped to the OCIDs of replicated/hydration server volume snapshots.
        Example: `{\"bar-key\": \"value\"}`


        :return: The snapshots of this MigrationAssetSummary.
        :rtype: dict(str, HydratedVolume)
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """
        Sets the snapshots of this MigrationAssetSummary.
        Key-value pair representing disk's ID that is mapped to the OCIDs of replicated/hydration server volume snapshots.
        Example: `{\"bar-key\": \"value\"}`


        :param snapshots: The snapshots of this MigrationAssetSummary.
        :type: dict(str, HydratedVolume)
        """
        self._snapshots = snapshots

    @property
    def parent_snapshot(self):
        """
        Gets the parent_snapshot of this MigrationAssetSummary.
        The parent snapshot of the mgration asset to be used by the replication task.


        :return: The parent_snapshot of this MigrationAssetSummary.
        :rtype: str
        """
        return self._parent_snapshot

    @parent_snapshot.setter
    def parent_snapshot(self, parent_snapshot):
        """
        Sets the parent_snapshot of this MigrationAssetSummary.
        The parent snapshot of the mgration asset to be used by the replication task.


        :param parent_snapshot: The parent_snapshot of this MigrationAssetSummary.
        :type: str
        """
        self._parent_snapshot = parent_snapshot

    @property
    def snapshot_info(self):
        """
        Gets the snapshot_info of this MigrationAssetSummary.
        The snapshot information.


        :return: The snapshot_info of this MigrationAssetSummary.
        :rtype: str
        """
        return self._snapshot_info

    @snapshot_info.setter
    def snapshot_info(self, snapshot_info):
        """
        Sets the snapshot_info of this MigrationAssetSummary.
        The snapshot information.


        :param snapshot_info: The snapshot_info of this MigrationAssetSummary.
        :type: str
        """
        self._snapshot_info = snapshot_info

    @property
    def source_asset_data(self):
        """
        Gets the source_asset_data of this MigrationAssetSummary.
        Key-value pair representing asset metadata keys and values scoped to a namespace.
        Example: `{\"bar-key\": \"value\"}`


        :return: The source_asset_data of this MigrationAssetSummary.
        :rtype: dict(str, object)
        """
        return self._source_asset_data

    @source_asset_data.setter
    def source_asset_data(self, source_asset_data):
        """
        Sets the source_asset_data of this MigrationAssetSummary.
        Key-value pair representing asset metadata keys and values scoped to a namespace.
        Example: `{\"bar-key\": \"value\"}`


        :param source_asset_data: The source_asset_data of this MigrationAssetSummary.
        :type: dict(str, object)
        """
        self._source_asset_data = source_asset_data

    @property
    def notifications(self):
        """
        Gets the notifications of this MigrationAssetSummary.
        List of notifications.

        Allowed values for items in this list are: "OUT_OF_DATE", "SOURCE_REMOVED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The notifications of this MigrationAssetSummary.
        :rtype: list[str]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """
        Sets the notifications of this MigrationAssetSummary.
        List of notifications.


        :param notifications: The notifications of this MigrationAssetSummary.
        :type: list[str]
        """
        allowed_values = ["OUT_OF_DATE", "SOURCE_REMOVED"]
        if notifications:
            notifications[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in notifications]
        self._notifications = notifications

    @property
    def source_asset_id(self):
        """
        Gets the source_asset_id of this MigrationAssetSummary.
        OCID that is referenced to an asset, for an inventory.


        :return: The source_asset_id of this MigrationAssetSummary.
        :rtype: str
        """
        return self._source_asset_id

    @source_asset_id.setter
    def source_asset_id(self, source_asset_id):
        """
        Sets the source_asset_id of this MigrationAssetSummary.
        OCID that is referenced to an asset, for an inventory.


        :param source_asset_id: The source_asset_id of this MigrationAssetSummary.
        :type: str
        """
        self._source_asset_id = source_asset_id

    @property
    def depended_on_by(self):
        """
        Gets the depended_on_by of this MigrationAssetSummary.
        List of migration assets that depend on this asset.


        :return: The depended_on_by of this MigrationAssetSummary.
        :rtype: list[str]
        """
        return self._depended_on_by

    @depended_on_by.setter
    def depended_on_by(self, depended_on_by):
        """
        Sets the depended_on_by of this MigrationAssetSummary.
        List of migration assets that depend on this asset.


        :param depended_on_by: The depended_on_by of this MigrationAssetSummary.
        :type: list[str]
        """
        self._depended_on_by = depended_on_by

    @property
    def depends_on(self):
        """
        Gets the depends_on of this MigrationAssetSummary.
        List of migration assets that depend on this asset.


        :return: The depends_on of this MigrationAssetSummary.
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """
        Sets the depends_on of this MigrationAssetSummary.
        List of migration assets that depend on this asset.


        :param depends_on: The depends_on of this MigrationAssetSummary.
        :type: list[str]
        """
        self._depends_on = depends_on

    @property
    def replication_schedule_id(self):
        """
        Gets the replication_schedule_id of this MigrationAssetSummary.
        Replication schedule identifier


        :return: The replication_schedule_id of this MigrationAssetSummary.
        :rtype: str
        """
        return self._replication_schedule_id

    @replication_schedule_id.setter
    def replication_schedule_id(self, replication_schedule_id):
        """
        Sets the replication_schedule_id of this MigrationAssetSummary.
        Replication schedule identifier


        :param replication_schedule_id: The replication_schedule_id of this MigrationAssetSummary.
        :type: str
        """
        self._replication_schedule_id = replication_schedule_id

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this MigrationAssetSummary.
        Tenancy Identifier


        :return: The tenancy_id of this MigrationAssetSummary.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this MigrationAssetSummary.
        Tenancy Identifier


        :param tenancy_id: The tenancy_id of this MigrationAssetSummary.
        :type: str
        """
        self._tenancy_id = tenancy_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
