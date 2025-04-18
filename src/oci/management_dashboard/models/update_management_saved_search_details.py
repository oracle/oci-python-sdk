# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateManagementSavedSearchDetails(object):
    """
    Properties of a saved search.  Saved search ID must not be provided.
    """

    #: A constant which can be used with the type property of a UpdateManagementSavedSearchDetails.
    #: This constant has a value of "SEARCH_SHOW_IN_DASHBOARD"
    TYPE_SEARCH_SHOW_IN_DASHBOARD = "SEARCH_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a UpdateManagementSavedSearchDetails.
    #: This constant has a value of "SEARCH_DONT_SHOW_IN_DASHBOARD"
    TYPE_SEARCH_DONT_SHOW_IN_DASHBOARD = "SEARCH_DONT_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a UpdateManagementSavedSearchDetails.
    #: This constant has a value of "WIDGET_SHOW_IN_DASHBOARD"
    TYPE_WIDGET_SHOW_IN_DASHBOARD = "WIDGET_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a UpdateManagementSavedSearchDetails.
    #: This constant has a value of "WIDGET_DONT_SHOW_IN_DASHBOARD"
    TYPE_WIDGET_DONT_SHOW_IN_DASHBOARD = "WIDGET_DONT_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a UpdateManagementSavedSearchDetails.
    #: This constant has a value of "FILTER_SHOW_IN_DASHBOARD"
    TYPE_FILTER_SHOW_IN_DASHBOARD = "FILTER_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a UpdateManagementSavedSearchDetails.
    #: This constant has a value of "FILTER_DONT_SHOW_IN_DASHBOARD"
    TYPE_FILTER_DONT_SHOW_IN_DASHBOARD = "FILTER_DONT_SHOW_IN_DASHBOARD"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateManagementSavedSearchDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateManagementSavedSearchDetails.
        :type display_name: str

        :param provider_id:
            The value to assign to the provider_id property of this UpdateManagementSavedSearchDetails.
        :type provider_id: str

        :param provider_version:
            The value to assign to the provider_version property of this UpdateManagementSavedSearchDetails.
        :type provider_version: str

        :param provider_name:
            The value to assign to the provider_name property of this UpdateManagementSavedSearchDetails.
        :type provider_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateManagementSavedSearchDetails.
        :type compartment_id: str

        :param is_oob_saved_search:
            The value to assign to the is_oob_saved_search property of this UpdateManagementSavedSearchDetails.
        :type is_oob_saved_search: bool

        :param description:
            The value to assign to the description property of this UpdateManagementSavedSearchDetails.
        :type description: str

        :param nls:
            The value to assign to the nls property of this UpdateManagementSavedSearchDetails.
        :type nls: object

        :param type:
            The value to assign to the type property of this UpdateManagementSavedSearchDetails.
            Allowed values for this property are: "SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD", "FILTER_SHOW_IN_DASHBOARD", "FILTER_DONT_SHOW_IN_DASHBOARD"
        :type type: str

        :param ui_config:
            The value to assign to the ui_config property of this UpdateManagementSavedSearchDetails.
        :type ui_config: object

        :param data_config:
            The value to assign to the data_config property of this UpdateManagementSavedSearchDetails.
        :type data_config: list[object]

        :param screen_image:
            The value to assign to the screen_image property of this UpdateManagementSavedSearchDetails.
        :type screen_image: str

        :param metadata_version:
            The value to assign to the metadata_version property of this UpdateManagementSavedSearchDetails.
        :type metadata_version: str

        :param widget_template:
            The value to assign to the widget_template property of this UpdateManagementSavedSearchDetails.
        :type widget_template: str

        :param widget_vm:
            The value to assign to the widget_vm property of this UpdateManagementSavedSearchDetails.
        :type widget_vm: str

        :param parameters_config:
            The value to assign to the parameters_config property of this UpdateManagementSavedSearchDetails.
        :type parameters_config: list[object]

        :param features_config:
            The value to assign to the features_config property of this UpdateManagementSavedSearchDetails.
        :type features_config: object

        :param drilldown_config:
            The value to assign to the drilldown_config property of this UpdateManagementSavedSearchDetails.
        :type drilldown_config: list[object]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateManagementSavedSearchDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateManagementSavedSearchDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'provider_id': 'str',
            'provider_version': 'str',
            'provider_name': 'str',
            'compartment_id': 'str',
            'is_oob_saved_search': 'bool',
            'description': 'str',
            'nls': 'object',
            'type': 'str',
            'ui_config': 'object',
            'data_config': 'list[object]',
            'screen_image': 'str',
            'metadata_version': 'str',
            'widget_template': 'str',
            'widget_vm': 'str',
            'parameters_config': 'list[object]',
            'features_config': 'object',
            'drilldown_config': 'list[object]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'provider_id': 'providerId',
            'provider_version': 'providerVersion',
            'provider_name': 'providerName',
            'compartment_id': 'compartmentId',
            'is_oob_saved_search': 'isOobSavedSearch',
            'description': 'description',
            'nls': 'nls',
            'type': 'type',
            'ui_config': 'uiConfig',
            'data_config': 'dataConfig',
            'screen_image': 'screenImage',
            'metadata_version': 'metadataVersion',
            'widget_template': 'widgetTemplate',
            'widget_vm': 'widgetVM',
            'parameters_config': 'parametersConfig',
            'features_config': 'featuresConfig',
            'drilldown_config': 'drilldownConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._provider_id = None
        self._provider_version = None
        self._provider_name = None
        self._compartment_id = None
        self._is_oob_saved_search = None
        self._description = None
        self._nls = None
        self._type = None
        self._ui_config = None
        self._data_config = None
        self._screen_image = None
        self._metadata_version = None
        self._widget_template = None
        self._widget_vm = None
        self._parameters_config = None
        self._features_config = None
        self._drilldown_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateManagementSavedSearchDetails.
        Display name of the saved search.


        :return: The display_name of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateManagementSavedSearchDetails.
        Display name of the saved search.


        :param display_name: The display_name of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def provider_id(self):
        """
        Gets the provider_id of this UpdateManagementSavedSearchDetails.
        ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.


        :return: The provider_id of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """
        Sets the provider_id of this UpdateManagementSavedSearchDetails.
        ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.


        :param provider_id: The provider_id of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._provider_id = provider_id

    @property
    def provider_version(self):
        """
        Gets the provider_version of this UpdateManagementSavedSearchDetails.
        The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.


        :return: The provider_version of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._provider_version

    @provider_version.setter
    def provider_version(self, provider_version):
        """
        Sets the provider_version of this UpdateManagementSavedSearchDetails.
        The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.


        :param provider_version: The provider_version of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._provider_version = provider_version

    @property
    def provider_name(self):
        """
        Gets the provider_name of this UpdateManagementSavedSearchDetails.
        The user friendly name of the service (for example, Logging Analytics) that owns the saved search.


        :return: The provider_name of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """
        Sets the provider_name of this UpdateManagementSavedSearchDetails.
        The user friendly name of the service (for example, Logging Analytics) that owns the saved search.


        :param provider_name: The provider_name of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UpdateManagementSavedSearchDetails.
        OCID of the compartment in which the saved search resides.


        :return: The compartment_id of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UpdateManagementSavedSearchDetails.
        OCID of the compartment in which the saved search resides.


        :param compartment_id: The compartment_id of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_oob_saved_search(self):
        """
        Gets the is_oob_saved_search of this UpdateManagementSavedSearchDetails.
        Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.


        :return: The is_oob_saved_search of this UpdateManagementSavedSearchDetails.
        :rtype: bool
        """
        return self._is_oob_saved_search

    @is_oob_saved_search.setter
    def is_oob_saved_search(self, is_oob_saved_search):
        """
        Sets the is_oob_saved_search of this UpdateManagementSavedSearchDetails.
        Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.


        :param is_oob_saved_search: The is_oob_saved_search of this UpdateManagementSavedSearchDetails.
        :type: bool
        """
        self._is_oob_saved_search = is_oob_saved_search

    @property
    def description(self):
        """
        Gets the description of this UpdateManagementSavedSearchDetails.
        Description of the saved search.


        :return: The description of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateManagementSavedSearchDetails.
        Description of the saved search.


        :param description: The description of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._description = description

    @property
    def nls(self):
        """
        Gets the nls of this UpdateManagementSavedSearchDetails.
        JSON that contains internationalization options.


        :return: The nls of this UpdateManagementSavedSearchDetails.
        :rtype: object
        """
        return self._nls

    @nls.setter
    def nls(self, nls):
        """
        Sets the nls of this UpdateManagementSavedSearchDetails.
        JSON that contains internationalization options.


        :param nls: The nls of this UpdateManagementSavedSearchDetails.
        :type: object
        """
        self._nls = nls

    @property
    def type(self):
        """
        Gets the type of this UpdateManagementSavedSearchDetails.
        Determines how the saved search is displayed in a dashboard.

        Allowed values for this property are: "SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD", "FILTER_SHOW_IN_DASHBOARD", "FILTER_DONT_SHOW_IN_DASHBOARD"


        :return: The type of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateManagementSavedSearchDetails.
        Determines how the saved search is displayed in a dashboard.


        :param type: The type of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        allowed_values = ["SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD", "FILTER_SHOW_IN_DASHBOARD", "FILTER_DONT_SHOW_IN_DASHBOARD"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def ui_config(self):
        """
        Gets the ui_config of this UpdateManagementSavedSearchDetails.
        It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.


        :return: The ui_config of this UpdateManagementSavedSearchDetails.
        :rtype: object
        """
        return self._ui_config

    @ui_config.setter
    def ui_config(self, ui_config):
        """
        Sets the ui_config of this UpdateManagementSavedSearchDetails.
        It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.


        :param ui_config: The ui_config of this UpdateManagementSavedSearchDetails.
        :type: object
        """
        self._ui_config = ui_config

    @property
    def data_config(self):
        """
        Gets the data_config of this UpdateManagementSavedSearchDetails.
        It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data sources.


        :return: The data_config of this UpdateManagementSavedSearchDetails.
        :rtype: list[object]
        """
        return self._data_config

    @data_config.setter
    def data_config(self, data_config):
        """
        Sets the data_config of this UpdateManagementSavedSearchDetails.
        It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data sources.


        :param data_config: The data_config of this UpdateManagementSavedSearchDetails.
        :type: list[object]
        """
        self._data_config = data_config

    @property
    def screen_image(self):
        """
        Gets the screen_image of this UpdateManagementSavedSearchDetails.
        Screen image of the saved search.


        :return: The screen_image of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._screen_image

    @screen_image.setter
    def screen_image(self, screen_image):
        """
        Sets the screen_image of this UpdateManagementSavedSearchDetails.
        Screen image of the saved search.


        :param screen_image: The screen_image of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._screen_image = screen_image

    @property
    def metadata_version(self):
        """
        Gets the metadata_version of this UpdateManagementSavedSearchDetails.
        The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.


        :return: The metadata_version of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._metadata_version

    @metadata_version.setter
    def metadata_version(self, metadata_version):
        """
        Sets the metadata_version of this UpdateManagementSavedSearchDetails.
        The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.


        :param metadata_version: The metadata_version of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._metadata_version = metadata_version

    @property
    def widget_template(self):
        """
        Gets the widget_template of this UpdateManagementSavedSearchDetails.
        The UI template that the saved search uses to render itself.


        :return: The widget_template of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._widget_template

    @widget_template.setter
    def widget_template(self, widget_template):
        """
        Sets the widget_template of this UpdateManagementSavedSearchDetails.
        The UI template that the saved search uses to render itself.


        :param widget_template: The widget_template of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._widget_template = widget_template

    @property
    def widget_vm(self):
        """
        Gets the widget_vm of this UpdateManagementSavedSearchDetails.
        The View Model that the saved search uses to render itself.


        :return: The widget_vm of this UpdateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._widget_vm

    @widget_vm.setter
    def widget_vm(self, widget_vm):
        """
        Sets the widget_vm of this UpdateManagementSavedSearchDetails.
        The View Model that the saved search uses to render itself.


        :param widget_vm: The widget_vm of this UpdateManagementSavedSearchDetails.
        :type: str
        """
        self._widget_vm = widget_vm

    @property
    def parameters_config(self):
        """
        Gets the parameters_config of this UpdateManagementSavedSearchDetails.
        Defines parameters for the saved search.


        :return: The parameters_config of this UpdateManagementSavedSearchDetails.
        :rtype: list[object]
        """
        return self._parameters_config

    @parameters_config.setter
    def parameters_config(self, parameters_config):
        """
        Sets the parameters_config of this UpdateManagementSavedSearchDetails.
        Defines parameters for the saved search.


        :param parameters_config: The parameters_config of this UpdateManagementSavedSearchDetails.
        :type: list[object]
        """
        self._parameters_config = parameters_config

    @property
    def features_config(self):
        """
        Gets the features_config of this UpdateManagementSavedSearchDetails.
        Contains configuration for enabling features.


        :return: The features_config of this UpdateManagementSavedSearchDetails.
        :rtype: object
        """
        return self._features_config

    @features_config.setter
    def features_config(self, features_config):
        """
        Sets the features_config of this UpdateManagementSavedSearchDetails.
        Contains configuration for enabling features.


        :param features_config: The features_config of this UpdateManagementSavedSearchDetails.
        :type: object
        """
        self._features_config = features_config

    @property
    def drilldown_config(self):
        """
        Gets the drilldown_config of this UpdateManagementSavedSearchDetails.
        Drill-down configuration to define the destination of a drill-down action.


        :return: The drilldown_config of this UpdateManagementSavedSearchDetails.
        :rtype: list[object]
        """
        return self._drilldown_config

    @drilldown_config.setter
    def drilldown_config(self, drilldown_config):
        """
        Sets the drilldown_config of this UpdateManagementSavedSearchDetails.
        Drill-down configuration to define the destination of a drill-down action.


        :param drilldown_config: The drilldown_config of this UpdateManagementSavedSearchDetails.
        :type: list[object]
        """
        self._drilldown_config = drilldown_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateManagementSavedSearchDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateManagementSavedSearchDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateManagementSavedSearchDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateManagementSavedSearchDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateManagementSavedSearchDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateManagementSavedSearchDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateManagementSavedSearchDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateManagementSavedSearchDetails.
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
