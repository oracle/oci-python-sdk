# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use use the Python SDK to create a remote peering of two virtual cloud networks
# between two different regions within a single compartment.
#
# This script accepts the following arguments:
#
#   * The OCID of the compartment where resources will be created
#   * The local region (e.g. us-phoenix-1)
#   * The remote region (e.g. us-ashburn-1)
#
# This script relies on the correct IAM policies already being in place for a given compartment ID.
# For more information, please refer to: https://docs.cloud.oracle.com/Content/Network/Tasks/remoteVCNpeering.htm
#
# In order to demonstrate remote peering, this script will also create one DRG and one VCN in each region. These resources will
# be deleted at the end of the script. DRGs and VCNs are a finite resource and may require contacting customer support if limits
# have been exceeded for your tenancy.

import oci
import sys


def create_vcn_drg_and_drg_attachment(virtual_network_client, compartment_id, cidr_block, vcn_dns_label):
    vcn_name = 'py_sdk_example_vcn'

    result = virtual_network_client.create_vcn(
        oci.core.models.CreateVcnDetails(
            cidr_block=cidr_block,
            display_name=vcn_name,
            compartment_id=compartment_id,
            dns_label=vcn_dns_label
        )
    )
    vcn = oci.wait_until(
        virtual_network_client,
        virtual_network_client.get_vcn(result.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_wait_seconds=300
    ).data
    print('Created VCN')
    print('===============')
    print(vcn)
    print('\n\n')

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
    print('\n\n')

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
    print('\n\n')

    return {'vcn': vcn, 'drg': drg, 'drg_attachment': drg_attachment}


def delete_vcn_drg_and_drg_attachment(virtual_network_client, vcn_drg_and_drg_attachment):
    vcn = vcn_drg_and_drg_attachment['vcn']
    drg = vcn_drg_and_drg_attachment['drg']
    drg_attachment = vcn_drg_and_drg_attachment['drg_attachment']
    composite_virtual_network_client = oci.core.VirtualNetworkClientCompositeOperations(
        virtual_network_client)

    print('Deleting DRG Attachment')
    composite_virtual_network_client.delete_drg_attachment_and_wait_for_state(
        drg_attachment.id,
        oci.core.models.DrgAttachment.LIFECYCLE_STATE_DETACHED
    )

    print('Deleting DRG')
    composite_virtual_network_client.delete_drg_and_wait_for_state(
        drg.id,
        oci.core.models.Drg.LIFECYCLE_STATE_TERMINATED
    )

    print('Deleting VCN')
    composite_virtual_network_client.delete_vcn_and_wait_for_state(
        vcn.id,
        oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED
    )


config = oci.config.from_file()
virtual_network_client_local = oci.core.VirtualNetworkClient(config)
virtual_network_client_remote = oci.core.VirtualNetworkClient(config)

if len(sys.argv) != 4:
    raise RuntimeError('This script expects an argument of the compartment OCID and the local and remote regions for peering')

compartment_id = sys.argv[1]
local_region = sys.argv[2]
remote_region = sys.argv[3]

virtual_network_client_local.base_client.set_region(local_region)
virtual_network_client_remote.base_client.set_region(remote_region)

local_vcn_and_drg = None
remote_vcn_and_drg = None

remote_peering_connection_in_local_region = None
remote_peering_connection_in_remote_region = None
remote_peering_connection_established = False

try:
    local_vcn_and_drg = create_vcn_drg_and_drg_attachment(
        virtual_network_client_local,
        compartment_id,
        '10.5.0.0/16',
        'pylocal'
    )

    remote_vcn_and_drg = create_vcn_drg_and_drg_attachment(
        virtual_network_client_remote,
        compartment_id,
        '10.6.0.0/16',
        'pyremote'
    )

    # Create a remote peering connection in the local region
    print('Creating remote peering connection in {}'.format(local_region))
    print('=====================================')
    result = virtual_network_client_local.create_remote_peering_connection(
        oci.core.models.CreateRemotePeeringConnectionDetails(
            compartment_id=compartment_id,
            drg_id=local_vcn_and_drg['drg'].id,
            display_name='Remote peering connection in local'
        )
    )
    remote_peering_connection_in_local_region = oci.wait_until(
        virtual_network_client_local,
        virtual_network_client_local.get_remote_peering_connection(result.data.id),
        'lifecycle_state',
        'AVAILABLE'
    ).data
    print(remote_peering_connection_in_local_region)
    print('\n\n')

    # Create a remote peering connection in the remote region
    print('Creating remote peering connection in {}'.format(remote_region))
    print('=====================================')
    result = virtual_network_client_remote.create_remote_peering_connection(
        oci.core.models.CreateRemotePeeringConnectionDetails(
            compartment_id=compartment_id,
            drg_id=remote_vcn_and_drg['drg'].id,
            display_name='Remote peering connection in remote'
        )
    )
    remote_peering_connection_in_remote_region = oci.wait_until(
        virtual_network_client_remote,
        virtual_network_client_remote.get_remote_peering_connection(result.data.id),
        'lifecycle_state',
        'AVAILABLE'
    ).data
    print(remote_peering_connection_in_remote_region)
    print('\n\n')

    # Now that we have remote peering connections created in the local and remote regions, we can link the two
    print("Establishing connection between local and remote regions")
    print('=====================================')
    # We use the service client in the LOCAL region
    # The first parameter is the remote peering connection in the LOCAL region
    # The ConnectRemotePeeringConnectionsDetails should contain the details of the remote peering connection in the REMOTE region
    virtual_network_client_local.connect_remote_peering_connections(
        remote_peering_connection_in_local_region.id,
        oci.core.models.ConnectRemotePeeringConnectionsDetails(
            peer_id=remote_peering_connection_in_remote_region.id,
            peer_region_name=remote_region
        )
    )
    remote_peering_connection_established = True

    # Now we wait until the local and remote peering connections say that both are peered. Note here that our waiter uses the
    # peering_status attribute
    oci.wait_until(
        virtual_network_client_local,
        virtual_network_client_local.get_remote_peering_connection(remote_peering_connection_in_local_region.id),
        'peering_status',
        'PEERED'
    )
    oci.wait_until(
        virtual_network_client_remote,
        virtual_network_client_remote.get_remote_peering_connection(remote_peering_connection_in_remote_region.id),
        'peering_status',
        'PEERED'
    )
    print('Remote peering connection established between {} and {}'.format(local_region, remote_region))
    print('\n\n')

finally:
    # Note that the order of deleting resources when we have remote peering connections is important. First we
    # delete the remote peering connections on either end and wait for their lifecycle states to be terminated
    # and their peering statuses to be revoked. Then we can delete our DRG and VCN in the local and remote region

    if remote_peering_connection_in_local_region is not None:
        print('Deleting remote peering connection in {}'.format(local_region))
        print('=======================')
        # After the delete, the call to get_remote_peering_connection() may 404, so we can't call it directly in an argument to
        # wait_until() because that'll cause an exception. We have two options:
        #
        #   1) Do a GET before the delete so that we have a response to provide to wait_until
        #   2) Catch the exception and proceed onwards if it is a 404
        #
        # The code directly below demonstrates the first option. The second option is demonstrated later on line 268
        get_response = virtual_network_client_local.get_remote_peering_connection(remote_peering_connection_in_local_region.id)
        virtual_network_client_local.delete_remote_peering_connection(remote_peering_connection_in_local_region.id)
        oci.wait_until(
            virtual_network_client_local,
            get_response,
            'lifecycle_state',
            'TERMINATED',
            succeed_on_not_found=True
        )
        print('Deleted remote peering connection\n\n')

        if remote_peering_connection_established:
            # No need for a succeed_on_not_found here because we haven't called delete_remote_peering_connection() in the
            # remote region yet
            result = oci.wait_until(
                virtual_network_client_remote,
                virtual_network_client_remote.get_remote_peering_connection(remote_peering_connection_in_remote_region.id),
                'peering_status',
                'REVOKED'
            )
            print('Remote peering connection in remote ({}) region revoked'.format(remote_region))
            print('\n\n')

            # It is possible that the get_remote_peering_connection() call here can 404. That's OK as it means the connection
            # is deleted and we can proceed
            try:
                oci.wait_until(
                    virtual_network_client_local,
                    virtual_network_client_local.get_remote_peering_connection(remote_peering_connection_in_local_region.id),
                    'peering_status',
                    'REVOKED',
                    succeed_on_not_found=True
                )
            except oci.exceptions.ServiceError as e:
                if e.status == 404:
                    pass
                else:
                    raise
            print('Remote peering connection in local ({}) region revoked'.format(local_region))
            print('\n\n')

    if remote_peering_connection_in_remote_region is not None:
        print('Deleting remote peering connection in {}'.format(remote_region))
        print('=======================')
        get_response = virtual_network_client_remote.get_remote_peering_connection(remote_peering_connection_in_remote_region.id)
        virtual_network_client_remote.delete_remote_peering_connection(remote_peering_connection_in_remote_region.id)
        oci.wait_until(
            virtual_network_client_remote,
            get_response,
            'lifecycle_state',
            'TERMINATED',
            succeed_on_not_found=True
        )
        print('Remote peering connection deleted')
        print('\n\n')

    if local_vcn_and_drg is not None:
        print('Deleting local VCN and DRG')
        print('================================')
        delete_vcn_drg_and_drg_attachment(virtual_network_client_local, local_vcn_and_drg)
        print('\n\n')

    if remote_vcn_and_drg is not None:
        print('Deleting remote VCN and DRG')
        print('================================')
        delete_vcn_drg_and_drg_attachment(virtual_network_client_remote, remote_vcn_and_drg)
