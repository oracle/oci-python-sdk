# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOAuth2ClientCredentialDetails(object):
    """
    UpdateOAuth2ClientCredentialDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOAuth2ClientCredentialDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateOAuth2ClientCredentialDetails.
        :type description: str

        :param scopes:
            The value to assign to the scopes property of this UpdateOAuth2ClientCredentialDetails.
        :type scopes: list[oci.identity.models.FullyQualifiedScope]

        :param is_reset_password:
            The value to assign to the is_reset_password property of this UpdateOAuth2ClientCredentialDetails.
        :type is_reset_password: bool

        """
        self.swagger_types = {
            'description': 'str',
            'scopes': 'list[FullyQualifiedScope]',
            'is_reset_password': 'bool'
        }

        self.attribute_map = {
            'description': 'description',
            'scopes': 'scopes',
            'is_reset_password': 'isResetPassword'
        }

        self._description = None
        self._scopes = None
        self._is_reset_password = None

    @property
    def description(self):
        """
        **[Required]** Gets the description of this UpdateOAuth2ClientCredentialDetails.
        Description of the oauth credential to help user differentiate them.


        :return: The description of this UpdateOAuth2ClientCredentialDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateOAuth2ClientCredentialDetails.
        Description of the oauth credential to help user differentiate them.


        :param description: The description of this UpdateOAuth2ClientCredentialDetails.
        :type: str
        """
        self._description = description

    @property
    def scopes(self):
        """
        **[Required]** Gets the scopes of this UpdateOAuth2ClientCredentialDetails.
        Allowed scopes for the given oauth credential.


        :return: The scopes of this UpdateOAuth2ClientCredentialDetails.
        :rtype: list[oci.identity.models.FullyQualifiedScope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this UpdateOAuth2ClientCredentialDetails.
        Allowed scopes for the given oauth credential.


        :param scopes: The scopes of this UpdateOAuth2ClientCredentialDetails.
        :type: list[oci.identity.models.FullyQualifiedScope]
        """
        self._scopes = scopes

    @property
    def is_reset_password(self):
        """
        Gets the is_reset_password of this UpdateOAuth2ClientCredentialDetails.
        Indicate if the password to be reset or not in the update.


        :return: The is_reset_password of this UpdateOAuth2ClientCredentialDetails.
        :rtype: bool
        """
        return self._is_reset_password

    @is_reset_password.setter
    def is_reset_password(self, is_reset_password):
        """
        Sets the is_reset_password of this UpdateOAuth2ClientCredentialDetails.
        Indicate if the password to be reset or not in the update.


        :param is_reset_password: The is_reset_password of this UpdateOAuth2ClientCredentialDetails.
        :type: bool
        """
        self._is_reset_password = is_reset_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
