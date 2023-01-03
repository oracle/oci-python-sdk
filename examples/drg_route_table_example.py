# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script demonstrates how to add, update, delete, and list static route rules in Dynamic Routing Gateway route tables
#
# This script accepts the following arguments:
#
#   * The OCID of the compartment where resources will be created
#   * VCN 1 CIDR
#   * VCN 2 CIDR
#
# This script relies on the correct IAM policies already being in place for a given compartment ID.
# Information on DRG: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm
# Information on DrgRouteTable API: https://docs.oracle.com/en-us/iaas/api/#/en/iaas/20160918/DrgRouteTable
#

import oci
import sys


def create_vcn(vcn_name, virtual_network_client_composite_operations, compartment_id, cidr_block, vcn_dns_label):
    vcn = virtual_network_client_composite_operations.create_vcn_and_wait_for_state(
        oci.core.models.CreateVcnDetails(
            cidr_block=cidr_block,
            display_name=vcn_name,
            compartment_id=compartment_id,
            dns_label=vcn_dns_label
        ),
        [oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE]
    ).data
    print('Created VCN')
    print('===============')
    print(vcn)
    print('\n')
    return vcn


def create_drg(virtual_network_client, compartment_id):
    result = virtual_network_client.create_drg(
        oci.core.models.CreateDrgDetails(
            compartment_id=compartment_id,
            display_name='Python SDK Example DRG'
        )
    )
    drg = oci.wait_until(
        virtual_network_client,
        virtual_network_client.get_drg(result.data.id),
        'lifecycle_state',
        'AVAILABLE'
    ).data
    print('Created DRG')
    print('===============')
    print(drg)
    print('\n')
    return drg


def create_drg_attachment(virtual_network_client, vcn, drg):
    result = virtual_network_client.create_drg_attachment(
        oci.core.models.CreateDrgAttachmentDetails(
            display_name='Python SDK Example DRG Attachment',
            vcn_id=vcn.id,
            drg_id=drg.id
        )
    )
    drg_attachment = oci.wait_until(
        virtual_network_client,
        virtual_network_client.get_drg_attachment(result.data.id),
        'lifecycle_state',
        'ATTACHED'
    ).data
    print('Created DRG Attachment')
    print('=========================')
    print(drg_attachment)
    print('\n')
    return drg_attachment


def list_static_route_rules(drg_route_table, virtual_network_client):
    static_route_rules = virtual_network_client.list_drg_route_rules(drg_route_table_id=drg_route_table.id, route_type="STATIC").data
    for rule in static_route_rules:
        print("id: " + rule.id)
        print("destination type: " + rule.destination_type)
        print("destination: " + rule.destination)
    return static_route_rules


# read oci config
config = oci.config.from_file()

# Create Virtual Network Client with configuration
virtual_network_client = oci.core.VirtualNetworkClient(config)

# Create Virtual Network Client with configuration for composite operations
virtual_network_client_composite_operations = oci.core.VirtualNetworkClientCompositeOperations(virtual_network_client)

if len(sys.argv) != 4:
    raise RuntimeError('This script expects three arguments: the compartment OCID and two VCN CIDRs')

compartment_id = sys.argv[1]
vcn1_cidr = sys.argv[2]
vcn2_cidr = sys.argv[3]

drg = None
drg_attachment_1 = None
drg_attachment_2 = None
vcn_1 = None
vcn_2 = None

try:
    print('Creating DRG.')
    drg = create_drg(virtual_network_client, compartment_id)

    print("Creating VCN 1.")
    vcn_1 = create_vcn("VCN 1", virtual_network_client_composite_operations, compartment_id, vcn1_cidr, 'dnslabel1')

    print("Creating DRG Attachment 1.")
    drg_attachment_1 = create_drg_attachment(virtual_network_client, vcn_1, drg)

    print("Creating VCN 2.")
    vcn_2 = create_vcn("VCN 2", virtual_network_client_composite_operations, compartment_id, vcn2_cidr, 'dnslabel2')

    print("Creating DRG Attachment 2.")
    drg_attachment_2 = create_drg_attachment(virtual_network_client, vcn_2, drg)

    print("Creating a new DRG route table.")
    result = virtual_network_client.create_drg_route_table(
        oci.core.models.CreateDrgRouteTableDetails(
            drg_id=drg.id
        )
    ).data
    drg_route_table = oci.wait_until(
        virtual_network_client,
        virtual_network_client.get_drg_route_table(result.id),
        'lifecycle_state',
        'AVAILABLE'
    ).data
    print(drg_route_table)
    print('\n')

    print("Assign the newly created DRG route table to drg attachment 1 (with VCN1).")
    virtual_network_client.update_drg_attachment(
        drg_attachment_id=drg_attachment_1.id,
        update_drg_attachment_details=oci.core.models.UpdateDrgAttachmentDetails(
            drg_route_table_id=drg_route_table.id
        )
    ).data

    print("Add static route rules pointing to attachment 2.")
    virtual_network_client.add_drg_route_rules(
        drg_route_table_id=drg_route_table.id,
        add_drg_route_rules_details=oci.core.models.AddDrgRouteRulesDetails(
            route_rules=[
                {
                    "destination": "192.168.250.0/24",
                    "destinationType": "CIDR_BLOCK",
                    "nextHopDrgAttachmentId": drg_attachment_2.id
                },
                {
                    "destination": "192.150.250.0/24",
                    "destinationType": "CIDR_BLOCK",
                    "nextHopDrgAttachmentId": drg_attachment_2.id
                }
            ]
        )
    )

    print("List static route rules in the DRG route table.")
    route_rules = list_static_route_rules(drg_route_table, virtual_network_client)

    print("Update static route rules.")
    virtual_network_client.update_drg_route_rules(
        drg_route_table_id=drg_route_table.id,
        update_drg_route_rules_details=oci.core.models.UpdateDrgRouteRulesDetails(
            route_rules=[
                {
                    "id": route_rules[0].id,
                    "destination": "120.168.250.0/24",
                    "destinationType": "CIDR_BLOCK",
                    "nextHopDrgAttachmentId": drg_attachment_2.id
                },
                {
                    "id": route_rules[1].id,
                    "destination": "115.150.250.0/24",
                    "destinationType": "CIDR_BLOCK",
                    "nextHopDrgAttachmentId": drg_attachment_2.id
                }
            ]
        )
    )

    print("List static route rules in the DRG route table.")
    list_static_route_rules(drg_route_table, virtual_network_client)

    print("Remove both static route rules.")
    virtual_network_client.remove_drg_route_rules(
        drg_route_table_id=drg_route_table.id,
        remove_drg_route_rules_details={"routeRuleIds": [route_rules[0].id, route_rules[1].id]}
    )

    print("List static route rules in the DRG route table.")
    list_static_route_rules(drg_route_table, virtual_network_client)

    print("Remove import route distribution.")
    import_route_distribution_id = drg_route_table.import_drg_route_distribution_id
    virtual_network_client.remove_import_drg_route_distribution(
        drg_route_table_id=drg_route_table.id
    )

    print("Add import route distribution back.")
    virtual_network_client.update_drg_route_table(
        drg_route_table_id=drg_route_table.id,
        update_drg_route_table_details={"importDrgRouteDistributionId": import_route_distribution_id}
    )

finally:
    if drg_attachment_1 is not None:
        print('Deleting Drg attachment 1')
        virtual_network_client_composite_operations.delete_drg_attachment_and_wait_for_state(
            drg_attachment_id=drg_attachment_1.id,
            wait_for_states=[oci.core.models.DrgAttachment.LIFECYCLE_STATE_DETACHED]
        )

    if drg_attachment_2 is not None:
        print('Deleting Drg attachment 2')
        virtual_network_client_composite_operations.delete_drg_attachment_and_wait_for_state(
            drg_attachment_id=drg_attachment_2.id,
            wait_for_states=[oci.core.models.DrgAttachment.LIFECYCLE_STATE_DETACHED]
        )

    if vcn_1 is not None:
        print('Deleting Vcn 1')
        virtual_network_client_composite_operations.delete_vcn_and_wait_for_state(
            vcn_id=vcn_1.id,
            wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
        )

    if vcn_2 is not None:
        print('Deleting Vcn 2')
        virtual_network_client_composite_operations.delete_vcn_and_wait_for_state(
            vcn_id=vcn_2.id,
            wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
        )

    if drg is not None:
        print('Deleting DRG')
        virtual_network_client_composite_operations.delete_drg_and_wait_for_state(
            drg_id=drg.id,
            wait_for_states=[oci.core.models.Drg.LIFECYCLE_STATE_TERMINATED]
        )
