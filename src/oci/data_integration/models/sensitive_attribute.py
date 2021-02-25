# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SensitiveAttribute(object):
    """
    The sensitive attribute to be used for sensitive content (for password/wallet).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SensitiveAttribute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param secret_config:
            The value to assign to the secret_config property of this SensitiveAttribute.
        :type secret_config: oci.data_integration.models.SecretConfig

        :param value:
            The value to assign to the value property of this SensitiveAttribute.
        :type value: str

        """
        self.swagger_types = {
            'secret_config': 'SecretConfig',
            'value': 'str'
        }

        self.attribute_map = {
            'secret_config': 'secretConfig',
            'value': 'value'
        }

        self._secret_config = None
        self._value = None

    @property
    def secret_config(self):
        """
        Gets the secret_config of this SensitiveAttribute.

        :return: The secret_config of this SensitiveAttribute.
        :rtype: oci.data_integration.models.SecretConfig
        """
        return self._secret_config

    @secret_config.setter
    def secret_config(self, secret_config):
        """
        Sets the secret_config of this SensitiveAttribute.

        :param secret_config: The secret_config of this SensitiveAttribute.
        :type: oci.data_integration.models.SecretConfig
        """
        self._secret_config = secret_config

    @property
    def value(self):
        """
        Gets the value of this SensitiveAttribute.
        Attribute to provide sensitive content.


        :return: The value of this SensitiveAttribute.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SensitiveAttribute.
        Attribute to provide sensitive content.


        :param value: The value of this SensitiveAttribute.
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
