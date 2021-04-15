# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomPropertySummary(object):
    """
    Summary of a custom property
    """

    #: A constant which can be used with the data_type property of a CustomPropertySummary.
    #: This constant has a value of "TEXT"
    DATA_TYPE_TEXT = "TEXT"

    #: A constant which can be used with the data_type property of a CustomPropertySummary.
    #: This constant has a value of "RICH_TEXT"
    DATA_TYPE_RICH_TEXT = "RICH_TEXT"

    #: A constant which can be used with the data_type property of a CustomPropertySummary.
    #: This constant has a value of "BOOLEAN"
    DATA_TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the data_type property of a CustomPropertySummary.
    #: This constant has a value of "NUMBER"
    DATA_TYPE_NUMBER = "NUMBER"

    #: A constant which can be used with the data_type property of a CustomPropertySummary.
    #: This constant has a value of "DATE"
    DATA_TYPE_DATE = "DATE"

    #: A constant which can be used with the lifecycle_state property of a CustomPropertySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CustomPropertySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CustomPropertySummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CustomPropertySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CustomPropertySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CustomPropertySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CustomPropertySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a CustomPropertySummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new CustomPropertySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CustomPropertySummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this CustomPropertySummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CustomPropertySummary.
        :type description: str

        :param data_type:
            The value to assign to the data_type property of this CustomPropertySummary.
            Allowed values for this property are: "TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_type: str

        :param namespace_name:
            The value to assign to the namespace_name property of this CustomPropertySummary.
        :type namespace_name: str

        :param is_sortable:
            The value to assign to the is_sortable property of this CustomPropertySummary.
        :type is_sortable: bool

        :param is_filterable:
            The value to assign to the is_filterable property of this CustomPropertySummary.
        :type is_filterable: bool

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this CustomPropertySummary.
        :type is_multi_valued: bool

        :param is_hidden:
            The value to assign to the is_hidden property of this CustomPropertySummary.
        :type is_hidden: bool

        :param is_editable:
            The value to assign to the is_editable property of this CustomPropertySummary.
        :type is_editable: bool

        :param is_shown_in_list:
            The value to assign to the is_shown_in_list property of this CustomPropertySummary.
        :type is_shown_in_list: bool

        :param is_service_defined:
            The value to assign to the is_service_defined property of this CustomPropertySummary.
        :type is_service_defined: bool

        :param is_hidden_in_search:
            The value to assign to the is_hidden_in_search property of this CustomPropertySummary.
        :type is_hidden_in_search: bool

        :param time_created:
            The value to assign to the time_created property of this CustomPropertySummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CustomPropertySummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param usage_count:
            The value to assign to the usage_count property of this CustomPropertySummary.
        :type usage_count: int

        :param scope:
            The value to assign to the scope property of this CustomPropertySummary.
        :type scope: list[oci.data_catalog.models.CustomPropertyTypeUsage]

        :param allowed_values:
            The value to assign to the allowed_values property of this CustomPropertySummary.
        :type allowed_values: list[str]

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'data_type': 'str',
            'namespace_name': 'str',
            'is_sortable': 'bool',
            'is_filterable': 'bool',
            'is_multi_valued': 'bool',
            'is_hidden': 'bool',
            'is_editable': 'bool',
            'is_shown_in_list': 'bool',
            'is_service_defined': 'bool',
            'is_hidden_in_search': 'bool',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'usage_count': 'int',
            'scope': 'list[CustomPropertyTypeUsage]',
            'allowed_values': 'list[str]'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'data_type': 'dataType',
            'namespace_name': 'namespaceName',
            'is_sortable': 'isSortable',
            'is_filterable': 'isFilterable',
            'is_multi_valued': 'isMultiValued',
            'is_hidden': 'isHidden',
            'is_editable': 'isEditable',
            'is_shown_in_list': 'isShownInList',
            'is_service_defined': 'isServiceDefined',
            'is_hidden_in_search': 'isHiddenInSearch',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'usage_count': 'usageCount',
            'scope': 'scope',
            'allowed_values': 'allowedValues'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._data_type = None
        self._namespace_name = None
        self._is_sortable = None
        self._is_filterable = None
        self._is_multi_valued = None
        self._is_hidden = None
        self._is_editable = None
        self._is_shown_in_list = None
        self._is_service_defined = None
        self._is_hidden_in_search = None
        self._time_created = None
        self._lifecycle_state = None
        self._usage_count = None
        self._scope = None
        self._allowed_values = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this CustomPropertySummary.
        Unique custom property key that is immutable.


        :return: The key of this CustomPropertySummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CustomPropertySummary.
        Unique custom property key that is immutable.


        :param key: The key of this CustomPropertySummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this CustomPropertySummary.
        Display name of the custom property


        :return: The display_name of this CustomPropertySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CustomPropertySummary.
        Display name of the custom property


        :param display_name: The display_name of this CustomPropertySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CustomPropertySummary.
        Description of the custom property


        :return: The description of this CustomPropertySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CustomPropertySummary.
        Description of the custom property


        :param description: The description of this CustomPropertySummary.
        :type: str
        """
        self._description = description

    @property
    def data_type(self):
        """
        Gets the data_type of this CustomPropertySummary.
        Data type of the custom property

        Allowed values for this property are: "TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_type of this CustomPropertySummary.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this CustomPropertySummary.
        Data type of the custom property


        :param data_type: The data_type of this CustomPropertySummary.
        :type: str
        """
        allowed_values = ["TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE"]
        if not value_allowed_none_or_none_sentinel(data_type, allowed_values):
            data_type = 'UNKNOWN_ENUM_VALUE'
        self._data_type = data_type

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this CustomPropertySummary.
        Namespace name of the custom property


        :return: The namespace_name of this CustomPropertySummary.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this CustomPropertySummary.
        Namespace name of the custom property


        :param namespace_name: The namespace_name of this CustomPropertySummary.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def is_sortable(self):
        """
        Gets the is_sortable of this CustomPropertySummary.
        If this field allows to sort from UI


        :return: The is_sortable of this CustomPropertySummary.
        :rtype: bool
        """
        return self._is_sortable

    @is_sortable.setter
    def is_sortable(self, is_sortable):
        """
        Sets the is_sortable of this CustomPropertySummary.
        If this field allows to sort from UI


        :param is_sortable: The is_sortable of this CustomPropertySummary.
        :type: bool
        """
        self._is_sortable = is_sortable

    @property
    def is_filterable(self):
        """
        Gets the is_filterable of this CustomPropertySummary.
        If this field allows to filter or create facets from UI


        :return: The is_filterable of this CustomPropertySummary.
        :rtype: bool
        """
        return self._is_filterable

    @is_filterable.setter
    def is_filterable(self, is_filterable):
        """
        Sets the is_filterable of this CustomPropertySummary.
        If this field allows to filter or create facets from UI


        :param is_filterable: The is_filterable of this CustomPropertySummary.
        :type: bool
        """
        self._is_filterable = is_filterable

    @property
    def is_multi_valued(self):
        """
        Gets the is_multi_valued of this CustomPropertySummary.
        If this field allows multiple values to be set


        :return: The is_multi_valued of this CustomPropertySummary.
        :rtype: bool
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued):
        """
        Sets the is_multi_valued of this CustomPropertySummary.
        If this field allows multiple values to be set


        :param is_multi_valued: The is_multi_valued of this CustomPropertySummary.
        :type: bool
        """
        self._is_multi_valued = is_multi_valued

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this CustomPropertySummary.
        If this field is a hidden field


        :return: The is_hidden of this CustomPropertySummary.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this CustomPropertySummary.
        If this field is a hidden field


        :param is_hidden: The is_hidden of this CustomPropertySummary.
        :type: bool
        """
        self._is_hidden = is_hidden

    @property
    def is_editable(self):
        """
        Gets the is_editable of this CustomPropertySummary.
        If this field is a editable field


        :return: The is_editable of this CustomPropertySummary.
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """
        Sets the is_editable of this CustomPropertySummary.
        If this field is a editable field


        :param is_editable: The is_editable of this CustomPropertySummary.
        :type: bool
        """
        self._is_editable = is_editable

    @property
    def is_shown_in_list(self):
        """
        Gets the is_shown_in_list of this CustomPropertySummary.
        If this field is displayed in a list view of applicable objects.


        :return: The is_shown_in_list of this CustomPropertySummary.
        :rtype: bool
        """
        return self._is_shown_in_list

    @is_shown_in_list.setter
    def is_shown_in_list(self, is_shown_in_list):
        """
        Sets the is_shown_in_list of this CustomPropertySummary.
        If this field is displayed in a list view of applicable objects.


        :param is_shown_in_list: The is_shown_in_list of this CustomPropertySummary.
        :type: bool
        """
        self._is_shown_in_list = is_shown_in_list

    @property
    def is_service_defined(self):
        """
        Gets the is_service_defined of this CustomPropertySummary.
        If this field is defined by service or by a user


        :return: The is_service_defined of this CustomPropertySummary.
        :rtype: bool
        """
        return self._is_service_defined

    @is_service_defined.setter
    def is_service_defined(self, is_service_defined):
        """
        Sets the is_service_defined of this CustomPropertySummary.
        If this field is defined by service or by a user


        :param is_service_defined: The is_service_defined of this CustomPropertySummary.
        :type: bool
        """
        self._is_service_defined = is_service_defined

    @property
    def is_hidden_in_search(self):
        """
        Gets the is_hidden_in_search of this CustomPropertySummary.
        If this field is allowed to pop in search results


        :return: The is_hidden_in_search of this CustomPropertySummary.
        :rtype: bool
        """
        return self._is_hidden_in_search

    @is_hidden_in_search.setter
    def is_hidden_in_search(self, is_hidden_in_search):
        """
        Sets the is_hidden_in_search of this CustomPropertySummary.
        If this field is allowed to pop in search results


        :param is_hidden_in_search: The is_hidden_in_search of this CustomPropertySummary.
        :type: bool
        """
        self._is_hidden_in_search = is_hidden_in_search

    @property
    def time_created(self):
        """
        Gets the time_created of this CustomPropertySummary.
        The date and time the custom property was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CustomPropertySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CustomPropertySummary.
        The date and time the custom property was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CustomPropertySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CustomPropertySummary.
        The current state of the custom property.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CustomPropertySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CustomPropertySummary.
        The current state of the custom property.


        :param lifecycle_state: The lifecycle_state of this CustomPropertySummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def usage_count(self):
        """
        Gets the usage_count of this CustomPropertySummary.
        Total number of first class objects using this custom property


        :return: The usage_count of this CustomPropertySummary.
        :rtype: int
        """
        return self._usage_count

    @usage_count.setter
    def usage_count(self, usage_count):
        """
        Sets the usage_count of this CustomPropertySummary.
        Total number of first class objects using this custom property


        :param usage_count: The usage_count of this CustomPropertySummary.
        :type: int
        """
        self._usage_count = usage_count

    @property
    def scope(self):
        """
        Gets the scope of this CustomPropertySummary.
        Type or scope of the custom property belongs to. This will be an array of type id it will be belongs to


        :return: The scope of this CustomPropertySummary.
        :rtype: list[oci.data_catalog.models.CustomPropertyTypeUsage]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this CustomPropertySummary.
        Type or scope of the custom property belongs to. This will be an array of type id it will be belongs to


        :param scope: The scope of this CustomPropertySummary.
        :type: list[oci.data_catalog.models.CustomPropertyTypeUsage]
        """
        self._scope = scope

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this CustomPropertySummary.
        Allowed values for the custom property if any


        :return: The allowed_values of this CustomPropertySummary.
        :rtype: list[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this CustomPropertySummary.
        Allowed values for the custom property if any


        :param allowed_values: The allowed_values of this CustomPropertySummary.
        :type: list[str]
        """
        self._allowed_values = allowed_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
