# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomProperty(object):
    """
    Custom Property Definition
    """

    #: A constant which can be used with the data_type property of a CustomProperty.
    #: This constant has a value of "TEXT"
    DATA_TYPE_TEXT = "TEXT"

    #: A constant which can be used with the data_type property of a CustomProperty.
    #: This constant has a value of "RICH_TEXT"
    DATA_TYPE_RICH_TEXT = "RICH_TEXT"

    #: A constant which can be used with the data_type property of a CustomProperty.
    #: This constant has a value of "BOOLEAN"
    DATA_TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the data_type property of a CustomProperty.
    #: This constant has a value of "NUMBER"
    DATA_TYPE_NUMBER = "NUMBER"

    #: A constant which can be used with the data_type property of a CustomProperty.
    #: This constant has a value of "DATE"
    DATA_TYPE_DATE = "DATE"

    #: A constant which can be used with the lifecycle_state property of a CustomProperty.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CustomProperty.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CustomProperty.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CustomProperty.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CustomProperty.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CustomProperty.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CustomProperty.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a CustomProperty.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new CustomProperty object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CustomProperty.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this CustomProperty.
        :type display_name: str

        :param data_type:
            The value to assign to the data_type property of this CustomProperty.
            Allowed values for this property are: "TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_type: str

        :param description:
            The value to assign to the description property of this CustomProperty.
        :type description: str

        :param namespace_name:
            The value to assign to the namespace_name property of this CustomProperty.
        :type namespace_name: str

        :param is_list_type:
            The value to assign to the is_list_type property of this CustomProperty.
        :type is_list_type: bool

        :param is_sortable:
            The value to assign to the is_sortable property of this CustomProperty.
        :type is_sortable: bool

        :param is_filterable:
            The value to assign to the is_filterable property of this CustomProperty.
        :type is_filterable: bool

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this CustomProperty.
        :type is_multi_valued: bool

        :param is_hidden:
            The value to assign to the is_hidden property of this CustomProperty.
        :type is_hidden: bool

        :param is_editable:
            The value to assign to the is_editable property of this CustomProperty.
        :type is_editable: bool

        :param is_service_defined:
            The value to assign to the is_service_defined property of this CustomProperty.
        :type is_service_defined: bool

        :param is_hidden_in_search:
            The value to assign to the is_hidden_in_search property of this CustomProperty.
        :type is_hidden_in_search: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CustomProperty.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this CustomProperty.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CustomProperty.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this CustomProperty.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this CustomProperty.
        :type updated_by_id: str

        :param usage_count:
            The value to assign to the usage_count property of this CustomProperty.
        :type usage_count: int

        :param scope:
            The value to assign to the scope property of this CustomProperty.
        :type scope: list[oci.data_catalog.models.CustomPropertyTypeUsage]

        :param allowed_values:
            The value to assign to the allowed_values property of this CustomProperty.
        :type allowed_values: list[str]

        :param properties:
            The value to assign to the properties property of this CustomProperty.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'data_type': 'str',
            'description': 'str',
            'namespace_name': 'str',
            'is_list_type': 'bool',
            'is_sortable': 'bool',
            'is_filterable': 'bool',
            'is_multi_valued': 'bool',
            'is_hidden': 'bool',
            'is_editable': 'bool',
            'is_service_defined': 'bool',
            'is_hidden_in_search': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'usage_count': 'int',
            'scope': 'list[CustomPropertyTypeUsage]',
            'allowed_values': 'list[str]',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'data_type': 'dataType',
            'description': 'description',
            'namespace_name': 'namespaceName',
            'is_list_type': 'isListType',
            'is_sortable': 'isSortable',
            'is_filterable': 'isFilterable',
            'is_multi_valued': 'isMultiValued',
            'is_hidden': 'isHidden',
            'is_editable': 'isEditable',
            'is_service_defined': 'isServiceDefined',
            'is_hidden_in_search': 'isHiddenInSearch',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'usage_count': 'usageCount',
            'scope': 'scope',
            'allowed_values': 'allowedValues',
            'properties': 'properties'
        }

        self._key = None
        self._display_name = None
        self._data_type = None
        self._description = None
        self._namespace_name = None
        self._is_list_type = None
        self._is_sortable = None
        self._is_filterable = None
        self._is_multi_valued = None
        self._is_hidden = None
        self._is_editable = None
        self._is_service_defined = None
        self._is_hidden_in_search = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._usage_count = None
        self._scope = None
        self._allowed_values = None
        self._properties = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this CustomProperty.
        Unique data asset key that is immutable.


        :return: The key of this CustomProperty.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CustomProperty.
        Unique data asset key that is immutable.


        :param key: The key of this CustomProperty.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this CustomProperty.
        Display name of the custom property


        :return: The display_name of this CustomProperty.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CustomProperty.
        Display name of the custom property


        :param display_name: The display_name of this CustomProperty.
        :type: str
        """
        self._display_name = display_name

    @property
    def data_type(self):
        """
        Gets the data_type of this CustomProperty.
        Data type of the custom property

        Allowed values for this property are: "TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_type of this CustomProperty.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this CustomProperty.
        Data type of the custom property


        :param data_type: The data_type of this CustomProperty.
        :type: str
        """
        allowed_values = ["TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE"]
        if not value_allowed_none_or_none_sentinel(data_type, allowed_values):
            data_type = 'UNKNOWN_ENUM_VALUE'
        self._data_type = data_type

    @property
    def description(self):
        """
        Gets the description of this CustomProperty.
        Description for the custom property


        :return: The description of this CustomProperty.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CustomProperty.
        Description for the custom property


        :param description: The description of this CustomProperty.
        :type: str
        """
        self._description = description

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this CustomProperty.
        Namespace name of the custom property


        :return: The namespace_name of this CustomProperty.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this CustomProperty.
        Namespace name of the custom property


        :param namespace_name: The namespace_name of this CustomProperty.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def is_list_type(self):
        """
        Gets the is_list_type of this CustomProperty.
        Is this property allowed to have list of values


        :return: The is_list_type of this CustomProperty.
        :rtype: bool
        """
        return self._is_list_type

    @is_list_type.setter
    def is_list_type(self, is_list_type):
        """
        Sets the is_list_type of this CustomProperty.
        Is this property allowed to have list of values


        :param is_list_type: The is_list_type of this CustomProperty.
        :type: bool
        """
        self._is_list_type = is_list_type

    @property
    def is_sortable(self):
        """
        Gets the is_sortable of this CustomProperty.
        If this field allows to sort from UI


        :return: The is_sortable of this CustomProperty.
        :rtype: bool
        """
        return self._is_sortable

    @is_sortable.setter
    def is_sortable(self, is_sortable):
        """
        Sets the is_sortable of this CustomProperty.
        If this field allows to sort from UI


        :param is_sortable: The is_sortable of this CustomProperty.
        :type: bool
        """
        self._is_sortable = is_sortable

    @property
    def is_filterable(self):
        """
        Gets the is_filterable of this CustomProperty.
        If this field allows to filter or create facets from UI


        :return: The is_filterable of this CustomProperty.
        :rtype: bool
        """
        return self._is_filterable

    @is_filterable.setter
    def is_filterable(self, is_filterable):
        """
        Sets the is_filterable of this CustomProperty.
        If this field allows to filter or create facets from UI


        :param is_filterable: The is_filterable of this CustomProperty.
        :type: bool
        """
        self._is_filterable = is_filterable

    @property
    def is_multi_valued(self):
        """
        Gets the is_multi_valued of this CustomProperty.
        If this field allows multiple values to be set


        :return: The is_multi_valued of this CustomProperty.
        :rtype: bool
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued):
        """
        Sets the is_multi_valued of this CustomProperty.
        If this field allows multiple values to be set


        :param is_multi_valued: The is_multi_valued of this CustomProperty.
        :type: bool
        """
        self._is_multi_valued = is_multi_valued

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this CustomProperty.
        If this field is a hidden field


        :return: The is_hidden of this CustomProperty.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this CustomProperty.
        If this field is a hidden field


        :param is_hidden: The is_hidden of this CustomProperty.
        :type: bool
        """
        self._is_hidden = is_hidden

    @property
    def is_editable(self):
        """
        Gets the is_editable of this CustomProperty.
        If this field is a editable field


        :return: The is_editable of this CustomProperty.
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """
        Sets the is_editable of this CustomProperty.
        If this field is a editable field


        :param is_editable: The is_editable of this CustomProperty.
        :type: bool
        """
        self._is_editable = is_editable

    @property
    def is_service_defined(self):
        """
        Gets the is_service_defined of this CustomProperty.
        If this field is defined by service or by a user


        :return: The is_service_defined of this CustomProperty.
        :rtype: bool
        """
        return self._is_service_defined

    @is_service_defined.setter
    def is_service_defined(self, is_service_defined):
        """
        Sets the is_service_defined of this CustomProperty.
        If this field is defined by service or by a user


        :param is_service_defined: The is_service_defined of this CustomProperty.
        :type: bool
        """
        self._is_service_defined = is_service_defined

    @property
    def is_hidden_in_search(self):
        """
        Gets the is_hidden_in_search of this CustomProperty.
        If this field is allowed to pop in search results


        :return: The is_hidden_in_search of this CustomProperty.
        :rtype: bool
        """
        return self._is_hidden_in_search

    @is_hidden_in_search.setter
    def is_hidden_in_search(self, is_hidden_in_search):
        """
        Sets the is_hidden_in_search of this CustomProperty.
        If this field is allowed to pop in search results


        :param is_hidden_in_search: The is_hidden_in_search of this CustomProperty.
        :type: bool
        """
        self._is_hidden_in_search = is_hidden_in_search

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CustomProperty.
        The current state of the custom property.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CustomProperty.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CustomProperty.
        The current state of the custom property.


        :param lifecycle_state: The lifecycle_state of this CustomProperty.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this CustomProperty.
        The date and time the custom property was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CustomProperty.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CustomProperty.
        The date and time the custom property was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CustomProperty.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this CustomProperty.
        The last time that any change was made to the custom property. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this CustomProperty.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this CustomProperty.
        The last time that any change was made to the custom property. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this CustomProperty.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this CustomProperty.
        OCID of the user who created the custom property.


        :return: The created_by_id of this CustomProperty.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this CustomProperty.
        OCID of the user who created the custom property.


        :param created_by_id: The created_by_id of this CustomProperty.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this CustomProperty.
        OCID of the user who last modified the custom property.


        :return: The updated_by_id of this CustomProperty.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this CustomProperty.
        OCID of the user who last modified the custom property.


        :param updated_by_id: The updated_by_id of this CustomProperty.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def usage_count(self):
        """
        Gets the usage_count of this CustomProperty.
        Total number of first class objects using this custom property


        :return: The usage_count of this CustomProperty.
        :rtype: int
        """
        return self._usage_count

    @usage_count.setter
    def usage_count(self, usage_count):
        """
        Sets the usage_count of this CustomProperty.
        Total number of first class objects using this custom property


        :param usage_count: The usage_count of this CustomProperty.
        :type: int
        """
        self._usage_count = usage_count

    @property
    def scope(self):
        """
        Gets the scope of this CustomProperty.
        Type or scope of the custom property belongs to. This will be an array of type id it will be belongs to


        :return: The scope of this CustomProperty.
        :rtype: list[oci.data_catalog.models.CustomPropertyTypeUsage]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this CustomProperty.
        Type or scope of the custom property belongs to. This will be an array of type id it will be belongs to


        :param scope: The scope of this CustomProperty.
        :type: list[oci.data_catalog.models.CustomPropertyTypeUsage]
        """
        self._scope = scope

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this CustomProperty.
        Allowed values for the custom property if any


        :return: The allowed_values of this CustomProperty.
        :rtype: list[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this CustomProperty.
        Allowed values for the custom property if any


        :param allowed_values: The allowed_values of this CustomProperty.
        :type: list[str]
        """
        self._allowed_values = allowed_values

    @property
    def properties(self):
        """
        Gets the properties of this CustomProperty.
        A map of maps that contains the properties which are specific to the asset type. Each data asset type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data assets have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :return: The properties of this CustomProperty.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CustomProperty.
        A map of maps that contains the properties which are specific to the asset type. Each data asset type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data assets have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :param properties: The properties of this CustomProperty.
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
