# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to create an IPv6 VNIC attachment to a provided
# instance using the Python SDK. NOTE: The provided instance must be within an IPv6-enabled VCN.
#
# USAGE:
# `python examples/create_ipv6_example.py --compartment-id 'foo' --instance-id 'bar'`
#
# This script will create an IPv6 VNIC attachment to the provided instance and
# accepts the following arguments:
#
#   * The compartment ID in which the instance is located
#   * The instance ID on which the IPv6 will be created
#   * The display name for the IPv6 to be created

import oci
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--compartment-id',
                    help='compartment ID in which to perform the operation',
                    required=True
                    )
parser.add_argument('--instance-id',
                    help='instance ID on which the IPv6 attachment will be created',
                    required=True
                    )
parser.add_argument('--display-name',
                    help='display name for the IPv6 to be created',
                    required=False,
                    default='python-sdk-create-ipv6-example'
                    )
args = parser.parse_args()


def get_vnic_attachments(compute_client, instance_id, compartment_id):
    vnic_attachments = compute_client.list_vnic_attachments(
        compartment_id,
        instance_id=instance_id
    ).data
    print('found VNIC attachments:\n{}'.format(vnic_attachments))
    return vnic_attachments


def create_ipv6(virtual_network_client, vnic_id, display_name):
    create_ipv6_response = virtual_network_client.create_ipv6(
        oci.core.models.CreateIpv6Details(
            display_name=display_name,
            vnic_id=vnic_id
        )
    ).data
    return create_ipv6_response


# ---------- assign provided arguments
compartment_id = args.compartment_id
instance_id = args.instance_id
display_name = args.display_name

# ---------- read config from file
config = oci.config.from_file()
compute_client = oci.core.ComputeClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)

# ---------- get VNIC attachments for provided instance
vnics = get_vnic_attachments(
    compute_client,
    args.instance_id,
    args.compartment_id
)

# ---------- create IPv6 object
create_ipv6(
    virtual_network_client,
    vnics[0].vnic_id,  # use first vnic ID returned from `get_vnic_attachments`
    display_name
)
