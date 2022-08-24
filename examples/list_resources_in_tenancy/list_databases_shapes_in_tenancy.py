# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# list_databases_shapes_in_tenancy.py
#
# @author: Adi Zohar
#
# Supports Python 3
#
# DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes
##########################################################################
# Info:
#    List all databases shapes in tenancy, it includes, dbsystems, exacs , exacc and autonomous
#
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of ListDBSystemGroup group with below Policy rules:
#          Allow group ListDBSystemGroup to inspect compartments in tenancy
#          Allow group ListDBSystemGroup to inspect tenancies in tenancy
#          Allow group ListDBSystemGroup to read database-family in tenancy
#
#    Option 2 - Instance Principle
#       Compute instance part of DynListDBSystemGroup dynamic group with policy rules:
#          Allow dynamic group DynListDBSystemGroup to inspect compartments in tenancy
#          Allow dynamic group DynListDBSystemGroup to inspect tenancies in tenancy
#          Allow dynamic group DynListDBSystemGroup to read database-family in tenancy
#
##########################################################################
# Application Command line parameters
#
#   -c config   - OCI CLI Config
#   -t config   - Config file section to use (tenancy profile)
#   -p proxy    - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip         - Use Instance Principals for Authentication
#   -is         - Use session token for Authentication
#   -dt         - Use Instance Principals with delegation token for cloud shell
#   -rg region  - Filter Region
#   -cp compart - Filter by Compartment
#   -cr compart - Filter by Comcpartment Path
#   -js           output as JSON
#   -csv FILE     output to CSV and Screen
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
import time
import platform

version = "2022.08.23"


##########################################################################
# Print header centered
##########################################################################
def print_header(name, category=0):
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
def create_signer(config_file, config_profile, is_instance_principals, is_delegation_token, is_security_token):

    # if instance principals authentications
    if is_instance_principals:
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            config = {'region': signer.region, 'tenancy': signer.tenancy_id}
            return config, signer

        except Exception:
            print_header("Error obtaining instance principals certificate, aborting")
            raise SystemExit

    if is_security_token:
        try:
            # create signer from config and security token
            config = oci.config.from_file(
                (config_file if config_file else oci.config.DEFAULT_LOCATION),
                (config_profile if config_profile else oci.config.DEFAULT_PROFILE)
            )
            security_token_file = config.get("security_token_file")
            token = None
            with open(security_token_file, 'r') as f:
                token = f.read()
            private_key = oci.signer.load_private_key_from_file(config['key_file'])
            signer = oci.auth.signers.SecurityTokenSigner(token, private_key)
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

    return_compartments = []
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
                        return_compartments.append(cvalue)
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
                return_compartments.append(cvalue)
        except Exception as error:
            raise Exception("Error in add_tenant_compartment: " + str(error.args))

        # Build the compartments
        build_compartments_nested(identity, tenancy.id, "")

        # sort the compartment
        sorted_compartments = sorted(return_compartments, key=lambda k: k['path'])

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
# get_license_model
##########################################################################
def get_license_model(license_model):
    if license_model == "LICENSE_INCLUDED":
        return "INCL"
    elif license_model == "BRING_YOUR_OWN_LICENSE":
        return "BYOL"
    else:
        return license_model


##########################################################################
# get_database_edition
##########################################################################
def get_database_edition(database_edition):
    if database_edition == "ENTERPRISE_EDITION":
        return "EE"
    elif database_edition == "ENTERPRISE_EDITION_EXTREME_PERFORMANCE":
        return "XP"
    elif database_edition == "ENTERPRISE_EDITION_HIGH_PERFORMANCE":
        return "HP"
    elif database_edition == "STANDARD_EDITION":
        return "SE"
    else:
        return database_edition


##########################################################################
# Print databases on screen
##########################################################################
def print_databases(databases_data):

    try:
        if not databases_data:
            return

        for region in databases_data:
            reg_name = region['region_name']
            databases = region['data']
            print_header("Region " + reg_name, 0)

            sorted_databases = sorted(databases, key=lambda i: i['compartment_name'])
            print("Compartment               Display Name              DB Name                   Lifecycle     Shape                     OCPUs             Nodes             Lic   Edition")
            print("------------------------- ------------------------- ------------------------- ------------- ------------------------- ----------------- ----------------- ----- -------------------")

            for ct in sorted_databases:
                compartment_name = str(ct['compartment_name']).ljust(25) + " "
                display_name = str(ct['display_name']).ljust(25) + " "
                db_name = str(ct['db_name']).ljust(25) + " "
                shape = str(ct['shape']).ljust(25) + " "
                cpu_core_count = "OCPUs: " + str(ct['cpu_core_count']).ljust(10) + " "
                node_count = "Nodes: " + str(ct['node_count']).ljust(10) + " "
                lifecycle_state = str(ct['lifecycle_state']).ljust(13) + " "
                license_model = str(ct['license_model']).ljust(6)
                database_edition = str(ct['database_edition']).ljust(6)

                print(compartment_name + display_name + db_name + lifecycle_state + shape + cpu_core_count + node_count + license_model + database_edition)

            print("")
            print("")

    except Exception as e:
        raise RuntimeError("Error in print_databases: " + str(e.args))


##########################################################################
# create csv file
##########################################################################
def export_to_csv_file(file_name, database_data):

    csv_data = []

    try:
        for region in database_data:
            databases = region['data']
            sorted_databases = sorted(databases, key=lambda i: i['compartment_name'])

            for ct in sorted_databases:
                csv_data.append(ct)

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
# load_databases
##########################################################################
def load_dbsystems_exadatas_databases(database_client, region_name, compartment, num):
    global warnings
    local_data = []
    try:

        start_time = time.time()
        str_num = str(str(num) + ".").ljust(4)
        print("    " + str_num + " Compartment " + (str(compartment['path']) + "... ").ljust(50), end="")
        cnt = 0

        # Get Database homes
        homes = []
        try:
            homes = oci.pagination.list_call_get_all_results(
                database_client.list_db_homes,
                compartment['id'],
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

        except oci.exceptions.ServiceError as e:
            if check_service_error(e.code):
                warnings += 1
                print("Warnings ")
                return
            raise

        # Loop on database homes
        for db_home in homes:
            if (db_home.lifecycle_state == "TERMINATED" or db_home.lifecycle_state == "TERMINATING" or db_home.lifecycle_state == "FAILED"):
                continue

            list_databases = []
            try:
                list_databases = oci.pagination.list_call_get_all_results(
                    database_client.list_databases,
                    compartment_id=compartment['id'],
                    db_home_id=db_home.id,
                    sort_by="DBNAME",
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

            except oci.exceptions.ServiceError as e:
                if check_service_error(e.code):
                    warnings += 1
                    print("Warnings ")
                    return local_data
                raise

            # loop on the databases inside the home
            # dbs = oci.database.models.DatabaseSummary
            for dbs in list_databases:
                if dbs.lifecycle_state == "TERMINATED" or dbs.lifecycle_state == "TERMINATING" or dbs.lifecycle_state == "FAILED":
                    continue

                value = {
                    'tenant': str(tenancy.name),
                    'region_name': region_name,
                    'compartment_id': str(compartment['id']),
                    'compartment_path': str(compartment['path']),
                    'compartment_name': str(compartment['name']),
                    'id': str(dbs.id),
                    'display_name': "",
                    'db_name': str(dbs.db_name),
                    'db_unique_name': str(dbs.db_unique_name),
                    'db_workload': str(dbs.db_workload),
                    'time_created': str(dbs.time_created),
                    'lifecycle_state': str(dbs.lifecycle_state),
                    'db_system_id': str(dbs.db_system_id),
                    'vm_cluster_id': str(dbs.vm_cluster_id),
                    'home_version': str(db_home.db_version),
                    'type': "",
                    'shape': "",
                    'cpu_core_count': "",
                    'node_count': "",
                    'version': "",
                    'hostname': "",
                    'cluster_name': "",
                    'database_edition': "",
                    'license_model': "",
                    'role': "",
                    'adb_auto_scaling_enabled': "",
                    'error': "",
                    'extract_date': str(datetime.datetime.now().strftime("%Y-%m-%d"))
                }

                ####################
                # if VM Cluster
                ####################
                if dbs.vm_cluster_id:
                    # ExaCS
                    if "cloudvmcluster" in dbs.vm_cluster_id or "dbsystem" in dbs.vm_cluster_id:
                        try:
                            vm = database_client.get_cloud_vm_cluster(
                                dbs.vm_cluster_id,
                                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                            ).data

                            value['type'] = "ExaCS"
                            value['shape'] = str(vm.shape)
                            value['display_name'] = str(vm.display_name)
                            value['cpu_core_count'] = str(vm.cpu_core_count)
                            value['node_count'] = ("" if vm.node_count is None else str(vm.node_count))
                            value['version'] = str(vm.gi_version)
                            value['cluster_name'] = str(vm.cluster_name)
                            value['license_model'] = get_license_model(vm.license_model)
                            value['database_edition'] = "XP"

                        except oci.exceptions.ServiceError as e:
                            print("W", end="")
                            warnings += 1
                            value['error'] = str(e)
                    else:
                        try:
                            ####################
                            # EdxaCC
                            ####################
                            vm = database_client.get_vm_cluster(
                                dbs.vm_cluster_id,
                                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                            ).data

                            value['type'] = "ExaCC"
                            value['shape'] = str(vm.shape)
                            value['display_name'] = str(vm.display_name)
                            value['cpu_core_count'] = str(vm.cpus_enabled)
                            value['node_count'] = str(len(vm.db_servers))
                            value['version'] = str(vm.gi_version)
                            value['cluster_name'] = str(vm.display_name)
                            value['license_model'] = get_license_model(vm.license_model)
                            value['database_edition'] = "XP"

                        except oci.exceptions.ServiceError as e:
                            print("W", end="")
                            warnings += 1
                            value['error'] = str(e)

                ####################
                # if DB SystemId
                ####################
                if dbs.db_system_id and not dbs.vm_cluster_id:
                    try:
                        vm = database_client.get_db_system(
                            dbs.db_system_id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data
                        value['type'] = "DBSystem"
                        value['shape'] = str(vm.shape)
                        value['display_name'] = str(vm.display_name)
                        value['cpu_core_count'] = str(vm.cpu_core_count)
                        value['node_count'] = ("" if vm.node_count is None else str(vm.node_count))
                        value['version'] = ("" if vm.version is None else str(vm.version))
                        value['cluster_name'] = ("" if vm.cluster_name is None else str(vm.cluster_name))
                        value['license_model'] = get_license_model(vm.license_model)
                        value['database_edition'] = get_database_edition(vm.database_edition)

                    except oci.exceptions.ServiceError as e:
                        print("W", end="")
                        warnings += 1
                        value['error'] = str(e)

                # add the data
                cnt += 1
                local_data.append(value)

        # print total and time for the compartment
        et = time.time() - start_time
        print(" (" + str(cnt) + ") - "'{:02d}:{:02d}:{:02d}'.format(round(et // 3600), (round(et % 3600 // 60)), round(et % 60)))

        # return data
        return local_data

    except Exception as e:
        raise RuntimeError("\nError extracting databases in load_databases - " + str(e))


##########################################################################
# load_databases
##########################################################################
def load_autonomous_databases(database_client, region_name, compartment, num):
    global warnings
    local_data = []
    try:

        start_time = time.time()
        str_num = str(str(num) + ".").ljust(4)
        print("    " + str_num + " Compartment " + (str(compartment['path']) + "... ").ljust(50), end="")
        cnt = 0

        list_databases = []
        try:
            list_databases = oci.pagination.list_call_get_all_results(
                database_client.list_autonomous_databases,
                compartment['id'],
                sort_by="DISPLAYNAME",
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

        except oci.exceptions.ServiceError as e:
            if check_service_error(e.code):
                warnings += 1
                print("Warnings ")
                return
            raise

        # loop on the databases
        # dbs = oci.database.models.AutonomousDatabaseSummary
        for dbs in list_databases:
            if dbs.lifecycle_state == oci.database.models.AutonomousDatabaseSummary.LIFECYCLE_STATE_TERMINATED or dbs.lifecycle_state == oci.database.models.AutonomousDatabaseSummary.LIFECYCLE_STATE_UNAVAILABLE:
                continue

            value = {
                'tenant': str(tenancy.name),
                'region_name': region_name,
                'compartment_id': str(compartment['id']),
                'compartment_path': str(compartment['path']),
                'compartment_name': str(compartment['name']),
                'id': str(dbs.id),
                'display_name': str(dbs.display_name),
                'db_name': str(dbs.db_name),
                'db_unique_name': "",
                'db_workload': str(dbs.db_workload),
                'time_created': str(dbs.time_created),
                'lifecycle_state': str(dbs.lifecycle_state),
                'db_system_id': "",
                'vm_cluster_id': "",
                'home_version': "",
                'type': "Autonomous",
                'shape': "ADB-D" if dbs.is_dedicated else "ADB-S",
                'cpu_core_count': str(dbs.cpu_core_count),
                'node_count': "-",
                'version': str(dbs.db_version),
                'hostname': "",
                'cluster_name': "",
                'role': str(dbs.role),
                'database_edition': get_database_edition(str(dbs.database_edition)),
                'license_model': get_license_model(dbs.license_model),
                'adb_auto_scaling_enabled': str(dbs.is_auto_scaling_enabled),
                'error': "",
                'extract_date': str(datetime.datetime.now().strftime("%Y-%m-%d"))
            }

            # add the data
            cnt += 1
            local_data.append(value)

        # print total and time for the compartment
        et = time.time() - start_time
        print(" (" + str(cnt) + ") - "'{:02d}:{:02d}:{:02d}'.format(round(et // 3600), (round(et % 3600 // 60)), round(et % 60)))
        return local_data

    except Exception as e:
        raise RuntimeError("\nError extracting databases in load_autonomous - " + str(e))


##########################################################################
# Main
##########################################################################

# Get Command Line Parser
parser = argparse.ArgumentParser()
parser.add_argument('-c', default="", dest='config_file', help='OCI CLI Config file')
parser.add_argument('-t', default="", dest='config_profile', help='Config file section to use (tenancy profile)')
parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
parser.add_argument('-ip', default=False, action='store_true', dest='is_instance_principals', help='Use Instance Principals for Authentication')
parser.add_argument('-is', default=False, action='store_true', dest='is_security_token', help='Use Security Token for Authentication')
parser.add_argument('-dt', default=False, action='store_true', dest='is_delegation_token', help='Use Delegation Token for Authentication')
parser.add_argument('-rg', default="", dest='filter_region', help='filter by region (i.e. us-ashburn-1) ')
parser.add_argument('-cp', default="", dest='filter_compn', help='filter by compartment Name or Id')
parser.add_argument('-cr', default="", dest='filter_compr', help='filter by compartment Path')
parser.add_argument('-js', default=False, action='store_true', dest='print_json', help='print in JSON format')
parser.add_argument('-csv', default="", dest='csv', help="Output to CSV file, Input as file name")
cmd = parser.parse_args()

# Start print time info
start_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("########################################################################################################################")
print("#                                         Running List Database Shapes in Tenancy                                      #")
print("#                                                                                                                      #")
print("# Written By Adi Zohar, Aug 2022                                                                                       #")
print("# You can filter by region or compartment to run faster, please check --help for help                                  #")
print("#                                                                                                                      #")
print("# DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support                    #")
print("# It should NOT be used for billing utilization calculation purposes                                                   #")
print("########################################################################################################################")
print("Date/Time       : " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
print("Program         : " + "list_databases_shapes_in_tenancy.py")
print("Machine         : " + platform.node() + " (" + platform.machine() + ")")
print("Python Version  : " + platform.python_version())
print("App     Version : " + version)
print("OCI SDK Version : " + oci.version.__version__)
print("Command Line    : " + ' '.join(x for x in sys.argv[1:]))

# Identity extract compartments
config, signer = create_signer(cmd.config_file, cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token, cmd.is_security_token)
compartments = []
filter_region = cmd.filter_region
filter_compartment_name = cmd.filter_compn
filter_compartment_path = cmd.filter_compr
print_json = cmd.print_json
data = []
warnings = 0
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

    compartments = identity_read_compartments(identity, tenancy, filter_compartment_name, filter_compartment_path)

except Exception as e:
    raise RuntimeError("\nError extracting compartments section - " + str(e))


############################################
# Loop on all regions
############################################
print("\nLoading DBSystems and Exadatas...")
main_data = []
warnings = 0

for region_name in [str(es.region_name) for es in regions]:
    if filter_region and str(filter_region) not in region_name:
        continue

    region_data = []

    print("\nRegion " + region_name + "...\n")

    # set the region in the config and signer
    config['region'] = region_name
    signer.region = region_name

    # connect to virtual_network
    database_client = oci.database.DatabaseClient(config, signer=signer)
    if cmd.proxy:
        database_client.base_client.session.proxies = {'https': cmd.proxy}

    ############################################
    # Running on DBSystems and Exadatas
    ############################################
    print("  Running on DBSystems and Exadatas...")
    for num, compartment in enumerate(compartments, start=1):
        compartment_data = load_dbsystems_exadatas_databases(database_client, region_name, compartment, num)
        region_data.extend(compartment_data)

    ############################################
    # Running on Autonomous Databases
    ############################################
    print("")
    print("  Running on Autonomous Databases...")
    for num, compartment in enumerate(compartments, start=1):

        compartment_data = load_autonomous_databases(database_client, region_name, compartment, num)
        region_data.extend(compartment_data)

    main_data.append({
        'region_name': region_name,
        'data': region_data
    })

############################################
# Print Output as JSON
############################################
print_header("Output")
if cmd.csv:
    print_databases(main_data)
    export_to_csv_file(cmd.csv, main_data)
elif print_json:
    print(json.dumps(main_data, indent=4, sort_keys=False))
else:
    print_databases(main_data)

if warnings > 0:
    print_header(str(warnings) + " Warnings appeared")
print_header("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
