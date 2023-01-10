# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the File Storage service in the Python SDK. This script accepts two
# arguments:
#
#   * The first argument is the OCID of the compartment where we'll create a file system
#   * The second is the name of the availability domain where we'll create a file system
#
# The script will demonstrate:
#
#     * Creating a new file system
#     * Creating a mount target via which the file system can be accessed. The mount target and file system must
#       be in the same availability domain in order to export the file system from the mount target
#     * Creating an export so that we can mount the file system (see
#       https://docs.cloud.oracle.com/Content/File/Tasks/mountingfilesystems.htm for more information)
#     * Creating a snapshot of the file system
#
# In order to demonstrate functionality for mount targets and export sets, this script will also create a VCN
# and subnet. These will be deleted at the end of the script.

import oci
import sys
import time


def create_vcn_and_subnet(virtual_network, compartment_id, availability_domain):
    vcn_name = 'py_sdk_fs_example_vcn'
    cidr_block = "10.0.0.0/16"
    vcn_dns_label = 'pysdkfs'

    result = virtual_network.create_vcn(
        oci.core.models.CreateVcnDetails(
            cidr_block=cidr_block,
            display_name=vcn_name,
            compartment_id=compartment_id,
            dns_label=vcn_dns_label
        )
    )
    vcn = oci.wait_until(
        virtual_network,
        virtual_network.get_vcn(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    ).data

    subnet_name = 'py_sdk_fs_example_subnet'
    subnet_dns_label = 'pyfssub'
    result = virtual_network.create_subnet(
        oci.core.models.CreateSubnetDetails(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            display_name=subnet_name,
            vcn_id=vcn.id,
            cidr_block=cidr_block,
            dns_label=subnet_dns_label
        )
    )
    subnet = oci.wait_until(
        virtual_network,
        virtual_network.get_subnet(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    ).data

    return {'vcn': vcn, 'subnet': subnet}


def delete_vcn_and_subnet(virtual_network, vcn_and_subnet):
    vcn = vcn_and_subnet['vcn']
    subnet = vcn_and_subnet['subnet']
    composite_virtual_network = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)
    # Sometimes we can't delete the subnet straight after a mount target has been deleted as network resources
    # still need to clear. If we get a conflict, try a few times before bailing out
    attempts = 0
    while attempts < 5:
        try:
            composite_virtual_network.delete_subnet_and_wait_for_state(
                subnet.id,
                [oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
            )
            break
        except oci.exceptions.ServiceError as e:
            attempts += 1
            if e.status == 409 and attempts < 5:
                time.sleep(50)
            else:
                raise
    composite_virtual_network.delete_vcn_and_wait_for_state(
        vcn.id,
        [oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
    )


config = oci.config.from_file()
iam_client = oci.identity.IdentityClient(config)
file_storage_client = oci.file_storage.FileStorageClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)

if len(sys.argv) != 5:
    raise RuntimeError('This script expects an argument of the compartment OCID '
                       'and availability domain where the file system will be created. '
                       'It also expects defined tag namespace/key.')

# The first argument is the name of the script, so start the index at 1
compartment_id = sys.argv[1]
availability_domain = sys.argv[2]
namespace = sys.argv[3]
defined_key = sys.argv[4]

# Here we apply a retry strategy to the call to ride out any throttles, timeouts or intermittent 500s (internal server
# errors). The retry strategy will also make requests with an opc-retry-token that it generates.
#
# If you do not use the retry_strategy (or have an alternate way of retrying you wish to use instead) we still
# recommend that you use an opc-retry-token in your service calls so that if you receive, say, a timeout or server error
# and need to retry/reissue the request you won't run the risk of creating multiple resources.
create_response = file_storage_client.create_file_system(
    oci.file_storage.models.CreateFileSystemDetails(
        display_name='py_sdk_example_fs',
        compartment_id=compartment_id,
        availability_domain=availability_domain,
        freeform_tags={"foo": "value"},
        defined_tags={namespace: {defined_key: "value"}}
    ),
    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
)

# A file system has a lifecycle state, we should wait until it is active. Note that wait_until returns a response, so
# to access the model object we use the .data attribute
file_system = oci.wait_until(
    file_storage_client,
    file_storage_client.get_file_system(create_response.data.id),
    'lifecycle_state',
    'ACTIVE'
).data
print('Created file system:\n{}'.format(file_system))
print('=============================\n')

# We can update the display name of the file system
update_response = file_storage_client.update_file_system(
    file_system.id,
    oci.file_storage.models.UpdateFileSystemDetails(display_name='updated_py_sdk_example_fs')
)
print('Updated file system:\n{}'.format(update_response.data))
print('=============================\n')

# Listing file systems is a paginated operation, so we can use the functionality in the oci.pagination
# module to get all the results
all_file_systems = oci.pagination.list_call_get_all_results(
    file_storage_client.list_file_systems,
    compartment_id,
    availability_domain
)
print('All file systems:\n{}'.format(all_file_systems.data))
print('=============================\n')

# To create a mount target, first we need a VCN and subnet
vcn_and_subnet = create_vcn_and_subnet(virtual_network_client, compartment_id, availability_domain)
mount_target_name = 'pysdk_example_mt'
subnet = vcn_and_subnet['subnet']

# Here we create a mount target but instead of using the retry_strategy we supply an opc-retry-token. This will not
# make the SDK automatically retry in the event of failure but means that if we reissue the same request with the same
# token (e.g. because our original request timed out or we received a 500/internal server error) we avoid the risk
# of multiple resources being created.
#
# The opc-retry-token should uniquely identify the request. The token generation shown here is just an example, but
# in Production code you should have a better way of generating these
#
# Some other items to note about mount target creation:
#   - This creates a mount target WITHOUT specifying a hostname. This means that the mount target will only be accessible
#     via its private IP address. A hostname can be specified by using the "hostname" attribute of CreateMountTargetDetails
#   - A private IP address can be specified by using the "ip_address" attribute of CreateMountTargetDetails. If no explicit
#     private IP address is specified then one will be selected from the available pool of free private IPs in the subnet. If
#     a private IP address is specified, then it must not already be used
mount_target_retry_token = 'example_token_{}'.format(int(time.time()))
create_response = file_storage_client.create_mount_target(
    oci.file_storage.models.CreateMountTargetDetails(
        availability_domain=subnet.availability_domain,
        subnet_id=subnet.id,
        compartment_id=compartment_id,
        display_name=mount_target_name,
        freeform_tags={"foo": "value"},
        defined_tags={namespace: {defined_key: "value"}}
    ),
    opc_retry_token=mount_target_retry_token
)

# A mount target also has a lifecycle state, so wait until it is active. Note that wait_until returns a response, so
# to access the model object we use the .data attribute
mount_target = oci.wait_until(
    file_storage_client,
    file_storage_client.get_mount_target(create_response.data.id),
    'lifecycle_state',
    'ACTIVE'
).data
print('Created mount target:\n{}'.format(mount_target))
print('=============================\n')

# If we submit the request to create the mount target with the same retry token then this won't result in a new resource
# but instead the response will contain the same resource which has already been created
create_response_with_retry_token = file_storage_client.create_mount_target(
    oci.file_storage.models.CreateMountTargetDetails(
        availability_domain=subnet.availability_domain,
        subnet_id=subnet.id,
        compartment_id=compartment_id,
        display_name=mount_target_name,
        freeform_tags={"foo": "value"},
        defined_tags={namespace: {defined_key: "value"}}
    ),
    opc_retry_token=mount_target_retry_token
)
print('Created mount target with same request and retry token:\n{}'.format(create_response_with_retry_token.data))
print('Same mount target returned? {}'.format(mount_target.id == create_response_with_retry_token.data.id))
print('=============================\n')

# Note that the MountTarget contains an array of private IP OCIDs. In order to get the
# IP address of the MountTarget, we can use VirtualNetworkClient's get_private_ip function
mount_target_private_ip_id = mount_target.private_ip_ids[0]
get_private_ip_response = virtual_network_client.get_private_ip(mount_target_private_ip_id)
print('Mount target private IP: {}'.format(get_private_ip_response.data.ip_address))
print('=============================\n')

# Listing mount targets is a paginated operation, so we can use the functionality in the oci.pagination
# module to get all the results
all_mount_targets = oci.pagination.list_call_get_all_results(
    file_storage_client.list_mount_targets,
    compartment_id,
    availability_domain
)
print('All mount targets:\n{}'.format(all_mount_targets.data))
print('=============================\n')

# A mount target contains an export set, which we can use to link the mount target to the file system. We do this
# by creating an export that links the export set and the file system. Once we have an export, we can access the
# file system via the mount target and the file system can be mounted on, say, a compute instance.
#
# For more information on mounting file systems see:
# https://docs.cloud.oracle.com/Content/File/Tasks/mountingfilesystems.htm
create_response = file_storage_client.create_export(
    oci.file_storage.models.CreateExportDetails(
        export_set_id=mount_target.export_set_id,
        file_system_id=file_system.id,
        path='/files'
    ),
    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
)

# We can list exports. This operation also takes optional filters so we can narrow this list down by file system
# or export set (mount target).
# Since listing is a paginated operation, we can use the functionality in oci.pagination
all_exports_by_file_system = oci.pagination.list_call_get_all_results(
    file_storage_client.list_exports,
    compartment_id=compartment_id,
    file_system_id=file_system.id
)
print('All exports by file system:\n{}'.format(all_exports_by_file_system.data))
print('=============================\n')
all_exports_by_export_set = oci.pagination.list_call_get_all_results(
    file_storage_client.list_exports,
    compartment_id=compartment_id,
    export_set_id=mount_target.export_set_id
)
print('All exports by export set:\n{}'.format(all_exports_by_export_set.data))
print('=============================\n')

# We can also retrieve information on an export set itself
get_export_set_response = file_storage_client.get_export_set(mount_target.export_set_id)
print('Export set on mount target:\n{}'.format(get_export_set_response.data))
print('=============================\n')

# Exports have a lifecycle state, so we can wait on it to become available. Also, if we no longer need an export
# then we can delete it.
#
# When deleting, since the resource may be gone, we set succeed_on_not_found on the waiter so that we consider
# receiving a 404 back from the service as a successful delete
get_export_response = oci.wait_until(
    file_storage_client,
    file_storage_client.get_export(create_response.data.id),
    'lifecycle_state',
    'ACTIVE'
)
export = get_export_response.data
file_storage_client.delete_export(export.id)
oci.wait_until(
    file_storage_client,
    get_export_response,
    'lifecycle_state',
    'DELETED',
    succeed_on_not_found=True
)
print('Deleted export: {}'.format(export.id))
print('=============================\n')

# We can create a point-in-time snapshot of a file system. Snapshots also have a lifecycle state, so we can wait on it
# to become available
#
# Note that snapshot names are immutable and must be unique amongst all non-DELETED snapshots for a file system.
create_snapshot_response = file_storage_client.create_snapshot(
    oci.file_storage.models.CreateSnapshotDetails(
        file_system_id=file_system.id,
        name='my_snapshot_1',
        freeform_tags={"foo": "value"},
        defined_tags={namespace: {defined_key: "value"}}
    ),
    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
)

# A snapshot also has a lifecycle state, so wait until it is active
get_snapshot_response = oci.wait_until(
    file_storage_client,
    file_storage_client.get_snapshot(create_snapshot_response.data.id),
    'lifecycle_state',
    'ACTIVE'
)
snapshot = get_snapshot_response.data
print('Created snapshot:\n{}'.format(snapshot))
print('=============================\n')

# We can list snapshots for a given file system. This is a paginated operation, so we can use the functions in
# oci.pagination
all_snapshots = oci.pagination.list_call_get_all_results(
    file_storage_client.list_snapshots,
    file_system.id
)
print('All snapshots for file system:\n{}'.format(all_snapshots.data))
print('=============================\n')

# We can also delete a snapshot and then wait for it to be deleted. The snapshot may already be deleted
# by the time we call wait_until, so pass the get_snapshot_response to the waiter. It is recommended that
# you have a get response prior to calling the delete, INSTEAD OF doing:
#
#   oci.wait_until(file_storage_client, file_storage_client.get_snapshot(snapshot_id), ...)
file_storage_client.delete_snapshot(snapshot.id)
oci.wait_until(
    file_storage_client,
    get_snapshot_response,
    'lifecycle_state',
    'DELETED',
    succeed_on_not_found=True
)
print('Deleted snapshot')

# Once we are done with the mount target, we can delete it and then wait for it to be deleted. The mount target
# may already be deleted by the time we call wait_until, so do a get before the delete in order to have a response
# object to pass to the waiter
get_mount_target_response = file_storage_client.get_mount_target(mount_target.id)
file_storage_client.delete_mount_target(mount_target.id)
oci.wait_until(
    file_storage_client,
    get_mount_target_response,
    'lifecycle_state',
    'DELETED',
    succeed_on_not_found=True
)
print('Deleted mount target')

file_storage_client.delete_file_system(file_system.id)
oci.wait_until(
    file_storage_client,
    file_storage_client.get_file_system(file_system.id),
    'lifecycle_state',
    'DELETED',
    succeed_on_not_found=True
)
print('Deleted file system')

delete_vcn_and_subnet(virtual_network_client, vcn_and_subnet)
print('Deleted VCN and subnet')

print('Script finished')
