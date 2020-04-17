# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
from .ephemeral_resource_principals_signer import EphemeralResourcePrincipalSigner

OCI_RESOURCE_PRINCIPAL_VERSION = "OCI_RESOURCE_PRINCIPAL_VERSION"
OCI_RESOURCE_PRINCIPAL_RPST = "OCI_RESOURCE_PRINCIPAL_RPST"
OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM = "OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM"
OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM_PASSPHRASE = "OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM_PASSPHRASE"
OCI_RESOURCE_PRINCIPAL_REGION = "OCI_RESOURCE_PRINCIPAL_REGION"


def get_resource_principals_signer():
    """
    A Resource Principals signer is token based signer.  The flavor of resource
    principals signer required is determined by the configured environment of
    the instance.

    returns: a resource principals signer
    """
    rp_version = os.environ.get(OCI_RESOURCE_PRINCIPAL_VERSION, "UNDEFINED")
    if rp_version == "2.2":
        """
        This signer takes its configuration from the following environment variables.
        - OCI_RESOURCE_PRINCIPAL_RPST: the Resource Principals Session Token
        - OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM: the private key in PEM format
        - OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM_PASSPHRASE: the (optional) passphrase for the private key

            These three variables may be used in one of two modes. In the first mode, they contain the actual
            contents of the RPST, private key (in PEM format) and the passphrase. This mode is only useful for
            short-lived programs.

            In the second mode, if these variables contain absolute paths, then those paths are taken as the
            on-filesystem location of the values in question. The signer may attempt to reload these values from
            the filesystem on receiving a 401 response from an OCI service. This mode is used in cases where the
            program executes in an environment where an external provider may inject updated tokens into
            the filesystem.

        - OCI_RESOURCE_PRINCIPAL_REGION: the canonical region name

            This is utilised in locating the "local" endpoints of services.
        """
        session_token = os.environ.get(OCI_RESOURCE_PRINCIPAL_RPST)
        private_key = os.environ.get(OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM)
        private_key_passphrase = os.environ.get(OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM_PASSPHRASE)
        region = os.environ.get(OCI_RESOURCE_PRINCIPAL_REGION)

        return EphemeralResourcePrincipalSigner(session_token=session_token,
                                                private_key=private_key,
                                                private_key_passphrase=private_key_passphrase,
                                                region=region)
    elif rp_version == "UNDEFINED":
        raise EnvironmentError("{} is not defined".format(OCI_RESOURCE_PRINCIPAL_VERSION))
    else:
        raise EnvironmentError("Unsupported {}: {}".format(OCI_RESOURCE_PRINCIPAL_VERSION, rp_version))
