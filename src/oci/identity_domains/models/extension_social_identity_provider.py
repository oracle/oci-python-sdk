# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionSocialIdentityProvider(object):
    """
    Social Identity Provider Extension Schema
    """

    #: A constant which can be used with the status property of a ExtensionSocialIdentityProvider.
    #: This constant has a value of "created"
    STATUS_CREATED = "created"

    #: A constant which can be used with the status property of a ExtensionSocialIdentityProvider.
    #: This constant has a value of "deleted"
    STATUS_DELETED = "deleted"

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionSocialIdentityProvider object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param account_linking_enabled:
            The value to assign to the account_linking_enabled property of this ExtensionSocialIdentityProvider.
        :type account_linking_enabled: bool

        :param registration_enabled:
            The value to assign to the registration_enabled property of this ExtensionSocialIdentityProvider.
        :type registration_enabled: bool

        :param status:
            The value to assign to the status property of this ExtensionSocialIdentityProvider.
            Allowed values for this property are: "created", "deleted", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param authz_url:
            The value to assign to the authz_url property of this ExtensionSocialIdentityProvider.
        :type authz_url: str

        :param access_token_url:
            The value to assign to the access_token_url property of this ExtensionSocialIdentityProvider.
        :type access_token_url: str

        :param profile_url:
            The value to assign to the profile_url property of this ExtensionSocialIdentityProvider.
        :type profile_url: str

        :param scope:
            The value to assign to the scope property of this ExtensionSocialIdentityProvider.
        :type scope: list[str]

        :param admin_scope:
            The value to assign to the admin_scope property of this ExtensionSocialIdentityProvider.
        :type admin_scope: list[str]

        :param consumer_key:
            The value to assign to the consumer_key property of this ExtensionSocialIdentityProvider.
        :type consumer_key: str

        :param consumer_secret:
            The value to assign to the consumer_secret property of this ExtensionSocialIdentityProvider.
        :type consumer_secret: str

        :param service_provider_name:
            The value to assign to the service_provider_name property of this ExtensionSocialIdentityProvider.
        :type service_provider_name: str

        :param clock_skew_in_seconds:
            The value to assign to the clock_skew_in_seconds property of this ExtensionSocialIdentityProvider.
        :type clock_skew_in_seconds: int

        :param redirect_url:
            The value to assign to the redirect_url property of this ExtensionSocialIdentityProvider.
        :type redirect_url: str

        :param discovery_url:
            The value to assign to the discovery_url property of this ExtensionSocialIdentityProvider.
        :type discovery_url: str

        :param client_credential_in_payload:
            The value to assign to the client_credential_in_payload property of this ExtensionSocialIdentityProvider.
        :type client_credential_in_payload: bool

        :param id_attribute:
            The value to assign to the id_attribute property of this ExtensionSocialIdentityProvider.
        :type id_attribute: str

        """
        self.swagger_types = {
            'account_linking_enabled': 'bool',
            'registration_enabled': 'bool',
            'status': 'str',
            'authz_url': 'str',
            'access_token_url': 'str',
            'profile_url': 'str',
            'scope': 'list[str]',
            'admin_scope': 'list[str]',
            'consumer_key': 'str',
            'consumer_secret': 'str',
            'service_provider_name': 'str',
            'clock_skew_in_seconds': 'int',
            'redirect_url': 'str',
            'discovery_url': 'str',
            'client_credential_in_payload': 'bool',
            'id_attribute': 'str'
        }

        self.attribute_map = {
            'account_linking_enabled': 'accountLinkingEnabled',
            'registration_enabled': 'registrationEnabled',
            'status': 'status',
            'authz_url': 'authzUrl',
            'access_token_url': 'accessTokenUrl',
            'profile_url': 'profileUrl',
            'scope': 'scope',
            'admin_scope': 'adminScope',
            'consumer_key': 'consumerKey',
            'consumer_secret': 'consumerSecret',
            'service_provider_name': 'serviceProviderName',
            'clock_skew_in_seconds': 'clockSkewInSeconds',
            'redirect_url': 'redirectUrl',
            'discovery_url': 'discoveryUrl',
            'client_credential_in_payload': 'clientCredentialInPayload',
            'id_attribute': 'idAttribute'
        }

        self._account_linking_enabled = None
        self._registration_enabled = None
        self._status = None
        self._authz_url = None
        self._access_token_url = None
        self._profile_url = None
        self._scope = None
        self._admin_scope = None
        self._consumer_key = None
        self._consumer_secret = None
        self._service_provider_name = None
        self._clock_skew_in_seconds = None
        self._redirect_url = None
        self._discovery_url = None
        self._client_credential_in_payload = None
        self._id_attribute = None

    @property
    def account_linking_enabled(self):
        """
        **[Required]** Gets the account_linking_enabled of this ExtensionSocialIdentityProvider.
        Whether account linking is enabled

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The account_linking_enabled of this ExtensionSocialIdentityProvider.
        :rtype: bool
        """
        return self._account_linking_enabled

    @account_linking_enabled.setter
    def account_linking_enabled(self, account_linking_enabled):
        """
        Sets the account_linking_enabled of this ExtensionSocialIdentityProvider.
        Whether account linking is enabled

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param account_linking_enabled: The account_linking_enabled of this ExtensionSocialIdentityProvider.
        :type: bool
        """
        self._account_linking_enabled = account_linking_enabled

    @property
    def registration_enabled(self):
        """
        **[Required]** Gets the registration_enabled of this ExtensionSocialIdentityProvider.
        Whether registration is enabled

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The registration_enabled of this ExtensionSocialIdentityProvider.
        :rtype: bool
        """
        return self._registration_enabled

    @registration_enabled.setter
    def registration_enabled(self, registration_enabled):
        """
        Sets the registration_enabled of this ExtensionSocialIdentityProvider.
        Whether registration is enabled

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param registration_enabled: The registration_enabled of this ExtensionSocialIdentityProvider.
        :type: bool
        """
        self._registration_enabled = registration_enabled

    @property
    def status(self):
        """
        Gets the status of this ExtensionSocialIdentityProvider.
        Status

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "created", "deleted", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ExtensionSocialIdentityProvider.
        Status

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param status: The status of this ExtensionSocialIdentityProvider.
        :type: str
        """
        allowed_values = ["created", "deleted"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def authz_url(self):
        """
        Gets the authz_url of this ExtensionSocialIdentityProvider.
        Social IDP Authorization URL

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The authz_url of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._authz_url

    @authz_url.setter
    def authz_url(self, authz_url):
        """
        Sets the authz_url of this ExtensionSocialIdentityProvider.
        Social IDP Authorization URL

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param authz_url: The authz_url of this ExtensionSocialIdentityProvider.
        :type: str
        """
        self._authz_url = authz_url

    @property
    def access_token_url(self):
        """
        Gets the access_token_url of this ExtensionSocialIdentityProvider.
        Social IDP Access token URL

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The access_token_url of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._access_token_url

    @access_token_url.setter
    def access_token_url(self, access_token_url):
        """
        Sets the access_token_url of this ExtensionSocialIdentityProvider.
        Social IDP Access token URL

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param access_token_url: The access_token_url of this ExtensionSocialIdentityProvider.
        :type: str
        """
        self._access_token_url = access_token_url

    @property
    def profile_url(self):
        """
        Gets the profile_url of this ExtensionSocialIdentityProvider.
        Social IDP User profile URL

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The profile_url of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        """
        Sets the profile_url of this ExtensionSocialIdentityProvider.
        Social IDP User profile URL

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param profile_url: The profile_url of this ExtensionSocialIdentityProvider.
        :type: str
        """
        self._profile_url = profile_url

    @property
    def scope(self):
        """
        Gets the scope of this ExtensionSocialIdentityProvider.
        Scope to request

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The scope of this ExtensionSocialIdentityProvider.
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this ExtensionSocialIdentityProvider.
        Scope to request

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param scope: The scope of this ExtensionSocialIdentityProvider.
        :type: list[str]
        """
        self._scope = scope

    @property
    def admin_scope(self):
        """
        Gets the admin_scope of this ExtensionSocialIdentityProvider.
        Admin scope to request

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The admin_scope of this ExtensionSocialIdentityProvider.
        :rtype: list[str]
        """
        return self._admin_scope

    @admin_scope.setter
    def admin_scope(self, admin_scope):
        """
        Sets the admin_scope of this ExtensionSocialIdentityProvider.
        Admin scope to request

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param admin_scope: The admin_scope of this ExtensionSocialIdentityProvider.
        :type: list[str]
        """
        self._admin_scope = admin_scope

    @property
    def consumer_key(self):
        """
        **[Required]** Gets the consumer_key of this ExtensionSocialIdentityProvider.
        Social IDP Client Application Client ID

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The consumer_key of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._consumer_key

    @consumer_key.setter
    def consumer_key(self, consumer_key):
        """
        Sets the consumer_key of this ExtensionSocialIdentityProvider.
        Social IDP Client Application Client ID

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param consumer_key: The consumer_key of this ExtensionSocialIdentityProvider.
        :type: str
        """
        self._consumer_key = consumer_key

    @property
    def consumer_secret(self):
        """
        **[Required]** Gets the consumer_secret of this ExtensionSocialIdentityProvider.
        Social IDP Client Application Client Secret

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsSensitive: encrypt
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The consumer_secret of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._consumer_secret

    @consumer_secret.setter
    def consumer_secret(self, consumer_secret):
        """
        Sets the consumer_secret of this ExtensionSocialIdentityProvider.
        Social IDP Client Application Client Secret

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsSensitive: encrypt
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param consumer_secret: The consumer_secret of this ExtensionSocialIdentityProvider.
        :type: str
        """
        self._consumer_secret = consumer_secret

    @property
    def service_provider_name(self):
        """
        **[Required]** Gets the service_provider_name of this ExtensionSocialIdentityProvider.
        Service Provider Name

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The service_provider_name of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._service_provider_name

    @service_provider_name.setter
    def service_provider_name(self, service_provider_name):
        """
        Sets the service_provider_name of this ExtensionSocialIdentityProvider.
        Service Provider Name

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param service_provider_name: The service_provider_name of this ExtensionSocialIdentityProvider.
        :type: str
        """
        self._service_provider_name = service_provider_name

    @property
    def clock_skew_in_seconds(self):
        """
        Gets the clock_skew_in_seconds of this ExtensionSocialIdentityProvider.
        Social IDP allowed clock skew time

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The clock_skew_in_seconds of this ExtensionSocialIdentityProvider.
        :rtype: int
        """
        return self._clock_skew_in_seconds

    @clock_skew_in_seconds.setter
    def clock_skew_in_seconds(self, clock_skew_in_seconds):
        """
        Sets the clock_skew_in_seconds of this ExtensionSocialIdentityProvider.
        Social IDP allowed clock skew time

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :param clock_skew_in_seconds: The clock_skew_in_seconds of this ExtensionSocialIdentityProvider.
        :type: int
        """
        self._clock_skew_in_seconds = clock_skew_in_seconds

    @property
    def redirect_url(self):
        """
        Gets the redirect_url of this ExtensionSocialIdentityProvider.
        redirect URL for social idp

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The redirect_url of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """
        Sets the redirect_url of this ExtensionSocialIdentityProvider.
        redirect URL for social idp

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param redirect_url: The redirect_url of this ExtensionSocialIdentityProvider.
        :type: str
        """
        self._redirect_url = redirect_url

    @property
    def discovery_url(self):
        """
        Gets the discovery_url of this ExtensionSocialIdentityProvider.
        Discovery URL

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The discovery_url of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._discovery_url

    @discovery_url.setter
    def discovery_url(self, discovery_url):
        """
        Sets the discovery_url of this ExtensionSocialIdentityProvider.
        Discovery URL

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param discovery_url: The discovery_url of this ExtensionSocialIdentityProvider.
        :type: str
        """
        self._discovery_url = discovery_url

    @property
    def client_credential_in_payload(self):
        """
        Gets the client_credential_in_payload of this ExtensionSocialIdentityProvider.
        Whether the client credential is contained in payload

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The client_credential_in_payload of this ExtensionSocialIdentityProvider.
        :rtype: bool
        """
        return self._client_credential_in_payload

    @client_credential_in_payload.setter
    def client_credential_in_payload(self, client_credential_in_payload):
        """
        Sets the client_credential_in_payload of this ExtensionSocialIdentityProvider.
        Whether the client credential is contained in payload

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param client_credential_in_payload: The client_credential_in_payload of this ExtensionSocialIdentityProvider.
        :type: bool
        """
        self._client_credential_in_payload = client_credential_in_payload

    @property
    def id_attribute(self):
        """
        Gets the id_attribute of this ExtensionSocialIdentityProvider.
        Id attribute used for account linking

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The id_attribute of this ExtensionSocialIdentityProvider.
        :rtype: str
        """
        return self._id_attribute

    @id_attribute.setter
    def id_attribute(self, id_attribute):
        """
        Sets the id_attribute of this ExtensionSocialIdentityProvider.
        Id attribute used for account linking

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param id_attribute: The id_attribute of this ExtensionSocialIdentityProvider.
        :type: str
        """
        self._id_attribute = id_attribute

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
