# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example of how use the instance pools CLI in terms of:
#   - Creating an instance configuration to be used for pool
#   - Creating an instance pool
#   - Wait for the pool to go to Running
#   - Updating instance pool size
#   - Wait for the pool to go to Running
#   - Attaching a load balancer to the pool
#   - Wait for the load balancer to become attached
#   - Get LB attachment info
#   - Terminating instance pool
#   - Deleting the instance configuration
#

import oci
import argparse
from oci.core import ComputeManagementClient
from oci.core import ComputeManagementClientCompositeOperations
from oci.core.models import CreateInstanceConfigurationDetails, \
    InstanceConfigurationLaunchInstanceDetails, \
    InstanceConfigurationInstanceSourceViaImageDetails, \
    InstanceConfigurationCreateVnicDetails, \
    ComputeInstanceDetails, \
    InstanceConfigurationBlockVolumeDetails, \
    InstanceConfigurationCreateVolumeDetails, \
    InstanceConfigurationParavirtualizedAttachVolumeDetails, \
    CreateInstancePoolDetails, \
    CreateInstancePoolPlacementConfigurationDetails, \
    UpdateInstancePoolDetails, \
    AttachLoadBalancerDetails


def _create_block_volume_details(compartment_id, ad):
    """Sets up the model for a simple 50gb BV for use by tests.
    :returns: InstanceConfigurationBlockVolumeDetails
    """
    block_volume_details = InstanceConfigurationBlockVolumeDetails()

    create_volume_details = InstanceConfigurationCreateVolumeDetails()
    create_volume_details.display_name = "blockvol1"
    create_volume_details.compartment_id = compartment_id
    create_volume_details.size_in_gbs = 50
    create_volume_details.availability_domain = ad

    volume_attach_details = InstanceConfigurationParavirtualizedAttachVolumeDetails()

    block_volume_details.create_details = create_volume_details
    block_volume_details.attach_details = volume_attach_details
    return block_volume_details


def _wait_until_lb_becomes_attached(cim_client, instance_pool_id):
    try:
        oci.wait_until(
            cim_client,
            cim_client.get_instance_pool(instance_pool_id),
            evaluate_response=(
                lambda r: r.data.load_balancers[0].lifecycle_state.upper() == "ATTACHED"),
            max_wait_seconds=6000)
        print("Load balancer attached to instance pool")
    except Exception:
        print("LB could not be attached!")
        raise


def _delete_tag_defaults(identity_client, compartment_id):
    tag_default_list = identity_client.list_tag_defaults(compartment_id=compartment_id).data
    for tag_default in tag_default_list:
        identity_client.delete_tag_default(tag_default.id)


#  === Main ===

if __name__ == "__main__":

    # Load the default configuration
    config = oci.config.from_file()

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--compartment-id',
                        help='Your compartment OCID',
                        required=True
                        )
    parser.add_argument('--availability-domain',
                        help='the AD where the pool will be spun up (the pool in this example only spans a single AD)',
                        required=True
                        )

    parser.add_argument('--subnet-id',
                        help='the ',
                        required=True
                        )

    parser.add_argument('--image-id',
                        help='the image ID to use for instances',
                        required=True
                        )

    parser.add_argument('--load-balancer-id',
                        help='The load balancer ID to use for the pool.',
                        required=True
                        )

    parser.add_argument('--lb-backendset-name',
                        help='The backendset name in the load balancer that is being attached.',
                        required=True
                        )

    args = parser.parse_args()

    # create the compute management client
    compute_management_client = ComputeManagementClient(config)
    composite_client = ComputeManagementClientCompositeOperations(compute_management_client)

    identity_client = oci.identity.IdentityClient(config)
    # disable tag defaults
    _delete_tag_defaults(identity_client, args.compartment_id)

    launch_details = InstanceConfigurationLaunchInstanceDetails(
        compartment_id=args.compartment_id,
        display_name="some instance name",
        shape="VM.Standard2.1",
        source_details=InstanceConfigurationInstanceSourceViaImageDetails(
            image_id=args.image_id
        ),
        create_vnic_details=InstanceConfigurationCreateVnicDetails()
    )

    instance_details = ComputeInstanceDetails(
        launch_details=launch_details,
        block_volumes=[
            _create_block_volume_details(args.compartment_id, args.availability_domain)
        ])

    create_instance_config_details = CreateInstanceConfigurationDetails(
        display_name="sample instance config name",
        compartment_id=args.compartment_id,
        instance_details=instance_details)

    try:
        # Creates and instance configuration to use with pool
        instance_config = compute_management_client.create_instance_configuration(
            create_instance_config_details).data
        print("Created instanceConfiguration: ", instance_config)

        # Creates a placement configuration to be used when creating a pool
        placement_config = \
            CreateInstancePoolPlacementConfigurationDetails()
        placement_config.availability_domain = args.availability_domain
        placement_config.primary_subnet_id = args.subnet_id

        create_instance_pool_details = CreateInstancePoolDetails(
            compartment_id=args.compartment_id,
            display_name="sample instance pool",
            instance_configuration_id=instance_config.id,
            placement_configurations=[placement_config],
            size=1)

        # Create a pool with initial size of 1.
        print("Creating instancePool: ", create_instance_pool_details)
        instance_pool = composite_client.create_instance_pool_and_wait_for_state(
            create_instance_pool_details, wait_for_states=["RUNNING"]).data

        print("Created instance pool: ", instance_pool)

        # updating the size of the pool to 2
        update_details = UpdateInstancePoolDetails(size=2)
        composite_client.update_instance_pool_and_wait_for_state(instance_pool.id, update_details,
                                                                 wait_for_states=["RUNNING"])

        # attach the load balancer to the pool
        attach_lb_details = AttachLoadBalancerDetails()
        attach_lb_details.load_balancer_id = args.load_balancer_id
        attach_lb_details.backend_set_name = args.lb_backendset_name
        attach_lb_details.port = 80
        attach_lb_details.vnic_selection = "PrimaryVnic"

        compute_management_client.attach_load_balancer(instance_pool.id, attach_lb_details)

        # wait until the load balancer becomes attached
        _wait_until_lb_becomes_attached(compute_management_client, instance_pool.id)

        # perform a get to refresh pool info and get the lb attachment ID
        instance_pool = compute_management_client.get_instance_pool(instance_pool.id).data

        # get lb attachment info
        lb_attachment_info = compute_management_client.get_instance_pool_load_balancer_attachment(
            instance_pool.id,
            instance_pool.load_balancers[0].id).data

        print("Lb attachment: ", lb_attachment_info)

    finally:
        # cleaning up created resources
        compute_management_client.terminate_instance_pool(instance_pool.id)
        print("Terminated instance pool: ", instance_pool)

        compute_management_client.delete_instance_configuration(instance_config.id)
        print("Deleted instanceConfiguration: ", instance_config)
