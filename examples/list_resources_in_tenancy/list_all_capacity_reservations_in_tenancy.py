# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# list_all_capacity_reservations_in_tenancy.py
#
# @author    : Adi Zohar
# @Contribute: Joe Scanlon
#
# Supports Python 3
#
# DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes
##########################################################################
# Info:
#    List all Capacity Reservations in Tenancy
#
##########################################################################
# Application Command line parameters
#
#   -t config   - Config file section to use (tenancy profile)
#   -p proxy    - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip         - Use Instance Principals for Authentication
#   -dt         - Use Instance Principals with delegation token for cloud shell
#   -cp compart - Filter by Comcpartment
#   -rg region  - Filter by Region
#   -csv file   - print to csv file
#   -json       - print as JSON
#
##########################################################################
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of ListComputeCapacityGroup group with below Policy rules:
#          Allow group ListComputeCapacityGroup to inspect compartments in tenancy
#          Allow group ListComputeCapacityGroup to inspect tenancies in tenancy
#          Allow group ListComputeCapacityGroup to read compute-capacity-reservations in tenancy
#
#    Option 2 - Instance Principle
#       Compute instance part of DynListComputeCapacityGroup dynamic group with policy rules:
#          Allow dynamic group DynListComputeCapacityGroup to inspect compartments in tenancy
#          Allow dynamic group DynListComputeCapacityGroup to inspect tenancies in tenancy
#          Allow dynamic group DynListComputeCapacityGroup to read compute-capacity-reservations in tenancy
#
##########################################################################
from __future__ import print_function
import sys
import argparse
import datetime
import oci
import json
import os
import csv


##########################################################################
# Print header centered
##########################################################################
def print_header(name, category):
    options = {0: 120, 1: 100, 2: 90, 3: 85}
    chars = int(options[category])
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
            print_header("Error obtaining instance principals certificate, aborting", 1)
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
# Print Limit
##########################################################################
def print_reservations(reservation_data):

    try:
        if not reservation_data:
            return

        for region in reservation_data:
            reg_name = region['region_name']
            reservation = region['data']
            print_header("Region " + reg_name, 1)

            sorted_list = sorted(reservation, key=lambda i: i['compartment_name'])

            prev_compartment = ""
            for ct in sorted_list:
                compartment_name = ct['compartment_name']
                lifecycle_state = ct['lifecycle_state']
                display_name = ct['display_name']
                value = "Reserved : " + str(ct['reserved_instance_count'])
                used = "Used : " + str(ct['used_instance_count'])
                available = "Available : " + str(ct['reserved_instance_count'] - ct['used_instance_count'])
                availability_domain = ct['availability_domain']
                shapes = ",".join(x['instance_shape'] + " (R=" + str(x['reserved_count']) + ":U=" + str(x['used_count']) + ")" for x in ct['config'])

                if not prev_compartment or prev_compartment != compartment_name:
                    print_header("Compartment " + compartment_name, 2)

                print("---> " + display_name + " (" + lifecycle_state + ")")
                print("     Reservation   = " + value + ", " + used + ", " + available)
                print("     Avail. Domain = " + availability_domain)
                print("     Config Shapes = " + shapes)
                print("")
                prev_compartment = compartment_name

    except Exception as e:
        raise RuntimeError("Error in print_reservations: " + str(e.args))


##########################################################################
# create csv file
##########################################################################
def export_to_csv_file(file_name, main_data):

    csv_data = []

    try:
        for region in main_data:
            reg_name = region['region_name']
            reservations = region['data']
            sorted_limit = sorted(reservations, key=lambda i: i['compartment_name'])

            for ct in sorted_limit:
                val = {
                    'region_name': reg_name,
                    'compartment_name': ct['compartment_name'],
                    'compartment_id': ct['compartment_id'],
                    'id': ct['id'],
                    'display_name': ct['display_name'],
                    'lifecycle_state': ct['lifecycle_state'],
                    'availability_domain': ct['availability_domain'],
                    'is_default_reservation': ct['is_default_reservation'],
                    'time_created': ct['time_created'],
                    'reserved_instance_count': str(ct['reserved_instance_count']),
                    'used_instance_count': str(ct['used_instance_count']),
                    'shapes': ",".join(x['instance_shape'] for x in ct['config'])
                }
                csv_data.append(val)

        # if no data
        if len(csv_data) == 0:
            return

        # prepare keys and data
        result = [dict(item) for item in csv_data]
        fields = [key for key in result[0].keys()]

        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)

            # write header
            writer.writeheader()

            for row in result:
                writer.writerow(row)

        print("")
        print("Extracted to CSV file : --> " + file_name)

    except Exception as e:
        raise Exception("Error in export_to_csv_file: " + str(e.args))


##########################################################################
# Main
##########################################################################

# Get Command Line Parser
parser = argparse.ArgumentParser()
parser.add_argument('-t', default="", dest='config_profile', help='Config file section to use (tenancy profile)')
parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
parser.add_argument('-dt', action='store_true', default=False, dest='is_delegation_token', help='Use Delegation Token for Authentication')
parser.add_argument('-cp', default="", dest='filter_compartment', help='filter by compartment Name or Id')
parser.add_argument('-rg', default="", dest='filter_region', help='filter by Region')
parser.add_argument('-js', action='store_true', default=False, dest='print_json', help='print in JSON format')
parser.add_argument('-csv', default="", dest='csv', help="Output to CSV files, Input as file header")
cmd = parser.parse_args()

# Start print time info
start_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print_header("Running List Capacity Reservations", 0)
print("Starts at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
print("base on work By Adi Zohar, re-written by Joe Scanlon")
print("Command Line : " + ' '.join(x for x in sys.argv[1:]))

# Identity extract compartments
config, signer = create_signer(cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)
compartments = []
tenancy = None

# input parameters
filter_region = cmd.filter_region
filter_compartment = cmd.filter_compartment
print_json = cmd.print_json

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
print("\nLoading capacity reservations ...")

main_data = []
warnings = 0

for region_name in [str(es.region_name) for es in regions]:
    if filter_region and filter_region not in region_name:
        continue

    print("\nRegion " + region_name + "...")

    # set the region in the config and signer
    config['region'] = region_name
    signer.region = region_name
    region_data = []

    compute_client = oci.core.ComputeClient(config, signer=signer)
    if cmd.proxy:
        compute_client.base_client.session.proxies = {'https': cmd.proxy}

    ############################################
    # Loop on all compartments
    ############################################
    try:
        for compartment in compartments:
            if compartment.id != tenancy.id and compartment.lifecycle_state != oci.identity.models.Compartment.LIFECYCLE_STATE_ACTIVE:
                continue
            if filter_compartment and not (filter_compartment == compartment.name or filter_compartment == compartment.id):
                continue

            print("    Compartment " + (str(compartment.name) + "... ").ljust(35), end="")
            cnt = 0

            list_reservations = oci.pagination.list_call_get_all_results(
                compute_client.list_compute_capacity_reservations,
                compartment_id=compartment.id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # Get the data from response
            for capres in list_reservations:
                if (capres.lifecycle_state == 'DELETED' or capres.lifecycle_state == 'DELETING'):
                    continue

                values = ({
                    'region_name': region_name,
                    'compartment_name': str(compartment.name),
                    'compartment_id': str(compartment.id),
                    'id': str(capres.id),
                    'display_name': str(capres.display_name),
                    'lifecycle_state': str(capres.lifecycle_state),
                    'availability_domain': str(capres.availability_domain),
                    'is_default_reservation': str(capres.is_default_reservation),
                    'time_created': str(capres.time_created)[0:16],
                    'reserved_instance_count': capres.reserved_instance_count,
                    'used_instance_count': capres.used_instance_count,
                    'instances': [],
                    'config': []
                })

                # config
                reservation = compute_client.get_compute_capacity_reservation(
                    capacity_reservation_id=capres.id,
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

                config_data = []
                for res_config in reservation.instance_reservation_configs:
                    config_data.append({
                        'fault_domain': res_config.fault_domain,
                        'instance_shape': res_config.instance_shape,
                        'reserved_count': res_config.reserved_count,
                        'used_count': res_config.used_count,
                        'ocpus': res_config.instance_shape_config.ocpus,
                        'memory_in_gbs': res_config.instance_shape_config.memory_in_gbs
                    })
                values['config'] = config_data

                # instances
                # oci.core.models.CapacityReservationInstanceSummary
                list_instances = oci.pagination.list_call_get_all_results(
                    compute_client.list_compute_capacity_reservation_instances,
                    capacity_reservation_id=capres.id,
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

                instances_data = []
                for inst in list_instances:
                    instances_data.append({
                        'fault_domain': inst.fault_domain,
                        'shape': inst.shape,
                        'memory_in_gbs': inst.shape_config.memory_in_gbs,
                        'ocpus': inst.shape_config.ocpus
                    })
                values['instances'] = instances_data

                region_data.append(values)
                cnt += 1

            if cnt == 0:
                print("(-)")
            else:
                print("(" + str(cnt) + " Instances)")

        # add region data
        main_data.append({
            'region_name': region_name,
            'data': region_data
        })

    except Exception as e:
        raise RuntimeError("\nError extracting capacity reservations - " + str(e))

############################################
# Print Output
############################################
if cmd.csv:
    export_to_csv_file(cmd.csv, main_data)
elif print_json:
    print(json.dumps(main_data, indent=4, sort_keys=False))
else:
    print_reservations(main_data)

if warnings > 0:
    print_header(str(warnings) + " Warnings appeared", 0)
print_header("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 0)
