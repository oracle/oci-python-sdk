# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

# This script provides a basic example of how to use the File Storage service in the Python SDK. This script accepts two
# arguments:
#
#   * The first argument is the OCID of the compartment where we'll create a file system
#   * The second is the name of the availability domain where we'll create a file system
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

    # Sometimes we can't delete the subnet straight after a mount target has been deleted as network resources
    # still need to clear. If we get a conflict, try a few times before bailing out
    attempts = 0
    while attempts < 5:
        try:
            virtual_network.delete_subnet(subnet.id)
            oci.wait_until(
                virtual_network,
                virtual_network.get_subnet(subnet.id),
                'lifecycle_state',
                'TERMINATED',
                max_wait_seconds=600,
                succeed_on_not_found=True
            )
            break
        except oci.exceptions.ServiceError as e:
            attempts += 1
            if e.status == 409 and attempts < 5:
                time.sleep(5)
            else:
                raise

    virtual_network.delete_vcn(vcn.id)
    oci.wait_until(
        virtual_network,
        virtual_network.get_vcn(vcn.id),
        'lifecycle_state',
        'TERMINATED',
        max_wait_seconds=600,
        succeed_on_not_found=True
    )


config = oci.config.from_file()
file_storage_client = oci.file_storage.FileStorageClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)

if len(sys.argv) != 3:
    raise RuntimeError('This script expects an argument of the compartment OCID and availability domain where the file system will be created')

# The first argument is the name of the script, so start the index at 1
compartment_id = sys.argv[1]
availability_domain = sys.argv[2]

# Here we apply a retry strategy to the call to ride out any throttles or intermittent 500s
create_response = file_storage_client.create_file_system(
    oci.file_storage.models.CreateFileSystemDetails(
        display_name='py_sdk_example_fs',
        compartment_id=compartment_id,
        availability_domain=availability_domain
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

# We can update the display name of the file system
update_response = file_storage_client.update_file_system(
    file_system.id,
    oci.file_storage.models.UpdateFileSystemDetails(display_name='updated_py_sdk_example_fs')
)
print('Updated file system:\n{}'.format(update_response.data))

# Listing file systems is a paginated operation, so we can use the functionality in the oci.pagination
# module to get all the results
all_file_systems = oci.pagination.list_call_get_all_results(
    file_storage_client.list_file_systems,
    compartment_id,
    availability_domain
)
print('All file systems:\n{}'.format(all_file_systems.data))

# To create a mount target, first we need a VCN and subnet
vcn_and_subnet = create_vcn_and_subnet(virtual_network_client, compartment_id, availability_domain)
mount_target_name = 'pysdk_example_mt'
subnet = vcn_and_subnet['subnet']

# Here we apply a retry strategy to the call to ride out any throttles or intermittent 500s
create_response = file_storage_client.create_mount_target(
    oci.file_storage.models.CreateMountTargetDetails(
        availability_domain=subnet.availability_domain,
        subnet_id=subnet.id,
        compartment_id=compartment_id,
        display_name=mount_target_name
    ),
    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
)

# A mount target also has a lifecycle state, so wait until it is active. Note that wait_until returns a response, so
# to access the model object we use the .data attribute
print('Sleeping for 60 seconds after mount target creation')
time.sleep(60)  # A mount target may not be available straight after creation, which can cause get_mount_target to fail
mount_target = oci.wait_until(
    file_storage_client,
    file_storage_client.get_mount_target(create_response.data.id),
    'lifecycle_state',
    'ACTIVE'
).data
print('Created mount target:\n{}'.format(mount_target))

# Listing mount targets is a paginated operation, so we can use the functionality in the oci.pagination
# module to get all the results
all_mount_targets = oci.pagination.list_call_get_all_results(
    file_storage_client.list_mount_targets,
    compartment_id,
    availability_domain
)
print('All mount targets:\n{}'.format(all_mount_targets.data))

# A mount target contains an export set, which we can use to link the mount target to the file system. We do this
# by creating an export that links the export set and the file system
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
    compartment_id,
    file_system_id=file_system.id
)
print('All exports by file system:\n{}'.format(all_exports_by_file_system.data))
all_exports_by_export_set = oci.pagination.list_call_get_all_results(
    file_storage_client.list_exports,
    compartment_id,
    export_set_id=mount_target.export_set_id
)
print('All exports by export set:\n{}'.format(all_exports_by_export_set.data))

# Exports have a lifecycle state, so we can wait on it to become available. Also, if we no longer need an export
# then we can delete it
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

# Once we are done with the mount target, we can delete it and then wait for it to be deleted. Since the reosurce may be gone, we set
# succeed_on_not_found on the waiter so that we consider receiving a 404 back from the service as a successful delete
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

# We can delete a file system in a similar way
try:
    file_storage_client.delete_file_system(file_system.id)
    oci.wait_until(
        file_storage_client,
        file_storage_client.get_file_system(file_system.id),
        'lifecycle_state',
        'DELETED',
        succeed_on_not_found=True
    )
    print('Deleted file system')
except oci.exceptions.ServiceError as e:
    print('Exception when deleting file system: {}'.format(file_system.id))

delete_vcn_and_subnet(virtual_network_client, vcn_and_subnet)
print('Deleted VCN and subnet')

print('Script finished')
