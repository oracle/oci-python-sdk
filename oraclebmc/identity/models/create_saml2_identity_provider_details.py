# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .create_identity_provider_details import CreateIdentityProviderDetails
from ...util import formatted_flat_dict


class CreateSaml2IdentityProviderDetails(CreateIdentityProviderDetails):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'product_type': 'str',
            'protocol': 'str',
            'metadata_url': 'str',
            'metadata': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'product_type': 'productType',
            'protocol': 'protocol',
            'metadata_url': 'metadataUrl',
            'metadata': 'metadata'
        }

        self._compartment_id = None
        self._name = None
        self._description = None
        self._product_type = None
        self._protocol = None
        self._metadata_url = None
        self._metadata = None
        self._protocol = 'SAML2'

    @property
    def metadata_url(self):
        """
        Gets the metadata_url of this CreateSaml2IdentityProviderDetails.
        The URL for retrieving the identity provider's metadata,
        which contains information required for federating.


        :return: The metadata_url of this CreateSaml2IdentityProviderDetails.
        :rtype: str
        """
        return self._metadata_url

    @metadata_url.setter
    def metadata_url(self, metadata_url):
        """
        Sets the metadata_url of this CreateSaml2IdentityProviderDetails.
        The URL for retrieving the identity provider's metadata,
        which contains information required for federating.


        :param metadata_url: The metadata_url of this CreateSaml2IdentityProviderDetails.
        :type: str
        """
        self._metadata_url = metadata_url

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateSaml2IdentityProviderDetails.
        The XML that contains the information required for federating.


        :return: The metadata of this CreateSaml2IdentityProviderDetails.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateSaml2IdentityProviderDetails.
        The XML that contains the information required for federating.


        :param metadata: The metadata of this CreateSaml2IdentityProviderDetails.
        :type: str
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
