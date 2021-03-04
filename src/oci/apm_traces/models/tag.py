# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Tag(object):
    """
    Definition of a tag which is a key value pair.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Tag object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tag_name:
            The value to assign to the tag_name property of this Tag.
        :type tag_name: str

        :param tag_value:
            The value to assign to the tag_value property of this Tag.
        :type tag_value: str

        """
        self.swagger_types = {
            'tag_name': 'str',
            'tag_value': 'str'
        }

        self.attribute_map = {
            'tag_name': 'tagName',
            'tag_value': 'tagValue'
        }

        self._tag_name = None
        self._tag_value = None

    @property
    def tag_name(self):
        """
        **[Required]** Gets the tag_name of this Tag.
        Key that specifies the tag name.


        :return: The tag_name of this Tag.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """
        Sets the tag_name of this Tag.
        Key that specifies the tag name.


        :param tag_name: The tag_name of this Tag.
        :type: str
        """
        self._tag_name = tag_name

    @property
    def tag_value(self):
        """
        **[Required]** Gets the tag_value of this Tag.
        Value associated with the tag key.


        :return: The tag_value of this Tag.
        :rtype: str
        """
        return self._tag_value

    @tag_value.setter
    def tag_value(self, tag_value):
        """
        Sets the tag_value of this Tag.
        Value associated with the tag key.


        :param tag_value: The tag_value of this Tag.
        :type: str
        """
        self._tag_value = tag_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
