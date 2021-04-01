# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SdkLanguageOptionalParameters(object):
    """
    List of additional applicable parameters for any given target language.
    """

    #: A constant which can be used with the input_type property of a SdkLanguageOptionalParameters.
    #: This constant has a value of "ENUM"
    INPUT_TYPE_ENUM = "ENUM"

    #: A constant which can be used with the input_type property of a SdkLanguageOptionalParameters.
    #: This constant has a value of "EMAIL"
    INPUT_TYPE_EMAIL = "EMAIL"

    #: A constant which can be used with the input_type property of a SdkLanguageOptionalParameters.
    #: This constant has a value of "URI"
    INPUT_TYPE_URI = "URI"

    #: A constant which can be used with the input_type property of a SdkLanguageOptionalParameters.
    #: This constant has a value of "STRING"
    INPUT_TYPE_STRING = "STRING"

    def __init__(self, **kwargs):
        """
        Initializes a new SdkLanguageOptionalParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param param_name:
            The value to assign to the param_name property of this SdkLanguageOptionalParameters.
        :type param_name: str

        :param display_name:
            The value to assign to the display_name property of this SdkLanguageOptionalParameters.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SdkLanguageOptionalParameters.
        :type description: str

        :param is_required:
            The value to assign to the is_required property of this SdkLanguageOptionalParameters.
        :type is_required: bool

        :param max_size:
            The value to assign to the max_size property of this SdkLanguageOptionalParameters.
        :type max_size: float

        :param input_type:
            The value to assign to the input_type property of this SdkLanguageOptionalParameters.
            Allowed values for this property are: "ENUM", "EMAIL", "URI", "STRING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type input_type: str

        :param allowed_values:
            The value to assign to the allowed_values property of this SdkLanguageOptionalParameters.
        :type allowed_values: list[oci.apigateway.models.SdkLanguageOptionalParametersAllowedValue]

        """
        self.swagger_types = {
            'param_name': 'str',
            'display_name': 'str',
            'description': 'str',
            'is_required': 'bool',
            'max_size': 'float',
            'input_type': 'str',
            'allowed_values': 'list[SdkLanguageOptionalParametersAllowedValue]'
        }

        self.attribute_map = {
            'param_name': 'paramName',
            'display_name': 'displayName',
            'description': 'description',
            'is_required': 'isRequired',
            'max_size': 'maxSize',
            'input_type': 'inputType',
            'allowed_values': 'allowedValues'
        }

        self._param_name = None
        self._display_name = None
        self._description = None
        self._is_required = None
        self._max_size = None
        self._input_type = None
        self._allowed_values = None

    @property
    def param_name(self):
        """
        **[Required]** Gets the param_name of this SdkLanguageOptionalParameters.
        Name of the parameter.


        :return: The param_name of this SdkLanguageOptionalParameters.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """
        Sets the param_name of this SdkLanguageOptionalParameters.
        Name of the parameter.


        :param param_name: The param_name of this SdkLanguageOptionalParameters.
        :type: str
        """
        self._param_name = param_name

    @property
    def display_name(self):
        """
        Gets the display_name of this SdkLanguageOptionalParameters.
        Display name of the parameter.


        :return: The display_name of this SdkLanguageOptionalParameters.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SdkLanguageOptionalParameters.
        Display name of the parameter.


        :param display_name: The display_name of this SdkLanguageOptionalParameters.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SdkLanguageOptionalParameters.
        Description for the parameter.


        :return: The description of this SdkLanguageOptionalParameters.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SdkLanguageOptionalParameters.
        Description for the parameter.


        :param description: The description of this SdkLanguageOptionalParameters.
        :type: str
        """
        self._description = description

    @property
    def is_required(self):
        """
        Gets the is_required of this SdkLanguageOptionalParameters.
        Information on whether the parameter is required or not.


        :return: The is_required of this SdkLanguageOptionalParameters.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this SdkLanguageOptionalParameters.
        Information on whether the parameter is required or not.


        :param is_required: The is_required of this SdkLanguageOptionalParameters.
        :type: bool
        """
        self._is_required = is_required

    @property
    def max_size(self):
        """
        Gets the max_size of this SdkLanguageOptionalParameters.
        Maximum size as input value for this parameter.


        :return: The max_size of this SdkLanguageOptionalParameters.
        :rtype: float
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """
        Sets the max_size of this SdkLanguageOptionalParameters.
        Maximum size as input value for this parameter.


        :param max_size: The max_size of this SdkLanguageOptionalParameters.
        :type: float
        """
        self._max_size = max_size

    @property
    def input_type(self):
        """
        Gets the input_type of this SdkLanguageOptionalParameters.
        The input type for this param.
        - Input type is ENUM when only specific list of input strings are allowed.
        - Input type is EMAIL when input type is an email ID.
        - Input type is URI when input type is an URI.
        - Input type is STRING in all other cases.

        Allowed values for this property are: "ENUM", "EMAIL", "URI", "STRING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The input_type of this SdkLanguageOptionalParameters.
        :rtype: str
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """
        Sets the input_type of this SdkLanguageOptionalParameters.
        The input type for this param.
        - Input type is ENUM when only specific list of input strings are allowed.
        - Input type is EMAIL when input type is an email ID.
        - Input type is URI when input type is an URI.
        - Input type is STRING in all other cases.


        :param input_type: The input_type of this SdkLanguageOptionalParameters.
        :type: str
        """
        allowed_values = ["ENUM", "EMAIL", "URI", "STRING"]
        if not value_allowed_none_or_none_sentinel(input_type, allowed_values):
            input_type = 'UNKNOWN_ENUM_VALUE'
        self._input_type = input_type

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this SdkLanguageOptionalParameters.
        List of allowed input values.
        Example: `[{\"name\": \"name1\", \"description\": \"description1\"}, ...]`


        :return: The allowed_values of this SdkLanguageOptionalParameters.
        :rtype: list[oci.apigateway.models.SdkLanguageOptionalParametersAllowedValue]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this SdkLanguageOptionalParameters.
        List of allowed input values.
        Example: `[{\"name\": \"name1\", \"description\": \"description1\"}, ...]`


        :param allowed_values: The allowed_values of this SdkLanguageOptionalParameters.
        :type: list[oci.apigateway.models.SdkLanguageOptionalParametersAllowedValue]
        """
        self._allowed_values = allowed_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
