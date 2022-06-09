# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_tools_user_password_details import DatabaseToolsUserPasswordDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsUserPasswordSecretIdDetails(DatabaseToolsUserPasswordDetails):
    """
    The user password.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsUserPasswordSecretIdDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_tools.models.DatabaseToolsUserPasswordSecretIdDetails.value_type` attribute
        of this class is ``SECRETID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value_type:
            The value to assign to the value_type property of this DatabaseToolsUserPasswordSecretIdDetails.
            Allowed values for this property are: "SECRETID"
        :type value_type: str

        :param secret_id:
            The value to assign to the secret_id property of this DatabaseToolsUserPasswordSecretIdDetails.
        :type secret_id: str

        """
        self.swagger_types = {
            'value_type': 'str',
            'secret_id': 'str'
        }

        self.attribute_map = {
            'value_type': 'valueType',
            'secret_id': 'secretId'
        }

        self._value_type = None
        self._secret_id = None
        self._value_type = 'SECRETID'

    @property
    def secret_id(self):
        """
        **[Required]** Gets the secret_id of this DatabaseToolsUserPasswordSecretIdDetails.
        The `OCID`__ of the secret containing the user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The secret_id of this DatabaseToolsUserPasswordSecretIdDetails.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this DatabaseToolsUserPasswordSecretIdDetails.
        The `OCID`__ of the secret containing the user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param secret_id: The secret_id of this DatabaseToolsUserPasswordSecretIdDetails.
        :type: str
        """
        self._secret_id = secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
