# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Configuration(object):
    """
    A configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Configuration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Configuration.
        :type key: str

        :param values:
            The value to assign to the values property of this Configuration.
        :type values: list[str]

        """
        self.swagger_types = {
            'key': 'str',
            'values': 'list[str]'
        }

        self.attribute_map = {
            'key': 'key',
            'values': 'values'
        }

        self._key = None
        self._values = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Configuration.
        The configuration key.


        :return: The key of this Configuration.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Configuration.
        The configuration key.


        :param key: The key of this Configuration.
        :type: str
        """
        self._key = key

    @property
    def values(self):
        """
        Gets the values of this Configuration.
        The configuration value.


        :return: The values of this Configuration.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this Configuration.
        The configuration value.


        :param values: The values of this Configuration.
        :type: list[str]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
