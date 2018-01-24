# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from . import auth_utils
from .security_token_container import SecurityTokenContainer
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from OpenSSL import crypto

import oci.signer
import requests
import threading


class X509FederationClient(object):
    REQUIRED_INIT_KWARGS = [
        'federation_endpoint',
        'tenancy_id',
        'session_key_supplier',
        'leaf_certificate_retriever'
    ]

    def __init__(self, **kwargs):
        """
        A client which can be used to retrieve a token from Auth Service. It needs the following supplied to it:

            - The endpoint for Auth Service
            - Our tenancy OCID
            - A session key supplier so that we can send its public key as part of the token request. The private key
            in the session key supplier should be used to sign all requests made with the token
            - The certificate (via leaf_certificate_retriever) which will be used to sign the requests to Auth Service.

        Optionally, intermediate certificates (if present) can be supplied as part of the request to Auth Service.

        The client has knowledge of its last requested token and can re-request the token if it is expired (otherwise
        it will vend the last requested token if it is not expired).

        :param str federation_endpoint:
            The Auth Service endpoint from which to retrieve the token.

        :param str tenancy_id:
            The OCID of the tenancy whose resources will be interacted with by users of the token.

        :param SessionKeySupplier session_key_supplier:
            A SessionKeySupplier that can vend a public and private key. The public key will be sent as part of the token
            request and the private key should be used to sign all requests made with the token vended by this client.

        :param CertificateRetriever leaf_certificate_retriever:
            The certificate which will be used to sign requests to Auth Service.

        :param list[CertificateRetriever] intermediate_certificate_retrievers (optional):
            A list of retrievers which can be used to fetch intermediate certificates which can be sent as part of the Auth Service request. This is an optional parameter

        :param cert_bundle_verify (optional):
            If we need a specific cert bundle in order to perform verification against the federation endpoint, this parameter is the path to that bundle. Alternatively,
            False can be passed to disable verification.
        :type cert_bundle_verify: str or Boolean
        """

        kwarg_keys = kwargs.keys()
        missing_keys = []

        for required in self.REQUIRED_INIT_KWARGS:
            if required not in kwarg_keys:
                missing_keys.append(required)
            elif not kwargs[required]:
                missing_keys.append(required)

        if missing_keys:
            raise TypeError('The following required arguments were not provided: {}'.format(', '.join(missing_keys)))

        self.federation_endpoint = kwargs['federation_endpoint']
        self.tenancy_id = kwargs['tenancy_id']
        self.session_key_supplier = kwargs['session_key_supplier']
        self.leaf_certificate_retriever = kwargs['leaf_certificate_retriever']

        if 'intermediate_certificate_retrievers' in kwargs and kwargs['intermediate_certificate_retrievers']:
            self.intermediate_certificate_retrievers = kwargs['intermediate_certificate_retrievers']
        else:
            self.intermediate_certificate_retrievers = []

        self.cert_bundle_verify = kwargs.get('cert_bundle_verify', None)
        self._refresh_lock = threading.Lock()

    def refresh_security_token(self):
        return self._refresh_security_token_inner()

    def get_security_token(self):
        if hasattr(self, 'security_token'):
            if self.security_token.valid():
                return self.security_token.security_token

        return self._refresh_security_token_inner()

    def _refresh_security_token_inner(self):
        self._refresh_lock.acquire()
        try:
            self.session_key_supplier.refresh()
            self.leaf_certificate_retriever.refresh()

            updated_tenancy_id = auth_utils.get_tenancy_id_from_certificate(self.leaf_certificate_retriever.get_certificate_as_certificate())
            if updated_tenancy_id != self.tenancy_id:
                raise RuntimeError('Unexpected update of tenancy OCID in the leaf certificate. Previous tenancy: {}, Updated: {}'.format(self.tenancy_id, updated_tenancy_id))

            for retriever in self.intermediate_certificate_retrievers:
                retriever.refresh()

            self._get_security_token_from_auth_service()
            return self.security_token.security_token
        finally:
            self._refresh_lock.release()

    def _get_security_token_from_auth_service(self):
        request_payload = {
            'certificate': auth_utils.sanitize_certificate_string(self.leaf_certificate_retriever.get_certificate_raw()),
            'publicKey': auth_utils.sanitize_certificate_string(self.session_key_supplier.get_key_pair()['public'].public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo))
        }

        if self.intermediate_certificate_retrievers:
            retrieved_certs = []
            for retriever in self.intermediate_certificate_retrievers:
                retrieved_certs.append(auth_utils.sanitize_certificate_string(retriever.get_certificate_raw()))

            request_payload['intermediateCertificates'] = retrieved_certs

        fingerprint = crypto.load_certificate(crypto.FILETYPE_PEM, self.leaf_certificate_retriever.get_certificate_raw()).digest('sha1').decode('utf-8')
        signer = AuthTokenRequestSigner(self.tenancy_id, fingerprint, self.leaf_certificate_retriever)

        if self.cert_bundle_verify:
            response = requests.post(self.federation_endpoint, json=request_payload, auth=signer, verify=self.cert_bundle_verify)
        else:
            response = requests.post(self.federation_endpoint, json=request_payload, auth=signer)
        self.security_token = SecurityTokenContainer(self.session_key_supplier, response.json()['token'])


class AuthTokenRequestSigner(oci.signer.AbstractBaseSigner):
    """
    A signer intended for X509FederationClient's use to request a token from Auth Service. Not intended for general use.


    """

    def __init__(self, tenancy_id, fingerprint, private_key_certificate_retriever):
        self.api_key = '{}/fed-x509/{}'.format(tenancy_id, fingerprint)
        self.private_key_certificate_retriever = private_key_certificate_retriever

        generic_headers = ["date", "(request-target)"]
        body_headers = ["content-length", "content-type", "x-content-sha256"]
        self.create_signers(self.api_key, self.private_key_certificate_retriever.get_private_key(), generic_headers, body_headers)
