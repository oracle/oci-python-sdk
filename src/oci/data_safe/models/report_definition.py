# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReportDefinition(object):
    """
    Description of report definition.
    """

    #: A constant which can be used with the category property of a ReportDefinition.
    #: This constant has a value of "CUSTOM_REPORTS"
    CATEGORY_CUSTOM_REPORTS = "CUSTOM_REPORTS"

    #: A constant which can be used with the category property of a ReportDefinition.
    #: This constant has a value of "SUMMARY"
    CATEGORY_SUMMARY = "SUMMARY"

    #: A constant which can be used with the category property of a ReportDefinition.
    #: This constant has a value of "ACTIVITY_AUDITING"
    CATEGORY_ACTIVITY_AUDITING = "ACTIVITY_AUDITING"

    #: A constant which can be used with the data_source property of a ReportDefinition.
    #: This constant has a value of "EVENTS"
    DATA_SOURCE_EVENTS = "EVENTS"

    #: A constant which can be used with the data_source property of a ReportDefinition.
    #: This constant has a value of "ALERTS"
    DATA_SOURCE_ALERTS = "ALERTS"

    #: A constant which can be used with the lifecycle_state property of a ReportDefinition.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ReportDefinition.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ReportDefinition.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ReportDefinition.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ReportDefinition.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ReportDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this ReportDefinition.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ReportDefinition.
        :type id: str

        :param parent_id:
            The value to assign to the parent_id property of this ReportDefinition.
        :type parent_id: str

        :param category:
            The value to assign to the category property of this ReportDefinition.
            Allowed values for this property are: "CUSTOM_REPORTS", "SUMMARY", "ACTIVITY_AUDITING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type category: str

        :param description:
            The value to assign to the description property of this ReportDefinition.
        :type description: str

        :param data_source:
            The value to assign to the data_source property of this ReportDefinition.
            Allowed values for this property are: "EVENTS", "ALERTS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_source: str

        :param is_seeded:
            The value to assign to the is_seeded property of this ReportDefinition.
        :type is_seeded: bool

        :param display_order:
            The value to assign to the display_order property of this ReportDefinition.
        :type display_order: int

        :param time_created:
            The value to assign to the time_created property of this ReportDefinition.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ReportDefinition.
        :type time_updated: datetime

        :param scim_filter:
            The value to assign to the scim_filter property of this ReportDefinition.
        :type scim_filter: str

        :param column_info:
            The value to assign to the column_info property of this ReportDefinition.
        :type column_info: list[oci.data_safe.models.Column]

        :param column_filters:
            The value to assign to the column_filters property of this ReportDefinition.
        :type column_filters: list[oci.data_safe.models.ColumnFilter]

        :param column_sortings:
            The value to assign to the column_sortings property of this ReportDefinition.
        :type column_sortings: list[oci.data_safe.models.ColumnSorting]

        :param summary:
            The value to assign to the summary property of this ReportDefinition.
        :type summary: list[oci.data_safe.models.Summary]

        :param compartment_id:
            The value to assign to the compartment_id property of this ReportDefinition.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ReportDefinition.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ReportDefinition.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ReportDefinition.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ReportDefinition.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'id': 'str',
            'parent_id': 'str',
            'category': 'str',
            'description': 'str',
            'data_source': 'str',
            'is_seeded': 'bool',
            'display_order': 'int',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'scim_filter': 'str',
            'column_info': 'list[Column]',
            'column_filters': 'list[ColumnFilter]',
            'column_sortings': 'list[ColumnSorting]',
            'summary': 'list[Summary]',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'id': 'id',
            'parent_id': 'parentId',
            'category': 'category',
            'description': 'description',
            'data_source': 'dataSource',
            'is_seeded': 'isSeeded',
            'display_order': 'displayOrder',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'scim_filter': 'scimFilter',
            'column_info': 'columnInfo',
            'column_filters': 'columnFilters',
            'column_sortings': 'columnSortings',
            'summary': 'summary',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._display_name = None
        self._id = None
        self._parent_id = None
        self._category = None
        self._description = None
        self._data_source = None
        self._is_seeded = None
        self._display_order = None
        self._time_created = None
        self._time_updated = None
        self._scim_filter = None
        self._column_info = None
        self._column_filters = None
        self._column_sortings = None
        self._summary = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ReportDefinition.
        Name of the report definition.


        :return: The display_name of this ReportDefinition.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ReportDefinition.
        Name of the report definition.


        :param display_name: The display_name of this ReportDefinition.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ReportDefinition.
        The OCID of the report definition.


        :return: The id of this ReportDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReportDefinition.
        The OCID of the report definition.


        :param id: The id of this ReportDefinition.
        :type: str
        """
        self._id = id

    @property
    def parent_id(self):
        """
        Gets the parent_id of this ReportDefinition.
        The OCID of the parent report definition. In the case of seeded report definition, this is same as definition OCID.


        :return: The parent_id of this ReportDefinition.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this ReportDefinition.
        The OCID of the parent report definition. In the case of seeded report definition, this is same as definition OCID.


        :param parent_id: The parent_id of this ReportDefinition.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def category(self):
        """
        Gets the category of this ReportDefinition.
        Specifies the name of the category that this report belongs to.

        Allowed values for this property are: "CUSTOM_REPORTS", "SUMMARY", "ACTIVITY_AUDITING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The category of this ReportDefinition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this ReportDefinition.
        Specifies the name of the category that this report belongs to.


        :param category: The category of this ReportDefinition.
        :type: str
        """
        allowed_values = ["CUSTOM_REPORTS", "SUMMARY", "ACTIVITY_AUDITING"]
        if not value_allowed_none_or_none_sentinel(category, allowed_values):
            category = 'UNKNOWN_ENUM_VALUE'
        self._category = category

    @property
    def description(self):
        """
        Gets the description of this ReportDefinition.
        A description of the report definition.


        :return: The description of this ReportDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ReportDefinition.
        A description of the report definition.


        :param description: The description of this ReportDefinition.
        :type: str
        """
        self._description = description

    @property
    def data_source(self):
        """
        Gets the data_source of this ReportDefinition.
        Specifies the name of a resource that provides data for the report. For example alerts, events.

        Allowed values for this property are: "EVENTS", "ALERTS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_source of this ReportDefinition.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """
        Sets the data_source of this ReportDefinition.
        Specifies the name of a resource that provides data for the report. For example alerts, events.


        :param data_source: The data_source of this ReportDefinition.
        :type: str
        """
        allowed_values = ["EVENTS", "ALERTS"]
        if not value_allowed_none_or_none_sentinel(data_source, allowed_values):
            data_source = 'UNKNOWN_ENUM_VALUE'
        self._data_source = data_source

    @property
    def is_seeded(self):
        """
        Gets the is_seeded of this ReportDefinition.
        Signifies whether the definition is seeded or user defined. Values can either be 'true' or 'false'.


        :return: The is_seeded of this ReportDefinition.
        :rtype: bool
        """
        return self._is_seeded

    @is_seeded.setter
    def is_seeded(self, is_seeded):
        """
        Sets the is_seeded of this ReportDefinition.
        Signifies whether the definition is seeded or user defined. Values can either be 'true' or 'false'.


        :param is_seeded: The is_seeded of this ReportDefinition.
        :type: bool
        """
        self._is_seeded = is_seeded

    @property
    def display_order(self):
        """
        Gets the display_order of this ReportDefinition.
        Specifies how the report definitions are ordered in the display.


        :return: The display_order of this ReportDefinition.
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """
        Sets the display_order of this ReportDefinition.
        Specifies how the report definitions are ordered in the display.


        :param display_order: The display_order of this ReportDefinition.
        :type: int
        """
        self._display_order = display_order

    @property
    def time_created(self):
        """
        Gets the time_created of this ReportDefinition.
        Specifies the time at which the report definition was created.


        :return: The time_created of this ReportDefinition.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ReportDefinition.
        Specifies the time at which the report definition was created.


        :param time_created: The time_created of this ReportDefinition.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ReportDefinition.
        The date and time of the report definition update in Data Safe.


        :return: The time_updated of this ReportDefinition.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ReportDefinition.
        The date and time of the report definition update in Data Safe.


        :param time_updated: The time_updated of this ReportDefinition.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def scim_filter(self):
        """
        Gets the scim_filter of this ReportDefinition.
        Additional scim filters used to specialize the report.


        :return: The scim_filter of this ReportDefinition.
        :rtype: str
        """
        return self._scim_filter

    @scim_filter.setter
    def scim_filter(self, scim_filter):
        """
        Sets the scim_filter of this ReportDefinition.
        Additional scim filters used to specialize the report.


        :param scim_filter: The scim_filter of this ReportDefinition.
        :type: str
        """
        self._scim_filter = scim_filter

    @property
    def column_info(self):
        """
        Gets the column_info of this ReportDefinition.
        An array of column objects in the order (left to right) displayed in the report. A column object stores all information about a column, including the name displayed on the UI, corresponding field name in the data source, data type of the column, and column visibility (if the column is visible to the user).


        :return: The column_info of this ReportDefinition.
        :rtype: list[oci.data_safe.models.Column]
        """
        return self._column_info

    @column_info.setter
    def column_info(self, column_info):
        """
        Sets the column_info of this ReportDefinition.
        An array of column objects in the order (left to right) displayed in the report. A column object stores all information about a column, including the name displayed on the UI, corresponding field name in the data source, data type of the column, and column visibility (if the column is visible to the user).


        :param column_info: The column_info of this ReportDefinition.
        :type: list[oci.data_safe.models.Column]
        """
        self._column_info = column_info

    @property
    def column_filters(self):
        """
        Gets the column_filters of this ReportDefinition.
        An array of column filter objects. A column Filter object stores all information about a column filter including field name, an operator, one or more expressions, if the filter is enabled, or if the filter is hidden.


        :return: The column_filters of this ReportDefinition.
        :rtype: list[oci.data_safe.models.ColumnFilter]
        """
        return self._column_filters

    @column_filters.setter
    def column_filters(self, column_filters):
        """
        Sets the column_filters of this ReportDefinition.
        An array of column filter objects. A column Filter object stores all information about a column filter including field name, an operator, one or more expressions, if the filter is enabled, or if the filter is hidden.


        :param column_filters: The column_filters of this ReportDefinition.
        :type: list[oci.data_safe.models.ColumnFilter]
        """
        self._column_filters = column_filters

    @property
    def column_sortings(self):
        """
        Gets the column_sortings of this ReportDefinition.
        An array of column sorting objects. Each column sorting object stores the column name to be sorted and if the sorting is in ascending order; sorting is done by the first column in the array, then by the second column in the array, etc.


        :return: The column_sortings of this ReportDefinition.
        :rtype: list[oci.data_safe.models.ColumnSorting]
        """
        return self._column_sortings

    @column_sortings.setter
    def column_sortings(self, column_sortings):
        """
        Sets the column_sortings of this ReportDefinition.
        An array of column sorting objects. Each column sorting object stores the column name to be sorted and if the sorting is in ascending order; sorting is done by the first column in the array, then by the second column in the array, etc.


        :param column_sortings: The column_sortings of this ReportDefinition.
        :type: list[oci.data_safe.models.ColumnSorting]
        """
        self._column_sortings = column_sortings

    @property
    def summary(self):
        """
        Gets the summary of this ReportDefinition.
        An array of report summary objects in the order (left to right)  displayed in the report.  A  report summary object stores all information about summary of report to be displayed, including the name displayed on UI, the display order, corresponding group by and count of values, summary visibility (if the summary is visible to user).


        :return: The summary of this ReportDefinition.
        :rtype: list[oci.data_safe.models.Summary]
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this ReportDefinition.
        An array of report summary objects in the order (left to right)  displayed in the report.  A  report summary object stores all information about summary of report to be displayed, including the name displayed on UI, the display order, corresponding group by and count of values, summary visibility (if the summary is visible to user).


        :param summary: The summary of this ReportDefinition.
        :type: list[oci.data_safe.models.Summary]
        """
        self._summary = summary

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ReportDefinition.
        The OCID of the compartment containing the report definition.


        :return: The compartment_id of this ReportDefinition.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ReportDefinition.
        The OCID of the compartment containing the report definition.


        :param compartment_id: The compartment_id of this ReportDefinition.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ReportDefinition.
        The current state of the report.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ReportDefinition.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ReportDefinition.
        The current state of the report.


        :param lifecycle_state: The lifecycle_state of this ReportDefinition.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ReportDefinition.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ReportDefinition.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ReportDefinition.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ReportDefinition.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ReportDefinition.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ReportDefinition.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ReportDefinition.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ReportDefinition.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ReportDefinition.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ReportDefinition.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ReportDefinition.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ReportDefinition.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
