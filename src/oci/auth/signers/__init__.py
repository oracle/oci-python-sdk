# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .security_token_signer import SecurityTokenSigner, X509FederationClientBasedSecurityTokenSigner  # noqa: F401
from .instance_principals_security_token_signer import InstancePrincipalsSecurityTokenSigner  # noqa: F401
from .instance_principals_delegation_token_signer import InstancePrincipalsDelegationTokenSigner  # noqa: F401
from .resource_principals_federation_signer import ResourcePrincipalsFederationSigner  # noqa: F401
from .resource_principals_delegation_token_signer import ResourcePrincipalsDelegationTokenSigner  # noqa: F401
from .ephemeral_resource_principals_signer import EphemeralResourcePrincipalSigner  # noqa: F401
from .ephemeral_resource_principals_delegation_token_signer import EphemeralResourcePrincipalsDelegationTokenSigner  # noqa: F401
from .resource_principals_signer import get_resource_principals_signer, get_resource_principal_delegation_token_signer, get_oke_workload_identity_resource_principal_signer  # noqa: F401
from .oke_workload_identity_resource_principal_signer import OkeWorkloadIdentityResourcePrincipalSigner  # noqa: F401
from .ephemeral_resource_principals_v21_signer import EphemeralResourcePrincipalV21Signer  # noqa: F401
from .key_pair_signer import KeyPairSigner  # noqa: F401
from .nested_resource_principals_signer import NestedResourcePrincipals  # noqa: F401
from .oauth_exhange_token_signer import OauthExchangeTokenSigner  # noqa: F401
from .token_exchange_signer import TokenExchangeSigner  # noqa: F401

try:
    from .pkcs11_signer import PKCS11RequestSigner, PKCS11Signer  # noqa: F401
except (ImportError, ModuleNotFoundError) as ex:
    # Some environments do not have optional PKCS#11 dependencies installed.
    # Keep importing oci.auth.signers usable for non-PKCS#11 paths, but do not
    # hide unrelated import problems.
    missing_module = getattr(ex, "name", "") or ""
    if missing_module:
        is_pkcs11_import_error = missing_module == "pkcs11" or missing_module.startswith("pkcs11.")
    else:
        is_pkcs11_import_error = "pkcs11" in str(ex).lower()
    if not is_pkcs11_import_error:
        raise
