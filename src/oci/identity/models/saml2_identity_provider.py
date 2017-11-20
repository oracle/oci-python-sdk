# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .identity_provider import IdentityProvider
from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Saml2IdentityProvider(IdentityProvider):

    def __init__(self, **kwargs):
        """
        Initializes a new Saml2IdentityProvider object with values from values from keyword arguments. The
        following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Saml2IdentityProvider.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Saml2IdentityProvider.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this Saml2IdentityProvider.
        :type name: str

        :param description:
            The value to assign to the description property of this Saml2IdentityProvider.
        :type description: str

        :param product_type:
            The value to assign to the product_type property of this Saml2IdentityProvider.
        :type product_type: str

        :param time_created:
            The value to assign to the time_created property of this Saml2IdentityProvider.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Saml2IdentityProvider.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this Saml2IdentityProvider.
        :type inactive_status: int

        :param protocol:
            The value to assign to the protocol property of this Saml2IdentityProvider.
        :type protocol: str

        :param metadata_url:
            The value to assign to the metadata_url property of this Saml2IdentityProvider.
        :type metadata_url: str

        :param signing_certificate:
            The value to assign to the signing_certificate property of this Saml2IdentityProvider.
        :type signing_certificate: str

        :param redirect_url:
            The value to assign to the redirect_url property of this Saml2IdentityProvider.
        :type redirect_url: str

        """
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
