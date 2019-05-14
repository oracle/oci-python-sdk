# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides a basic example of how to get Object Storage namespace of a tenancy that is not their own. This
# is useful in cross-tenant Object Storage operations. Object Storage namespace can be retrieved using the
# compartment id of the target tenancy if the user has necessary permissions to access that tenancy.
#
# For example if Tenant A wants to access Tenant B's object storage namespace then Tenant A has to define
# a policy similar to following:
#
# DEFINE TENANCY TenantB AS <TenantB OCID>
# ENDORSE GROUP <TenantA user group OCID> TO {TENANCY_INSPECT} IN TENANCY TenantB
#
# and Tenant B should add a policy similar to following:
#
# DEFINE TENANCY TenantA AS <TenantA OCID>
# DEFINE GROUP TenantAGroup AS <TenantA user group OCID>
# ADMIT GROUP TenantAGroup OF TENANCY TenantA TO {TENANCY_INSPECT} IN TENANCY
#
# This example covers only GetNamespace operation across tenants. Additional permissions
# will be required to perform more Object Storage operations.
#
# This script accepts one argument:
#
#   * The OCID of the compartment for which namespace should be retrieved

import oci
import sys

if len(sys.argv) != 2:
    raise RuntimeError('Unexpected number of arguments received. Consult the script header comments for expected arguments')

compartment_id = sys.argv[1]

# Default config file and profile
config = oci.config.from_file()
object_storage_client = oci.object_storage.ObjectStorageClient(config)

namespace = object_storage_client.get_namespace(compartment_id=compartment_id).data

print('Object storage namespace for compartment id {} is: {}'.format(compartment_id, namespace))
print('\n=========================\n')
