# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci

compartment_id = '<your compartment id here>'

# By default this will hit the auth service in the region returned by http://169.254.169.254/opc/v2/instance/region on the instance.
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

# In the base case, configuration does not need to be provided as the region and tenancy are obtained from the InstancePrincipalsSecurityTokenSigner
identity_client = oci.identity.IdentityClient(config={}, signer=signer)

print(identity_client.list_regions().data)
print(identity_client.list_availability_domains(compartment_id=compartment_id).data)

# If you explicitly specify a region in configuration, it will be honoured. In the below example, you can also change the region later by doing:
#
#   object_storage_client.base_client.set_region('us-ashburn-1')
#
# You can also explicitly set an endpoint via:
#
#   object_storage_client.base_client.set_endpoint('https://<some endpoint>')
object_storage_client = oci.object_storage.ObjectStorageClient(config={'region': 'us-ashburn-1'}, signer=signer)
print(object_storage_client.get_namespace().data)
print(object_storage_client.list_buckets(namespace_name=object_storage_client.get_namespace().data, compartment_id=compartment_id).data)
