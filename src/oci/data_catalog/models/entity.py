# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Entity(object):
    """
    Data entity details. A representation of data with a set of attributes, normally representing a single
    business entity. Synonymous with 'table' or 'view' in a database, or a single logical file structure
    that one or many files may match.
    """

    #: A constant which can be used with the lifecycle_state property of a Entity.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Entity.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Entity.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Entity.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Entity.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Entity.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Entity.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Entity.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    #: A constant which can be used with the harvest_status property of a Entity.
    #: This constant has a value of "COMPLETE"
    HARVEST_STATUS_COMPLETE = "COMPLETE"

    #: A constant which can be used with the harvest_status property of a Entity.
    #: This constant has a value of "ERROR"
    HARVEST_STATUS_ERROR = "ERROR"

    #: A constant which can be used with the harvest_status property of a Entity.
    #: This constant has a value of "IN_PROGRESS"
    HARVEST_STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the harvest_status property of a Entity.
    #: This constant has a value of "DEFERRED"
    HARVEST_STATUS_DEFERRED = "DEFERRED"

    def __init__(self, **kwargs):
        """
        Initializes a new Entity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Entity.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this Entity.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Entity.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Entity.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Entity.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this Entity.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this Entity.
        :type updated_by_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Entity.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param external_key:
            The value to assign to the external_key property of this Entity.
        :type external_key: str

        :param time_external:
            The value to assign to the time_external property of this Entity.
        :type time_external: datetime

        :param time_status_updated:
            The value to assign to the time_status_updated property of this Entity.
        :type time_status_updated: datetime

        :param is_logical:
            The value to assign to the is_logical property of this Entity.
        :type is_logical: bool

        :param is_partition:
            The value to assign to the is_partition property of this Entity.
        :type is_partition: bool

        :param data_asset_key:
            The value to assign to the data_asset_key property of this Entity.
        :type data_asset_key: str

        :param folder_key:
            The value to assign to the folder_key property of this Entity.
        :type folder_key: str

        :param path:
            The value to assign to the path property of this Entity.
        :type path: str

        :param harvest_status:
            The value to assign to the harvest_status property of this Entity.
            Allowed values for this property are: "COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type harvest_status: str

        :param last_job_key:
            The value to assign to the last_job_key property of this Entity.
        :type last_job_key: str

        :param type_key:
            The value to assign to the type_key property of this Entity.
        :type type_key: str

        :param uri:
            The value to assign to the uri property of this Entity.
        :type uri: str

        :param properties:
            The value to assign to the properties property of this Entity.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'lifecycle_state': 'str',
            'external_key': 'str',
            'time_external': 'datetime',
            'time_status_updated': 'datetime',
            'is_logical': 'bool',
            'is_partition': 'bool',
            'data_asset_key': 'str',
            'folder_key': 'str',
            'path': 'str',
            'harvest_status': 'str',
            'last_job_key': 'str',
            'type_key': 'str',
            'uri': 'str',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'lifecycle_state': 'lifecycleState',
            'external_key': 'externalKey',
            'time_external': 'timeExternal',
            'time_status_updated': 'timeStatusUpdated',
            'is_logical': 'isLogical',
            'is_partition': 'isPartition',
            'data_asset_key': 'dataAssetKey',
            'folder_key': 'folderKey',
            'path': 'path',
            'harvest_status': 'harvestStatus',
            'last_job_key': 'lastJobKey',
            'type_key': 'typeKey',
            'uri': 'uri',
            'properties': 'properties'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._lifecycle_state = None
        self._external_key = None
        self._time_external = None
        self._time_status_updated = None
        self._is_logical = None
        self._is_partition = None
        self._data_asset_key = None
        self._folder_key = None
        self._path = None
        self._harvest_status = None
        self._last_job_key = None
        self._type_key = None
        self._uri = None
        self._properties = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Entity.
        Unique data entity key that is immutable.


        :return: The key of this Entity.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Entity.
        Unique data entity key that is immutable.


        :param key: The key of this Entity.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this Entity.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Entity.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Entity.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Entity.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Entity.
        Detailed description of a data entity.


        :return: The description of this Entity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Entity.
        Detailed description of a data entity.


        :param description: The description of this Entity.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this Entity.
        The date and time the data entity was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Entity.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Entity.
        The date and time the data entity was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Entity.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Entity.
        The last time that any change was made to the data entity. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Entity.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Entity.
        The last time that any change was made to the data entity. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Entity.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this Entity.
        OCID of the user who created this object in the data catalog.


        :return: The created_by_id of this Entity.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this Entity.
        OCID of the user who created this object in the data catalog.


        :param created_by_id: The created_by_id of this Entity.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this Entity.
        OCID of the user who updated this object in the data catalog.


        :return: The updated_by_id of this Entity.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this Entity.
        OCID of the user who updated this object in the data catalog.


        :param updated_by_id: The updated_by_id of this Entity.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Entity.
        The current state of the data entity.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Entity.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Entity.
        The current state of the data entity.


        :param lifecycle_state: The lifecycle_state of this Entity.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def external_key(self):
        """
        Gets the external_key of this Entity.
        Unique external key of this object in the source system.


        :return: The external_key of this Entity.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this Entity.
        Unique external key of this object in the source system.


        :param external_key: The external_key of this Entity.
        :type: str
        """
        self._external_key = external_key

    @property
    def time_external(self):
        """
        Gets the time_external of this Entity.
        Last modified timestamp of this object in the external system.


        :return: The time_external of this Entity.
        :rtype: datetime
        """
        return self._time_external

    @time_external.setter
    def time_external(self, time_external):
        """
        Sets the time_external of this Entity.
        Last modified timestamp of this object in the external system.


        :param time_external: The time_external of this Entity.
        :type: datetime
        """
        self._time_external = time_external

    @property
    def time_status_updated(self):
        """
        Gets the time_status_updated of this Entity.
        Time that the data entities status was last updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_status_updated of this Entity.
        :rtype: datetime
        """
        return self._time_status_updated

    @time_status_updated.setter
    def time_status_updated(self, time_status_updated):
        """
        Sets the time_status_updated of this Entity.
        Time that the data entities status was last updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_status_updated: The time_status_updated of this Entity.
        :type: datetime
        """
        self._time_status_updated = time_status_updated

    @property
    def is_logical(self):
        """
        Gets the is_logical of this Entity.
        Property that identifies if the object is a physical object (materialized) or virtual/logical object
        defined on other objects.


        :return: The is_logical of this Entity.
        :rtype: bool
        """
        return self._is_logical

    @is_logical.setter
    def is_logical(self, is_logical):
        """
        Sets the is_logical of this Entity.
        Property that identifies if the object is a physical object (materialized) or virtual/logical object
        defined on other objects.


        :param is_logical: The is_logical of this Entity.
        :type: bool
        """
        self._is_logical = is_logical

    @property
    def is_partition(self):
        """
        Gets the is_partition of this Entity.
        Property that identifies if an object is a sub object of a physical or materialized parent object.


        :return: The is_partition of this Entity.
        :rtype: bool
        """
        return self._is_partition

    @is_partition.setter
    def is_partition(self, is_partition):
        """
        Sets the is_partition of this Entity.
        Property that identifies if an object is a sub object of a physical or materialized parent object.


        :param is_partition: The is_partition of this Entity.
        :type: bool
        """
        self._is_partition = is_partition

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this Entity.
        Unique key of the parent data asset.


        :return: The data_asset_key of this Entity.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this Entity.
        Unique key of the parent data asset.


        :param data_asset_key: The data_asset_key of this Entity.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def folder_key(self):
        """
        Gets the folder_key of this Entity.
        Key of the associated folder.


        :return: The folder_key of this Entity.
        :rtype: str
        """
        return self._folder_key

    @folder_key.setter
    def folder_key(self, folder_key):
        """
        Sets the folder_key of this Entity.
        Key of the associated folder.


        :param folder_key: The folder_key of this Entity.
        :type: str
        """
        self._folder_key = folder_key

    @property
    def path(self):
        """
        Gets the path of this Entity.
        Full path of the data entity.


        :return: The path of this Entity.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Entity.
        Full path of the data entity.


        :param path: The path of this Entity.
        :type: str
        """
        self._path = path

    @property
    def harvest_status(self):
        """
        Gets the harvest_status of this Entity.
        Status of the object as updated by the harvest process.

        Allowed values for this property are: "COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The harvest_status of this Entity.
        :rtype: str
        """
        return self._harvest_status

    @harvest_status.setter
    def harvest_status(self, harvest_status):
        """
        Sets the harvest_status of this Entity.
        Status of the object as updated by the harvest process.


        :param harvest_status: The harvest_status of this Entity.
        :type: str
        """
        allowed_values = ["COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"]
        if not value_allowed_none_or_none_sentinel(harvest_status, allowed_values):
            harvest_status = 'UNKNOWN_ENUM_VALUE'
        self._harvest_status = harvest_status

    @property
    def last_job_key(self):
        """
        Gets the last_job_key of this Entity.
        Key of the last harvest process to update this object.


        :return: The last_job_key of this Entity.
        :rtype: str
        """
        return self._last_job_key

    @last_job_key.setter
    def last_job_key(self, last_job_key):
        """
        Sets the last_job_key of this Entity.
        Key of the last harvest process to update this object.


        :param last_job_key: The last_job_key of this Entity.
        :type: str
        """
        self._last_job_key = last_job_key

    @property
    def type_key(self):
        """
        Gets the type_key of this Entity.
        The type of data entity object. Type key's can be found via the '/types' endpoint.


        :return: The type_key of this Entity.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this Entity.
        The type of data entity object. Type key's can be found via the '/types' endpoint.


        :param type_key: The type_key of this Entity.
        :type: str
        """
        self._type_key = type_key

    @property
    def uri(self):
        """
        Gets the uri of this Entity.
        URI to the data entity instance in the API.


        :return: The uri of this Entity.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Entity.
        URI to the data entity instance in the API.


        :param uri: The uri of this Entity.
        :type: str
        """
        self._uri = uri

    @property
    def properties(self):
        """
        Gets the properties of this Entity.
        A map of maps that contains the properties which are specific to the entity type. Each entity type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data entities have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :return: The properties of this Entity.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Entity.
        A map of maps that contains the properties which are specific to the entity type. Each entity type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data entities have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :param properties: The properties of this Entity.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
