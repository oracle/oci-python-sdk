#!/usr/bin/env python3
##########################################################################
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# showoci.py
#
# @author: Adi Zohar
# @contributors: Olaf Heimburger
#
# Supports Python 3 and above
#
# coding: utf-8
##########################################################################
# OCI Report Tool SHOWOCI:
#
# Requires OCI read only user with OCI authentication:
#    ALLOW GROUP ReadOnlyUsers to read all-resources IN TENANCY
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
# - oci.ocvp.EsxiHostClient
# - oci.ocvp.SddcClient
# - oci.ocvp.ClusterClient
# - oci.golden_gate.GoldenGateClient
# - oci.network_load_balancer.NetworkLoadBalancerClient
# - oci.management_agent.ManagementAgentClient
# - oci.database_management.DbManagementClient
# - oci.bastion.BastionClient
# - oci.key_management.KmsVaultClient
# - oci.data_integration.DataIntegrationClient
# - oci.visual_builder.VbInstanceClient
# - oci.data_connectivity.models.RegistrySummary
# - oci.queue.QueueAdminClient
# - oci.identity_domains.IdentityDomainsClient
# - oci.network_firewall.NetworkFirewallClient
# - oci.opensearch.OpensearchClusterClient
# - oci.psql.PostgresqlClient
# - oci.generative_ai.GenerativeAiClient
# - oci.certificates_management.CertificatesManagementClient
# - oci.data_safe.DataSafeClient
# - oci.optimizer.OptimizerClient
# - oci.disaster_recovery.DisasterRecoveryClient
#
# Modules without CSV yet:
# - datasciencemodeldeployment
# - datasciencenotebooksession
#
# Modules Not Yet Covered:
# - oci.ai_document.AIServiceDocumentClient
# - oci.ai_language.AIServiceLanguageClient
# - oci.ai_speech.AIServiceSpeechClient
# - oci.ai_vision.AIServiceVisionClient
# - oci.apm_config.ConfigClient
# - oci.apm_synthetics.ApmSyntheticClient
# - oci.apm_control_plane.ApmDomainClient
# - oci.apm_traces.TraceClient
# - oci.apm_traces.QueryClient
# - oci.appmgmt_control.AppmgmtControlClient
# - oci.application_migration.ApplicationMigrationClient
# - oci.artifacts.ArtifactsClient
# - oci.cloud_migrations.MigrationClient
# - oci.container_instances.ContainerInstanceClient
# - oci.data_labeling_service.DataLabelingManagementClient
# - oci.fusion_apps.FusionApplicationsClient
# - oci.jms.JavaManagementServiceClient
# - oci.license_manager.LicenseManagerClient
# - oci.lockbox.LockboxClient
# - oci.media_services.MediaServicesClient
# - oci.opa.OpaInstanceClient
# - oci.opsi.OperationsInsightsClient
# - oci.recovery.DatabaseRecoveryClient
# - oci.redis.RedisClusterClient
# - oci.threat_intelligence.ThreatintelClient
##########################################################################
from __future__ import print_function
from showoci_data import ShowOCIData
from showoci_output import ShowOCIOutput, ShowOCISummary, ShowOCICSV
from showoci_service import ShowOCIFlags, ShowOCIService

import json
import sys
import argparse
import datetime
import contextlib
import os
import time

version = "25.08.26"

##########################################################################
# check OCI version
##########################################################################
if sys.version_info.major < 3:
    python_version = str(sys.version_info.major) + '.' + str(sys.version_info.minor)
    print("******************************************************")
    print("***    Showoci only supports Python 3 or Above     ***")
    print(f"***             Current Version = {python_version.ljust(16)} ***")
    print("******************************************************")
    sys.exit()

##########################################################################
# check application files version
##########################################################################
if version != ShowOCIData.version or version != ShowOCIService.version or version != ShowOCIOutput.version:
    print("******************************************************")
    print("***    Showoci files have different versions       ***")
    print(f"***    showoci.py         - {version}               ***")
    print(f"***    showoci_data.py    - {ShowOCIData.version}               ***")
    print(f"***    showoci_output.py  - {ShowOCIOutput.version}               ***")
    print(f"***    showoci_service.py - {ShowOCIService.version}               ***")
    print("******************************************************")
    print("Aborting!")
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
    start_time = time.time()
    start_time_str = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # get flags object for calling cache
    flags = set_service_extract_flags(cmd)

    ############################################
    # create data instance
    ############################################
    data = ShowOCIData(flags)
    if flags.excludelist:
        return

    ############################################
    # output and summary instances
    ############################################
    output = ShowOCIOutput()
    summary = ShowOCISummary()
    csv = ShowOCICSV(start_time_str)

    ############################################
    # print showoci config
    ############################################
    cmdline = ' '.join(x for x in sys.argv[1:])
    showoci_config = data.get_showoci_config(cmdline, start_time_str)
    output.print_showoci_config(showoci_config['data'])

    ############################################
    # load oci data to cache
    ############################################
    output.print_header('Load OCI data to Memory', 1)

    if not data.load_service_data():
        return

    ############################################
    # Get Tenancy details from file
    ############################################
    tenancy = data.get_tenancy_data()

    ############################################
    # if print service data to file or screen
    ############################################
    if cmd.servicefile or cmd.servicescr:
        if cmd.servicefile:
            if cmd.servicefile.name:
                print_to_json_file(output, cmd.servicefile.name, data.get_service_data(), "Service Data")

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
            csv.csv_tags_to_cols = not cmd.csv_notagstocols
            csv.generate_csv(extracted_data, cmd.csv, tenancy, not cmd.csv_nodate, cmd.csvcol)

    ############################################
    # print completion
    ############################################
    service_errors = data.get_service_errors()
    service_warnings = data.get_service_warnings()
    output_errors = output.get_errors() + summary.get_errors() + csv.get_errors()
    complete_message = return_error_message(service_errors, service_warnings, data.error, output_errors)

    # if reboot migration
    if data.get_service_reboot_migration() > 0:
        output.print_header(str(data.get_service_reboot_migration()) + " Reboot Migration Alert for Compute or DB Node", 0)

    # if dbsystem maintenance
    if data.get_service_dbsystem_maintenance():
        output.print_header("DB System Maintenance", 0)
        for alert in data.get_service_dbsystem_maintenance():
            print(alert)

    # calculate elapsed
    end_time_str = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elapsed = time.time() - start_time
    str_elapsed = " - Elapsed " + '{:02d}:{:02d}:{:02d}'.format(round(elapsed // 3600), (round(elapsed % 3600 // 60)), round(elapsed % 60))

    # print completion
    output.print_header("Completed " + complete_message + " at " + end_time_str + str_elapsed, 0)


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
def set_parser_arguments(argsList=[]):
    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=150))
    parser.add_argument('-a', action='store_true', default=False, dest='all', help='Print All Resources.')
    parser.add_argument('-ani', action='store_true', default=False, dest='allnoiam', help='Print All Resources but identity.')
    parser.add_argument('-an', action='store_true', default=False, dest='announcement', help='Print Announcements.')
    parser.add_argument('-andays', default=30, dest='announcement_days', type=int, help='Announcement Last X Days (Default=30).')
    parser.add_argument('-c', '-cn', action='store_true', default=False, dest='compute', help='Print Compute and Containers.')
    parser.add_argument('-d', action='store_true', default=False, dest='database', help='Print Database.')
    parser.add_argument('-dsa', '--datasafe-assessments', action='store_true', default=False, dest='datasafe_assessments', help='When Data Safe is implemented, get the assessments, too.')
    parser.add_argument('-edge', action='store_true', default=False, dest='edge', help='Print Edge, DNS Services and WAAS policies, DNS Zone is slow can be excluded using -exclude DNSZONE.')
    parser.add_argument('-f', '-o', action='store_true', default=False, dest='file', help='Print File and Object Storage.')
    parser.add_argument('-i', action='store_true', default=False, dest='identity', help='Print Identity and Identity Domains.')
    parser.add_argument('-iold', action='store_true', default=False, dest='identity_old', help='Print Identity from the old APIs when choosing identity extract.')
    parser.add_argument('-ic', action='store_true', default=False, dest='identity_compartments', help='Print Identity Compartments only.')
    parser.add_argument('-isc', action='store_true', default=False, dest='skip_identity_user_credential', help='Skip Identity User Credential extract.')
    parser.add_argument('-ifilter', default="", dest='ifilter', help='Filter IAM domains by Domain Names using comma seperated')

    parser.add_argument('-s', '-api', '-rm', '-fun', action='store_true', default=False, dest='streams_queues', help='Print API, Functions, Resource management, Gateways, FSDR, Streams and Queues.')

    parser.add_argument('-m', '-sec', '-lq', '-e', '-b', action='store_true', default=False, dest='monitoring', help='Print Monitor, Events, Agents, Security, Quotas, E-Mail, Limits, Cert...')
    parser.add_argument('-paas', '-dataai', action='store_true', default=False, dest='paas_native', help='Print Native, Data and AI.')
    parser.add_argument('-n', '-l', action='store_true', default=False, dest='network', help='Print Network.')

    parser.add_argument('-exclude', default="", dest='exclude', help='Exclude Services, use -excludelist to for list of values')
    parser.add_argument('-excludelist', action='store_true', default=False, dest='excludelist', help='Generate Exclude List for -exclude command')
    parser.add_argument('-noparallel', action='store_true', default=False, dest='skip_threads', help='Do not run in parallel processing (Threads).')
    parser.add_argument('-threads', default=8, dest='threads', type=int, help='Threads Processes when running with Threads (default=8).')
    parser.add_argument('-nobackups', action='store_true', default=False, dest='skip_backups', help='Do not process backups.')
    parser.add_argument('-skipdbhomes', action='store_true', default=False, dest='skip_dbhomes', help='Do not process Database Homes and below.')
    parser.add_argument('-readtimeout', default=20, dest='readtimeout', type=int, help='Timeout for REST API Connection (default=20).')
    parser.add_argument('-conntimeout', default=150, dest='conntimeout', type=int, help='Timeout for REST API Read (default=150).')
    parser.add_argument('-so', action='store_true', default=False, dest='sumonly', help='Print Summary Only.')
    parser.add_argument('-mc', action='store_true', default=False, dest='mgdcompart', help='Exclude ManagedCompartmentForPaaS.')
    parser.add_argument('-nr', action='store_true', default=False, dest='noroot', help='Not include root compartment.')
    parser.add_argument('-ip', action='store_true', default=False, dest='instance_principals', help='Use Instance Principals for authentication.')
    parser.add_argument('-rp', action='store_true', default=False, dest='resource_principals', help='Use Resource Principals for authentication.')
    parser.add_argument('-is', action='store_true', default=False, dest='security_token', help='Use Config and Security Token for authentication.')
    parser.add_argument('-dt', action='store_true', default=False, dest='delegation_token', help='Use Delegation Token (Cloud Shell).')
    parser.add_argument('-t', default="", dest='profile', help='Config file section to use (tenancy profile).')
    parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80).')
    parser.add_argument('-rg', default="", dest='region', help='Filter by Region, partial name or comma seperated.')
    parser.add_argument('-rgn', default="", dest='not_region', help='Filter by Region, do not include region partial name or comma seperated.')
    parser.add_argument('-cp', default="", dest='compart', help='Filter by Compartment Name or OCID.')
    parser.add_argument('-cpr', default="", dest='compart_recur', help='Filter by Compartment Name Recursive.')
    parser.add_argument('-cpath', default="", dest='compartpath', help='Filter by Compartment path (i.e. -cpath "Adi / Sub").')
    parser.add_argument('-tenantid', default="", dest='tenantid', help='Override confile file tenancy_id.')
    parser.add_argument('-cf', type=argparse.FileType('r'), dest='config', help="Config File (~/.oci/config).")
    parser.add_argument('-csv', default="", dest='csv', help="Output to CSV files, Input as file header.")
    parser.add_argument('-csvcol', default="", dest='csvcol', help="Extract define tags as columns for Compute in CSV.")
    parser.add_argument('-csv_nodate', action='store_true', default=False, dest='csv_nodate', help='Do not add date field to the CSV.')
    parser.add_argument('-csv_notagstocols', action='store_true', default=False, dest='csv_notagstocols', help='Do not Convert Tags to Columns in CSV Extract.')
    parser.add_argument('-jf', type=argparse.FileType('w'), dest='joutfile', help="Output to file (JSON format).")
    parser.add_argument('-js', action='store_true', default=False, dest='joutscr', help="Output to screen (JSON format).")
    parser.add_argument('-sjf', type=argparse.FileType('w'), dest='sjoutfile', help="Output to screen (nice format) and JSON File.")
    parser.add_argument('-cachef', type=argparse.FileType('w'), dest='servicefile', help="Output Cache to file (JSON format).")
    parser.add_argument('-caches', action='store_true', default=False, dest='servicescr', help="Output Cache to screen (JSON format).")
    parser.add_argument('--version', action='version', version='%(prog)s ' + version)

    if not argsList:
        result = parser.parse_args()
    else:
        with contextlib.redirect_stdout(os.devnull):
            try:
                result = parser.parse_args(args=argsList)
                return result
            except Exception:
                return False

    result = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return None

    if not (result.all or result.allnoiam or result.network or result.identity or result.identity_compartments or
            result.compute or result.database or result.file or result.streams_queues or result.monitoring or
            result.edge or result.announcement or result.paas_native or result.excludelist or result.identity_old):

        parser.print_help()

        print("******************************************************")
        print("***    You must choose at least one parameter!     ***")
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

    if cmd.all or cmd.identity or cmd.identity_old:
        prm.read_identity = True

    if cmd.all or cmd.allnoiam or cmd.network:
        prm.read_network = True
        prm.read_load_balancer = True

    if cmd.all or cmd.allnoiam or cmd.compute:
        prm.read_compute = True
        prm.read_containers = True

    if cmd.all or cmd.allnoiam or cmd.database:
        prm.read_database = True

    if cmd.all or cmd.allnoiam or cmd.file:
        prm.read_file_storage = True
        prm.read_object_storage = True

    if cmd.all or cmd.allnoiam or cmd.streams_queues:
        prm.read_streams_queues = True
        prm.read_function = True
        prm.read_resource_management = True
        prm.read_api = True

    if cmd.all or cmd.allnoiam or cmd.paas_native:
        prm.read_paas_native = True
        prm.read_data_ai = True

    if cmd.all or cmd.allnoiam or cmd.monitoring:
        prm.read_monitoring_notifications = True
        prm.read_security = True
        prm.read_limits = True
        prm.read_email_distribution = True
        prm.read_budgets = True

    if cmd.all or cmd.allnoiam or cmd.announcement:
        prm.read_announcement = True
        prm.read_announcement_days = cmd.announcement_days

    if cmd.all or cmd.allnoiam or cmd.edge:
        prm.read_edge = True

    if cmd.noroot:
        prm.read_root_compartment = False

    if cmd.skip_backups:
        prm.skip_backups = True

    if cmd.datasafe_assessments:
        prm.read_datasafe_assessments = True

    if cmd.skip_threads:
        prm.skip_threads = True

    if cmd.threads:
        prm.threads = cmd.threads

    if cmd.exclude:
        prm.exclude = str(cmd.exclude).split(",")

    if cmd.ifilter:
        prm.iam_domain_name_filter = str(cmd.ifilter).split(",")

    if cmd.excludelist:
        prm.excludelist = True

    if cmd.conntimeout:
        prm.connection_timeout = cmd.conntimeout

    if cmd.readtimeout:
        prm.read_timeout = cmd.readtimeout

    if cmd.skip_dbhomes:
        prm.skip_dbhomes = True

    if cmd.config:
        if cmd.config.name:
            prm.config_file = cmd.config.name

    if cmd.profile:
        prm.config_section = cmd.profile

    if cmd.region:
        prm.filter_by_region = str(cmd.region)

    if cmd.not_region:
        prm.filter_by_region_not = str(cmd.not_region)

    if cmd.compart:
        prm.filter_by_compartment = str(cmd.compart)

    if cmd.compart_recur:
        prm.filter_by_compartment_recursive = str(cmd.compart_recur)

    if cmd.compartpath:
        prm.filter_by_compartment_path = str(cmd.compartpath)

    if cmd.instance_principals:
        prm.use_instance_principals = True

    if cmd.resource_principals:
        prm.use_resource_principals = True

    if cmd.delegation_token:
        prm.use_delegation_token = True

    if cmd.security_token:
        prm.use_security_token = True

    if cmd.identity_old:
        prm.read_identity_old = True

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
if __name__ == "__main__":
    try:
        execute_extract()
    except KeyboardInterrupt:
        print('Interrupted')
