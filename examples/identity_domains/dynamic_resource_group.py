# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script demonstrates how to list, search and get dynamic resource groups, as well as the CRUD procedures.

import oci

# DEFAULT profile will load by default
# To use a different profile in ~/.oci/config:
# config = oci.config.from_file(profile_name='<replace with profile name>')
config = oci.config.from_file()
compartment_id = config["tenancy"]

# ATTN: regarding adding "domain_endpoint":
# To find Domain URL, naviage to Identity > Domains in OCI console, choose relevant domain,
# then in the overview page, find "Domain URL" under "Domain Information", click "Copy",
# open ~/.oci/config in editor of your choice, create custom value "domain_endpoint", paste the URL after the value name.
# Should look like: domain_endpoint=https://idcs-...
# Further reading: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains
# OCI config docs: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm

try:
    domain_url = config["domain_endpoint"]
except NameError:
    print("Please add \"domain_endpoint\" to your ~/.oci/config: view comments in the source code for more information.\n")

identity_domains_client = oci.identity_domains.IdentityDomainsClient(
    config=config, service_endpoint=domain_url
)

# List all dynamic resource groups
dg_list = identity_domains_client.list_dynamic_resource_groups().data
print("Number of dynamic resource groups: ", dg_list.total_results)

# Get dynamic resource group
for dg in dg_list.resources:
    dg1 = identity_domains_client.get_dynamic_resource_group(
        dynamic_resource_group_id=dg.ocid, attributes="matchingRule"
    ).data
    print(
        "Dynamic resource group: ",
        dg1.display_name,
        ", Ocid: ",
        dg1.ocid,
        ", matching_rule: ",
        dg1.matching_rule,
    )
    break

# Search for dynamic resource groups using post
dg_search = identity_domains_client.search_dynamic_resource_groups(
    dynamic_resource_group_search_request=oci.identity_domains.models.DynamicResourceGroupSearchRequest(
        schemas=["urn:ietf:params:scim:api:messages:2.0:SearchRequest"],
        attributes=["display_name", "id"],
        filter='displayName co "inspectors"',
        start_index=1,
        count=2,
    )
).data
print("", dg_search)

# Create dynamic resource group
dg = identity_domains_client.create_dynamic_resource_group(
    dynamic_resource_group=oci.identity_domains.models.DynamicResourceGroup(
        display_name="another-test-dg-from-idcs_sdk",
        description="test description",
        matching_rule="All {instance.compartment.id = 'ocid.blah'}",
        schemas=["urn:ietf:params:scim:schemas:oracle:idcs:DynamicResourceGroup"],
    )
).data
print("Created dynamic resource group: ", dg.display_name, ", Ocid: ", dg.ocid)

# Update dynamic resource group (patch)
dg = identity_domains_client.patch_dynamic_resource_group(
    dynamic_resource_group_id=dg.ocid,
    patch_op=oci.identity_domains.models.PatchOp(
        schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        operations=[
            {"op": "replace", "path": "description", "value": "updated description"},
            {
                "op": "replace",
                "path": "matchingRule",
                "value": "compartment.id = 'ocid1.compartment.oc1.phx.ocid2'",
            },
        ],
    ),
).data
print(
    "Dynamic resource group new description: ",
    dg.description,
    " matching rule:",
    dg.matching_rule,
)

# Replace a dynamic resource group (put)
dg = identity_domains_client.put_dynamic_resource_group(
    dynamic_resource_group_id=dg.ocid,
    dynamic_resource_group=oci.identity_domains.models.DynamicResourceGroup(
        schemas=["urn:ietf:params:scim:schemas:oracle:idcs:DynamicResourceGroup"],
        display_name="Replacement name",
        description="replacement description",
        matching_rule="All {instance.compartment.id = 'ocid.replacement.blah'}",
    ),
).data
print(
    "Dynamic resource group new description: ",
    dg.description,
    " matching rule:",
    dg.matching_rule,
)

# Delete dynamic resource group
print("Deleting dynamic resource group ", dg.ocid)
identity_domains_client.delete_dynamic_resource_group(dynamic_resource_group_id=dg.ocid)
