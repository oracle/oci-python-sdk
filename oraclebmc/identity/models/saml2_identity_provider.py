# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .identity_provider import IdentityProvider
from ...util import formatted_flat_dict


class Saml2IdentityProvider(IdentityProvider):

    def __init__(self):

        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'product_type': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int',
            'protocol': 'str',
            'metadata_url': 'str',
            'signing_certificate': 'str',
            'redirect_url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'product_type': 'productType',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus',
            'protocol': 'protocol',
            'metadata_url': 'metadataUrl',
            'signing_certificate': 'signingCertificate',
            'redirect_url': 'redirectUrl'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._product_type = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None
        self._protocol = None
        self._metadata_url = None
        self._signing_certificate = None
        self._redirect_url = None
        self._protocol = 'SAML2'

    @property
    def metadata_url(self):
        """
        Gets the metadata_url of this Saml2IdentityProvider.
        The URL for retrieving the identity provider's metadata, which
        contains information required for federating.


        :return: The metadata_url of this Saml2IdentityProvider.
        :rtype: str
        """
        return self._metadata_url

    @metadata_url.setter
    def metadata_url(self, metadata_url):
        """
        Sets the metadata_url of this Saml2IdentityProvider.
        The URL for retrieving the identity provider's metadata, which
        contains information required for federating.


        :param metadata_url: The metadata_url of this Saml2IdentityProvider.
        :type: str
        """
        self._metadata_url = metadata_url

    @property
    def signing_certificate(self):
        """
        Gets the signing_certificate of this Saml2IdentityProvider.
        The identity provider's signing certificate used by the IAM Service
        to validate the SAML2 token.


        :return: The signing_certificate of this Saml2IdentityProvider.
        :rtype: str
        """
        return self._signing_certificate

    @signing_certificate.setter
    def signing_certificate(self, signing_certificate):
        """
        Sets the signing_certificate of this Saml2IdentityProvider.
        The identity provider's signing certificate used by the IAM Service
        to validate the SAML2 token.


        :param signing_certificate: The signing_certificate of this Saml2IdentityProvider.
        :type: str
        """
        self._signing_certificate = signing_certificate

    @property
    def redirect_url(self):
        """
        Gets the redirect_url of this Saml2IdentityProvider.
        The URL to redirect federated users to for authentication with the
        identity provider.


        :return: The redirect_url of this Saml2IdentityProvider.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """
        Sets the redirect_url of this Saml2IdentityProvider.
        The URL to redirect federated users to for authentication with the
        identity provider.


        :param redirect_url: The redirect_url of this Saml2IdentityProvider.
        :type: str
        """
        self._redirect_url = redirect_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
