# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GoodBot(object):
    """
    The good bot settings. Good bots provides a list of bots which are managed by known providers.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GoodBot object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this GoodBot.
        :type key: str

        :param name:
            The value to assign to the name property of this GoodBot.
        :type name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this GoodBot.
        :type is_enabled: bool

        :param description:
            The value to assign to the description property of this GoodBot.
        :type description: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'is_enabled': 'bool',
            'description': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'is_enabled': 'isEnabled',
            'description': 'description'
        }

        self._key = None
        self._name = None
        self._is_enabled = None
        self._description = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this GoodBot.
        The unique key for the bot.


        :return: The key of this GoodBot.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this GoodBot.
        The unique key for the bot.


        :param key: The key of this GoodBot.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this GoodBot.
        The bot name.


        :return: The name of this GoodBot.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GoodBot.
        The bot name.


        :param name: The name of this GoodBot.
        :type: str
        """
        self._name = name

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this GoodBot.
        Enables or disables the bot.


        :return: The is_enabled of this GoodBot.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this GoodBot.
        Enables or disables the bot.


        :param is_enabled: The is_enabled of this GoodBot.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def description(self):
        """
        Gets the description of this GoodBot.
        The description of the bot.


        :return: The description of this GoodBot.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GoodBot.
        The description of the bot.


        :param description: The description of this GoodBot.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
