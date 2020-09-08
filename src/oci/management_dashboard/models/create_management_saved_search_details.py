# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateManagementSavedSearchDetails(object):
    """
    Properties of a saved search.
    """

    #: A constant which can be used with the type property of a CreateManagementSavedSearchDetails.
    #: This constant has a value of "SEARCH_SHOW_IN_DASHBOARD"
    TYPE_SEARCH_SHOW_IN_DASHBOARD = "SEARCH_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a CreateManagementSavedSearchDetails.
    #: This constant has a value of "SEARCH_DONT_SHOW_IN_DASHBOARD"
    TYPE_SEARCH_DONT_SHOW_IN_DASHBOARD = "SEARCH_DONT_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a CreateManagementSavedSearchDetails.
    #: This constant has a value of "WIDGET_SHOW_IN_DASHBOARD"
    TYPE_WIDGET_SHOW_IN_DASHBOARD = "WIDGET_SHOW_IN_DASHBOARD"

    #: A constant which can be used with the type property of a CreateManagementSavedSearchDetails.
    #: This constant has a value of "WIDGET_DONT_SHOW_IN_DASHBOARD"
    TYPE_WIDGET_DONT_SHOW_IN_DASHBOARD = "WIDGET_DONT_SHOW_IN_DASHBOARD"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateManagementSavedSearchDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CreateManagementSavedSearchDetails.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this CreateManagementSavedSearchDetails.
        :type display_name: str

        :param provider_id:
            The value to assign to the provider_id property of this CreateManagementSavedSearchDetails.
        :type provider_id: str

        :param provider_version:
            The value to assign to the provider_version property of this CreateManagementSavedSearchDetails.
        :type provider_version: str

        :param provider_name:
            The value to assign to the provider_name property of this CreateManagementSavedSearchDetails.
        :type provider_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateManagementSavedSearchDetails.
        :type compartment_id: str

        :param is_oob_saved_search:
            The value to assign to the is_oob_saved_search property of this CreateManagementSavedSearchDetails.
        :type is_oob_saved_search: bool

        :param description:
            The value to assign to the description property of this CreateManagementSavedSearchDetails.
        :type description: str

        :param nls:
            The value to assign to the nls property of this CreateManagementSavedSearchDetails.
        :type nls: object

        :param type:
            The value to assign to the type property of this CreateManagementSavedSearchDetails.
            Allowed values for this property are: "SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD"
        :type type: str

        :param ui_config:
            The value to assign to the ui_config property of this CreateManagementSavedSearchDetails.
        :type ui_config: object

        :param data_config:
            The value to assign to the data_config property of this CreateManagementSavedSearchDetails.
        :type data_config: list[object]

        :param screen_image:
            The value to assign to the screen_image property of this CreateManagementSavedSearchDetails.
        :type screen_image: str

        :param metadata_version:
            The value to assign to the metadata_version property of this CreateManagementSavedSearchDetails.
        :type metadata_version: str

        :param widget_template:
            The value to assign to the widget_template property of this CreateManagementSavedSearchDetails.
        :type widget_template: str

        :param widget_vm:
            The value to assign to the widget_vm property of this CreateManagementSavedSearchDetails.
        :type widget_vm: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateManagementSavedSearchDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateManagementSavedSearchDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
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
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
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
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
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
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CreateManagementSavedSearchDetails.
        id for saved search.  Must be provided if OOB, otherwise must not be provided.


        :return: The id of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CreateManagementSavedSearchDetails.
        id for saved search.  Must be provided if OOB, otherwise must not be provided.


        :param id: The id of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateManagementSavedSearchDetails.
        Display name for saved search.


        :return: The display_name of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateManagementSavedSearchDetails.
        Display name for saved search.


        :param display_name: The display_name of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def provider_id(self):
        """
        **[Required]** Gets the provider_id of this CreateManagementSavedSearchDetails.
        Id for application (LA, APM, etc.) that owners this saved search.  Each owner has a unique Id.


        :return: The provider_id of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """
        Sets the provider_id of this CreateManagementSavedSearchDetails.
        Id for application (LA, APM, etc.) that owners this saved search.  Each owner has a unique Id.


        :param provider_id: The provider_id of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._provider_id = provider_id

    @property
    def provider_version(self):
        """
        **[Required]** Gets the provider_version of this CreateManagementSavedSearchDetails.
        Version.


        :return: The provider_version of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._provider_version

    @provider_version.setter
    def provider_version(self, provider_version):
        """
        Sets the provider_version of this CreateManagementSavedSearchDetails.
        Version.


        :param provider_version: The provider_version of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._provider_version = provider_version

    @property
    def provider_name(self):
        """
        **[Required]** Gets the provider_name of this CreateManagementSavedSearchDetails.
        Name for application (LA, APM, etc.) that owners this saved search.


        :return: The provider_name of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """
        Sets the provider_name of this CreateManagementSavedSearchDetails.
        Name for application (LA, APM, etc.) that owners this saved search.


        :param provider_name: The provider_name of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateManagementSavedSearchDetails.
        The ocid of the compartment that owns the saved search.


        :return: The compartment_id of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateManagementSavedSearchDetails.
        The ocid of the compartment that owns the saved search.


        :param compartment_id: The compartment_id of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_oob_saved_search(self):
        """
        **[Required]** Gets the is_oob_saved_search of this CreateManagementSavedSearchDetails.
        String boolean (\"true\" or \"false\") to indicate Out Of the Box saved search.


        :return: The is_oob_saved_search of this CreateManagementSavedSearchDetails.
        :rtype: bool
        """
        return self._is_oob_saved_search

    @is_oob_saved_search.setter
    def is_oob_saved_search(self, is_oob_saved_search):
        """
        Sets the is_oob_saved_search of this CreateManagementSavedSearchDetails.
        String boolean (\"true\" or \"false\") to indicate Out Of the Box saved search.


        :param is_oob_saved_search: The is_oob_saved_search of this CreateManagementSavedSearchDetails.
        :type: bool
        """
        self._is_oob_saved_search = is_oob_saved_search

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateManagementSavedSearchDetails.
        Description.


        :return: The description of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateManagementSavedSearchDetails.
        Description.


        :param description: The description of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._description = description

    @property
    def nls(self):
        """
        **[Required]** Gets the nls of this CreateManagementSavedSearchDetails.
        Json for internationalization.


        :return: The nls of this CreateManagementSavedSearchDetails.
        :rtype: object
        """
        return self._nls

    @nls.setter
    def nls(self, nls):
        """
        Sets the nls of this CreateManagementSavedSearchDetails.
        Json for internationalization.


        :param nls: The nls of this CreateManagementSavedSearchDetails.
        :type: object
        """
        self._nls = nls

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateManagementSavedSearchDetails.
        How to show the saved search.

        Allowed values for this property are: "SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD"


        :return: The type of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateManagementSavedSearchDetails.
        How to show the saved search.


        :param type: The type of this CreateManagementSavedSearchDetails.
        :type: str
        """
        allowed_values = ["SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def ui_config(self):
        """
        **[Required]** Gets the ui_config of this CreateManagementSavedSearchDetails.
        Json to contain options for UI.


        :return: The ui_config of this CreateManagementSavedSearchDetails.
        :rtype: object
        """
        return self._ui_config

    @ui_config.setter
    def ui_config(self, ui_config):
        """
        Sets the ui_config of this CreateManagementSavedSearchDetails.
        Json to contain options for UI.


        :param ui_config: The ui_config of this CreateManagementSavedSearchDetails.
        :type: object
        """
        self._ui_config = ui_config

    @property
    def data_config(self):
        """
        **[Required]** Gets the data_config of this CreateManagementSavedSearchDetails.
        Array of Json to contain options for source of data.


        :return: The data_config of this CreateManagementSavedSearchDetails.
        :rtype: list[object]
        """
        return self._data_config

    @data_config.setter
    def data_config(self, data_config):
        """
        Sets the data_config of this CreateManagementSavedSearchDetails.
        Array of Json to contain options for source of data.


        :param data_config: The data_config of this CreateManagementSavedSearchDetails.
        :type: list[object]
        """
        self._data_config = data_config

    @property
    def screen_image(self):
        """
        **[Required]** Gets the screen_image of this CreateManagementSavedSearchDetails.
        Screenshot.


        :return: The screen_image of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._screen_image

    @screen_image.setter
    def screen_image(self, screen_image):
        """
        Sets the screen_image of this CreateManagementSavedSearchDetails.
        Screenshot.


        :param screen_image: The screen_image of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._screen_image = screen_image

    @property
    def metadata_version(self):
        """
        **[Required]** Gets the metadata_version of this CreateManagementSavedSearchDetails.
        Version of the metadata.


        :return: The metadata_version of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._metadata_version

    @metadata_version.setter
    def metadata_version(self, metadata_version):
        """
        Sets the metadata_version of this CreateManagementSavedSearchDetails.
        Version of the metadata.


        :param metadata_version: The metadata_version of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._metadata_version = metadata_version

    @property
    def widget_template(self):
        """
        **[Required]** Gets the widget_template of this CreateManagementSavedSearchDetails.
        Template.


        :return: The widget_template of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._widget_template

    @widget_template.setter
    def widget_template(self, widget_template):
        """
        Sets the widget_template of this CreateManagementSavedSearchDetails.
        Template.


        :param widget_template: The widget_template of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._widget_template = widget_template

    @property
    def widget_vm(self):
        """
        **[Required]** Gets the widget_vm of this CreateManagementSavedSearchDetails.
        View Model


        :return: The widget_vm of this CreateManagementSavedSearchDetails.
        :rtype: str
        """
        return self._widget_vm

    @widget_vm.setter
    def widget_vm(self, widget_vm):
        """
        Sets the widget_vm of this CreateManagementSavedSearchDetails.
        View Model


        :param widget_vm: The widget_vm of this CreateManagementSavedSearchDetails.
        :type: str
        """
        self._widget_vm = widget_vm

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateManagementSavedSearchDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateManagementSavedSearchDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateManagementSavedSearchDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateManagementSavedSearchDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateManagementSavedSearchDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateManagementSavedSearchDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateManagementSavedSearchDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateManagementSavedSearchDetails.
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
