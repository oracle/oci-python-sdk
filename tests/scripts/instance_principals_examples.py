# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import os

signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

identity_client = oci.identity.IdentityClient(config={}, signer=signer)
print(identity_client.list_regions().data)
print(identity_client.list_availability_domains(compartment_id=os.environ.get('OCI_PYSDK_COMPARTMENT_ID')).data)

# If you explicitly specify a region in configuration, it will be honoured. In the below example, you can also change the region later by doing:
#
#   object_storage_client.base_client.set_region('us-ashburn-1')
#
# You can also explicitly set an endpoint via:
#
#   object_storage_client.base_client.set_endpoint('https://<some endpoint>')
object_storage_client = oci.object_storage.ObjectStorageClient(config={'region': 'us-ashburn-1'}, signer=signer)
print(object_storage_client.get_namespace().data)
