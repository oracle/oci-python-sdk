# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .update_identity_provider_details import UpdateIdentityProviderDetails
from ...util import formatted_flat_dict


class UpdateSaml2IdentityProviderDetails(UpdateIdentityProviderDetails):

    def __init__(self):

        self.swagger_types = {
            'protocol': 'str',
            'description': 'str',
            'metadata_url': 'str',
            'metadata': 'str'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'description': 'description',
            'metadata_url': 'metadataUrl',
            'metadata': 'metadata'
        }

        self._protocol = None
        self._description = None
        self._metadata_url = None
        self._metadata = None
        self._protocol = 'SAML2'

    @property
    def metadata_url(self):
        """
        Gets the metadata_url of this UpdateSaml2IdentityProviderDetails.
        The URL for retrieving the identity provider's metadata,
        which contains information required for federating.


        :return: The metadata_url of this UpdateSaml2IdentityProviderDetails.
        :rtype: str
        """
        return self._metadata_url

    @metadata_url.setter
    def metadata_url(self, metadata_url):
        """
        Sets the metadata_url of this UpdateSaml2IdentityProviderDetails.
        The URL for retrieving the identity provider's metadata,
        which contains information required for federating.


        :param metadata_url: The metadata_url of this UpdateSaml2IdentityProviderDetails.
        :type: str
        """
        self._metadata_url = metadata_url

    @property
    def metadata(self):
        """
        Gets the metadata of this UpdateSaml2IdentityProviderDetails.
        The XML that contains the information required for federating.


        :return: The metadata of this UpdateSaml2IdentityProviderDetails.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UpdateSaml2IdentityProviderDetails.
        The XML that contains the information required for federating.


        :param metadata: The metadata of this UpdateSaml2IdentityProviderDetails.
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
