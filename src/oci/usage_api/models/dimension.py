# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Dimension(object):
    """
    The dimension use for filtering.
    example:
    `[{value: \"COMPUTE\", key: \"service\"}]`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Dimension object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Dimension.
        :type key: str

        :param value:
            The value to assign to the value property of this Dimension.
        :type value: str

        """
        self.swagger_types = {
            'key': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value'
        }

        self._key = None
        self._value = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Dimension.
        The key of the dimension.


        :return: The key of this Dimension.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Dimension.
        The key of the dimension.


        :param key: The key of this Dimension.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Dimension.
        The value of the dimension.


        :return: The value of this Dimension.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Dimension.
        The value of the dimension.


        :param value: The value of this Dimension.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
