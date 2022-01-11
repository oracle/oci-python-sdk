# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# A very basic script that can be run at the end of a wercker build to ensure that the SDK can be imported
# and used to make a call. This uses dummy values so the intended behaviour is that the call will fail
# with a ServiceError (i.e. we did actually hit the service and it came back with an error response).

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from oci.exceptions import ServiceError

import oci


key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

key_content = key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# These are dummy values and don't exist
config = {
    'log_requests': True,
    'region': 'us-ashburn-1',
    'tenancy': 'ocidv1:tenancy:oc1:phx:1111111111111:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'user': 'ocid1.user.oc1..aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'key_content': key_content,
    'fingerprint': '00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00'
}

identity_client = oci.identity.IdentityClient(config)
try:
    identity_client.list_regions()
except ServiceError:
    # We expect a service error here because we sent dummy auth information
    pass
