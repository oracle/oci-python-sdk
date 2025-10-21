# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import threading
import base64
import logging


from oci._vendor import requests
from oci.auth.session_key_supplier import SessionKeySupplier
from oci.auth.security_token_container import SecurityTokenContainer
from oci.auth.signers.security_token_signer import SecurityTokenSigner, SECURITY_TOKEN_FORMAT_STRING
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat


class TokenExchangeSigner(SecurityTokenSigner):
    """
    OCI Python SDK signer for OAuth2 Token Exchange (UPST) authentication.
    Automatically refreshes tokens as needed, suitable for use with OCI SDK clients.
    """

    def __init__(self, jwt_or_func, oci_domain_id, client_id, client_secret, region=None, **kwargs):
        # Initialize per-instance logger
        self.logger = logging.getLogger(f"{__name__}.{id(self)}")
        self.logger.addHandler(logging.NullHandler())

        # Enable or disable logging based on argument
        if kwargs.get('log_requests'):
            self.logger.disabled = False
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.disabled = True
        """
         This block ensures the jwt_or_func parameter is always treated as a callable function.
         If the user passes a function, it is assigned directly to self.jwt_function.
         If the user passes a string (a static JWT token), it is wrapped inside a lambda function
         so that self.jwt_function() can be called uniformly to retrieve the JWT token.
         This design provides flexibility:
         - Accepts either a dynamic function that returns a JWT token when called,
         - Or a static string token wrapped as a function for consistent usage internally.
        """
        if callable(jwt_or_func):
            self.jwt_function = jwt_or_func
        else:
            self.jwt_function = lambda: jwt_or_func

        self.client_id = client_id
        self.client_secret = client_secret
        self.oci_domain_id = oci_domain_id
        self.region = region

        self._reset_signers_lock = threading.Lock()
        self.requests_session = requests.Session()
        self.session_key_supplier = SessionKeySupplier()

        self.logger.debug("Initializing TokenExchangeSigner for domain: %s", oci_domain_id)

        token = self._get_new_token()
        self.security_token_container = SecurityTokenContainer(self.session_key_supplier, token)

        generic_headers = kwargs.get("generic_headers", ["date", "(request-target)", "host"])
        super().__init__(
            self.security_token_container.security_token,
            self.session_key_supplier.get_key_pair()['private'],
            generic_headers=generic_headers
        )

    def __call__(self, request, enforce_content_headers=True):
        if not self.security_token_container.valid():
            self.logger.debug("Security token invalid or expired. Refreshing token.")
            self._refresh_security_token_inner()
        return super().__call__(request, enforce_content_headers)

    def _get_jwt(self):
        return self.jwt_function()

    def get_security_token(self):
        # Proactively refresh if token is past half its lifetime
        if self.security_token_container.valid_with_half_expiration_time():
            self.logger.debug("Security token still valid (within half-life).")
            return self.security_token_container.security_token
        else:
            self.logger.debug("Security token past half-life. Refreshing token.")
            self._refresh_security_token_inner()
            return self.security_token_container.security_token

    def _refresh_security_token_inner(self):
        with self._reset_signers_lock:
            self.logger.debug("Refreshing session key supplier and security token.")
            self.session_key_supplier.refresh()
            token = self._get_new_token()
            self.logger.debug("New private key PEM generated (not shown for security).")
            self.security_token_container = SecurityTokenContainer(self.session_key_supplier, token)
            self._reset_signers()

    def _reset_signers(self):
        self.api_key = SECURITY_TOKEN_FORMAT_STRING.format(self.security_token_container.security_token)
        self.private_key = self.session_key_supplier.get_key_pair()['private']
        if hasattr(self, '_basic_signer'):
            self._basic_signer.reset_signer(self.api_key, self.private_key)
        if hasattr(self, '_body_signer'):
            self._body_signer.reset_signer(self.api_key, self.private_key)
        self.logger.debug("Signers reset with new API key and private key.")

    def _get_new_token(self):
        """
        Requests a new UPST token from the token exchange endpoint.
        """
        try:
            jwt = self._get_jwt()
            private_key = self.session_key_supplier.private_key
            public_key = private_key.public_key()
            public_key_pem = public_key.public_bytes(
                encoding=Encoding.PEM,
                format=PublicFormat.SubjectPublicKeyInfo
            ).decode("utf-8").replace("\n", "").replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "")

            encoded_auth = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode("utf-8")).decode("utf-8")
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {encoded_auth}"
            }

            data = {
                "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
                "requested_token_type": "urn:oci:token-type:oci-upst",
                "subject_token": jwt,
                "subject_token_type": "jwt",
                "public_key": public_key_pem
            }

            full_token_url = f"https://{self.oci_domain_id}.identity.oraclecloud.com/oauth2/v1/token"
            self.logger.debug("Requesting UPST token from: %s", full_token_url)

            response = self.requests_session.post(full_token_url, headers=headers, data=data)
            self.logger.debug("Received response: status=%s, url=%s", response.status_code, response.url)

            response.raise_for_status()
            response_json = response.json()

            if "token" not in response_json:
                self.logger.error("'token' not found in token exchange response: %s", response_json)
                raise RuntimeError("'token' not found in token exchange response")

            self.logger.debug("Successfully obtained new UPST token.")
            return response_json["token"]

        except Exception as e:
            self.logger.error("Failed to get new token: %s", str(e))
            raise
