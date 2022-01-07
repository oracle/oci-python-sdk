# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class X509FederationRequest(object):
    """
    X509FederationRequest model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new X509FederationRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate:
            The value to assign to the certificate property of this X509FederationRequest.
        :type certificate: str

        :param public_key:
            The value to assign to the public_key property of this X509FederationRequest.
        :type public_key: str

        :param intermediate_certificates:
            The value to assign to the intermediate_certificates property of this X509FederationRequest.
        :type intermediate_certificates: list[str]

        """
        self.swagger_types = {
            'certificate': 'str',
            'public_key': 'str',
            'intermediate_certificates': 'list[str]'
        }

        self.attribute_map = {
            'certificate': 'certificate',
            'public_key': 'publicKey',
            'intermediate_certificates': 'intermediateCertificates'
        }

        self._certificate = None
        self._public_key = None
        self._intermediate_certificates = None

    @property
    def certificate(self):
        """
        **[Required]** Gets the certificate of this X509FederationRequest.
        The x509 certificate of the service instance, issued by his CA.


        :return: The certificate of this X509FederationRequest.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this X509FederationRequest.
        The x509 certificate of the service instance, issued by his CA.


        :param certificate: The certificate of this X509FederationRequest.
        :type: str
        """
        self._certificate = certificate

    @property
    def public_key(self):
        """
        **[Required]** Gets the public_key of this X509FederationRequest.
        A temporary public key, owned by the service. The service also owns the corresponding private key. This public
        key will by put inside the security token by the auth service after successful validation of the certificate.


        :return: The public_key of this X509FederationRequest.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this X509FederationRequest.
        A temporary public key, owned by the service. The service also owns the corresponding private key. This public
        key will by put inside the security token by the auth service after successful validation of the certificate.


        :param public_key: The public_key of this X509FederationRequest.
        :type: str
        """
        self._public_key = public_key

    @property
    def intermediate_certificates(self):
        """
        Gets the intermediate_certificates of this X509FederationRequest.
        An array of intermediate certificates to form the chain from the leaf certificate to the root CA. If auth
        service already has the intermediate certificate(s), then this is not required.


        :return: The intermediate_certificates of this X509FederationRequest.
        :rtype: list[str]
        """
        return self._intermediate_certificates

    @intermediate_certificates.setter
    def intermediate_certificates(self, intermediate_certificates):
        """
        Sets the intermediate_certificates of this X509FederationRequest.
        An array of intermediate certificates to form the chain from the leaf certificate to the root CA. If auth
        service already has the intermediate certificate(s), then this is not required.


        :param intermediate_certificates: The intermediate_certificates of this X509FederationRequest.
        :type: list[str]
        """
        self._intermediate_certificates = intermediate_certificates

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
