# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetSummary(object):
    """
    Summary of a data asset. A physical store, or stream, of data known to the data catalog and containing one or
    many data entities, possibly in an organized structure of folders. A data asset is often synonymous with
    a 'System', such as a database, or may be a file container or a message stream.
    """

    #: A constant which can be used with the lifecycle_state property of a DataAssetSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DataAssetSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DataAssetSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DataAssetSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DataAssetSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DataAssetSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DataAssetSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DataAssetSummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DataAssetSummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this DataAssetSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DataAssetSummary.
        :type description: str

        :param catalog_id:
            The value to assign to the catalog_id property of this DataAssetSummary.
        :type catalog_id: str

        :param external_key:
            The value to assign to the external_key property of this DataAssetSummary.
        :type external_key: str

        :param uri:
            The value to assign to the uri property of this DataAssetSummary.
        :type uri: str

        :param time_created:
            The value to assign to the time_created property of this DataAssetSummary.
        :type time_created: datetime

        :param type_key:
            The value to assign to the type_key property of this DataAssetSummary.
        :type type_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataAssetSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'catalog_id': 'str',
            'external_key': 'str',
            'uri': 'str',
            'time_created': 'datetime',
            'type_key': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'catalog_id': 'catalogId',
            'external_key': 'externalKey',
            'uri': 'uri',
            'time_created': 'timeCreated',
            'type_key': 'typeKey',
            'lifecycle_state': 'lifecycleState'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._catalog_id = None
        self._external_key = None
        self._uri = None
        self._time_created = None
        self._type_key = None
        self._lifecycle_state = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DataAssetSummary.
        Unique data asset key that is immutable.


        :return: The key of this DataAssetSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataAssetSummary.
        Unique data asset key that is immutable.


        :param key: The key of this DataAssetSummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this DataAssetSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this DataAssetSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DataAssetSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this DataAssetSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DataAssetSummary.
        Detailed description of the data asset.


        :return: The description of this DataAssetSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataAssetSummary.
        Detailed description of the data asset.


        :param description: The description of this DataAssetSummary.
        :type: str
        """
        self._description = description

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this DataAssetSummary.
        The data catalog's OCID.


        :return: The catalog_id of this DataAssetSummary.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this DataAssetSummary.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this DataAssetSummary.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def external_key(self):
        """
        Gets the external_key of this DataAssetSummary.
        External URI that can be used to reference the object. Format will differ based on the type of object.


        :return: The external_key of this DataAssetSummary.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this DataAssetSummary.
        External URI that can be used to reference the object. Format will differ based on the type of object.


        :param external_key: The external_key of this DataAssetSummary.
        :type: str
        """
        self._external_key = external_key

    @property
    def uri(self):
        """
        Gets the uri of this DataAssetSummary.
        URI to the data asset instance in the API.


        :return: The uri of this DataAssetSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this DataAssetSummary.
        URI to the data asset instance in the API.


        :param uri: The uri of this DataAssetSummary.
        :type: str
        """
        self._uri = uri

    @property
    def time_created(self):
        """
        Gets the time_created of this DataAssetSummary.
        The date and time the data asset was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DataAssetSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataAssetSummary.
        The date and time the data asset was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DataAssetSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def type_key(self):
        """
        Gets the type_key of this DataAssetSummary.
        The key of the object type. Type keys's can be found via the '/types' endpoint.


        :return: The type_key of this DataAssetSummary.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this DataAssetSummary.
        The key of the object type. Type keys's can be found via the '/types' endpoint.


        :param type_key: The type_key of this DataAssetSummary.
        :type: str
        """
        self._type_key = type_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DataAssetSummary.
        State of the data asset.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DataAssetSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataAssetSummary.
        State of the data asset.


        :param lifecycle_state: The lifecycle_state of this DataAssetSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
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
