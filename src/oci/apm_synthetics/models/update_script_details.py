# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateScriptDetails(object):
    """
    Details of the request body used to update a script.
    Only Side or JavaScript content types are supported and content should be in Side or JavaScript formats only.
    """

    #: A constant which can be used with the content_type property of a UpdateScriptDetails.
    #: This constant has a value of "SIDE"
    CONTENT_TYPE_SIDE = "SIDE"

    #: A constant which can be used with the content_type property of a UpdateScriptDetails.
    #: This constant has a value of "JS"
    CONTENT_TYPE_JS = "JS"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateScriptDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateScriptDetails.
        :type display_name: str

        :param content_type:
            The value to assign to the content_type property of this UpdateScriptDetails.
            Allowed values for this property are: "SIDE", "JS"
        :type content_type: str

        :param content:
            The value to assign to the content property of this UpdateScriptDetails.
        :type content: str

        :param content_file_name:
            The value to assign to the content_file_name property of this UpdateScriptDetails.
        :type content_file_name: str

        :param parameters:
            The value to assign to the parameters property of this UpdateScriptDetails.
        :type parameters: list[oci.apm_synthetics.models.ScriptParameter]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateScriptDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateScriptDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'content_type': 'str',
            'content': 'str',
            'content_file_name': 'str',
            'parameters': 'list[ScriptParameter]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'content_type': 'contentType',
            'content': 'content',
            'content_file_name': 'contentFileName',
            'parameters': 'parameters',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._content_type = None
        self._content = None
        self._content_file_name = None
        self._parameters = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateScriptDetails.
        Unique name that can be edited. The name should not contain any confidential information.


        :return: The display_name of this UpdateScriptDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateScriptDetails.
        Unique name that can be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this UpdateScriptDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def content_type(self):
        """
        Gets the content_type of this UpdateScriptDetails.
        Content type of script.

        Allowed values for this property are: "SIDE", "JS"


        :return: The content_type of this UpdateScriptDetails.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this UpdateScriptDetails.
        Content type of script.


        :param content_type: The content_type of this UpdateScriptDetails.
        :type: str
        """
        allowed_values = ["SIDE", "JS"]
        if not value_allowed_none_or_none_sentinel(content_type, allowed_values):
            raise ValueError(
                "Invalid value for `content_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._content_type = content_type

    @property
    def content(self):
        """
        Gets the content of this UpdateScriptDetails.
        The content of the script. It may contain custom-defined tags that can be used for setting dynamic parameters.
        The format to set dynamic parameters is: `<ORAP><ON>param name</ON><OV>param value</OV><OS>isParamValueSecret(true/false)</OS></ORAP>`.
        Param value and isParamValueSecret are optional, the default value for isParamValueSecret is false.
        Examples:
        With mandatory param name : `<ORAP><ON>param name</ON></ORAP>`
        With parameter name and value : `<ORAP><ON>param name</ON><OV>param value</OV></ORAP>`
        Note that the content is valid if it matches the given content type. For example, if the content type is SIDE, then the content should be in Side script format. If the content type is JS, then the content should be in JavaScript format.


        :return: The content of this UpdateScriptDetails.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this UpdateScriptDetails.
        The content of the script. It may contain custom-defined tags that can be used for setting dynamic parameters.
        The format to set dynamic parameters is: `<ORAP><ON>param name</ON><OV>param value</OV><OS>isParamValueSecret(true/false)</OS></ORAP>`.
        Param value and isParamValueSecret are optional, the default value for isParamValueSecret is false.
        Examples:
        With mandatory param name : `<ORAP><ON>param name</ON></ORAP>`
        With parameter name and value : `<ORAP><ON>param name</ON><OV>param value</OV></ORAP>`
        Note that the content is valid if it matches the given content type. For example, if the content type is SIDE, then the content should be in Side script format. If the content type is JS, then the content should be in JavaScript format.


        :param content: The content of this UpdateScriptDetails.
        :type: str
        """
        self._content = content

    @property
    def content_file_name(self):
        """
        Gets the content_file_name of this UpdateScriptDetails.
        File name of uploaded script content.


        :return: The content_file_name of this UpdateScriptDetails.
        :rtype: str
        """
        return self._content_file_name

    @content_file_name.setter
    def content_file_name(self, content_file_name):
        """
        Sets the content_file_name of this UpdateScriptDetails.
        File name of uploaded script content.


        :param content_file_name: The content_file_name of this UpdateScriptDetails.
        :type: str
        """
        self._content_file_name = content_file_name

    @property
    def parameters(self):
        """
        Gets the parameters of this UpdateScriptDetails.
        List of script parameters. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\", \"isSecret\": false}]`


        :return: The parameters of this UpdateScriptDetails.
        :rtype: list[oci.apm_synthetics.models.ScriptParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this UpdateScriptDetails.
        List of script parameters. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\", \"isSecret\": false}]`


        :param parameters: The parameters of this UpdateScriptDetails.
        :type: list[oci.apm_synthetics.models.ScriptParameter]
        """
        self._parameters = parameters

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateScriptDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateScriptDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateScriptDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateScriptDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateScriptDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateScriptDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateScriptDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateScriptDetails.
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
