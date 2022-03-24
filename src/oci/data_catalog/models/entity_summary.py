# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntitySummary(object):
    """
    Summary of an data entity. A representation of data with a set of attributes, normally representing a single
    business entity. Synonymous with 'table' or 'view' in a database, or a single logical file structure
    that one or many files may match.
    """

    #: A constant which can be used with the lifecycle_state property of a EntitySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a EntitySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EntitySummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EntitySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a EntitySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a EntitySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a EntitySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a EntitySummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new EntitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this EntitySummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this EntitySummary.
        :type display_name: str

        :param business_name:
            The value to assign to the business_name property of this EntitySummary.
        :type business_name: str

        :param description:
            The value to assign to the description property of this EntitySummary.
        :type description: str

        :param is_logical:
            The value to assign to the is_logical property of this EntitySummary.
        :type is_logical: bool

        :param is_partition:
            The value to assign to the is_partition property of this EntitySummary.
        :type is_partition: bool

        :param data_asset_key:
            The value to assign to the data_asset_key property of this EntitySummary.
        :type data_asset_key: str

        :param folder_key:
            The value to assign to the folder_key property of this EntitySummary.
        :type folder_key: str

        :param folder_name:
            The value to assign to the folder_name property of this EntitySummary.
        :type folder_name: str

        :param external_key:
            The value to assign to the external_key property of this EntitySummary.
        :type external_key: str

        :param pattern_key:
            The value to assign to the pattern_key property of this EntitySummary.
        :type pattern_key: str

        :param type_key:
            The value to assign to the type_key property of this EntitySummary.
        :type type_key: str

        :param realized_expression:
            The value to assign to the realized_expression property of this EntitySummary.
        :type realized_expression: str

        :param path:
            The value to assign to the path property of this EntitySummary.
        :type path: str

        :param time_created:
            The value to assign to the time_created property of this EntitySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EntitySummary.
        :type time_updated: datetime

        :param updated_by_id:
            The value to assign to the updated_by_id property of this EntitySummary.
        :type updated_by_id: str

        :param uri:
            The value to assign to the uri property of this EntitySummary.
        :type uri: str

        :param object_storage_url:
            The value to assign to the object_storage_url property of this EntitySummary.
        :type object_storage_url: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EntitySummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param properties:
            The value to assign to the properties property of this EntitySummary.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'business_name': 'str',
            'description': 'str',
            'is_logical': 'bool',
            'is_partition': 'bool',
            'data_asset_key': 'str',
            'folder_key': 'str',
            'folder_name': 'str',
            'external_key': 'str',
            'pattern_key': 'str',
            'type_key': 'str',
            'realized_expression': 'str',
            'path': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'updated_by_id': 'str',
            'uri': 'str',
            'object_storage_url': 'str',
            'lifecycle_state': 'str',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'business_name': 'businessName',
            'description': 'description',
            'is_logical': 'isLogical',
            'is_partition': 'isPartition',
            'data_asset_key': 'dataAssetKey',
            'folder_key': 'folderKey',
            'folder_name': 'folderName',
            'external_key': 'externalKey',
            'pattern_key': 'patternKey',
            'type_key': 'typeKey',
            'realized_expression': 'realizedExpression',
            'path': 'path',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'updated_by_id': 'updatedById',
            'uri': 'uri',
            'object_storage_url': 'objectStorageUrl',
            'lifecycle_state': 'lifecycleState',
            'properties': 'properties'
        }

        self._key = None
        self._display_name = None
        self._business_name = None
        self._description = None
        self._is_logical = None
        self._is_partition = None
        self._data_asset_key = None
        self._folder_key = None
        self._folder_name = None
        self._external_key = None
        self._pattern_key = None
        self._type_key = None
        self._realized_expression = None
        self._path = None
        self._time_created = None
        self._time_updated = None
        self._updated_by_id = None
        self._uri = None
        self._object_storage_url = None
        self._lifecycle_state = None
        self._properties = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this EntitySummary.
        Unique data entity key that is immutable.


        :return: The key of this EntitySummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this EntitySummary.
        Unique data entity key that is immutable.


        :param key: The key of this EntitySummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this EntitySummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this EntitySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EntitySummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this EntitySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def business_name(self):
        """
        Gets the business_name of this EntitySummary.
        Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.


        :return: The business_name of this EntitySummary.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """
        Sets the business_name of this EntitySummary.
        Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.


        :param business_name: The business_name of this EntitySummary.
        :type: str
        """
        self._business_name = business_name

    @property
    def description(self):
        """
        Gets the description of this EntitySummary.
        Detailed description of a data entity.


        :return: The description of this EntitySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EntitySummary.
        Detailed description of a data entity.


        :param description: The description of this EntitySummary.
        :type: str
        """
        self._description = description

    @property
    def is_logical(self):
        """
        Gets the is_logical of this EntitySummary.
        Property that identifies if the object is a physical object (materialized) or virtual/logical object
        defined on other objects.


        :return: The is_logical of this EntitySummary.
        :rtype: bool
        """
        return self._is_logical

    @is_logical.setter
    def is_logical(self, is_logical):
        """
        Sets the is_logical of this EntitySummary.
        Property that identifies if the object is a physical object (materialized) or virtual/logical object
        defined on other objects.


        :param is_logical: The is_logical of this EntitySummary.
        :type: bool
        """
        self._is_logical = is_logical

    @property
    def is_partition(self):
        """
        Gets the is_partition of this EntitySummary.
        Property that identifies if an object is a sub object of a physical or materialized parent object.


        :return: The is_partition of this EntitySummary.
        :rtype: bool
        """
        return self._is_partition

    @is_partition.setter
    def is_partition(self, is_partition):
        """
        Sets the is_partition of this EntitySummary.
        Property that identifies if an object is a sub object of a physical or materialized parent object.


        :param is_partition: The is_partition of this EntitySummary.
        :type: bool
        """
        self._is_partition = is_partition

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this EntitySummary.
        Unique key of the parent data asset.


        :return: The data_asset_key of this EntitySummary.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this EntitySummary.
        Unique key of the parent data asset.


        :param data_asset_key: The data_asset_key of this EntitySummary.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def folder_key(self):
        """
        Gets the folder_key of this EntitySummary.
        Key of the associated folder.


        :return: The folder_key of this EntitySummary.
        :rtype: str
        """
        return self._folder_key

    @folder_key.setter
    def folder_key(self, folder_key):
        """
        Sets the folder_key of this EntitySummary.
        Key of the associated folder.


        :param folder_key: The folder_key of this EntitySummary.
        :type: str
        """
        self._folder_key = folder_key

    @property
    def folder_name(self):
        """
        Gets the folder_name of this EntitySummary.
        Name of the associated folder. This name is harvested from the source data asset when the parent folder for the entiy is harvested.


        :return: The folder_name of this EntitySummary.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """
        Sets the folder_name of this EntitySummary.
        Name of the associated folder. This name is harvested from the source data asset when the parent folder for the entiy is harvested.


        :param folder_name: The folder_name of this EntitySummary.
        :type: str
        """
        self._folder_name = folder_name

    @property
    def external_key(self):
        """
        Gets the external_key of this EntitySummary.
        Unique external key of this object in the source system.


        :return: The external_key of this EntitySummary.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this EntitySummary.
        Unique external key of this object in the source system.


        :param external_key: The external_key of this EntitySummary.
        :type: str
        """
        self._external_key = external_key

    @property
    def pattern_key(self):
        """
        Gets the pattern_key of this EntitySummary.
        Key of the associated pattern if this is a logical entity.


        :return: The pattern_key of this EntitySummary.
        :rtype: str
        """
        return self._pattern_key

    @pattern_key.setter
    def pattern_key(self, pattern_key):
        """
        Sets the pattern_key of this EntitySummary.
        Key of the associated pattern if this is a logical entity.


        :param pattern_key: The pattern_key of this EntitySummary.
        :type: str
        """
        self._pattern_key = pattern_key

    @property
    def type_key(self):
        """
        Gets the type_key of this EntitySummary.
        The type of data entity object. Type keys can be found via the '/types' endpoint.


        :return: The type_key of this EntitySummary.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this EntitySummary.
        The type of data entity object. Type keys can be found via the '/types' endpoint.


        :param type_key: The type_key of this EntitySummary.
        :type: str
        """
        self._type_key = type_key

    @property
    def realized_expression(self):
        """
        Gets the realized_expression of this EntitySummary.
        The expression realized after resolving qualifiers . Used in deriving this logical entity


        :return: The realized_expression of this EntitySummary.
        :rtype: str
        """
        return self._realized_expression

    @realized_expression.setter
    def realized_expression(self, realized_expression):
        """
        Sets the realized_expression of this EntitySummary.
        The expression realized after resolving qualifiers . Used in deriving this logical entity


        :param realized_expression: The realized_expression of this EntitySummary.
        :type: str
        """
        self._realized_expression = realized_expression

    @property
    def path(self):
        """
        Gets the path of this EntitySummary.
        Full path of the data entity.


        :return: The path of this EntitySummary.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this EntitySummary.
        Full path of the data entity.


        :param path: The path of this EntitySummary.
        :type: str
        """
        self._path = path

    @property
    def time_created(self):
        """
        Gets the time_created of this EntitySummary.
        The date and time the data entity was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this EntitySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EntitySummary.
        The date and time the data entity was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this EntitySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EntitySummary.
        The last time that any change was made to the data entity. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this EntitySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EntitySummary.
        The last time that any change was made to the data entity. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this EntitySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this EntitySummary.
        OCID of the user who updated this object in the data catalog.


        :return: The updated_by_id of this EntitySummary.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this EntitySummary.
        OCID of the user who updated this object in the data catalog.


        :param updated_by_id: The updated_by_id of this EntitySummary.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def uri(self):
        """
        Gets the uri of this EntitySummary.
        URI to the data entity instance in the API.


        :return: The uri of this EntitySummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this EntitySummary.
        URI to the data entity instance in the API.


        :param uri: The uri of this EntitySummary.
        :type: str
        """
        self._uri = uri

    @property
    def object_storage_url(self):
        """
        Gets the object_storage_url of this EntitySummary.
        URL of the data entity in the object store.


        :return: The object_storage_url of this EntitySummary.
        :rtype: str
        """
        return self._object_storage_url

    @object_storage_url.setter
    def object_storage_url(self, object_storage_url):
        """
        Sets the object_storage_url of this EntitySummary.
        URL of the data entity in the object store.


        :param object_storage_url: The object_storage_url of this EntitySummary.
        :type: str
        """
        self._object_storage_url = object_storage_url

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this EntitySummary.
        State of the data entity.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EntitySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EntitySummary.
        State of the data entity.


        :param lifecycle_state: The lifecycle_state of this EntitySummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def properties(self):
        """
        Gets the properties of this EntitySummary.
        A map of maps that contains the properties which are specific to the entity type. Each entity type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data entities have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :return: The properties of this EntitySummary.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this EntitySummary.
        A map of maps that contains the properties which are specific to the entity type. Each entity type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data entities have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :param properties: The properties of this EntitySummary.
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
