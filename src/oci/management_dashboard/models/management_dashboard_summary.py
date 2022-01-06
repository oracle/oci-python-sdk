# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementDashboardSummary(object):
    """
    Summary of the properties of a dashboard.
    """

    #: A constant which can be used with the lifecycle_state property of a ManagementDashboardSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementDashboardSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dashboard_id:
            The value to assign to the dashboard_id property of this ManagementDashboardSummary.
        :type dashboard_id: str

        :param id:
            The value to assign to the id property of this ManagementDashboardSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ManagementDashboardSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ManagementDashboardSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagementDashboardSummary.
        :type compartment_id: str

        :param provider_id:
            The value to assign to the provider_id property of this ManagementDashboardSummary.
        :type provider_id: str

        :param provider_name:
            The value to assign to the provider_name property of this ManagementDashboardSummary.
        :type provider_name: str

        :param provider_version:
            The value to assign to the provider_version property of this ManagementDashboardSummary.
        :type provider_version: str

        :param is_oob_dashboard:
            The value to assign to the is_oob_dashboard property of this ManagementDashboardSummary.
        :type is_oob_dashboard: bool

        :param created_by:
            The value to assign to the created_by property of this ManagementDashboardSummary.
        :type created_by: str

        :param time_created:
            The value to assign to the time_created property of this ManagementDashboardSummary.
        :type time_created: datetime

        :param updated_by:
            The value to assign to the updated_by property of this ManagementDashboardSummary.
        :type updated_by: str

        :param time_updated:
            The value to assign to the time_updated property of this ManagementDashboardSummary.
        :type time_updated: datetime

        :param metadata_version:
            The value to assign to the metadata_version property of this ManagementDashboardSummary.
        :type metadata_version: str

        :param screen_image:
            The value to assign to the screen_image property of this ManagementDashboardSummary.
        :type screen_image: str

        :param nls:
            The value to assign to the nls property of this ManagementDashboardSummary.
        :type nls: object

        :param type:
            The value to assign to the type property of this ManagementDashboardSummary.
        :type type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagementDashboardSummary.
            Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagementDashboardSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagementDashboardSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'dashboard_id': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'provider_id': 'str',
            'provider_name': 'str',
            'provider_version': 'str',
            'is_oob_dashboard': 'bool',
            'created_by': 'str',
            'time_created': 'datetime',
            'updated_by': 'str',
            'time_updated': 'datetime',
            'metadata_version': 'str',
            'screen_image': 'str',
            'nls': 'object',
            'type': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'dashboard_id': 'dashboardId',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'provider_id': 'providerId',
            'provider_name': 'providerName',
            'provider_version': 'providerVersion',
            'is_oob_dashboard': 'isOobDashboard',
            'created_by': 'createdBy',
            'time_created': 'timeCreated',
            'updated_by': 'updatedBy',
            'time_updated': 'timeUpdated',
            'metadata_version': 'metadataVersion',
            'screen_image': 'screenImage',
            'nls': 'nls',
            'type': 'type',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._dashboard_id = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._provider_id = None
        self._provider_name = None
        self._provider_version = None
        self._is_oob_dashboard = None
        self._created_by = None
        self._time_created = None
        self._updated_by = None
        self._time_updated = None
        self._metadata_version = None
        self._screen_image = None
        self._nls = None
        self._type = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def dashboard_id(self):
        """
        **[Required]** Gets the dashboard_id of this ManagementDashboardSummary.
        ID of the dashboard.  Same as id.


        :return: The dashboard_id of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """
        Sets the dashboard_id of this ManagementDashboardSummary.
        ID of the dashboard.  Same as id.


        :param dashboard_id: The dashboard_id of this ManagementDashboardSummary.
        :type: str
        """
        self._dashboard_id = dashboard_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagementDashboardSummary.
        ID of the dashboard.  Same as dashboardId.


        :return: The id of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagementDashboardSummary.
        ID of the dashboard.  Same as dashboardId.


        :param id: The id of this ManagementDashboardSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagementDashboardSummary.
        Display name of the dashboard.


        :return: The display_name of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagementDashboardSummary.
        Display name of the dashboard.


        :param display_name: The display_name of this ManagementDashboardSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this ManagementDashboardSummary.
        Description of the dashboard.


        :return: The description of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagementDashboardSummary.
        Description of the dashboard.


        :param description: The description of this ManagementDashboardSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagementDashboardSummary.
        OCID of the compartment in which the dashboard resides.


        :return: The compartment_id of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagementDashboardSummary.
        OCID of the compartment in which the dashboard resides.


        :param compartment_id: The compartment_id of this ManagementDashboardSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def provider_id(self):
        """
        **[Required]** Gets the provider_id of this ManagementDashboardSummary.
        ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.


        :return: The provider_id of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """
        Sets the provider_id of this ManagementDashboardSummary.
        ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.


        :param provider_id: The provider_id of this ManagementDashboardSummary.
        :type: str
        """
        self._provider_id = provider_id

    @property
    def provider_name(self):
        """
        **[Required]** Gets the provider_name of this ManagementDashboardSummary.
        Name of the service (for example, Logging Analytics) that owns the dashboard.


        :return: The provider_name of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """
        Sets the provider_name of this ManagementDashboardSummary.
        Name of the service (for example, Logging Analytics) that owns the dashboard.


        :param provider_name: The provider_name of this ManagementDashboardSummary.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def provider_version(self):
        """
        **[Required]** Gets the provider_version of this ManagementDashboardSummary.
        Version of the service that owns the dashboard.


        :return: The provider_version of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._provider_version

    @provider_version.setter
    def provider_version(self, provider_version):
        """
        Sets the provider_version of this ManagementDashboardSummary.
        Version of the service that owns the dashboard.


        :param provider_version: The provider_version of this ManagementDashboardSummary.
        :type: str
        """
        self._provider_version = provider_version

    @property
    def is_oob_dashboard(self):
        """
        **[Required]** Gets the is_oob_dashboard of this ManagementDashboardSummary.
        Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.


        :return: The is_oob_dashboard of this ManagementDashboardSummary.
        :rtype: bool
        """
        return self._is_oob_dashboard

    @is_oob_dashboard.setter
    def is_oob_dashboard(self, is_oob_dashboard):
        """
        Sets the is_oob_dashboard of this ManagementDashboardSummary.
        Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.


        :param is_oob_dashboard: The is_oob_dashboard of this ManagementDashboardSummary.
        :type: bool
        """
        self._is_oob_dashboard = is_oob_dashboard

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this ManagementDashboardSummary.
        User who created the dashboard.


        :return: The created_by of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this ManagementDashboardSummary.
        User who created the dashboard.


        :param created_by: The created_by of this ManagementDashboardSummary.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ManagementDashboardSummary.
        Date and time the dashboard was created.


        :return: The time_created of this ManagementDashboardSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagementDashboardSummary.
        Date and time the dashboard was created.


        :param time_created: The time_created of this ManagementDashboardSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def updated_by(self):
        """
        **[Required]** Gets the updated_by of this ManagementDashboardSummary.
        User who updated the dashboard.


        :return: The updated_by of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this ManagementDashboardSummary.
        User who updated the dashboard.


        :param updated_by: The updated_by of this ManagementDashboardSummary.
        :type: str
        """
        self._updated_by = updated_by

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ManagementDashboardSummary.
        Date and time the dashboard was updated.


        :return: The time_updated of this ManagementDashboardSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ManagementDashboardSummary.
        Date and time the dashboard was updated.


        :param time_updated: The time_updated of this ManagementDashboardSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def metadata_version(self):
        """
        **[Required]** Gets the metadata_version of this ManagementDashboardSummary.
        Version of the metadata.


        :return: The metadata_version of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._metadata_version

    @metadata_version.setter
    def metadata_version(self, metadata_version):
        """
        Sets the metadata_version of this ManagementDashboardSummary.
        Version of the metadata.


        :param metadata_version: The metadata_version of this ManagementDashboardSummary.
        :type: str
        """
        self._metadata_version = metadata_version

    @property
    def screen_image(self):
        """
        **[Required]** Gets the screen_image of this ManagementDashboardSummary.
        Screen image of the dashboard.


        :return: The screen_image of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._screen_image

    @screen_image.setter
    def screen_image(self, screen_image):
        """
        Sets the screen_image of this ManagementDashboardSummary.
        Screen image of the dashboard.


        :param screen_image: The screen_image of this ManagementDashboardSummary.
        :type: str
        """
        self._screen_image = screen_image

    @property
    def nls(self):
        """
        **[Required]** Gets the nls of this ManagementDashboardSummary.
        JSON that contains internationalization options.


        :return: The nls of this ManagementDashboardSummary.
        :rtype: object
        """
        return self._nls

    @nls.setter
    def nls(self, nls):
        """
        Sets the nls of this ManagementDashboardSummary.
        JSON that contains internationalization options.


        :param nls: The nls of this ManagementDashboardSummary.
        :type: object
        """
        self._nls = nls

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ManagementDashboardSummary.
        Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.


        :return: The type of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ManagementDashboardSummary.
        Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.


        :param type: The type of this ManagementDashboardSummary.
        :type: str
        """
        self._type = type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ManagementDashboardSummary.
        Current lifecycle state of the dashboard.

        Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ManagementDashboardSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagementDashboardSummary.
        Current lifecycle state of the dashboard.


        :param lifecycle_state: The lifecycle_state of this ManagementDashboardSummary.
        :type: str
        """
        allowed_values = ["ACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this ManagementDashboardSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ManagementDashboardSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagementDashboardSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ManagementDashboardSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this ManagementDashboardSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ManagementDashboardSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagementDashboardSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ManagementDashboardSummary.
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
