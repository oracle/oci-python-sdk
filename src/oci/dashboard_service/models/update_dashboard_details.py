# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDashboardDetails(object):
    """
    The base schema for updating a dashboard.
    Derived schemas have configurations and widgets specific to the  `schemaVersion`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDashboardDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.dashboard_service.models.UpdateV1DashboardDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDashboardDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateDashboardDetails.
        :type description: str

        :param schema_version:
            The value to assign to the schema_version property of this UpdateDashboardDetails.
        :type schema_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDashboardDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDashboardDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'schema_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'schema_version': 'schemaVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._schema_version = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['schemaVersion']

        if type == 'V1':
            return 'UpdateV1DashboardDetails'
        else:
            return 'UpdateDashboardDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDashboardDetails.
        A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information.
        Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\


        :return: The display_name of this UpdateDashboardDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDashboardDetails.
        A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information.
        Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\


        :param display_name: The display_name of this UpdateDashboardDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateDashboardDetails.
        A short description of the dashboard. It can be changed. Avoid entering confidential information.
        The following special characters are not allowed: <>()=/'\"&\\


        :return: The description of this UpdateDashboardDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDashboardDetails.
        A short description of the dashboard. It can be changed. Avoid entering confidential information.
        The following special characters are not allowed: <>()=/'\"&\\


        :param description: The description of this UpdateDashboardDetails.
        :type: str
        """
        self._description = description

    @property
    def schema_version(self):
        """
        **[Required]** Gets the schema_version of this UpdateDashboardDetails.
        The schema describing how to interpret the dashboard configuration and widgets.


        :return: The schema_version of this UpdateDashboardDetails.
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """
        Sets the schema_version of this UpdateDashboardDetails.
        The schema describing how to interpret the dashboard configuration and widgets.


        :param schema_version: The schema_version of this UpdateDashboardDetails.
        :type: str
        """
        self._schema_version = schema_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDashboardDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateDashboardDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDashboardDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateDashboardDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDashboardDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDashboardDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDashboardDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDashboardDetails.
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
