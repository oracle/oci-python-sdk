# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .sql_tuning_task_credential_details import SqlTuningTaskCredentialDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningTaskSecretCredentialDetails(SqlTuningTaskCredentialDetails):
    """
    The OCID of the Secret provided by the user to retrieve the password to connect to the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningTaskSecretCredentialDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.SqlTuningTaskSecretCredentialDetails.sql_tuning_task_credential_type` attribute
        of this class is ``SECRET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_tuning_task_credential_type:
            The value to assign to the sql_tuning_task_credential_type property of this SqlTuningTaskSecretCredentialDetails.
            Allowed values for this property are: "SECRET", "PASSWORD"
        :type sql_tuning_task_credential_type: str

        :param username:
            The value to assign to the username property of this SqlTuningTaskSecretCredentialDetails.
        :type username: str

        :param role:
            The value to assign to the role property of this SqlTuningTaskSecretCredentialDetails.
            Allowed values for this property are: "NORMAL", "SYSDBA"
        :type role: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this SqlTuningTaskSecretCredentialDetails.
        :type password_secret_id: str

        """
        self.swagger_types = {
            'sql_tuning_task_credential_type': 'str',
            'username': 'str',
            'role': 'str',
            'password_secret_id': 'str'
        }

        self.attribute_map = {
            'sql_tuning_task_credential_type': 'sqlTuningTaskCredentialType',
            'username': 'username',
            'role': 'role',
            'password_secret_id': 'passwordSecretId'
        }

        self._sql_tuning_task_credential_type = None
        self._username = None
        self._role = None
        self._password_secret_id = None
        self._sql_tuning_task_credential_type = 'SECRET'

    @property
    def password_secret_id(self):
        """
        **[Required]** Gets the password_secret_id of this SqlTuningTaskSecretCredentialDetails.
        The `OCID`__ of the Secret
        where the database password is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this SqlTuningTaskSecretCredentialDetails.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this SqlTuningTaskSecretCredentialDetails.
        The `OCID`__ of the Secret
        where the database password is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this SqlTuningTaskSecretCredentialDetails.
        :type: str
        """
        self._password_secret_id = password_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
