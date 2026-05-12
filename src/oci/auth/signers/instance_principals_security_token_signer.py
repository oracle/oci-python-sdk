# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .security_token_signer import X509FederationClientBasedSecurityTokenSigner
from ..certificate_retriever import UrlBasedCertificateRetriever, INSTANCE_METADATA_URL_CERTIFICATE_RETRIEVER_RETRY_STRATEGY
from ..session_key_supplier import SessionKeySupplier
from ..federation_client import X509FederationClient
from .. import auth_utils
from oci._vendor import requests
from oci._vendor.requests.exceptions import HTTPError
from oci._vendor.requests.exceptions import ConnectTimeout
from oci._vendor.requests.exceptions import ConnectionError as RequestsConnectionError
from oci._vendor.requests.exceptions import Timeout as RequestsTimeout

import oci.regions
import os
import logging
import socket


class InstancePrincipalsSecurityTokenSigner(X509FederationClientBasedSecurityTokenSigner):
    """
    A SecurityTokenSigner which uses a security token for an instance principal.  This signer can also
    refresh its token as needed.

    This signer is self-sufficient in that its internals know how to source the required information to request and use
    the token:

    * Using the metadata endpoint for the instance (http://169.254.169.254/opc/v2) we can discover the region the instance is in, its leaf certificate and any intermediate certificates (for requesting the token) and the tenancy (as) that is in the leaf certificate.
    * You can override the metadata endpoint by overriding the environment variable OCI_METADATA_BASE_URL with an endpoint of your choice
    * If OCI_METADATA_BASE_URL is not set, signer resolves IMDS endpoint candidates in this order: IPv4 default when IPv4 route is present; otherwise IPv6 IMDS first and IPv4 IMDS fallback.
    * The signer leverages X509FederationClient so it can refresh the security token and also get the private key needed to sign requests (via the client's session_key_supplier)

    This signer can be used as follows:

    .. code-block:: python

        import oci

        signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
        identity_client = oci.identity.IdentityClient(config={}, signer=signer)
        regions = identity_client.list_regions()

    :param str federation_endpoint: (optional)
        Users of this class can specify an explicit federation_endpoint, representing the Auth Service endpoint from which to retrieve a security token. If it is not
        provided then we will construct an endpoint based on the region we read from the metadata endpoint for the instance

    :param federation_client_cert_bundle_verify: (optional)
        If we need a specific cert bundle in order to perform verification against the federation endpoint, this parameter is the path to that bundle. Alternatively,
        False can be passed to disable verification.
    :type federation_client_cert_bundle_verify: str or Boolean

    :param obj federation_client_retry_strategy: (optional):
        A retry strategy to apply to calls made by the X509FederationClient used by this class. This should be one of the strategies available in
        the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_FEDERATION_CLIENT_RETRY_STRATEGY` is also available and
        will be used by the X509FederationClient if no explicit retry strategy is specified.

        The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

        To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

    :param bool log_requests: (optional)
        log_request if set to True, will log the request url and response data when retrieving
        the certificate & corresponding private key (if there is one defined for this retriever) from UrlBasedCertificateRetriever,
        region, federation endpoint, and the response for receiving the token from the federation endpoint
    """
    METADATA_URL_BASE_ENV_VAR = 'OCI_METADATA_BASE_URL'
    DEFAULT_METADATA_URL_BASE = 'http://169.254.169.254/opc/v2'
    # IPv6 literal hosts in URLs must be enclosed in square brackets (RFC 3986).
    DEFAULT_METADATA_URL_BASE_IPV6 = 'http://[fd00:c1::a9fe:a9fe]/opc/v2'
    METADATA_URL_BASE = DEFAULT_METADATA_URL_BASE
    GET_REGION_URL = '{}/instance/region'.format(DEFAULT_METADATA_URL_BASE)
    LEAF_CERTIFICATE_URL = '{}/identity/cert.pem'.format(DEFAULT_METADATA_URL_BASE)
    LEAF_CERTIFICATE_PRIVATE_KEY_URL = '{}/identity/key.pem'.format(DEFAULT_METADATA_URL_BASE)
    INTERMEDIATE_CERTIFICATE_URL = '{}/identity/intermediate.pem'.format(DEFAULT_METADATA_URL_BASE)
    METADATA_AUTH_HEADERS = {'Authorization': 'Bearer Oracle'}
    INSTANCE_PRINCIPAL_USAGE_HINT = (
        "Instance principals authentication can only be used on OCI compute instances. "
        "Please confirm this code is running on an OCI compute instance. "
        "See https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm for more info."
    )

    IMDS_IPV4_PROBE_HOST = '169.254.169.254'
    IMDS_IPV4_PROBE_PORT = 80
    IMDS_IPV4_PROBE_TIMEOUT_SECONDS = 0.2

    def _get_logger(self):
        # Some helper methods are unit-tested via __new__() without running __init__().
        # Fall back to a module logger if self.logger is not set.
        return getattr(self, 'logger', logging.getLogger(__name__))

    def _append_instance_principal_usage_hint(self, exception):
        # Keep existing exception type for compatibility while appending a stable,
        # non-sensitive usage hint that helps identify instance principal context.
        if not exception.args:
            exception.args = ('',)
        if self.INSTANCE_PRINCIPAL_USAGE_HINT not in exception.args:
            exception.args = exception.args + (self.INSTANCE_PRINCIPAL_USAGE_HINT,)
        return exception

    def _close_retriever_session_safely(self, certificate_retriever):
        logger = self._get_logger()
        if certificate_retriever is None:
            return

        requests_session = getattr(certificate_retriever, 'requests_session', None)
        if requests_session is None:
            return

        try:
            requests_session.close()
        except Exception as close_error:
            logger.debug(
                "Failed to close UrlBasedCertificateRetriever session due to error type: %s",
                type(close_error).__name__
            )

    @classmethod
    def _build_metadata_service_urls(cls, metadata_base_url):
        return {
            'metadata_base_url': metadata_base_url,
            'get_region_url': '{}/instance/region'.format(metadata_base_url),
            'leaf_certificate_url': '{}/identity/cert.pem'.format(metadata_base_url),
            'leaf_certificate_private_key_url': '{}/identity/key.pem'.format(metadata_base_url),
            'intermediate_certificate_url': '{}/identity/intermediate.pem'.format(metadata_base_url)
        }

    def _set_metadata_service_urls(self, metadata_base_url):
        """
        Store resolved IMDS URLs on this signer instance.

        This intentionally sets instance attributes (not class-level state), so
        multiple signer instances can resolve and retain endpoint state independently.
        """
        metadata_service_urls = self._build_metadata_service_urls(metadata_base_url)
        self.METADATA_URL_BASE = metadata_service_urls['metadata_base_url']
        self.GET_REGION_URL = metadata_service_urls['get_region_url']
        self.LEAF_CERTIFICATE_URL = metadata_service_urls['leaf_certificate_url']
        self.LEAF_CERTIFICATE_PRIVATE_KEY_URL = metadata_service_urls['leaf_certificate_private_key_url']
        self.INTERMEDIATE_CERTIFICATE_URL = metadata_service_urls['intermediate_certificate_url']

    def _get_env_override_metadata_base_url(self):
        """
        Return explicit OCI_METADATA_BASE_URL override if present.
        Whitespace-only values are treated as unset.
        """
        logger = self._get_logger()
        env_override_metadata_base_url = os.environ.get(self.METADATA_URL_BASE_ENV_VAR)
        if env_override_metadata_base_url is None:
            return None

        env_override_metadata_base_url = env_override_metadata_base_url.strip()
        if not env_override_metadata_base_url:
            logger.debug("%s is whitespace-only and will be treated as unset", self.METADATA_URL_BASE_ENV_VAR)
        return env_override_metadata_base_url if env_override_metadata_base_url else None

    def _has_ipv4_route_for_imds(self):
        logger = self._get_logger()
        ipv4_probe_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            ipv4_probe_socket.settimeout(self.IMDS_IPV4_PROBE_TIMEOUT_SECONDS)
            ipv4_probe_socket.connect((self.IMDS_IPV4_PROBE_HOST, self.IMDS_IPV4_PROBE_PORT))
            return True
        except OSError as e:
            logger.debug(
                "IPv4 IMDS route probe failed with error type: %s, errno: %s",
                type(e).__name__,
                getattr(e, 'errno', None)
            )
            return False
        finally:
            ipv4_probe_socket.close()

    def _get_metadata_base_url_candidates(self):
        """
        Candidate precedence for IMDS endpoint resolution:
        1) Explicit OCI_METADATA_BASE_URL override.
        2) IPv4 default if IPv4 route probe succeeds.
        3) IPv6 IMDS first, then IPv4 fallback when IPv4 route probe fails.
        """
        env_override_metadata_base_url = self._get_env_override_metadata_base_url()
        if env_override_metadata_base_url:
            return [env_override_metadata_base_url]

        if self._has_ipv4_route_for_imds():
            return [self.DEFAULT_METADATA_URL_BASE]

        return [self.DEFAULT_METADATA_URL_BASE_IPV6, self.DEFAULT_METADATA_URL_BASE]

    def _initialize_certificate_retrievers_from_imds_candidates(self, log_requests=False):
        logger = self._get_logger()
        metadata_base_url_candidates = self._get_metadata_base_url_candidates()
        has_explicit_metadata_base_url_override = self._get_env_override_metadata_base_url() is not None
        last_connection_exception = None

        for metadata_base_url in metadata_base_url_candidates:
            metadata_service_urls = self._build_metadata_service_urls(metadata_base_url)
            leaf_certificate_retriever = None
            intermediate_certificate_retriever = None
            try:
                leaf_certificate_retriever = UrlBasedCertificateRetriever(
                    certificate_url=metadata_service_urls['leaf_certificate_url'],
                    private_key_url=metadata_service_urls['leaf_certificate_private_key_url'],
                    retry_strategy=self.retry_strategy,
                    headers=self.METADATA_AUTH_HEADERS,
                    log_requests=log_requests)

                intermediate_certificate_retriever = UrlBasedCertificateRetriever(
                    certificate_url=metadata_service_urls['intermediate_certificate_url'],
                    retry_strategy=self.retry_strategy,
                    headers=self.METADATA_AUTH_HEADERS)

                self._set_metadata_service_urls(metadata_base_url)
                self.leaf_certificate_retriever = leaf_certificate_retriever
                self.intermediate_certificate_retriever = intermediate_certificate_retriever
                logger.debug("Using IMDS metadata base URL: %s", self.METADATA_URL_BASE)
                return
            except (RequestsConnectionError, RequestsTimeout, ConnectTimeout) as e:
                last_connection_exception = e
                self._close_retriever_session_safely(leaf_certificate_retriever)
                self._close_retriever_session_safely(intermediate_certificate_retriever)
                logger.debug(
                    "Failed to initialize IMDS certificate retrievers from %s due to error type: %s",
                    metadata_base_url,
                    type(e).__name__
                )

                if has_explicit_metadata_base_url_override:
                    raise self._append_instance_principal_usage_hint(e)
            except Exception as unexpected_error:
                self._close_retriever_session_safely(leaf_certificate_retriever)
                self._close_retriever_session_safely(intermediate_certificate_retriever)
                logger.debug(
                    "Unexpected IMDS retriever initialization failure for endpoint %s due to error type: %s",
                    metadata_base_url,
                    type(unexpected_error).__name__
                )
                raise

        if last_connection_exception is not None:
            raise self._append_instance_principal_usage_hint(last_connection_exception)

        raise RuntimeError("Unable to initialize IMDS certificate retrievers for all candidate endpoints")

    def __init__(self, **kwargs):
        self.logger = logging.getLogger("{}.{}".format(__name__, id(self)))
        self.logger.addHandler(logging.NullHandler())
        if kwargs.get('log_requests'):
            self.logger.disabled = False
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.disabled = True

        # If user sends in custom retry strategy use that, else use INSTANCE_METADATA_URL_CERTIFICATE_RETRIEVER_RETRY_STRATEGY
        if kwargs.get('retry_strategy'):
            self.retry_strategy = kwargs['retry_strategy']
        else:
            self.retry_strategy = INSTANCE_METADATA_URL_CERTIFICATE_RETRIEVER_RETRY_STRATEGY

        try:
            self._initialize_certificate_retrievers_from_imds_candidates(log_requests=kwargs.get('log_requests'))
        except (HTTPError, ConnectTimeout, RequestsConnectionError, RequestsTimeout, oci.exceptions.ServiceError) as e:
            raise self._append_instance_principal_usage_hint(e)
        self.session_key_supplier = SessionKeySupplier()
        self.tenancy_id = auth_utils.get_tenancy_id_from_certificate(self.leaf_certificate_retriever.get_certificate_as_certificate())
        self.initialize_and_return_region()

        if 'federation_endpoint' in kwargs and kwargs['federation_endpoint']:
            federation_endpoint = kwargs['federation_endpoint']
        else:
            federation_endpoint = '{}/v1/x509'.format(oci.regions.endpoint_for('auth', self.region))

        self.logger.debug("federation endpoint is set to : %s " % (federation_endpoint))

        federation_client = X509FederationClient(
            federation_endpoint=federation_endpoint,
            tenancy_id=self.tenancy_id,
            session_key_supplier=self.session_key_supplier,
            leaf_certificate_retriever=self.leaf_certificate_retriever,
            intermediate_certificate_retrievers=[self.intermediate_certificate_retriever],
            cert_bundle_verify=kwargs.get('federation_client_cert_bundle_verify', None),
            retry_strategy=kwargs.get('federation_client_retry_strategy', None),
            purpose=kwargs.get('purpose', None),
            log_requests=kwargs.get('log_requests')
        )
        if 'generic_headers' in kwargs:
            generic_headers = kwargs['generic_headers']
            super(InstancePrincipalsSecurityTokenSigner, self).__init__(federation_client=federation_client, generic_headers=generic_headers)
        else:
            super(InstancePrincipalsSecurityTokenSigner, self).__init__(federation_client)

    def initialize_and_return_region(self):
        if hasattr(self, 'region'):
            return self.region

        if self.retry_strategy:
            self.retry_strategy.make_retrying_call(self._set_region_from_imds)
        else:
            self._set_region_from_imds()

        self.logger.debug(f"Region is set to: {self.region}")
        return self.region

    def _set_region_from_imds(self):
        self.logger.debug(f"Requesting region information from IMDS: {self.GET_REGION_URL}")
        response = requests.get(self.GET_REGION_URL, timeout=(10, 60), headers=self.METADATA_AUTH_HEADERS)

        try:
            response.raise_for_status()
        except HTTPError as e:
            raise oci.exceptions.ServiceError(e.response.status_code, e.errno, e.response.headers, str(e))

        region_raw = response.text.strip().lower()

        # The region can be something like "phx" but internally we expect "us-phoenix-1", "us-ashburn-1" etc.
        if region_raw in oci.regions.REGIONS_SHORT_NAMES:
            self.region = oci.regions.REGIONS_SHORT_NAMES[region_raw]
        else:
            self.region = region_raw
