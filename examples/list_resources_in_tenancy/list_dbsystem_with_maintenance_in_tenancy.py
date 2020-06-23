# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# list_dbsystem_with_maintenance_in_tenancy.py
#
# @author: Adi Zohar
#
# Supports Python 3
##########################################################################
# Info:
#    List all dbsystems including maintenance in Tenancy
#
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of ListDBSystemGroup group with below Policy rules:
#          Allow group ListDBSystemGroup to inspect compartments in tenancy
#          Allow group ListDBSystemGroup to inspect tenancies in tenancy
#          Allow group ListDBSystemGroup to inspect db-systems in tenancy
#
#    Option 2 - Instance Principle
#       Compute instance part of DynListDBSystemGroup dynamic group with policy rules:
#          Allow dynamic group DynListDBSystemGroup to inspect compartments in tenancy
#          Allow dynamic group DynListDBSystemGroup to inspect tenancies in tenancy
#          Allow dynamic group DynListDBSystemGroup to inspect db-systems in tenancy
#
##########################################################################
# Modules Included:
# - oci.identity.IdentityClient
#
# APIs Used:
# - IdentityClient.list_compartments         - Policy COMPARTMENT_INSPECT
# - IdentityClient.get_tenancy               - Policy TENANCY_INSPECT
# - IdentityClient.list_region_subscriptions - Policy TENANCY_INSPECT
# - DatabaseClient.list_db_systems           - Policy DB_SYSTEM_INSPECT
# - DatabaseClient.get_maintenance_run       - Policy DB_SYSTEM_INSPECT
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
print_header("Running DB Systems Extract")
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


##########################################################################
# load_database_maintatance
##########################################################################
def load_database_maintatance(database_client, maintenance_run_id, db_system_name):
    try:
        if not maintenance_run_id:
            return {}

        # oci.database.models.MaintenanceRun
        mt = database_client.get_maintenance_run(maintenance_run_id).data
        val = {'id': str(mt.id),
               'display_name': str(mt.display_name),
               'description': str(mt.description),
               'lifecycle_state': str(mt.lifecycle_state),
               'time_scheduled': str(mt.time_scheduled),
               'time_started': str(mt.time_started),
               'time_ended': str(mt.time_ended),
               'target_resource_type': str(mt.target_resource_type),
               'target_resource_id': str(mt.target_resource_id),
               'maintenance_type': str(mt.maintenance_type),
               'maintenance_subtype': str(mt.maintenance_subtype),
               'maintenance_display': str(mt.display_name) + " ( " + str(mt.maintenance_type) + ", " + str(mt.maintenance_subtype) + ", " + str(mt.lifecycle_state) + " ), Scheduled: " + str(mt.time_scheduled)[0:16] + ((", Execution: " + str(mt.time_started)[0:16] + " - " + str(mt.time_ended)[0:16]) if str(mt.time_started) != 'None' else ""),
               'maintenance_alert': ""
               }

        # If maintenance is less than 14 days
        if mt.time_scheduled:
            delta = mt.time_scheduled.date() - datetime.date.today()
            if delta.days <= 14 and delta.days >= 0 and not mt.time_started:
                val['maintenance_alert'] = "DBSystem Maintenance is in " + str(delta.days).ljust(2, ' ') + " days, on " + str(mt.time_scheduled)[0:16] + " for " + db_system_name
        return val

    except oci.exceptions.ServiceError:
        print("m", end="")
        return ""
    except oci.exceptions.RequestException:
        print("m", end="")
        return ""
    except Exception as e:
        raise RuntimeError("\nError extracting database maintenance section - " + str(e))


##########################################################################
# load_database_maintatance_windows
##########################################################################
def load_database_maintatance_windows(maintenance_window):
    try:
        if not maintenance_window:
            return {}

        mw = maintenance_window
        value = {
            'preference': str(mw.preference),
            'months': ", ".join([x.name for x in mw.months]) if mw.months else "",
            'weeks_of_month': ", ".join([str(x) for x in mw.weeks_of_month]) if mw.weeks_of_month else "",
            'hours_of_day': ", ".join([str(x) for x in mw.hours_of_day]) if mw.hours_of_day else "",
            'days_of_week': ", ".join([str(x.name) for x in mw.days_of_week]) if mw.days_of_week else "",
            'lead_time_in_weeks': str(mw.lead_time_in_weeks) if mw.lead_time_in_weeks else "",
        }
        value['display'] = str(mw.preference) if str(mw.preference) == "NO_PREFERENCE" else (str(mw.preference) + ": Months: " + value['months'] + ", Weeks: " + value['weeks_of_month'] + ", DOW: " + value['days_of_week'] + ", Hours: " + value['hours_of_day'] + ", Lead Weeks: " + value['lead_time_in_weeks'])
        return value

    except Exception as e:
        raise RuntimeError("\nError handling Maintenance Window - " + str(e))


############################################
# Loop on all regions
############################################
print("\nLoading DBSystems...")
data = []
warnings = 0
for region_name in [str(es.region_name) for es in regions]:

    print("\nRegion " + region_name + "...")

    # set the region in the config and signer
    config['region'] = region_name
    signer.region = region_name

    # connect to virtual_network
    database_client = oci.database.DatabaseClient(config, signer=signer)
    if cmd.proxy:
        database_client.base_client.session.proxies = {'https': cmd.proxy}

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
            # Retrieve DBSystems
            ############################################
            list_db_systems = []
            try:
                list_db_systems = oci.pagination.list_call_get_all_results(
                    database_client.list_db_systems,
                    compartment.id,
                    sort_by="DISPLAYNAME"
                ).data

            except oci.exceptions.ServiceError as e:
                if check_service_error(e.code):
                    warnings += 1
                    print("Warnings ")
                    continue
                raise

            # loop on the db systems
            # dbs = oci.database.models.DbSystemSummary
            for dbs in list_db_systems:
                if dbs.lifecycle_state == oci.database.models.DbSystemSummary.LIFECYCLE_STATE_TERMINATED:
                    continue

                value = {
                    'region_name': region_name,
                    'compartment_name': str(compartment.name),
                    'compartment_id': str(compartment.id),
                    'id': str(dbs.id),
                    'display_name': str(dbs.display_name),
                    'shape': str(dbs.shape),
                    'lifecycle_state': str(dbs.lifecycle_state),
                    'data_storage_size_in_gbs': "" if dbs.data_storage_size_in_gbs is None else str(dbs.data_storage_size_in_gbs),
                    'availability_domain': str(dbs.availability_domain),
                    'cpu_core_count': str(dbs.cpu_core_count),
                    'node_count': ("" if dbs.node_count is None else str(dbs.node_count)),
                    'version': str(dbs.version),
                    'hostname': str(dbs.hostname),
                    'domain': str(dbs.domain),
                    'data_storage_percentage': str(dbs.data_storage_percentage),
                    'data_subnet_id': str(dbs.subnet_id),
                    'backup_subnet_id': str(dbs.backup_subnet_id),
                    'scan_dns_record_id': "" if dbs.scan_dns_record_id is None else str(dbs.scan_dns_record_id),
                    'listener_port': str(dbs.listener_port),
                    'cluster_name': "" if dbs.cluster_name is None else str(dbs.cluster_name),
                    'database_edition': str(dbs.database_edition),
                    'time_created': str(dbs.time_created),
                    'storage_management': "",
                    'sparse_diskgroup': str(dbs.sparse_diskgroup),
                    'reco_storage_size_in_gb': str(dbs.reco_storage_size_in_gb),
                    'last_maintenance_run': load_database_maintatance(database_client, dbs.last_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                    'next_maintenance_run': load_database_maintatance(database_client, dbs.next_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                    'maintenance_window': load_database_maintatance_windows(dbs.maintenance_window),
                    'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                    'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags
                }

                # storage_management
                if dbs.db_system_options:
                    if dbs.db_system_options.storage_management:
                        value['storage_management'] = dbs.db_system_options.storage_management

                # license model
                if dbs.license_model == oci.database.models.DbSystem.LICENSE_MODEL_LICENSE_INCLUDED:
                    value['license_model'] = "INCL"
                elif dbs.license_model == oci.database.models.DbSystem.LICENSE_MODEL_BRING_YOUR_OWN_LICENSE:
                    value['license_model'] = "BYOL"
                else:
                    value['license_model'] = str(dbs.license_model)

                # Edition
                if dbs.database_edition == oci.database.models.DbSystem.DATABASE_EDITION_ENTERPRISE_EDITION:
                    value['database_edition_short'] = "EE"
                elif dbs.database_edition == oci.database.models.DbSystem.DATABASE_EDITION_ENTERPRISE_EDITION_EXTREME_PERFORMANCE:
                    value['database_edition_short'] = "XP"
                elif dbs.database_edition == oci.database.models.DbSystem.DATABASE_EDITION_ENTERPRISE_EDITION_HIGH_PERFORMANCE:
                    value['database_edition_short'] = "HP"
                elif dbs.database_edition == oci.database.models.DbSystem.DATABASE_EDITION_STANDARD_EDITION:
                    value['database_edition_short'] = "SE"
                else:
                    value['database_edition_short'] = dbs.database_edition

                # add the data
                cnt += 1
                data.append(value)

            # print dbsystems for the compartment
            if cnt == 0:
                print("(-)")
            else:
                print("(" + str(cnt) + " DBSystems)")

    except Exception as e:
        raise RuntimeError("\nError extracting DBSystems - " + str(e))

############################################
# Print Output as JSON
############################################
print_header("Output")
print(json.dumps(data, indent=4, sort_keys=False))

if warnings > 0:
    print_header(str(warnings) + " Warnings appeared")
print_header("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
