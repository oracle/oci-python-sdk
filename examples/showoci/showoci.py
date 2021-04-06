#!/usr/bin/env python3
##########################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# showoci.py
#
# @author: Adi Zohar
#
# Supports Python 3 and above
#
# coding: utf-8
##########################################################################
# OCI Report Tool SHOWOCI:
#
# require OCI read only user with OCI authentication:
#    ALLOW GROUP ReadOnlyUsers to read all-resources IN TENANCY
#
# config file should contain:
#     [TENANT_NAME]
#     user =         user_ocid
#     fingerprint =  fingerprint of the api ssh key
#     key_file =     the path to the private key
#     tenancy =      tenancy ocid
#     region =       region
#
# Recommend to set below for display interactive
# export PYTHONUNBUFFERED=TRUE
##########################################################################
#
# Modules Included:
# - oci.core.VirtualNetworkClient
# - oci.core.ComputeClient
# - oci.core.ComputeManagementClient
# - oci.core.BlockstorageClient
# - oci.file_storage.FileStorageClient
# - oci.object_storage.ObjectStorageClient
# - oci.database.DatabaseClient
# - oci.identity.IdentityClient
# - oci.load_balancer.LoadBalancerClient
# - oci.email.EmailClient
# - oci.container_engine.ContainerEngineClient
# - oci.streaming.StreamAdminClient
# - oci.budget.BudgetClient
# - oci.autoscaling.AutoScalingClient
# - oci.monitoring.MonitoringClient
# - oci.ons.NotificationControlPlaneClient
# - oci.ons.NotificationDataPlaneClient
# - oci.healthchecks.HealthChecksClient
# - oci.announcements_service.AnnouncementClient
# - oci.limits.LimitsClient
# - oci.integration.IntegrationInstanceClient
# - oci.analytics.AnalyticsClient
# - oci.oda.OdaClient
# - oci.oce.OceInstanceClient
# - oci.apigateway.GatewaysClient
# - oci.functions.FunctionsManagementClient
# - oci.data_catalog.DataCatalogClient
# - oci.data_science.DataScienceClient
# - oci.data_flow.DataFlowClient
# - oci.nosql.NosqlClient
# - oci.dns.DnsClient
# - oci.events.EventsClient
# - oci.bds.BdsClient
# - oci.waas.WaasClient
# - oci.mysql.DbSystemClient
# - oci.cloud_guard.CloudGuardClient
# - oci.logging.LoggingManagementClient
# - oci.ocvp.EsxiHostClient and oci.ocvp.SddcClient
# - oci.golden_gate.GoldenGateClient
# - oci.network_load_balancer.NetworkLoadBalancerClient
#
# Modules Not Yet Covered:
# - oci.secrets.SecretsClient
# - oci.vault.VaultsClient
# - oci.blockchain.BlockchainPlatformClient
# - oci.data_integration.DataIntegrationClient
# - oci.data_safe.DataSafeClient
# - oci.usage_api.UsageapiClient
# - oci.sch.ServiceConnectorClient
# - oci.os_management.OsManagementClient
# - oci.log_analytics.LogAnalyticsClient
# - oci.tenant_manager_control_plane.LinkClient

##########################################################################
from __future__ import print_function
from showoci_data import ShowOCIData
from showoci_output import ShowOCIOutput, ShowOCISummary, ShowOCICSV
from showoci_service import ShowOCIFlags

import json
import sys
import argparse
import datetime

version = "21.03.23"

##########################################################################
# check OCI version
##########################################################################
if sys.version_info.major < 3:
    python_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)
    print("******************************************************")
    print("***    Showoci only supports Python 3 or Above     ***")
    print("***             Current Version = " + python_version.ljust(16) + " ***")
    print("******************************************************")
    sys.exit()


##########################################################################
# execute_extract
##########################################################################
def execute_extract():

    # get parset cmd
    cmd = set_parser_arguments()
    if cmd is None:
        return

    # Start time
    start_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # get flags object for calling cache
    flags = set_service_extract_flags(cmd)

    ############################################
    # create data instance
    ############################################
    data = ShowOCIData(flags)

    ############################################
    # output and summary instances
    ############################################
    output = ShowOCIOutput()
    summary = ShowOCISummary()
    csv = ShowOCICSV(start_time)

    ############################################
    # print showoci config
    ############################################
    cmdline = ' '.join(x for x in sys.argv[1:])
    showoci_config = data.get_showoci_config(cmdline, start_time)
    output.print_showoci_config(showoci_config['data'])

    ############################################
    # load oci data to cache
    ############################################
    output.print_header('Load OCI data to Memory', 1)

    if not data.load_service_data():
        return

    ############################################
    # if print service data to file or screen
    ############################################
    if cmd.servicefile or cmd.servicescr:
        if cmd.servicefile:
            if cmd.servicefile.name:
                print_to_json_file(cmd.servicefile.name, data.get_service_data(), "Service Data")

        elif cmd.servicescr:
            print(json.dumps(data.get_service_data(), indent=4, sort_keys=False))

    else:
        ############################################
        # process the data into data json
        ############################################
        output.print_header("Start Processing Data", 1)
        extracted_data = data.process_oci_data()

        ############################################
        # if JSON and screen
        ############################################
        if cmd.sjoutfile:
            # print nice
            output.print_data(extracted_data)
            summary.print_summary(extracted_data)

            # Add summary to JSON and print to JSON file
            extracted_data.append({'summary': summary.get_summary_json()})
            if cmd.sjoutfile.name:
                print_to_json_file(output, cmd.sjoutfile.name, extracted_data, "JSON Data")

        ############################################
        # JSON File only
        ############################################
        elif cmd.joutfile:
            if cmd.joutfile.name:
                summary.print_summary(extracted_data)
                extracted_data.append({'summary': summary.get_summary_json()})
                print_to_json_file(output, cmd.joutfile.name, extracted_data, "JSON Data")

        ############################################
        # JSON to screen only
        ############################################
        elif cmd.joutscr:
            summary.print_summary(extracted_data)
            extracted_data.append({'summary': summary.get_summary_json()})
            print(json.dumps(extracted_data, indent=4, sort_keys=False))

        ############################################
        # print summary only
        ############################################
        elif cmd.sumonly:
            summary.print_summary(extracted_data)

        ############################################
        # print nice output as default to screen
        # and summary
        ############################################
        else:
            output.print_data(extracted_data)
            summary.print_summary(extracted_data)

        ############################################
        # if print to CSV
        ############################################
        if cmd.csv:
            csv.generate_csv(extracted_data, cmd.csv, not cmd.csv_nodate)

    ############################################
    # print completion
    ############################################
    service_errors = data.get_service_errors()
    service_warnings = data.get_service_warnings()
    output_errors = output.get_errors() + summary.get_errors()
    complete_message = return_error_message(service_errors, service_warnings, data.error, output_errors)

    # if reboot migration
    if data.get_service_reboot_migration() > 0:
        output.print_header(str(data.get_service_reboot_migration()) + " Reboot Migration Alert for Compute or DB Node", 0)

    # if dbsystem maintenance
    if data.get_service_dbsystem_maintenance():
        output.print_header("DB System Maintenance", 0)
        for alert in data.get_service_dbsystem_maintenance():
            print(alert)

    # print completion
    output.print_header("Completed " + complete_message + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 0)


##########################################################################
# compile the error message
##########################################################################
def return_error_message(service_error, service_warning, data_error, output_error):

    complete_message = "Successfully"

    if service_error > 0 or service_warning > 0 or data_error > 0 or output_error > 0:
        complete_message = "With "

        if service_error > 0:
            complete_message += str(service_error) + "x(Service Errors) "

        if service_warning > 0:
            complete_message += str(service_warning) + "x(Service Warnings) "

        if data_error > 0:
            complete_message += str(data_error) + " (Processing Errors) "

        if output_error > 0:
            complete_message += str(output_error) + "x(Output Errors) "

    return complete_message


##########################################################################
# set parser
##########################################################################
def set_parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', action='store_true', default=False, dest='all', help='Print All Resources')
    parser.add_argument('-ani', action='store_true', default=False, dest='allnoiam', help='Print All Resources but identity')
    parser.add_argument('-an', action='store_true', default=False, dest='announcement', help='Print Announcements')
    parser.add_argument('-api', action='store_true', default=False, dest='api', help='Print API Gateways')
    parser.add_argument('-b', action='store_true', default=False, dest='budgets', help='Print Budgets')
    parser.add_argument('-c', action='store_true', default=False, dest='compute', help='Print Compute')
    parser.add_argument('-cn', action='store_true', default=False, dest='container', help='Print Containers')
    parser.add_argument('-d', action='store_true', default=False, dest='database', help='Print Database')
    parser.add_argument('-e', action='store_true', default=False, dest='email', help='Print EMail')
    parser.add_argument('-edge', action='store_true', default=False, dest='edge', help='Print Edge, DNS Services and WAAS policies')
    parser.add_argument('-f', action='store_true', default=False, dest='file', help='Print File Storage')
    parser.add_argument('-fun', action='store_true', default=False, dest='function', help='Print Functions')
    parser.add_argument('-i', action='store_true', default=False, dest='identity', help='Print Identity')
    parser.add_argument('-ic', action='store_true', default=False, dest='identity_compartments', help='Print Identity Compartments only')
    parser.add_argument('-isc', action='store_true', default=False, dest='skip_identity_user_credential', help='Skip Identity User Credential extract')
    parser.add_argument('-l', action='store_true', default=False, dest='load', help='Print Load Balancer')
    parser.add_argument('-lq', action='store_true', default=False, dest='limits', help='Print Limits and Quotas')
    parser.add_argument('-m', action='store_true', default=False, dest='monitoring', help='Print Monitoring, Notifications and Events')
    parser.add_argument('-n', action='store_true', default=False, dest='network', help='Print Network')
    parser.add_argument('-o', action='store_true', default=False, dest='object', help='Print Object Storage')
    parser.add_argument('-paas', action='store_true', default=False, dest='paas_native', help='Print PaaS Platform Services - OIC OAC OCE OCVS')
    parser.add_argument('-dataai', action='store_true', default=False, dest='data_ai', help='Print - D.Science, D.Catalog, D.Flow, ODA and BDS')
    parser.add_argument('-rm', action='store_true', default=False, dest='orm', help='Print Resource management')
    parser.add_argument('-s', action='store_true', default=False, dest='streams', help='Print Streams')
    parser.add_argument('-sec', action='store_true', default=False, dest='security', help='Print Security and Logging')

    parser.add_argument('-nobackups', action='store_true', default=False, dest='skip_backups', help='Do not process backups')
    parser.add_argument('-so', action='store_true', default=False, dest='sumonly', help='Print Summary Only')
    parser.add_argument('-mc', action='store_true', default=False, dest='mgdcompart', help='exclude ManagedCompartmentForPaaS')
    parser.add_argument('-nr', action='store_true', default=False, dest='noroot', help='Not include root compartment')
    parser.add_argument('-ip', action='store_true', default=False, dest='instance_principals', help='Use Instance Principals for Authentication')
    parser.add_argument('-dt', action='store_true', default=False, dest='delegation_token', help='Use Delegation Token (Cloud shell)')
    parser.add_argument('-t', default="", dest='profile', help='Config file section to use (tenancy profile)')
    parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
    parser.add_argument('-rg', default="", dest='region', help='Filter by Region')
    parser.add_argument('-cp', default="", dest='compart', help='Filter by Compartment Name or OCID')
    parser.add_argument('-cpr', default="", dest='compart_recur', help='Filter by Comp Name Recursive')
    parser.add_argument('-cpath', default="", dest='compartpath', help='Filter by Compartment path ,(i.e. -cpath "Adi / Sub"')
    parser.add_argument('-tenantid', default="", dest='tenantid', help='Override confile file tenancy_id')
    parser.add_argument('-cf', type=argparse.FileType('r'), dest='config', help="Config File (~/.oci/config)")
    parser.add_argument('-csv', default="", dest='csv', help="Output to CSV files, Input as file header")
    parser.add_argument('-csv_nodate', action='store_true', default=False, dest='csv_nodate', help='Do not add date field to the csv')
    parser.add_argument('-jf', type=argparse.FileType('w'), dest='joutfile', help="Output to file   (JSON format)")
    parser.add_argument('-js', action='store_true', default=False, dest='joutscr', help="Output to screen (JSON format)")
    parser.add_argument('-sjf', type=argparse.FileType('w'), dest='sjoutfile', help="Output to screen (nice format) and JSON File")
    parser.add_argument('-cachef', type=argparse.FileType('w'), dest='servicefile', help="Output Cache to file   (JSON format)")
    parser.add_argument('-caches', action='store_true', default=False, dest='servicescr', help="Output Cache to screen (JSON format)")
    parser.add_argument('--version', action='version', version='%(prog)s ' + version)

    result = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return None

    if not (result.all or result.allnoiam or result.network or result.identity or result.identity_compartments or
            result.compute or result.object or
            result.load or result.database or result.file or result.email or result.orm or result.container or
            result.streams or result.budgets or result.monitoring or result.edge or result.announcement or result.limits or result.paas_native or
            result.api or result.function or result.data_ai or result.security):

        parser.print_help()

        print("******************************************************")
        print("***    You must choose at least one parameter!!    ***")
        print("******************************************************")
        return None

    return result


##########################################################################
# set cache flags for extract
##########################################################################
def set_service_extract_flags(cmd):

    prm = ShowOCIFlags()

    prm.showoci_version = version

    if cmd.proxy:
        prm.proxy = cmd.proxy

    if cmd.mgdcompart:
        prm.read_ManagedCompartmentForPaaS = False

    if cmd.all or cmd.identity:
        prm.read_identity = True

    if cmd.all or cmd.allnoiam or cmd.network:
        prm.read_network = True

    if cmd.all or cmd.allnoiam or cmd.compute:
        prm.read_compute = True

    if cmd.all or cmd.allnoiam or cmd.database:
        prm.read_database = True

    if cmd.all or cmd.allnoiam or cmd.file:
        prm.read_file_storage = True

    if cmd.all or cmd.allnoiam or cmd.object:
        prm.read_object_storage = True

    if cmd.all or cmd.allnoiam or cmd.orm:
        prm.read_resource_management = True

    if cmd.all or cmd.allnoiam or cmd.load:
        prm.read_load_balancer = True

    if cmd.all or cmd.allnoiam or cmd.email:
        prm.read_email_distribution = True

    if cmd.all or cmd.allnoiam or cmd.container:
        prm.read_containers = True

    if cmd.all or cmd.allnoiam or cmd.streams:
        prm.read_streams = True

    if cmd.all or cmd.allnoiam or cmd.budgets:
        prm.read_budgets = True

    if cmd.all or cmd.allnoiam or cmd.function:
        prm.read_function = True

    if cmd.all or cmd.allnoiam or cmd.api:
        prm.read_api = True

    if cmd.all or cmd.allnoiam or cmd.limits:
        prm.read_limits = True

    if cmd.all or cmd.allnoiam or cmd.paas_native:
        prm.read_paas_native = True

    if cmd.all or cmd.allnoiam or cmd.data_ai:
        prm.read_data_ai = True

    if cmd.all or cmd.allnoiam or cmd.monitoring:
        prm.read_monitoring_notifications = True

    if cmd.all or cmd.allnoiam or cmd.announcement:
        prm.read_announcement = True

    if cmd.all or cmd.allnoiam or cmd.edge:
        prm.read_edge = True

    if cmd.all or cmd.allnoiam or cmd.security:
        prm.read_security = True

    if cmd.noroot:
        prm.read_root_compartment = False

    if cmd.skip_backups:
        prm.skip_backups = True

    if cmd.config:
        if cmd.config.name:
            prm.config_file = cmd.config.name

    if cmd.profile:
        prm.config_section = cmd.profile

    if cmd.region:
        prm.filter_by_region = str(cmd.region)

    if cmd.compart:
        prm.filter_by_compartment = str(cmd.compart)

    if cmd.compart_recur:
        prm.filter_by_compartment_recursive = str(cmd.compart_recur)

    if cmd.compartpath:
        prm.filter_by_compartment_path = str(cmd.compartpath)

    if cmd.instance_principals:
        prm.use_instance_principals = True

    if cmd.delegation_token:
        prm.use_delegation_token = True

    if cmd.skip_identity_user_credential:
        prm.skip_identity_user_credential = True

    if cmd.tenantid:
        prm.filter_by_tenancy_id = cmd.tenantid

    return prm


############################################
# print data to json file
############################################
def print_to_json_file(output, file_name, data, header):

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=False)

    output.print_header(header + " exported to " + file_name, 0)


##########################################################################
# Main
##########################################################################
execute_extract()
