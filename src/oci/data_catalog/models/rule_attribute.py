# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleAttribute(object):
    """
    Object that defines a usage of an attribute in the context of a rule.
    Example: For a UNIQUEKEY rule, declares the attribute in a table whose value must be unique.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RuleAttribute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this RuleAttribute.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this RuleAttribute.
        :type display_name: str

        :param position:
            The value to assign to the position property of this RuleAttribute.
        :type position: int

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'position': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'position': 'position'
        }

        self._key = None
        self._display_name = None
        self._position = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this RuleAttribute.
        Immutable unique key of the attribute.


        :return: The key of this RuleAttribute.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this RuleAttribute.
        Immutable unique key of the attribute.


        :param key: The key of this RuleAttribute.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this RuleAttribute.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this RuleAttribute.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RuleAttribute.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this RuleAttribute.
        :type: str
        """
        self._display_name = display_name

    @property
    def position(self):
        """
        Gets the position of this RuleAttribute.
        Position of the attribute in the record definition.


        :return: The position of this RuleAttribute.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this RuleAttribute.
        Position of the attribute in the record definition.


        :param position: The position of this RuleAttribute.
        :type: int
        """
        self._position = position

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
