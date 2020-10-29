# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateProfileDetails(object):
    """
    Details for updating a profile.

    **Caution:** Avoid using any confidential information when you use the API to supply string values.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateProfileDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateProfileDetails.
        :type description: str

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateProfileDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateProfileDetails.
        :type freeform_tags: dict(str, str)

        :param levels_configuration:
            The value to assign to the levels_configuration property of this UpdateProfileDetails.
        :type levels_configuration: LevelsConfiguration

        """
        self.swagger_types = {
            'description': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'levels_configuration': 'LevelsConfiguration'
        }

        self.attribute_map = {
            'description': 'description',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'levels_configuration': 'levelsConfiguration'
        }

        self._description = None
        self._defined_tags = None
        self._freeform_tags = None
        self._levels_configuration = None

    @property
    def description(self):
        """
        Gets the description of this UpdateProfileDetails.
        Text describing the profile.


        :return: The description of this UpdateProfileDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateProfileDetails.
        Text describing the profile.


        :param description: The description of this UpdateProfileDetails.
        :type: str
        """
        self._description = description

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateProfileDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateProfileDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateProfileDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateProfileDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateProfileDetails.
        Simple key-value pair applied without any predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Exists for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateProfileDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateProfileDetails.
        Simple key-value pair applied without any predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Exists for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateProfileDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def levels_configuration(self):
        """
        Gets the levels_configuration of this UpdateProfileDetails.

        :return: The levels_configuration of this UpdateProfileDetails.
        :rtype: LevelsConfiguration
        """
        return self._levels_configuration

    @levels_configuration.setter
    def levels_configuration(self, levels_configuration):
        """
        Sets the levels_configuration of this UpdateProfileDetails.

        :param levels_configuration: The levels_configuration of this UpdateProfileDetails.
        :type: LevelsConfiguration
        """
        self._levels_configuration = levels_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
