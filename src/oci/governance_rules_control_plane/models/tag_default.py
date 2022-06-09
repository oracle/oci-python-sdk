# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TagDefault(object):
    """
    Tag defaults let you specify a default tag (tagnamespace.tag=\"value\") to apply to all resource types
    in a specified compartment. The tag default is applied at the time the resource is created. Resources
    that exist in the compartment before you create the tag default are not tagged.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TagDefault object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tag_name:
            The value to assign to the tag_name property of this TagDefault.
        :type tag_name: str

        :param value:
            The value to assign to the value property of this TagDefault.
        :type value: str

        :param is_required:
            The value to assign to the is_required property of this TagDefault.
        :type is_required: bool

        """
        self.swagger_types = {
            'tag_name': 'str',
            'value': 'str',
            'is_required': 'bool'
        }

        self.attribute_map = {
            'tag_name': 'tagName',
            'value': 'value',
            'is_required': 'isRequired'
        }

        self._tag_name = None
        self._value = None
        self._is_required = None

    @property
    def tag_name(self):
        """
        **[Required]** Gets the tag_name of this TagDefault.
        The name of the tag. The tag default will always assign a default value for this tag name.


        :return: The tag_name of this TagDefault.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """
        Sets the tag_name of this TagDefault.
        The name of the tag. The tag default will always assign a default value for this tag name.


        :param tag_name: The tag_name of this TagDefault.
        :type: str
        """
        self._tag_name = tag_name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this TagDefault.
        The default value for the tag name. This will be applied to all new resources created in the compartment.


        :return: The value of this TagDefault.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this TagDefault.
        The default value for the tag name. This will be applied to all new resources created in the compartment.


        :param value: The value of this TagDefault.
        :type: str
        """
        self._value = value

    @property
    def is_required(self):
        """
        **[Required]** Gets the is_required of this TagDefault.
        If you specify that a value is required, a value is set during resource creation (either by
        the user creating the resource or another tag default). If no value is set, resource
        creation is blocked.

        * If the `isRequired` flag is set to \"true\", the value is set during resource creation.
        * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

        Example: `false`


        :return: The is_required of this TagDefault.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this TagDefault.
        If you specify that a value is required, a value is set during resource creation (either by
        the user creating the resource or another tag default). If no value is set, resource
        creation is blocked.

        * If the `isRequired` flag is set to \"true\", the value is set during resource creation.
        * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

        Example: `false`


        :param is_required: The is_required of this TagDefault.
        :type: bool
        """
        self._is_required = is_required

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
