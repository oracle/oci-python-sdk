#!/usr/bin/env python3
##########################################################################
# Copyright(c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.
# list_all_ipsec_tunnels_in_tenancy.py
#
# @author: Adi Zohar
#
# Supports Python 2 and 3
#
# coding: utf-8
##########################################################################
# Info:
#    List all IPSEC tunnels in Tenancy including DRG redundancy
#
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of ListIPsecGroup group with below Policy rules:
#          Allow group ListIPsecGroup to inspect compartments in tenancy
#          Allow group ListIPsecGroup to inspect tenancies in tenancy
#          Allow group ListIPsecGroup to inspect ipsec-connections in tenancy
#          Allow group ListIPsecGroup to inspect drgs in tenancy
#
#    Option 2 - Instance Principle
#       Compute instance part of DynListIPsecGroup dynamic group with policy rules:
#          Allow dynamic group DynListIPsecGroup to inspect compartments in tenancy
#          Allow dynamic group DynListIPsecGroup to inspect tenancies in tenancy
#          Allow dynamic group DynListIPsecGroup to inspect ipsec-connections in tenancy
#          Allow dynamic group DynListIPsecGroup to inspect drgs in tenancy
#
##########################################################################
# Modules Included:
# - oci.identity.IdentityClient
#
# APIs Used:
# - IdentityClient.list_compartments         - Policy COMPARTMENT_INSPECT
# - IdentityClient.get_tenancy               - Policy TENANCY_INSPECT
# - IdentityClient.list_region_subscriptions - Policy TENANCY_INSPECT
# - VirtualNetworkClient.list_ip_sec_connections        - Policy IPSEC_CONNECTION_READ
# - VirtualNetworkClient.list_ip_sec_connection_tunnels - Policy IPSEC_CONNECTION_READ
# - VirtualNetworkClient.get_drg_redundancy_status      - Policy DRG_READ
#
##########################################################################
# Application Command line parameters
#
#   -t config - Config file section to use (tenancy profile)
#   -p proxy  - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip       - Use Instance Principals for Authentication
#   -dt       - Use Instance Principals with delegation token for cloud shell
##########################################################################
from __future__ import print_function
import sys
import argparse
import datetime
import oci
import json
import os


##########################################################################
# Print header centered
##########################################################################
def print_header(name):
    chars = int(90)
    print("")
    print('#' * chars)
    print("#" + name.center(chars - 2, " ") + "#")
    print('#' * chars)


##########################################################################
# check service error to warn instead of error
##########################################################################
def check_service_error(code):
    return ('max retries exceeded' in str(code).lower() or
            'auth' in str(code).lower() or
            'notfound' in str(code).lower() or
            code == 'Forbidden' or
            code == 'TooManyRequests' or
            code == 'IncorrectState' or
            code == 'LimitExceeded'
            )


##########################################################################
# Create signer for Authentication
# Input - config_profile and is_instance_principals and is_delegation_token
# Output - config and signer objects
##########################################################################
def create_signer(config_profile, is_instance_principals, is_delegation_token):

    # if instance principals authentications
    if is_instance_principals:
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            config = {'region': signer.region, 'tenancy': signer.tenancy_id}
            return config, signer

        except Exception:
            print_header("Error obtaining instance principals certificate, aborting")
            raise SystemExit

    # -----------------------------
    # Delegation Token
    # -----------------------------
    elif is_delegation_token:

        try:
            # check if env variables OCI_CONFIG_FILE, OCI_CONFIG_PROFILE exist and use them
            env_config_file = os.environ.get('OCI_CONFIG_FILE')
            env_config_section = os.environ.get('OCI_CONFIG_PROFILE')

            # check if file exist
            if env_config_file is None or env_config_section is None:
                print("*** OCI_CONFIG_FILE and OCI_CONFIG_PROFILE env variables not found, abort. ***")
                print("")
                raise SystemExit

            config = oci.config.from_file(env_config_file, env_config_section)
            delegation_token_location = config["delegation_token_file"]

            with open(delegation_token_location, 'r') as delegation_token_file:
                delegation_token = delegation_token_file.read().strip()
                # get signer from delegation token
                signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(delegation_token=delegation_token)

                return config, signer

        except KeyError:
            print("* Key Error obtaining delegation_token_file")
            raise SystemExit

        except Exception:
            raise

    # -----------------------------
    # config file authentication
    # -----------------------------
    else:
        config = oci.config.from_file(
            oci.config.DEFAULT_LOCATION,
            (config_profile if config_profile else oci.config.DEFAULT_PROFILE)
        )
        signer = oci.signer.Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config.get("key_file"),
            pass_phrase=oci.config.get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content")
        )
        return config, signer


##########################################################################
# Load compartments
##########################################################################
def identity_read_compartments(identity, tenancy):

    print("Loading Compartments...")
    try:
        compartments = oci.pagination.list_call_get_all_results(
            identity.list_compartments,
            tenancy.id,
            compartment_id_in_subtree=True
        ).data

        # Add root compartment which is not part of the list_compartments
        compartments.append(tenancy)

        print("    Total " + str(len(compartments)) + " compartments loaded.")
        return compartments

    except Exception as e:
        raise RuntimeError("Error in identity_read_compartments: " + str(e.args))


##########################################################################
# Main
##########################################################################

# Get Command Line Parser
parser = argparse.ArgumentParser()
parser.add_argument('-t', default="", dest='config_profile', help='Config file section to use (tenancy profile)')
parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
parser.add_argument('-dt', action='store_true', default=False, dest='is_delegation_token', help='Use Delegation Token for Authentication')
cmd = parser.parse_args()

# Start print time info
start_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print_header("Running List IPSecTunnels")
print("Starts at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
print("Written By Adi Zohar, June 2020")
print("Command Line : " + ' '.join(x for x in sys.argv[1:]))

# Identity extract compartments
config, signer = create_signer(cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)
compartments = []
tenancy = None
try:
    print("\nConnecting to Identity Service...")
    identity = oci.identity.IdentityClient(config, signer=signer)
    if cmd.proxy:
        identity.base_client.session.proxies = {'https': cmd.proxy}

    tenancy = identity.get_tenancy(config["tenancy"]).data
    regions = identity.list_region_subscriptions(tenancy.id).data

    print("Tenant Name : " + str(tenancy.name))
    print("Tenant Id   : " + tenancy.id)
    print("")

    compartments = identity_read_compartments(identity, tenancy)

except Exception as e:
    raise RuntimeError("\nError extracting compartments section - " + str(e))


############################################
# Loop on all regions
############################################
print("\nLoading IPSEC Tunnels...")
data = []
warnings = 0
for region_name in [str(es.region_name) for es in regions]:

    print("\nRegion " + region_name + "...")

    # set the region in the config and signer
    config['region'] = region_name
    signer.region = region_name

    # connect to virtual_network
    virtual_network = oci.core.VirtualNetworkClient(config, signer=signer)
    if cmd.proxy:
        virtual_network.base_client.session.proxies = {'https': cmd.proxy}

    ############################################
    # Loop on all compartments
    ############################################
    try:
        for compartment in compartments:
            if compartment.id != tenancy.id and compartment.lifecycle_state != oci.identity.models.Compartment.LIFECYCLE_STATE_ACTIVE:
                continue

            print("    Compartment " + (str(compartment.name) + "... ").ljust(35), end="")
            cnt = 0

            ############################################
            # Retrieve ip sec connections
            ############################################
            ipsec_connnections = []
            try:
                ipsec_connnections = oci.pagination.list_call_get_all_results(
                    virtual_network.list_ip_sec_connections,
                    compartment.id
                ).data

            except oci.exceptions.ServiceError as e:
                if check_service_error(e.code):
                    warnings += 1
                    print("Warnings ")
                    continue
                raise

            # loop on array,
            # ipsec_conn = oci.core.models.IPSecConnection
            for ipsec_conn in ipsec_connnections:
                if ipsec_conn.lifecycle_state != oci.core.models.IPSecConnection.LIFECYCLE_STATE_AVAILABLE:
                    continue

                ############################################
                # Retrieve DRG Redundancy
                ############################################
                drg_redundancy = ""
                try:
                    # redundancy = oci.core.models.DrgRedundancyStatus
                    redundancy = virtual_network.get_drg_redundancy_status(ipsec_conn.drg_id).data
                    if redundancy:
                        drg_redundancy = str(redundancy.status)
                except oci.exceptions.ServiceError as e:
                    if check_service_error(e.code):
                        print("DRG-Redun-Err ", end="")
                    pass

                ############################################
                # Get IPSEC connection tunnels
                ############################################
                data_tunnel = []
                try:
                    tunnels = virtual_network.list_ip_sec_connection_tunnels(ipsec_conn.id).data
                    # tunnel = oci.core.models.IPSecConnectionTunnel
                    for tunnel in tunnels:

                        # get bgp tunnel info
                        tunnel_bgp_info = ""
                        if tunnel.bgp_session_info:
                            bs = tunnel.bgp_session_info
                            tunnel_bgp_info = "BGP Status = " + str(bs.bgp_state) + ", Cust: " + str(bs.customer_interface_ip) + " (ASN = " + str(bs.customer_bgp_asn) + "), Oracle: " + str(bs.oracle_interface_ip) + " (ASN = " + str(bs.oracle_bgp_asn) + ")"

                        # append the data to data_tunnel
                        data_tunnel.append(
                            {'id': str(tunnel.id),
                             'status': str(tunnel.status),
                             'lifecycle_state': str(tunnel.lifecycle_state),
                             'status_date': tunnel.time_status_updated.strftime("%Y-%m-%d %H:%M"),
                             'display_name': str(tunnel.display_name),
                             'routing': str(tunnel.routing),
                             'cpe_ip': str(tunnel.cpe_ip),
                             'vpn_ip': str(tunnel.vpn_ip),
                             'bgp_info': tunnel_bgp_info}
                        )

                        cnt += 1
                except Exception as e:
                    print("Error (" + str(e) + ") ", end="")
                    pass

                # Add all data to the data array
                data.append({
                    'region_name': region_name,
                    'compartment_name': str(compartment.name),
                    'compartment_id': str(compartment.id),
                    'id': str(ipsec_conn.id),
                    'name': str(ipsec_conn.display_name),
                    'drg_id': str(ipsec_conn.drg_id),
                    'drg_redundancy': drg_redundancy,
                    'cpe_id': str(ipsec_conn.cpe_id),
                    'time_created': str(ipsec_conn.time_created),
                    'static_routes': [str(es) for es in ipsec_conn.static_routes],
                    'tunnels': data_tunnel
                })

            # print tunnels for the compartment
            if cnt == 0:
                print("(-)")
            else:
                print("(" + str(cnt) + " Tunnels)")

    except Exception as e:
        raise RuntimeError("\nError extracting IPSEC tunnels - " + str(e))

############################################
# Print Output as JSON
############################################
print_header("Output")
print(json.dumps(data, indent=4, sort_keys=False))

if warnings > 0:
    print_header(str(warnings) + " Warnings appeared")
print_header("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
