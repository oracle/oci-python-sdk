# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CredentialAuthenticatorInfo(object):
    """
    CredentialAuthenticatorInfo model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CredentialAuthenticatorInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param raw_credential:
            The value to assign to the raw_credential property of this CredentialAuthenticatorInfo.
        :type raw_credential: str

        :param user_id:
            The value to assign to the user_id property of this CredentialAuthenticatorInfo.
        :type user_id: str

        :param tenant_id:
            The value to assign to the tenant_id property of this CredentialAuthenticatorInfo.
        :type tenant_id: str

        :param user_name:
            The value to assign to the user_name property of this CredentialAuthenticatorInfo.
        :type user_name: str

        :param tenant_name:
            The value to assign to the tenant_name property of this CredentialAuthenticatorInfo.
        :type tenant_name: str

        :param credential_identifier:
            The value to assign to the credential_identifier property of this CredentialAuthenticatorInfo.
        :type credential_identifier: str

        :param credential_list:
            The value to assign to the credential_list property of this CredentialAuthenticatorInfo.
        :type credential_list: list[str]

        :param service:
            The value to assign to the service property of this CredentialAuthenticatorInfo.
        :type service: str

        :param client_id:
            The value to assign to the client_id property of this CredentialAuthenticatorInfo.
        :type client_id: str

        """
        self.swagger_types = {
            'raw_credential': 'str',
            'user_id': 'str',
            'tenant_id': 'str',
            'user_name': 'str',
            'tenant_name': 'str',
            'credential_identifier': 'str',
            'credential_list': 'list[str]',
            'service': 'str',
            'client_id': 'str'
        }

        self.attribute_map = {
            'raw_credential': 'rawCredential',
            'user_id': 'userId',
            'tenant_id': 'tenantId',
            'user_name': 'userName',
            'tenant_name': 'tenantName',
            'credential_identifier': 'credentialIdentifier',
            'credential_list': 'credentialList',
            'service': 'service',
            'client_id': 'clientId'
        }

        self._raw_credential = None
        self._user_id = None
        self._tenant_id = None
        self._user_name = None
        self._tenant_name = None
        self._credential_identifier = None
        self._credential_list = None
        self._service = None
        self._client_id = None

    @property
    def raw_credential(self):
        """
        **[Required]** Gets the raw_credential of this CredentialAuthenticatorInfo.
        The raw credential.


        :return: The raw_credential of this CredentialAuthenticatorInfo.
        :rtype: str
        """
        return self._raw_credential

    @raw_credential.setter
    def raw_credential(self, raw_credential):
        """
        Sets the raw_credential of this CredentialAuthenticatorInfo.
        The raw credential.


        :param raw_credential: The raw_credential of this CredentialAuthenticatorInfo.
        :type: str
        """
        self._raw_credential = raw_credential

    @property
    def user_id(self):
        """
        **[Required]** Gets the user_id of this CredentialAuthenticatorInfo.
        The id of the user.


        :return: The user_id of this CredentialAuthenticatorInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CredentialAuthenticatorInfo.
        The id of the user.


        :param user_id: The user_id of this CredentialAuthenticatorInfo.
        :type: str
        """
        self._user_id = user_id

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this CredentialAuthenticatorInfo.
        The id of the tenant.


        :return: The tenant_id of this CredentialAuthenticatorInfo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this CredentialAuthenticatorInfo.
        The id of the tenant.


        :param tenant_id: The tenant_id of this CredentialAuthenticatorInfo.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this CredentialAuthenticatorInfo.
        The name of the user.


        :return: The user_name of this CredentialAuthenticatorInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this CredentialAuthenticatorInfo.
        The name of the user.


        :param user_name: The user_name of this CredentialAuthenticatorInfo.
        :type: str
        """
        self._user_name = user_name

    @property
    def tenant_name(self):
        """
        **[Required]** Gets the tenant_name of this CredentialAuthenticatorInfo.
        The name of the tenant.


        :return: The tenant_name of this CredentialAuthenticatorInfo.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """
        Sets the tenant_name of this CredentialAuthenticatorInfo.
        The name of the tenant.


        :param tenant_name: The tenant_name of this CredentialAuthenticatorInfo.
        :type: str
        """
        self._tenant_name = tenant_name

    @property
    def credential_identifier(self):
        """
        **[Required]** Gets the credential_identifier of this CredentialAuthenticatorInfo.
        The credential identifier.


        :return: The credential_identifier of this CredentialAuthenticatorInfo.
        :rtype: str
        """
        return self._credential_identifier

    @credential_identifier.setter
    def credential_identifier(self, credential_identifier):
        """
        Sets the credential_identifier of this CredentialAuthenticatorInfo.
        The credential identifier.


        :param credential_identifier: The credential_identifier of this CredentialAuthenticatorInfo.
        :type: str
        """
        self._credential_identifier = credential_identifier

    @property
    def credential_list(self):
        """
        **[Required]** Gets the credential_list of this CredentialAuthenticatorInfo.
        The credential list.


        :return: The credential_list of this CredentialAuthenticatorInfo.
        :rtype: list[str]
        """
        return self._credential_list

    @credential_list.setter
    def credential_list(self, credential_list):
        """
        Sets the credential_list of this CredentialAuthenticatorInfo.
        The credential list.


        :param credential_list: The credential_list of this CredentialAuthenticatorInfo.
        :type: list[str]
        """
        self._credential_list = credential_list

    @property
    def service(self):
        """
        **[Required]** Gets the service of this CredentialAuthenticatorInfo.
        The name of the service that is making this authorization request.


        :return: The service of this CredentialAuthenticatorInfo.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this CredentialAuthenticatorInfo.
        The name of the service that is making this authorization request.


        :param service: The service of this CredentialAuthenticatorInfo.
        :type: str
        """
        self._service = service

    @property
    def client_id(self):
        """
        **[Required]** Gets the client_id of this CredentialAuthenticatorInfo.
        The id of the client.


        :return: The client_id of this CredentialAuthenticatorInfo.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CredentialAuthenticatorInfo.
        The id of the client.


        :param client_id: The client_id of this CredentialAuthenticatorInfo.
        :type: str
        """
        self._client_id = client_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
