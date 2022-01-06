# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import tests.util
import oci
import os
import time
import pytest

from . import util
from .. import test_config_container


def test_tutorial(virtual_network, compute, block_storage, config):
    test_id = tests.util.random_number_string()
    # print('Running Launching Your First Instance tutorial')
    # print('Objects will have ID ' + test_id)

    availability_domain = util.availability_domain()
    compartment = config["tenancy"]

    ssh_file = os.environ['OCI_PYSDK_PUBLIC_SSH_KEY_FILE']
    with open(ssh_file) as f:
        public_key = f.read().strip()

    vcn = None
    subnet = None
    instance = None
    volume = None
    attachment = None

    with test_config_container.create_vcr().use_cassette('launch_instance_tutorial.yml'):
        try:
            vcn = create_cloud_network(virtual_network, compartment, test_id)
            subnet = create_subnet(virtual_network, compartment, test_id, availability_domain, vcn)
            gateway = create_internet_gateway(virtual_network, compartment, test_id, vcn)
            update_route_table(virtual_network, test_id, vcn, gateway)

            # There's a bug where the instance will immediately terminate if we
            # don't add some extra wait time before launching. (COM-79)
            time.sleep(15)

            instance = launch_instance(
                compute, compartment, test_id, availability_domain, subnet, public_key)
            log_public_ip_address(compute, virtual_network, compartment, instance)

            volume = create_volume(block_storage, compartment, test_id, availability_domain)
            attachment = attach_volume(compute, compartment, instance, volume)
        except Exception as e:
            # print('Exception during creation phase: ' + str(e))
            raise e
        finally:
            if volume:
                if attachment:
                    detach_volume(compute, attachment)
                delete_volume(block_storage, volume)
            if instance:
                terminate_instance(compute, instance)
            if subnet:
                delete_subnet(virtual_network, subnet)
            if gateway:
                # Clear the route table so it does not have a reference to the internet gateway
                virtual_network.update_route_table(vcn.default_route_table_id, oci.core.models.UpdateRouteTableDetails(route_rules=[]))
                delete_internet_gateway(virtual_network, gateway.id)
            if vcn:
                delete_cloud_network(virtual_network, vcn)


def create_cloud_network(virtual_network, compartment, test_id):
    # print('Creating cloud network')
    request = oci.core.models.CreateVcnDetails()
    request.cidr_block = '10.0.0.0/16'
    request.display_name = 'pythonsdk_test_vcn_' + test_id
    request.compartment_id = compartment

    response = virtual_network.create_vcn(request)

    assert response.status == 200
    assert type(response.data) is oci.core.models.Vcn

    response = virtual_network.get_vcn(response.data.id)
    vcn = test_config_container.do_wait(virtual_network, response, 'lifecycle_state', 'AVAILABLE').data

    assert 'AVAILABLE' == vcn.lifecycle_state
    return vcn


def delete_cloud_network(virtual_network, vcn):
    # print('Deleting vcn')
    response = virtual_network.delete_vcn(vcn.id)
    assert response.status == 204

    with pytest.raises(oci.exceptions.ServiceError) as excinfo:
        response = virtual_network.get_vcn(vcn.id)
        test_config_container.do_wait(
            virtual_network,
            response,
            'lifecycle_state',
            'TERMINATED',
            max_wait_seconds=180
        )
    assert excinfo.value.status == 404


def create_subnet(virtual_network, compartment, test_id, availability_domain, vcn):
    # print('Creating subnet')
    request = oci.core.models.CreateSubnetDetails()
    request.cidr_block = '10.0.0.0/16'
    request.availability_domain = availability_domain
    request.display_name = 'pythonsdk_test_subnet_' + test_id
    request.compartment_id = compartment
    request.route_table_id = vcn.default_route_table_id
    request.vcn_id = vcn.id
    response = virtual_network.create_subnet(request)

    assert response.status == 200
    assert type(response.data) is oci.core.models.Subnet

    response = virtual_network.get_subnet(response.data.id)
    subnet = test_config_container.do_wait(
        virtual_network,
        response,
        'lifecycle_state',
        'AVAILABLE'
    ).data
    return subnet


def delete_subnet(virtual_network, subnet):
    # print('Deleting subnet')
    response = virtual_network.delete_subnet(subnet.id)
    assert response.status == 204

    with pytest.raises(oci.exceptions.ServiceError) as excinfo:
        response = virtual_network.get_subnet(subnet.id)
        test_config_container.do_wait(
            virtual_network,
            response,
            'lifecycle_state',
            'TERMINATED'
        )
    assert excinfo.value.status == 404


def create_internet_gateway(virtual_network, compartment, test_id, vcn):
    # print('Creating internet gateway')
    request = oci.core.models.CreateInternetGatewayDetails()
    request.display_name = 'pythonsdk_test_ig_' + test_id
    request.compartment_id = compartment
    request.is_enabled = True
    request.vcn_id = vcn.id
    response = virtual_network.create_internet_gateway(request)

    assert response.status == 200
    assert type(response.data) is oci.core.models.InternetGateway

    response = virtual_network.get_internet_gateway(response.data.id)
    gateway = test_config_container.do_wait(
        virtual_network,
        response,
        'lifecycle_state',
        'AVAILABLE'
    ).data

    return gateway


def delete_internet_gateway(virtual_network, gateway_id):
    vcn_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)
    vcn_composite_ops.delete_internet_gateway_and_wait_for_state(gateway_id, wait_for_states=[oci.core.models.InternetGateway.LIFECYCLE_STATE_TERMINATED])


def update_route_table(virtual_network, test_id, vcn, gateway):
    # print('Updating route table')
    route_rule = oci.core.models.RouteRule()
    route_rule.cidr_block = None
    route_rule.destination = '0.0.0.0/0'
    route_rule.destination_type = 'CIDR_BLOCK'
    route_rule.display_name = 'pythonsdk_route_rule_' + test_id
    route_rule.network_entity_id = gateway.id
    route_rule.network_entity_type = 'INTERNET_GATEWAY'

    request = oci.core.models.UpdateRouteTableDetails()
    request.route_rules = [route_rule]
    response = virtual_network.update_route_table(vcn.default_route_table_id, request)

    assert response.status == 200
    assert type(response.data) is oci.core.models.RouteTable

    response = virtual_network.get_route_table(vcn.default_route_table_id)
    test_config_container.do_wait(virtual_network, response, 'lifecycle_state', 'AVAILABLE')


def launch_instance(compute, compartment, test_id, availability_domain, subnet, public_key):
    # print('Launching instance')

    request = oci.core.models.LaunchInstanceDetails()
    request.availability_domain = availability_domain
    request.compartment_id = compartment
    request.display_name = 'pythonsdk_tutorial_instance_' + test_id
    # Oracle-Linux-7.3-2017.03.03-0
    request.image_id = util.oracle_linux_image()
    request.shape = 'VM.Standard1.1'
    request.subnet_id = subnet.id
    request.metadata = {'ssh_authorized_keys': public_key}
    response = compute.launch_instance(request)

    assert response.status == 200
    assert 'PROVISIONING' == response.data.lifecycle_state

    response = compute.get_instance(response.data.id)
    instance = test_config_container.do_wait(
        compute,
        response,
        'lifecycle_state',
        'RUNNING',
        max_wait_seconds=300
    ).data

    assert 'RUNNING' == instance.lifecycle_state
    return instance


def terminate_instance(compute, instance):
    # print('Terminating instance')
    response = compute.terminate_instance(instance.id)
    assert response.status == 204

    response = compute.get_instance(instance.id)
    test_config_container.do_wait(compute, response, 'lifecycle_state', 'TERMINATED')


def create_volume(block_storage, compartment, test_id, availability_domain):
    # print('Creating volume')
    request = oci.core.models.CreateVolumeDetails()
    request.display_name = 'pythonsdk_volume_' + test_id
    request.compartment_id = compartment
    request.availability_domain = availability_domain
    response = block_storage.create_volume(
        request, opc_retry_token='testtoken{}'.format(int(time.time())))

    assert response.status == 200
    assert type(response.data) is oci.core.models.Volume

    response = block_storage.get_volume(response.data.id)
    volume = test_config_container.do_wait(
        block_storage,
        response,
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=180
    ).data
    return volume


def delete_volume(block_storage, volume):
    # print('Deleting volume')
    response = block_storage.delete_volume(volume.id)
    assert response.status == 204

    response = block_storage.get_volume(volume.id)
    test_config_container.do_wait(
        block_storage,
        response,
        'lifecycle_state',
        'TERMINATED',
        max_wait_seconds=180
    )


def log_public_ip_address(compute, virtual_network, compartment, instance):
    # print('Getting public IP address')
    response = compute.list_vnic_attachments(
        compartment, instance_id=instance.id)
    assert response.status == 200
    assert len(response.data) > 0

    vnic_attachment = next(va for va in response.data if va.instance_id == instance.id)

    # Just get the address for the first vnic attachment.
    response = virtual_network.get_vnic(vnic_attachment.vnic_id)
    response = test_config_container.do_wait(
        virtual_network,
        response,
        'lifecycle_state',
        'AVAILABLE'
    )
    assert response.status == 200
    assert response.data.public_ip is not None
    # print('Public IP Address: ' + response.data.public_ip)


def attach_volume(compute, compartment, instance, volume):
    # print('Attaching volume')
    request = oci.core.models.AttachIScsiVolumeDetails()
    request.compartment_id = compartment
    request.instance_id = instance.id
    request.volume_id = volume.id
    response = compute.attach_volume(request)

    assert response.status == 200
    assert type(response.data) is oci.core.models.IScsiVolumeAttachment

    response = compute.get_volume_attachment(response.data.id)
    attachment = test_config_container.do_wait(
        compute,
        response,
        'lifecycle_state',
        'ATTACHED'
    ).data
    return attachment


def detach_volume(compute, attachment):
    # print('Detaching volume')
    response = compute.detach_volume(attachment.id)
    assert response.status == 204

    response = compute.get_volume_attachment(attachment.id)
    test_config_container.do_wait(compute, response, 'lifecycle_state', 'DETACHED')
