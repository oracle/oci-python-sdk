# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateRegistryDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateRegistryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateRegistryDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateRegistryDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this UpdateRegistryDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateRegistryDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'description': 'description',
            'display_name': 'displayName'
        }

        self._freeform_tags = None
        self._defined_tags = None
        self._description = None
        self._display_name = None

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateRegistryDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateRegistryDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateRegistryDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateRegistryDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateRegistryDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateRegistryDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateRegistryDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateRegistryDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this UpdateRegistryDetails.
        Data Connectivity Management Registry description


        :return: The description of this UpdateRegistryDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateRegistryDetails.
        Data Connectivity Management Registry description


        :param description: The description of this UpdateRegistryDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateRegistryDetails.
        Data Connectivity Management Registry display name, registries can be renamed


        :return: The display_name of this UpdateRegistryDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateRegistryDetails.
        Data Connectivity Management Registry display name, registries can be renamed


        :param display_name: The display_name of this UpdateRegistryDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
