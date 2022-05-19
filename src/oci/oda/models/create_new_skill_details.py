# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_skill_details import CreateSkillDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNewSkillDetails(CreateSkillDetails):
    """
    Properties that are required to create a Skill from scratch.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNewSkillDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateNewSkillDetails.kind` attribute
        of this class is ``NEW`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this CreateNewSkillDetails.
            Allowed values for this property are: "NEW", "CLONE", "VERSION", "EXTEND"
        :type kind: str

        :param category:
            The value to assign to the category property of this CreateNewSkillDetails.
        :type category: str

        :param description:
            The value to assign to the description property of this CreateNewSkillDetails.
        :type description: str

        :param platform_version:
            The value to assign to the platform_version property of this CreateNewSkillDetails.
        :type platform_version: str

        :param multilingual_mode:
            The value to assign to the multilingual_mode property of this CreateNewSkillDetails.
            Allowed values for this property are: "NATIVE", "TRANSLATION"
        :type multilingual_mode: str

        :param primary_language_tag:
            The value to assign to the primary_language_tag property of this CreateNewSkillDetails.
        :type primary_language_tag: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateNewSkillDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateNewSkillDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param name:
            The value to assign to the name property of this CreateNewSkillDetails.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this CreateNewSkillDetails.
        :type display_name: str

        :param version:
            The value to assign to the version property of this CreateNewSkillDetails.
        :type version: str

        :param native_language_tags:
            The value to assign to the native_language_tags property of this CreateNewSkillDetails.
        :type native_language_tags: list[str]

        """
        self.swagger_types = {
            'kind': 'str',
            'category': 'str',
            'description': 'str',
            'platform_version': 'str',
            'multilingual_mode': 'str',
            'primary_language_tag': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'name': 'str',
            'display_name': 'str',
            'version': 'str',
            'native_language_tags': 'list[str]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'category': 'category',
            'description': 'description',
            'platform_version': 'platformVersion',
            'multilingual_mode': 'multilingualMode',
            'primary_language_tag': 'primaryLanguageTag',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'name': 'name',
            'display_name': 'displayName',
            'version': 'version',
            'native_language_tags': 'nativeLanguageTags'
        }

        self._kind = None
        self._category = None
        self._description = None
        self._platform_version = None
        self._multilingual_mode = None
        self._primary_language_tag = None
        self._freeform_tags = None
        self._defined_tags = None
        self._name = None
        self._display_name = None
        self._version = None
        self._native_language_tags = None
        self._kind = 'NEW'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateNewSkillDetails.
        The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.


        :return: The name of this CreateNewSkillDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateNewSkillDetails.
        The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.


        :param name: The name of this CreateNewSkillDetails.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateNewSkillDetails.
        The resource's display name.


        :return: The display_name of this CreateNewSkillDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateNewSkillDetails.
        The resource's display name.


        :param display_name: The display_name of this CreateNewSkillDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this CreateNewSkillDetails.
        The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.


        :return: The version of this CreateNewSkillDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CreateNewSkillDetails.
        The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.


        :param version: The version of this CreateNewSkillDetails.
        :type: str
        """
        self._version = version

    @property
    def native_language_tags(self):
        """
        Gets the native_language_tags of this CreateNewSkillDetails.
        A list of native languages supported by this resource.


        :return: The native_language_tags of this CreateNewSkillDetails.
        :rtype: list[str]
        """
        return self._native_language_tags

    @native_language_tags.setter
    def native_language_tags(self, native_language_tags):
        """
        Sets the native_language_tags of this CreateNewSkillDetails.
        A list of native languages supported by this resource.


        :param native_language_tags: The native_language_tags of this CreateNewSkillDetails.
        :type: list[str]
        """
        self._native_language_tags = native_language_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
