# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


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

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Zone.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Zone.
        :type defined_tags: dict(str, dict(str, object))

        :param external_masters:
            The value to assign to the external_masters property of this Zone.
        :type external_masters: list[ExternalMaster]

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
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param nameservers:
            The value to assign to the nameservers property of this Zone.
        :type nameservers: list[Nameserver]

        """
        self.swagger_types = {
            'name': 'str',
            'zone_type': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'external_masters': 'list[ExternalMaster]',
            'self_uri': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'version': 'str',
            'serial': 'int',
            'lifecycle_state': 'str',
            'nameservers': 'list[Nameserver]'
        }

        self.attribute_map = {
            'name': 'name',
            'zone_type': 'zoneType',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'external_masters': 'externalMasters',
            'self_uri': 'self',
            'id': 'id',
            'time_created': 'timeCreated',
            'version': 'version',
            'serial': 'serial',
            'lifecycle_state': 'lifecycleState',
            'nameservers': 'nameservers'
        }

        self._name = None
        self._zone_type = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._external_masters = None
        self._self_uri = None
        self._id = None
        self._time_created = None
        self._version = None
        self._serial = None
        self._lifecycle_state = None
        self._nameservers = None

    @property
    def name(self):
        """
        Gets the name of this Zone.
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
        Gets the zone_type of this Zone.
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`.

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
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`.


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
        Gets the compartment_id of this Zone.
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
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Zone.
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
        Gets the defined_tags of this Zone.
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
    def external_masters(self):
        """
        Gets the external_masters of this Zone.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :return: The external_masters of this Zone.
        :rtype: list[ExternalMaster]
        """
        return self._external_masters

    @external_masters.setter
    def external_masters(self, external_masters):
        """
        Sets the external_masters of this Zone.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :param external_masters: The external_masters of this Zone.
        :type: list[ExternalMaster]
        """
        self._external_masters = external_masters

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Zone.
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
        Gets the id of this Zone.
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
        Gets the time_created of this Zone.
        The date and time the resource was created in \"YYYY-MM-ddThh:mmZ\" format
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
        The date and time the resource was created in \"YYYY-MM-ddThh:mmZ\" format
        with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_created: The time_created of this Zone.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def version(self):
        """
        Gets the version of this Zone.
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
        Gets the serial of this Zone.
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
        Gets the lifecycle_state of this Zone.
        The current state of the zone resource.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
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
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def nameservers(self):
        """
        Gets the nameservers of this Zone.
        The authoritative nameservers for the zone.


        :return: The nameservers of this Zone.
        :rtype: list[Nameserver]
        """
        return self._nameservers

    @nameservers.setter
    def nameservers(self, nameservers):
        """
        Sets the nameservers of this Zone.
        The authoritative nameservers for the zone.


        :param nameservers: The nameservers of this Zone.
        :type: list[Nameserver]
        """
        self._nameservers = nameservers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
