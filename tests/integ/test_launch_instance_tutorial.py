import tests.util
import oraclebmc
import time
import pytest
from . import util


@util.slow
def test_tutorial(virtual_network, compute, block_storage, config):
    test_id = tests.util.random_number_string()
    print('Running Launching Your First Instance tutorial')
    print('Objects will have ID ' + test_id)

    # TODO DEX-17: Currently this test only runs against R2 and
    # if you have the private and public key files. We should be
    # getting these dynamically based on a specified environment.
    availability_domain = 'kIdk:PHX-AD-2'
    compartment = util.COMPARTMENT_ID

    with open(tests.util.get_key_file_path("public_ssh_key.pub")) as f:
        public_key = f.read().strip()

    vcn = None
    subnet = None
    instance = None
    volume = None
    attachment = None

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
        print('Exception during creation phase: ' + str(e))
        raise
    finally:
        if volume:
            if attachment:
                detach_volume(compute, attachment)
            delete_volume(block_storage, volume)
        if instance:
            terminate_instance(compute, instance)
        if subnet:
            delete_subnet(virtual_network, subnet)
        if vcn:
            delete_cloud_network(virtual_network, vcn)


def create_cloud_network(virtual_network, compartment, test_id):
    print('Creating cloud network')
    request = oraclebmc.core.models.CreateVcnDetails()
    request.cidr_block = '10.0.0.0/16'
    request.display_name = 'pythonsdk_test_vcn_' + test_id
    request.compartment_id = compartment

    response = virtual_network.create_vcn(request)

    assert response.status == 200
    assert type(response.data) is oraclebmc.core.models.Vcn

    response = virtual_network.get_vcn(response.data.id)
    vcn = oraclebmc.wait_until(
        virtual_network,
        response,
        'lifecycle_state',
        'AVAILABLE'
    ).data

    assert 'AVAILABLE' == vcn.lifecycle_state
    return vcn


def delete_cloud_network(virtual_network, vcn):
    print('Deleting vcn')
    response = virtual_network.delete_vcn(vcn.id)
    assert response.status == 204

    with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
        response = virtual_network.get_vcn(vcn.id)
        oraclebmc.wait_until(
            virtual_network,
            response,
            'lifecycle_state',
            'TERMINATED',
            max_wait_seconds=180
        )
    assert excinfo.value.status == 404


def create_subnet(virtual_network, compartment, test_id, availability_domain, vcn):
    print('Creating subnet')
    request = oraclebmc.core.models.CreateSubnetDetails()
    request.cidr_block = '10.0.0.0/16'
    request.availability_domain = availability_domain
    request.display_name = 'pythonsdk_test_subnet_' + test_id
    request.compartment_id = compartment
    request.route_table_id = vcn.default_route_table_id
    request.vcn_id = vcn.id
    response = virtual_network.create_subnet(request)

    assert response.status == 200
    assert type(response.data) is oraclebmc.core.models.Subnet

    response = virtual_network.get_subnet(response.data.id)
    subnet = oraclebmc.wait_until(
        virtual_network,
        response,
        'lifecycle_state',
        'AVAILABLE'
    ).data
    return subnet


def delete_subnet(virtual_network, subnet):
    print('Deleting subnet')
    response = virtual_network.delete_subnet(subnet.id)
    assert response.status == 204

    with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
        response = virtual_network.get_subnet(subnet.id)
        oraclebmc.wait_until(
            virtual_network,
            response,
            'lifecycle_state',
            'TERMINATED'
        )
    assert excinfo.value.status == 404


def create_internet_gateway(virtual_network, compartment, test_id, vcn):
    print('Creating internet gateway')
    request = oraclebmc.core.models.CreateInternetGatewayDetails()
    request.display_name = 'pythonsdk_test_ig_' + test_id
    request.compartment_id = compartment
    request.is_enabled = True
    request.vcn_id = vcn.id
    response = virtual_network.create_internet_gateway(request)

    assert response.status == 200
    assert type(response.data) is oraclebmc.core.models.InternetGateway

    response = virtual_network.get_internet_gateway(response.data.id)
    gateway = oraclebmc.wait_until(
        virtual_network,
        response,
        'lifecycle_state',
        'AVAILABLE'
    ).data

    return gateway


def update_route_table(virtual_network, test_id, vcn, gateway):
    print('Updating route table')
    route_rule = oraclebmc.core.models.RouteRule()
    route_rule.cidr_block = '0.0.0.0/0'
    route_rule.display_name = 'pythonsdk_route_rule_' + test_id
    route_rule.network_entity_id = gateway.id
    route_rule.network_entity_type = 'INTERNET_GATEWAY'

    request = oraclebmc.core.models.UpdateRouteTableDetails()
    request.route_rules = [route_rule]
    response = virtual_network.update_route_table(vcn.default_route_table_id, request)

    assert response.status == 200
    assert type(response.data) is oraclebmc.core.models.RouteTable

    response = virtual_network.get_route_table(vcn.default_route_table_id)
    oraclebmc.wait_until(virtual_network, response, 'lifecycle_state', 'AVAILABLE')


def launch_instance(compute, compartment, test_id, availability_domain, subnet, public_key):
    print('Launching instance')

    request = oraclebmc.core.models.LaunchInstanceDetails()
    request.availability_domain = availability_domain
    request.compartment_id = compartment
    request.display_name = 'pythonsdk_tutorial_instance_' + test_id
    # ol7.1-base-0.0.1
    request.image_id = 'ocid1.image.oc1.phx.aaaaaaaa4wdx32cwjdjdasqyzatmvlxbef4673rs5y7cowvc3g3o7iwhmhfa'
    request.shape = 'x5-2.36.256'
    request.subnet_id = subnet.id
    request.metadata = {'ssh_authorized_keys': public_key}
    response = compute.launch_instance(request)

    assert response.status == 200
    assert 'PROVISIONING' == response.data.lifecycle_state

    response = compute.get_instance(response.data.id)
    instance = oraclebmc.wait_until(
        compute,
        response,
        'lifecycle_state',
        'RUNNING',
        max_wait_seconds=300
    ).data

    assert 'RUNNING' == instance.lifecycle_state
    return instance


def terminate_instance(compute, instance):
    print('Terminating instance')
    response = compute.terminate_instance(instance.id)
    assert response.status == 204

    response = compute.get_instance(instance.id)
    oraclebmc.wait_until(compute, response, 'lifecycle_state', 'TERMINATED')


def create_volume(block_storage, compartment, test_id, availability_domain):
    print('Creating volume')
    request = oraclebmc.core.models.CreateVolumeDetails()
    request.display_name = 'pythonsdk_volume_' + test_id
    request.compartment_id = compartment
    request.availability_domain = availability_domain
    response = block_storage.create_volume(
        request, opc_retry_token='testtoken' + test_id)

    assert response.status == 200
    assert type(response.data) is oraclebmc.core.models.Volume

    response = block_storage.get_volume(response.data.id)
    volume = oraclebmc.wait_until(
        block_storage,
        response,
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=180
    ).data
    return volume


def delete_volume(block_storage, volume):
    print('Deleting volume')
    response = block_storage.delete_volume(volume.id)
    assert response.status == 204

    response = block_storage.get_volume(volume.id)
    oraclebmc.wait_until(
        block_storage,
        response,
        'lifecycle_state',
        'TERMINATED',
        max_wait_seconds=180
    )


def log_public_ip_address(compute, virtual_network, compartment, instance):
    print('Getting public IP address')
    response = compute.list_vnic_attachments(
        compartment, instance_id=instance.id)
    assert response.status == 200
    assert len(response.data) > 0

    vnic_attachment = next(va for va in response.data if va.instance_id == instance.id)

    # Just get the address for the first vnic attachment.
    response = virtual_network.get_vnic(vnic_attachment.vnic_id)
    response = oraclebmc.wait_until(
        virtual_network,
        response,
        'lifecycle_state',
        'AVAILABLE'
    )
    assert response.status == 200
    assert response.data.public_ip is not None
    print('Public IP Address: ' + response.data.public_ip)


def attach_volume(compute, compartment, instance, volume):
    print('Attaching volume')
    request = oraclebmc.core.models.AttachIScsiVolumeDetails()
    request.compartment_id = compartment
    request.instance_id = instance.id
    request.volume_id = volume.id
    response = compute.attach_volume(request)

    assert response.status == 200
    assert type(response.data) is oraclebmc.core.models.IScsiVolumeAttachment

    response = compute.get_volume_attachment(response.data.id)
    attachment = oraclebmc.wait_until(
        compute,
        response,
        'lifecycle_state',
        'ATTACHED'
    ).data
    return attachment


def detach_volume(compute, attachment):
    print('Detaching volume')
    response = compute.detach_volume(attachment.id)
    assert response.status == 204

    response = compute.get_volume_attachment(attachment.id)
    oraclebmc.wait_until(compute, response, 'lifecycle_state', 'DETACHED')
