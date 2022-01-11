# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNotebookSessionDetails(object):
    """
    Details for updating a notebook session. `notebookSessionConfigurationDetails` can only be updated while the notebook session is in the `INACTIVE` state.
    Changes to the `notebookSessionConfigurationDetails` take effect the next time the `ActivateNotebookSession` action is invoked on the notebook session resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNotebookSessionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateNotebookSessionDetails.
        :type display_name: str

        :param notebook_session_configuration_details:
            The value to assign to the notebook_session_configuration_details property of this UpdateNotebookSessionDetails.
        :type notebook_session_configuration_details: oci.data_science.models.NotebookSessionConfigurationDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateNotebookSessionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateNotebookSessionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'notebook_session_configuration_details': 'NotebookSessionConfigurationDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'notebook_session_configuration_details': 'notebookSessionConfigurationDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._notebook_session_configuration_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateNotebookSessionDetails.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        Example: `My NotebookSession`


        :return: The display_name of this UpdateNotebookSessionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateNotebookSessionDetails.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        Example: `My NotebookSession`


        :param display_name: The display_name of this UpdateNotebookSessionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def notebook_session_configuration_details(self):
        """
        Gets the notebook_session_configuration_details of this UpdateNotebookSessionDetails.

        :return: The notebook_session_configuration_details of this UpdateNotebookSessionDetails.
        :rtype: oci.data_science.models.NotebookSessionConfigurationDetails
        """
        return self._notebook_session_configuration_details

    @notebook_session_configuration_details.setter
    def notebook_session_configuration_details(self, notebook_session_configuration_details):
        """
        Sets the notebook_session_configuration_details of this UpdateNotebookSessionDetails.

        :param notebook_session_configuration_details: The notebook_session_configuration_details of this UpdateNotebookSessionDetails.
        :type: oci.data_science.models.NotebookSessionConfigurationDetails
        """
        self._notebook_session_configuration_details = notebook_session_configuration_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateNotebookSessionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateNotebookSessionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateNotebookSessionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateNotebookSessionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateNotebookSessionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateNotebookSessionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateNotebookSessionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateNotebookSessionDetails.
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
