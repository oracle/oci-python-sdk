# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import sys

"""
Example showing how to initialize and use the Resource Principals signer.

This example shows the resource principals signer being used with the
DBaaS service.  The instance must be set up for resource principals for
this example to work.

The compartment ID must be provided when running the example.

python resource_principals_example <compartment_id>
"""

if len(sys.argv) != 2:
    raise RuntimeError('A compartment ID must be provided')

compartment_id = sys.argv[1]

# Create a Response Pricipals signer
print("=" * 80)
print("Intializing new signer")
rps = oci.auth.signers.get_resource_principals_signer()

# Print the Resource Principal Security Token
# This step is not required to use the signer, it just shows that the security
# token can be retrieved from the signer.
print("=" * 80)
print("Resource Principal Security Token")
print(rps.get_security_token())

print("=" * 80)
print("Calling list_autonomous_databases")
# Note that the config is passed in as an empty dictionary.  A populated config
# is not needed when using a Resource Principals signer
db_client = oci.database.DatabaseClient({}, signer=rps)
response = db_client.list_autonomous_databases(compartment_id, limit=5)
print(response.data)
