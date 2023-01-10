# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to create an IPv6 load balancer using the Python SDK.
# NOTE: The provided subnet must be within an IPv6-enabled VCN.
#
# USAGE:
# `python examples/create_ipv6_load_balancer_example.py --compartment-id 'foo' --subnet-id 'bar' --display-name 'bat'`
#
# This script will create an IPv6 load balancer and
# accepts the following arguments:
#
#   * The compartment ID in which the load balancer will be created
#   * The subnet ID in which the load balancer will be created
#   * The shape of the load balancer to be created
#   * The display name for the load balancer to be created

import oci
import argparse

# ---------- parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--compartment-id',
                    help='compartment ID in which to perform the operation',
                    required=True
                    )
parser.add_argument('--subnet-id',
                    help='subnet ID in which the load balancer will be created',
                    required=True
                    )
parser.add_argument('--display-name',
                    help='display name for the load balancer to be created',
                    required=False,
                    default='python-sdk-create-ipv6-lb-example'
                    )
parser.add_argument('--shape-name',
                    help='shape name of the load balancer to be created',
                    required=False,
                    default='100Mbps'
                    )
args = parser.parse_args()

# ---------- assign provided arguments
compartment_id = args.compartment_id
subnet_id = args.subnet_id
display_name = args.display_name
shape_name = args.shape_name

# ---------- read config from file
config = oci.config.from_file()
load_balancer_client = oci.core.LoadBalancerClient(config)
load_balancer_client_composite_ops = oci.load_balancer.LoadBalancerClientCompositeOperations(load_balancer_client)

# ---------- create load balancer
load_balancer = load_balancer_client_composite_ops.create_load_balancer_and_wait_for_state(
    oci.core.models.CreateLoadBalancerDetails(
        compartment_id=compartment_id,
        display_name=display_name,
        shape_name=shape_name,
        ip_mode="IPV6",
        subnet_ids=[subnet_id]
    ),
    [oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)

print('Created Load Balancer %s' % (load_balancer.data.id))
