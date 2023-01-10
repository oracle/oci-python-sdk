# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to move a service gateway from one compartment to another using Python SDK.
# This script will perform the following operations to perform the above operation:
#
#    * Read user configuration
#    * Construct VirtualNetworkClient using user configuration
#    * Create VCN
#    * Create Service Gateway
#    * Change Service Gateway Compartment
#    * Get Service Gateway
#    * Delete Service Gateway
#    * Delete VCN
#
# This script takes the following arguments
#
#    * The source destination id (from where the service gateway should be created and moved from)
#    * The destination compartment id
#
# Usage :
#    change_service_gateway_compartment_example.py --src-compartment-id=<src compartment OCID>
#                                           --dest-compartment-id=<dest compartment OCID>
#
#

import argparse
import oci
from oci.core import VirtualNetworkClient
from oci.core import VirtualNetworkClientCompositeOperations
from oci.core.models import ChangeServiceGatewayCompartmentDetails
from oci.core.models import CreateServiceGatewayDetails
from oci.core.models import CreateVcnDetails
from oci.core.models import Vcn
from oci.core.models import ServiceGateway


infoEnabled = True
service_gateway_id = None
src_compartment_id = None
dest_compartment_id = None
virtual_network_client = None
virtual_network_client_composite_ops = None
vcn_id = None


def info(message):
    if infoEnabled:
        print("[INFO] " + str(message))


def error(message):
    if infoEnabled:
        print("[ERROR]" + str(message))


def setup_client():
    global virtual_network_client
    global virtual_network_client_composite_ops

    # read oci config
    config = oci.config.from_file()

    # Create Virtual Network Client with configuration
    virtual_network_client = VirtualNetworkClient(config)

    # Create Virtual Network Client with configuration for composite operations
    virtual_network_client_composite_ops = VirtualNetworkClientCompositeOperations(virtual_network_client)


def create_vcn():
    global virtual_network_client_composite_ops
    global vcn_id

    # setup create vcn details
    create_vcn_details = CreateVcnDetails()
    create_vcn_details.cidr_block = '10.0.0.0/16'
    create_vcn_details.compartment_id = src_compartment_id
    create_vcn_details.display_name = 'test_change_service_gateway'

    # create vcn
    response = virtual_network_client_composite_ops.create_vcn_and_wait_for_state(create_vcn_details, wait_for_states=[Vcn.LIFECYCLE_STATE_AVAILABLE])
    vcn_id = response.data.id
    info("VCN ID : %s" % vcn_id)


def create_service_gateway():
    global virtual_network_client_composite_ops
    global service_gateway_id
    global vcn_id

    # setup create service gateway details
    create_sgw_details = CreateServiceGatewayDetails()
    create_sgw_details.vcn_id = vcn_id
    create_sgw_details.compartment_id = src_compartment_id
    create_sgw_details.display_name = 'test_change_service_gateway'
    # Providing empty services field for the purpose of the test. Please update to required
    # services' value if reaching Oracle Services.
    create_sgw_details.services = list()

    # create sgw
    response = virtual_network_client_composite_ops.create_service_gateway_and_wait_for_state(create_sgw_details, wait_for_states=[ServiceGateway.LIFECYCLE_STATE_AVAILABLE])
    service_gateway_id = response.data.id

    info("SERVICE GATEWAY ID : %s" % service_gateway_id)


def change_service_gateway_compartment():
    global virtual_network_client
    global dest_compartment_id
    global service_gateway_id

    # setup change compartment details
    change_compartment_details = ChangeServiceGatewayCompartmentDetails()
    change_compartment_details.compartment_id = dest_compartment_id

    virtual_network_client.change_service_gateway_compartment(service_gateway_id, change_compartment_details)


def get_service_gateway():
    global virtual_network_client
    global service_gateway_id

    response = virtual_network_client.get_service_gateway(service_gateway_id)
    info(response.data)


def delete_service_gateway():
    global virtual_network_client_composite_ops
    global service_gateway_id

    virtual_network_client_composite_ops.delete_service_gateway_and_wait_for_state(service_gateway_id, wait_for_states=[ServiceGateway.LIFECYCLE_STATE_TERMINATED])


def delete_vcn():
    global virtual_network_client_composite_ops
    global vcn_id

    virtual_network_client_composite_ops.delete_vcn_and_wait_for_state(vcn_id, wait_for_states=[Vcn.LIFECYCLE_STATE_TERMINATED])


def parse_command_line():
    global src_compartment_id
    global dest_compartment_id

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--src-compartment-id',
                        help='source compartment ID in which to create and change service gateway from',
                        required=True
                        )
    parser.add_argument('--dest-compartment-id',
                        help='destination compartment ID where the service gateway should be moved',
                        required=True
                        )
    args = parser.parse_args()
    src_compartment_id = args.src_compartment_id
    dest_compartment_id = args.dest_compartment_id


def perform_change_compartment():
    global service_gateway_id
    global vcn_id

    try:
        info("Setup Client")
        setup_client()

        info("Create VCN")
        create_vcn()

        info("Create Service Gateway")
        create_service_gateway()

        info("Change Service Gateway Compartment to %s" % dest_compartment_id)
        change_service_gateway_compartment()
        info("Service Gateway moved to destination compartment")

        info("Get Service Gateway's new compartment after change compartment")
        get_service_gateway()
    except Exception as e:
        error("Error during change service gateway example execution : %s" % e)
    finally:
        if service_gateway_id:
            info("Delete Service Gateway")
            delete_service_gateway()

        if vcn_id:
            info("Delete VCN")
            delete_vcn()


if __name__ == '__main__':
    parse_command_line()
    perform_change_compartment()
