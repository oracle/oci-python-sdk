# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementSavedSearchSummary(object):
    """
    Summary of the properties of a saved search.
    """

    #: A constant which can be used with the type property of a ManagementSavedSearchSummary.
    #: This constant has a value of "SEARCH_SHOW_IN_DASHBOARD"
    TYPE_SEARCH_SHOW_IN_DASHBOARD = "SEARCH_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a ManagementSavedSearchSummary.
    #: This constant has a value of "SEARCH_DONT_SHOW_IN_DASHBOARD"
    TYPE_SEARCH_DONT_SHOW_IN_DASHBOARD = "SEARCH_DONT_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a ManagementSavedSearchSummary.
    #: This constant has a value of "WIDGET_SHOW_IN_DASHBOARD"
    TYPE_WIDGET_SHOW_IN_DASHBOARD = "WIDGET_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a ManagementSavedSearchSummary.
    #: This constant has a value of "WIDGET_DONT_SHOW_IN_DASHBOARD"
    TYPE_WIDGET_DONT_SHOW_IN_DASHBOARD = "WIDGET_DONT_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the lifecycle_state property of a ManagementSavedSearchSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementSavedSearchSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagementSavedSearchSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ManagementSavedSearchSummary.
        :type display_name: str

        :param is_oob_saved_search:
            The value to assign to the is_oob_saved_search property of this ManagementSavedSearchSummary.
        :type is_oob_saved_search: bool

        :param provider_id:
            The value to assign to the provider_id property of this ManagementSavedSearchSummary.
        :type provider_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagementSavedSearchSummary.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this ManagementSavedSearchSummary.
        :type description: str

        :param nls:
            The value to assign to the nls property of this ManagementSavedSearchSummary.
        :type nls: object

        :param type:
            The value to assign to the type property of this ManagementSavedSearchSummary.
            Allowed values for this property are: "SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param ui_config:
            The value to assign to the ui_config property of this ManagementSavedSearchSummary.
        :type ui_config: object

        :param data_config:
            The value to assign to the data_config property of this ManagementSavedSearchSummary.
        :type data_config: list[object]

        :param created_by:
            The value to assign to the created_by property of this ManagementSavedSearchSummary.
        :type created_by: str

        :param updated_by:
            The value to assign to the updated_by property of this ManagementSavedSearchSummary.
        :type updated_by: str

        :param time_created:
            The value to assign to the time_created property of this ManagementSavedSearchSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ManagementSavedSearchSummary.
        :type time_updated: datetime

        :param screen_image:
            The value to assign to the screen_image property of this ManagementSavedSearchSummary.
        :type screen_image: str

        :param metadata_version:
            The value to assign to the metadata_version property of this ManagementSavedSearchSummary.
        :type metadata_version: str

        :param widget_template:
            The value to assign to the widget_template property of this ManagementSavedSearchSummary.
        :type widget_template: str

        :param widget_vm:
            The value to assign to the widget_vm property of this ManagementSavedSearchSummary.
        :type widget_vm: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagementSavedSearchSummary.
            Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagementSavedSearchSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagementSavedSearchSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'is_oob_saved_search': 'bool',
            'provider_id': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'nls': 'object',
            'type': 'str',
            'ui_config': 'object',
            'data_config': 'list[object]',
            'created_by': 'str',
            'updated_by': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'screen_image': 'str',
            'metadata_version': 'str',
            'widget_template': 'str',
            'widget_vm': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'is_oob_saved_search': 'isOobSavedSearch',
            'provider_id': 'providerId',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'nls': 'nls',
            'type': 'type',
            'ui_config': 'uiConfig',
            'data_config': 'dataConfig',
            'created_by': 'createdBy',
            'updated_by': 'updatedBy',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'screen_image': 'screenImage',
            'metadata_version': 'metadataVersion',
            'widget_template': 'widgetTemplate',
            'widget_vm': 'widgetVM',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._is_oob_saved_search = None
        self._provider_id = None
        self._compartment_id = None
        self._description = None
        self._nls = None
        self._type = None
        self._ui_config = None
        self._data_config = None
        self._created_by = None
        self._updated_by = None
        self._time_created = None
        self._time_updated = None
        self._screen_image = None
        self._metadata_version = None
        self._widget_template = None
        self._widget_vm = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagementSavedSearchSummary.
        ID of the saved search.


        :return: The id of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagementSavedSearchSummary.
        ID of the saved search.


        :param id: The id of this ManagementSavedSearchSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagementSavedSearchSummary.
        Display name of the saved search.


        :return: The display_name of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagementSavedSearchSummary.
        Display name of the saved search.


        :param display_name: The display_name of this ManagementSavedSearchSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_oob_saved_search(self):
        """
        **[Required]** Gets the is_oob_saved_search of this ManagementSavedSearchSummary.
        Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.


        :return: The is_oob_saved_search of this ManagementSavedSearchSummary.
        :rtype: bool
        """
        return self._is_oob_saved_search

    @is_oob_saved_search.setter
    def is_oob_saved_search(self, is_oob_saved_search):
        """
        Sets the is_oob_saved_search of this ManagementSavedSearchSummary.
        Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.


        :param is_oob_saved_search: The is_oob_saved_search of this ManagementSavedSearchSummary.
        :type: bool
        """
        self._is_oob_saved_search = is_oob_saved_search

    @property
    def provider_id(self):
        """
        **[Required]** Gets the provider_id of this ManagementSavedSearchSummary.
        ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.


        :return: The provider_id of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """
        Sets the provider_id of this ManagementSavedSearchSummary.
        ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.


        :param provider_id: The provider_id of this ManagementSavedSearchSummary.
        :type: str
        """
        self._provider_id = provider_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagementSavedSearchSummary.
        OCID of the compartment in which the saved search resides.


        :return: The compartment_id of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagementSavedSearchSummary.
        OCID of the compartment in which the saved search resides.


        :param compartment_id: The compartment_id of this ManagementSavedSearchSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        **[Required]** Gets the description of this ManagementSavedSearchSummary.
        Description of the saved search.


        :return: The description of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagementSavedSearchSummary.
        Description of the saved search.


        :param description: The description of this ManagementSavedSearchSummary.
        :type: str
        """
        self._description = description

    @property
    def nls(self):
        """
        **[Required]** Gets the nls of this ManagementSavedSearchSummary.
        JSON that contains internationalization options.


        :return: The nls of this ManagementSavedSearchSummary.
        :rtype: object
        """
        return self._nls

    @nls.setter
    def nls(self, nls):
        """
        Sets the nls of this ManagementSavedSearchSummary.
        JSON that contains internationalization options.


        :param nls: The nls of this ManagementSavedSearchSummary.
        :type: object
        """
        self._nls = nls

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ManagementSavedSearchSummary.
        Determines how the saved search is displayed in a dashboard.

        Allowed values for this property are: "SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ManagementSavedSearchSummary.
        Determines how the saved search is displayed in a dashboard.


        :param type: The type of this ManagementSavedSearchSummary.
        :type: str
        """
        allowed_values = ["SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def ui_config(self):
        """
        **[Required]** Gets the ui_config of this ManagementSavedSearchSummary.
        JSON that contains user interface options.


        :return: The ui_config of this ManagementSavedSearchSummary.
        :rtype: object
        """
        return self._ui_config

    @ui_config.setter
    def ui_config(self, ui_config):
        """
        Sets the ui_config of this ManagementSavedSearchSummary.
        JSON that contains user interface options.


        :param ui_config: The ui_config of this ManagementSavedSearchSummary.
        :type: object
        """
        self._ui_config = ui_config

    @property
    def data_config(self):
        """
        **[Required]** Gets the data_config of this ManagementSavedSearchSummary.
        Array of JSON that contain data source options.


        :return: The data_config of this ManagementSavedSearchSummary.
        :rtype: list[object]
        """
        return self._data_config

    @data_config.setter
    def data_config(self, data_config):
        """
        Sets the data_config of this ManagementSavedSearchSummary.
        Array of JSON that contain data source options.


        :param data_config: The data_config of this ManagementSavedSearchSummary.
        :type: list[object]
        """
        self._data_config = data_config

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this ManagementSavedSearchSummary.
        User who created the saved search.


        :return: The created_by of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this ManagementSavedSearchSummary.
        User who created the saved search.


        :param created_by: The created_by of this ManagementSavedSearchSummary.
        :type: str
        """
        self._created_by = created_by

    @property
    def updated_by(self):
        """
        **[Required]** Gets the updated_by of this ManagementSavedSearchSummary.
        User who updated the saved search.


        :return: The updated_by of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this ManagementSavedSearchSummary.
        User who updated the saved search.


        :param updated_by: The updated_by of this ManagementSavedSearchSummary.
        :type: str
        """
        self._updated_by = updated_by

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ManagementSavedSearchSummary.
        Date and time the saved search was created.


        :return: The time_created of this ManagementSavedSearchSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagementSavedSearchSummary.
        Date and time the saved search was created.


        :param time_created: The time_created of this ManagementSavedSearchSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ManagementSavedSearchSummary.
        Date and time the saved search was updated.


        :return: The time_updated of this ManagementSavedSearchSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ManagementSavedSearchSummary.
        Date and time the saved search was updated.


        :param time_updated: The time_updated of this ManagementSavedSearchSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def screen_image(self):
        """
        **[Required]** Gets the screen_image of this ManagementSavedSearchSummary.
        Screen image of the saved search.


        :return: The screen_image of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._screen_image

    @screen_image.setter
    def screen_image(self, screen_image):
        """
        Sets the screen_image of this ManagementSavedSearchSummary.
        Screen image of the saved search.


        :param screen_image: The screen_image of this ManagementSavedSearchSummary.
        :type: str
        """
        self._screen_image = screen_image

    @property
    def metadata_version(self):
        """
        **[Required]** Gets the metadata_version of this ManagementSavedSearchSummary.
        Version of the metadata.


        :return: The metadata_version of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._metadata_version

    @metadata_version.setter
    def metadata_version(self, metadata_version):
        """
        Sets the metadata_version of this ManagementSavedSearchSummary.
        Version of the metadata.


        :param metadata_version: The metadata_version of this ManagementSavedSearchSummary.
        :type: str
        """
        self._metadata_version = metadata_version

    @property
    def widget_template(self):
        """
        **[Required]** Gets the widget_template of this ManagementSavedSearchSummary.
        Reference to the HTML file of the widget.


        :return: The widget_template of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._widget_template

    @widget_template.setter
    def widget_template(self, widget_template):
        """
        Sets the widget_template of this ManagementSavedSearchSummary.
        Reference to the HTML file of the widget.


        :param widget_template: The widget_template of this ManagementSavedSearchSummary.
        :type: str
        """
        self._widget_template = widget_template

    @property
    def widget_vm(self):
        """
        **[Required]** Gets the widget_vm of this ManagementSavedSearchSummary.
        Reference to the view model of the widget.


        :return: The widget_vm of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._widget_vm

    @widget_vm.setter
    def widget_vm(self, widget_vm):
        """
        Sets the widget_vm of this ManagementSavedSearchSummary.
        Reference to the view model of the widget.


        :param widget_vm: The widget_vm of this ManagementSavedSearchSummary.
        :type: str
        """
        self._widget_vm = widget_vm

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ManagementSavedSearchSummary.
        Current lifecycle state of the saved search.

        Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ManagementSavedSearchSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagementSavedSearchSummary.
        Current lifecycle state of the saved search.


        :param lifecycle_state: The lifecycle_state of this ManagementSavedSearchSummary.
        :type: str
        """
        allowed_values = ["ACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ManagementSavedSearchSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ManagementSavedSearchSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagementSavedSearchSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ManagementSavedSearchSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ManagementSavedSearchSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ManagementSavedSearchSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagementSavedSearchSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ManagementSavedSearchSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
