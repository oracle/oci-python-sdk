# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides an example of how use the cluster networks SDK in terms of:
#   - Creating an Instance Configuration
#   - Create a Cluster Network based on that configuration.
#   - Wait for the Cluster Network to go to Running state.
#   - List instance of the Cluster Network
#   - Terminating Cluster Network
#   - Deleting the Instance Configuration
#
# USAGE:
# `python examples/cluster_networks_example.py  \
#        --compartment '<COMPARTMENT_ID>' \
#        --availability-domain '<AVAILABILITY_DOMAIN>' \
#        --subnet-id '<SUBNET_ID>' \
#        --image-id '<IMAGE_ID>'`
#
# Example (create a cluster network in uk-london-1):
# `python examples/cluster_networks_example.py  \
#        --compartment 'ocid1.compartment.oc1..aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
#        --availability-domain 'asdf:UK-LONDON-1-AD-1' \
#        --subnet-id 'ocid1.subnet.oc1.uk-london-1.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
#        --image-id 'ocid1.image.oc1.uk-london-1.aaaaaaaa5sh4s5zyq5p54zf26u7j2ne6k7q3ryzsajnhy264ydbyr74gqsoq'`
#

import oci
import argparse
from oci.core import ComputeManagementClient, ComputeManagementClientCompositeOperations
from oci.core.models import CreateInstanceConfigurationDetails, \
    InstanceConfigurationLaunchInstanceDetails, \
    InstanceConfigurationInstanceSourceViaImageDetails, \
    InstanceConfigurationCreateVnicDetails, \
    ComputeInstanceDetails, \
    InstanceConfigurationBlockVolumeDetails, \
    InstanceConfigurationCreateVolumeDetails, \
    InstanceConfigurationIscsiAttachVolumeDetails, \
    CreateClusterNetworkDetails, \
    ClusterNetworkPlacementConfigurationDetails, \
    CreateClusterNetworkInstancePoolDetails


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

    volume_attach_details = InstanceConfigurationIscsiAttachVolumeDetails()

    block_volume_details.create_details = create_volume_details
    block_volume_details.attach_details = volume_attach_details
    return block_volume_details


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
                        help='the AD where the cluster network will be spun up (cluster network only spans a single AD)',
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

    args = parser.parse_args()

    # create the compute management client
    compute_management_client = ComputeManagementClient(config)
    composite_client = ComputeManagementClientCompositeOperations(compute_management_client)

    launch_details = InstanceConfigurationLaunchInstanceDetails(
        compartment_id=args.compartment_id,
        display_name="some hpc instance name",
        shape="BM.HPC2.36",
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
        # Creates an hpc instance configuration to use with cluster network
        instance_config = compute_management_client.create_instance_configuration(
            create_instance_config_details).data
        print("Created instanceConfiguration: ", instance_config)

        # Creates a placement configuration to be used when creating a pool
        placement_config = \
            ClusterNetworkPlacementConfigurationDetails()
        placement_config.availability_domain = args.availability_domain
        placement_config.primary_subnet_id = args.subnet_id

        instance_pool_def = CreateClusterNetworkInstancePoolDetails()
        instance_pool_def.instance_configuration_id = instance_config.id
        instance_pool_def.size = 1

        create_cluster_network_details = CreateClusterNetworkDetails()
        create_cluster_network_details.compartment_id = args.compartment_id
        create_cluster_network_details.display_name = "sample cluster network"
        create_cluster_network_details.instance_pools = [instance_pool_def]
        create_cluster_network_details.placement_configuration = placement_config

        # Create a cluster network.
        print("Creating cluster network: ", create_cluster_network_details)
        cluster_network = composite_client.create_cluster_network_and_wait_for_state(
            create_cluster_network_details, wait_for_states=["RUNNING"]).data

        print("Created cluster network: ", cluster_network)

    finally:
        # cleaning up created resources
        compute_management_client.terminate_cluster_network(cluster_network.id)
        print("Terminated cluster network: ", cluster_network)

        compute_management_client.delete_instance_configuration(instance_config.id)
        print("Deleted instanceConfiguration: ", instance_config)
