# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateScopedAccessTokenDetails(object):
    """
    GenerateScopedAccessTokenDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateScopedAccessTokenDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scope:
            The value to assign to the scope property of this GenerateScopedAccessTokenDetails.
        :type scope: str

        :param public_key:
            The value to assign to the public_key property of this GenerateScopedAccessTokenDetails.
        :type public_key: str

        """
        self.swagger_types = {
            'scope': 'str',
            'public_key': 'str'
        }

        self.attribute_map = {
            'scope': 'scope',
            'public_key': 'publicKey'
        }

        self._scope = None
        self._public_key = None

    @property
    def scope(self):
        """
        **[Required]** Gets the scope of this GenerateScopedAccessTokenDetails.
        Scope definition for the scoped access token


        :return: The scope of this GenerateScopedAccessTokenDetails.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this GenerateScopedAccessTokenDetails.
        Scope definition for the scoped access token


        :param scope: The scope of this GenerateScopedAccessTokenDetails.
        :type: str
        """
        self._scope = scope

    @property
    def public_key(self):
        """
        **[Required]** Gets the public_key of this GenerateScopedAccessTokenDetails.
        A temporary public key, owned by the service. The service also owns the corresponding private key. This public
        key will by put inside the security token by the auth service after successful validation of the certificate.


        :return: The public_key of this GenerateScopedAccessTokenDetails.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this GenerateScopedAccessTokenDetails.
        A temporary public key, owned by the service. The service also owns the corresponding private key. This public
        key will by put inside the security token by the auth service after successful validation of the certificate.


        :param public_key: The public_key of this GenerateScopedAccessTokenDetails.
        :type: str
        """
        self._public_key = public_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
