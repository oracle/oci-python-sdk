# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to create a Service Gateway.
#
# USAGE:
# `python examples/create_service_gateway_example.py --compartment-id 'foo' --vcn-id 'bar'`
#
# This script will create a Service Gateway
# accepts the following arguments:
#
#   * The compartment ID in which to perform the operation
#   * The VCN ID on which the Service Gateway will be created
#   * The display name for the Service Gateway to be created (optional)
#   * The route table ID to which the Service Gateway will be assigned (optional)
#
# for more information on Service Gateways see: https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm


import oci
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--compartment-id',
                    help='compartment ID in which to perform the operation',
                    required=True
                    )
parser.add_argument('--vcn-id',
                    help='VCN ID on which the Service Gateway will be created',
                    required=True
                    )
parser.add_argument('--display-name',
                    help='display name for the Service Gateway to be created',
                    required=False,
                    default='python-sdk-create-service-gateway-example'
                    )
parser.add_argument('--route-table-id',
                    help='OPTIONAL: route table ID to which the Service Gateway will be assigned',
                    required=False
                    )
args = parser.parse_args()

# ---------- assign provided arguments
compartment_id = args.compartment_id
vcn_id = args.vcn_id
display_name = args.display_name
route_table_id = args.route_table_id


def create_service_gateway(virtual_network_client, compartment_id, vcn_id, display_name):
    create_sgw_details = oci.core.models.CreateServiceGatewayDetails(
        compartment_id=compartment_id,
        vcn_id=vcn_id,
        display_name=display_name,
        services=list()
    )

    response_data = virtual_network_client.create_service_gateway_and_wait_for_state(
        create_sgw_details,
        wait_for_states=[oci.core.models.ServiceGateway.LIFECYCLE_STATE_AVAILABLE]
    ).data

    print("Created Service Gateway %s" % response_data.id)


# ---------- read config from file
config = oci.config.from_file()
compute_client = oci.core.ComputeClient(config)

# Create Virtual Network Client with configuration for composite operations
virtual_network_client = oci.core.VirtualNetworkClientCompositeOperations(
    oci.core.VirtualNetworkClient(config)
)

# create Service Gateway
create_service_gateway(
    virtual_network_client,
    compartment_id,
    vcn_id,
    display_name
)
