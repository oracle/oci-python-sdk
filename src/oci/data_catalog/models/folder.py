# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Folder(object):
    """
    A generic term used in the data catalog for an external organization concept used for a collection of data entities
    or processes within a data asset. This term is an internal term which models multiple external types of folder,
    such as file directories, database schemas, and so on. Some data assets, such as Object Store containers, may contain
    many levels of folders.
    """

    #: A constant which can be used with the lifecycle_state property of a Folder.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Folder.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Folder.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Folder.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Folder.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Folder.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Folder.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Folder.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    #: A constant which can be used with the harvest_status property of a Folder.
    #: This constant has a value of "COMPLETE"
    HARVEST_STATUS_COMPLETE = "COMPLETE"

    #: A constant which can be used with the harvest_status property of a Folder.
    #: This constant has a value of "ERROR"
    HARVEST_STATUS_ERROR = "ERROR"

    #: A constant which can be used with the harvest_status property of a Folder.
    #: This constant has a value of "IN_PROGRESS"
    HARVEST_STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the harvest_status property of a Folder.
    #: This constant has a value of "DEFERRED"
    HARVEST_STATUS_DEFERRED = "DEFERRED"

    def __init__(self, **kwargs):
        """
        Initializes a new Folder object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Folder.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this Folder.
        :type display_name: str

        :param business_name:
            The value to assign to the business_name property of this Folder.
        :type business_name: str

        :param description:
            The value to assign to the description property of this Folder.
        :type description: str

        :param parent_folder_key:
            The value to assign to the parent_folder_key property of this Folder.
        :type parent_folder_key: str

        :param path:
            The value to assign to the path property of this Folder.
        :type path: str

        :param data_asset_key:
            The value to assign to the data_asset_key property of this Folder.
        :type data_asset_key: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this Folder.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertyGetUsage]

        :param properties:
            The value to assign to the properties property of this Folder.
        :type properties: dict(str, dict(str, str))

        :param external_key:
            The value to assign to the external_key property of this Folder.
        :type external_key: str

        :param time_created:
            The value to assign to the time_created property of this Folder.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Folder.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this Folder.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this Folder.
        :type updated_by_id: str

        :param time_external:
            The value to assign to the time_external property of this Folder.
        :type time_external: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Folder.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param harvest_status:
            The value to assign to the harvest_status property of this Folder.
            Allowed values for this property are: "COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type harvest_status: str

        :param last_job_key:
            The value to assign to the last_job_key property of this Folder.
        :type last_job_key: str

        :param uri:
            The value to assign to the uri property of this Folder.
        :type uri: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'business_name': 'str',
            'description': 'str',
            'parent_folder_key': 'str',
            'path': 'str',
            'data_asset_key': 'str',
            'custom_property_members': 'list[CustomPropertyGetUsage]',
            'properties': 'dict(str, dict(str, str))',
            'external_key': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'time_external': 'datetime',
            'lifecycle_state': 'str',
            'harvest_status': 'str',
            'last_job_key': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'business_name': 'businessName',
            'description': 'description',
            'parent_folder_key': 'parentFolderKey',
            'path': 'path',
            'data_asset_key': 'dataAssetKey',
            'custom_property_members': 'customPropertyMembers',
            'properties': 'properties',
            'external_key': 'externalKey',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'time_external': 'timeExternal',
            'lifecycle_state': 'lifecycleState',
            'harvest_status': 'harvestStatus',
            'last_job_key': 'lastJobKey',
            'uri': 'uri'
        }

        self._key = None
        self._display_name = None
        self._business_name = None
        self._description = None
        self._parent_folder_key = None
        self._path = None
        self._data_asset_key = None
        self._custom_property_members = None
        self._properties = None
        self._external_key = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._time_external = None
        self._lifecycle_state = None
        self._harvest_status = None
        self._last_job_key = None
        self._uri = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Folder.
        Unique folder key that is immutable.


        :return: The key of this Folder.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Folder.
        Unique folder key that is immutable.


        :param key: The key of this Folder.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this Folder.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Folder.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Folder.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Folder.
        :type: str
        """
        self._display_name = display_name

    @property
    def business_name(self):
        """
        Gets the business_name of this Folder.
        Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.


        :return: The business_name of this Folder.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """
        Sets the business_name of this Folder.
        Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.


        :param business_name: The business_name of this Folder.
        :type: str
        """
        self._business_name = business_name

    @property
    def description(self):
        """
        Gets the description of this Folder.
        Detailed description of a folder.


        :return: The description of this Folder.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Folder.
        Detailed description of a folder.


        :param description: The description of this Folder.
        :type: str
        """
        self._description = description

    @property
    def parent_folder_key(self):
        """
        Gets the parent_folder_key of this Folder.
        The unique key of the containing folder or null if there is no parent folder.


        :return: The parent_folder_key of this Folder.
        :rtype: str
        """
        return self._parent_folder_key

    @parent_folder_key.setter
    def parent_folder_key(self, parent_folder_key):
        """
        Sets the parent_folder_key of this Folder.
        The unique key of the containing folder or null if there is no parent folder.


        :param parent_folder_key: The parent_folder_key of this Folder.
        :type: str
        """
        self._parent_folder_key = parent_folder_key

    @property
    def path(self):
        """
        Gets the path of this Folder.
        Full path of the folder.


        :return: The path of this Folder.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Folder.
        Full path of the folder.


        :param path: The path of this Folder.
        :type: str
        """
        self._path = path

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this Folder.
        The key of the associated data asset.


        :return: The data_asset_key of this Folder.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this Folder.
        The key of the associated data asset.


        :param data_asset_key: The data_asset_key of this Folder.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def custom_property_members(self):
        """
        Gets the custom_property_members of this Folder.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this Folder.
        :rtype: list[oci.data_catalog.models.CustomPropertyGetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this Folder.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this Folder.
        :type: list[oci.data_catalog.models.CustomPropertyGetUsage]
        """
        self._custom_property_members = custom_property_members

    @property
    def properties(self):
        """
        Gets the properties of this Folder.
        A map of maps that contains the properties which are specific to the folder type. Each folder type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        folders have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :return: The properties of this Folder.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Folder.
        A map of maps that contains the properties which are specific to the folder type. Each folder type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        folders have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :param properties: The properties of this Folder.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    @property
    def external_key(self):
        """
        Gets the external_key of this Folder.
        Unique external key of this object in the source system.


        :return: The external_key of this Folder.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this Folder.
        Unique external key of this object in the source system.


        :param external_key: The external_key of this Folder.
        :type: str
        """
        self._external_key = external_key

    @property
    def time_created(self):
        """
        Gets the time_created of this Folder.
        The date and time the folder was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Folder.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Folder.
        The date and time the folder was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Folder.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Folder.
        The last time that any change was made to the folder. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Folder.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Folder.
        The last time that any change was made to the folder. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Folder.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this Folder.
        OCID of the user who created the folder.


        :return: The created_by_id of this Folder.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this Folder.
        OCID of the user who created the folder.


        :param created_by_id: The created_by_id of this Folder.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this Folder.
        OCID of the user who modified the folder.


        :return: The updated_by_id of this Folder.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this Folder.
        OCID of the user who modified the folder.


        :param updated_by_id: The updated_by_id of this Folder.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def time_external(self):
        """
        Gets the time_external of this Folder.
        Last modified timestamp of this object in the external system.


        :return: The time_external of this Folder.
        :rtype: datetime
        """
        return self._time_external

    @time_external.setter
    def time_external(self, time_external):
        """
        Sets the time_external of this Folder.
        Last modified timestamp of this object in the external system.


        :param time_external: The time_external of this Folder.
        :type: datetime
        """
        self._time_external = time_external

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Folder.
        The current state of the folder.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Folder.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Folder.
        The current state of the folder.


        :param lifecycle_state: The lifecycle_state of this Folder.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def harvest_status(self):
        """
        Gets the harvest_status of this Folder.
        Status of the object as updated by the harvest process.

        Allowed values for this property are: "COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The harvest_status of this Folder.
        :rtype: str
        """
        return self._harvest_status

    @harvest_status.setter
    def harvest_status(self, harvest_status):
        """
        Sets the harvest_status of this Folder.
        Status of the object as updated by the harvest process.


        :param harvest_status: The harvest_status of this Folder.
        :type: str
        """
        allowed_values = ["COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"]
        if not value_allowed_none_or_none_sentinel(harvest_status, allowed_values):
            harvest_status = 'UNKNOWN_ENUM_VALUE'
        self._harvest_status = harvest_status

    @property
    def last_job_key(self):
        """
        Gets the last_job_key of this Folder.
        The key of the last harvest process to update the metadata of this object.


        :return: The last_job_key of this Folder.
        :rtype: str
        """
        return self._last_job_key

    @last_job_key.setter
    def last_job_key(self, last_job_key):
        """
        Sets the last_job_key of this Folder.
        The key of the last harvest process to update the metadata of this object.


        :param last_job_key: The last_job_key of this Folder.
        :type: str
        """
        self._last_job_key = last_job_key

    @property
    def uri(self):
        """
        Gets the uri of this Folder.
        URI to the folder instance in the API.


        :return: The uri of this Folder.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Folder.
        URI to the folder instance in the API.


        :param uri: The uri of this Folder.
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
