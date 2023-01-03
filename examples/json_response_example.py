# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example to demostrate converting a response payload to a json string.
# For more information see: https://docs.python.org/3/library/json.html
import oci
import json

# Load the default configuration
config = oci.config.from_file()
identity_client = oci.identity.IdentityClient(config)
response = identity_client.list_regions().data

# Convert the response to a json string
json_response = json.dumps(str(response))
print("My json string response: ", json_response)
