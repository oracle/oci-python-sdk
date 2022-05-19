# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDigitalAssistantDetails(object):
    """
    Properties that are required to create a Digital Assistant.
    """

    #: A constant which can be used with the kind property of a CreateDigitalAssistantDetails.
    #: This constant has a value of "NEW"
    KIND_NEW = "NEW"

    #: A constant which can be used with the kind property of a CreateDigitalAssistantDetails.
    #: This constant has a value of "CLONE"
    KIND_CLONE = "CLONE"

    #: A constant which can be used with the kind property of a CreateDigitalAssistantDetails.
    #: This constant has a value of "VERSION"
    KIND_VERSION = "VERSION"

    #: A constant which can be used with the kind property of a CreateDigitalAssistantDetails.
    #: This constant has a value of "EXTEND"
    KIND_EXTEND = "EXTEND"

    #: A constant which can be used with the multilingual_mode property of a CreateDigitalAssistantDetails.
    #: This constant has a value of "NATIVE"
    MULTILINGUAL_MODE_NATIVE = "NATIVE"

    #: A constant which can be used with the multilingual_mode property of a CreateDigitalAssistantDetails.
    #: This constant has a value of "TRANSLATION"
    MULTILINGUAL_MODE_TRANSLATION = "TRANSLATION"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDigitalAssistantDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.oda.models.CreateDigitalAssistantVersionDetails`
        * :class:`~oci.oda.models.CloneDigitalAssistantDetails`
        * :class:`~oci.oda.models.CreateNewDigitalAssistantDetails`
        * :class:`~oci.oda.models.ExtendDigitalAssistantDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this CreateDigitalAssistantDetails.
            Allowed values for this property are: "NEW", "CLONE", "VERSION", "EXTEND"
        :type kind: str

        :param category:
            The value to assign to the category property of this CreateDigitalAssistantDetails.
        :type category: str

        :param description:
            The value to assign to the description property of this CreateDigitalAssistantDetails.
        :type description: str

        :param platform_version:
            The value to assign to the platform_version property of this CreateDigitalAssistantDetails.
        :type platform_version: str

        :param multilingual_mode:
            The value to assign to the multilingual_mode property of this CreateDigitalAssistantDetails.
            Allowed values for this property are: "NATIVE", "TRANSLATION"
        :type multilingual_mode: str

        :param primary_language_tag:
            The value to assign to the primary_language_tag property of this CreateDigitalAssistantDetails.
        :type primary_language_tag: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDigitalAssistantDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDigitalAssistantDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'kind': 'str',
            'category': 'str',
            'description': 'str',
            'platform_version': 'str',
            'multilingual_mode': 'str',
            'primary_language_tag': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'kind': 'kind',
            'category': 'category',
            'description': 'description',
            'platform_version': 'platformVersion',
            'multilingual_mode': 'multilingualMode',
            'primary_language_tag': 'primaryLanguageTag',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._kind = None
        self._category = None
        self._description = None
        self._platform_version = None
        self._multilingual_mode = None
        self._primary_language_tag = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['kind']

        if type == 'VERSION':
            return 'CreateDigitalAssistantVersionDetails'

        if type == 'CLONE':
            return 'CloneDigitalAssistantDetails'

        if type == 'NEW':
            return 'CreateNewDigitalAssistantDetails'

        if type == 'EXTEND':
            return 'ExtendDigitalAssistantDetails'
        else:
            return 'CreateDigitalAssistantDetails'

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this CreateDigitalAssistantDetails.
        How to create the Digital Assistant.

        Allowed values for this property are: "NEW", "CLONE", "VERSION", "EXTEND"


        :return: The kind of this CreateDigitalAssistantDetails.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this CreateDigitalAssistantDetails.
        How to create the Digital Assistant.


        :param kind: The kind of this CreateDigitalAssistantDetails.
        :type: str
        """
        allowed_values = ["NEW", "CLONE", "VERSION", "EXTEND"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            raise ValueError(
                "Invalid value for `kind`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._kind = kind

    @property
    def category(self):
        """
        Gets the category of this CreateDigitalAssistantDetails.
        The resource's category.  This is used to group resource's together.


        :return: The category of this CreateDigitalAssistantDetails.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this CreateDigitalAssistantDetails.
        The resource's category.  This is used to group resource's together.


        :param category: The category of this CreateDigitalAssistantDetails.
        :type: str
        """
        self._category = category

    @property
    def description(self):
        """
        Gets the description of this CreateDigitalAssistantDetails.
        A short description of the resource.


        :return: The description of this CreateDigitalAssistantDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDigitalAssistantDetails.
        A short description of the resource.


        :param description: The description of this CreateDigitalAssistantDetails.
        :type: str
        """
        self._description = description

    @property
    def platform_version(self):
        """
        Gets the platform_version of this CreateDigitalAssistantDetails.
        The ODA Platform Version for this resource.


        :return: The platform_version of this CreateDigitalAssistantDetails.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """
        Sets the platform_version of this CreateDigitalAssistantDetails.
        The ODA Platform Version for this resource.


        :param platform_version: The platform_version of this CreateDigitalAssistantDetails.
        :type: str
        """
        self._platform_version = platform_version

    @property
    def multilingual_mode(self):
        """
        Gets the multilingual_mode of this CreateDigitalAssistantDetails.
        The multilingual mode for the resource.

        Allowed values for this property are: "NATIVE", "TRANSLATION"


        :return: The multilingual_mode of this CreateDigitalAssistantDetails.
        :rtype: str
        """
        return self._multilingual_mode

    @multilingual_mode.setter
    def multilingual_mode(self, multilingual_mode):
        """
        Sets the multilingual_mode of this CreateDigitalAssistantDetails.
        The multilingual mode for the resource.


        :param multilingual_mode: The multilingual_mode of this CreateDigitalAssistantDetails.
        :type: str
        """
        allowed_values = ["NATIVE", "TRANSLATION"]
        if not value_allowed_none_or_none_sentinel(multilingual_mode, allowed_values):
            raise ValueError(
                "Invalid value for `multilingual_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._multilingual_mode = multilingual_mode

    @property
    def primary_language_tag(self):
        """
        Gets the primary_language_tag of this CreateDigitalAssistantDetails.
        The primary language for the resource.


        :return: The primary_language_tag of this CreateDigitalAssistantDetails.
        :rtype: str
        """
        return self._primary_language_tag

    @primary_language_tag.setter
    def primary_language_tag(self, primary_language_tag):
        """
        Sets the primary_language_tag of this CreateDigitalAssistantDetails.
        The primary language for the resource.


        :param primary_language_tag: The primary_language_tag of this CreateDigitalAssistantDetails.
        :type: str
        """
        self._primary_language_tag = primary_language_tag

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDigitalAssistantDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDigitalAssistantDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDigitalAssistantDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDigitalAssistantDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDigitalAssistantDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDigitalAssistantDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDigitalAssistantDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDigitalAssistantDetails.
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
