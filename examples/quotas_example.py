# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This is an example demonstrating how Quotas can be manageed using the OCI Python SDK

# This example will perform the following operations sequentially-
# - Create a Quota
# - Get the created Quota
# - List all Quotas
# - Update the previously created Quota
# - Delete this Quota

# Description of Parameters
# compartment_id	: The OCID of the compartment where Quotas will reside (this has to be the root compartment)
# name			: Name of the Quota
# description		: Description for the Quota
# statements		: An array of Quota statements written in the declarative language

# Required imports
from oci import config
from oci.limits import QuotasClient
from oci.limits.models import CreateQuotaDetails, UpdateQuotaDetails

# User configs
user_config = config.from_file()

# Sample inputs
compartment_id = user_config["tenancy"]
name = "MyQuota"
description = "This is a sample Quota"
statements = ["Zero test-family quota 'test-quota-1' in tenancy"]

# Client initialization
quotas_client = QuotasClient(user_config)

# Create
print("Creating a Quota")
create_quota_details = CreateQuotaDetails(compartment_id=compartment_id, name=name, description=description, statements=statements)
response = quotas_client.create_quota(create_quota_details)
created_quota = response.data

# Get
print("Getting Quota")
response = quotas_client.get_quota(created_quota.id)
quota = response.data
print(quota)

# List
print("Listing Quotas")
response = quotas_client.list_quotas(compartment_id)
print(response.data)

# Update
print("Updating Quota")
update_quota_details = UpdateQuotaDetails(description="This is a modified Quota")
response = quotas_client.update_quota(quota.id, update_quota_details)
print(response.data)

# Delete
print("Deleting Quota")
response = quotas_client.delete_quota(quota.id)

print("Done")
