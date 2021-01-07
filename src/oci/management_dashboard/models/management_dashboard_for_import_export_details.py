# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementDashboardForImportExportDetails(object):
    """
    Properties of a dashboard, including dashboard ID and saved searches, for import purposes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementDashboardForImportExportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dashboard_id:
            The value to assign to the dashboard_id property of this ManagementDashboardForImportExportDetails.
        :type dashboard_id: str

        :param provider_id:
            The value to assign to the provider_id property of this ManagementDashboardForImportExportDetails.
        :type provider_id: str

        :param provider_name:
            The value to assign to the provider_name property of this ManagementDashboardForImportExportDetails.
        :type provider_name: str

        :param provider_version:
            The value to assign to the provider_version property of this ManagementDashboardForImportExportDetails.
        :type provider_version: str

        :param tiles:
            The value to assign to the tiles property of this ManagementDashboardForImportExportDetails.
        :type tiles: list[oci.management_dashboard.models.ManagementDashboardTileDetails]

        :param display_name:
            The value to assign to the display_name property of this ManagementDashboardForImportExportDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ManagementDashboardForImportExportDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagementDashboardForImportExportDetails.
        :type compartment_id: str

        :param is_oob_dashboard:
            The value to assign to the is_oob_dashboard property of this ManagementDashboardForImportExportDetails.
        :type is_oob_dashboard: bool

        :param is_show_in_home:
            The value to assign to the is_show_in_home property of this ManagementDashboardForImportExportDetails.
        :type is_show_in_home: bool

        :param metadata_version:
            The value to assign to the metadata_version property of this ManagementDashboardForImportExportDetails.
        :type metadata_version: str

        :param is_show_description:
            The value to assign to the is_show_description property of this ManagementDashboardForImportExportDetails.
        :type is_show_description: bool

        :param screen_image:
            The value to assign to the screen_image property of this ManagementDashboardForImportExportDetails.
        :type screen_image: str

        :param nls:
            The value to assign to the nls property of this ManagementDashboardForImportExportDetails.
        :type nls: object

        :param ui_config:
            The value to assign to the ui_config property of this ManagementDashboardForImportExportDetails.
        :type ui_config: object

        :param data_config:
            The value to assign to the data_config property of this ManagementDashboardForImportExportDetails.
        :type data_config: list[object]

        :param type:
            The value to assign to the type property of this ManagementDashboardForImportExportDetails.
        :type type: str

        :param is_favorite:
            The value to assign to the is_favorite property of this ManagementDashboardForImportExportDetails.
        :type is_favorite: bool

        :param saved_searches:
            The value to assign to the saved_searches property of this ManagementDashboardForImportExportDetails.
        :type saved_searches: list[oci.management_dashboard.models.ManagementSavedSearchForImportDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagementDashboardForImportExportDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagementDashboardForImportExportDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'dashboard_id': 'str',
            'provider_id': 'str',
            'provider_name': 'str',
            'provider_version': 'str',
            'tiles': 'list[ManagementDashboardTileDetails]',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'is_oob_dashboard': 'bool',
            'is_show_in_home': 'bool',
            'metadata_version': 'str',
            'is_show_description': 'bool',
            'screen_image': 'str',
            'nls': 'object',
            'ui_config': 'object',
            'data_config': 'list[object]',
            'type': 'str',
            'is_favorite': 'bool',
            'saved_searches': 'list[ManagementSavedSearchForImportDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'dashboard_id': 'dashboardId',
            'provider_id': 'providerId',
            'provider_name': 'providerName',
            'provider_version': 'providerVersion',
            'tiles': 'tiles',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'is_oob_dashboard': 'isOobDashboard',
            'is_show_in_home': 'isShowInHome',
            'metadata_version': 'metadataVersion',
            'is_show_description': 'isShowDescription',
            'screen_image': 'screenImage',
            'nls': 'nls',
            'ui_config': 'uiConfig',
            'data_config': 'dataConfig',
            'type': 'type',
            'is_favorite': 'isFavorite',
            'saved_searches': 'savedSearches',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._dashboard_id = None
        self._provider_id = None
        self._provider_name = None
        self._provider_version = None
        self._tiles = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._is_oob_dashboard = None
        self._is_show_in_home = None
        self._metadata_version = None
        self._is_show_description = None
        self._screen_image = None
        self._nls = None
        self._ui_config = None
        self._data_config = None
        self._type = None
        self._is_favorite = None
        self._saved_searches = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def dashboard_id(self):
        """
        **[Required]** Gets the dashboard_id of this ManagementDashboardForImportExportDetails.
        ID of the dashboard.


        :return: The dashboard_id of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """
        Sets the dashboard_id of this ManagementDashboardForImportExportDetails.
        ID of the dashboard.


        :param dashboard_id: The dashboard_id of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._dashboard_id = dashboard_id

    @property
    def provider_id(self):
        """
        **[Required]** Gets the provider_id of this ManagementDashboardForImportExportDetails.
        ID of the service (for example log-analytics) that owns the dashboard. Each service has a unique ID.


        :return: The provider_id of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """
        Sets the provider_id of this ManagementDashboardForImportExportDetails.
        ID of the service (for example log-analytics) that owns the dashboard. Each service has a unique ID.


        :param provider_id: The provider_id of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._provider_id = provider_id

    @property
    def provider_name(self):
        """
        **[Required]** Gets the provider_name of this ManagementDashboardForImportExportDetails.
        Name of the service (for example, Logging Analytics) that owns the dashboard.


        :return: The provider_name of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """
        Sets the provider_name of this ManagementDashboardForImportExportDetails.
        Name of the service (for example, Logging Analytics) that owns the dashboard.


        :param provider_name: The provider_name of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def provider_version(self):
        """
        **[Required]** Gets the provider_version of this ManagementDashboardForImportExportDetails.
        Version of the service that owns the dashboard.


        :return: The provider_version of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._provider_version

    @provider_version.setter
    def provider_version(self, provider_version):
        """
        Sets the provider_version of this ManagementDashboardForImportExportDetails.
        Version of the service that owns the dashboard.


        :param provider_version: The provider_version of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._provider_version = provider_version

    @property
    def tiles(self):
        """
        **[Required]** Gets the tiles of this ManagementDashboardForImportExportDetails.
        Array of dashboard tiles.


        :return: The tiles of this ManagementDashboardForImportExportDetails.
        :rtype: list[oci.management_dashboard.models.ManagementDashboardTileDetails]
        """
        return self._tiles

    @tiles.setter
    def tiles(self, tiles):
        """
        Sets the tiles of this ManagementDashboardForImportExportDetails.
        Array of dashboard tiles.


        :param tiles: The tiles of this ManagementDashboardForImportExportDetails.
        :type: list[oci.management_dashboard.models.ManagementDashboardTileDetails]
        """
        self._tiles = tiles

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagementDashboardForImportExportDetails.
        Display name of the dashboard.


        :return: The display_name of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagementDashboardForImportExportDetails.
        Display name of the dashboard.


        :param display_name: The display_name of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this ManagementDashboardForImportExportDetails.
        Description of the dashboard.


        :return: The description of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagementDashboardForImportExportDetails.
        Description of the dashboard.


        :param description: The description of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagementDashboardForImportExportDetails.
        OCID of the compartment in which the dashboard resides.


        :return: The compartment_id of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagementDashboardForImportExportDetails.
        OCID of the compartment in which the dashboard resides.


        :param compartment_id: The compartment_id of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_oob_dashboard(self):
        """
        **[Required]** Gets the is_oob_dashboard of this ManagementDashboardForImportExportDetails.
        Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.


        :return: The is_oob_dashboard of this ManagementDashboardForImportExportDetails.
        :rtype: bool
        """
        return self._is_oob_dashboard

    @is_oob_dashboard.setter
    def is_oob_dashboard(self, is_oob_dashboard):
        """
        Sets the is_oob_dashboard of this ManagementDashboardForImportExportDetails.
        Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.


        :param is_oob_dashboard: The is_oob_dashboard of this ManagementDashboardForImportExportDetails.
        :type: bool
        """
        self._is_oob_dashboard = is_oob_dashboard

    @property
    def is_show_in_home(self):
        """
        **[Required]** Gets the is_show_in_home of this ManagementDashboardForImportExportDetails.
        Determines whether the dashboard will be displayed in Dashboard Home.


        :return: The is_show_in_home of this ManagementDashboardForImportExportDetails.
        :rtype: bool
        """
        return self._is_show_in_home

    @is_show_in_home.setter
    def is_show_in_home(self, is_show_in_home):
        """
        Sets the is_show_in_home of this ManagementDashboardForImportExportDetails.
        Determines whether the dashboard will be displayed in Dashboard Home.


        :param is_show_in_home: The is_show_in_home of this ManagementDashboardForImportExportDetails.
        :type: bool
        """
        self._is_show_in_home = is_show_in_home

    @property
    def metadata_version(self):
        """
        **[Required]** Gets the metadata_version of this ManagementDashboardForImportExportDetails.
        Version of the metadata.


        :return: The metadata_version of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._metadata_version

    @metadata_version.setter
    def metadata_version(self, metadata_version):
        """
        Sets the metadata_version of this ManagementDashboardForImportExportDetails.
        Version of the metadata.


        :param metadata_version: The metadata_version of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._metadata_version = metadata_version

    @property
    def is_show_description(self):
        """
        **[Required]** Gets the is_show_description of this ManagementDashboardForImportExportDetails.
        Determines whether the description of the dashboard is displayed.


        :return: The is_show_description of this ManagementDashboardForImportExportDetails.
        :rtype: bool
        """
        return self._is_show_description

    @is_show_description.setter
    def is_show_description(self, is_show_description):
        """
        Sets the is_show_description of this ManagementDashboardForImportExportDetails.
        Determines whether the description of the dashboard is displayed.


        :param is_show_description: The is_show_description of this ManagementDashboardForImportExportDetails.
        :type: bool
        """
        self._is_show_description = is_show_description

    @property
    def screen_image(self):
        """
        **[Required]** Gets the screen_image of this ManagementDashboardForImportExportDetails.
        Screen image of the dashboard.


        :return: The screen_image of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._screen_image

    @screen_image.setter
    def screen_image(self, screen_image):
        """
        Sets the screen_image of this ManagementDashboardForImportExportDetails.
        Screen image of the dashboard.


        :param screen_image: The screen_image of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._screen_image = screen_image

    @property
    def nls(self):
        """
        **[Required]** Gets the nls of this ManagementDashboardForImportExportDetails.
        JSON that contains internationalization options.


        :return: The nls of this ManagementDashboardForImportExportDetails.
        :rtype: object
        """
        return self._nls

    @nls.setter
    def nls(self, nls):
        """
        Sets the nls of this ManagementDashboardForImportExportDetails.
        JSON that contains internationalization options.


        :param nls: The nls of this ManagementDashboardForImportExportDetails.
        :type: object
        """
        self._nls = nls

    @property
    def ui_config(self):
        """
        **[Required]** Gets the ui_config of this ManagementDashboardForImportExportDetails.
        JSON that contains user interface options.


        :return: The ui_config of this ManagementDashboardForImportExportDetails.
        :rtype: object
        """
        return self._ui_config

    @ui_config.setter
    def ui_config(self, ui_config):
        """
        Sets the ui_config of this ManagementDashboardForImportExportDetails.
        JSON that contains user interface options.


        :param ui_config: The ui_config of this ManagementDashboardForImportExportDetails.
        :type: object
        """
        self._ui_config = ui_config

    @property
    def data_config(self):
        """
        **[Required]** Gets the data_config of this ManagementDashboardForImportExportDetails.
        Array of JSON that contain data source options.


        :return: The data_config of this ManagementDashboardForImportExportDetails.
        :rtype: list[object]
        """
        return self._data_config

    @data_config.setter
    def data_config(self, data_config):
        """
        Sets the data_config of this ManagementDashboardForImportExportDetails.
        Array of JSON that contain data source options.


        :param data_config: The data_config of this ManagementDashboardForImportExportDetails.
        :type: list[object]
        """
        self._data_config = data_config

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ManagementDashboardForImportExportDetails.
        Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.


        :return: The type of this ManagementDashboardForImportExportDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ManagementDashboardForImportExportDetails.
        Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.


        :param type: The type of this ManagementDashboardForImportExportDetails.
        :type: str
        """
        self._type = type

    @property
    def is_favorite(self):
        """
        **[Required]** Gets the is_favorite of this ManagementDashboardForImportExportDetails.
        Determines whether the dashboard is set as favorite.


        :return: The is_favorite of this ManagementDashboardForImportExportDetails.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """
        Sets the is_favorite of this ManagementDashboardForImportExportDetails.
        Determines whether the dashboard is set as favorite.


        :param is_favorite: The is_favorite of this ManagementDashboardForImportExportDetails.
        :type: bool
        """
        self._is_favorite = is_favorite

    @property
    def saved_searches(self):
        """
        **[Required]** Gets the saved_searches of this ManagementDashboardForImportExportDetails.
        Array of saved searches in the dashboard.


        :return: The saved_searches of this ManagementDashboardForImportExportDetails.
        :rtype: list[oci.management_dashboard.models.ManagementSavedSearchForImportDetails]
        """
        return self._saved_searches

    @saved_searches.setter
    def saved_searches(self, saved_searches):
        """
        Sets the saved_searches of this ManagementDashboardForImportExportDetails.
        Array of saved searches in the dashboard.


        :param saved_searches: The saved_searches of this ManagementDashboardForImportExportDetails.
        :type: list[oci.management_dashboard.models.ManagementSavedSearchForImportDetails]
        """
        self._saved_searches = saved_searches

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ManagementDashboardForImportExportDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ManagementDashboardForImportExportDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagementDashboardForImportExportDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ManagementDashboardForImportExportDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ManagementDashboardForImportExportDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ManagementDashboardForImportExportDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagementDashboardForImportExportDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ManagementDashboardForImportExportDetails.
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
