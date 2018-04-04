# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .security_token_signer import X509FederationClientBasedSecurityTokenSigner
from ..certificate_retriever import UrlBasedCertificateRetriever
from ..session_key_supplier import SessionKeySupplier
from ..federation_client import X509FederationClient
from .. import auth_utils

import oci.regions
import requests


class InstancePrincipalsSecurityTokenSigner(X509FederationClientBasedSecurityTokenSigner):
    """
    A SecurityTokenSigner which uses a security token for an instance principal.  This signer can also
    refresh its token as needed.

    This signer is self-sufficient in that its internals know how to source the required information to request and use
    the token:

    * Using the metadata endpoint for the instance (http://169.254.169.254/opc/v1) we can discover the region the instance is in, its leaf certificate and any intermediate certificates (for requesting the token) and the tenancy (as) that is in the leaf certificate.
    * The signer leverages X509FederationClient so it can refresh the security token and also get the private key needed to sign requests (via the client's session_key_supplier)

    This signer can be used as follows:

    .. code-block:: python

        import oci

        signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
        identity_client = oci.identity.IdentityClient(config={}, signer=signer)
        regions = identity_client.list_regions()

    :param str federation_endpoint (optional):
        Users of this class can specify an explicit federation_endpoint, representing the Auth Service endpoint from which to retrieve a security token. If it is not
        provided then we will construct an endpoint based on the region we read from the metadata endpoint for the instance

    :param federation_client_cert_bundle_verify (optional):
        If we need a specific cert bundle in order to perform verification against the federation endpoint, this parameter is the path to that bundle. Alternatively,
        False can be passed to disable verification.
    :type federation_client_cert_bundle_verify: str or Boolean
    """

    METADATA_URL_BASE = 'http://169.254.169.254/opc/v1'
    GET_REGION_URL = '{}/instance/region'.format(METADATA_URL_BASE)
    LEAF_CERTIFICATE_URL = '{}/identity/cert.pem'.format(METADATA_URL_BASE)
    LEAF_CERTIFICATE_PRIVATE_KEY_URL = '{}/identity/key.pem'.format(METADATA_URL_BASE)
    INTERMEDIATE_CERTIFICATE_URL = '{}/identity/intermediate.pem'.format(METADATA_URL_BASE)

    def __init__(self, **kwargs):
        self.leaf_certificate_retriever = UrlBasedCertificateRetriever(certificate_url=self.LEAF_CERTIFICATE_URL, private_key_url=self.LEAF_CERTIFICATE_PRIVATE_KEY_URL)
        self.intermediate_certificate_retriever = UrlBasedCertificateRetriever(certificate_url=self.INTERMEDIATE_CERTIFICATE_URL)
        self.session_key_supplier = SessionKeySupplier()
        self.tenancy_id = auth_utils.get_tenancy_id_from_certificate(self.leaf_certificate_retriever.get_certificate_as_certificate())
        self.initialize_and_return_region()

        if 'federation_endpoint' in kwargs and kwargs['federation_endpoint']:
            federation_endpoint = kwargs['federation_endpoint']
        else:
            federation_endpoint = '{}/v1/x509'.format(oci.regions.endpoint_for('auth', self.region))

        federation_client = X509FederationClient(
            federation_endpoint=federation_endpoint,
            tenancy_id=self.tenancy_id,
            session_key_supplier=self.session_key_supplier,
            leaf_certificate_retriever=self.leaf_certificate_retriever,
            intermediate_certificate_retrievers=[self.intermediate_certificate_retriever],
            cert_bundle_verify=kwargs.get('federation_client_cert_bundle_verify', None)
        )

        super(InstancePrincipalsSecurityTokenSigner, self).__init__(federation_client)

    def initialize_and_return_region(self):
        if hasattr(self, 'region'):
            return self.region

        response = requests.get(self.GET_REGION_URL)
        region_raw = response.text.strip().lower()

        # The region can be something like "phx" but internally we expect "us-phoenix-1", "us-ashburn-1" etc.
        if region_raw in oci.regions.REGIONS_SHORT_NAMES:
            self.region = oci.regions.REGIONS_SHORT_NAMES[region_raw]
        else:
            self.region = region_raw

        return self.region
