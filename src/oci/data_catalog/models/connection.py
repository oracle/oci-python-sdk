# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Connection(object):
    """
    Detailed representation of a connection to a data asset, minus any sensitive properties.
    """

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new Connection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Connection.
        :type key: str

        :param description:
            The value to assign to the description property of this Connection.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this Connection.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this Connection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Connection.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this Connection.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this Connection.
        :type updated_by_id: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this Connection.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertyGetUsage]

        :param properties:
            The value to assign to the properties property of this Connection.
        :type properties: dict(str, dict(str, str))

        :param external_key:
            The value to assign to the external_key property of this Connection.
        :type external_key: str

        :param time_status_updated:
            The value to assign to the time_status_updated property of this Connection.
        :type time_status_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Connection.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param is_default:
            The value to assign to the is_default property of this Connection.
        :type is_default: bool

        :param data_asset_key:
            The value to assign to the data_asset_key property of this Connection.
        :type data_asset_key: str

        :param type_key:
            The value to assign to the type_key property of this Connection.
        :type type_key: str

        :param uri:
            The value to assign to the uri property of this Connection.
        :type uri: str

        """
        self.swagger_types = {
            'key': 'str',
            'description': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'custom_property_members': 'list[CustomPropertyGetUsage]',
            'properties': 'dict(str, dict(str, str))',
            'external_key': 'str',
            'time_status_updated': 'datetime',
            'lifecycle_state': 'str',
            'is_default': 'bool',
            'data_asset_key': 'str',
            'type_key': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'description': 'description',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'custom_property_members': 'customPropertyMembers',
            'properties': 'properties',
            'external_key': 'externalKey',
            'time_status_updated': 'timeStatusUpdated',
            'lifecycle_state': 'lifecycleState',
            'is_default': 'isDefault',
            'data_asset_key': 'dataAssetKey',
            'type_key': 'typeKey',
            'uri': 'uri'
        }

        self._key = None
        self._description = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._custom_property_members = None
        self._properties = None
        self._external_key = None
        self._time_status_updated = None
        self._lifecycle_state = None
        self._is_default = None
        self._data_asset_key = None
        self._type_key = None
        self._uri = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Connection.
        Unique connection key that is immutable.


        :return: The key of this Connection.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Connection.
        Unique connection key that is immutable.


        :param key: The key of this Connection.
        :type: str
        """
        self._key = key

    @property
    def description(self):
        """
        Gets the description of this Connection.
        A description of the connection.


        :return: The description of this Connection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Connection.
        A description of the connection.


        :param description: The description of this Connection.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this Connection.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Connection.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Connection.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Connection.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this Connection.
        The date and time the connection was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Connection.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Connection.
        The date and time the connection was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Connection.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Connection.
        The last time that any change was made to the connection. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Connection.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Connection.
        The last time that any change was made to the connection. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Connection.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this Connection.
        OCID of the user who created the connection.


        :return: The created_by_id of this Connection.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this Connection.
        OCID of the user who created the connection.


        :param created_by_id: The created_by_id of this Connection.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this Connection.
        OCID of the user who modified the connection.


        :return: The updated_by_id of this Connection.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this Connection.
        OCID of the user who modified the connection.


        :param updated_by_id: The updated_by_id of this Connection.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def custom_property_members(self):
        """
        Gets the custom_property_members of this Connection.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this Connection.
        :rtype: list[oci.data_catalog.models.CustomPropertyGetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this Connection.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this Connection.
        :type: list[oci.data_catalog.models.CustomPropertyGetUsage]
        """
        self._custom_property_members = custom_property_members

    @property
    def properties(self):
        """
        Gets the properties of this Connection.
        A map of maps that contains the properties which are specific to the connection type. Each connection type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        connections have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`


        :return: The properties of this Connection.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Connection.
        A map of maps that contains the properties which are specific to the connection type. Each connection type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        connections have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`


        :param properties: The properties of this Connection.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    @property
    def external_key(self):
        """
        Gets the external_key of this Connection.
        Unique external key of this object from the source system.


        :return: The external_key of this Connection.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this Connection.
        Unique external key of this object from the source system.


        :param external_key: The external_key of this Connection.
        :type: str
        """
        self._external_key = external_key

    @property
    def time_status_updated(self):
        """
        Gets the time_status_updated of this Connection.
        Time that the connections status was last updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_status_updated of this Connection.
        :rtype: datetime
        """
        return self._time_status_updated

    @time_status_updated.setter
    def time_status_updated(self, time_status_updated):
        """
        Sets the time_status_updated of this Connection.
        Time that the connections status was last updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_status_updated: The time_status_updated of this Connection.
        :type: datetime
        """
        self._time_status_updated = time_status_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Connection.
        The current state of the connection.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Connection.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Connection.
        The current state of the connection.


        :param lifecycle_state: The lifecycle_state of this Connection.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def is_default(self):
        """
        Gets the is_default of this Connection.
        Indicates whether this connection is the default connection.


        :return: The is_default of this Connection.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this Connection.
        Indicates whether this connection is the default connection.


        :param is_default: The is_default of this Connection.
        :type: bool
        """
        self._is_default = is_default

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this Connection.
        Unique key of the parent data asset.


        :return: The data_asset_key of this Connection.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this Connection.
        Unique key of the parent data asset.


        :param data_asset_key: The data_asset_key of this Connection.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def type_key(self):
        """
        Gets the type_key of this Connection.
        The key of the object type. Type key's can be found via the '/types' endpoint.


        :return: The type_key of this Connection.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this Connection.
        The key of the object type. Type key's can be found via the '/types' endpoint.


        :param type_key: The type_key of this Connection.
        :type: str
        """
        self._type_key = type_key

    @property
    def uri(self):
        """
        Gets the uri of this Connection.
        URI to the connection instance in the API.


        :return: The uri of this Connection.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Connection.
        URI to the connection instance in the API.


        :param uri: The uri of this Connection.
        :type: str
        """
        self._uri = uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
