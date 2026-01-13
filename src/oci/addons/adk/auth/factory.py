# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from enum import Enum
from typing import Optional

import oci.config

from oci.addons.adk.auth.auth_provider import AuthProvider
from oci.addons.adk.auth.oci.instance_principal import OCIInstancePrincipalAuth
from oci.addons.adk.auth.oci.resource_principal import OCIResourcePrincipalAuth
from oci.addons.adk.auth.oci.session import OCISessionAuth
from oci.addons.adk.auth.oci.user_principal import OCIUserPrincipalAuth


class OCIAuthType(str, Enum):
    """OCI authentication types as enumerator."""

    API_KEY = "api_key"
    SECURITY_TOKEN = "security_token"
    INSTANCE_PRINCIPAL = "instance_principal"
    RESOURCE_PRINCIPAL = "resource_principal"


class AuthFactory:
    """Factory for creating authentication providers."""

    @staticmethod
    def create_oci_auth(
        auth_type: OCIAuthType,
        config_path: Optional[str] = oci.config.DEFAULT_LOCATION,
        profile: Optional[str] = oci.config.DEFAULT_PROFILE,
        token: Optional[str] = None,
        region: Optional[str] = None,
    ) -> AuthProvider:
        """Create OCI authentication provider.

        Args:
            auth_type (str): Type of OCI auth. One of: 'user_principal',
            'instance_principal', 'security_token'

            config_path (Optional[str]): Path to OCI config file. Required for
            user_principal and session auth.

            profile (Optional[str]): Profile name in config.
            Only used with user_principal and session auth. Defaults to "DEFAULT".

            token (Optional[str]): token string.
            region (Optional[str]): OCI region.

        Returns:
            AuthProvider: OCI auth provider

        Raises:
            ValueError: If auth_type is invalid or required args are missing
        """
        # Validate auth_type first
        if auth_type not in OCIAuthType:
            raise ValueError(
                f"Invalid auth_type: {auth_type}. Must be one of: "
                f"{', '.join(repr(t) for t in OCIAuthType)}"
            )

        if auth_type == OCIAuthType.INSTANCE_PRINCIPAL:
            return OCIInstancePrincipalAuth(security_token=token, region=region)

        if auth_type == OCIAuthType.RESOURCE_PRINCIPAL:
            return OCIResourcePrincipalAuth(security_token=token, region=region)

        if auth_type == OCIAuthType.API_KEY:
            return OCIUserPrincipalAuth(config_path=config_path, profile=profile)

        if auth_type == OCIAuthType.SECURITY_TOKEN:
            return OCISessionAuth(config_path=config_path, profile=profile)

        # This code is unreachable since we validate auth_type at the start
        raise ValueError(f"Unsupported auth_type: {auth_type}")  # pragma: no cover
