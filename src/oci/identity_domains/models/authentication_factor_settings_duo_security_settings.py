# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationFactorSettingsDuoSecuritySettings(object):
    """
    Settings related to Duo Security

    **Added In:** 19.2.1

    **SCIM++ Properties:**
    - idcsSearchable: false
    - multiValued: false
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the user_mapping_attribute property of a AuthenticationFactorSettingsDuoSecuritySettings.
    #: This constant has a value of "primaryEmail"
    USER_MAPPING_ATTRIBUTE_PRIMARY_EMAIL = "primaryEmail"

    #: A constant which can be used with the user_mapping_attribute property of a AuthenticationFactorSettingsDuoSecuritySettings.
    #: This constant has a value of "userName"
    USER_MAPPING_ATTRIBUTE_USER_NAME = "userName"

    #: A constant which can be used with the user_mapping_attribute property of a AuthenticationFactorSettingsDuoSecuritySettings.
    #: This constant has a value of "givenName"
    USER_MAPPING_ATTRIBUTE_GIVEN_NAME = "givenName"

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationFactorSettingsDuoSecuritySettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param integration_key:
            The value to assign to the integration_key property of this AuthenticationFactorSettingsDuoSecuritySettings.
        :type integration_key: str

        :param secret_key:
            The value to assign to the secret_key property of this AuthenticationFactorSettingsDuoSecuritySettings.
        :type secret_key: str

        :param attestation_key:
            The value to assign to the attestation_key property of this AuthenticationFactorSettingsDuoSecuritySettings.
        :type attestation_key: str

        :param api_hostname:
            The value to assign to the api_hostname property of this AuthenticationFactorSettingsDuoSecuritySettings.
        :type api_hostname: str

        :param user_mapping_attribute:
            The value to assign to the user_mapping_attribute property of this AuthenticationFactorSettingsDuoSecuritySettings.
            Allowed values for this property are: "primaryEmail", "userName", "givenName", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type user_mapping_attribute: str

        """
        self.swagger_types = {
            'integration_key': 'str',
            'secret_key': 'str',
            'attestation_key': 'str',
            'api_hostname': 'str',
            'user_mapping_attribute': 'str'
        }
        self.attribute_map = {
            'integration_key': 'integrationKey',
            'secret_key': 'secretKey',
            'attestation_key': 'attestationKey',
            'api_hostname': 'apiHostname',
            'user_mapping_attribute': 'userMappingAttribute'
        }
        self._integration_key = None
        self._secret_key = None
        self._attestation_key = None
        self._api_hostname = None
        self._user_mapping_attribute = None

    @property
    def integration_key(self):
        """
        **[Required]** Gets the integration_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        Integration key from Duo Security authenticator

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The integration_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        :rtype: str
        """
        return self._integration_key

    @integration_key.setter
    def integration_key(self, integration_key):
        """
        Sets the integration_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        Integration key from Duo Security authenticator

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param integration_key: The integration_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        :type: str
        """
        self._integration_key = integration_key

    @property
    def secret_key(self):
        """
        **[Required]** Gets the secret_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        Secret key from Duo Security authenticator

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The secret_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """
        Sets the secret_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        Secret key from Duo Security authenticator

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param secret_key: The secret_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        :type: str
        """
        self._secret_key = secret_key

    @property
    def attestation_key(self):
        """
        Gets the attestation_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        Attestation key to attest the request and response between Duo Security

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: never
         - type: string
         - uniqueness: none


        :return: The attestation_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        :rtype: str
        """
        return self._attestation_key

    @attestation_key.setter
    def attestation_key(self, attestation_key):
        """
        Sets the attestation_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        Attestation key to attest the request and response between Duo Security

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: never
         - type: string
         - uniqueness: none


        :param attestation_key: The attestation_key of this AuthenticationFactorSettingsDuoSecuritySettings.
        :type: str
        """
        self._attestation_key = attestation_key

    @property
    def api_hostname(self):
        """
        **[Required]** Gets the api_hostname of this AuthenticationFactorSettingsDuoSecuritySettings.
        Hostname to access the Duo security account

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The api_hostname of this AuthenticationFactorSettingsDuoSecuritySettings.
        :rtype: str
        """
        return self._api_hostname

    @api_hostname.setter
    def api_hostname(self, api_hostname):
        """
        Sets the api_hostname of this AuthenticationFactorSettingsDuoSecuritySettings.
        Hostname to access the Duo security account

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param api_hostname: The api_hostname of this AuthenticationFactorSettingsDuoSecuritySettings.
        :type: str
        """
        self._api_hostname = api_hostname

    @property
    def user_mapping_attribute(self):
        """
        **[Required]** Gets the user_mapping_attribute of this AuthenticationFactorSettingsDuoSecuritySettings.
        User attribute mapping value

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "primaryEmail", "userName", "givenName", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The user_mapping_attribute of this AuthenticationFactorSettingsDuoSecuritySettings.
        :rtype: str
        """
        return self._user_mapping_attribute

    @user_mapping_attribute.setter
    def user_mapping_attribute(self, user_mapping_attribute):
        """
        Sets the user_mapping_attribute of this AuthenticationFactorSettingsDuoSecuritySettings.
        User attribute mapping value

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param user_mapping_attribute: The user_mapping_attribute of this AuthenticationFactorSettingsDuoSecuritySettings.
        :type: str
        """
        allowed_values = ["primaryEmail", "userName", "givenName"]
        if not value_allowed_none_or_none_sentinel(user_mapping_attribute, allowed_values):
            user_mapping_attribute = 'UNKNOWN_ENUM_VALUE'
        self._user_mapping_attribute = user_mapping_attribute

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
