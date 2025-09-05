import os
import threading
import base64
import json
import logging
from datetime import datetime

from oci._vendor import requests
from oci.auth.session_key_supplier import SessionKeySupplier
from oci.auth.security_token_container import SecurityTokenContainer
from oci.auth.signers.security_token_signer import SecurityTokenSigner, SECURITY_TOKEN_FORMAT_STRING
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, PrivateFormat, NoEncryption

class TokenExchangeSigner(SecurityTokenSigner):
    
    """
    OCI Python SDK signer for OAuth2 Token Exchange (UPST) authentication.
    Automatically refreshes tokens as needed, suitable for use with OCI SDK clients.
    """

    
    def __init__(self, jwt, oci_domain_id, client_id, client_secret, region=None, **kwargs):       
        self.jwt = jwt
        self.client_id = client_id
        self.client_secret = client_secret
        self.oci_domain_id = oci_domain_id
        self.region = region
        self._reset_signers_lock = threading.Lock()
        self.requests_session = requests.Session()

        self.session_key_supplier = SessionKeySupplier()
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
            self._refresh_security_token_inner()
        return super().__call__(request, enforce_content_headers)

    def get_security_token(self):
        # Proactively refresh if token is past half its lifetime
        if self.security_token_container.valid_with_half_expiration_time():
            return self.security_token_container.security_token
        else:
            self._refresh_security_token_inner()
            return self.security_token_container.security_token

    def _refresh_security_token_inner(self):
        with self._reset_signers_lock:
            self.session_key_supplier.refresh()
            token = self._get_new_token()

            # Optional: Write token and key for debugging/auditing

            private_key = self.session_key_supplier.private_key
            private_pem = private_key.private_bytes(
                encoding=Encoding.PEM,
                format=PrivateFormat.PKCS8,
                encryption_algorithm=NoEncryption()
            ).decode("utf-8")


            self.security_token_container = SecurityTokenContainer(self.session_key_supplier, token)
            self._reset_signers()
    def _reset_signers(self):
        self.api_key = SECURITY_TOKEN_FORMAT_STRING.format(self.security_token_container.security_token)
        self.private_key = self.session_key_supplier.get_key_pair()['private']

        if hasattr(self, '_basic_signer'):
            self._basic_signer.reset_signer(self.api_key, self.private_key)
        if hasattr(self, '_body_signer'):
            self._body_signer.reset_signer(self.api_key, self.private_key)

    def _get_new_token(self):
        """
        Requests a new UPST token from the token exchange endpoint.
        """
        try:
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
                "subject_token": self.jwt,
                "subject_token_type": "jwt",
                "public_key": public_key_pem
            }

            full_token_url = f"https://{self.oci_domain_id}.identity.oraclecloud.com/oauth2/v1/token"
            response = self.requests_session.post(full_token_url, headers=headers, data=data)
            response.raise_for_status()            

            response_json = response.json()
            if "token" not in response_json:
                raise RuntimeError("'token' not found in token exchange response")
            return response_json["token"]

        except Exception as e:
            raise