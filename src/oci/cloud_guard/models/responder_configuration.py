# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponderConfiguration(object):
    """
    A single configuration applied to a responder
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResponderConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_key:
            The value to assign to the config_key property of this ResponderConfiguration.
        :type config_key: str

        :param name:
            The value to assign to the name property of this ResponderConfiguration.
        :type name: str

        :param value:
            The value to assign to the value property of this ResponderConfiguration.
        :type value: str

        """
        self.swagger_types = {
            'config_key': 'str',
            'name': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'config_key': 'configKey',
            'name': 'name',
            'value': 'value'
        }

        self._config_key = None
        self._name = None
        self._value = None

    @property
    def config_key(self):
        """
        **[Required]** Gets the config_key of this ResponderConfiguration.
        Unique name of the configuration


        :return: The config_key of this ResponderConfiguration.
        :rtype: str
        """
        return self._config_key

    @config_key.setter
    def config_key(self, config_key):
        """
        Sets the config_key of this ResponderConfiguration.
        Unique name of the configuration


        :param config_key: The config_key of this ResponderConfiguration.
        :type: str
        """
        self._config_key = config_key

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ResponderConfiguration.
        configuration name


        :return: The name of this ResponderConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResponderConfiguration.
        configuration name


        :param name: The name of this ResponderConfiguration.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this ResponderConfiguration.
        configuration value


        :return: The value of this ResponderConfiguration.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ResponderConfiguration.
        configuration value


        :param value: The value of this ResponderConfiguration.
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
