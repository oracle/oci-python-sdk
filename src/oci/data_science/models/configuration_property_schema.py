# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationPropertySchema(object):
    """
    Schema for single configuration property
    """

    #: A constant which can be used with the value_type property of a ConfigurationPropertySchema.
    #: This constant has a value of "STRING"
    VALUE_TYPE_STRING = "STRING"

    #: A constant which can be used with the value_type property of a ConfigurationPropertySchema.
    #: This constant has a value of "SECRET"
    VALUE_TYPE_SECRET = "SECRET"

    #: A constant which can be used with the value_type property of a ConfigurationPropertySchema.
    #: This constant has a value of "VAULT_SECRET_ID"
    VALUE_TYPE_VAULT_SECRET_ID = "VAULT_SECRET_ID"

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigurationPropertySchema object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_name:
            The value to assign to the key_name property of this ConfigurationPropertySchema.
        :type key_name: str

        :param value_type:
            The value to assign to the value_type property of this ConfigurationPropertySchema.
            Allowed values for this property are: "STRING", "SECRET", "VAULT_SECRET_ID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type value_type: str

        :param description:
            The value to assign to the description property of this ConfigurationPropertySchema.
        :type description: str

        :param is_mandatory:
            The value to assign to the is_mandatory property of this ConfigurationPropertySchema.
        :type is_mandatory: bool

        :param default_value:
            The value to assign to the default_value property of this ConfigurationPropertySchema.
        :type default_value: str

        :param validation_regexp:
            The value to assign to the validation_regexp property of this ConfigurationPropertySchema.
        :type validation_regexp: str

        :param sample_value:
            The value to assign to the sample_value property of this ConfigurationPropertySchema.
        :type sample_value: str

        """
        self.swagger_types = {
            'key_name': 'str',
            'value_type': 'str',
            'description': 'str',
            'is_mandatory': 'bool',
            'default_value': 'str',
            'validation_regexp': 'str',
            'sample_value': 'str'
        }
        self.attribute_map = {
            'key_name': 'keyName',
            'value_type': 'valueType',
            'description': 'description',
            'is_mandatory': 'isMandatory',
            'default_value': 'defaultValue',
            'validation_regexp': 'validationRegexp',
            'sample_value': 'sampleValue'
        }
        self._key_name = None
        self._value_type = None
        self._description = None
        self._is_mandatory = None
        self._default_value = None
        self._validation_regexp = None
        self._sample_value = None

    @property
    def key_name(self):
        """
        **[Required]** Gets the key_name of this ConfigurationPropertySchema.
        Name of key (parameter name)


        :return: The key_name of this ConfigurationPropertySchema.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """
        Sets the key_name of this ConfigurationPropertySchema.
        Name of key (parameter name)


        :param key_name: The key_name of this ConfigurationPropertySchema.
        :type: str
        """
        self._key_name = key_name

    @property
    def value_type(self):
        """
        **[Required]** Gets the value_type of this ConfigurationPropertySchema.
        Type of value

        Allowed values for this property are: "STRING", "SECRET", "VAULT_SECRET_ID", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The value_type of this ConfigurationPropertySchema.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this ConfigurationPropertySchema.
        Type of value


        :param value_type: The value_type of this ConfigurationPropertySchema.
        :type: str
        """
        allowed_values = ["STRING", "SECRET", "VAULT_SECRET_ID"]
        if not value_allowed_none_or_none_sentinel(value_type, allowed_values):
            value_type = 'UNKNOWN_ENUM_VALUE'
        self._value_type = value_type

    @property
    def description(self):
        """
        **[Required]** Gets the description of this ConfigurationPropertySchema.
        Description of this configuration property


        :return: The description of this ConfigurationPropertySchema.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConfigurationPropertySchema.
        Description of this configuration property


        :param description: The description of this ConfigurationPropertySchema.
        :type: str
        """
        self._description = description

    @property
    def is_mandatory(self):
        """
        Gets the is_mandatory of this ConfigurationPropertySchema.
        If the value is true this configuration property is mandatory and visa versa. If not specified configuration property is optional.


        :return: The is_mandatory of this ConfigurationPropertySchema.
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """
        Sets the is_mandatory of this ConfigurationPropertySchema.
        If the value is true this configuration property is mandatory and visa versa. If not specified configuration property is optional.


        :param is_mandatory: The is_mandatory of this ConfigurationPropertySchema.
        :type: bool
        """
        self._is_mandatory = is_mandatory

    @property
    def default_value(self):
        """
        Gets the default_value of this ConfigurationPropertySchema.
        The default value for the optional configuration property (it must not be specified for mandatory configuration properties)


        :return: The default_value of this ConfigurationPropertySchema.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this ConfigurationPropertySchema.
        The default value for the optional configuration property (it must not be specified for mandatory configuration properties)


        :param default_value: The default_value of this ConfigurationPropertySchema.
        :type: str
        """
        self._default_value = default_value

    @property
    def validation_regexp(self):
        """
        Gets the validation_regexp of this ConfigurationPropertySchema.
        A regular expression will be used for the validation of property value.


        :return: The validation_regexp of this ConfigurationPropertySchema.
        :rtype: str
        """
        return self._validation_regexp

    @validation_regexp.setter
    def validation_regexp(self, validation_regexp):
        """
        Sets the validation_regexp of this ConfigurationPropertySchema.
        A regular expression will be used for the validation of property value.


        :param validation_regexp: The validation_regexp of this ConfigurationPropertySchema.
        :type: str
        """
        self._validation_regexp = validation_regexp

    @property
    def sample_value(self):
        """
        **[Required]** Gets the sample_value of this ConfigurationPropertySchema.
        Sample property value (it must match validationRegexp if it is specified)


        :return: The sample_value of this ConfigurationPropertySchema.
        :rtype: str
        """
        return self._sample_value

    @sample_value.setter
    def sample_value(self, sample_value):
        """
        Sets the sample_value of this ConfigurationPropertySchema.
        Sample property value (it must match validationRegexp if it is specified)


        :param sample_value: The sample_value of this ConfigurationPropertySchema.
        :type: str
        """
        self._sample_value = sample_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
