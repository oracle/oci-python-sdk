# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
OAuth Exchange Token Signer for OCI SDK

This module implements OAuth 2.0 token exchange authentication for Oracle Cloud Infrastructure.
It allows applications to exchange existing OCI authentication tokens for scoped OAuth tokens
that provide limited access to specific resources within a target compartment.

The OAuth Exchange Token Signer is particularly useful for:

1. **Cross-tenancy Access**: When workloads in one tenancy need limited access to resources
   in another tenancy through federated authentication.

2. **Least Privilege Access**: When applications need access to only specific OCI services
   or resources rather than full tenant-wide permissions.

3. **Service-to-Service Authentication**: When microservices need to authenticate with each
   other using scoped tokens rather than sharing broad credentials.

4. **Workload Identity**: When containerized workloads or functions need temporary, scoped
   access to OCI resources without storing long-term credentials.

Usage Pattern:
    # Create base authentication (instance principal, user principal, etc.)
    base_signer = InstancePrincipalsSecurityTokenSigner()

    # Exchange for scoped OAuth token
    oauth_signer = OauthExchangeTokenSigner(
        token_signer=base_signer,
        scope="monitoring_write_urn-ocid1.compartment...:instance",
        target_compartment="ocid1.compartment.region1..."
    )

    # Use with any OCI service client
    client = MonitoringClient(config, signer=oauth_signer)

The signer automatically handles token lifecycle including refresh and expiration.
"""

import json
import logging
import pprint
import threading
import time
import typing

from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

import oci
from oci._vendor import requests
from oci.auth import auth_utils
from oci.auth.certificate_retriever import INSTANCE_METADATA_URL_CERTIFICATE_RETRIEVER_RETRY_STRATEGY
from oci.auth.security_token_container import SecurityTokenContainer
from oci.auth.session_key_supplier import SessionKeySupplier

from oci.auth.signers import SecurityTokenSigner
from oci.auth.signers.security_token_signer import SECURITY_TOKEN_FORMAT_STRING
from oci.regions import REGION_IDENTIFIER_PROPERTY_NAME


class OauthExchangeTokenSigner(SecurityTokenSigner):
    """
    OAuth Exchange Token Signer for OCI SDK Authentication

    This signer implements OAuth 2.0 token exchange for secure authentication with Oracle Cloud Infrastructure.
    It exchanges an existing authentication token (from another signer) for a scoped OAuth token that provides
    access to specific OCI resources within a target compartment.

    Key Features:
    - Token Exchange: Converts an existing OCI token into a scoped OAuth token
    - Automatic Refresh: Handles token expiration and renewal automatically
    - Scoped Access: Restricts access to specific resources and compartments
    """

    # Token refresh threshold: refresh tokens that are older than 20 minutes
    # This provides a safety buffer before the actual token expiration
    TOKEN_STALENESS_IN_SECONDS = 20 * 60

    def __init__(self, token_signer, scope, target_compartment, **kwargs): # noqa
        """
        Initialize the OAuth Exchange Token Signer

        Args:
            token_signer: An existing OCI signer (e.g., InstancePrincipalsSecurityTokenSigner)
                         that will be used to authenticate the OAuth token exchange request
            scope (str): The OAuth scope string defining what resources this token can access
                        Format: "service_permission_urn-compartment_ocid:resource_type"
                        Example: "monitoring_write_urn-ocid1.compartment...:instance"
            target_compartment (str): The OCID of the compartment where resources will be accessed

        Keyword Args:
            oauth_token_endpoint (str, optional): Custom OAuth endpoint URL. If not provided,
                                                 will be auto-discovered from instance metadata
            log_requests (bool, optional): Enable debug logging for OAuth requests. Default: False
            cert_bundle_verify (str|bool, optional): Path to CA certificate bundle for SSL verification
                                                    or True/False to enable/disable verification
            generic_headers (list, optional): List of headers to include in request signatures
                                            Default: ["date", "(request-target)", "host"]

        Raises:
            ValueError: If required parameters (token_signer, scope, target_compartment) are missing
            oci.exceptions.ServiceError: If OAuth token exchange fails
            RuntimeError: If token response is malformed or endpoint discovery fails
        """
        # Validate required parameters
        self._validate_args(token_signer, scope, target_compartment)

        # Set up per-instance logging
        self._setup_logging(kwargs.get("log_requests"))

        # Store configuration parameters
        self._set_class_vars(token_signer, scope, target_compartment, kwargs.get("cert_bundle_verify"))

        # Determine or set the OAuth endpoint URL
        self._set_oauth_token_endpoint(kwargs.get("oauth_token_endpoint"))

        # Initialize thread synchronization
        self._initialize_locks()

        # Set up key management and token containers
        self._initialize_keys_and_suppliers()

        # Perform initial OAuth token exchange and setup
        self._generate_oauth_token_and_set_state()

        # Initialize the parent SecurityTokenSigner with our OAuth token
        self._initialize_parent(kwargs.get("generic_headers")) # noqa

    @staticmethod
    def _validate_args(token_signer, scope, target_compartment):
        if not token_signer or not scope or not target_compartment:
            raise ValueError("token_signer, scope, target_compartment are required")

    def _setup_logging(self, log_requests):
        self.logger = logging.getLogger(f"{__name__}.{id(self)}")
        self.logger.addHandler(logging.NullHandler())
        self.logger.disabled = True
        if log_requests:
            self.logger.disabled = False
            self.logger.setLevel(logging.DEBUG)

    def _set_class_vars(self, token_signer, scope, target_compartment, cert_bundle_verify):
        self.token_signer = token_signer
        self.scope = scope
        self.target_compartment = target_compartment
        self.cert_bundle_verify = cert_bundle_verify
        self._last_fetch_time = None

    def _set_oauth_token_endpoint(self, oauth_token_endpoint):
        if not oauth_token_endpoint:
            oauth_token_endpoint = self._fetch_oauth_token_endpoint()
        self.oauth_token_endpoint = oauth_token_endpoint
        self.logger.debug(f"OAuth endpoint: {self.oauth_token_endpoint}")

    @staticmethod
    def _fetch_oauth_token_endpoint():
        """
        Auto-discover the OAuth token endpoint URL from instance metadata

        Queries the OCI Instance Metadata Service (IMDS) to determine the current region,
        then constructs the appropriate OAuth endpoint URL for that region.

        Returns:
            str: The OAuth endpoint URL (e.g., "https://auth.us-phoenix-1.oraclecloud.com/v1/oauth2/scoped")

        Raises:
            RuntimeError: If region cannot be determined from instance metadata
        """
        region_data = INSTANCE_METADATA_URL_CERTIFICATE_RETRIEVER_RETRY_STRATEGY.make_retrying_call(
            auth_utils.get_region_data_from_imds)
        region = region_data.get(REGION_IDENTIFIER_PROPERTY_NAME)
        return f"{oci.regions.endpoint_for('auth', region)}/v1/oauth2/scoped"

    def _initialize_locks(self):
        self._reset_signers_lock = threading.Lock()

    def _initialize_keys_and_suppliers(self):
        self._session_key_supplier = SessionKeySupplier()
        self._private_key = None
        self._security_token: typing.Optional[SecurityTokenContainer] = None
        self._security_token: typing.Optional[SecurityTokenContainer] = None

    def _generate_oauth_token_and_set_state(self):
        oauth_token = self._generate_oauth_token()
        print("Generated OAuth token, setting state...")
        print(oauth_token)
        self._set_state(oauth_token)

    def _generate_oauth_token(self):
        """
        Execute the OAuth token exchange process

        This is the core method that performs the OAuth 2.0 token exchange:
        1. Builds the request payload with scope, public key, and target compartment
        2. Makes an authenticated request to the OAuth endpoint using the token_signer
        3. Parses the response and extracts the new OAuth token
        4. Wraps the token in a SecurityTokenContainer for lifecycle management

        Returns:
            SecurityTokenContainer: Container holding the new OAuth token with expiration info

        Raises:
            oci.exceptions.ServiceError: If the OAuth endpoint returns an error
            RuntimeError: If the response cannot be decoded or lacks expected fields
        """
        request_payload = self._get_oauth_request_payload()
        request_headers = {"Content-type": "application/json"}

        response = self._make_oauth_request(request_headers, request_payload)
        if not response.ok:
            raise oci.exceptions.ServiceError(response.status_code, response.reason, response.headers,
                                              "Failed to get OAuth token")

        decoded_response = self._decode_oauth_response(response)

        return self._get_security_token(decoded_response)

    def _get_oauth_request_payload(self):
        """
        Build the JSON payload for the OAuth token exchange request

        The payload contains:
        - scope: Defines what resources/actions this token can access
        - public_key: PEM-formatted public key (sanitized, no headers/footers)
        - target_compartment: OCID of the compartment for scoped access

        Returns:
            dict: JSON-serializable payload for the OAuth request
        """
        return {
            "scope": self.scope,
            "public_key": self._get_sanitized_public_key(),
            "target_compartment": self.target_compartment
        }

    def _get_sanitized_public_key(self):
        """Extract and format the public key for OAuth request payload"""
        # Get the current public key from our session key supplier
        public_key = self._session_key_supplier.get_key_pair()["public"]
        # Convert to PEM format bytes
        public_key_bytes = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
        # Remove PEM headers/footers and whitespace for the OAuth request
        return auth_utils.sanitize_certificate_string(public_key_bytes)

    def _make_oauth_request(self, headers, payload):
        """Execute the authenticated HTTP request to the OAuth endpoint"""
        print(f"Requesting OAuth token from : {self.oauth_token_endpoint}")
        print(headers)
        # Make POST request to OAuth endpoint, authenticated with the original token_signer
        response = requests.Session().post(self.oauth_token_endpoint,
                                           json=payload,  # JSON payload with scope, public_key, target_compartment
                                           headers=headers,  # Content-Type: application/json
                                           auth=self.token_signer,  # Original signer (e.g., instance principal)
                                           verify=self.cert_bundle_verify,  # SSL verification
                                           timeout=(10, 60))  # Connection and read timeouts

        # Log response details for debugging (excluding sensitive token data)
        log_dict = {"status_code": response.status_code,
                    "url": response.url,
                    "header": dict(response.headers.items()),
                    "reason": response.reason}
        print(f"Received OAuth token response:\n{pprint.pformat(log_dict, indent=2)}")

        return response

    @staticmethod
    def _decode_oauth_response(response):
        try:
            return response.content.decode("UTF-8")
        except ValueError:
            raise RuntimeError("Unable to decode the response for OAuth token.")

    def _get_security_token(self, decoded_response):
        if "token" in decoded_response:
            response_json = json.loads(decoded_response)
            return SecurityTokenContainer(self._session_key_supplier, response_json["token"])
        else:
            raise RuntimeError(f"Could not find token in the decoded response: {decoded_response}")

    def _set_state(self, security_token):
        self._security_token = security_token
        self._private_key = self._get_private_key()
        self._last_fetch_time = time.time()

    def _get_private_key(self):
        return self._session_key_supplier.get_key_pair()["private"]

    def _initialize_parent(self, generic_headers):
        token = self._security_token.security_token
        if generic_headers:
            super(OauthExchangeTokenSigner, self).__init__(token, self._private_key, generic_headers=generic_headers)
        else:
            super(OauthExchangeTokenSigner, self).__init__(token, self._private_key)

    def __call__(self, request, enforce_content_headers=True):
        """
        Sign an HTTP request with the OAuth token (called automatically by OCI clients)

        This method is invoked by OCI service clients before each API call to sign the request.
        It ensures the OAuth token is fresh and valid before signing:

        1. Checks if the current token is stale (older than TOKEN_STALENESS_IN_SECONDS)
        2. If stale, attempts to refresh the token using thread-safe locking
        3. Updates internal signers with the new token if refresh succeeds
        4. Delegates to parent SecurityTokenSigner to perform the actual request signing

        Args:
            request: The HTTP request object to be signed
            enforce_content_headers (bool): Whether to enforce content-related headers in signature

        Returns:
            The signed request object ready for transmission

        Note:
            This method is thread-safe and handles concurrent refresh attempts properly.
        """

        if self._is_security_token_stale():
            with self._reset_signers_lock:
                token_refreshed = self._refresh_oauth_token()
                if token_refreshed:
                    self._reset_signers()
        return super(OauthExchangeTokenSigner, self).__call__(request, enforce_content_headers)

    def _is_security_token_stale(self):
        return self._last_fetch_time is None or (time.time() - self._last_fetch_time > self.TOKEN_STALENESS_IN_SECONDS)

    def _refresh_oauth_token(self):
        """
        Attempt to refresh the OAuth token with error handling and fallback

        This method tries to obtain a new OAuth token and gracefully handles failures:
        1. Refreshes the session key pair (generates new public/private keys)
        2. Performs the OAuth token exchange to get a fresh token
        3. If exchange fails but current token is still valid, continues with cached token
        4. If exchange fails and no valid cached token exists, raises the exception

        Returns:
            bool: True if token was successfully refreshed, False if using cached token

        Raises:
            oci.exceptions.ServiceError: If token refresh fails and no valid cached token available
            RuntimeError: If token refresh fails and no valid cached token available
        """
        self.logger.debug("Refreshing OAuth token")
        try:
            self._session_key_supplier.refresh()
            self._generate_oauth_token_and_set_state()
            return True
        except (oci.exceptions.ServiceError, RuntimeError) as e:
            if self._is_security_token_valid():
                self.logger.info("Fetching OAuth token failed, using token from cache")
                return False
            else:
                self.logger.error("Fetching OAuth token failed")
                raise e

    def _is_security_token_valid(self):
        return self._security_token and self._security_token.valid()

    def _reset_signers(self):
        """
        Update internal signers with the current OAuth token and private key

        This method updates the API key and private key used by the underlying
        SecurityTokenSigner components after a token refresh. It ensures that
        both the basic signer (for most requests) and body signer (for requests
        with body content) use the latest authentication credentials.

        The API key format follows OCI's security token standard:
        "ST${security_token}" where security_token is the OAuth token
        """
        self.api_key = SECURITY_TOKEN_FORMAT_STRING.format(self._security_token.security_token)
        self.private_key = self._get_private_key()

        self._basic_signer.reset_signer(self.api_key, self.private_key)
        self._body_signer.reset_signer(self.api_key, self.private_key)
