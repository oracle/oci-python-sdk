# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_connection_credentials import DatabaseConnectionCredentials
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseConnectionCredentailsByName(DatabaseConnectionCredentials):
    """
    Existing named credential used to connect to the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseConnectionCredentailsByName object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.DatabaseConnectionCredentailsByName.credential_type` attribute
        of this class is ``NAME_REFERENCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this DatabaseConnectionCredentailsByName.
            Allowed values for this property are: "NAME_REFERENCE", "DETAILS", "SSL_DETAILS"
        :type credential_type: str

        :param credential_name:
            The value to assign to the credential_name property of this DatabaseConnectionCredentailsByName.
        :type credential_name: str

        """
        self.swagger_types = {
            'credential_type': 'str',
            'credential_name': 'str'
        }

        self.attribute_map = {
            'credential_type': 'credentialType',
            'credential_name': 'credentialName'
        }

        self._credential_type = None
        self._credential_name = None
        self._credential_type = 'NAME_REFERENCE'

    @property
    def credential_name(self):
        """
        **[Required]** Gets the credential_name of this DatabaseConnectionCredentailsByName.
        The name of the credential information that used to connect to the database. The name should be in \"x.y\" format, where
        the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters.
        The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for
        the \".\" character that separates the \"x\" and \"y\" portions of the name.
        *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name
        that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already
        using the name.

        For example: inventorydb.abc112233445566778899


        :return: The credential_name of this DatabaseConnectionCredentailsByName.
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """
        Sets the credential_name of this DatabaseConnectionCredentailsByName.
        The name of the credential information that used to connect to the database. The name should be in \"x.y\" format, where
        the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters.
        The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for
        the \".\" character that separates the \"x\" and \"y\" portions of the name.
        *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name
        that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already
        using the name.

        For example: inventorydb.abc112233445566778899


        :param credential_name: The credential_name of this DatabaseConnectionCredentailsByName.
        :type: str
        """
        self._credential_name = credential_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
