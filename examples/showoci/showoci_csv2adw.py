#!/usr/bin/env python3
##########################################################################
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# DISCLAIMER This is not an official Oracle application,  It does not supported by Oracle Support,
# It should NOT be used for utilization calculation purposes, and rather OCI's official
#
# showoci_csv2adw.py
#
# @author: Adi Zohar
#
# coding: utf-8
##########################################################################
# showoci_csv2adw - Load showoci csv reports to ADW to be used with usage2adw,
# Currently supported: Compute + Block Volumes
#
# Requires oracledb python package
# python3 -m pip install oracledb
##########################################################################
# Tables used:
# - OCI_SHOWOCI_COMPUTE
# - OCI_SHOWOCI_COMPUTE_RESERVATIONS
# - OCI_SHOWOCI_BLOCK_VOLUMES
# - OCI_SHOWOCI_BLOCK_VOLUMES_BACKUP
# - OCI_SHOWOCI_DATABASE_ALL
# - OCI_SHOWOCI_DATABASE_BACKUPS
# - OCI_SHOWOCI_DATABASE_EXA_CS_VMS
# - OCI_SHOWOCI_DATABASE_EXA_INFRA
# - OCI_SHOWOCI_DATABASE_EXA_CC_VMS
# - OCI_SHOWOCI_DATABASES
# - OCI_SHOWOCI_DATABASE_VM_BM
# - OCI_SHOWOCI_DATABASES_ADB
# - OCI_SHOWOCI_DB_NOSQL
# - OCI_SHOWOCI_DB_MYSQL
# - OCI_SHOWOCI_DB_GOLDENGATE_DEP
# - OCI_SHOWOCI_FILE_STORAGE
# - OCI_SHOWOCI_OBJECT_STORAGE
# - OCI_SHOWOCI_LB_LISTENERS
# - OCI_SHOWOCI_LB_BACKENDSET
# - OCI_SHOWOCI_OAC
# - OCI_SHOWOCI_OIC
# - OCI_SHOWOCI_OCE
# - OCI_SHOWOCI_DEVOPS
# - OCI_SHOWOCI_VISUAL_BUILDER
# - OCI_SHOWOCI_CONTAINERS
# - OCI_SHOWOCI_CONTAINERS_NODEPOOLS
# - OCI_SHOWOCI_APIGW
# - OCI_SHOWOCI_NETWORK_VCN
# - OCI_SHOWOCI_NETWORK_SUBNET
# - OCI_SHOWOCI_NETWORK_SUBNET_PRV_IPS
# - OCI_SHOWOCI_NETWORK_SECLIST_RULES
# - OCI_SHOWOCI_NETWORK_SECGROUPS_RULES
# - OCI_SHOWOCI_NETWORK_DRGS
# - OCI_SHOWOCI_NETWORK_DHCP_OPTIONS
# - OCI_SHOWOCI_NETWORK_ROUTES
# - OCI_SHOWOCI_NETWORK_DRG_VC
# - OCI_SHOWOCI_NETWORK_DRG_IPSEC
# - OCI_SHOWOCI_NETWORK_FIREWALL
# - OCI_SHOWOCI_DIGITAL_ASSISTANCE
# - OCI_SHOWOCI_BIG_DATA
# - OCI_SHOWOCI_DATA_FLOW
# - OCI_SHOWOCI_DATA_CATALOG
# - OCI_SHOWOCI_DATA_CONN_REGISTRY
# - OCI_SHOWOCI_DATA_SCIENCE
# - OCI_SHOWOCI_DATA_INTEGRATION
# - OCI_SHOWOCI_STREAMS_QUEUES
# - OCI_SHOWOCI_WAF
# - OCI_SHOWOCI_HEALTHCHECKS
# - OCI_SHOWOCI_DNS_STEERING_POL
# - OCI_SHOWOCI_IAM_COMPARTMENTS
# - OCI_SHOWOCI_SECURITY_BASTIONS
# - OCI_SHOWOCI_SECURITY_CLOUDGUARD
# - OCI_SHOWOCI_SECURITY_LOGGINGS
# - OCI_SHOWOCI_SECURITY_KMS_VAULTS
# - OCI_SHOWOCI_LIMITS
# - OCI_SHOWOCI_QUOTAS
# - OCI_SHOWOCI_MONITOR_AGENTS
# - OCI_SHOWOCI_MONITOR_EVENTS
# - OCI_SHOWOCI_MONITOR_DB_MANAGEMENT
# - OCI_SHOWOCI_MONITOR_ALARMS
# - OCI_SHOWOCI_MONITOR_NOTIFICATIONS
# - OCI_SHOWOCI_OPEN_SEARCH
#
##########################################################################
# TO DO
##########################################################################
#
# paas_ocvs_vmware
# edge_waas_policies
# identity_compartments
# identity_domains_auth
# identity_domains
# identity_domains_dyngroup
# identity_domains_groups
# identity_domains_idps
# identity_domains_kmsi
# identity_domains_users
# identity_policy
##########################################################################

import sys
import argparse
import datetime
import csv
import oracledb
import time
import os

version = "23.04.11"
cmd = None
file_num = 0


##########################################################################
# Print header centered
##########################################################################
def print_header(name, category):
    options = {0: 90, 1: 60, 2: 30}
    chars = int(options[category])
    print("")
    print('#' * chars)
    print("#" + name.center(chars - 2, " ") + "#")
    print('#' * chars)


##########################################################################
# Get Column from Array
##########################################################################
def get_column_value_from_array(column, array, limit_size):
    if column in array:
        value = array[column][0:limit_size]
        if value == "None":
            value = ""
        return value
    else:
        print("   Column not found in CSV --> " + column)
        return ""


##########################################################################
# Get Currnet Date Time
##########################################################################
def get_current_date_time():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


##########################################################################
# print count result
##########################################################################
def get_time_elapsed(start_time):
    et = time.time() - start_time
    return ", Process Time " + str('{:02d}:{:02d}:{:02d}'.format(round(et // 3600), (round(et % 3600 // 60)), round(et % 60)))


##########################################################################
# set parser
##########################################################################
def set_parser_arguments():

    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=130))
    parser.add_argument('-csv', default="", dest='csv_location', help='CSV Location from showoci including header')
    parser.add_argument('-du', default="", dest='duser', help='ADB User')
    parser.add_argument('-dp', default="", dest='dpass', help='ADB Password')
    parser.add_argument('-dn', default="", dest='dname', help='ADB DSN')

    parser.add_argument('-usethick', action='store_true', default=False, dest='usethick', help='Use sqlnet thick client library')
    parser.add_argument('-wl', default="", dest='wallet_location', help='Wallet Location')
    parser.add_argument('-wp', default="", dest='wallet_password', help='Wallet Password')

    parser.add_argument('-drop', action='store_true', default=False, dest='drop', help='Drop Tables before Load')
    parser.add_argument('-verbose', action='store_true', default=False, dest='verbose', help='Print more details')

    parser.add_argument('--version', action='version', version='%(prog)s ' + version)

    result = parser.parse_args()

    if not (result.duser and result.dpass and result.dname and result.csv_location):
        parser.print_help()
        print_header("You must specify database credentials and csv location!!", 0)
        return None

    return result


##########################################################################
# Check Table Structure for Compute
##########################################################################
def handle_compute(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_COMPUTE",
            'csv_file': "compute.csv",
            'items': [
                {'col': 'tenant_name           ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id             ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'instance_id           ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name           ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain   ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'fault_domain          ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path      ', 'csv': '    ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name      ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'server_name           ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status                ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                  ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'image                 ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'primary_vcn           ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'primary_subnet        ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape                 ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'ocpus                 ', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'memory_gb             ', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'local_storage_tb      ', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'public_ips            ', 'csv': '    ', 'type': 'varchar2(500) ', 'pk': 'n'},
                {'col': 'private_ips           ', 'csv': '    ', 'type': 'varchar2(500) ', 'pk': 'n'},
                {'col': 'security_groups       ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'internal_fqdn         ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created          ', 'csv': '    ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'boot_volume           ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'boot_volume_id        ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'boot_volume_size_gb   ', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'boot_volume_b_policy  ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'boot_volume_encryption', 'csv': '    ', 'type': 'varchar2(200) ', 'pk': 'n'},
                {'col': 'block_volumes         ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'block_volumes_ids     ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'block_volumes_total_gb', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'block_volumes_b_policy', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vnic_ids              ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags          ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags         ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date          ', 'csv': '    ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "instance_id", "server_name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_compute - " + str(e))


##########################################################################
# Check Table Structure for Block Storage
##########################################################################
def handle_block_volume(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_BLOCK_VOLUMES",
            'csv_file': "block_volumes.csv",
            'items': [
                {'col': 'tenant_name        ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id          ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                 ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path   ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name   ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'display_name       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'size_gb            ', 'csv': 'size ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'backup_policy      ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vpus_per_gb        ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'volume_group_name  ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'instance_name      ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'instance_id        ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'defined_tags       ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags      ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date       ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "display_name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_block_storage - " + str(e))


##########################################################################
# Check Table Structure for handle_block_volumes_backups
##########################################################################
def handle_block_volume_backups(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_BLOCK_VOLUMES_BACKUP",
            'csv_file': "block_volumes_backups.csv",
            'items': [
                {'col': 'tenant_name        ', 'csv': '         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id          ', 'csv': '         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                 ', 'csv': 'backup_id', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name        ', 'csv': '         ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path   ', 'csv': '         ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name   ', 'csv': '         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description        ', 'csv': 'desc     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'volume_type        ', 'csv': '         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'backup_type        ', 'csv': '         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'schedule_type      ', 'csv': '         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'source_name        ', 'csv': '         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'unique_size_in_gbs ', 'csv': '         ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'size_in_gbs        ', 'csv': '         ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'expiration_time    ', 'csv': '         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created       ', 'csv': '         ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date       ', 'csv': '         ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "source_name", "backup Source ")
    except Exception as e:
        raise Exception("\nError at procedure: handle_block_volume_backups - " + str(e))


##########################################################################
# Check Table Structure for Database All
##########################################################################
def handle_database_all(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASE_ALL",
            'csv_file': "database_db_all.csv",
            'items': [
                {'col': 'tenant_name         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id           ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                  ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name         ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path    ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name    ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status              ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'name                ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vm_name             ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape               ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'gi_version          ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'gi_version_date     ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'system_version      ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'system_version_date ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'database_edition    ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'license_model       ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'data_subnet         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'backup_subnet       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'scan_ips            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vip_ips             ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cluster_name        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'domain              ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'db_nodes            ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'db_homes            ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'maintenance_window  ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'last_maintenance_run', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'next_maintenance_run', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'infra_id            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cpu_core_count      ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'shape_ocpus         ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'db_storage_gb       ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'memory_gb           ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'local_storage_tb    ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_count          ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'defined_tags        ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags       ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created        ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date        ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_all - " + str(e))


##########################################################################
# Check Table Structure for handle_database_backups
##########################################################################
def handle_database_backups(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASE_BACKUPS",
            'csv_file': "database_backups.csv",
            'items': [
                {'col': 'tenant_name         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id           ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                  ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name         ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path    ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name    ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state     ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'dbs_name            ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'database            ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape               ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'database_edition    ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'backup_name         ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'time                ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'size_gb             ', 'csv': 'size ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'database_id         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'extract_date        ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_backups - " + str(e))


##########################################################################
# Check Table Structure for handle_database_exa_cs_vms
##########################################################################
def handle_database_exa_cs_vms(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASE_EXA_CS_VMS",
            'csv_file': "database_db_exacs.csv",
            'items': [
                {'col': 'tenant_name         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id           ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                  ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name         ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path    ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name    ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status              ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'name                ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vm_name             ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape               ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'gi_version          ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'gi_version_date     ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'system_version      ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'system_version_date ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'database_edition    ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'license_model       ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'data_subnet         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'backup_subnet       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'scan_ips            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vip_ips             ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cluster_name        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'domain              ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'db_nodes            ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'db_homes            ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'maintenance_window  ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'last_maintenance_run', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'next_maintenance_run', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'infra_id            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cpu_core_count      ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'shape_ocpus         ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'db_storage_gb       ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'memory_gb           ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'local_storage_tb    ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_count          ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'defined_tags        ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags       ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created        ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date        ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_exa_cs_vms - " + str(e))


##########################################################################
# Check Table Structure for handle_database_exa_infra
##########################################################################
def handle_database_exa_infra(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASE_EXA_INFRA",
            'csv_file': "database_db_exa_infra.csv",
            'items': [
                {'col': 'tenant_name                  ', 'csv': '        ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                    ', 'csv': '        ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                           ', 'csv': 'infra_id', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                  ', 'csv': '        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain          ', 'csv': '        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path             ', 'csv': '        ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name             ', 'csv': '        ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status                       ', 'csv': '        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                         ', 'csv': '        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'name                         ', 'csv': '        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape                        ', 'csv': '        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'time_zone                    ', 'csv': '        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'cpus_enabled                 ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'max_cpu_count                ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'memory_size_in_gbs           ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'max_memory_in_gbs            ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'db_node_storage_size_in_gbs  ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'max_db_node_storage_in_g_bs  ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'data_storage_size_in_tbs     ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'max_data_storage_in_t_bs     ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'total_storage_size_in_gbs    ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'available_storage_size_in_gbs', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'storage_count                ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'additional_storage_count     ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'activated_storage_count      ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'compute_count                ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_count                   ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'cluster_count                ', 'csv': '        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'cluster_names                ', 'csv': '        ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'dns_server                   ', 'csv': '        ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ntp_server                   ', 'csv': '        ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'csi_number                   ', 'csv': '        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'db_servers                   ', 'csv': '        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'db_servers_ids               ', 'csv': '        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'maintenance_window           ', 'csv': '        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'last_maintenance_run         ', 'csv': '        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'next_maintenance_run         ', 'csv': '        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                 ', 'csv': '        ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'infra_id                     ', 'csv': '        ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'defined_tags                 ', 'csv': '        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags                ', 'csv': '        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date                 ', 'csv': '        ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_exa_infra - " + str(e))


##########################################################################
# Check Table Structure for handle_database_exa_cc_vms
##########################################################################
def handle_database_exa_cc_vms(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASE_EXA_CC_VMS",
            'csv_file': "database_db_exacc.csv",
            'items': [
                {'col': 'tenant_name         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id           ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                  ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name         ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path    ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name    ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status              ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'name                ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vm_name             ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape               ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'gi_version          ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'gi_version_date     ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'system_version      ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'system_version_date ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'database_edition    ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'license_model       ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'data_subnet         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'backup_subnet       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'scan_ips            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vip_ips             ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cluster_name        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'domain              ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'db_nodes            ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'db_homes            ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'maintenance_window  ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'last_maintenance_run', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'next_maintenance_run', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'infra_id            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cpu_core_count      ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'shape_ocpus         ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'db_storage_gb       ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'memory_gb           ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'local_storage_tb    ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_count          ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'defined_tags        ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags       ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created        ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date        ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_exa_cs_vms - " + str(e))


##########################################################################
# Check Table Structure for Database
##########################################################################
def handle_database(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASES",
            'csv_file': "database.csv",
            'items': [
                {'col': 'tenant_name         ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id           ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                  ', 'csv': 'database_id', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name         ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path    ', 'csv': '           ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name    ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status              ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'name                ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape               ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'cpu_core_count      ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'shape_ocpus         ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'db_storage_gb       ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'memory_gb           ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'local_storage_tb    ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_count          ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'database            ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'database_edition    ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'license_model       ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'data_subnet         ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'backup_subnet       ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'scan_ips            ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vip_ips             ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'pdbs                ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'cluster_name        ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vm_name             ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'domain              ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'auto_backup_enabled ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'db_nodes            ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'db_home             ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'db_home_version     ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'database_id         ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'dbsystem_id         ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags        ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags       ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created        ', 'csv': '           ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date        ', 'csv': '           ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database - " + str(e))


##########################################################################
# Check Table Structure for handle_database_vm_bm
##########################################################################
def handle_database_vm_bm(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASE_VM_BM",
            'csv_file': "database_db_vm_bm.csv",
            'items': [
                {'col': 'tenant_name         ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id           ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                  ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name         ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path    ', 'csv': '           ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name    ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status              ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'name                ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vm_name             ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape               ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'cpu_core_count      ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'shape_ocpus         ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'db_storage_gb       ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'memory_gb           ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'local_storage_tb    ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_count          ', 'csv': '           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'gi_version          ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'gi_version_date     ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'system_version      ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'system_version_date ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'database_edition    ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'license_model       ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'data_subnet         ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'backup_subnet       ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'scan_ips            ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vip_ips             ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cluster_name        ', 'csv': '           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'domain              ', 'csv': '           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'db_nodes            ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'db_homes            ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'infra_id            ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags        ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags       ', 'csv': '           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created        ', 'csv': '           ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date        ', 'csv': '           ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_vm_bm - " + str(e))


##########################################################################
# Check Table Structure for Databases
##########################################################################
def handle_database_autonomous(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASES_ADB",
            'csv_file': "database_autonomous.csv",
            'items': [
                {'col': 'tenant_name                  ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                    ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                           ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                  ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path             ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name             ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status                       ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                         ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'name                         ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'infra_name                   ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'cluster_name                 ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'container_name               ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'db_version                   ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'db_name                      ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'version_license_model        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'data_safe_status             ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'time_maintenance_begin       ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'time_maintenance_end         ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'subnet_id                    ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_name                  ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'private_endpoint             ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'private_endpoint_label       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'nsg_ids                      ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'nsg_names                    ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'whitelisted_ips              ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'service_console_url          ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'connection_strings           ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_auto_scaling_enabled      ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'is_data_guard_enabled        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'standby_lag_time_in_seconds  ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'standby_lifecycle_state      ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'time_of_last_switchover      ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_local_data_guard_enabled', 'csv': '     ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'dataguard_region_type        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'supported_regions_to_clone_to', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'key_store_wallet_name        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'key_store_id                 ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'is_dedicated                 ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'cpu_core_count               ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'db_storage_tb                ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'defined_tags                 ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags                ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                 ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                 ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_autonomous - " + str(e))


##########################################################################
# Check Table Structure for handle_database_goldengate_deployments
##########################################################################
def handle_database_goldengate_deployments(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DB_GOLDENGATE_DEP",
            'csv_file': "database_goldengate_deployments.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': 'display_name', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state             ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_id                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_name                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'license_model               ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'fqdn                        ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cpu_core_count              ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'is_auto_scaling_enabled     ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_public                   ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'public_ip_address           ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'private_ip_address          ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'deployment_url              ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_latest_version           ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'deployment_type             ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_updated                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_goldengate_deployments - " + str(e))


##########################################################################
# Check Table Structure for handle_database_mysql
##########################################################################
def handle_database_mysql(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DB_MYSQL",
            'csv_file': "database_mysql.csv",
            'items': [
                {'col': 'tenant_name                  ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                    ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                           ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                  ', 'csv': '            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name             ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path             ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                         ', 'csv': 'display_name', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'description                  ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_highly_available          ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'current_placement            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_analytics_cluster_attached', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'analytics_cluster            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_heat_wave_cluster_attached', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'heat_wave_cluster            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'availability_domain          ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'fault_domain                 ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'endpoints                    ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'endpoints_text               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'lifecycle_state              ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'mysql_version                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'deletion_policy              ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'shape_name                   ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'shape_ocpu                   ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'shape_memory_gb              ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'crash_recovery               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'backup_is_enabled            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'subnet_id                    ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'subnet_name                  ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'configuration_id             ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'source                       ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'hostname_label               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'ip_address                   ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'port                         ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'port_x                       ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'channels                     ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'maintenance                  ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_earliest_recovery_point ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_latest_recovery_point   ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'data_storage_size_in_gbs     ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                 ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                 ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_updated                 ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                 ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_mysql - " + str(e))


##########################################################################
# Check Table Structure for handle_database_nosql
##########################################################################
def handle_database_nosql(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DB_NOSQL",
            'csv_file': "database_nosql.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state             ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_auto_reclaimable         ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'capacity_mode               ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'max_read_units              ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'max_write_units             ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'max_storage_in_g_bs         ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'freeform_tags               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_of_expiration          ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_created                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_updated                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_nosql - " + str(e))


##########################################################################
# Check Table Structure for File Storage
##########################################################################
def handle_file_storage(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_FILE_STORAGE",
            'csv_file': "file_storage.csv",
            'items': [
                {'col': 'tenant_name        ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id          ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                 ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name        ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'availability_domain', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path   ', 'csv': '    ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name   ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'display_name       ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'size_gb            ', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'exports            ', 'csv': '    ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'snapshots          ', 'csv': '    ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'mount_ips          ', 'csv': '    ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'defined_tags       ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags      ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created       ', 'csv': '    ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date       ', 'csv': '    ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "display_name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_file_storage - " + str(e))


##########################################################################
# Check Table Structure for File Storage
##########################################################################
def handle_object_storage(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_OBJECT_STORAGE",
            'csv_file': "object_storage_buckets.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '          ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '          ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': 'bucket_id ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'namespace_name           ', 'csv': '          ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'region_name              ', 'csv': '          ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '          ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bucket_name              ', 'csv': '          ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'size_gb                  ', 'csv': '          ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'objects                  ', 'csv': '          ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'object_lifecycle         ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'public_access_type       ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'storage_tier             ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'is_read_only             ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'versioning               ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'auto_tiering             ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'kms_key_id               ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'logs                     ', 'csv': '          ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '          ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '          ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'preauthenticated_requests', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'object_events_enabled    ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'replication_enabled      ', 'csv': '          ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '          ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '          ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "bucket_name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_object_storage - " + str(e))


##########################################################################
# Check Table Structure for load_balancer_listeners
##########################################################################
def handle_load_balancer_listeners(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_LB_LISTENERS",
            'csv_file': "load_balancer_listeners.csv",
            'items': [
                {'col': 'tenant_name        ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id          ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                 ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'loadbalancer_id    ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path   ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name   ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'name               ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status             ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'shape              ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'type               ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ip_addresses       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'log_errors         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'log_access         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'logs               ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnets            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'listener_name      ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'listener_port      ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'listener_def_bs    ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'listener_ssl       ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'listener_host      ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'listener_path      ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'listener_rule      ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'lb_certificates    ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags       ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags      ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created       ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date       ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_load_balancer_listeners - " + str(e))


##########################################################################
# Check Table Structure for handle_load_balancer_backendset
##########################################################################
def handle_load_balancer_backendset(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_LB_BACKENDSET",
            'csv_file': "load_balancer_backendset.csv",
            'items': [
                {'col': 'tenant_name        ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id          ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                 ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name        ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path   ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name   ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'name               ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status             ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'shape              ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'type               ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ip_addresses       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnets            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bs_name            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bs_desc            ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bs_status          ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'health_check       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'session_persistence', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ssl_cert           ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'backend_name       ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'backend            ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'backend_ip         ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'loadbalancer_id    ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date       ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_load_balancer_backendset - " + str(e))


##########################################################################
# Check Table Structure for handle_paas_oac
##########################################################################
def handle_paas_oac(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_OAC",
            'csv_file': "paas_oac.csv",
            'items': [
                {'col': 'tenant_name             ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id               ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                      ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name             ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path        ', 'csv': '    ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name        ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'name                    ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state         ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'feature_set             ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'license_type            ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'capacity_type           ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'capacity_value          ', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'email_notification      ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'service_url             ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vanity_domain           ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vanity_url              ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'network_endpoint_details', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'defined_tags            ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags           ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created            ', 'csv': '    ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date            ', 'csv': '    ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_paas_oac - " + str(e))


##########################################################################
# Check Table Structure for handle_paas_oic
##########################################################################
def handle_paas_oic(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_OIC",
            'csv_file': "paas_oic.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'instance_url             ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'message_packs            ', 'csv': '     ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'is_byol                  ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_file_server_enabled   ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_visual_builder_enabled', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'network_endpoint_type    ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'consumption_model        ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'shape                    ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_paas_oic - " + str(e))


##########################################################################
# Check Table Structure for handle_paas_oce
##########################################################################
def handle_paas_oce(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_OCE",
            'csv_file': "paas_oce.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '     ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description              ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'guid                     ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'idcs_tenancy             ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'object_storage_namespace ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'admin_email              ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'service                  ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '     ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '     ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_paas_oce - " + str(e))


##########################################################################
# Check Table Structure for handle_paas_visual_builder
##########################################################################
def handle_paas_visual_builder(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_VISUAL_BUILDER",
            'csv_file': "paas_visualbuilder.csv",
            'items': [
                {'col': 'tenant_name               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name               ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path          ', 'csv': '             ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'name                      ', 'csv': 'display_name ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'instance_url              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'node_count                ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'is_visual_builder_enabled ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'custom_endpoint           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'alternate_custom_endpoints', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'consumption_model         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'defined_tags              ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created              ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_updated              ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date              ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_paas_visual_builder - " + str(e))


##########################################################################
# Check Table Structure for handle_paas_devops
##########################################################################
def handle_paas_devops(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DEVOPS",
            'csv_file': "paas_devops.csv",
            'items': [
                {'col': 'tenant_name               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name               ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path          ', 'csv': '             ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'name                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'namespace                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'notification_config       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'defined_tags              ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created              ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_updated              ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date              ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_paas_devops - " + str(e))


##########################################################################
# Check Table Structure for handle_containers
##########################################################################
def handle_containers(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_CONTAINERS",
            'csv_file': "containers.csv",
            'items': [
                {'col': 'tenant_name                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                            ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name                       ', 'csv': '             ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_path                       ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn                                    ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'node_pools                             ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'lifecycle_state                        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'kubernetes_version                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'endpoint_is_public_ip_enabled          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'endpoint_nsg_ids                       ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'endpoint_nsg_names                     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'endpoint_subnet_id                     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'endpoint_subnet_name                   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'option_lb_ids                          ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'option_network_pods_cidr               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'option_network_services_cidr           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'option_is_kubernetes_dashboard_enabled ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'option_is_tiller_enabled               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'option_is_pod_security_policy_enabled  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created                           ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_deleted                           ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_updated                           ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'created_by_user_id                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'deleted_by_user_id                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'updated_by_user_id                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'endpoint_kubernetes                    ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'endpoint_public_endpoint               ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'endpoint_private_endpoint              ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'endpoint_vcn_hostname_endpoint         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'available_kubernetes_upgrades          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags                          ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                           ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vcn_id                                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'extract_date                           ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_paas_visual_builder - " + str(e))


##########################################################################
# Check Table Structure for handle_containers_nodepools
##########################################################################
def handle_containers_nodepools(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_CONTAINERS_NODEPOOLS",
            'csv_file': "containers_nodepools.csv",
            'items': [
                {'col': 'tenant_name               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                        ', 'csv': 'node_pool_id ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name               ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name          ', 'csv': '             ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_path          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'container_name            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'node_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'node_image_name           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'kubernetes_version        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'node_shape                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'quantity_per_subnet       ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_shape_mem_gb         ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_shape_ocpus          ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_source_type          ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'node_source_name          ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vcn                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnets                   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'subnet_ids                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'container_id              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'node_pool_id              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_id                    ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags              ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date              ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "node_name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_containers_nodepools - " + str(e))


##########################################################################
# Check Table Structure for handle_apigw
##########################################################################
def handle_apigw(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_APIGW",
            'csv_file': "api_gateways.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': 'dp_id        ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'gw_name                  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'gw_endpoint_type         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'gw_hostname              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'gw_subnet_id             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'gw_subnet_name           ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'gw_time_created          ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'gw_time_updated          ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'gw_lifecycle_state       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'gw_nsg_ids               ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'gw_nsg_names             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'gw_certificate_id        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'gw_freeform_tags         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'gw_defined_tags          ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'dp_display_name          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'path_prefix              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'endpoint                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_updated             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'log_execution            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'log_access               ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'logs                     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'dp_id                    ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'api_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "api_id", "gw_name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_apigw - " + str(e))


##########################################################################
# Check Table Structure for handle_network_vcn
##########################################################################
def handle_network_vcn(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_VCN",
            'csv_file': "network_vcn.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': 'vcn_id       ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment              ', 'csv': '             ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cidr                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cidrs                    ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'internet_gateway         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'service_gateway          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'nat                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'drg                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'local_peering            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'subnets                  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnets_cidrs            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_vcn - " + str(e))


##########################################################################
# Check Table Structure for handle_network_subnet
##########################################################################
def handle_network_subnet(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_SUBNET",
            'csv_file': "network_subnet.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': 'subnet_id    ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vcn_compartment          ', 'csv': '             ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'vcn_compartment_path     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidr                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidrs                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'internet_gateway         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'service_gateway          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'nat                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'drg                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'local_peering            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'subnet_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_cidr              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'availability_domain      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_compartment       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_compartment_path  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'public_private           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'dhcp_options             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'route                    ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'security_list            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'dns                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'logs                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "subnet_name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_subnet - " + str(e))


##########################################################################
# Check Table Structure for handle_network_subnet_private_ips
##########################################################################
def handle_network_subnet_private_ips(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_SUBNET_PRV_IPS",
            'csv_file': "network_subnet_prv_ips.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': 'privateip_id ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vcn_compartment          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_compartment_path     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vcn_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidr                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidrs                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'subnet_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_cidr              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_compartment       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_compartment_path  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ip_address               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'display_name             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'hostname_label           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_primary               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ip_compartment_name      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ip_compartment_path      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'privateip_id             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vlan_id                  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "ip_address")
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_subnet_private_ips - " + str(e))


##########################################################################
# Check Table Structure for handle_network_security_list
##########################################################################
def handle_network_security_list(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_SECLIST_RULES",
            'csv_file': "network_security_list.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vcn_compartment          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_compartment_path     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vcn_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidr                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidrs                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'sec_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'sec_compartment          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'sec_compartment_path     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'sec_protocol             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'sec_rules                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_stateless             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'sec_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_security_list - " + str(e))


##########################################################################
# Check Table Structure for handle_network_security_groups
##########################################################################
def handle_network_security_groups(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_SECGROUPS_RULES",
            'csv_file': "network_security_group.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vcn_compartment          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_compartment_path     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vcn_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidr                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidrs                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'sec_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'sec_compartment          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'sec_compartment_path     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'sec_protocol             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'sec_rules                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_stateless             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'sec_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_security_groups - " + str(e))


##########################################################################
# Check Table Structure for handle_network_drg
##########################################################################
def handle_network_drg(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_DRGS",
            'csv_file': "network_drgs.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'redundancy               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'drg_route_tables         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'ip_sec_connections       ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'virtual_circuits         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'remote_peerings          ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vcns                     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_drg - " + str(e))


##########################################################################
# Check Table Structure for handle_network_firewall
##########################################################################
def handle_network_firewall(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_FIREWALL",
            'csv_file': "network_firewalls.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'availability_domain         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ipv4_address                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ipv6_address                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'network_firewall_policy_id  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'network_firewall_policy_name', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags               ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_updated                ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_firewall - " + str(e))


##########################################################################
# Check Table Structure for handle_network_dhcp_options
##########################################################################
def handle_network_dhcp_options(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_DHCP_OPTIONS",
            'csv_file': "network_dhcp_options.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': 'dhcp_id      ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vcn_compartment          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_compartment_path     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vcn_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidr                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidrs                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'dhcp_name                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'option_1                 ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'option_2                 ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'dhcp_compartment         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'dhcp_compartment_path    ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vcn_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_dhcp_options - " + str(e))


##########################################################################
# Check Table Structure for handle_network_routes
##########################################################################
def handle_network_routes(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_ROUTES",
            'csv_file': "network_routes.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vcn_compartment          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_compartment_path     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vcn_name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidr                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_cidrs                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'route_name               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'route_compartment        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'route_compartment_path   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'destination              ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'route                    ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'route_id                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_routes - " + str(e))


##########################################################################
# Check Table Structure for handle_network_drg_virtual_circuit
##########################################################################
def handle_network_drg_virtual_circuit(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_DRG_VC",
            'csv_file': "network_drg_virtual_circuits.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bandwidth_shape_name     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bgp_management           ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'bgp_session_state        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bgp_ipv6_session_state   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bgp_admin_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_bfd_enabled           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'customer_asn             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'gateway_id               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'provider_service_id      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'provider_service_key_name', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'routing_policy           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'public_prefixes          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'region                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'customer_bgp_asn         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'drg                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'oracle_bgp_asn           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'provider_name            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'provider_service_name    ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'provider_state           ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'reference_comment        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'service_type             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cross_connect_mappings   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'type                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'drg_route_table          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'drg_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'drg_route_table_id       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_drg_virtual_circuit - " + str(e))


##########################################################################
# Check Table Structure for handle_network_drg_ipsec
##########################################################################
def handle_network_drg_ipsec(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_NETWORK_DRG_IPSEC",
            'csv_file': "network_drg_ipsec_tunnels.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'tunnel_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'routing                  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bgp_info                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ipsec_name               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'drg                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'drg_route_table          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cpe                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cpe_local_identifier     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'routes                   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'drg_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cpe_id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ipsec_id                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'cpe_time_created         ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "tunnel_name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_network_drg_ipsec - " + str(e))


##########################################################################
# Check Table Structure for handle_data_ai_oda
##########################################################################
def handle_data_digital_assistance(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DIGITAL_ASSISTANCE",
            'csv_file': "digital_assistance.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'shape_name               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_role_based_access     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'identity_domain          ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'imported_package_names   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'attachment_types         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_data_ai_oda - " + str(e))


##########################################################################
# Check Table Structure for handle_data_ai_bds
##########################################################################
def handle_big_data_service(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_BIG_DATA",
            'csv_file': "big_data_service.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'number_of_nodes          ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'is_high_availability     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cluster_version          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cluster_profile          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_secure                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_cloud_sql_configured  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_data_ai_bds - " + str(e))


##########################################################################
# Check Table Structure for handle_network_data_flow
##########################################################################
def handle_data_flow(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATA_FLOW",
            'csv_file': "data_flow.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'language                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'owner_principal_id       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'owner_user_name          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'spark_version            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'type                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_data_flow - " + str(e))


##########################################################################
# Check Table Structure for handle_data_catalog
##########################################################################
def handle_data_catalog(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATA_CATALOG",
            'csv_file': "data_catalog.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'number_of_objects        ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'attached_catalog_private_endpoints', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_data_catalog - " + str(e))


##########################################################################
# Check Table Structure for handle_data_conn_registry
##########################################################################
def handle_data_conn_registry(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATA_CONN_REGISTRY",
            'csv_file': "data_conn_registry.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'conn_id                  ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_updated             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_data_conn_registry - " + str(e))


##########################################################################
# Check Table Structure for handle_data_science
##########################################################################
def handle_data_science(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATA_SCIENCE",
            'csv_file': "data_science.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_data_science - " + str(e))


##########################################################################
# Check Table Structure for handle_data_integration
##########################################################################
def handle_data_integration(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATA_INTEGRATION",
            'csv_file': "data_integration.csv",
            'items': [
                {'col': 'tenant_name              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name              ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags            ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date             ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_data_integration - " + str(e))


##########################################################################
# Check Table Structure for handle_streams_queues
##########################################################################
def handle_streams_queues(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_STREAMS_QUEUES",
            'csv_file': "streams_queues.csv",
            'items': [
                {'col': 'tenant_name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                     ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'type                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'partitions                      ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'retention_in_seconds            ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'visibility_in_seconds           ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'timeout_in_seconds              ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'dead_letter_queue_delivery_count', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'custom_encryption_key_id        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'messages_endpoint               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags                   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                    ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_streams_queues - " + str(e))


##########################################################################
# Check Table Structure for handle_edge_web_application_firewall
##########################################################################
def handle_edge_web_application_firewall(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_WAF",
            'csv_file': "edge_web_application_firewall.csv",
            'items': [
                {'col': 'tenant_name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                     ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'backend_type                    ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'web_app_firewall_policy_id      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags                   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                    ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_edge_web_application_firewall - " + str(e))


##########################################################################
# Check Table Structure for handle_edge_healthchecks
##########################################################################
def handle_edge_healthchecks(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_HEALTHCHECKS",
            'csv_file': "edge_healthchecks.csv",
            'items': [
                {'col': 'tenant_name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                     ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                            ', 'csv': 'display_name ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'type                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'results_url                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'targets                         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'vantage_point_names             ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'port                            ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'timeout_in_seconds              ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'interval_in_seconds             ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'protocol                        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'method                          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'path                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'headers                         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_enabled                      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags                   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                    ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_edge_healthchecks - " + str(e))


##########################################################################
# Check Table Structure for handle_edge_dns_steering_policies
##########################################################################
def handle_edge_dns_steering_policies(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DNS_STEERING_POL",
            'csv_file': "edge_dns_steering_policies.csv",
            'items': [
                {'col': 'tenant_name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                     ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'ttl                             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'template                        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'health_check_monitor_id         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'lifecycle_state                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags                   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                    ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_edge_dns_steering_policies - " + str(e))


##########################################################################
# Check Table Structure for handle_identity_compartments
##########################################################################
def handle_identity_compartments(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_IAM_COMPARTMENTS",
            'csv_file': "identity_compartments.csv",
            'items': [
                {'col': 'tenant_name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'name                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'path                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_accessible                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'inactive_status                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags                   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                    ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_identity_compartments - " + str(e))


##########################################################################
# Check Table Structure for handle_security_bastions
##########################################################################
def handle_security_bastions(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_SECURITY_BASTIONS",
            'csv_file': "security_bastions.csv",
            'items': [
                {'col': 'tenant_name          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name          ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'target_vcn_name      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'target_subnet_name   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'bastion_type         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state      ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags        ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'target_vcn_id        ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'target_subnet_id     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_updated         ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_created         ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date         ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_security_bastions - " + str(e))


##########################################################################
# Check Table Structure for handle_security_cloud_guard
##########################################################################
def handle_security_cloud_guard(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_SECURITY_CLOUDGUARD",
            'csv_file': "security_cloud_guards.csv",
            'items': [
                {'col': 'tenant_name                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                     ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path                ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'target_resource_type            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'target_resource_id              ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'target_resource_name            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'inherited_by_compartments       ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'inherited_by_compartments_names ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'target_detector_recipes         ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'target_responder_recipes        ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'target_detector_rules           ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'target_responder_rules          ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'recipe_count                    ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'lifecycle_state                 ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags                   ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                    ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_updated                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_created                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                    ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_security_cloud_guard - " + str(e))


##########################################################################
# Check Table Structure for handle_paas_open_search
##########################################################################
def handle_paas_open_search(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_OPEN_SEARCH",
            'csv_file': "paas_opensearch.csv",
            'items': [
                {'col': 'tenant_name                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                       ', 'csv': '             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name                  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path                  ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                              ', 'csv': 'display_name ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'software_version                  ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'total_storage_gb                  ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'security_mode                     ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'availability_domains              ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'opensearch_fqdn                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'opensearch_private_ip             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'opendashboard_fqdn                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'opendashboard_private_ip          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'master_node_count                 ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'master_node_host_type             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'master_node_host_bare_metal_shape ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'master_node_host_ocpu_count       ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'master_node_host_memory_gb        ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'data_node_count                   ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'data_node_host_type               ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'data_node_host_bare_metal_shape   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'data_node_host_ocpu_count         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'data_node_host_memory_gb          ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'data_node_storage_gb              ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'opendashboard_node_count          ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'opendashboard_node_host_ocpu_count', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'opendashboard_node_host_memory_gb ', 'csv': '             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'vcn_id                            ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_name                          ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_id                         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_name                       ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vcn_compartment_id                ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'subnet_compartment_id             ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'security_master_user_name         ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'security_master_user_password_hash', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state                   ', 'csv': '             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags                     ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                      ', 'csv': '             ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_updated                      ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'time_created                      ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                      ', 'csv': '             ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_paas_open_search - " + str(e))


##########################################################################
# Check Table Structure for handle_security_kms_vaults
##########################################################################
def handle_security_kms_vaults(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_SECURITY_KMS_VAULTS",
            'csv_file': "security_kms_vaults.csv",
            'items': [
                {'col': 'tenant_name               ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                 ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                        ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name               ', 'csv': '    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name          ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path          ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                      ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'crypto_endpoint           ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'management_endpoint       ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vault_type                ', 'csv': '    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'key_count                 ', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'key_version_count         ', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'software_key_count        ', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'software_key_version_count', 'csv': '    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'freeform_tags             ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags              ', 'csv': '    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created              ', 'csv': '    ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date              ', 'csv': '    ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_security_kms_vaults - " + str(e))


##########################################################################
# Check Table Structure for handle_security_logging
##########################################################################
def handle_security_logging(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_SECURITY_LOGGINGS",
            'csv_file': "security_loggings.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': 'log_id', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '      ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '      ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'log_group                   ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'log_group_description       ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'log_name                    ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_enabled                  ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state             ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'log_type                    ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'retention_duration          ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'archiving                   ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'source_service              ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'source_category             ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'source_sourcetype           ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'source_resource             ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags               ', 'csv': '      ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'source_parameters           ', 'csv': '      ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                ', 'csv': '      ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_last_modified          ', 'csv': '      ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'log_group_time_last_modified', 'csv': '      ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'log_group_id                ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'log_id                      ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created                ', 'csv': '      ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '      ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "log_name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_security_logging - " + str(e))


##########################################################################
# Check Table Structure for handle_limits
##########################################################################
def handle_limits(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_LIMITS",
            'csv_file': "limits.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'scope_type                  ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'availability_domain         ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description                 ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'limit_name                  ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'value                       ', 'csv': '      ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'used                        ', 'csv': '      ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'available                   ', 'csv': '      ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '      ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_limits - " + str(e))


##########################################################################
# Check Table Structure for handle_quotas
##########################################################################
def handle_quotas(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_QUOTAS",
            'csv_file': "quotas.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '      ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '      ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description                 ', 'csv': '      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'statements                  ', 'csv': '      ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                ', 'csv': '      ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '      ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_quotas - " + str(e))


##########################################################################
# Check Table Structure for handle_monitor_agents
##########################################################################
def handle_monitor_agents(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_MONITOR_AGENTS",
            'csv_file': "monitor_agents.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': 'display_name', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'platform_name               ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'platform_type               ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'platform_version            ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'version                     ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_agent_auto_upgradable    ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'host                        ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'plugin_list                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_last_heartbeat         ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'availability_status         ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'install_key_id              ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_monitor_agents - " + str(e))


##########################################################################
# Check Table Structure for handle_monitor_agents
##########################################################################
def handle_monitor_events(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_MONITOR_EVENTS",
            'csv_file': "monitor_events.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': 'display_name', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'description                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'condition                   ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_enabled                  ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'actions                     ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_monitor_events - " + str(e))


##########################################################################
# Check Table Structure for handle_monitor_alarms
##########################################################################
def handle_monitor_alarms(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_MONITOR_ALARMS",
            'csv_file': "monitor_alarms.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': 'display_name', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'namespace                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'query                       ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'severity                    ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'destinations                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'destinations_names          ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_enabled                  ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'metric_compartment_id       ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'freeform_tags               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_monitor_alarms - " + str(e))


##########################################################################
# Check Table Structure for handle_monitor_notifications
##########################################################################
def handle_monitor_notifications(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_MONITOR_NOTIFICATIONS",
            'csv_file': "monitor_topics_subs.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'topic_compartment_name      ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'topic_compartment_path      ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'topic_name                  ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'topic_description           ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'topic_etag                  ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'topic_api_endpoint          ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'topic_freeform_tags         ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'topic_defined_tags          ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'topic_id                    ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'protocol                    ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'endpoint                    ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'created_time                ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'topic_time_created          ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json)
    except Exception as e:
        raise Exception("\nError at procedure: handle_monitor_notifications - " + str(e))


##########################################################################
# Check Table Structure for handle_monitor_db_management
##########################################################################
def handle_monitor_db_management(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_MONITOR_DB_MANAGEMENT",
            'csv_file': "monitor_db_managements.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'database_type               ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'database_sub_type           ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_cluster                  ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'parent_container_id         ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'deployment_type             ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'management_option           ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'workload_type               ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'db_system_id                ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'storage_system_id           ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_monitor_db_management - " + str(e))


##########################################################################
# Check Table Structure for handle_compute_reservations
##########################################################################
def handle_compute_reservations(connection):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_COMPUTE_RESERVATIONS",
            'csv_file': "compute_reservations.csv",
            'items': [
                {'col': 'tenant_name                 ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id                   ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'id                          ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name                 ', 'csv': '            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_name            ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'compartment_path            ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'name                        ', 'csv': 'display_name', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'lifecycle_state             ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'availability_domain         ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'is_default_reservation      ', 'csv': '            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'reserved_instance_count     ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'used_instance_count         ', 'csv': '            ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'shapes                      ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'shapes_capacity             ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags               ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'defined_tags                ', 'csv': '            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date                ', 'csv': '            ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, "id", "name")
    except Exception as e:
        raise Exception("\nError at procedure: handle_compute_reservations - " + str(e))


##########################################################################
# Check Table Structure for Compute
##########################################################################
def variable_generation(item, index):
    if 'number' in item['type']:
        return "to_number(:" + str(index) + ")"
    if 'date' in item['type']:
        return "to_date(:" + str(index) + ",'YYYY-MM-DD HH24:MI')"
    return ":" + str(index) + " "


##########################################################################
# Check Table Structure for Compute
##########################################################################
def handle_old_structure(connection):
    try:

        # check if tables exist
        with connection.cursor() as cursor:

            # tables that need to drop
            for table_name in ["OCI_SHOWOCI_DATABASE_SYSTEMS",
                               "OCI_SHOWOCI_DATABASE_SYSTEMS_TMP",
                               "OCI_SHOWOCI_SECURITY_CLOUDGUARD_TMP",
                               "OCI_SHOWOCI_SECURITY_CLOUDGUARD"]:

                sql = "select count(*) from user_tables where table_name = :table_name"
                cursor.execute(sql, table_name=table_name)
                val, = cursor.fetchone()

                # if table exist drop
                if val > 0:
                    sql = "drop table " + table_name
                    cursor.execute(sql)

    except oracledb.DatabaseError as e:
        print("\nDatabaseError at procedure: handle_table() - handle_old_structure " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError at Procedure: handle_table() - handle_old_structure " + str(e))


##########################################################################
# Check Resource Table Structure
##########################################################################
def check_database_table_structure_resource(connection):
    global cmd
    verbose = cmd.verbose

    try:
        # open cursor
        with connection.cursor() as cursor:

            # check if OCI_USAGE table exist, if not create
            sql = "select count(*) from user_tables where table_name = 'OCI_RESOURCES'"
            cursor.execute(sql)
            val, = cursor.fetchone()

            # if table not exist, create it
            if val == 0:
                if verbose:
                    print("   Table OCI_RESOURCES was not exist, creating")

                sql = """create table OCI_RESOURCES (
                    RESOURCE_ID             VARCHAR2(200) NOT NULL,
                    RESOURCE_NAME           VARCHAR2(1000),
                    SOURCE_TENANT           VARCHAR2(100),
                    SOURCE_TABLE            VARCHAR2(100),
                    LAST_LOADED             DATE,
                    CONSTRAINT OCI_RESOURCES_PK PRIMARY KEY (RESOURCE_ID) USING INDEX)"""

                cursor.execute(sql)
                if verbose:
                    print("   Table OCI_RESOURCES created")

    except oracledb.DatabaseError as e:
        print("\nError manipulating database at check_database_table_structure_resource() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at check_database_table_structure_resource() - " + str(e))


##########################################################################
# Check Table Structure for Compute
##########################################################################
def handle_table(connection, inputdata, resource_id="", resource_name="", resource_prefix=""):
    global cmd
    global file_num
    process_location = "Start"
    try:
        start_time = time.time()
        file_num += 1
        file_num_str = str(str(file_num) + ".   ")[0:4]

        # Input Parameters from CMD
        csv_location = cmd.csv_location
        drop_before_load = cmd.drop
        verbose = cmd.verbose

        # Parameters
        csv_file = inputdata['csv_file']
        path_filename = csv_location + '_' + csv_file
        table_name = inputdata['table_name']
        csv_table_name_lpad = table_name.ljust(40) + " " + csv_file.ljust(35)
        tmp_table_name = table_name + "_TMP"
        compute_sql_columns = str(',\n '.join(x['col'] + " " + x['type'] for x in inputdata['items']))
        merge_sql_columns = str(', '.join("a." + x['col'] + " = b." + x['col'] for x in inputdata['items'] if x['pk'] != "y"))
        insert_def_sql_columns = str(', '.join(x['col'] for x in inputdata['items']))
        insert_val_sql_columns = str(', '.join("b." + x['col'] for x in inputdata['items']))
        primary_key = next((col for col in inputdata['items'] if col['pk'] == "y"), None)['col']
        insert_bulk_func = str(', '.join(variable_generation(x, index) for index, x in enumerate(inputdata['items'], start=1)))

        # Check if file exist
        if not os.path.isfile(path_filename):
            if verbose:
                print("\nFile " + path_filename + " does not exist, skipping...")
            else:
                print(file_num_str + csv_table_name_lpad + " ---> Does not exist, skipping...")
            return

        if verbose:
            print("\nHandling " + table_name + " - " + path_filename)
        else:
            print(file_num_str + csv_table_name_lpad, end="")

        ################################################
        # Check Table Structure and create if not exist
        ################################################
        process_location = "Checking Table Structure"

        # check if tables exist
        with connection.cursor() as cursor:

            sql = "select count(*) from user_tables where table_name = :table_name"
            cursor.execute(sql, table_name=table_name)
            val, = cursor.fetchone()

            # if main table exist and drop before load
            if val > 0 and drop_before_load:
                if verbose:
                    print("   Table " + table_name + " exist, but drop flag enabled, dropping..")
                else:
                    print(" Drop Flag, ", end="")

                sql = "drop table " + table_name
                cursor.execute(sql)
                val = 0

            # if main table not exist, create it
            if val == 0:
                if verbose:
                    print("   Table " + table_name + " was not exist, creating, ", end="")
                sql = "create table " + table_name + " ( " + compute_sql_columns + " ,CONSTRAINT " + table_name + "_PK PRIMARY KEY (" + primary_key + ") USING INDEX) "
                cursor.execute(sql)
                if verbose:
                    print("Table " + table_name + " created")

            # check if temp table exist, if not create
            sql = "select count(*) from user_tables where table_name = :table_name"
            cursor.execute(sql, table_name=tmp_table_name)
            val, = cursor.fetchone()

            # if temp table exist and drop before load
            if val > 0 and drop_before_load:
                if verbose:
                    print("   Table " + tmp_table_name + " exist, but drop flag enabled, dropping..")
                sql = "drop table " + tmp_table_name
                cursor.execute(sql)
                val = 0

            # if table not exist, create it
            if val == 0:
                if verbose:
                    print("   Table " + tmp_table_name + " was not exist, creating, ", end="")
                sql = "create GLOBAL TEMPORARY TABLE " + tmp_table_name + " ( " + compute_sql_columns + " ) ON COMMIT PRESERVE ROWS "
                cursor.execute(sql)
                if verbose:
                    print("Table " + tmp_table_name + " created")

        ################################################
        # Load Data
        ################################################
        num_rows = 0
        process_location = "Before Load Data"

        with open(path_filename, 'rt') as file_in:
            csv_reader = csv.DictReader(file_in)

            # Adjust the batch size to meet memory and performance requirements for oracledb
            batch_size = 5000
            array_size = 1000

            sql = "INSERT INTO " + tmp_table_name + " ("
            sql += insert_def_sql_columns
            sql += ") VALUES ( "
            sql += insert_bulk_func + ")"

            # insert bulk to database
            with connection.cursor() as cursor:

                # Predefine the memory areas to match the table definition
                cursor.setinputsizes(None, array_size)
                process_location = "before CSV load"

                data = []
                for row in csv_reader:
                    rowarray = []
                    for item in inputdata['items']:
                        column = str(item['csv']).strip()
                        if not column:
                            column = str(item['col']).strip()
                        limit_size = 16 if 'date' in item['type'] else 3999
                        value = get_column_value_from_array(column, row, limit_size)
                        rowarray.append(value)
                    data.append(tuple(rowarray))
                    num_rows += 1

                    # executemany every batch size
                    process_location = "before executemany"
                    if len(data) % batch_size == 0:
                        cursor.executemany(sql, data)
                        data = []

                # if data exist final execute
                if data:
                    cursor.executemany(sql, data)

                if verbose:
                    print("   Loading data to tmp  table... Insert Completed, " + str(num_rows) + " Rows Inserted")
                else:
                    print(" TMP = " + str(num_rows).ljust(7), end="")

                connection.commit()

        ################################################
        # Merge data from tmp to main table
        ################################################
        process_location = "before Merge"

        with connection.cursor() as cursor:

            if verbose:
                print("   Merging data to main table... ", end="")

            # run merge to oci_update_stats
            sql = "merge into " + table_name + " a using " + tmp_table_name + " b "
            sql += "on (a." + primary_key + " = b." + primary_key + ")"
            sql += "when matched then update set "
            sql += merge_sql_columns
            sql += "when not matched then insert ("
            sql += insert_def_sql_columns
            sql += ") values ("
            sql += insert_val_sql_columns + ")"

            cursor.execute(sql)
            connection.commit()

            if verbose:
                print("Merge  Completed, " + str(cursor.rowcount) + " rows merged" + get_time_elapsed(start_time))
            else:
                print(" Merged = " + str(cursor.rowcount).ljust(7), end="")

        if resource_id:
            ################################################
            # Merge data from tmp to resource table
            ################################################
            process_location = "before Resrouce Merge"

            with connection.cursor() as cursor:

                if verbose:
                    print("   Merging data to ocid table... ", end="")

                # run merge to oci_update_stats
                sql = "merge into oci_resources a using "
                sql += "(select distinct " + resource_id + " as id, '" + resource_prefix + "'||" + resource_name + " as name, "
                sql += "'" + table_name + "' as table_name, TENANT_NAME from " + tmp_table_name + ") b "
                sql += """on (a.resource_id = b.id)
                          when matched then update set
                          a.RESOURCE_NAME = b.NAME,
                          a.SOURCE_TABLE = b.TABLE_NAME,
                          a.SOURCE_TENANT = b.TENANT_NAME,
                          a.LAST_LOADED = SYSDATE
                          when not matched then insert
                          (RESOURCE_ID,RESOURCE_NAME,SOURCE_TABLE,SOURCE_TENANT,LAST_LOADED)
                          values
                          (b.ID,b.NAME,b.TABLE_NAME,b.TENANT_NAME,SYSDATE)"""

                cursor.execute(sql)
                connection.commit()

                if verbose:
                    print("Merge  Completed, " + str(cursor.rowcount) + " rows merged" + get_time_elapsed(start_time))
                else:
                    print(" OCIDs = " + str(cursor.rowcount))

        # if no resource id
        else:
            if not verbose:
                print("")

    except oracledb.DatabaseError as e:
        print("\nDatabaseError at procedure: handle_table() - " + process_location + " - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError at Procedure: handle_table() - " + process_location + " - " + str(e))


##########################################################################
# Main
##########################################################################
def main_process():
    global cmd
    cmd = set_parser_arguments()
    if cmd is None:
        exit()

    ############################################
    # Start
    ############################################
    print_header("Running ShowOCI_CSV2ADW", 0)
    print("Starts at " + get_current_date_time())
    print("Command Line : " + ' '.join(x for x in sys.argv[1:]))
    print("Version      : " + version)

    # Init the Oracle Thick Client Library in order to use sqlnet.ora and instant client
    if cmd.usethick:
        oracledb.init_oracle_client()
        print("OracleDB     : Thick Drivers")
    else:
        print("OracleDB     : Thin Drivers")

    ############################################
    # connect to database
    ############################################
    try:
        print("\nConnecting to database " + cmd.dname, end="")
        with oracledb.connect(user=cmd.duser, password=cmd.dpass, dsn=cmd.dname, config_dir=cmd.wallet_location, wallet_location=cmd.wallet_location, wallet_password=cmd.wallet_password) as connection:

            print("...Connected\n")

            # Checking structure of tables
            handle_old_structure(connection)
            check_database_table_structure_resource(connection)

            # Handling CSVs
            handle_compute(connection)
            handle_compute_reservations(connection)
            handle_block_volume(connection)
            handle_block_volume_backups(connection)
            handle_database_all(connection)
            handle_database(connection)
            handle_database_backups(connection)
            handle_database_exa_cs_vms(connection)
            handle_database_exa_cc_vms(connection)
            handle_database_exa_infra(connection)
            handle_database_autonomous(connection)
            handle_database_vm_bm(connection)
            handle_database_goldengate_deployments(connection)
            handle_database_nosql(connection)
            handle_database_mysql(connection)
            handle_file_storage(connection)
            handle_object_storage(connection)
            handle_load_balancer_listeners(connection)
            handle_load_balancer_backendset(connection)
            handle_paas_oac(connection)
            handle_paas_oic(connection)
            handle_paas_oce(connection)
            handle_paas_visual_builder(connection)
            handle_paas_devops(connection)
            handle_paas_open_search(connection)
            handle_containers(connection)
            handle_containers_nodepools(connection)
            handle_apigw(connection)
            handle_network_vcn(connection)
            handle_network_drg(connection)
            handle_network_subnet(connection)
            handle_network_subnet_private_ips(connection)
            handle_network_security_groups(connection)
            handle_network_security_list(connection)
            handle_network_dhcp_options(connection)
            handle_network_routes(connection)
            handle_network_drg_virtual_circuit(connection)
            handle_network_drg_ipsec(connection)
            handle_network_firewall(connection)
            handle_data_digital_assistance(connection)
            handle_big_data_service(connection)
            handle_data_flow(connection)
            handle_data_catalog(connection)
            handle_data_conn_registry(connection)
            handle_data_science(connection)
            handle_data_integration(connection)
            handle_streams_queues(connection)
            handle_edge_web_application_firewall(connection)
            handle_edge_healthchecks(connection)
            handle_edge_dns_steering_policies(connection)
            handle_identity_compartments(connection)
            handle_security_bastions(connection)
            handle_security_cloud_guard(connection)
            handle_security_kms_vaults(connection)
            handle_security_logging(connection)
            handle_limits(connection)
            handle_quotas(connection)
            handle_monitor_agents(connection)
            handle_monitor_events(connection)
            handle_monitor_db_management(connection)
            handle_monitor_alarms(connection)
            handle_monitor_notifications(connection)

    except oracledb.DatabaseError as e:
        print("\nError manipulating database - " + str(e) + "\n")

    except Exception as e:
        print("\nError appeared - " + str(e))

    ############################################
    # print completed
    ############################################
    print("\nCompleted at " + get_current_date_time())


##########################################################################
# Execute Main Process
##########################################################################
main_process()
