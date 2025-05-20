# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from typing import Any, Dict, Optional

import oci

from oci.addons.adk.auth.auth_provider import AuthProvider


class OCISessionAuth(AuthProvider):
    """OCI Authentication Provider using session authentication."""

    def __init__(
        self,
        config_path: Optional[str] = oci.config.DEFAULT_LOCATION,
        profile: Optional[str] = oci.config.DEFAULT_PROFILE,
    ):
        """Initialize OCI Session Auth Provider.

        Args:
            config_path (str): Path to OCI config file
            profile (str): Profile name to use from config file. Defaults to "DEFAULT".
        """
        self.config_path = config_path
        self.profile = profile
        self._config: Optional[Dict[str, Any]] = None
        self._signer: Optional[oci.signer.AbstractBaseSigner] = None

    def get_config(self) -> Dict[str, Any]:
        """Get OCI configuration from config file.

        Returns:
            Dict[str, Any]: OCI configuration

        Raises:
            oci.exceptions.InvalidConfig: If config validation fails
            FileNotFoundError: If security token file not found
        """
        if self._config is None:
            self._config = oci.config.from_file(
                file_location=self.config_path, profile_name=self.profile
            )

            # Verify required fields for session auth
            required_fields = ["key_file", "security_token_file", "region"]
            missing_fields = [
                field for field in required_fields if field not in (self._config or {})
            ]
            if missing_fields:
                raise oci.exceptions.InvalidConfig(
                    {field: "missing" for field in missing_fields}
                )
        return self._config or {}

    def get_auth_credentials(self) -> oci.signer.AbstractBaseSigner:
        """Get OCI signer using security token authentication.

        Returns:
            oci.signer.AbstractBaseSigner: OCI signer for authentication

        Raises:
            oci.exceptions.InvalidConfig: If config validation fails
            FileNotFoundError: If key file or security token file not found
        """
        if self._signer is None:
            config = self.get_config()

            key_file = config.get("key_file")
            if not key_file:
                raise oci.exceptions.InvalidConfig({"key_file": "missing"})

            security_token_file = config.get("security_token_file")
            if not security_token_file:
                raise oci.exceptions.InvalidConfig({"security_token_file": "missing"})

            # Load private key
            private_key = oci.signer.load_private_key_from_file(
                key_file,
                None,  # No passphrase
            )

            # Load security token
            with open(security_token_file) as f:
                security_token = f.read()

            self._signer = oci.auth.signers.SecurityTokenSigner(
                security_token, private_key
            )
        return self._signer
