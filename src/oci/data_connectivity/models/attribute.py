# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Attribute(object):
    """
    Registry Attribute Object, to get connector details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Attribute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Attribute.
        :type name: str

        :param is_sensitive:
            The value to assign to the is_sensitive property of this Attribute.
        :type is_sensitive: bool

        :param is_mandatory:
            The value to assign to the is_mandatory property of this Attribute.
        :type is_mandatory: bool

        :param is_generated:
            The value to assign to the is_generated property of this Attribute.
        :type is_generated: bool

        :param is_base64_encoded:
            The value to assign to the is_base64_encoded property of this Attribute.
        :type is_base64_encoded: bool

        :param valid_key_list:
            The value to assign to the valid_key_list property of this Attribute.
        :type valid_key_list: list[str]

        :param attribute_type:
            The value to assign to the attribute_type property of this Attribute.
        :type attribute_type: str

        """
        self.swagger_types = {
            'name': 'str',
            'is_sensitive': 'bool',
            'is_mandatory': 'bool',
            'is_generated': 'bool',
            'is_base64_encoded': 'bool',
            'valid_key_list': 'list[str]',
            'attribute_type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'is_sensitive': 'isSensitive',
            'is_mandatory': 'isMandatory',
            'is_generated': 'isGenerated',
            'is_base64_encoded': 'isBase64Encoded',
            'valid_key_list': 'validKeyList',
            'attribute_type': 'attributeType'
        }

        self._name = None
        self._is_sensitive = None
        self._is_mandatory = None
        self._is_generated = None
        self._is_base64_encoded = None
        self._valid_key_list = None
        self._attribute_type = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Attribute.
        The name of of the Attribute.


        :return: The name of this Attribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Attribute.
        The name of of the Attribute.


        :param name: The name of this Attribute.
        :type: str
        """
        self._name = name

    @property
    def is_sensitive(self):
        """
        Gets the is_sensitive of this Attribute.
        True if Attribute is sensitive.


        :return: The is_sensitive of this Attribute.
        :rtype: bool
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        """
        Sets the is_sensitive of this Attribute.
        True if Attribute is sensitive.


        :param is_sensitive: The is_sensitive of this Attribute.
        :type: bool
        """
        self._is_sensitive = is_sensitive

    @property
    def is_mandatory(self):
        """
        Gets the is_mandatory of this Attribute.
        True if Attribute is mandatory.


        :return: The is_mandatory of this Attribute.
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """
        Sets the is_mandatory of this Attribute.
        True if Attribute is mandatory.


        :param is_mandatory: The is_mandatory of this Attribute.
        :type: bool
        """
        self._is_mandatory = is_mandatory

    @property
    def is_generated(self):
        """
        Gets the is_generated of this Attribute.
        True if Attribute is generated.


        :return: The is_generated of this Attribute.
        :rtype: bool
        """
        return self._is_generated

    @is_generated.setter
    def is_generated(self, is_generated):
        """
        Sets the is_generated of this Attribute.
        True if Attribute is generated.


        :param is_generated: The is_generated of this Attribute.
        :type: bool
        """
        self._is_generated = is_generated

    @property
    def is_base64_encoded(self):
        """
        Gets the is_base64_encoded of this Attribute.
        True if Attribute is encoded.


        :return: The is_base64_encoded of this Attribute.
        :rtype: bool
        """
        return self._is_base64_encoded

    @is_base64_encoded.setter
    def is_base64_encoded(self, is_base64_encoded):
        """
        Sets the is_base64_encoded of this Attribute.
        True if Attribute is encoded.


        :param is_base64_encoded: The is_base64_encoded of this Attribute.
        :type: bool
        """
        self._is_base64_encoded = is_base64_encoded

    @property
    def valid_key_list(self):
        """
        Gets the valid_key_list of this Attribute.
        List of valid key list


        :return: The valid_key_list of this Attribute.
        :rtype: list[str]
        """
        return self._valid_key_list

    @valid_key_list.setter
    def valid_key_list(self, valid_key_list):
        """
        Sets the valid_key_list of this Attribute.
        List of valid key list


        :param valid_key_list: The valid_key_list of this Attribute.
        :type: list[str]
        """
        self._valid_key_list = valid_key_list

    @property
    def attribute_type(self):
        """
        Gets the attribute_type of this Attribute.
        Attribute type details


        :return: The attribute_type of this Attribute.
        :rtype: str
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """
        Sets the attribute_type of this Attribute.
        Attribute type details


        :param attribute_type: The attribute_type of this Attribute.
        :type: str
        """
        self._attribute_type = attribute_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
