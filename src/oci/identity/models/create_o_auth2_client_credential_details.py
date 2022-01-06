# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOAuth2ClientCredentialDetails(object):
    """
    CreateOAuth2ClientCredentialDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOAuth2ClientCredentialDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateOAuth2ClientCredentialDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateOAuth2ClientCredentialDetails.
        :type description: str

        :param scopes:
            The value to assign to the scopes property of this CreateOAuth2ClientCredentialDetails.
        :type scopes: list[oci.identity.models.FullyQualifiedScope]

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'scopes': 'list[FullyQualifiedScope]'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'scopes': 'scopes'
        }

        self._name = None
        self._description = None
        self._scopes = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateOAuth2ClientCredentialDetails.
        Name of the oauth credential to help user differentiate them.


        :return: The name of this CreateOAuth2ClientCredentialDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateOAuth2ClientCredentialDetails.
        Name of the oauth credential to help user differentiate them.


        :param name: The name of this CreateOAuth2ClientCredentialDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateOAuth2ClientCredentialDetails.
        Description of the oauth credential to help user differentiate them.


        :return: The description of this CreateOAuth2ClientCredentialDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateOAuth2ClientCredentialDetails.
        Description of the oauth credential to help user differentiate them.


        :param description: The description of this CreateOAuth2ClientCredentialDetails.
        :type: str
        """
        self._description = description

    @property
    def scopes(self):
        """
        **[Required]** Gets the scopes of this CreateOAuth2ClientCredentialDetails.
        Allowed scopes for the given oauth credential.


        :return: The scopes of this CreateOAuth2ClientCredentialDetails.
        :rtype: list[oci.identity.models.FullyQualifiedScope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this CreateOAuth2ClientCredentialDetails.
        Allowed scopes for the given oauth credential.


        :param scopes: The scopes of this CreateOAuth2ClientCredentialDetails.
        :type: list[oci.identity.models.FullyQualifiedScope]
        """
        self._scopes = scopes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
