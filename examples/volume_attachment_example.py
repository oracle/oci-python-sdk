# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This example demonstrates how to attach volumes to an instance using different volume attachment
# types. It covers:
#
#   - How to do an iSCSI volume attachment
#   - How to do a paravirtualized volume attachment
#
# This script accepts two arguments:
#   - The first argument is the compartment where we'll create the resources required by the script
#   - The second argument is the availability domain where resources will be created
#
# This script will create all the resources it requires:
#   - 2 volumes (using the default size of 50GB)
#   - A VCN and subnet
#   - An instance to attach the volume to. This instance will be running Oracle Linux 7.4 and have a shape of
#     VM.Standard.1.1
#
# The script will clean up these resources upon completion

import oci
import sys


def create_vcn_and_subnet(virtual_network, compartment_id, availability_domain):
    # Create a VCN
    vcn_name = 'python_sdk_test_vol_attach_vcn'
    cidr_block = "10.0.0.0/16"
    result = virtual_network.create_vcn(
        oci.core.models.CreateVcnDetails(
            cidr_block=cidr_block,
            display_name=vcn_name,
            compartment_id=compartment_id
        )
    )
    vcn = oci.wait_until(
        virtual_network,
        virtual_network.get_vcn(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    ).data
    print('Created VCN')

    # Create a subnet
    subnet_name = 'python_sdk_test_vol_attach_subnet'
    subnet_cidr_block = "10.0.0.0/24"
    result = virtual_network.create_subnet(
        oci.core.models.CreateSubnetDetails(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            display_name=subnet_name,
            vcn_id=vcn.id,
            cidr_block=subnet_cidr_block
        )
    )
    subnet = oci.wait_until(
        virtual_network,
        virtual_network.get_subnet(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    ).data
    print('Created Subnet')

    return {'vcn': vcn, 'subnet': subnet}


def create_volume(block_storage, compartment_id, availability_domain, display_name):
    result = block_storage.create_volume(
        oci.core.models.CreateVolumeDetails(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            display_name=display_name
        )
    )
    volume = oci.wait_until(
        block_storage,
        block_storage.get_volume(result.data.id),
        'lifecycle_state',
        'AVAILABLE'
    ).data
    print('Created Volume: {}'.format(display_name))

    return volume


def get_image(compute, compartment_id, operating_system, os_version, target_shape):
    images = oci.pagination.list_call_get_all_results(
        compute.list_images,
        compartment_id,
        operating_system=operating_system,
        operating_system_version=os_version
    ).data

    for img in images:
        shapes_for_image = oci.pagination.list_call_get_all_results(
            compute.list_shapes,
            compartment_id,
            image_id=img.id
        ).data

        for s in shapes_for_image:
            if s.shape == target_shape:
                return img

    raise RuntimeError('No valid image found for target OS, Version and Shape')


def launch_instance(compute, vcn_and_subnet):
    result = compute.launch_instance(
        oci.core.models.LaunchInstanceDetails(
            availability_domain=vcn_and_subnet['subnet'].availability_domain,
            compartment_id=vcn_and_subnet['subnet'].compartment_id,
            display_name='VolAttachTypesExampleInstance',
            shape='VM.Standard2.1',
            subnet_id=vcn_and_subnet['subnet'].id,
            image_id=get_image(compute, vcn_and_subnet['subnet'].compartment_id, 'Oracle Linux', '7.7', 'VM.Standard2.1').id
        )
    )
    get_instance_response = oci.wait_until(
        compute,
        compute.get_instance(result.data.id),
        'lifecycle_state',
        'RUNNING',
        max_wait_seconds=300
    )
    print('Launched Instance')

    return get_instance_response.data


def terminate_instance(compute, instance):
    compute.terminate_instance(instance.id)
    oci.wait_until(
        compute,
        compute.get_instance(instance.id),
        'lifecycle_state',
        'TERMINATED',
        max_wait_seconds=300,
        succeed_on_not_found=True
    )


def delete_vcn_and_subnet(virtual_network, vcn_and_subnet):
    composite_virtual_network = oci.core.VirtualNetworkClientCompositeOperations(virtual_network_client)

    vcn = vcn_and_subnet['vcn']
    subnet = vcn_and_subnet['subnet']

    composite_virtual_network.delete_subnet_and_wait_for_state(
        subnet.id,
        [oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
    )

    composite_virtual_network.delete_vcn_and_wait_for_state(
        vcn.id,
        [oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
    )


def delete_volume(block_storage, volume):
    block_storage.delete_volume(volume.id)
    oci.wait_until(
        block_storage,
        block_storage.get_volume(volume.id),
        'lifecycle_state',
        'TERMINATED'
    )


def detach_volume(compute, volume_attachment):
    compute.detach_volume(volume_attachment.id)
    oci.wait_until(
        compute,
        compute.get_volume_attachment(volume_attachment.id),
        'lifecycle_state',
        'DETACHED'
    )


if len(sys.argv) != 3:
    raise RuntimeError('This script needs to be provided a compartment ID and an availability domain')

compartment_id = sys.argv[1]
availability_domain = sys.argv[2]

config = oci.config.from_file()
compute_client = oci.core.ComputeClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)
block_storage_client = oci.core.BlockstorageClient(config)

vcn_and_subnet = None
volume_one = None
volume_two = None
instance = None
try:
    vcn_and_subnet = create_vcn_and_subnet(virtual_network_client, compartment_id, availability_domain)
    volume_one = create_volume(block_storage_client, compartment_id, availability_domain, 'vol_attach_example_vol_1')
    volume_two = create_volume(block_storage_client, compartment_id, availability_domain, 'vol_attach_example_vol_2')
    instance = launch_instance(compute_client, vcn_and_subnet)

    print('')
    print('')

    # All volume attachments are done via the attach_volume operation but we pass different objects to inform it what
    # type of volume attachment to do.
    #
    # These are all subclasses of oci.core.models.AttachVolumeDetails
    iscsi_volume_attachment_response = compute_client.attach_volume(
        oci.core.models.AttachIScsiVolumeDetails(
            display_name='IscsiVolAttachment',
            instance_id=instance.id,
            volume_id=volume_one.id
        )
    )
    print('Attached iSCSI volume')
    paravirtualized_volume_attachment_response = compute_client.attach_volume(
        oci.core.models.AttachParavirtualizedVolumeDetails(
            display_name='ParavirtualizedVolAttachment',
            instance_id=instance.id,
            volume_id=volume_two.id
        )
    )
    print('Attached paravirtualized volume')
    print('')

    # We can wait until the volumes have attached
    oci.wait_until(
        compute_client,
        compute_client.get_volume_attachment(iscsi_volume_attachment_response.data.id),
        'lifecycle_state',
        'ATTACHED'
    )
    oci.wait_until(
        compute_client,
        compute_client.get_volume_attachment(paravirtualized_volume_attachment_response.data.id),
        'lifecycle_state',
        'ATTACHED'
    )

    # Listing volume attachments is a paginated operation, so we can use the functions in the
    # oci.pagination module to get them all. We can also supply keyword argument filters - in
    # this case we are only interested in the volume attachments on our instance
    volume_attachments = oci.pagination.list_call_get_all_results(
        compute_client.list_volume_attachments,
        compartment_id,
        instance_id=instance.id
    ).data

    # Note that each element is a different attachment_type, denoting the different types of volume attachments
    # there are.
    #
    # These are all subclasses of oci.core.models.VolumeAttachment
    print('Volume attachments:\n{}'.format(volume_attachments))
    print('')
    print('')

    detach_volume(compute_client, paravirtualized_volume_attachment_response.data)
    print('Detached paravirtualized volume')
    print('')

    detach_volume(compute_client, iscsi_volume_attachment_response.data)
    print('Detached iSCSI volume attachment')
    print('')
finally:
    if instance:
        terminate_instance(compute_client, instance)
        print('Terminated Instance')

    if volume_one:
        delete_volume(block_storage_client, volume_one)
        print('Deleted Volume One')

    if volume_two:
        delete_volume(block_storage_client, volume_two)
        print('Deleted Volume Two')

    if vcn_and_subnet:
        delete_vcn_and_subnet(virtual_network_client, vcn_and_subnet)
        print('Deleted VCN and Subnet')

print('Script Finished')
