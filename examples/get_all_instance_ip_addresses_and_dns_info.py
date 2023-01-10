# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example of retrieving the IP addresses (private and public) and the fully qualified
# domain names for an instance.
#
# Note that this script queries across compartments for public IP addresses, so you should ensure that the user
# you are running under has permissions to perform this action.
#
# This script accepts a single argument:
#   - The OCID of the instance whose details will be retrieved

import json
import oci
import sys


# These dictionaries will store the information on subnets and VCNs which we have
# previously retrieved information for so that we don't have to make redundant service
# calls
subnet_info = {}
vcn_info = {}

# This dictionary stores which public IP address a private IP (identified via its OCID)
# is assigned to
private_ip_to_public_ip = {}


def get_reserved_public_ips_for_compartment(virtual_network_client, compartment_id):
    return oci.pagination.list_call_get_all_results(
        virtual_network_client.list_public_ips,
        'REGION',
        compartment_id
    ).data


def load_reserved_public_ips_for_all_compartments(virtual_network_client, identity_client, config):
    compartments = oci.pagination.list_call_get_all_results(
        identity_client.list_compartments,
        config['tenancy']
    ).data
    compartment_ids = [c.id for c in filter(lambda c: c.lifecycle_state == 'ACTIVE', compartments)]
    if config['tenancy'] not in compartment_ids:
        compartment_ids.append(config['tenancy'])

    for compartment_id in compartment_ids:
        public_ips = get_reserved_public_ips_for_compartment(virtual_network_client, compartment_id)
        private_ip_to_public_ip_for_compartment = {p.private_ip_id: p for p in public_ips}
        private_ip_to_public_ip.update(private_ip_to_public_ip_for_compartment)


def get_subnet_info(virtual_network_client, subnet_id):
    subnet = virtual_network_client.get_subnet(subnet_id).data

    if subnet.vcn_id not in vcn_info:
        vcn_info[subnet.vcn_id] = virtual_network_client.get_vcn(subnet.vcn_id).data

    return subnet


def get_instance_ip_addresses_and_dns_info(compute_client, virtual_network_client, identity_client, instance_id, config):
    instance_info = {
        'private_ips': [],
        'dns_info': [],
        'public_ips': []
    }

    instance = compute_client.get_instance(instance_id).data

    vnic_attachments = oci.pagination.list_call_get_all_results(
        compute_client.list_vnic_attachments,
        compartment_id=instance.compartment_id,
        instance_id=instance.id
    ).data

    vnics = [virtual_network_client.get_vnic(va.vnic_id).data for va in vnic_attachments]
    for vnic in vnics:
        # Each VNIC has:
        #   (A) A primary private IP address
        #   (B) (Optionally) secondary private IP addresses
        #   (C) (Optionally) a public IP address
        #   (D) (Optionally) hostname labels (for DNS) for each private IP address (either
        #       primary or secondary)
        #
        # Additionally, each secondary private IP address can have:
        #   (E) A hostname label (for DNS). This is the same as (D) but is just called
        #       out for completeness
        #   (F) An assigned RESERVED public IP address

        # This handles (C)
        if vnic.public_ip:
            instance_info['public_ips'].append(vnic.public_ip)

        if vnic.subnet_id not in subnet_info:
            subnet_info[vnic.subnet_id] = get_subnet_info(virtual_network_client, vnic.subnet_id)

        # Listing accounts for both primary and secondary private IPs so listing them
        # all allows us to account for (A) and (B)
        private_ips_for_vnic = oci.pagination.list_call_get_all_results(
            virtual_network_client.list_private_ips,
            vnic_id=vnic.id
        ).data

        for private_ip in private_ips_for_vnic:
            instance_info['private_ips'].append(private_ip.ip_address)

            subnet = subnet_info[private_ip.subnet_id]  # Could also use vnic_id rather than private_ip.subnet_id
            vcn = vcn_info[subnet.vcn_id]

            # This accounts for (D) / (E) - the hostname labels for private IPs. Additionally, only
            # try and form a FQDN if we have DNS labels for the subnet and the VCN. See:
            # https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm
            if subnet.dns_label and vcn.dns_label and private_ip.hostname_label:
                instance_info['dns_info'].append(
                    '{}.{}.{}.oraclevcn.com'.format(private_ip.hostname_label, subnet.dns_label, vcn.dns_label)
                )

            # Now we try and cover (F). There are a couple of approaches to do this:
            #
            #   (F1) Preemptively get the RESERVED public IPs for all compartments and then do an in-memory lookup
            #        to see if they are being used by any of the private IPs we have already retrieved. We
            #        need to look at all compartments as a RESERVED public IP may be in a different compartment
            #        to the private IP: https://docs.cloud.oracle.com/Content/Network/Tasks/managingpublicIPs.htm
            #
            #   (F2) Lazily retrieve the public IP used by the private IP address (if any) by individual calls to
            #        get_public_ip_by_private_ip_id
            #
            # Each has drawbacks and benefits, but the one you choose will vary by use case and how you have set up your
            # Oracle Cloud Infrastructure resources. For example, if you have many secondary private IPs then (F2) may result
            # in substantially more service calls than (F1); however for (F1) your user needs permissions to list these resources
            # across multiple compartments and you may also be retrieving redundant data. Depending on how many "things" you
            # are looking for, there is also the potential under (F1) for the data to have become stale, whereas there is no such
            # issue for (F2) because you're always getting that data at the current point in time (however, even in that case under
            # (F1) the more up-to-date data would likely be captured in a subsequent run of this script/example).
            #
            # For illustration purposes, we will demonstrate both (F1) and (F2)
            if not private_ip_to_public_ip:
                load_reserved_public_ips_for_all_compartments(virtual_network_client, identity_client, config)

            if private_ip.id in private_ip_to_public_ip:  # This is (F1)
                print('Found public IP mapping for private IP in list. Public IP details: {}'.format(private_ip_to_public_ip[private_ip.id]))

            try:
                public_ip = virtual_network_client.get_public_ip_by_private_ip_id(
                    oci.core.models.GetPublicIpByPrivateIpIdDetails(
                        private_ip_id=private_ip.id
                    )
                ).data

                if public_ip.ip_address not in instance_info['public_ips']:
                    instance_info['public_ips'].append(public_ip.ip_address)
            except oci.exceptions.ServiceError as e:
                if e.status == 404:
                    print('No public IP mapping found for private IP: {} ({})'.format(private_ip.id, private_ip.ip_address))
                else:
                    print('Unexpected error when retrieving public IPs: {}'.format(str(e)))

    return instance_info


if len(sys.argv) != 2:
    raise RuntimeError('This script expects an argument of the OCID of the instance you wish to retrieve information for')

instance_id = sys.argv[1]

config = oci.config.from_file()
compute_client = oci.core.ComputeClient(config, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
virtual_network_client = oci.core.VirtualNetworkClient(config, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
identity_client = oci.identity.IdentityClient(config, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

ip_addresses_and_dns_info = get_instance_ip_addresses_and_dns_info(compute_client, virtual_network_client, identity_client, instance_id, config)
print('\n\nIP Address and DNS Info')
print('========================')
print(json.dumps(ip_addresses_and_dns_info, sort_keys=True, indent=2))
