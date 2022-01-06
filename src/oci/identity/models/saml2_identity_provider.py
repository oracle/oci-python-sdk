# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .identity_provider import IdentityProvider
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Saml2IdentityProvider(IdentityProvider):
    """
    A special type of :class:`IdentityProvider` that
    supports the SAML 2.0 protocol. For more information, see
    `Identity Providers and Federation`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/federation.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Saml2IdentityProvider object with values from keyword arguments. The default value of the :py:attr:`~oci.identity.models.Saml2IdentityProvider.protocol` attribute
        of this class is ``SAML2`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

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

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Saml2IdentityProvider.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Saml2IdentityProvider.
        :type defined_tags: dict(str, dict(str, object))

        :param metadata_url:
            The value to assign to the metadata_url property of this Saml2IdentityProvider.
        :type metadata_url: str

        :param metadata:
            The value to assign to the metadata property of this Saml2IdentityProvider.
        :type metadata: str

        :param signing_certificate:
            The value to assign to the signing_certificate property of this Saml2IdentityProvider.
        :type signing_certificate: str

        :param redirect_url:
            The value to assign to the redirect_url property of this Saml2IdentityProvider.
        :type redirect_url: str

        :param freeform_attributes:
            The value to assign to the freeform_attributes property of this Saml2IdentityProvider.
        :type freeform_attributes: dict(str, str)

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
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'metadata_url': 'str',
            'metadata': 'str',
            'signing_certificate': 'str',
            'redirect_url': 'str',
            'freeform_attributes': 'dict(str, str)'
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
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'metadata_url': 'metadataUrl',
            'metadata': 'metadata',
            'signing_certificate': 'signingCertificate',
            'redirect_url': 'redirectUrl',
            'freeform_attributes': 'freeformAttributes'
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
        self._freeform_tags = None
        self._defined_tags = None
        self._metadata_url = None
        self._metadata = None
        self._signing_certificate = None
        self._redirect_url = None
        self._freeform_attributes = None
        self._protocol = 'SAML2'

    @property
    def metadata_url(self):
        """
        **[Required]** Gets the metadata_url of this Saml2IdentityProvider.
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
    def metadata(self):
        """
        Gets the metadata of this Saml2IdentityProvider.
        The XML that contains the information required for federating Identity with SAML2 Identity Provider.


        :return: The metadata of this Saml2IdentityProvider.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Saml2IdentityProvider.
        The XML that contains the information required for federating Identity with SAML2 Identity Provider.


        :param metadata: The metadata of this Saml2IdentityProvider.
        :type: str
        """
        self._metadata = metadata

    @property
    def signing_certificate(self):
        """
        **[Required]** Gets the signing_certificate of this Saml2IdentityProvider.
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
        **[Required]** Gets the redirect_url of this Saml2IdentityProvider.
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

    @property
    def freeform_attributes(self):
        """
        Gets the freeform_attributes of this Saml2IdentityProvider.
        Extra name value pairs associated with this identity provider.
        Example: `{\"clientId\": \"app_sf3kdjf3\"}`


        :return: The freeform_attributes of this Saml2IdentityProvider.
        :rtype: dict(str, str)
        """
        return self._freeform_attributes

    @freeform_attributes.setter
    def freeform_attributes(self, freeform_attributes):
        """
        Sets the freeform_attributes of this Saml2IdentityProvider.
        Extra name value pairs associated with this identity provider.
        Example: `{\"clientId\": \"app_sf3kdjf3\"}`


        :param freeform_attributes: The freeform_attributes of this Saml2IdentityProvider.
        :type: dict(str, str)
        """
        self._freeform_attributes = freeform_attributes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
