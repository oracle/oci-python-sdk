# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSdkDetails(object):
    """
    Information about the new SDK.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSdkDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateSdkDetails.
        :type display_name: str

        :param target_language:
            The value to assign to the target_language property of this CreateSdkDetails.
        :type target_language: str

        :param api_id:
            The value to assign to the api_id property of this CreateSdkDetails.
        :type api_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSdkDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSdkDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param parameters:
            The value to assign to the parameters property of this CreateSdkDetails.
        :type parameters: dict(str, str)

        """
        self.swagger_types = {
            'display_name': 'str',
            'target_language': 'str',
            'api_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'parameters': 'dict(str, str)'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'target_language': 'targetLanguage',
            'api_id': 'apiId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'parameters': 'parameters'
        }

        self._display_name = None
        self._target_language = None
        self._api_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._parameters = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSdkDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateSdkDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSdkDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateSdkDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def target_language(self):
        """
        **[Required]** Gets the target_language of this CreateSdkDetails.
        The string representing the target programming language for generating the SDK.


        :return: The target_language of this CreateSdkDetails.
        :rtype: str
        """
        return self._target_language

    @target_language.setter
    def target_language(self, target_language):
        """
        Sets the target_language of this CreateSdkDetails.
        The string representing the target programming language for generating the SDK.


        :param target_language: The target_language of this CreateSdkDetails.
        :type: str
        """
        self._target_language = target_language

    @property
    def api_id(self):
        """
        **[Required]** Gets the api_id of this CreateSdkDetails.
        The `OCID`__ of API resource

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The api_id of this CreateSdkDetails.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """
        Sets the api_id of this CreateSdkDetails.
        The `OCID`__ of API resource

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param api_id: The api_id of this CreateSdkDetails.
        :type: str
        """
        self._api_id = api_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSdkDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSdkDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSdkDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSdkDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSdkDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSdkDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSdkDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSdkDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def parameters(self):
        """
        Gets the parameters of this CreateSdkDetails.
        Additional optional configurations that can be passed to generate SDK Api.
        The applicable parameters are listed under \"parameters\" when \"/sdkLanguageTypes\" is called.

        Example: `{\"configName\": \"configValue\"}`


        :return: The parameters of this CreateSdkDetails.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CreateSdkDetails.
        Additional optional configurations that can be passed to generate SDK Api.
        The applicable parameters are listed under \"parameters\" when \"/sdkLanguageTypes\" is called.

        Example: `{\"configName\": \"configValue\"}`


        :param parameters: The parameters of this CreateSdkDetails.
        :type: dict(str, str)
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
