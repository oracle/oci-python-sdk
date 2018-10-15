# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateAutonomousDatabaseWalletDetails(object):
    """
    Details to create and download an Oracle Autonomous Transaction Processing database wallet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateAutonomousDatabaseWalletDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password:
            The value to assign to the password property of this GenerateAutonomousDatabaseWalletDetails.
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
        **[Required]** Gets the password of this GenerateAutonomousDatabaseWalletDetails.
        The password to encrypt the keys inside the wallet.


        :return: The password of this GenerateAutonomousDatabaseWalletDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this GenerateAutonomousDatabaseWalletDetails.
        The password to encrypt the keys inside the wallet.


        :param password: The password of this GenerateAutonomousDatabaseWalletDetails.
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
