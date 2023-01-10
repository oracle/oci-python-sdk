# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci


config = oci.config.from_file()
compartment_id = config["tenancy"]
identity = oci.identity.IdentityClient(config)

# list users from the compartmentId, adding allow_control_chars=True
# to the request will allow the response to contain control characters
users = identity.list_users(compartment_id, allow_control_chars=True)
