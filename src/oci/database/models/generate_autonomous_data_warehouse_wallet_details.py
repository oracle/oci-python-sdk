# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateAutonomousDataWarehouseWalletDetails(object):
    """
    Details to create and download a wallet for an Oracle Autonomous Data Warehouse.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateAutonomousDataWarehouseWalletDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password:
            The value to assign to the password property of this GenerateAutonomousDataWarehouseWalletDetails.
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
        **[Required]** Gets the password of this GenerateAutonomousDataWarehouseWalletDetails.
        The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and must include at least 1 letter and either 1 numeric character or 1 special character.


        :return: The password of this GenerateAutonomousDataWarehouseWalletDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this GenerateAutonomousDataWarehouseWalletDetails.
        The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and must include at least 1 letter and either 1 numeric character or 1 special character.


        :param password: The password of this GenerateAutonomousDataWarehouseWalletDetails.
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
