# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdentitySettingsMyProfile(object):
    """
    Whether to allow users to update their own profile.

    **Added In:** 2207040824

    **SCIM++ Properties:**
    - caseExact: false
    - multiValued: false
    - required: false
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IdentitySettingsMyProfile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param allow_end_users_to_change_their_password:
            The value to assign to the allow_end_users_to_change_their_password property of this IdentitySettingsMyProfile.
        :type allow_end_users_to_change_their_password: bool

        :param allow_end_users_to_link_their_support_account:
            The value to assign to the allow_end_users_to_link_their_support_account property of this IdentitySettingsMyProfile.
        :type allow_end_users_to_link_their_support_account: bool

        :param allow_end_users_to_update_their_security_settings:
            The value to assign to the allow_end_users_to_update_their_security_settings property of this IdentitySettingsMyProfile.
        :type allow_end_users_to_update_their_security_settings: bool

        :param allow_end_users_to_manage_their_capabilities:
            The value to assign to the allow_end_users_to_manage_their_capabilities property of this IdentitySettingsMyProfile.
        :type allow_end_users_to_manage_their_capabilities: bool

        """
        self.swagger_types = {
            'allow_end_users_to_change_their_password': 'bool',
            'allow_end_users_to_link_their_support_account': 'bool',
            'allow_end_users_to_update_their_security_settings': 'bool',
            'allow_end_users_to_manage_their_capabilities': 'bool'
        }
        self.attribute_map = {
            'allow_end_users_to_change_their_password': 'allowEndUsersToChangeTheirPassword',
            'allow_end_users_to_link_their_support_account': 'allowEndUsersToLinkTheirSupportAccount',
            'allow_end_users_to_update_their_security_settings': 'allowEndUsersToUpdateTheirSecuritySettings',
            'allow_end_users_to_manage_their_capabilities': 'allowEndUsersToManageTheirCapabilities'
        }
        self._allow_end_users_to_change_their_password = None
        self._allow_end_users_to_link_their_support_account = None
        self._allow_end_users_to_update_their_security_settings = None
        self._allow_end_users_to_manage_their_capabilities = None

    @property
    def allow_end_users_to_change_their_password(self):
        """
        Gets the allow_end_users_to_change_their_password of this IdentitySettingsMyProfile.
        Whether to allow users to change their own password.

        **Added In:** 2207040824

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The allow_end_users_to_change_their_password of this IdentitySettingsMyProfile.
        :rtype: bool
        """
        return self._allow_end_users_to_change_their_password

    @allow_end_users_to_change_their_password.setter
    def allow_end_users_to_change_their_password(self, allow_end_users_to_change_their_password):
        """
        Sets the allow_end_users_to_change_their_password of this IdentitySettingsMyProfile.
        Whether to allow users to change their own password.

        **Added In:** 2207040824

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param allow_end_users_to_change_their_password: The allow_end_users_to_change_their_password of this IdentitySettingsMyProfile.
        :type: bool
        """
        self._allow_end_users_to_change_their_password = allow_end_users_to_change_their_password

    @property
    def allow_end_users_to_link_their_support_account(self):
        """
        Gets the allow_end_users_to_link_their_support_account of this IdentitySettingsMyProfile.
        Whether to allow users to link or unlink their support accounts.

        **Added In:** 2207040824

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The allow_end_users_to_link_their_support_account of this IdentitySettingsMyProfile.
        :rtype: bool
        """
        return self._allow_end_users_to_link_their_support_account

    @allow_end_users_to_link_their_support_account.setter
    def allow_end_users_to_link_their_support_account(self, allow_end_users_to_link_their_support_account):
        """
        Sets the allow_end_users_to_link_their_support_account of this IdentitySettingsMyProfile.
        Whether to allow users to link or unlink their support accounts.

        **Added In:** 2207040824

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param allow_end_users_to_link_their_support_account: The allow_end_users_to_link_their_support_account of this IdentitySettingsMyProfile.
        :type: bool
        """
        self._allow_end_users_to_link_their_support_account = allow_end_users_to_link_their_support_account

    @property
    def allow_end_users_to_update_their_security_settings(self):
        """
        Gets the allow_end_users_to_update_their_security_settings of this IdentitySettingsMyProfile.
        Whether to allow users to update their security settings.

        **Added In:** 2207040824

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The allow_end_users_to_update_their_security_settings of this IdentitySettingsMyProfile.
        :rtype: bool
        """
        return self._allow_end_users_to_update_their_security_settings

    @allow_end_users_to_update_their_security_settings.setter
    def allow_end_users_to_update_their_security_settings(self, allow_end_users_to_update_their_security_settings):
        """
        Sets the allow_end_users_to_update_their_security_settings of this IdentitySettingsMyProfile.
        Whether to allow users to update their security settings.

        **Added In:** 2207040824

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param allow_end_users_to_update_their_security_settings: The allow_end_users_to_update_their_security_settings of this IdentitySettingsMyProfile.
        :type: bool
        """
        self._allow_end_users_to_update_their_security_settings = allow_end_users_to_update_their_security_settings

    @property
    def allow_end_users_to_manage_their_capabilities(self):
        """
        Gets the allow_end_users_to_manage_their_capabilities of this IdentitySettingsMyProfile.
        Whether to allow users to update their capabilities.

        **Added In:** 2207040824

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The allow_end_users_to_manage_their_capabilities of this IdentitySettingsMyProfile.
        :rtype: bool
        """
        return self._allow_end_users_to_manage_their_capabilities

    @allow_end_users_to_manage_their_capabilities.setter
    def allow_end_users_to_manage_their_capabilities(self, allow_end_users_to_manage_their_capabilities):
        """
        Sets the allow_end_users_to_manage_their_capabilities of this IdentitySettingsMyProfile.
        Whether to allow users to update their capabilities.

        **Added In:** 2207040824

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param allow_end_users_to_manage_their_capabilities: The allow_end_users_to_manage_their_capabilities of this IdentitySettingsMyProfile.
        :type: bool
        """
        self._allow_end_users_to_manage_their_capabilities = allow_end_users_to_manage_their_capabilities

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
