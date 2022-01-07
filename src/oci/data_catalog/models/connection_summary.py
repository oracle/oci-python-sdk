# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionSummary(object):
    """
    Summary representation of a connection to a data asset.
    """

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ConnectionSummary.
        :type key: str

        :param description:
            The value to assign to the description property of this ConnectionSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this ConnectionSummary.
        :type display_name: str

        :param data_asset_key:
            The value to assign to the data_asset_key property of this ConnectionSummary.
        :type data_asset_key: str

        :param type_key:
            The value to assign to the type_key property of this ConnectionSummary.
        :type type_key: str

        :param uri:
            The value to assign to the uri property of this ConnectionSummary.
        :type uri: str

        :param external_key:
            The value to assign to the external_key property of this ConnectionSummary.
        :type external_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConnectionSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param is_default:
            The value to assign to the is_default property of this ConnectionSummary.
        :type is_default: bool

        :param time_created:
            The value to assign to the time_created property of this ConnectionSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'key': 'str',
            'description': 'str',
            'display_name': 'str',
            'data_asset_key': 'str',
            'type_key': 'str',
            'uri': 'str',
            'external_key': 'str',
            'lifecycle_state': 'str',
            'is_default': 'bool',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'key': 'key',
            'description': 'description',
            'display_name': 'displayName',
            'data_asset_key': 'dataAssetKey',
            'type_key': 'typeKey',
            'uri': 'uri',
            'external_key': 'externalKey',
            'lifecycle_state': 'lifecycleState',
            'is_default': 'isDefault',
            'time_created': 'timeCreated'
        }

        self._key = None
        self._description = None
        self._display_name = None
        self._data_asset_key = None
        self._type_key = None
        self._uri = None
        self._external_key = None
        self._lifecycle_state = None
        self._is_default = None
        self._time_created = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this ConnectionSummary.
        Unique connection key that is immutable.


        :return: The key of this ConnectionSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ConnectionSummary.
        Unique connection key that is immutable.


        :param key: The key of this ConnectionSummary.
        :type: str
        """
        self._key = key

    @property
    def description(self):
        """
        Gets the description of this ConnectionSummary.
        A description of the connection.


        :return: The description of this ConnectionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConnectionSummary.
        A description of the connection.


        :param description: The description of this ConnectionSummary.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this ConnectionSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this ConnectionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ConnectionSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ConnectionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this ConnectionSummary.
        The unique key of the parent data asset.


        :return: The data_asset_key of this ConnectionSummary.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this ConnectionSummary.
        The unique key of the parent data asset.


        :param data_asset_key: The data_asset_key of this ConnectionSummary.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def type_key(self):
        """
        Gets the type_key of this ConnectionSummary.
        The key of the object type. Type key's can be found via the '/types' endpoint.


        :return: The type_key of this ConnectionSummary.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this ConnectionSummary.
        The key of the object type. Type key's can be found via the '/types' endpoint.


        :param type_key: The type_key of this ConnectionSummary.
        :type: str
        """
        self._type_key = type_key

    @property
    def uri(self):
        """
        Gets the uri of this ConnectionSummary.
        URI to the connection instance in the API.


        :return: The uri of this ConnectionSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ConnectionSummary.
        URI to the connection instance in the API.


        :param uri: The uri of this ConnectionSummary.
        :type: str
        """
        self._uri = uri

    @property
    def external_key(self):
        """
        Gets the external_key of this ConnectionSummary.
        Unique external key for this object as defined in the source systems.


        :return: The external_key of this ConnectionSummary.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this ConnectionSummary.
        Unique external key for this object as defined in the source systems.


        :param external_key: The external_key of this ConnectionSummary.
        :type: str
        """
        self._external_key = external_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ConnectionSummary.
        The current state of the connection.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ConnectionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConnectionSummary.
        The current state of the connection.


        :param lifecycle_state: The lifecycle_state of this ConnectionSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def is_default(self):
        """
        Gets the is_default of this ConnectionSummary.
        Indicates whether this connection is the default connection.


        :return: The is_default of this ConnectionSummary.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this ConnectionSummary.
        Indicates whether this connection is the default connection.


        :param is_default: The is_default of this ConnectionSummary.
        :type: bool
        """
        self._is_default = is_default

    @property
    def time_created(self):
        """
        Gets the time_created of this ConnectionSummary.
        The date and time the connection was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ConnectionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConnectionSummary.
        The date and time the connection was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ConnectionSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
