# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateOnPremConnectorConfigurationDetails(object):
    """
    The details used to create and download on-premises connector's configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateOnPremConnectorConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password:
            The value to assign to the password property of this GenerateOnPremConnectorConfigurationDetails.
        :type password: str

        """
        self.swagger_types = {
            'password': 'str'
        }

        self.attribute_map = {
            'password': 'password'
        }

        self._password = None

    @property
    def password(self):
        """
        **[Required]** Gets the password of this GenerateOnPremConnectorConfigurationDetails.
        The password to encrypt the keys inside the wallet included as part of the configuration. The password must be between 12 and 30 characters long and must contain atleast 1 uppercase, 1 lowercase, 1 numeric, and 1 special character.


        :return: The password of this GenerateOnPremConnectorConfigurationDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this GenerateOnPremConnectorConfigurationDetails.
        The password to encrypt the keys inside the wallet included as part of the configuration. The password must be between 12 and 30 characters long and must contain atleast 1 uppercase, 1 lowercase, 1 numeric, and 1 special character.


        :param password: The password of this GenerateOnPremConnectorConfigurationDetails.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
