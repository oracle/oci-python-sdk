# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Zone(object):

    def __init__(self, **kwargs):
        """
        Initializes a new Zone object with values from values from keyword arguments.
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

        """
        self.swagger_types = {
            'name': 'str',
            'zone_type': 'str',
            'compartment_id': 'str',
            'external_masters': 'list[ExternalMaster]',
            'self_uri': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'version': 'str',
            'serial': 'int',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'zone_type': 'zoneType',
            'compartment_id': 'compartmentId',
            'external_masters': 'externalMasters',
            'self_uri': 'self',
            'id': 'id',
            'time_created': 'timeCreated',
            'version': 'version',
            'serial': 'serial',
            'lifecycle_state': 'lifecycleState'
        }

        self._name = None
        self._zone_type = None
        self._compartment_id = None
        self._external_masters = None
        self._self_uri = None
        self._id = None
        self._time_created = None
        self._version = None
        self._serial = None
        self._lifecycle_state = None

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
    def external_masters(self):
        """
        Gets the external_masters of this Zone.
        External master servers for the zone.


        :return: The external_masters of this Zone.
        :rtype: list[ExternalMaster]
        """
        return self._external_masters

    @external_masters.setter
    def external_masters(self, external_masters):
        """
        Sets the external_masters of this Zone.
        External master servers for the zone.


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
        The date and time the image was created in \"YYYY-MM-ddThh:mmZ\" format
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
        The date and time the image was created in \"YYYY-MM-ddThh:mmZ\" format
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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
