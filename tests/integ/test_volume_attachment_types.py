# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from . import util
from .. import test_config_container
import oci


def test_volume_attachment_with_different_types(virtual_network, block_storage, compute):
    with test_config_container.create_vcr().use_cassette('test_volume_attachment_types.yml'):
        vcn_and_subnet = None
        volume_one = None
        volume_two = None
        instance = None

        iscsi_volume_attachment = None
        paravirtualized_volume_attachment = None

        try:
            vcn_and_subnet = create_vcn_and_subnet(virtual_network)
            volume_one = create_volume(block_storage, 'VolAttachTypesTest_Vol1')
            volume_two = create_volume(block_storage, 'VolAttachTypesTest_Vol2')
            instance = launch_instance(compute, vcn_and_subnet)

            iscsi_volume_attachment = attach_iscsi_volume(compute, volume_one, instance, 'VolAttachTypeTestIscsi')
            assert_volume_attachment(
                iscsi_volume_attachment,
                volume_one,
                instance,
                'VolAttachTypeTestIscsi',
                ['iscsi'],
                oci.core.models.IScsiVolumeAttachment
            )

            paravirtualized_volume_attachment = attach_paravirtualized_volume(compute, volume_two, instance, 'VolAttachTypeTestPara')
            assert_volume_attachment(
                paravirtualized_volume_attachment,
                volume_two,
                instance,
                'VolAttachTypeTestPara',
                ['paravirtualized'],
                oci.core.models.ParavirtualizedVolumeAttachment
            )

            volume_attachments = oci.pagination.list_call_get_all_results(
                compute.list_volume_attachments,
                util.COMPARTMENT_ID,
                instance_id=instance.id
            ).data

            volume_one_attachment = None
            volume_two_attachment = None
            for va in volume_attachments:
                if va.volume_id == volume_one.id:
                    volume_one_attachment = va
                elif va.volume_id == volume_two.id:
                    volume_two_attachment = va
            assert iscsi_volume_attachment == volume_one_attachment
            assert paravirtualized_volume_attachment == volume_two_attachment
        finally:
            if iscsi_volume_attachment:
                detach_volume(compute, iscsi_volume_attachment)

            if paravirtualized_volume_attachment:
                detach_volume(compute, paravirtualized_volume_attachment)

            if volume_one:
                delete_volume(block_storage, volume_one)

            if volume_two:
                delete_volume(block_storage, volume_two)

            if instance:
                terminate_instance(compute, instance)

            if vcn_and_subnet:
                delete_vcn_and_subnet(virtual_network, vcn_and_subnet)


def attach_iscsi_volume(compute, volume, instance, display_name):
    result = compute.attach_volume(
        oci.core.models.AttachIScsiVolumeDetails(
            display_name=display_name,
            instance_id=instance.id,
            volume_id=volume.id
        )
    )
    get_volume_attachment_response = test_config_container.do_wait(
        compute,
        compute.get_volume_attachment(result.data.id),
        'lifecycle_state',
        'ATTACHED'
    )
    return get_volume_attachment_response.data


def attach_paravirtualized_volume(compute, volume, instance, display_name):
    result = compute.attach_volume(
        oci.core.models.AttachParavirtualizedVolumeDetails(
            display_name=display_name,
            instance_id=instance.id,
            volume_id=volume.id
        )
    )
    get_volume_attachment_response = test_config_container.do_wait(
        compute,
        compute.get_volume_attachment(result.data.id),
        'lifecycle_state',
        'ATTACHED'
    )
    return get_volume_attachment_response.data


def assert_volume_attachment(volume_attachment, volume, instance, display_name, target_type_names, target_type_ref):
    assert isinstance(volume_attachment, target_type_ref)
    assert volume_attachment.attachment_type in target_type_names
    assert display_name == volume_attachment.display_name
    assert instance.id == volume_attachment.instance_id
    assert volume.id == volume_attachment.volume_id


def create_volume(block_storage, display_name):
    create_response = block_storage.create_volume(
        oci.core.models.CreateVolumeDetails(
            availability_domain=util.availability_domain(),
            compartment_id=util.COMPARTMENT_ID,
            display_name=display_name
        )
    )
    get_volume_response = test_config_container.do_wait(block_storage, block_storage.get_volume(create_response.data.id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

    return get_volume_response.data


def delete_volume(block_storage, volume):
    try:
        block_storage.delete_volume(volume.id)
        test_config_container.do_wait(block_storage, block_storage.get_volume(volume.id), 'lifecycle_state', 'TERMINATED', max_wait_seconds=300, succeed_on_not_found=True)
    except Exception as e:
        print('Error deleting volume: {}'.format(e))


def detach_volume(compute, volume_attachment):
    try:
        compute.detach_volume(volume_attachment.id)
        test_config_container.do_wait(
            compute,
            compute.get_volume_attachment(volume_attachment.id),
            'lifecycle_state',
            'DETACHED'
        )
    except Exception as e:
        print('Error detaching volume: {}'.format(e))


def create_vcn_and_subnet(virtual_network):
    # Create a VCN
    vcn_name = util.random_name('python_sdk_test_vol_attach_vcn')
    cidr_block = "10.0.0.0/16"

    create_vcn_details = oci.core.models.CreateVcnDetails(
        cidr_block=cidr_block,
        display_name=vcn_name,
        compartment_id=util.COMPARTMENT_ID
    )
    result = virtual_network.create_vcn(create_vcn_details)
    util.validate_response(result, expect_etag=True)

    vcn_ocid = result.data.id
    get_vcn_response = test_config_container.do_wait(virtual_network, virtual_network.get_vcn(vcn_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

    # Create a subnet
    subnet_name = util.random_name('python_sdk_test_lb_subnet')
    subnet_cidr_block = "10.0.0.0/24"

    create_subnet_details = oci.core.models.CreateSubnetDetails(
        compartment_id=util.COMPARTMENT_ID,
        availability_domain=util.availability_domain(),
        display_name=subnet_name,
        vcn_id=vcn_ocid,
        cidr_block=subnet_cidr_block
    )
    result = virtual_network.create_subnet(create_subnet_details)
    util.validate_response(result, expect_etag=True)

    subnet_ocid = result.data.id
    get_subnet_response = test_config_container.do_wait(virtual_network, virtual_network.get_subnet(subnet_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

    return {'vcn': get_vcn_response.data, 'subnet': get_subnet_response.data}


def delete_vcn_and_subnet(virtual_network, vcn_and_subnet):
    vcn = vcn_and_subnet['vcn']
    subnet = vcn_and_subnet['subnet']

    try:
        subnet_response = virtual_network.get_subnet(subnet.id)
        virtual_network.delete_subnet(subnet.id)
        test_config_container.do_wait(virtual_network, subnet_response, 'lifecycle_state', 'TERMINATED', max_wait_seconds=300, succeed_on_not_found=True)
    except Exception as e:
        print('Error deleting Subnet: {}'.format(e))

    try:
        vcn_response = virtual_network.get_vcn(vcn.id)
        virtual_network.delete_vcn(vcn.id)
        test_config_container.do_wait(virtual_network, vcn_response, 'lifecycle_state', 'TERMINATED', max_wait_seconds=300, succeed_on_not_found=True)
    except Exception as e:
        print('Error deleting VCN: {}'.format(e))


def launch_instance(compute, vcn_and_subnet):
    result = compute.launch_instance(
        oci.core.models.LaunchInstanceDetails(
            availability_domain=vcn_and_subnet['subnet'].availability_domain,
            compartment_id=vcn_and_subnet['subnet'].compartment_id,
            display_name='VolAttachTypesTestInstance',
            shape='VM.Standard1.1',
            subnet_id=vcn_and_subnet['subnet'].id,
            image_id=get_image(compute, 'Oracle Linux', '7.5', 'VM.Standard1.1').id
        )
    )
    get_instance_response = test_config_container.do_wait(
        compute,
        compute.get_instance(result.data.id),
        'lifecycle_state',
        'RUNNING',
        max_wait_seconds=300
    )

    return get_instance_response.data


def terminate_instance(compute, instance):
    try:
        compute.terminate_instance(instance.id)
        test_config_container.do_wait(
            compute,
            compute.get_instance(instance.id),
            'lifecycle_state',
            'TERMINATED',
            max_wait_seconds=300,
            succeed_on_not_found=True
        )
    except Exception as e:
        print('Error terminating instance: {}'.format(e))


def get_image(compute, operating_system, os_version, target_shape):
    images = oci.pagination.list_call_get_all_results(
        compute.list_images,
        util.COMPARTMENT_ID,
        operating_system=operating_system,
        operating_system_version=os_version
    ).data

    if len(images) == 0:
        raise RuntimeError('No valid images found for {} version {}'.format(operating_system, os_version))

    for img in images:
        shapes_for_image = oci.pagination.list_call_get_all_results(
            compute.list_shapes,
            util.COMPARTMENT_ID,
            image_id=img.id
        ).data

        for s in shapes_for_image:
            if s.shape == target_shape:
                return img

    raise RuntimeError('No valid image found for target OS, Version and Shape')
