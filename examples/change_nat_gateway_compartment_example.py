# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This sample will create the VCN where the NAT Gateway will be created, and create the NAT Gateway that
# will be moved to a new compartment.  Cleanup of NAT gateway and VCN is performed after completion of
# the change compartment operation.
#
# This script takes the following arguments
#
#    * The OCID of the compartment where the NAT gateway and related resources will be created
#    * TThe OCID of the compartment where the NAT gateway will be moved to
#
# Usage :
#    change_nat_gateway_compartment_example.py --src-compartment-id=<src compartment OCID>
#                                           --dest-compartment-id=<dest compartment OCID>
#
#

import argparse
import oci
from oci.core import VirtualNetworkClient
from oci.core import VirtualNetworkClientCompositeOperations
from oci.core.models import ChangeNatGatewayCompartmentDetails
from oci.core.models import CreateNatGatewayDetails
from oci.core.models import CreateVcnDetails
from oci.core.models import Vcn
from oci.core.models import NatGateway

nat_gateway_id = None
src_compartment_id = None
dest_compartment_id = None
virtual_network_client = None
virtual_network_client_composite_ops = None
vcn_id = None


# Sets up the service client used to perform the operations
def setup_client():
    global virtual_network_client
    global virtual_network_client_composite_ops

    # read oci config
    config = oci.config.from_file()

    # Create Virtual Network Client with configuration
    virtual_network_client = VirtualNetworkClient(config)

    # Create Virtual Network Client with configuration for composite operations
    virtual_network_client_composite_ops = VirtualNetworkClientCompositeOperations(virtual_network_client)


# Creates VCN and waits for it to become available
def create_vcn():
    global virtual_network_client_composite_ops
    global vcn_id

    # setup create vcn details
    create_vcn_details = CreateVcnDetails()
    create_vcn_details.cidr_block = '10.0.0.0/16'
    create_vcn_details.compartment_id = src_compartment_id
    create_vcn_details.display_name = 'test_change_nat_gateway'

    # create vcn
    response = virtual_network_client_composite_ops.create_vcn_and_wait_for_state(create_vcn_details, wait_for_states=[Vcn.LIFECYCLE_STATE_AVAILABLE])
    vcn_id = response.data.id
    print("Created Vcn: " + vcn_id)
    print("")


# Creates NAT Gateway and waits for it to become available
def create_nat_gateway():
    global virtual_network_client_composite_ops
    global nat_gateway_id
    global vcn_id

    print("Creating NAT Gateway")
    print("=======================================")
    # setup create nat gateway details
    create_ngw_details = CreateNatGatewayDetails()
    create_ngw_details.vcn_id = vcn_id
    create_ngw_details.compartment_id = src_compartment_id
    create_ngw_details.display_name = 'test_change_nat_gateway'

    # create ngw
    response = virtual_network_client_composite_ops.create_nat_gateway_and_wait_for_state(create_ngw_details, wait_for_states=[NatGateway.LIFECYCLE_STATE_AVAILABLE])
    nat_gateway_id = response.data.id

    print("Created NAT Gateway and waited for it to become available %s" % response.data)
    print("")
    print("")


# Changes the compartment of the NAT Gateway
def change_nat_gateway_compartment():
    global virtual_network_client
    global dest_compartment_id
    global nat_gateway_id
    print("Changing NAT Gateway's compartment")
    print("=======================================")
    # setup change compartment details
    change_compartment_details = ChangeNatGatewayCompartmentDetails()
    change_compartment_details.compartment_id = dest_compartment_id

    virtual_network_client.change_nat_gateway_compartment(nat_gateway_id, change_compartment_details)
    changedNatGateway = get_nat_gateway()
    print("NAT Gateway's compartment has been changed: %s" % changedNatGateway.data)
    print("")
    print("")


# Gets the NAT Gateway
def get_nat_gateway():
    global virtual_network_client
    global nat_gateway_id

    response = virtual_network_client.get_nat_gateway(nat_gateway_id)
    return response


# Deletes the NAT Gateway and waits for it to become terminated
def delete_nat_gateway():
    global virtual_network_client_composite_ops
    global nat_gateway_id

    virtual_network_client_composite_ops.delete_nat_gateway_and_wait_for_state(nat_gateway_id, wait_for_states=[NatGateway.LIFECYCLE_STATE_TERMINATED])


# Deletes the VCN and waits for it to become terminated
def delete_vcn():
    global virtual_network_client_composite_ops
    global vcn_id

    virtual_network_client_composite_ops.delete_vcn_and_wait_for_state(vcn_id, wait_for_states=[Vcn.LIFECYCLE_STATE_TERMINATED])


# Parses the command line
def parse_command_line():
    global src_compartment_id
    global dest_compartment_id

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--src-compartment-id',
                        help='source compartment ID in which to create and change nat gateway from',
                        required=True
                        )
    parser.add_argument('--dest-compartment-id',
                        help='destination compartment ID where the nat gateway should be moved',
                        required=True
                        )
    args = parser.parse_args()
    src_compartment_id = args.src_compartment_id
    dest_compartment_id = args.dest_compartment_id


def perform_change_compartment():
    global nat_gateway_id
    global vcn_id

    try:
        print("")
        print("Performing operations to change NAT Gateway compartment from %s to %s" % (src_compartment_id, dest_compartment_id))
        print("")
        setup_client()
        # A VCN is required to create a NAT Gateway
        create_vcn()
        # Here we demonstrate:
        #
        #      - Creating a NAT gateway
        #      - Changing the NAT gateway's compartment
        #
        # And we'll delete these resources when we're done
        #
        create_nat_gateway()
        change_nat_gateway_compartment()

    except Exception as e:
        print("[ERROR]: Error during change nat gateway example execution : %s" % e)
    finally:
        print("Clean Up")
        print("===========")
        if nat_gateway_id:
            delete_nat_gateway()
            print("Deleted NAT Gateway")
        if vcn_id:
            delete_vcn()
            print("Deleted VCN")


if __name__ == '__main__':
    parse_command_line()
    perform_change_compartment()
