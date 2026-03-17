# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# list_all_compartments_in_tenancy.py
#
# @author: Adi Zohar
#
# Supports Python 3
#
# DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes
##########################################################################
# Info:
#    List all compartments in Tenancy and print Id, Name and Path
#
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of ListCompartments group with below Policy rules:
#          Allow group ListCompartments to inspect compartments in tenancy
#          Allow group ListCompartments to inspect tenancies in tenancy
#
#    Option 2 - Instance Principle
#       Compute instance part of DynListCompartments dynamic group with policy rules:
#          Allow dynamic group DynListCompartments to inspect compartments in tenancy
#          Allow dynamic group DynListCompartments to inspect tenancies in tenancy
#
##########################################################################
# Modules Included:
# - oci.identity.IdentityClient
#
# APIs Used:
# - IdentityClient.list_compartments         - Policy COMPARTMENT_INSPECT
# - IdentityClient.get_compartment           - Policy COMPARTMENT_INSPECT
# - IdentityClient.get_tenancy               - Policy TENANCY_INSPECT
#
##########################################################################
# Application Command line parameters
#
#   -t config  - Config file section to use (tenancy profile)
#   -p proxy   - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip        - Use Instance Principals for Authentication
#   -dt        - Use Instance Principals with delegation token for cloud shell
#   -csv  name - Write to CSV file
#   -json name - Write to JSON file
##########################################################################
from __future__ import print_function
import sys
import argparse
import datetime
import oci
import os
import platform
import csv
import json

version = "25.04.01"
command_line = ' '.join(x for x in sys.argv[1:])


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


##################################################################################
# get_date
# Example of Date 2022-08-20T23:32:54.491Z -> 2022-08-20 23:32:54
##################################################################################
def get_date(val):
    if not val:
        return ''
    return str(val)[0:19].replace("T", " ")


##########################################################################
# get value from service
##########################################################################
def get_value(in_value):
    try:
        out_value = ""
        if in_value:
            if str(in_value).lower() == "false" or str(in_value).lower() == "true":
                out_value = str(in_value).capitalize()
            elif str(in_value).lower() == "none":
                out_value = ""
            else:
                out_value = str(in_value)
        return out_value

    except Exception as e:
        raise RuntimeError("Error in get_value: " + str(e.args))


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

    all_compartments = []
    tree_compartments = []
    root_compartment = {}

    print("Loading Compartments...")
    try:
        all_compartments = oci.pagination.list_call_get_all_results(
            identity.list_compartments,
            tenancy.id,
            compartment_id_in_subtree=True
        ).data

        # get root compartment
        root_compartment = identity.get_compartment(tenancy.id).data

        print("    Compartments Loaded.")

    except Exception as e:
        raise RuntimeError("Error in identity_read_compartments: " + str(e.args))

    ###################################################
    # Build Compartments
    # return nested compartment list
    ###################################################
    def build_nested_compartments(cid, path):
        try:
            compartment_list = [item for item in all_compartments if str(item.compartment_id) == str(cid)]

            if path != "":
                path = path + " / "

            for c in compartment_list:
                if c.lifecycle_state == 'ACTIVE':
                    cvalue = {
                        'id': get_value(c.id),
                        'name': get_value(c.name),
                        'description': get_value(c.description),
                        'time_created': get_date(c.time_created),
                        'is_accessible': get_value(c.is_accessible),
                        'lifecycle_state': get_value(c.lifecycle_state),
                        'inactive_status': get_value(c.inactive_status),
                        'path': path + get_value(c.name),
                        'defined_tags': [] if c.defined_tags is None else c.defined_tags,
                        'freeform_tags': [] if c.freeform_tags is None else c.freeform_tags
                    }
                    tree_compartments.append(cvalue)
                    build_nested_compartments(c.id, cvalue['path'])

        except Exception as error:
            raise Exception("Error in build_compartments_nested: " + str(error.args))

    ###################################################
    # End Internal Function
    ###################################################

    # Build the Compartments Hierarchy
    print("Build Compartments Hierarchy...")
    build_nested_compartments(tenancy.id, "")

    # Add the root compartment:
    root_compartment_value = {
        'id': get_value(root_compartment.id),
        'name': get_value(root_compartment.name),
        'description': get_value(root_compartment.description),
        'time_created': get_date(root_compartment.time_created),
        'is_accessible': get_value(root_compartment.is_accessible),
        'lifecycle_state': 'ACTIVE',
        'inactive_status': "",
        'path': "/ " + get_value(root_compartment.name) + " (root)",
        'defined_tags': [] if root_compartment.defined_tags is None else root_compartment.defined_tags,
        'freeform_tags': [] if root_compartment.freeform_tags is None else root_compartment.freeform_tags
    }
    tree_compartments.append(root_compartment_value)

    # sort by compartment path
    sorted_compartments = sorted(tree_compartments, key=lambda k: k['path'])

    print("    Build Compartments Hierarchy completed.")

    return sorted_compartments


##########################################################################
# create csv file
##########################################################################
def export_to_csv_file(file_name, data):

    try:
        # if no data
        if len(data) == 0:
            return

        # generate fields keys
        fields = []
        for dict_ in data:
            for key in dict_:
                if key not in fields:
                    fields.append(key)

        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)

            # write header
            writer.writeheader()

            for row in data:
                writer.writerow(row)

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
parser.add_argument('-csv', type=argparse.FileType('w'), dest='csv_file', help="Output to CSV file")
parser.add_argument('-json', type=argparse.FileType('w'), dest='json_file', help="Output to JSON file")
cmd = parser.parse_args()

######################################################
# Start and Print Info
######################################################
start_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print_header("Running List Compartments")
print("Author          : Adi Zohar")
print("Disclaimer      : This is not an official Oracle application. (Please use --help for help)")
print("Machine         : " + platform.node() + " (" + platform.machine() + ")")
print("App Version     : " + version)
print("OCI SDK Version : " + oci.version.__version__)
print("Python Version  : " + platform.python_version())
if cmd.is_instance_principals:
    print("Authentication  : Instance Principals")
elif cmd.is_delegation_token:
    print("Authentication  : Instance Principals With Delegation Token")
else:
    print("Authentication  : Config File")
print("Date/Time       : " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
print("Command Line    : " + command_line)
print("")

######################################################
# Identity extract compartments
######################################################
config, signer = create_signer(cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)
compartments = []
tenancy = None
try:
    print("\nConnecting to Identity Service...")
    identity = oci.identity.IdentityClient(config, signer=signer)
    if cmd.proxy:
        identity.base_client.session.proxies = {'https': cmd.proxy}

    tenancy = identity.get_tenancy(config["tenancy"]).data

    print("Tenant Name : " + str(tenancy.name))
    print("Tenant Id   : " + tenancy.id)
    print("")

    compartments = identity_read_compartments(identity, tenancy)

    print_header("Output " + str(len(compartments)) + " Compartments")

    for c in compartments:
        print(c['path'])

    if cmd.csv_file or cmd.json_file:
        print_header("Output to Files")

    if cmd.csv_file and compartments:
        export_to_csv_file(cmd.csv_file.name, compartments)
        print("")
        print("Exported to CSV file " + cmd.csv_file.name)

    if cmd.json_file and compartments:
        with open(cmd.json_file.name, 'w') as outfile:
            json.dump(compartments, outfile, indent=4, sort_keys=False)
        print("")
        print("Exported to JSON file " + cmd.json_file.name)

    print_header("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
except Exception as e:
    raise RuntimeError("\nError extracting compartments section - " + str(e))
