# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This example demonstrates how to list and apply backup policies to an existing volume. Note that in order to list and apply backup policies you will need
# the appropriate level of access. See the section "Required IAM Policy" on this page:
# https://docs.cloud.oracle.com/Content/Block/Tasks/schedulingvolumebackups.htm for more information
#
# This example takes a single argument, which is the OCID of the volume which we'll apply the policy to
#
# You can also specify a backup policy at volume create time by providing a backup_policy_id. For example:
#
# result = block_storage.create_volume(
#     oci.core.models.CreateVolumeDetails(
#         display_name='my_volume_with_a_policy',
#         size_in_gbs=50,
#         availability_domain=availability_domain,
#         compartment_id=compartment_id,
#         backup_policy_id=volume_backup_policy.id
#     )
# )

import oci
import sys


config = oci.config.from_file()
block_storage_client = oci.core.BlockstorageClient(config)

if len(sys.argv) != 2:
    raise RuntimeError('This script expects an argument the OCID of the volume which the policy will be applied to')
volume_id = sys.argv[1]

# Backup policies are a paginated call, so we can use the functions in the oci.pagination module to get all available policies
volume_backup_policies = oci.pagination.list_call_get_all_results(block_storage_client.list_volume_backup_policies)
print('Policies:\n{}'.format(volume_backup_policies.data))

# We can retrieve a specific policy
volume_backup_policy = block_storage_client.get_volume_backup_policy(volume_backup_policies.data[0].id).data
print('Selected policy:\n{}'.format(volume_backup_policy))

# We can assign a policy to a volume
create_response = block_storage_client.create_volume_backup_policy_assignment(
    oci.core.models.CreateVolumeBackupPolicyAssignmentDetails(
        asset_id=volume_id,
        policy_id=volume_backup_policy.id
    )
)
print('Assigned policy to volume:\n{}'.format(create_response.data))

# We can interrogate whether an asset (a volume in this case) has a policy applied
get_policy_asset_assignment = block_storage_client.get_volume_backup_policy_asset_assignment(volume_id)
print('Assigned policy:\n{}'.format(get_policy_asset_assignment.data))

# We can remove a policy from an asset using the ID of the record which represents the assignment of the policy to the asset
block_storage_client.delete_volume_backup_policy_assignment(get_policy_asset_assignment.data[0].id)

# And now the asset reports it has no policies on it
get_policy_asset_assignment = block_storage_client.get_volume_backup_policy_asset_assignment(volume_id)
print('Assigned policy:\n{}'.format(get_policy_asset_assignment.data))
