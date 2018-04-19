# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .update_identity_provider_details import UpdateIdentityProviderDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSaml2IdentityProviderDetails(UpdateIdentityProviderDetails):
    """
    UpdateSaml2IdentityProviderDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSaml2IdentityProviderDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.identity.models.UpdateSaml2IdentityProviderDetails.protocol` attribute
        of this class is ``SAML2`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this UpdateSaml2IdentityProviderDetails.
            Allowed values for this property are: "SAML2"
        :type protocol: str

        :param description:
            The value to assign to the description property of this UpdateSaml2IdentityProviderDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSaml2IdentityProviderDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSaml2IdentityProviderDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param metadata_url:
            The value to assign to the metadata_url property of this UpdateSaml2IdentityProviderDetails.
        :type metadata_url: str

        :param metadata:
            The value to assign to the metadata property of this UpdateSaml2IdentityProviderDetails.
        :type metadata: str

        """
        self.swagger_types = {
            'protocol': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'metadata_url': 'str',
            'metadata': 'str'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'metadata_url': 'metadataUrl',
            'metadata': 'metadata'
        }

        self._protocol = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
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
