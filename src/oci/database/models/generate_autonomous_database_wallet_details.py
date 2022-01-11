# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateAutonomousDatabaseWalletDetails(object):
    """
    Details to create and download an Oracle Autonomous Database wallet.
    """

    #: A constant which can be used with the generate_type property of a GenerateAutonomousDatabaseWalletDetails.
    #: This constant has a value of "ALL"
    GENERATE_TYPE_ALL = "ALL"

    #: A constant which can be used with the generate_type property of a GenerateAutonomousDatabaseWalletDetails.
    #: This constant has a value of "SINGLE"
    GENERATE_TYPE_SINGLE = "SINGLE"

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateAutonomousDatabaseWalletDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param generate_type:
            The value to assign to the generate_type property of this GenerateAutonomousDatabaseWalletDetails.
            Allowed values for this property are: "ALL", "SINGLE"
        :type generate_type: str

        :param password:
            The value to assign to the password property of this GenerateAutonomousDatabaseWalletDetails.
        :type password: str

        """
        self.swagger_types = {
            'generate_type': 'str',
            'password': 'str'
        }

        self.attribute_map = {
            'generate_type': 'generateType',
            'password': 'password'
        }

        self._generate_type = None
        self._password = None

    @property
    def generate_type(self):
        """
        Gets the generate_type of this GenerateAutonomousDatabaseWalletDetails.
        The type of wallet to generate.

        **Shared Exadata infrastructure usage:**
        * `SINGLE` - used to generate a wallet for a single database
        * `ALL` - used to generate wallet for all databases in the region

        **Dedicated Exadata infrastructure usage:** Value must be `NULL` if attribute is used.

        Allowed values for this property are: "ALL", "SINGLE"


        :return: The generate_type of this GenerateAutonomousDatabaseWalletDetails.
        :rtype: str
        """
        return self._generate_type

    @generate_type.setter
    def generate_type(self, generate_type):
        """
        Sets the generate_type of this GenerateAutonomousDatabaseWalletDetails.
        The type of wallet to generate.

        **Shared Exadata infrastructure usage:**
        * `SINGLE` - used to generate a wallet for a single database
        * `ALL` - used to generate wallet for all databases in the region

        **Dedicated Exadata infrastructure usage:** Value must be `NULL` if attribute is used.


        :param generate_type: The generate_type of this GenerateAutonomousDatabaseWalletDetails.
        :type: str
        """
        allowed_values = ["ALL", "SINGLE"]
        if not value_allowed_none_or_none_sentinel(generate_type, allowed_values):
            raise ValueError(
                "Invalid value for `generate_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._generate_type = generate_type

    @property
    def password(self):
        """
        **[Required]** Gets the password of this GenerateAutonomousDatabaseWalletDetails.
        The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and must include at least 1 letter and either 1 numeric character or 1 special character.


        :return: The password of this GenerateAutonomousDatabaseWalletDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this GenerateAutonomousDatabaseWalletDetails.
        The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and must include at least 1 letter and either 1 numeric character or 1 special character.


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
