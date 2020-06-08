#!/usr/bin/env python3
##########################################################################
# Copyright(c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.
# list_compute_tags_in_tenancy.py
#
# @author: Adi Zohar
#
# Supports Python  3
#
# coding: utf-8
##########################################################################
# Info:
#    List all compute tags in Tenancy
#
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of ListComputeTagsGroup group with below Policy rules:
#          Allow group ListComputeTagsGroup to inspect compartments in tenancy
#          Allow group ListComputeTagsGroup to inspect tenancies in tenancy
#          Allow group ListComputeTagsGroup to inspect instances in tenancy
#
#    Option 2 - Instance Principle
#       Compute instance part of DynListComputeTagsGroup dynamic group with policy rules:
#          Allow dynamic group DynListComputeTagsGroup to inspect compartments in tenancy
#          Allow dynamic group DynListComputeTagsGroup to inspect tenancies in tenancy
#          Allow dynamic group DynListComputeTagsGroup to inspect instances in tenancy
#
##########################################################################
# Modules Included:
# - oci.identity.IdentityClient
#
# APIs Used:
# - IdentityClient.list_compartments         - Policy COMPARTMENT_INSPECT
# - IdentityClient.get_tenancy               - Policy TENANCY_INSPECT
# - IdentityClient.list_region_subscriptions - Policy TENANCY_INSPECT
# - ComputeClient.list_instances             - Policy
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

            # check if file exist
            if not os.path.isfile(env_config_file):
                print("*** Config File " + env_config_file + " does not exist, Abort. ***")
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
print_header("Running List Compute Tags")
print("Written By Adi Zohar, June 2020")
print("Starts at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
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
print("\nLoading Compute Instances...")
data = []
warnings = 0
for region_name in [str(es.region_name) for es in regions]:

    print("\nRegion " + region_name + "...")

    # set the region in the config and signer
    config['region'] = region_name
    signer.region = region_name

    # connect to virtual_network
    compute_client = oci.core.ComputeClient(config, signer=signer)
    if cmd.proxy:
        compute_client.base_client.session.proxies = {'https': cmd.proxy}

    ############################################
    # Loop on all compartments
    ############################################
    try:
        for compartment in compartments:

            # skip non active compartments
            if compartment.id != tenancy.id and compartment.lifecycle_state != oci.identity.models.Compartment.LIFECYCLE_STATE_ACTIVE:
                continue

            print("    Compartment " + (str(compartment.name) + "... ").ljust(35), end="")
            cnt = 0

            ############################################
            # Retrieve instances
            ############################################
            instances = []
            try:
                instances = oci.pagination.list_call_get_all_results(
                    compute_client.list_instances,
                    compartment.id,
                    sort_by="DISPLAYNAME"
                ).data

            except oci.exceptions.ServiceError as e:
                if check_service_error(e.code):
                    warnings += 1
                    print("Warnings ")
                    continue
                raise

            # loop on instances array
            # instance = oci.core.models.Instance
            for instance in instances:
                if (instance.lifecycle_state == oci.core.models.Instance.LIFECYCLE_STATE_TERMINATED or
                        instance.lifecycle_state == oci.core.models.Instance.LIFECYCLE_STATE_TERMINATING):
                    continue

                ############################################
                # get the info
                ############################################

                shape = {}
                if instance.shape_config:
                    sc = instance.shape_config
                    shape['ocpu'] = sc.ocpus
                    shape['memory_gb'] = sc.memory_in_gbs
                    shape['gpu_description'] = str(sc.gpu_description)
                    shape['gpus'] = str(sc.gpus)
                    shape['max_vnic_attachments'] = sc.max_vnic_attachments
                    shape['networking_bandwidth_in_gbps'] = sc.networking_bandwidth_in_gbps
                    shape['processor_description'] = str(sc.processor_description)

                value = ({
                    'region_name': region_name,
                    'compartment_name': str(compartment.name),
                    'compartment_id': str(compartment.id),
                    'id': str(instance.id),
                    'name': str(instance.display_name),
                    'availability_domain': str(instance.availability_domain),
                    'lifecycle_state': str(instance.lifecycle_state),
                    'time_created': str(instance.time_created),
                    'shape': str(instance.shape),
                    'shape_config': shape,
                    'defined_tags': instance.defined_tags,
                    'freeform_tags': instance.freeform_tags
                })

                data.append(value)
                cnt += 1

            # print instances for the compartment
            if cnt == 0:
                print("(-)")
            else:
                print("(" + str(cnt) + " Instances)")

    except Exception as e:
        raise RuntimeError("\nError extracting Instances - " + str(e))

############################################
# Print Output as JSON
############################################
print_header("Output")
print(json.dumps(data, indent=4, sort_keys=False))

if warnings > 0:
    print_header(str(warnings) + " Warnings appeared")
print_header("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
