# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .client_app_details import ClientAppDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomClientAppDetails(ClientAppDetails):
    """
    Client App Credentials to be provided again.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomClientAppDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.CustomClientAppDetails.type` attribute
        of this class is ``CUSTOM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CustomClientAppDetails.
            Allowed values for this property are: "VALIDATION_BLOCK", "CUSTOM"
        :type type: str

        :param client_id:
            The value to assign to the client_id property of this CustomClientAppDetails.
        :type client_id: str

        :param client_secret_id:
            The value to assign to the client_secret_id property of this CustomClientAppDetails.
        :type client_secret_id: str

        :param client_secret_version_number:
            The value to assign to the client_secret_version_number property of this CustomClientAppDetails.
        :type client_secret_version_number: int

        """
        self.swagger_types = {
            'type': 'str',
            'client_id': 'str',
            'client_secret_id': 'str',
            'client_secret_version_number': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'client_id': 'clientId',
            'client_secret_id': 'clientSecretId',
            'client_secret_version_number': 'clientSecretVersionNumber'
        }

        self._type = None
        self._client_id = None
        self._client_secret_id = None
        self._client_secret_version_number = None
        self._type = 'CUSTOM'

    @property
    def client_id(self):
        """
        **[Required]** Gets the client_id of this CustomClientAppDetails.
        Client ID for the OAuth2/OIDC app.


        :return: The client_id of this CustomClientAppDetails.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CustomClientAppDetails.
        Client ID for the OAuth2/OIDC app.


        :param client_id: The client_id of this CustomClientAppDetails.
        :type: str
        """
        self._client_id = client_id

    @property
    def client_secret_id(self):
        """
        **[Required]** Gets the client_secret_id of this CustomClientAppDetails.
        The `OCID`__ of the Oracle Vault Service secret resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The client_secret_id of this CustomClientAppDetails.
        :rtype: str
        """
        return self._client_secret_id

    @client_secret_id.setter
    def client_secret_id(self, client_secret_id):
        """
        Sets the client_secret_id of this CustomClientAppDetails.
        The `OCID`__ of the Oracle Vault Service secret resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param client_secret_id: The client_secret_id of this CustomClientAppDetails.
        :type: str
        """
        self._client_secret_id = client_secret_id

    @property
    def client_secret_version_number(self):
        """
        **[Required]** Gets the client_secret_version_number of this CustomClientAppDetails.
        The version number of the client secret to use.


        :return: The client_secret_version_number of this CustomClientAppDetails.
        :rtype: int
        """
        return self._client_secret_version_number

    @client_secret_version_number.setter
    def client_secret_version_number(self, client_secret_version_number):
        """
        Sets the client_secret_version_number of this CustomClientAppDetails.
        The version number of the client secret to use.


        :param client_secret_version_number: The client_secret_version_number of this CustomClientAppDetails.
        :type: int
        """
        self._client_secret_version_number = client_secret_version_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
