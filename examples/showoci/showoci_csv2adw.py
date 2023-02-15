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
# - OCI_SHOWOCI_BLOCK_VOLUMES
# - OCI_SHOWOCI_DATABASE_SYSTEMS
# - OCI_SHOWOCI_DATABASES_ADB
##########################################################################
import sys
import argparse
import datetime
import csv
import oracledb
import time
import os

version = "23.02.14"


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
        return array[column][0:limit_size]
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
    parser.add_argument('-csv', default="", dest='csvlocation', help='CSV Location from showoci including header')
    parser.add_argument('-du', default="", dest='duser', help='ADB User')
    parser.add_argument('-dp', default="", dest='dpass', help='ADB Password')
    parser.add_argument('-dn', default="", dest='dname', help='ADB DSN')

    parser.add_argument('-usethick', action='store_true', default=False, dest='usethick', help='Use sqlnet thick client library')
    parser.add_argument('-wl', default="", dest='wallet_location', help='Wallet Location')
    parser.add_argument('-wp', default="", dest='wallet_password', help='Wallet Password')

    parser.add_argument('--version', action='version', version='%(prog)s ' + version)

    result = parser.parse_args()

    if not (result.duser and result.dpass and result.dname and result.csvlocation):
        parser.print_help()
        print_header("You must specify database credentials and csv location!!", 0)
        return None

    return result


##########################################################################
# Check Table Structure for Compute
##########################################################################
def handle_compute(connection, csv_location):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_COMPUTE",
            'csv_file': "compute.csv",
            'items': [
                {'col': 'tenant_name           ', 'csv': 'tenant_name           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id             ', 'csv': 'tenant_id             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'instance_id           ', 'csv': 'instance_id           ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name           ', 'csv': 'region_name           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain   ', 'csv': 'availability_domain   ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'fault_domain          ', 'csv': 'fault_domain          ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path      ', 'csv': 'compartment_path      ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name      ', 'csv': 'compartment_name      ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'server_name           ', 'csv': 'server_name           ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status                ', 'csv': 'status                ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                  ', 'csv': 'type                  ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'image                 ', 'csv': 'image                 ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'primary_vcn           ', 'csv': 'primary_vcn           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'primary_subnet        ', 'csv': 'primary_subnet        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape                 ', 'csv': 'shape                 ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'ocpus                 ', 'csv': 'ocpus                 ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'memory_gb             ', 'csv': 'memory_gb             ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'local_storage_tb      ', 'csv': 'local_storage_tb      ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'public_ips            ', 'csv': 'public_ips            ', 'type': 'varchar2(500) ', 'pk': 'n'},
                {'col': 'private_ips           ', 'csv': 'private_ips           ', 'type': 'varchar2(500) ', 'pk': 'n'},
                {'col': 'security_groups       ', 'csv': 'security_groups       ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'internal_fqdn         ', 'csv': 'internal_fqdn         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'time_created          ', 'csv': 'time_created          ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'boot_volume           ', 'csv': 'boot_volume           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'boot_volume_size_gb   ', 'csv': 'boot_volume_size_gb   ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'boot_volume_b_policy  ', 'csv': 'boot_volume_b_policy  ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'boot_volume_encryption', 'csv': 'boot_volume_encryption', 'type': 'varchar2(20)  ', 'pk': 'n'},
                {'col': 'block_volumes         ', 'csv': 'block_volumes         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'block_volumes_total_gb', 'csv': 'block_volumes_total_gb', 'type': 'number        ', 'pk': 'n'},
                {'col': 'block_volumes_b_policy', 'csv': 'block_volumes_b_policy', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'defined_tags          ', 'csv': 'defined_tags          ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags         ', 'csv': 'freeform_tags         ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date          ', 'csv': 'extract_date          ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, csv_location)
    except Exception as e:
        raise Exception("\nError at procedure: handle_compute - " + str(e))


##########################################################################
# Check Table Structure for Block Storage
##########################################################################
def handle_block_volume(connection, csv_location):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_BLOCK_VOLUMES",
            'csv_file': "block_volumes.csv",
            'items': [
                {'col': 'tenant_name        ', 'csv': 'tenant_name        ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id          ', 'csv': 'tenant_id          ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'id                 ', 'csv': 'id                 ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name        ', 'csv': 'region_name        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain', 'csv': 'availability_domain', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path   ', 'csv': 'compartment_path   ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name   ', 'csv': 'compartment_name   ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'display_name       ', 'csv': 'display_name       ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'size_gb            ', 'csv': 'size               ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'backup_policy      ', 'csv': 'backup_policy      ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vpus_per_gb        ', 'csv': 'vpus_per_gb        ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'volume_group_name  ', 'csv': 'volume_group_name  ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'instance_name      ', 'csv': 'instance_name      ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'instance_id        ', 'csv': 'instance_id        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'defined_tags       ', 'csv': 'defined_tags       ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags      ', 'csv': 'freeform_tags      ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'extract_date       ', 'csv': 'extract_date       ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, csv_location)
    except Exception as e:
        raise Exception("\nError at procedure: handle_block_storage - " + str(e))


##########################################################################
# Check Table Structure for Database All
##########################################################################
def handle_database_systems(connection, csv_location):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASE_SYSTEMS",
            'csv_file': "database_db_all.csv",
            'items': [
                {'col': 'tenant_name         ', 'csv': 'tenant_name         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id           ', 'csv': 'tenant_id           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'id                  ', 'csv': 'id                  ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name         ', 'csv': 'region_name         ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'availability_domain ', 'csv': 'availability_domain ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path    ', 'csv': 'compartment_path    ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name    ', 'csv': 'compartment_name    ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status              ', 'csv': 'status              ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                ', 'csv': 'type                ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'name                ', 'csv': 'name                ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'vm_name             ', 'csv': 'vm_name             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'shape               ', 'csv': 'shape               ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'gi_version          ', 'csv': 'gi_version          ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'gi_version_date     ', 'csv': 'gi_version_date     ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'system_version      ', 'csv': 'system_version      ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'system_version_date ', 'csv': 'system_version_date ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'database_edition    ', 'csv': 'database_edition    ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'license_model       ', 'csv': 'license_model       ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'data_subnet         ', 'csv': 'data_subnet         ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'backup_subnet       ', 'csv': 'backup_subnet       ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'scan_ips            ', 'csv': 'scan_ips            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'vip_ips             ', 'csv': 'vip_ips             ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'cluster_name        ', 'csv': 'cluster_name        ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'domain              ', 'csv': 'domain              ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'db_nodes            ', 'csv': 'db_nodes            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'db_homes            ', 'csv': 'db_homes            ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'maintenance_window  ', 'csv': 'maintenance_window  ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'last_maintenance_run', 'csv': 'last_maintenance_run', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'next_maintenance_run', 'csv': 'next_maintenance_run', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'infra_id            ', 'csv': 'infra_id            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'cpu_core_count      ', 'csv': 'cpu_core_count      ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'shape_ocpus         ', 'csv': 'shape_ocpus         ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'db_storage_gb       ', 'csv': 'db_storage_gb       ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'memory_gb           ', 'csv': 'memory_gb           ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'local_storage_tb    ', 'csv': 'local_storage_tb    ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'node_count          ', 'csv': 'node_count          ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'defined_tags        ', 'csv': 'defined_tags        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags       ', 'csv': 'freeform_tags       ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created        ', 'csv': 'time_created        ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date        ', 'csv': 'extract_date        ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, csv_location)
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_systems - " + str(e))


##########################################################################
# Check Table Structure for Databases
##########################################################################
def handle_database_autonomous(connection, csv_location):
    try:

        json = {
            'table_name': "OCI_SHOWOCI_DATABASES_ADB",
            'csv_file': "database_autonomous.csv",
            'items': [
                {'col': 'tenant_name            ', 'csv': 'tenant_name            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'tenant_id              ', 'csv': 'tenant_id              ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'id                     ', 'csv': 'id                     ', 'type': 'varchar2(1000)', 'pk': 'y'},
                {'col': 'region_name            ', 'csv': 'region_name            ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'compartment_path       ', 'csv': 'compartment_path       ', 'type': 'varchar2(2000)', 'pk': 'n'},
                {'col': 'compartment_name       ', 'csv': 'compartment_name       ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'status                 ', 'csv': 'status                 ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'type                   ', 'csv': 'type                   ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'name                   ', 'csv': 'name                   ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'infra_name             ', 'csv': 'infra_name             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'cluster_name           ', 'csv': 'cluster_name           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'container_name         ', 'csv': 'container_name         ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'db_version             ', 'csv': 'db_version             ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'db_name                ', 'csv': 'db_name                ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'version_license_model  ', 'csv': 'version_license_model  ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'data_safe_status       ', 'csv': 'data_safe_status       ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'time_maintenance_begin ', 'csv': 'time_maintenance_begin ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'time_maintenance_end   ', 'csv': 'time_maintenance_end   ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'subnet_id              ', 'csv': 'subnet_id              ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'subnet_name            ', 'csv': 'subnet_name            ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'private_endpoint       ', 'csv': 'private_endpoint       ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'private_endpoint_label ', 'csv': 'private_endpoint_label ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'nsg_ids                ', 'csv': 'nsg_ids                ', 'type': 'varchar2(1000)', 'pk': 'n'},
                {'col': 'nsg_names              ', 'csv': 'nsg_names              ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'whitelisted_ips        ', 'csv': 'whitelisted_ips        ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'service_console_url    ', 'csv': 'service_console_url    ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'connection_strings     ', 'csv': 'connection_strings     ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'is_auto_scaling_enabled', 'csv': 'is_auto_scaling_enabled', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'is_dedicated           ', 'csv': 'is_dedicated           ', 'type': 'varchar2(100) ', 'pk': 'n'},
                {'col': 'cpu_core_count         ', 'csv': 'cpu_core_count         ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'db_storage_tb          ', 'csv': 'db_storage_tb          ', 'type': 'number        ', 'pk': 'n'},
                {'col': 'defined_tags           ', 'csv': 'defined_tags           ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'freeform_tags          ', 'csv': 'freeform_tags          ', 'type': 'varchar2(4000)', 'pk': 'n'},
                {'col': 'time_created           ', 'csv': 'time_created           ', 'type': 'date          ', 'pk': 'n'},
                {'col': 'extract_date           ', 'csv': 'extract_date           ', 'type': 'date          ', 'pk': 'n'}
            ]
        }
        handle_table(connection, json, csv_location)
    except Exception as e:
        raise Exception("\nError at procedure: handle_database_autonomous - " + str(e))


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
def handle_table(connection, inputdata, csv_location):
    process_location = "Start"
    try:

        start_time = time.time()

        # Parameters
        csv_file = inputdata['csv_file']
        path_filename = csv_location + '_' + csv_file
        table_name = inputdata['table_name']
        tmp_table_name = table_name + "_TMP"
        compute_sql_columns = str(', '.join(x['col'] + " " + x['type'] for x in inputdata['items']))
        merge_sql_columns = str(', '.join("a." + x['col'] + " = b." + x['col'] for x in inputdata['items'] if x['pk'] != "y"))
        insert_def_sql_columns = str(', '.join(x['col'] for x in inputdata['items']))
        insert_val_sql_columns = str(', '.join("b." + x['col'] for x in inputdata['items']))
        primary_key = next((col for col in inputdata['items'] if col['pk'] == "y"), None)['col']
        insert_bulk_func = str(', '.join(variable_generation(x, index) for index, x in enumerate(inputdata['items'], start=1)))
        print("\nHandling " + csv_file)

        # Check if file exist
        if not os.path.isfile(path_filename):
            print("   file " + path_filename + " does not exist, skipping...")
            return

        ################################################
        # Check Table Structure and create if not exist
        ################################################
        process_location = "Checking Table Structure"

        # check if tables exist
        with connection.cursor() as cursor:

            sql = "select count(*) from user_tables where table_name = :table_name"
            cursor.execute(sql, table_name=table_name)
            val, = cursor.fetchone()

            # if main table not exist, create it
            if val == 0:
                print("   Table " + table_name + " was not exist, creating")
                sql = "create table " + table_name + " ( " + compute_sql_columns + " ,CONSTRAINT " + table_name + "_PK PRIMARY KEY (" + primary_key + ") USING INDEX) "
                cursor.execute(sql)
                print("   Table " + table_name + " created")
            else:
                print("   Table " + table_name + " exist")

            # check if temp table exist, if not create
            sql = "select count(*) from user_tables where table_name = :table_name"
            cursor.execute(sql, table_name=tmp_table_name)
            val, = cursor.fetchone()

            # if table not exist, create it
            if val == 0:
                print("   Table " + tmp_table_name + " was not exist, creating")
                sql = "create GLOBAL TEMPORARY TABLE " + tmp_table_name + " ( " + compute_sql_columns + " ) ON COMMIT PRESERVE ROWS "
                cursor.execute(sql)
                print("   Table " + tmp_table_name + " created")
            else:
                print("   Table " + tmp_table_name + " exist")

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

                print("   Completed file " + csv_file + " - " + str(num_rows) + " Rows Inserted")
                connection.commit()

        ################################################
        # Merge data from tmp to main table
        ################################################
        process_location = "before Merge"

        with connection.cursor() as cursor:

            print("   Merging data to main table...")

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
            print("   Merge Completed, " + str(cursor.rowcount) + " rows merged")

            print("   " + csv_file + " Completed " + get_time_elapsed(start_time))

    except oracledb.DatabaseError as e:
        print("\nDatabaseError at procedure: handle_table() - " + process_location + " - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError at Procedure: handle_table() - " + process_location + " - " + str(e))


##########################################################################
# Main
##########################################################################
def main_process():
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
        print("\nConnecting to database " + cmd.dname)
        with oracledb.connect(user=cmd.duser, password=cmd.dpass, dsn=cmd.dname, config_dir=cmd.wallet_location, wallet_location=cmd.wallet_location, wallet_password=cmd.wallet_password) as connection:

            print("   Connected")

            # Handling CSVs
            handle_compute(connection, cmd.csvlocation)
            handle_block_volume(connection, cmd.csvlocation)
            handle_database_systems(connection, cmd.csvlocation)
            handle_database_autonomous(connection, cmd.csvlocation)

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
