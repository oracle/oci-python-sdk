# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionSelfRegistrationUser(object):
    """
    This extension defines attributes used to manage self registration profile linked to the user.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionSelfRegistrationUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param consent_granted:
            The value to assign to the consent_granted property of this ExtensionSelfRegistrationUser.
        :type consent_granted: bool

        :param user_token:
            The value to assign to the user_token property of this ExtensionSelfRegistrationUser.
        :type user_token: str

        :param self_registration_profile:
            The value to assign to the self_registration_profile property of this ExtensionSelfRegistrationUser.
        :type self_registration_profile: oci.identity_domains.models.UserExtSelfRegistrationProfile

        """
        self.swagger_types = {
            'consent_granted': 'bool',
            'user_token': 'str',
            'self_registration_profile': 'UserExtSelfRegistrationProfile'
        }
        self.attribute_map = {
            'consent_granted': 'consentGranted',
            'user_token': 'userToken',
            'self_registration_profile': 'selfRegistrationProfile'
        }
        self._consent_granted = None
        self._user_token = None
        self._self_registration_profile = None

    @property
    def consent_granted(self):
        """
        Gets the consent_granted of this ExtensionSelfRegistrationUser.
        A boolean value that indicates whether the consent is granted.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The consent_granted of this ExtensionSelfRegistrationUser.
        :rtype: bool
        """
        return self._consent_granted

    @consent_granted.setter
    def consent_granted(self, consent_granted):
        """
        Sets the consent_granted of this ExtensionSelfRegistrationUser.
        A boolean value that indicates whether the consent is granted.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param consent_granted: The consent_granted of this ExtensionSelfRegistrationUser.
        :type: bool
        """
        self._consent_granted = consent_granted

    @property
    def user_token(self):
        """
        Gets the user_token of this ExtensionSelfRegistrationUser.
        User token used for auto-login.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The user_token of this ExtensionSelfRegistrationUser.
        :rtype: str
        """
        return self._user_token

    @user_token.setter
    def user_token(self, user_token):
        """
        Sets the user_token of this ExtensionSelfRegistrationUser.
        User token used for auto-login.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param user_token: The user_token of this ExtensionSelfRegistrationUser.
        :type: str
        """
        self._user_token = user_token

    @property
    def self_registration_profile(self):
        """
        **[Required]** Gets the self_registration_profile of this ExtensionSelfRegistrationUser.

        :return: The self_registration_profile of this ExtensionSelfRegistrationUser.
        :rtype: oci.identity_domains.models.UserExtSelfRegistrationProfile
        """
        return self._self_registration_profile

    @self_registration_profile.setter
    def self_registration_profile(self, self_registration_profile):
        """
        Sets the self_registration_profile of this ExtensionSelfRegistrationUser.

        :param self_registration_profile: The self_registration_profile of this ExtensionSelfRegistrationUser.
        :type: oci.identity_domains.models.UserExtSelfRegistrationProfile
        """
        self._self_registration_profile = self_registration_profile

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
