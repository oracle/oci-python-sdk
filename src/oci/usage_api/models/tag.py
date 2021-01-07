# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Tag(object):
    """
    The tag used for filtering.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Tag object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this Tag.
        :type namespace: str

        :param key:
            The value to assign to the key property of this Tag.
        :type key: str

        :param value:
            The value to assign to the value property of this Tag.
        :type value: str

        """
        self.swagger_types = {
            'namespace': 'str',
            'key': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'key': 'key',
            'value': 'value'
        }

        self._namespace = None
        self._key = None
        self._value = None

    @property
    def namespace(self):
        """
        Gets the namespace of this Tag.
        The tag namespace.


        :return: The namespace of this Tag.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this Tag.
        The tag namespace.


        :param namespace: The namespace of this Tag.
        :type: str
        """
        self._namespace = namespace

    @property
    def key(self):
        """
        Gets the key of this Tag.
        The tag key.


        :return: The key of this Tag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Tag.
        The tag key.


        :param key: The key of this Tag.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """
        Gets the value of this Tag.
        The tag value.


        :return: The value of this Tag.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Tag.
        The tag value.


        :param value: The value of this Tag.
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
