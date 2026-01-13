# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from typing import Any, Dict, Optional

import oci

from oci.addons.adk.auth.auth_provider import AuthProvider


class OCIResourcePrincipalAuth(AuthProvider):
    """OCI Authentication Provider using resource principal."""

    def __init__(
        self, security_token: Optional[str] = None, region: Optional[str] = None
    ):
        """Initialize OCI Resource Principal Auth Provider.

        Args:
            security_token (Optional[str]): Security token for authentication
            region (Optional[str]): OCI region
        """
        self._signer = None
        self.region = region

    def get_config(self) -> Dict[str, Any]:
        """Get OCI configuration.

        Returns:
            Dict[str, Any]: OCI configuration dictionary with region and tenancy

        Raises:
            Exception: If resource principal auth is not configured
        """
        signer = self.get_auth_credentials()
        config = {"region": signer.region, "tenancy": signer.tenancy_id}  # type: ignore[attr-defined]
        if self.region:
            config["region"] = self.region
        return config

    def get_auth_credentials(self) -> oci.signer.AbstractBaseSigner:
        """Get OCI resource principal signer.

        Returns:
            oci.signer.AbstractBaseSigner: OCI resource principal signer

        Raises:
            Exception: If resource principal auth is not configured
        """
        if self._signer is None:
            self._signer = oci.auth.signers.get_resource_principals_signer()
        return self._signer  # type: ignore[return-value]
