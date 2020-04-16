#!/usr/bin/env python3
##########################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# usage2adw.py
#
# @author: Adi Zohar
#
# Supports Python 3 and above
#
# coding: utf-8
##########################################################################
# OCI Usage to ADWC:
#
# Required OCI user part of UsageDownloadGroup with below permission:
#   define tenancy usage-report as ocid1.tenancy.oc1..aaaaaaaaned4fkpkisbwjlr56u7cj63lf3wffbilvqknstgtvzub7vhqkggq
#   endorse group UsageDownloadGroup to read objects in tenancy usage-report
#   Allow group UsageDownloadGroup to inspect compartments in tenancy
#   Allow group UsageDownloadGroup to inspect tenancies in tenancy
#
# config file should contain:
#     [TENANT_NAME]
#     user        = user_ocid
#     fingerprint = fingerprint of the api ssh key
#     key_file    = the path to the private key
#     tenancy     = tenancy ocid
#     region      = region
#
##########################################################################
# Database user:
#     create user usage identified by PaSsw0rd2#_#;
#     grant connect, resource, dwrole, unlimited tablespace to usage;
##########################################################################
#
# Modules Included:
# - oci.object_storage.ObjectStorageClient
# - oci.identity.IdentityClient
#
# APIs Used:
# - IdentityClient.list_compartments - Policy COMPARTMENT_INSPECT
# - IdentityClient.get_tenancy       - Policy TENANCY_INSPECT
# - ObjectStorageClient.list_objects - Policy OBJECT_INSPECT
# - ObjectStorageClient.get_object   - Policy OBJECT_READ
#
##########################################################################
import sys
import argparse
import datetime
import oci
import gzip
import os
import csv
import cx_Oracle

version = "20.4.13"
usage_report_namespace = "bling"
work_report_dir = os.curdir + "/work_report_dir"

# create the work dit if not exist
if not os.path.exists(work_report_dir):
    os.mkdir(work_report_dir)


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
# Create signer
##########################################################################
def create_signer(cmd):

    # assign default values
    config_file = oci.config.DEFAULT_LOCATION
    config_section = oci.config.DEFAULT_PROFILE
    signer = None
    config = None

    if cmd.config:
        if cmd.config.name:
            config_file = cmd.config.name

    if cmd.profile:
        config_section = cmd.profile

    if cmd.instance_principals:
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            config = {'region': signer.region, 'tenancy': signer.tenancy_id}
        except Exception:
            print_header("Error obtaining instance principals certificate, aborting", 0)
            raise SystemExit
    else:
        config = oci.config.from_file(config_file, config_section)
        signer = oci.signer.Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config.get("key_file"),
            pass_phrase=oci.config.get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content")
        )

    # return config and signer
    return config, signer


##########################################################################
# Load compartments
##########################################################################
def identity_read_compartments(identity, tenancy):

    compartments = []
    print("Loading Compartments...")

    try:
        # read all compartments to variable
        all_compartments = []
        try:
            all_compartments = oci.pagination.list_call_get_all_results(
                identity.list_compartments,
                tenancy.id,
                compartment_id_in_subtree=True
            ).data

        except oci.exceptions.ServiceError:
            raise

        ###################################################
        # Build Compartments - return nested compartment list
        ###################################################
        def build_compartments_nested(identity_client, cid, path):

            try:
                compartment_list = [item for item in all_compartments if str(item.compartment_id) == str(cid)]

                if path != "":
                    path = path + " / "

                for c in compartment_list:
                    if c.lifecycle_state == oci.identity.models.Compartment.LIFECYCLE_STATE_ACTIVE:
                        cvalue = {'id': str(c.id), 'name': str(c.name), 'path': path + str(c.name)}
                        compartments.append(cvalue)
                        build_compartments_nested(identity_client, c.id, cvalue['path'])

            except Exception as error:
                raise Exception("Error in build_compartments_nested: " + str(error.args))

        ###################################################
        # Add root compartment
        ###################################################
        value = {'id': str(tenancy.id), 'name': str(tenancy.name) + " (root)", 'path': "/ " + str(tenancy.name) + " (root)"}
        compartments.append(value)

        # Build the compartments
        build_compartments_nested(identity, str(tenancy.id), "")

        # sort the compartment
        sorted_compartments = sorted(compartments, key=lambda k: k['path'])
        print("    Total " + str(len(sorted_compartments)) + " compartments loaded.")
        return sorted_compartments

    except oci.exceptions.RequestException:
        raise
    except Exception as e:
        raise Exception("Error in identity_read_compartments: " + str(e.args))


##########################################################################
# set parser
##########################################################################
def set_parser_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', type=argparse.FileType('r'), dest='config', help="Config File")
    parser.add_argument('-t', default="", dest='profile', help='Config file section to use (tenancy profile)')
    parser.add_argument('-f', default="", dest='fileid', help='File Id to load')
    parser.add_argument('-d', default="", dest='filedate', help='Minimum File Date to load (i.e. yyyy-mm-dd)')
    parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
    parser.add_argument('-ip', action='store_true', default=False, dest='instance_principals', help='Use Instance Principals for Authentication')
    parser.add_argument('-du', default="", dest='duser', help='ADB User')
    parser.add_argument('-dp', default="", dest='dpass', help='ADB Password')
    parser.add_argument('-dn', default="", dest='dname', help='ADB Name')
    parser.add_argument('--version', action='version', version='%(prog)s ' + version)

    result = parser.parse_args()

    if not (result.duser and result.dpass and result.dname):
        parser.print_help()
        print_header("You must specify database credentials!!", 0)
        return None

    return result


##########################################################################
# Main
##########################################################################
cmd = set_parser_arguments()
if cmd is None:
    exit()
config, signer = create_signer(cmd)

############################################
# Start
############################################
start_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print_header("Running Usage Load to ADW", 0)
print("Starts at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
print("Command Line : " + ' '.join(x for x in sys.argv[1:]))

############################################
# Identity extract compartments
############################################
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
    print("App Version : " + version)
    print("")

    compartments = identity_read_compartments(identity, tenancy)

except Exception as e:
    print("\nError extracting compartments section - " + str(e) + "\n")
    raise SystemExit

############################################
# connect to database
############################################
max_file_id = ""
try:
    print("\nConnecting to database " + cmd.dname)
    con = cx_Oracle.connect(user=cmd.duser, password=cmd.dpass, dsn=cmd.dname)
    cur = con.cursor()

    # check if oci_usage table exist, if not create
    sql = "select count(*) from user_tables where table_name = 'OCI_USAGE'"
    cur.execute(sql)
    val, = cur.fetchone()

    # if table not exist, create it
    if val == 0:
        print("Table OCI_USAGE was not exist, creating")
        sql = "create table OCI_USAGE ("
        sql += "    TENANT_NAME             VARCHAR2(30),"
        sql += "    FILE_ID                 VARCHAR2(30),"
        sql += "    USAGE_INTERVAL_START    DATE,"
        sql += "    USAGE_INTERVAL_END      DATE,"
        sql += "    PRD_SERVICE             VARCHAR2(100),"
        sql += "    PRD_RESOURCE            VARCHAR2(100),"
        sql += "    PRD_COMPARTMENT_ID      VARCHAR2(100),"
        sql += "    PRD_COMPARTMENT_NAME    VARCHAR2(100),"
        sql += "    PRD_COMPARTMENT_PATH    VARCHAR2(1000),"
        sql += "    PRD_REGION              VARCHAR2(100),"
        sql += "    PRD_AVAILABILITY_DOMAIN VARCHAR2(100),"
        sql += "    USG_RESOURCE_ID         VARCHAR2(1000),"
        sql += "    USG_BILLED_QUANTITY     NUMBER,"
        sql += "    USG_CONSUMED_QUANTITY   NUMBER,"
        sql += "    USG_CONSUMED_UNITS      VARCHAR2(100),"
        sql += "    USG_CONSUMED_MEASURE    VARCHAR2(100),"
        sql += "    IS_CORRECTION           VARCHAR2(10),"
        sql += "    TAGS_KEYS               VARCHAR2(4000),"
        sql += "    TAGS_DATA               VARCHAR2(4000)"
        sql += ") COMPRESS"
        cur.execute(sql)
    else:
        print("Table OCI_USAGE Exist")

    # check if TAGS_KEYS and TAGS_DATA columns exist in OCI_USAGE table, if not create
    sql = "select count(*) from user_tab_columns where table_name = 'OCI_USAGE' and column_name='TAGS_KEYS'"
    cur.execute(sql)
    val, = cur.fetchone()

    # if columns not exist, create them
    if val == 0:
        print("Columns TAGS_KEYS and TAGS_DATA do not exist in the table OCI_USAGE, adding...")
        sql = "alter table OCI_USAGE add (TAGS_KEYS VARCHAR2(4000), TAGS_DATA VARCHAR2(4000))"
        cur.execute(sql)

    ###############################
    # fetch max file id processed
    ###############################
    sql = "select max(file_id) as file_id from OCI_USAGE where TENANT_NAME=:tenant_name"
    cur.execute(sql, {"tenant_name": str(tenancy.name)})
    max_file_id, = cur.fetchone()

    print("Max File Id Processed = " + str(max_file_id))

except cx_Oracle.DatabaseError as e:
    print("\nError manipulating database - " + str(e) + "\n")
    raise SystemExit

except Exception as e:
    raise Exception("\nError manipulating database - " + str(e))

############################################
# Download Usage and insert to database
############################################
try:
    num = 0
    print("\nConnecting to Object Storage Service...")

    object_storage = oci.object_storage.ObjectStorageClient(config, signer=signer)
    if cmd.proxy:
        object_storage.base_client.session.proxies = {'https': cmd.proxy}

    objects = object_storage.list_objects(usage_report_namespace, str(tenancy.id), fields="timeCreated,size").data
    for o in objects.objects:
        filename = o.name.rsplit('/', 1)[-1]
        file_id = filename[:-7]
        file_time = str(o.time_created)[0:16]

        # if file already loaded, skip (check if < max_file_id
        if str(max_file_id) != "None":
            if file_id <= str(max_file_id):
                continue

        # if file id enabled, check
        if cmd.fileid:
            if file_id != cmd.fileid:
                continue

        # check file date
        if cmd.filedate:
            if file_time <= cmd.filedate:
                continue

        path_filename = work_report_dir + '/' + filename
        path_filename_csv = path_filename[:-3]
        print("   Processing file " + o.name + " - " + str(o.size) + ", " + file_time)

        # check if file already loaded

        # download file
        object_details = object_storage.get_object(usage_report_namespace, str(tenancy.id), o.name)
        with open(path_filename, 'wb') as f:
            for chunk in object_details.data.raw.stream(1024 * 1024, decode_content=False):
                f.write(chunk)

        # Read file to variable
        with gzip.open(path_filename, 'rt') as file_in:
            csv_reader = csv.DictReader(file_in)

            data = []
            for row in csv_reader:

                # find compartment path
                compartment_path = ""
                for c in compartments:
                    if c['id'] == row['product/compartmentId']:
                        compartment_path = c['path']

                # Handle Tags up to 4000 chars with # seperator
                tags_keys = ""
                tags_data = ""
                for (key, value) in row.items():
                    if 'tags' in key and len(value) > 0:

                        # remove # and = from the tags keys and value
                        keyadj = str(key).replace("tags/", "").replace("#", "").replace("=", "")
                        valueadj = str(value).replace("#", "").replace("=", "")

                        # check if length < 4000 to avoid overflow database column
                        if len(tags_data) + len(keyadj) + len(valueadj) + 2 < 4000:
                            tags_keys += ("#" if tags_keys == "" else "") + keyadj + "#"
                            tags_data += ("#" if tags_data == "" else "") + keyadj + "=" + valueadj + "#"

                # create array for bulk insert
                row_data = (
                    str(tenancy.name),
                    file_id,
                    row['lineItem/intervalUsageStart'][0:10] + " " + row['lineItem/intervalUsageStart'][11:16],
                    row['lineItem/intervalUsageEnd'][0:10] + " " + row['lineItem/intervalUsageEnd'][11:16],
                    row['product/service'],
                    row['product/resource'],
                    row['product/compartmentId'],
                    row['product/compartmentName'],
                    compartment_path,
                    row['product/region'],
                    row['product/availabilityDomain'],
                    row['product/resourceId'],
                    row['usage/billedQuantity'],
                    row['usage/consumedQuantity'],
                    row['usage/consumedQuantityUnits'],
                    row['usage/consumedQuantityMeasure'],
                    row['lineItem/isCorrection'],
                    tags_keys,
                    tags_data
                )
                data.append(row_data)

            # insert bulk to database
            cursor = cx_Oracle.Cursor(con)
            sql = "INSERT INTO OCI_USAGE (TENANT_NAME , FILE_ID, USAGE_INTERVAL_START, USAGE_INTERVAL_END, PRD_SERVICE, PRD_RESOURCE, "
            sql += "PRD_COMPARTMENT_ID, PRD_COMPARTMENT_NAME, PRD_COMPARTMENT_PATH, PRD_REGION, PRD_AVAILABILITY_DOMAIN, USG_RESOURCE_ID, "
            sql += "USG_BILLED_QUANTITY, USG_CONSUMED_QUANTITY, USG_CONSUMED_UNITS, USG_CONSUMED_MEASURE, IS_CORRECTION, TAGS_KEYS, TAGS_DATA) "
            sql += "VALUES "
            sql += "( :1, :2, to_date(:3,'YYYY-MM-DD HH24:MI'), to_date(:4,'YYYY-MM-DD HH24:MI'), :5, :6, "
            sql += "  :7, :8, :9, :10, :11, :12, "
            sql += "  to_number(:13), to_number(:14), :15, :16, :17 ,:18 ,:19) "

            cursor.prepare(sql)
            cursor.executemany(None, data)
            con.commit()
            cursor.close()
            print("   Completed  file " + o.name + " - " + str(len(data)) + " Rows Inserted")

        num += 1

        # remove file
        os.remove(path_filename)

    print("Total Objects Processed = " + str(num))
    con.close()

except cx_Oracle.DatabaseError as e:
    print("\nError manipulating database - " + str(e) + "\n")

except Exception as e:
    print("\nError Download Usage and insert to database - " + str(e))

############################################
# print completed
############################################
print("\nCompleted at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
