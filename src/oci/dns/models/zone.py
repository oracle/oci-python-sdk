# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180115


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Zone(object):
    """
    A DNS zone.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the zone_type property of a Zone.
    #: This constant has a value of "PRIMARY"
    ZONE_TYPE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the zone_type property of a Zone.
    #: This constant has a value of "SECONDARY"
    ZONE_TYPE_SECONDARY = "SECONDARY"

    #: A constant which can be used with the scope property of a Zone.
    #: This constant has a value of "GLOBAL"
    SCOPE_GLOBAL = "GLOBAL"

    #: A constant which can be used with the scope property of a Zone.
    #: This constant has a value of "PRIVATE"
    SCOPE_PRIVATE = "PRIVATE"

    #: A constant which can be used with the dnssec_state property of a Zone.
    #: This constant has a value of "ENABLED"
    DNSSEC_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the dnssec_state property of a Zone.
    #: This constant has a value of "DISABLED"
    DNSSEC_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a Zone.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Zone.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Zone.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Zone.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Zone.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Zone.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new Zone object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Zone.
        :type name: str

        :param zone_type:
            The value to assign to the zone_type property of this Zone.
            Allowed values for this property are: "PRIMARY", "SECONDARY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type zone_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Zone.
        :type compartment_id: str

        :param view_id:
            The value to assign to the view_id property of this Zone.
        :type view_id: str

        :param scope:
            The value to assign to the scope property of this Zone.
            Allowed values for this property are: "GLOBAL", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scope: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Zone.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Zone.
        :type defined_tags: dict(str, dict(str, object))

        :param dnssec_state:
            The value to assign to the dnssec_state property of this Zone.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type dnssec_state: str

        :param external_masters:
            The value to assign to the external_masters property of this Zone.
        :type external_masters: list[oci.dns.models.ExternalMaster]

        :param external_downstreams:
            The value to assign to the external_downstreams property of this Zone.
        :type external_downstreams: list[oci.dns.models.ExternalDownstream]

        :param self_uri:
            The value to assign to the self_uri property of this Zone.
        :type self_uri: str

        :param id:
            The value to assign to the id property of this Zone.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this Zone.
        :type time_created: datetime

        :param version:
            The value to assign to the version property of this Zone.
        :type version: str

        :param serial:
            The value to assign to the serial property of this Zone.
        :type serial: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Zone.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param is_protected:
            The value to assign to the is_protected property of this Zone.
        :type is_protected: bool

        :param dnssec_config:
            The value to assign to the dnssec_config property of this Zone.
        :type dnssec_config: oci.dns.models.DnssecConfig

        :param nameservers:
            The value to assign to the nameservers property of this Zone.
        :type nameservers: list[oci.dns.models.Nameserver]

        :param zone_transfer_servers:
            The value to assign to the zone_transfer_servers property of this Zone.
        :type zone_transfer_servers: list[oci.dns.models.ZoneTransferServer]

        """
        self.swagger_types = {
            'name': 'str',
            'zone_type': 'str',
            'compartment_id': 'str',
            'view_id': 'str',
            'scope': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'dnssec_state': 'str',
            'external_masters': 'list[ExternalMaster]',
            'external_downstreams': 'list[ExternalDownstream]',
            'self_uri': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'version': 'str',
            'serial': 'int',
            'lifecycle_state': 'str',
            'is_protected': 'bool',
            'dnssec_config': 'DnssecConfig',
            'nameservers': 'list[Nameserver]',
            'zone_transfer_servers': 'list[ZoneTransferServer]'
        }
        self.attribute_map = {
            'name': 'name',
            'zone_type': 'zoneType',
            'compartment_id': 'compartmentId',
            'view_id': 'viewId',
            'scope': 'scope',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'dnssec_state': 'dnssecState',
            'external_masters': 'externalMasters',
            'external_downstreams': 'externalDownstreams',
            'self_uri': 'self',
            'id': 'id',
            'time_created': 'timeCreated',
            'version': 'version',
            'serial': 'serial',
            'lifecycle_state': 'lifecycleState',
            'is_protected': 'isProtected',
            'dnssec_config': 'dnssecConfig',
            'nameservers': 'nameservers',
            'zone_transfer_servers': 'zoneTransferServers'
        }
        self._name = None
        self._zone_type = None
        self._compartment_id = None
        self._view_id = None
        self._scope = None
        self._freeform_tags = None
        self._defined_tags = None
        self._dnssec_state = None
        self._external_masters = None
        self._external_downstreams = None
        self._self_uri = None
        self._id = None
        self._time_created = None
        self._version = None
        self._serial = None
        self._lifecycle_state = None
        self._is_protected = None
        self._dnssec_config = None
        self._nameservers = None
        self._zone_transfer_servers = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Zone.
        The name of the zone.


        :return: The name of this Zone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Zone.
        The name of the zone.


        :param name: The name of this Zone.
        :type: str
        """
        self._name = name

    @property
    def zone_type(self):
        """
        **[Required]** Gets the zone_type of this Zone.
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL zones.

        Allowed values for this property are: "PRIMARY", "SECONDARY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The zone_type of this Zone.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """
        Sets the zone_type of this Zone.
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL zones.


        :param zone_type: The zone_type of this Zone.
        :type: str
        """
        allowed_values = ["PRIMARY", "SECONDARY"]
        if not value_allowed_none_or_none_sentinel(zone_type, allowed_values):
            zone_type = 'UNKNOWN_ENUM_VALUE'
        self._zone_type = zone_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Zone.
        The OCID of the compartment containing the zone.


        :return: The compartment_id of this Zone.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Zone.
        The OCID of the compartment containing the zone.


        :param compartment_id: The compartment_id of this Zone.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def view_id(self):
        """
        Gets the view_id of this Zone.
        The OCID of the private view containing the zone. This value will
        be null for zones in the global DNS, which are publicly resolvable and
        not part of a private view.


        :return: The view_id of this Zone.
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """
        Sets the view_id of this Zone.
        The OCID of the private view containing the zone. This value will
        be null for zones in the global DNS, which are publicly resolvable and
        not part of a private view.


        :param view_id: The view_id of this Zone.
        :type: str
        """
        self._view_id = view_id

    @property
    def scope(self):
        """
        **[Required]** Gets the scope of this Zone.
        The scope of the zone.

        Allowed values for this property are: "GLOBAL", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scope of this Zone.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this Zone.
        The scope of the zone.


        :param scope: The scope of this Zone.
        :type: str
        """
        allowed_values = ["GLOBAL", "PRIVATE"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            scope = 'UNKNOWN_ENUM_VALUE'
        self._scope = scope

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this Zone.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Zone.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Zone.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Zone.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this Zone.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Zone.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Zone.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Zone.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def dnssec_state(self):
        """
        **[Required]** Gets the dnssec_state of this Zone.
        The state of DNSSEC on the zone.

        For DNSSEC to function, every parent zone in the DNS tree up to the top-level domain (or an independent
        trust anchor) must also have DNSSEC correctly set up.
        After enabling DNSSEC, you must add a DS record to the zone's parent zone containing the
        `KskDnssecKeyVersion` data. You can find the DS data in the `dsData` attribute of the `KskDnssecKeyVersion`.
        Then, use the `PromoteZoneDnssecKeyVersion` operation to promote the `KskDnssecKeyVersion`.

        New `KskDnssecKeyVersion`s are generated annually, a week before the existing `KskDnssecKeyVersion`'s expiration.
        To rollover a `KskDnssecKeyVersion`, you must replace the parent zone's DS record containing the old
        `KskDnssecKeyVersion` data with the data from the new `KskDnssecKeyVersion`.

        To remove the old DS record without causing service disruption, wait until the old DS record's TTL has
        expired, and the new DS record has propagated. After the DS replacement has been completed, then the
        `PromoteZoneDnssecKeyVersion` operation must be called.

        Metrics are emitted in the `oci_dns` namespace daily for each `KskDnssecKeyVersion` indicating how many
        days are left until expiration.
        We recommend that you set up alarms and notifications for KskDnssecKeyVersion expiration so that the
        necessary parent zone updates can be made and the `PromoteZoneDnssecKeyVersion` operation can be called.

        Enabling DNSSEC results in additional records in DNS responses which increases their size and can
        cause higher response latency.

        For more information, see `DNSSEC`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Concepts/dnssec.htm

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The dnssec_state of this Zone.
        :rtype: str
        """
        return self._dnssec_state

    @dnssec_state.setter
    def dnssec_state(self, dnssec_state):
        """
        Sets the dnssec_state of this Zone.
        The state of DNSSEC on the zone.

        For DNSSEC to function, every parent zone in the DNS tree up to the top-level domain (or an independent
        trust anchor) must also have DNSSEC correctly set up.
        After enabling DNSSEC, you must add a DS record to the zone's parent zone containing the
        `KskDnssecKeyVersion` data. You can find the DS data in the `dsData` attribute of the `KskDnssecKeyVersion`.
        Then, use the `PromoteZoneDnssecKeyVersion` operation to promote the `KskDnssecKeyVersion`.

        New `KskDnssecKeyVersion`s are generated annually, a week before the existing `KskDnssecKeyVersion`'s expiration.
        To rollover a `KskDnssecKeyVersion`, you must replace the parent zone's DS record containing the old
        `KskDnssecKeyVersion` data with the data from the new `KskDnssecKeyVersion`.

        To remove the old DS record without causing service disruption, wait until the old DS record's TTL has
        expired, and the new DS record has propagated. After the DS replacement has been completed, then the
        `PromoteZoneDnssecKeyVersion` operation must be called.

        Metrics are emitted in the `oci_dns` namespace daily for each `KskDnssecKeyVersion` indicating how many
        days are left until expiration.
        We recommend that you set up alarms and notifications for KskDnssecKeyVersion expiration so that the
        necessary parent zone updates can be made and the `PromoteZoneDnssecKeyVersion` operation can be called.

        Enabling DNSSEC results in additional records in DNS responses which increases their size and can
        cause higher response latency.

        For more information, see `DNSSEC`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Concepts/dnssec.htm


        :param dnssec_state: The dnssec_state of this Zone.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(dnssec_state, allowed_values):
            dnssec_state = 'UNKNOWN_ENUM_VALUE'
        self._dnssec_state = dnssec_state

    @property
    def external_masters(self):
        """
        **[Required]** Gets the external_masters of this Zone.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :return: The external_masters of this Zone.
        :rtype: list[oci.dns.models.ExternalMaster]
        """
        return self._external_masters

    @external_masters.setter
    def external_masters(self, external_masters):
        """
        Sets the external_masters of this Zone.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :param external_masters: The external_masters of this Zone.
        :type: list[oci.dns.models.ExternalMaster]
        """
        self._external_masters = external_masters

    @property
    def external_downstreams(self):
        """
        **[Required]** Gets the external_downstreams of this Zone.
        External secondary servers for the zone.
        This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.


        :return: The external_downstreams of this Zone.
        :rtype: list[oci.dns.models.ExternalDownstream]
        """
        return self._external_downstreams

    @external_downstreams.setter
    def external_downstreams(self, external_downstreams):
        """
        Sets the external_downstreams of this Zone.
        External secondary servers for the zone.
        This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.


        :param external_downstreams: The external_downstreams of this Zone.
        :type: list[oci.dns.models.ExternalDownstream]
        """
        self._external_downstreams = external_downstreams

    @property
    def self_uri(self):
        """
        **[Required]** Gets the self_uri of this Zone.
        The canonical absolute URL of the resource.


        :return: The self_uri of this Zone.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Zone.
        The canonical absolute URL of the resource.


        :param self_uri: The self_uri of this Zone.
        :type: str
        """
        self._self_uri = self_uri

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Zone.
        The OCID of the zone.


        :return: The id of this Zone.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Zone.
        The OCID of the zone.


        :param id: The id of this Zone.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Zone.
        The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format
        with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :return: The time_created of this Zone.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Zone.
        The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format
        with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_created: The time_created of this Zone.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def version(self):
        """
        **[Required]** Gets the version of this Zone.
        Version is the never-repeating, totally-orderable, version of the
        zone, from which the serial field of the zone's SOA record is
        derived.


        :return: The version of this Zone.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Zone.
        Version is the never-repeating, totally-orderable, version of the
        zone, from which the serial field of the zone's SOA record is
        derived.


        :param version: The version of this Zone.
        :type: str
        """
        self._version = version

    @property
    def serial(self):
        """
        **[Required]** Gets the serial of this Zone.
        The current serial of the zone. As seen in the zone's SOA record.


        :return: The serial of this Zone.
        :rtype: int
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this Zone.
        The current serial of the zone. As seen in the zone's SOA record.


        :param serial: The serial of this Zone.
        :type: int
        """
        self._serial = serial

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Zone.
        The current state of the zone resource.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Zone.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Zone.
        The current state of the zone resource.


        :param lifecycle_state: The lifecycle_state of this Zone.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def is_protected(self):
        """
        **[Required]** Gets the is_protected of this Zone.
        A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.


        :return: The is_protected of this Zone.
        :rtype: bool
        """
        return self._is_protected

    @is_protected.setter
    def is_protected(self, is_protected):
        """
        Sets the is_protected of this Zone.
        A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.


        :param is_protected: The is_protected of this Zone.
        :type: bool
        """
        self._is_protected = is_protected

    @property
    def dnssec_config(self):
        """
        Gets the dnssec_config of this Zone.

        :return: The dnssec_config of this Zone.
        :rtype: oci.dns.models.DnssecConfig
        """
        return self._dnssec_config

    @dnssec_config.setter
    def dnssec_config(self, dnssec_config):
        """
        Sets the dnssec_config of this Zone.

        :param dnssec_config: The dnssec_config of this Zone.
        :type: oci.dns.models.DnssecConfig
        """
        self._dnssec_config = dnssec_config

    @property
    def nameservers(self):
        """
        **[Required]** Gets the nameservers of this Zone.
        The authoritative nameservers for the zone.


        :return: The nameservers of this Zone.
        :rtype: list[oci.dns.models.Nameserver]
        """
        return self._nameservers

    @nameservers.setter
    def nameservers(self, nameservers):
        """
        Sets the nameservers of this Zone.
        The authoritative nameservers for the zone.


        :param nameservers: The nameservers of this Zone.
        :type: list[oci.dns.models.Nameserver]
        """
        self._nameservers = nameservers

    @property
    def zone_transfer_servers(self):
        """
        Gets the zone_transfer_servers of this Zone.
        The OCI nameservers that transfer the zone data with external nameservers.


        :return: The zone_transfer_servers of this Zone.
        :rtype: list[oci.dns.models.ZoneTransferServer]
        """
        return self._zone_transfer_servers

    @zone_transfer_servers.setter
    def zone_transfer_servers(self, zone_transfer_servers):
        """
        Sets the zone_transfer_servers of this Zone.
        The OCI nameservers that transfer the zone data with external nameservers.


        :param zone_transfer_servers: The zone_transfer_servers of this Zone.
        :type: list[oci.dns.models.ZoneTransferServer]
        """
        self._zone_transfer_servers = zone_transfer_servers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
