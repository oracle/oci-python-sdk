# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseConnectionCredentials(object):
    """
    Credentials used to connect to the database. Currently only the `DETAILS` type is supported for creating MACS connector crendentials.
    """

    #: A constant which can be used with the credential_type property of a DatabaseConnectionCredentials.
    #: This constant has a value of "NAME_REFERENCE"
    CREDENTIAL_TYPE_NAME_REFERENCE = "NAME_REFERENCE"

    #: A constant which can be used with the credential_type property of a DatabaseConnectionCredentials.
    #: This constant has a value of "DETAILS"
    CREDENTIAL_TYPE_DETAILS = "DETAILS"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseConnectionCredentials object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.DatabaseConnectionCredentailsByName`
        * :class:`~oci.database.models.DatabaseConnectionCredentialsByDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this DatabaseConnectionCredentials.
            Allowed values for this property are: "NAME_REFERENCE", "DETAILS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        """
        self.swagger_types = {
            'credential_type': 'str'
        }

        self.attribute_map = {
            'credential_type': 'credentialType'
        }

        self._credential_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['credentialType']

        if type == 'NAME_REFERENCE':
            return 'DatabaseConnectionCredentailsByName'

        if type == 'DETAILS':
            return 'DatabaseConnectionCredentialsByDetails'
        else:
            return 'DatabaseConnectionCredentials'

    @property
    def credential_type(self):
        """
        Gets the credential_type of this DatabaseConnectionCredentials.
        The type of credential used to connect to the database.

        Allowed values for this property are: "NAME_REFERENCE", "DETAILS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The credential_type of this DatabaseConnectionCredentials.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """
        Sets the credential_type of this DatabaseConnectionCredentials.
        The type of credential used to connect to the database.


        :param credential_type: The credential_type of this DatabaseConnectionCredentials.
        :type: str
        """
        allowed_values = ["NAME_REFERENCE", "DETAILS"]
        if not value_allowed_none_or_none_sentinel(credential_type, allowed_values):
            credential_type = 'UNKNOWN_ENUM_VALUE'
        self._credential_type = credential_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
