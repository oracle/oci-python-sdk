# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example of how use the instance configuration CLI in terms of:
#   - Creating an instance configuration from input details
#   - Launching an instance with instance configuration
#   - Creating an instance configuration from a running instance
#   - Deleting the instance configuration
#

import oci
import argparse
from oci.core import ComputeClient
from oci.core import ComputeManagementClient
from oci.core.models import CreateInstanceConfigurationDetails, \
    CreateInstanceConfigurationFromInstanceDetails, \
    InstanceConfigurationLaunchInstanceDetails, \
    InstanceConfigurationInstanceSourceViaImageDetails, \
    InstanceConfigurationCreateVnicDetails, \
    ComputeInstanceDetails, \
    InstanceConfigurationBlockVolumeDetails, \
    InstanceConfigurationCreateVolumeDetails, \
    InstanceConfigurationParavirtualizedAttachVolumeDetails


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

    args = parser.parse_args()

    # create the compute management client
    compute_management_client = ComputeManagementClient(config)

    # create the compute client
    compute_client = ComputeClient(config)

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
        display_name="instance config from input",
        compartment_id=args.compartment_id,
        instance_details=instance_details)

    launch_instance_details = InstanceConfigurationLaunchInstanceDetails(
        availability_domain=args.availability_domain,
        create_vnic_details=InstanceConfigurationCreateVnicDetails(
            subnet_id=args.subnet_id)
    )

    try:
        # Creates an instance configuration from input
        instance_config = compute_management_client.create_instance_configuration(
            create_instance_config_details).data
        print("Created instanceConfiguration: ", instance_config)

        instance = compute_management_client.launch_instance_configuration(
            instance_configuration_id=instance_config.id,
            instance_configuration=ComputeInstanceDetails(
                launch_details=launch_instance_details)
        ).data
        print("Launched instance: ", instance)

        oci.wait_until(
            compute_client,
            compute_client.get_instance(instance.id),
            'lifecycle_state',
            'RUNNING',
            max_interval_seconds=900,
            max_wait_seconds=21600
        )

        create_instance_config_from_instance_details = CreateInstanceConfigurationFromInstanceDetails(
            display_name="instance config from instance",
            compartment_id=args.compartment_id,
            instance_id=instance.id)

        instance_config_from_instance = compute_management_client.create_instance_configuration(
            create_instance_config_from_instance_details).data
        print("Created instanceConfiguration from instance: ", instance_config_from_instance)

    finally:
        # cleaning up created resources
        compute_management_client.delete_instance_configuration(instance_config.id)
        print("Deleted instanceConfiguration: ", instance_config)

        compute_management_client.delete_instance_configuration(instance_config_from_instance.id)
        print("Deleted instanceConfiguration: ", instance_config_from_instance)

        compute_client.terminate_instance(instance.id)
        print("Terminated instance: ", instance)
