# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FolderSummary(object):
    """
    Summary of a folder.
    A generic term used in the data catalog for an external organization concept used for a collection of data entities
    or processes within a data asset. This term is an internal term which models multiple external types of folder,
    such as file directories, database schemas, and so on. Some data assets, such as Object Store containers,
    may contain many levels of folders.
    """

    #: A constant which can be used with the lifecycle_state property of a FolderSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a FolderSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FolderSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FolderSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a FolderSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a FolderSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a FolderSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a FolderSummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new FolderSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this FolderSummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this FolderSummary.
        :type display_name: str

        :param business_name:
            The value to assign to the business_name property of this FolderSummary.
        :type business_name: str

        :param description:
            The value to assign to the description property of this FolderSummary.
        :type description: str

        :param data_asset_key:
            The value to assign to the data_asset_key property of this FolderSummary.
        :type data_asset_key: str

        :param parent_folder_key:
            The value to assign to the parent_folder_key property of this FolderSummary.
        :type parent_folder_key: str

        :param path:
            The value to assign to the path property of this FolderSummary.
        :type path: str

        :param external_key:
            The value to assign to the external_key property of this FolderSummary.
        :type external_key: str

        :param time_external:
            The value to assign to the time_external property of this FolderSummary.
        :type time_external: datetime

        :param time_created:
            The value to assign to the time_created property of this FolderSummary.
        :type time_created: datetime

        :param uri:
            The value to assign to the uri property of this FolderSummary.
        :type uri: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FolderSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'business_name': 'str',
            'description': 'str',
            'data_asset_key': 'str',
            'parent_folder_key': 'str',
            'path': 'str',
            'external_key': 'str',
            'time_external': 'datetime',
            'time_created': 'datetime',
            'uri': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'business_name': 'businessName',
            'description': 'description',
            'data_asset_key': 'dataAssetKey',
            'parent_folder_key': 'parentFolderKey',
            'path': 'path',
            'external_key': 'externalKey',
            'time_external': 'timeExternal',
            'time_created': 'timeCreated',
            'uri': 'uri',
            'lifecycle_state': 'lifecycleState'
        }

        self._key = None
        self._display_name = None
        self._business_name = None
        self._description = None
        self._data_asset_key = None
        self._parent_folder_key = None
        self._path = None
        self._external_key = None
        self._time_external = None
        self._time_created = None
        self._uri = None
        self._lifecycle_state = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this FolderSummary.
        Unique folder key that is immutable.


        :return: The key of this FolderSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FolderSummary.
        Unique folder key that is immutable.


        :param key: The key of this FolderSummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this FolderSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this FolderSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FolderSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this FolderSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def business_name(self):
        """
        Gets the business_name of this FolderSummary.
        Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.


        :return: The business_name of this FolderSummary.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """
        Sets the business_name of this FolderSummary.
        Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.


        :param business_name: The business_name of this FolderSummary.
        :type: str
        """
        self._business_name = business_name

    @property
    def description(self):
        """
        Gets the description of this FolderSummary.
        Detailed description of a folder.


        :return: The description of this FolderSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FolderSummary.
        Detailed description of a folder.


        :param description: The description of this FolderSummary.
        :type: str
        """
        self._description = description

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this FolderSummary.
        The unique key of the parent data asset.


        :return: The data_asset_key of this FolderSummary.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this FolderSummary.
        The unique key of the parent data asset.


        :param data_asset_key: The data_asset_key of this FolderSummary.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def parent_folder_key(self):
        """
        Gets the parent_folder_key of this FolderSummary.
        The key of the containing folder or null if there is no parent.


        :return: The parent_folder_key of this FolderSummary.
        :rtype: str
        """
        return self._parent_folder_key

    @parent_folder_key.setter
    def parent_folder_key(self, parent_folder_key):
        """
        Sets the parent_folder_key of this FolderSummary.
        The key of the containing folder or null if there is no parent.


        :param parent_folder_key: The parent_folder_key of this FolderSummary.
        :type: str
        """
        self._parent_folder_key = parent_folder_key

    @property
    def path(self):
        """
        Gets the path of this FolderSummary.
        Full path of the folder.


        :return: The path of this FolderSummary.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this FolderSummary.
        Full path of the folder.


        :param path: The path of this FolderSummary.
        :type: str
        """
        self._path = path

    @property
    def external_key(self):
        """
        Gets the external_key of this FolderSummary.
        Unique external key of this object from the source systems.


        :return: The external_key of this FolderSummary.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this FolderSummary.
        Unique external key of this object from the source systems.


        :param external_key: The external_key of this FolderSummary.
        :type: str
        """
        self._external_key = external_key

    @property
    def time_external(self):
        """
        Gets the time_external of this FolderSummary.
        Last modified timestamp of this object in the external system.


        :return: The time_external of this FolderSummary.
        :rtype: datetime
        """
        return self._time_external

    @time_external.setter
    def time_external(self, time_external):
        """
        Sets the time_external of this FolderSummary.
        Last modified timestamp of this object in the external system.


        :param time_external: The time_external of this FolderSummary.
        :type: datetime
        """
        self._time_external = time_external

    @property
    def time_created(self):
        """
        Gets the time_created of this FolderSummary.
        The date and time the folder was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this FolderSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FolderSummary.
        The date and time the folder was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this FolderSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def uri(self):
        """
        Gets the uri of this FolderSummary.
        URI of the folder resource within the data catalog API.


        :return: The uri of this FolderSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this FolderSummary.
        URI of the folder resource within the data catalog API.


        :param uri: The uri of this FolderSummary.
        :type: str
        """
        self._uri = uri

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this FolderSummary.
        State of the folder.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FolderSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FolderSummary.
        State of the folder.


        :param lifecycle_state: The lifecycle_state of this FolderSummary.
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
