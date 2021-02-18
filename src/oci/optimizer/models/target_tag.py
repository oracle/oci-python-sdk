# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetTag(object):
    """
    A target tag with tag namespace, tag definition, tag value type, and tag values attached to the current profile override.
    """

    #: A constant which can be used with the tag_value_type property of a TargetTag.
    #: This constant has a value of "VALUE"
    TAG_VALUE_TYPE_VALUE = "VALUE"

    #: A constant which can be used with the tag_value_type property of a TargetTag.
    #: This constant has a value of "ANY"
    TAG_VALUE_TYPE_ANY = "ANY"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetTag object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tag_namespace_name:
            The value to assign to the tag_namespace_name property of this TargetTag.
        :type tag_namespace_name: str

        :param tag_definition_name:
            The value to assign to the tag_definition_name property of this TargetTag.
        :type tag_definition_name: str

        :param tag_value_type:
            The value to assign to the tag_value_type property of this TargetTag.
            Allowed values for this property are: "VALUE", "ANY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type tag_value_type: str

        :param tag_values:
            The value to assign to the tag_values property of this TargetTag.
        :type tag_values: list[str]

        """
        self.swagger_types = {
            'tag_namespace_name': 'str',
            'tag_definition_name': 'str',
            'tag_value_type': 'str',
            'tag_values': 'list[str]'
        }

        self.attribute_map = {
            'tag_namespace_name': 'tagNamespaceName',
            'tag_definition_name': 'tagDefinitionName',
            'tag_value_type': 'tagValueType',
            'tag_values': 'tagValues'
        }

        self._tag_namespace_name = None
        self._tag_definition_name = None
        self._tag_value_type = None
        self._tag_values = None

    @property
    def tag_namespace_name(self):
        """
        **[Required]** Gets the tag_namespace_name of this TargetTag.
        The name of the tag namespace.


        :return: The tag_namespace_name of this TargetTag.
        :rtype: str
        """
        return self._tag_namespace_name

    @tag_namespace_name.setter
    def tag_namespace_name(self, tag_namespace_name):
        """
        Sets the tag_namespace_name of this TargetTag.
        The name of the tag namespace.


        :param tag_namespace_name: The tag_namespace_name of this TargetTag.
        :type: str
        """
        self._tag_namespace_name = tag_namespace_name

    @property
    def tag_definition_name(self):
        """
        **[Required]** Gets the tag_definition_name of this TargetTag.
        The name of the tag definition.


        :return: The tag_definition_name of this TargetTag.
        :rtype: str
        """
        return self._tag_definition_name

    @tag_definition_name.setter
    def tag_definition_name(self, tag_definition_name):
        """
        Sets the tag_definition_name of this TargetTag.
        The name of the tag definition.


        :param tag_definition_name: The tag_definition_name of this TargetTag.
        :type: str
        """
        self._tag_definition_name = tag_definition_name

    @property
    def tag_value_type(self):
        """
        **[Required]** Gets the tag_value_type of this TargetTag.
        The tag value type.

        Allowed values for this property are: "VALUE", "ANY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The tag_value_type of this TargetTag.
        :rtype: str
        """
        return self._tag_value_type

    @tag_value_type.setter
    def tag_value_type(self, tag_value_type):
        """
        Sets the tag_value_type of this TargetTag.
        The tag value type.


        :param tag_value_type: The tag_value_type of this TargetTag.
        :type: str
        """
        allowed_values = ["VALUE", "ANY"]
        if not value_allowed_none_or_none_sentinel(tag_value_type, allowed_values):
            tag_value_type = 'UNKNOWN_ENUM_VALUE'
        self._tag_value_type = tag_value_type

    @property
    def tag_values(self):
        """
        Gets the tag_values of this TargetTag.
        The list of tag values.


        :return: The tag_values of this TargetTag.
        :rtype: list[str]
        """
        return self._tag_values

    @tag_values.setter
    def tag_values(self, tag_values):
        """
        Sets the tag_values of this TargetTag.
        The list of tag values.


        :param tag_values: The tag_values of this TargetTag.
        :type: list[str]
        """
        self._tag_values = tag_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
