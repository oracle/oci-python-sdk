# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# list_limits_per_compartments.py
#
# @author: Adi Zohar
#
# Supports Python 3
##########################################################################
# Application Command line parameters
#
#   -t config   - Config file section to use (tenancy profile)
#   -p proxy    - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip         - Use Instance Principals for Authentication
#   -dt         - Use Instance Principals with delegation token for cloud shell
#   -rg region  - Filter Region
#   -cp compart - Filter by Comcpartment
#   -sr service - Filter by Service
#   -js         - print in JSON format
#
##########################################################################
# Info:
#    List all limits per compartments in Tenancy
#
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of ListLimitsGroup group with below Policy rules:
#          Allow group ListLimitsGroup to inspect compartments in tenancy
#          Allow group ListLimitsGroup to inspect tenancies in tenancy
#          Allow group ListLimitsGroup to inspect limits in tenancy
#          Allow group ListLimitsGroup to read resource-availability in tenancy
#
#    Option 2 - Instance Principle
#       Compute instance part of DynListLimitsGroup dynamic group with policy rules:
#          Allow dynamic group DynListLimitsGroup to inspect compartments in tenancy
#          Allow dynamic group DynListLimitsGroup to inspect tenancies in tenancy
#          Allow dynamic group DynListLimitsGroup to inspect ipsec-connections in tenancy
#          Allow dynamic group DynListLimitsGroup to inspect limits in tenancy
#          Allow dynamic group DynListLimitsGroup to read resource-availability in tenancy
#
##########################################################################
# Modules Included:
# - oci.identity.IdentityClient
# - oci.limits.LimitsClient
#
# APIs Used:
# - IdentityClient.list_compartments         - Policy COMPARTMENT_INSPECT
# - IdentityClient.get_tenancy               - Policy TENANCY_INSPECT
# - IdentityClient.list_region_subscriptions - Policy TENANCY_INSPECT
# - LimitsClient.list_services               - inspect limits
# - LimitsClient.list_limit_values           - inspect limits
# - LimitsClient.get_resource_availability   - read resource-availability
#
##########################################################################
from __future__ import print_function
import sys
import argparse
import datetime
import oci
import json
import os
import time


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
            print_header("Error obtaining instance principals certificate, aborting", 0)
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
def print_limits(limits_data):

    try:
        if not limits_data:
            return

        for region in limits_data:
            reg_name = region['region_name']
            limits = region['data']
            print_header("Region " + reg_name, 1)

            sorted_limit = sorted(limits, key=lambda i: i['compartment_name'])

            prev_compartment = ""
            for ct in sorted_limit:
                compartment_name = ct['compartment_name']
                limit_name = ct['limit_name'].ljust(37)
                value = " = " + ct['value'].ljust(16)[0:16]
                used = (" Used = " + ct['used'].ljust(16)[0:16] + " ") if ct['used'] != "" else str(" ").ljust(25)
                available = (" Available = " + ct['available'].ljust(16)[0:16] + " ") if ct['available'] != "" else str(" ").ljust(30)
                scope = " SCOPE=" + ct['scope_type'].ljust(8) + ct['availability_domain']

                if not prev_compartment or prev_compartment != compartment_name:
                    print_header(compartment_name, 2)

                print(str(ct['name'] + " ").ljust(20) + limit_name + value + used + available + scope)
                prev_compartment = compartment_name

            print("")
            print("* numbers trimmed to 16 digits, if you need full value, please use json output")
            print("")

    except Exception as e:
        raise RuntimeError("Error in print_limits: " + str(e.args))


##########################################################################
# Main
##########################################################################

# Get Command Line Parser
parser = argparse.ArgumentParser()
parser.add_argument('-t', default="", dest='config_profile', help='Config file section to use (tenancy profile)')
parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
parser.add_argument('-rg', default="", dest='filter_region', help='filter by region (i.e. us-ashburn-1) ')
parser.add_argument('-cp', default="", dest='filter_comp', help='filter by compartment (i.e. production) ')
parser.add_argument('-sr', default="", dest='filter_service', help='filter by servoce (i.e. compute) ')
parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
parser.add_argument('-dt', action='store_true', default=False, dest='is_delegation_token', help='Use Delegation Token for Authentication')
parser.add_argument('-js', action='store_true', default=False, dest='print_json', help='print in JSON format')
cmd = parser.parse_args()

# Start print time info
start_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("############################################################")
print("#                   Running List Limits                    #")
print("#  This process takes long time to run on the full tenant  #")
print("#  I would advise to filter region, compartment or service #")
print("#  Use --help for help                                     #")
print("############################################################")

print("Starts at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
print("Written By Adi Zohar, Sep 2021")
print("Command Line : " + ' '.join(x for x in sys.argv[1:]))

# Identity extract compartments
config, signer = create_signer(cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)
compartments = []
tenancy = None
filter_region = cmd.filter_region
filter_compartment = cmd.filter_comp
filter_service = cmd.filter_service
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
print("\nLoading Limits...")
main_data = []
warnings = 0
for region_name in [str(es.region_name) for es in regions]:
    if filter_region and str(filter_region) not in region_name:
        continue

    region_data = []

    print("\nRegion " + region_name + "...")

    # set the region in the config and signer
    config['region'] = region_name
    signer.region = region_name

    # connect to virtual_network
    limits_client = oci.limits.LimitsClient(config, signer=signer)
    if cmd.proxy:
        limits_client.base_client.session.proxies = {'https': cmd.proxy}

    ############################################
    # Loop on all compartments
    ############################################
    try:

        # Read Services
        print("    Read Services... ", end="")
        services = []
        try:
            services = oci.pagination.list_call_get_all_results(
                limits_client.list_services,
                tenancy.id,
                sort_by="name",
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data
        except oci.exceptions.ServiceError as e:
            if check_service_error(e.code):
                warnings += 1
                print("Error Reading Services..")
                continue
            raise

        print(str(len(services)) + " loaded, Running on Compartments..")

        ############################################
        # Loop on Services
        ############################################
        start_time = time.time()
        for service in services:
            if filter_service and str(filter_service) not in service.name:
                continue

            ############################################
            # Retrieve limits for each service
            ############################################
            limits = []
            try:
                limits = oci.pagination.list_call_get_all_results(
                    limits_client.list_limit_values,
                    tenancy.id,
                    service_name=service.name,
                    sort_by="name",
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

            except oci.exceptions.ServiceError as e:
                if check_service_error(e.code):
                    warnings += 1
                    print("Warnings ")
                    continue
                raise

            print("    " + str(service.name + " (" + str(len(limits)) + " limits) ").ljust(35), end="")

            ###########################################################
            # Loop each compartment to get the availability for each
            ###########################################################
            cnt = 0
            for compartment in compartments:
                if compartment.id != tenancy.id and compartment.lifecycle_state != oci.identity.models.Compartment.LIFECYCLE_STATE_ACTIVE:
                    continue
                if filter_compartment and str(filter_compartment) not in compartment.name and str(filter_compartment) not in str(compartment.id):
                    continue

                print(".", end="")

                # oci.limits.models.LimitValueSummary
                for limit in limits:
                    val = {
                        'compartment_name': str(compartment.name),
                        'compartment_id': str(compartment.id),
                        'name': str(service.name),
                        'description': str(service.description),
                        'limit_name': str(limit.name),
                        'availability_domain': ("" if limit.availability_domain is None else str(limit.availability_domain)),
                        'scope_type': str(limit.scope_type),
                        'value': str(limit.value),
                        'used': "",
                        'available': ""
                    }

                    # only run on limit > 0
                    if limit.value == 0:
                        continue

                    # get usage per limit if available
                    try:
                        usage = []
                        if limit.scope_type == "AD":
                            usage = limits_client.get_resource_availability(service.name, limit.name, compartment.id, availability_domain=limit.availability_domain).data
                        else:
                            usage = limits_client.get_resource_availability(service.name, limit.name, compartment.id).data

                        # oci.limits.models.ResourceAvailability
                        if usage.used is not None:
                            val['used'] = str(usage.used)
                        if usage.available is not None:
                            val['available'] = str(usage.available)
                    except oci.exceptions.ServiceError as e:
                        if e.code == 'NotAuthorizedOrNotFound':
                            val['used'] = 'NotAuth'
                            val['available'] = 'NotAuth'
                            warnings += 1
                    except Exception:
                        pass

                    region_data.append(val)
                    cnt += 1

            # print info for the compartment
            et = time.time() - start_time
            print(" (" + str(cnt) + ") - "'{:02d}:{:02d}:{:02d}'.format(round(et // 3600), (round(et % 3600 // 60)), round(et % 60)))

        # add region data
        main_data.append({
            'region_name': region_name,
            'data': region_data
        })

    except Exception as e:
        raise RuntimeError("\nError extracting Limits - " + str(e))

############################################
# Print Output
############################################
# to print JSON
if print_json:
    print(json.dumps(main_data, indent=4, sort_keys=False))
else:
    print_limits(main_data)

if warnings > 0:
    print_header(str(warnings) + " Warnings appeared", 1)
print_header("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 1)
