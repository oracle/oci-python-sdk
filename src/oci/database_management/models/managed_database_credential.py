# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedDatabaseCredential(object):
    """
    The credential used to connect to the Managed Database and obtain the details of the optimizer statistics tasks.
    """

    #: A constant which can be used with the credential_type property of a ManagedDatabaseCredential.
    #: This constant has a value of "SECRET"
    CREDENTIAL_TYPE_SECRET = "SECRET"

    #: A constant which can be used with the credential_type property of a ManagedDatabaseCredential.
    #: This constant has a value of "PASSWORD"
    CREDENTIAL_TYPE_PASSWORD = "PASSWORD"

    #: A constant which can be used with the role property of a ManagedDatabaseCredential.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    #: A constant which can be used with the role property of a ManagedDatabaseCredential.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedDatabaseCredential object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.ManagedDatabasePasswordCredential`
        * :class:`~oci.database_management.models.ManagedDatabaseSecretCredential`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this ManagedDatabaseCredential.
            Allowed values for this property are: "SECRET", "PASSWORD"
        :type credential_type: str

        :param username:
            The value to assign to the username property of this ManagedDatabaseCredential.
        :type username: str

        :param role:
            The value to assign to the role property of this ManagedDatabaseCredential.
            Allowed values for this property are: "NORMAL", "SYSDBA"
        :type role: str

        """
        self.swagger_types = {
            'credential_type': 'str',
            'username': 'str',
            'role': 'str'
        }

        self.attribute_map = {
            'credential_type': 'credentialType',
            'username': 'username',
            'role': 'role'
        }

        self._credential_type = None
        self._username = None
        self._role = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['credentialType']

        if type == 'PASSWORD':
            return 'ManagedDatabasePasswordCredential'

        if type == 'SECRET':
            return 'ManagedDatabaseSecretCredential'
        else:
            return 'ManagedDatabaseCredential'

    @property
    def credential_type(self):
        """
        **[Required]** Gets the credential_type of this ManagedDatabaseCredential.
        Indicates the type of credential required to retrieve the details of the optimizer statistics tasks.

        Allowed values for this property are: "SECRET", "PASSWORD"


        :return: The credential_type of this ManagedDatabaseCredential.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """
        Sets the credential_type of this ManagedDatabaseCredential.
        Indicates the type of credential required to retrieve the details of the optimizer statistics tasks.


        :param credential_type: The credential_type of this ManagedDatabaseCredential.
        :type: str
        """
        allowed_values = ["SECRET", "PASSWORD"]
        if not value_allowed_none_or_none_sentinel(credential_type, allowed_values):
            raise ValueError(
                "Invalid value for `credential_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._credential_type = credential_type

    @property
    def username(self):
        """
        **[Required]** Gets the username of this ManagedDatabaseCredential.
        The user name used to connect to the database.


        :return: The username of this ManagedDatabaseCredential.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ManagedDatabaseCredential.
        The user name used to connect to the database.


        :param username: The username of this ManagedDatabaseCredential.
        :type: str
        """
        self._username = username

    @property
    def role(self):
        """
        **[Required]** Gets the role of this ManagedDatabaseCredential.
        The role of the database user.

        Allowed values for this property are: "NORMAL", "SYSDBA"


        :return: The role of this ManagedDatabaseCredential.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this ManagedDatabaseCredential.
        The role of the database user.


        :param role: The role of this ManagedDatabaseCredential.
        :type: str
        """
        allowed_values = ["NORMAL", "SYSDBA"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            raise ValueError(
                "Invalid value for `role`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
