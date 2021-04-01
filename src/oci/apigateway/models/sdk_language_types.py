# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SdkLanguageTypes(object):
    """
    SDK target language details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SdkLanguageTypes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SdkLanguageTypes.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this SdkLanguageTypes.
        :type display_name: str

        :param version:
            The value to assign to the version property of this SdkLanguageTypes.
        :type version: str

        :param description:
            The value to assign to the description property of this SdkLanguageTypes.
        :type description: str

        :param parameters:
            The value to assign to the parameters property of this SdkLanguageTypes.
        :type parameters: list[oci.apigateway.models.SdkLanguageOptionalParameters]

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'version': 'str',
            'description': 'str',
            'parameters': 'list[SdkLanguageOptionalParameters]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'version': 'version',
            'description': 'description',
            'parameters': 'parameters'
        }

        self._name = None
        self._display_name = None
        self._version = None
        self._description = None
        self._parameters = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SdkLanguageTypes.
        Name of the programming language.


        :return: The name of this SdkLanguageTypes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SdkLanguageTypes.
        Name of the programming language.


        :param name: The name of this SdkLanguageTypes.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this SdkLanguageTypes.
        Display name of the target programming language.


        :return: The display_name of this SdkLanguageTypes.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SdkLanguageTypes.
        Display name of the target programming language.


        :param display_name: The display_name of this SdkLanguageTypes.
        :type: str
        """
        self._display_name = display_name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this SdkLanguageTypes.
        Version string of the programming language defined in name.


        :return: The version of this SdkLanguageTypes.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SdkLanguageTypes.
        Version string of the programming language defined in name.


        :param version: The version of this SdkLanguageTypes.
        :type: str
        """
        self._version = version

    @property
    def description(self):
        """
        Gets the description of this SdkLanguageTypes.
        Additional details.


        :return: The description of this SdkLanguageTypes.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SdkLanguageTypes.
        Additional details.


        :param description: The description of this SdkLanguageTypes.
        :type: str
        """
        self._description = description

    @property
    def parameters(self):
        """
        Gets the parameters of this SdkLanguageTypes.
        List of optional configurations that can be used while generating SDK for the given target language.


        :return: The parameters of this SdkLanguageTypes.
        :rtype: list[oci.apigateway.models.SdkLanguageOptionalParameters]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this SdkLanguageTypes.
        List of optional configurations that can be used while generating SDK for the given target language.


        :param parameters: The parameters of this SdkLanguageTypes.
        :type: list[oci.apigateway.models.SdkLanguageOptionalParameters]
        """
        self._parameters = parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
