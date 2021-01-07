# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Basic sanity tests for each exposed composite operation class

import oci

from . import util
from .. import test_config_container


def test_block_storage_composite_operations(block_storage):
    with test_config_container.create_vcr().use_cassette('test_block_storage_composite_operations.yml'):
        block_storage_service_helper = oci.core.BlockstorageClientCompositeOperations(block_storage)

        get_response = block_storage_service_helper.create_volume_and_wait_for_state(
            oci.core.models.CreateVolumeDetails(
                display_name=util.random_name('service_helper_test'),
                size_in_gbs=50,
                availability_domain=util.availability_domain(),
                compartment_id=util.COMPARTMENT_ID
            ),
            wait_for_states=[oci.core.models.Volume.LIFECYCLE_STATE_AVAILABLE]
        )
        assert get_response.data.id
        assert get_response.data.size_in_gbs == 50
        assert get_response.data.availability_domain == util.availability_domain()
        assert get_response.data.compartment_id == util.COMPARTMENT_ID
        assert get_response.data.lifecycle_state == oci.core.models.Volume.LIFECYCLE_STATE_AVAILABLE

        delete_response = block_storage_service_helper.delete_volume_and_wait_for_state(
            get_response.data.id,
            wait_for_states=[oci.core.models.Volume.LIFECYCLE_STATE_TERMINATED]
        )
        if delete_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
            assert delete_response.data.lifecycle_state == oci.core.models.Volume.LIFECYCLE_STATE_TERMINATED


def test_compute_and_vcn_composite_operations(compute, virtual_network):
    with test_config_container.create_vcr().use_cassette('test_compute_and_vcn_composite_operations.yml'):
        vcn_id = None
        subnet_id = None
        instance_id = None

        compute_service_helper = oci.core.ComputeClientCompositeOperations(compute)
        virtual_network_service_helper = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)

        try:
            get_vcn_response = virtual_network_service_helper.create_vcn_and_wait_for_state(
                oci.core.models.CreateVcnDetails(
                    display_name=util.random_name('python_sdk_test_compute_vcn'),
                    compartment_id=util.COMPARTMENT_ID,
                    cidr_block="10.0.0.0/16"
                ),
                wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE]
            )
            vcn_id = get_vcn_response.data.id
            assert get_vcn_response.data.id
            assert get_vcn_response.data.compartment_id == util.COMPARTMENT_ID
            assert get_vcn_response.data.lifecycle_state == oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE

            get_subnet_response = virtual_network_service_helper.create_subnet_and_wait_for_state(
                oci.core.models.CreateSubnetDetails(
                    compartment_id=util.COMPARTMENT_ID,
                    availability_domain=util.availability_domain(),
                    display_name=util.random_name('python_sdk_test_compute_subnet'),
                    vcn_id=vcn_id,
                    cidr_block="10.0.0.0/16"
                ),
                wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE]
            )
            subnet_id = get_subnet_response.data.id
            assert get_subnet_response.data.id
            assert get_subnet_response.data.compartment_id == util.COMPARTMENT_ID
            assert get_subnet_response.data.availability_domain == util.availability_domain()
            assert get_subnet_response.data.vcn_id == vcn_id
            assert get_subnet_response.data.lifecycle_state == oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE

            get_instance_response = compute_service_helper.launch_instance_and_wait_for_state(
                oci.core.models.LaunchInstanceDetails(
                    image_id=util.oracle_linux_image(),
                    shape='VM.Standard1.1',
                    compartment_id=util.COMPARTMENT_ID,
                    availability_domain=get_subnet_response.data.availability_domain,
                    display_name=util.random_name('python_sdk_test_instance'),
                    subnet_id=subnet_id
                ),
                wait_for_states=[oci.core.models.Instance.LIFECYCLE_STATE_RUNNING]
            )
            instance_id = get_instance_response.data.id
            assert get_instance_response.data.id
            assert get_instance_response.data.compartment_id == util.COMPARTMENT_ID
            assert get_instance_response.data.availability_domain == get_subnet_response.data.availability_domain
            assert get_instance_response.data.lifecycle_state == oci.core.models.Instance.LIFECYCLE_STATE_RUNNING
        finally:
            if instance_id:
                terminate_instance_response = compute_service_helper.terminate_instance_and_wait_for_state(
                    instance_id,
                    wait_for_states=[oci.core.models.Instance.LIFECYCLE_STATE_TERMINATED]
                )
                if terminate_instance_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
                    assert terminate_instance_response.data.lifecycle_state == oci.core.models.Instance.LIFECYCLE_STATE_TERMINATED

            if subnet_id:
                delete_subnet_response = virtual_network_service_helper.delete_subnet_and_wait_for_state(
                    subnet_id,
                    wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
                )
                if delete_subnet_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
                    assert delete_subnet_response.data.lifecycle_state == oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED

            if vcn_id:
                delete_vcn_response = virtual_network_service_helper.delete_vcn_and_wait_for_state(
                    vcn_id,
                    wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
                )
                if delete_vcn_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
                    assert delete_vcn_response.data.lifecycle_state == oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED


def test_dns_composite_operations(dns_client):
    with test_config_container.create_vcr().use_cassette('test_dns_composite_operations.yml'):
        dns_service_helper = oci.dns.DnsClientCompositeOperations(dns_client)

        zone_name = '{}.com'.format(util.random_name('python-sdk-svc-helper-testing-', insert_underscore=False))
        create_zone_details = oci.dns.models.CreateZoneDetails(
            name=zone_name,
            zone_type='PRIMARY',
            compartment_id=util.COMPARTMENT_ID
        )

        get_dns_response = dns_service_helper.create_zone_and_wait_for_state(
            create_zone_details,
            wait_for_states=[oci.dns.models.Zone.LIFECYCLE_STATE_ACTIVE]
        )
        assert get_dns_response.data.name == zone_name
        assert get_dns_response.data.lifecycle_state == oci.dns.models.Zone.LIFECYCLE_STATE_ACTIVE

        delete_response = dns_service_helper.delete_zone_and_wait_for_state(
            zone_name,
            wait_for_states=[oci.dns.models.Zone.LIFECYCLE_STATE_DELETED]
        )
        if delete_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
            assert delete_response.data.lifecycle_state == oci.dns.models.Zone.LIFECYCLE_STATE_DELETED


def test_email_composite_operations(email_client):
    with test_config_container.create_vcr().use_cassette('test_email_composite_operations.yml'):
        email_service_helper = oci.email.EmailClientCompositeOperations(email_client)

        email_address = 'svc-helper-test@pythonsdktesting.com'

        get_sender_response = email_service_helper.create_sender_and_wait_for_state(
            oci.email.models.CreateSenderDetails(
                compartment_id=util.COMPARTMENT_ID,
                email_address=email_address
            ),
            wait_for_states=[oci.email.models.Sender.LIFECYCLE_STATE_ACTIVE]
        )
        assert get_sender_response.data.id
        assert get_sender_response.data.email_address == email_address
        assert get_sender_response.data.lifecycle_state == oci.email.models.Sender.LIFECYCLE_STATE_ACTIVE

        delete_response = email_service_helper.delete_sender_and_wait_for_state(
            get_sender_response.data.id,
            wait_for_states=[oci.email.models.Sender.LIFECYCLE_STATE_DELETED]
        )
        if delete_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
            assert delete_response.data.lifecycle_state == oci.email.models.Sender.LIFECYCLE_STATE_DELETED


def test_file_storage_composite_operations(file_storage_client):
    with test_config_container.create_vcr().use_cassette('test_file_storage_composite_operations.yml'):
        file_storage_helper = oci.file_storage.FileStorageClientCompositeOperations(file_storage_client)

        get_file_system_response = file_storage_helper.create_file_system_and_wait_for_state(
            oci.file_storage.models.CreateFileSystemDetails(
                display_name=util.random_name('pysdk_test_fs'),
                compartment_id=util.COMPARTMENT_ID,
                availability_domain=util.availability_domain()
            ),
            wait_for_states=[oci.file_storage.models.FileSystem.LIFECYCLE_STATE_ACTIVE]
        )
        assert get_file_system_response.data.id
        assert get_file_system_response.data.compartment_id == util.COMPARTMENT_ID
        assert get_file_system_response.data.availability_domain == util.availability_domain()
        assert get_file_system_response.data.lifecycle_state == oci.file_storage.models.FileSystem.LIFECYCLE_STATE_ACTIVE

        delete_response = file_storage_helper.delete_file_system_and_wait_for_state(
            get_file_system_response.data.id,
            wait_for_states=[oci.file_storage.models.FileSystem.LIFECYCLE_STATE_DELETED]
        )
        if delete_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
            assert delete_response.data.lifecycle_state == oci.file_storage.models.FileSystem.LIFECYCLE_STATE_DELETED


def test_identity_composite_operations(identity, config):
    with test_config_container.create_vcr().use_cassette('test_identity_composite_operations.yml'):
        identity_service_helper = oci.identity.IdentityClientCompositeOperations(identity)

        group_name = util.random_name('python_sdk_svc_helper_test_group')
        get_group_response = identity_service_helper.create_group_and_wait_for_state(
            oci.identity.models.CreateGroupDetails(
                name=group_name,
                description='Python SDK Service Helper test group',
                compartment_id=config['tenancy']
            ),
            wait_for_states=[oci.identity.models.Group.LIFECYCLE_STATE_ACTIVE]
        )
        assert get_group_response.data.id
        assert get_group_response.data.name == group_name
        assert get_group_response.data.compartment_id == config['tenancy']
        assert get_group_response.data.description == 'Python SDK Service Helper test group'

        delete_response = identity_service_helper.delete_group_and_wait_for_state(
            get_group_response.data.id,
            wait_for_states=[oci.identity.models.Group.LIFECYCLE_STATE_DELETED]
        )
        if delete_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
            assert delete_response.data.lifecycle_state == oci.identity.models.Group.LIFECYCLE_STATE_DELETED


def test_load_balancer_composite_operations(load_balancer_client, virtual_network):
    with test_config_container.create_vcr().use_cassette('test_load_balancer_composite_operations.yml'):
        lb_service_helper = oci.load_balancer.LoadBalancerClientCompositeOperations(load_balancer_client)
        virtual_network_service_helper = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)

        vcn_id = None
        subnet_one_id = None
        subnet_two_id = None

        try:
            get_vcn_response = virtual_network_service_helper.create_vcn_and_wait_for_state(
                oci.core.models.CreateVcnDetails(
                    display_name=util.random_name('python_sdk_test_compute_vcn'),
                    compartment_id=util.COMPARTMENT_ID,
                    cidr_block="10.0.0.0/16"
                ),
                wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE]
            )
            vcn_id = get_vcn_response.data.id
            assert get_vcn_response.data.id
            assert get_vcn_response.data.compartment_id == util.COMPARTMENT_ID
            assert get_vcn_response.data.lifecycle_state == oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE

            get_subnet_response = virtual_network_service_helper.create_subnet_and_wait_for_state(
                oci.core.models.CreateSubnetDetails(
                    compartment_id=util.COMPARTMENT_ID,
                    availability_domain=util.availability_domain(),
                    display_name=util.random_name('python_sdk_test_compute_subnet'),
                    vcn_id=vcn_id,
                    cidr_block="10.0.0.0/24"
                ),
                wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE]
            )
            subnet_one_id = get_subnet_response.data.id
            assert get_subnet_response.data.id
            assert get_subnet_response.data.compartment_id == util.COMPARTMENT_ID
            assert get_subnet_response.data.availability_domain == util.availability_domain()
            assert get_subnet_response.data.vcn_id == vcn_id
            assert get_subnet_response.data.lifecycle_state == oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE

            get_subnet_response = virtual_network_service_helper.create_subnet_and_wait_for_state(
                oci.core.models.CreateSubnetDetails(
                    compartment_id=util.COMPARTMENT_ID,
                    availability_domain=util.second_availability_domain(),
                    display_name=util.random_name('python_sdk_test_compute_subnet'),
                    vcn_id=vcn_id,
                    cidr_block="10.0.1.0/24"
                ),
                wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE]
            )
            subnet_two_id = get_subnet_response.data.id
            assert get_subnet_response.data.id
            assert get_subnet_response.data.compartment_id == util.COMPARTMENT_ID
            assert get_subnet_response.data.availability_domain == util.second_availability_domain()
            assert get_subnet_response.data.vcn_id == vcn_id
            assert get_subnet_response.data.lifecycle_state == oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE

            get_load_balancer_response = lb_service_helper.create_load_balancer_and_wait_for_state(
                oci.load_balancer.models.CreateLoadBalancerDetails(
                    compartment_id=util.COMPARTMENT_ID,
                    display_name='Python SDK Service Helper Test',
                    shape_name='100Mbps',
                    subnet_ids=[subnet_one_id, subnet_two_id]
                ),
                wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
            )
            assert get_load_balancer_response.data.id
            assert get_load_balancer_response.data.display_name == 'Python SDK Service Helper Test'
            assert get_load_balancer_response.data.compartment_id == util.COMPARTMENT_ID
            assert get_load_balancer_response.data.shape_name == '100Mbps'
            assert set(get_load_balancer_response.data.subnet_ids) == set([subnet_one_id, subnet_two_id])
            assert get_load_balancer_response.data.lifecycle_state == oci.load_balancer.models.LoadBalancer.LIFECYCLE_STATE_ACTIVE

            delete_load_balancer_response = lb_service_helper.delete_load_balancer_and_wait_for_state(
                get_load_balancer_response.data.id,
                wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
            )
            assert delete_load_balancer_response.data.id
            assert delete_load_balancer_response.data.load_balancer_id == get_load_balancer_response.data.id
            assert delete_load_balancer_response.data.lifecycle_state == oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED
        finally:
            if subnet_one_id:
                delete_subnet_response = virtual_network_service_helper.delete_subnet_and_wait_for_state(
                    subnet_one_id,
                    wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
                )
                if delete_subnet_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
                    assert delete_subnet_response.data.lifecycle_state == oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED

            if subnet_two_id:
                delete_subnet_response = virtual_network_service_helper.delete_subnet_and_wait_for_state(
                    subnet_two_id,
                    wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
                )
                if delete_subnet_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
                    assert delete_subnet_response.data.lifecycle_state == oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED

            if vcn_id:
                delete_vcn_response = virtual_network_service_helper.delete_vcn_and_wait_for_state(
                    vcn_id,
                    wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
                )
                if delete_vcn_response is not oci.waiter.WAIT_RESOURCE_NOT_FOUND:
                    assert delete_vcn_response.data.lifecycle_state == oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED
