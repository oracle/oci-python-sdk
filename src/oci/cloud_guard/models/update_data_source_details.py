# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDataSourceDetails(object):
    """
    Update of Data Source
    """

    #: A constant which can be used with the status property of a UpdateDataSourceDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a UpdateDataSourceDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDataSourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDataSourceDetails.
        :type display_name: str

        :param status:
            The value to assign to the status property of this UpdateDataSourceDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type status: str

        :param data_source_details:
            The value to assign to the data_source_details property of this UpdateDataSourceDetails.
        :type data_source_details: oci.cloud_guard.models.DataSourceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDataSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDataSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'status': 'str',
            'data_source_details': 'DataSourceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'status': 'status',
            'data_source_details': 'dataSourceDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._status = None
        self._data_source_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDataSourceDetails.
        Data Source display name.


        :return: The display_name of this UpdateDataSourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDataSourceDetails.
        Data Source display name.


        :param display_name: The display_name of this UpdateDataSourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def status(self):
        """
        Gets the status of this UpdateDataSourceDetails.
        Status of DataSource.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The status of this UpdateDataSourceDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateDataSourceDetails.
        Status of DataSource.


        :param status: The status of this UpdateDataSourceDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def data_source_details(self):
        """
        Gets the data_source_details of this UpdateDataSourceDetails.

        :return: The data_source_details of this UpdateDataSourceDetails.
        :rtype: oci.cloud_guard.models.DataSourceDetails
        """
        return self._data_source_details

    @data_source_details.setter
    def data_source_details(self, data_source_details):
        """
        Sets the data_source_details of this UpdateDataSourceDetails.

        :param data_source_details: The data_source_details of this UpdateDataSourceDetails.
        :type: oci.cloud_guard.models.DataSourceDetails
        """
        self._data_source_details = data_source_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDataSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this UpdateDataSourceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDataSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this UpdateDataSourceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDataSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDataSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDataSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDataSourceDetails.
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
