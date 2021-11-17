# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# list_policies_in_tennacy
#
# @author: Adi Zohar
#
# Supports Python 3
#
# DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes
##########################################################################
# Application Command line parameters
#
#   -c config   - OCI CLI Config
#   -t profile  - profile inside the config file
#   -p proxy    - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip         - Use Instance Principals for Authentication
#   -dt         - Use Instance Principals with delegation token for cloud shell
#   -cp compart - Filter by Comcpartment
#   -cr compart - Filter by Comcpartment Path
#   -g group    - Filter by Group
#   -ia         - Ignore Any-User when filterring groups [Default=False]
#   -csv file   - print to csv file
#
##########################################################################
# Info:
#    List all policies in Tenancy
#
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of ListLimitsGroup group with below Policy rules:
#          Allow group ListLimitsGroup to inspect compartments in tenancy
#          Allow group ListLimitsGroup to inspect tenancies in tenancy
#          Allow group ListLimitsGroup to inspect policies in tenancy
#
#    Option 2 - Instance Principle
#       Compute instance part of DynListLimitsGroup dynamic group with policy rules:
#          Allow dynamic group DynListLimitsGroup to inspect compartments in tenancy
#          Allow dynamic group DynListLimitsGroup to inspect tenancies in tenancy
#          Allow dynamic group DynListLimitsGroup to inspect policies in tenancy
#
##########################################################################
# Modules Included:
# - oci.identity.IdentityClient
#
# APIs Used:
# - IdentityClient.list_compartments         - Policy COMPARTMENT_INSPECT
# - IdentityClient.get_tenancy               - Policy TENANCY_INSPECT
# - IdentityClient.list_policies             - Policy POLICY_READ
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
def create_signer(config_file, config_profile, is_instance_principals, is_delegation_token):

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
            (config_file if config_file else oci.config.DEFAULT_LOCATION),
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
def identity_read_compartments(identity, tenancy, filter_by_compartment_name, filter_by_compartment_path):

    compartments = []
    print("Loading Compartments...")

    try:
        # read all compartments to variable
        all_compartments = []
        try:
            all_compartments = oci.pagination.list_call_get_all_results(
                identity.list_compartments,
                tenancy.id,
                compartment_id_in_subtree=True,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

        except oci.exceptions.ServiceError as e:
            raise RuntimeError("Error in identity_read_compartments: " + str(e.args))

        ###################################################
        # Build Compartments
        # return nested compartment list
        ###################################################
        def build_compartments_nested(identity_client, cid, path):
            try:
                compartment_list = [item for item in all_compartments if str(item.compartment_id) == str(cid)]

                if path != "":
                    path = path + " / "

                for c in compartment_list:
                    if c.lifecycle_state == oci.identity.models.Compartment.LIFECYCLE_STATE_ACTIVE:
                        cvalue = {
                            'id': str(c.id),
                            'name': str(c.name),
                            'description': str(c.description),
                            'time_created': str(c.time_created),
                            'is_accessible': str(c.is_accessible),
                            'path': path + str(c.name)
                        }
                        compartments.append(cvalue)
                        build_compartments_nested(identity_client, c.id, cvalue['path'])

            except Exception as error:
                raise Exception("Error in build_compartments_nested: " + str(error.args))

        ###################################################
        # Add root compartment
        ###################################################
        try:
            tenc = identity.get_compartment(tenancy.id).data
            if tenc:
                cvalue = {
                    'id': str(tenc.id),
                    'name': str(tenc.name),
                    'description': str(tenc.description),
                    'time_created': str(tenc.time_created),
                    'is_accessible': str(tenc.is_accessible),
                    'path': "/ " + str(tenc.name) + " (root)"
                }
                compartments.append(cvalue)
        except Exception as error:
            raise Exception("Error in add_tenant_compartment: " + str(error.args))

        # Build the compartments
        build_compartments_nested(identity, tenancy.id, "")

        # sort the compartment
        sorted_compartments = sorted(compartments, key=lambda k: k['path'])

        # if not filtered by compartment return
        if not (filter_by_compartment_name or filter_by_compartment_path):
            print(str(len(sorted_compartments)) + " Compartments Loaded")
            return sorted_compartments

        filtered_compart = []

        # if filter by compartment, then reduce list and return new list
        if filter_by_compartment_name:
            for x in sorted_compartments:
                if filter_by_compartment_name in x['name'] or filter_by_compartment_name in x['id']:
                    filtered_compart.append(x)

        # if filter by path compartment path, then reduce list and return new list
        if filter_by_compartment_path:
            for x in sorted_compartments:
                if filter_by_compartment_path in x['path']:
                    filtered_compart.append(x)

        print(str(len(filtered_compart)) + " Filtered Compartments Loaded")
        return filtered_compart

    except oci.exceptions.RequestException:
        raise
    except Exception as e:
        raise Exception("Error in identity_read_compartments: " + str(e.args))


##########################################################################
# Check if group in statement
##########################################################################
def check_group_in_statement(statement, group, not_include_anyuser):
    try:
        # split statement words
        array = str(statement).lower().replace(" ,", ",").replace(", ", ",").replace(" id ", "").split(" ")
        if len(array) < 4:
            return False

        # if anyuser - return true
        if not not_include_anyuser and (array[1] == "any-user" or array[1] == "anyuser"):
            return True

        # if group or dynamic group
        if array[1] == "group" or array[2] == "dynamic-group":
            for sgroup in array[2].split(","):
                if str(group).lower() == sgroup:
                    return True

        return False

    except Exception as e:
        raise RuntimeError("Error in check_group_in_statement: " + str(e.args))


##########################################################################
# Print Limit
##########################################################################
def print_policies(main_data):

    try:
        if not main_data:
            return

        for compartment in main_data:
            compartment_path = compartment['compartment_path']
            policies = compartment['policies']
            print_header("Compartment " + compartment_path, 1)

            for policy in policies:
                policy_name = policy['name']
                statements = policy['statements']

                print("---> " + policy_name)
                for statement in statements:
                    print(statement)
                print("")

    except Exception as e:
        raise RuntimeError("Error in print_policies: " + str(e.args))


##########################################################################
# create csv file
##########################################################################
def export_to_csv_file(file_name, main_data):

    csv_data = []

    try:
        for ct in main_data:
            for policy in ct['policies']:
                for statement in policy['statements']:
                    val = {
                        'compartment_path': ct['compartment_path'],
                        'compartment_name': ct['compartment_name'],
                        'compartment_id': ct['compartment_id'],
                        'policy_id': policy['id'],
                        'policy_name': policy['name'],
                        'description': policy['description'],
                        'time_created': policy['time_created'],
                        'lifecycle_state': policy['lifecycle_state'],
                        'statement': statement
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
parser.add_argument('-c', default="", dest='config_file', help='OCI CLI Config file')
parser.add_argument('-t', default="", dest='config_profile', help='Config Profile inside the config file')
parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
parser.add_argument('-cp', default="", dest='filter_compn', help='filter by compartment Name or Id')
parser.add_argument('-cr', default="", dest='filter_compr', help='filter by compartment Path')
parser.add_argument('-g', default="", dest='filter_group', help='filter by IAM Group or Dynamic Group')
parser.add_argument('-ia', action='store_true', default=False, dest='not_include_anyuser', help='Do not include Any-User when filterring groups [Default=False]')
parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
parser.add_argument('-dt', action='store_true', default=False, dest='is_delegation_token', help='Use Delegation Token for Authentication')
parser.add_argument('-json', action='store_true', default=False, dest='print_json', help='Output to JSON')
parser.add_argument('-csv', default="", dest='csv', help="Output to CSV files, Input as file header")
cmd = parser.parse_args()

# Start print time info
start_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print_header("Running List Policies", 0)

print("Starts at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
print("Written By Adi Zohar, Oct 2021")
print("This is not an official Oracle application,  It does not supported by Oracle Support")
print("Command Line : " + ' '.join(x for x in sys.argv[1:]))

# Identity extract compartments
config, signer = create_signer(cmd.config_file, cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)
compartments = []
tenancy = None
filter_compartment_name = cmd.filter_compn
filter_compartment_path = cmd.filter_compr
print_json = cmd.print_json
filter_group = cmd.filter_group
not_include_anyuser = cmd.not_include_anyuser

try:
    print("\nConnecting to Identity Service...")
    identity = oci.identity.IdentityClient(config, signer=signer)
    if cmd.proxy:
        identity.base_client.session.proxies = {'https': cmd.proxy}

    tenancy = identity.get_tenancy(config["tenancy"]).data

    print("Tenant Name : " + str(tenancy.name))
    print("Tenant Id   : " + tenancy.id)
    print("")

    compartments = identity_read_compartments(identity, tenancy, filter_compartment_name, filter_compartment_path)

except Exception as e:
    raise RuntimeError("\nError extracting compartments section - " + str(e))


############################################
# Loop on all regions
############################################
print("\nLoading Policies...")
main_data = []
warnings = 0

for compartment in compartments:
    print(".", end="")

    try:
        policies = oci.pagination.list_call_get_all_results(
            identity.list_policies,
            compartment['id'],
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        ).data

        if policies:
            data_policies = []

            # loop on policies
            for policy in policies:
                data_statements = []

                # loop on statements
                for statement in policy.statements:
                    if filter_group and not check_group_in_statement(statement, filter_group, not_include_anyuser):
                        continue
                    data_statements.append(str(statement))

                # if statements exist add policy
                if data_statements:
                    data_policies.append({
                        'id': policy.id,
                        'name': policy.name,
                        'description': str(policy.description),
                        'time_created': str(policy.time_created),
                        'lifecycle_state': str(policy.lifecycle_state),
                        'statements': data_statements
                    })

            if data_policies:
                dataval = {
                    'compartment_id': compartment['id'],
                    'compartment_name': compartment['name'],
                    'compartment_path': compartment['path'],
                    'policies': data_policies
                }
                main_data.append(dataval)

    except oci.exceptions.ServiceError as e:
        if check_service_error(e.code):
            warnings += 1
            print("w", end="")
            continue
        raise

    except Exception as e:
        raise RuntimeError("\nError extracting policies - " + str(e))

############################################
# Print Output
############################################
if cmd.csv:
    export_to_csv_file(cmd.csv, main_data)
elif print_json:
    print(json.dumps(main_data, indent=4, sort_keys=False))
else:
    print_policies(main_data)

if warnings > 0:
    print_header(str(warnings) + " Warnings appeared", 1)
print_header("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 1)
