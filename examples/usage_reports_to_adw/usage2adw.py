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
# - IdentityClient.list_compartments          - Policy COMPARTMENT_INSPECT
# - IdentityClient.get_tenancy                - Policy TENANCY_INSPECT
# - IdentityClient.list_region_subscriptions  - Policy TENANCY_INSPECT
# - ObjectStorageClient.list_objects          - Policy OBJECT_INSPECT
# - ObjectStorageClient.get_object            - Policy OBJECT_READ
#
# Meter API for Public Rate:
# - https://itra.oraclecloud.com/itas/.anon/myservices/api/v1/products?partNumber=XX
#
##########################################################################
# Tables used:
# - OCI_USAGE - Raw data of the usage reports
# - OCI_USAGE_STATS - Summary Stats of the Usage Report for quick query if only filtered by tenant and date
# - OCI_USAGE_TAG_KEYS - Tag keys of the usage reports
# - OCI_COST - Raw data of the cost reports
# - OCI_COST_STATS - Summary Stats of the Cost Report for quick query if only filtered by tenant and date
# - OCI_COST_TAG_KEYS - Tag keys of the cost reports
# - OCI_COST_REFERENCE - Reference table of the cost filter keys - SERVICE, REGION, COMPARTMENT, PRODUCT, SUBSCRIPTION
# - OCI_PRICE_LIST - Hold the price list and the cost per product
##########################################################################
import sys
import argparse
import datetime
import oci
import gzip
import os
import csv
import cx_Oracle
import requests


version = "20.07.07"
usage_report_namespace = "bling"
work_report_dir = os.curdir + "/work_report_dir"

# create the work dir if not exist
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
# Get Column from Array
##########################################################################
def get_column_value_from_array(column, array):
    if column in array:
        return array[column]
    else:
        return ""


##########################################################################
# Create signer
##########################################################################
def create_signer(cmd):

    # assign default values
    config_file = oci.config.DEFAULT_LOCATION
    config_section = oci.config.DEFAULT_PROFILE

    if cmd.config:
        if cmd.config.name:
            config_file = cmd.config.name

    if cmd.profile:
        config_section = cmd.profile

    if cmd.instance_principals:
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            config = {'region': signer.region, 'tenancy': signer.tenancy_id}
            return config, signer
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
    parser.add_argument('-su', action='store_true', default=False, dest='skip_usage', help='Skip Load Usage Files')
    parser.add_argument('-sc', action='store_true', default=False, dest='skip_cost', help='Skip Load Cost Files')
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
# Check Table Structure for usage
##########################################################################
def check_database_table_structure_usage(connection):
    try:
        # open cursor
        cursor = connection.cursor()

        # check if OCI_USAGE table exist, if not create
        sql = "select count(*) from user_tables where table_name = 'OCI_USAGE'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if table not exist, create it
        if val == 0:
            print("   Table OCI_USAGE was not exist, creating")
            sql = "create table OCI_USAGE ("
            sql += "    TENANT_NAME             VARCHAR2(100),"
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
            sql += "    TAGS_DATA               VARCHAR2(4000)"
            sql += ") COMPRESS"
            cursor.execute(sql)
            print("   Table OCI_USAGE created")
        else:
            print("   Table OCI_USAGE exist")

        # check if TAGS_DATA columns exist in OCI_USAGE table, if not create
        sql = "select count(*) from user_tab_columns where table_name = 'OCI_USAGE' and column_name='TAGS_DATA'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if columns not exist, create them
        if val == 0:
            print("   Column TAGS_DATA does not exist in the table OCI_USAGE, adding...")
            sql = "alter table OCI_USAGE add (TAGS_DATA VARCHAR2(4000))"
            cursor.execute(sql)

        # check if OCI_USAGE_TAG_KEYS table exist, if not create
        sql = "select count(*) from user_tables where table_name = 'OCI_USAGE_TAG_KEYS'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if table not exist, create it
        if val == 0:
            print("   Table OCI_USAGE_TAG_KEYS was not exist, creating")
            sql = "CREATE TABLE OCI_USAGE_TAG_KEYS (TENANT_NAME VARCHAR2(100), TAG_KEY VARCHAR2(100), "
            sql += "CONSTRAINT OCI_USAGE_TAG_KEYS_PK PRIMARY KEY(TENANT_NAME,TAG_KEY)"
            sql += ")"
            cursor.execute(sql)
            print("   Table OCI_USAGE_TAG_KEYS created")
        else:
            print("   Table OCI_USAGE_TAG_KEYS exist")

        # check if OCI_USAGE_STATS table exist, if not create
        sql = "select count(*) from user_tables where table_name = 'OCI_USAGE_STATS'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if table not exist, create it
        if val == 0:
            print("   Table OCI_USAGE_STATS was not exist, creating")
            sql = "CREATE TABLE OCI_USAGE_STATS ( "
            sql += "    TENANT_NAME             VARCHAR2(100),"
            sql += "    FILE_ID                 VARCHAR2(30),"
            sql += "    USAGE_INTERVAL_START    DATE,"
            sql += "    NUM_ROWS                NUMBER,"
            sql += "    UPDATE_DATE             DATE,"
            sql += "    AGENT_VERSION           VARCHAR2(30),"
            sql += "    CONSTRAINT OCI_USAGE_STATS_PK PRIMARY KEY (TENANT_NAME,FILE_ID,USAGE_INTERVAL_START)"
            sql += ")"
            cursor.execute(sql)
            print("   Table OCI_USAGE_STATS created")

            update_usage_stats(connection)
        else:
            print("   Table OCI_USAGE_STATS exist")

        # close cursor
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at check_database_table_structure_usage() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at check_database_table_structure_usage() - " + str(e))


##########################################################################
# Check Index Structure Usage to be created after the first load
##########################################################################
def check_database_index_structure_usage(connection):
    try:
        # open cursor
        cursor = connection.cursor()

        # check if index OCI_USAGE_1IX exist in OCI_USAGE table, if not create
        sql = "select count(*) from user_indexes where table_name = 'OCI_USAGE' and index_name='OCI_USAGE_1IX'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if index not exist, create it
        if val == 0:
            print("\nChecking Index for OCI_USAGE")
            print("   Index OCI_USAGE_1IX does not exist for table OCI_USAGE, adding...")
            sql = "CREATE INDEX OCI_USAGE_1IX ON OCI_USAGE(TENANT_NAME,USAGE_INTERVAL_START)"
            cursor.execute(sql)
            print("   Index created.")

        # close cursor
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at check_database_index_structure_usage() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at check_database_index_structure_usage() - " + str(e))


##########################################################################
# Check Index Structure Usage to be created after the first load
##########################################################################
def check_database_index_structure_cost(connection):
    try:
        # open cursor
        cursor = connection.cursor()

        # check if index OCI_USAGE_1IX exist in OCI_USAGE table, if not create
        sql = "select count(*) from user_indexes where table_name = 'OCI_COST' and index_name='OCI_COST_1IX'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if index not exist, create it
        if val == 0:
            print("\nChecking Index for OCI_COST")
            print("   Index OCI_COST_1IX does not exist for table OCI_COST, adding...")
            sql = "CREATE INDEX OCI_COST_1IX ON OCI_COST(TENANT_NAME,USAGE_INTERVAL_START)"
            cursor.execute(sql)
            print("   Index created.")

        # close cursor
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at check_database_index_structure_cost() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at check_database_index_structure_cost() - " + str(e))


##########################################################################
# update_cost_stats
##########################################################################
def update_cost_stats(connection):
    try:
        # open cursor
        cursor = connection.cursor()

        print("\nMerging statistics into OCI_COST_STATS...")

        # run merge to oci_update_stats
        sql = "merge into OCI_COST_STATS a "
        sql += "using "
        sql += "( "
        sql += "    select  "
        sql += "        tenant_name, "
        sql += "        file_id, "
        sql += "        USAGE_INTERVAL_START, "
        sql += "        sum(COST_MY_COST) COST_MY_COST, "
        sql += "        sum(COST_MY_COST_OVERAGE) COST_MY_COST_OVERAGE, "
        sql += "        min(COST_CURRENCY_CODE) COST_CURRENCY_CODE, "
        sql += "        count(*) NUM_ROWS "
        sql += "    from  "
        sql += "        oci_cost "
        sql += "    group by  "
        sql += "        tenant_name, "
        sql += "        file_id, "
        sql += "        USAGE_INTERVAL_START "
        sql += ") b "
        sql += "on (a.tenant_name=b.tenant_name and a.file_id=b.file_id and a.USAGE_INTERVAL_START=b.USAGE_INTERVAL_START) "
        sql += "when matched then update set a.num_rows=b.num_rows, a.COST_MY_COST=b.COST_MY_COST, a.UPDATE_DATE=sysdate, a.AGENT_VERSION=:version,"
        sql += "    a.COST_MY_COST_OVERAGE=b.COST_MY_COST_OVERAGE, a.COST_CURRENCY_CODE=b.COST_CURRENCY_CODE "
        sql += "where a.num_rows <> b.num_rows "
        sql += "when not matched then insert (TENANT_NAME,FILE_ID,USAGE_INTERVAL_START,NUM_ROWS,COST_MY_COST,UPDATE_DATE,AGENT_VERSION,COST_MY_COST_OVERAGE,COST_CURRENCY_CODE)  "
        sql += "   values (b.TENANT_NAME,b.FILE_ID,b.USAGE_INTERVAL_START,b.NUM_ROWS,b.COST_MY_COST,sysdate,:version,b.COST_MY_COST_OVERAGE,b.COST_CURRENCY_CODE) "

        cursor.execute(sql, {"version": version})
        connection.commit()
        print("   Merge Completed, " + str(cursor.rowcount) + " rows merged")
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at update_cost_stats() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at update_cost_stats() - " + str(e))


##########################################################################
# update_price_list
##########################################################################
def update_price_list(connection):
    try:
        # open cursor
        cursor = connection.cursor()

        print("\nMerging statistics into OCI_PRICE_LIST...")

        # run merge to oci_update_stats
        sql = "MERGE INTO OCI_PRICE_LIST A "
        sql += "USING "
        sql += "( "
        sql += "    SELECT "
        sql += "        TENANT_NAME, "
        sql += "        COST_PRODUCT_SKU, "
        sql += "        PRD_DESCRIPTION, "
        sql += "        COST_CURRENCY_CODE, "
        sql += "        COST_UNIT_PRICE "
        sql += "    FROM "
        sql += "    ( "
        sql += "        SELECT  "
        sql += "            TENANT_NAME, "
        sql += "            COST_PRODUCT_SKU, "
        sql += "            PRD_DESCRIPTION, "
        sql += "            COST_CURRENCY_CODE, "
        sql += "            COST_UNIT_PRICE, "
        sql += "            ROW_NUMBER() OVER (PARTITION BY TENANT_NAME, COST_PRODUCT_SKU ORDER BY USAGE_INTERVAL_START DESC, COST_UNIT_PRICE DESC) RN "
        sql += "        FROM OCI_COST A  "
        sql += "    )     "
        sql += "    WHERE RN = 1 "
        sql += "    ORDER BY 1,2 "
        sql += ") B "
        sql += "ON (A.TENANT_NAME = B.TENANT_NAME AND A.COST_PRODUCT_SKU = B.COST_PRODUCT_SKU) "
        sql += "WHEN MATCHED THEN UPDATE SET A.PRD_DESCRIPTION=B.PRD_DESCRIPTION, A.COST_CURRENCY_CODE=B.COST_CURRENCY_CODE, A.COST_UNIT_PRICE=B.COST_UNIT_PRICE, COST_LAST_UPDATE = SYSDATE "
        sql += "WHEN NOT MATCHED THEN INSERT (TENANT_NAME,COST_PRODUCT_SKU,PRD_DESCRIPTION,COST_CURRENCY_CODE,COST_UNIT_PRICE,COST_LAST_UPDATE)  "
        sql += "  VALUES (B.TENANT_NAME,B.COST_PRODUCT_SKU,B.PRD_DESCRIPTION,B.COST_CURRENCY_CODE,B.COST_UNIT_PRICE,SYSDATE)"

        cursor.execute(sql)
        connection.commit()
        print("   Merge Completed, " + str(cursor.rowcount) + " rows merged")
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at update_price_list() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at update_price_list() - " + str(e))


##########################################################################
# update_cost_reference
##########################################################################
def update_cost_reference(connection):
    try:
        # open cursor
        cursor = connection.cursor()

        print("\nMerging statistics into OCI_COST_REFERENCE...")

        # run merge to oci_update_stats
        sql = "merge into OCI_COST_REFERENCE a "
        sql += "using "
        sql += "( "
        sql += "    select TENANT_NAME, REF_TYPE, REF_NAME "
        sql += "    from "
        sql += "    ( "
        sql += "        select distinct TENANT_NAME, 'PRD_SERVICE' as REF_TYPE, PRD_SERVICE as REF_NAME from OCI_COST "
        sql += "        union all "
        sql += "        select distinct TENANT_NAME, 'PRD_COMPARTMENT_PATH' as REF_TYPE,  "
        sql += "            case when prd_compartment_path like '%/%' then substr(prd_compartment_path,1,instr(prd_compartment_path,' /')-1)  "
        sql += "            else prd_compartment_path end as REF_NAME  "
        sql += "            from OCI_COST "
        sql += "        union all "
        sql += "        select distinct TENANT_NAME, 'PRD_COMPARTMENT_NAME' as REF_TYPE, PRD_COMPARTMENT_NAME as ref_name from OCI_COST "
        sql += "        union all "
        sql += "        select distinct TENANT_NAME, 'PRD_REGION' as REF_TYPE, PRD_REGION as ref_name from OCI_COST "
        sql += "        union all "
        sql += "        select distinct TENANT_NAME, 'COST_SUBSCRIPTION_ID' as REF_TYPE, to_char(COST_SUBSCRIPTION_ID) as ref_name from OCI_COST "
        sql += "        union all "
        sql += "        select distinct TENANT_NAME, 'COST_PRODUCT_SKU' as REF_TYPE, COST_PRODUCT_SKU || ' '||min(PRD_DESCRIPTION) as ref_name from OCI_COST  "
        sql += "        group by TENANT_NAME, COST_PRODUCT_SKU "
        sql += "    ) where ref_name is not null "
        sql += ") b "
        sql += "on (a.TENANT_NAME=b.TENANT_NAME and a.REF_TYPE=b.REF_TYPE and a.REF_NAME=b.REF_NAME) "
        sql += "when not matched then insert (TENANT_NAME,REF_TYPE,REF_NAME)  "
        sql += "values (b.TENANT_NAME,b.REF_TYPE,b.REF_NAME)"

        cursor.execute(sql)
        connection.commit()
        print("   Merge Completed, " + str(cursor.rowcount) + " rows merged")
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at update_cost_reference() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at update_cost_reference() - " + str(e))


##########################################################################
# update_public_rates
##########################################################################
def update_public_rates(connection, tenant_name):
    try:
        # open cursor
        num_rows = 0
        cursor = connection.cursor()
        api_url = "https://itra.oraclecloud.com/itas/.anon/myservices/api/v1/products?partNumber="

        print("\nMerging Public Rates into OCI_RATE_CARD...")

        # retrieve the SKUS to query
        sql = "select COST_PRODUCT_SKU, COST_CURRENCY_CODE from OCI_PRICE_LIST where tenant_name=:tenant_name"

        cursor.execute(sql, {"tenant_name": tenant_name})
        rows = cursor.fetchall()

        if rows:
            for row in rows:

                rate_description = ""
                rate_paygo_price = None
                rate_monthly_flex_price = None

                # Call API to fetch the data
                cost_produdt_sku = str(row[0])
                country_code = str(row[1])
                resp = requests.get(api_url + cost_produdt_sku, headers={'X-Oracle-Accept-CurrencyCode': country_code})

                if not resp:
                    continue

                for item in resp.json()['items']:
                    rate_description = item["displayName"]
                    for price in item['prices']:
                        if price['model'] == 'PAY_AS_YOU_GO':
                            rate_paygo_price = price['value']
                        elif price['model'] == 'MONTHLY_COMMIT':
                            rate_monthly_flex_price = price['value']

                # update database
                sql = "update OCI_PRICE_LIST set "
                sql += "RATE_DESCRIPTION=:rate_description, "
                sql += "RATE_PAYGO_PRICE=:rate_paygo, "
                sql += "RATE_MONTHLY_FLEX_PRICE=:rate_monthly, "
                sql += "RATE_UPDATE_DATE=sysdate "
                sql += "where TENANT_NAME=:tenant_name and COST_PRODUCT_SKU=:cost_produdt_sku "

                sql_variables = {
                    "rate_description": rate_description,
                    "rate_paygo": rate_paygo_price,
                    "rate_monthly": rate_monthly_flex_price,
                    "tenant_name": tenant_name,
                    "cost_produdt_sku": cost_produdt_sku
                }

                cursor.execute(sql, sql_variables)
                num_rows += 1

            # Commit
            connection.commit()

        print("   Update Completed, " + str(num_rows) + " rows updated.")
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at update_public_rates() - " + str(e) + "\n")
        raise SystemExit

    except requests.exceptions.ConnectionError as e:
        print("\nError connecting to billing metering API at update_public_rates() - " + str(e))

    except Exception as e:
        raise Exception("\nError manipulating database at update_public_rates() - " + str(e))


##########################################################################
# update_usage_stats
##########################################################################
def update_usage_stats(connection):
    try:
        # open cursor
        cursor = connection.cursor()

        print("\nMerging statistics into OCI_USAGE_STATS...")

        # run merge to oci_update_stats
        sql = "merge into OCI_USAGE_STATS a "
        sql += "using "
        sql += "( "
        sql += "    select  "
        sql += "        tenant_name, "
        sql += "        file_id, "
        sql += "        USAGE_INTERVAL_START, "
        sql += "        count(*) NUM_ROWS "
        sql += "    from  "
        sql += "        oci_usage "
        sql += "    group by  "
        sql += "        tenant_name, "
        sql += "        file_id, "
        sql += "        USAGE_INTERVAL_START "
        sql += ") b "
        sql += "on (a.tenant_name=b.tenant_name and a.file_id=b.file_id and a.USAGE_INTERVAL_START=b.USAGE_INTERVAL_START) "
        sql += "when matched then update set a.num_rows=b.num_rows, a.UPDATE_DATE=sysdate, a.AGENT_VERSION=:version "
        sql += "where a.num_rows <> b.num_rows "
        sql += "when not matched then insert (TENANT_NAME,FILE_ID,USAGE_INTERVAL_START,NUM_ROWS,UPDATE_DATE,AGENT_VERSION)  "
        sql += "   values (b.TENANT_NAME,b.FILE_ID,b.USAGE_INTERVAL_START,b.NUM_ROWS,sysdate,:version) "

        cursor.execute(sql, {"version": version})
        connection.commit()
        print("   Merge Completed, " + str(cursor.rowcount) + " rows merged")
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at update_usage_stats() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at update_usage_stats() - " + str(e))


##########################################################################
# Check Table Structure Cost
##########################################################################
def check_database_table_structure_cost(connection):
    try:
        # open cursor
        cursor = connection.cursor()

        # check if OCI_COST table exist, if not create
        sql = "select count(*) from user_tables where table_name = 'OCI_COST'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if table not exist, create it
        if val == 0:
            print("   Table OCI_COST was not exist, creating")
            sql = "create table OCI_COST ("
            sql += "    TENANT_NAME             VARCHAR2(100),"
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
            sql += "    USG_BILLED_QUANTITY_OVERAGE NUMBER,"
            sql += "    COST_SUBSCRIPTION_ID    NUMBER,"
            sql += "    COST_PRODUCT_SKU        VARCHAR2(10),"
            sql += "    PRD_DESCRIPTION         VARCHAR2(1000),"
            sql += "    COST_UNIT_PRICE         NUMBER,"
            sql += "    COST_UNIT_PRICE_OVERAGE NUMBER,"
            sql += "    COST_MY_COST            NUMBER,"
            sql += "    COST_MY_COST_OVERAGE    NUMBER,"
            sql += "    COST_CURRENCY_CODE      VARCHAR2(10),"
            sql += "    COST_BILLING_UNIT       VARCHAR2(1000),"
            sql += "    COST_OVERAGE_FLAG       VARCHAR2(10),"
            sql += "    IS_CORRECTION           VARCHAR2(10),"
            sql += "    TAGS_DATA               VARCHAR2(4000)"
            sql += ") COMPRESS"
            cursor.execute(sql)
            print("   Table OCI_COST created")
        else:
            print("   Table OCI_COST exist")

        # check if OCI_COST_TAG_KEYS table exist, if not create
        sql = "select count(*) from user_tables where table_name = 'OCI_COST_TAG_KEYS'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if table not exist, create it
        if val == 0:
            print("   Table OCI_COST_TAG_KEYS was not exist, creating")
            sql = "CREATE TABLE OCI_COST_TAG_KEYS (TENANT_NAME VARCHAR2(100), TAG_KEY VARCHAR2(100), "
            sql += "CONSTRAINT OCI_COST_TAG_KEYS_PK PRIMARY KEY(TENANT_NAME,TAG_KEY)"
            sql += ")"
            cursor.execute(sql)
            print("   Table OCI_COST_TAG_KEYS created")
        else:
            print("   Table OCI_COST_TAG_KEYS exist")

        # check if OCI_COST_STATS table exist, if not create
        sql = "select count(*) from user_tables where table_name = 'OCI_COST_STATS'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if table not exist, create it
        if val == 0:
            print("   Table OCI_COST_STATS was not exist, creating")
            sql = "CREATE TABLE OCI_COST_STATS ( "
            sql += "    TENANT_NAME             VARCHAR2(100),"
            sql += "    FILE_ID                 VARCHAR2(30),"
            sql += "    USAGE_INTERVAL_START    DATE,"
            sql += "    NUM_ROWS                NUMBER,"
            sql += "    COST_MY_COST            NUMBER,"
            sql += "    COST_MY_COST_OVERAGE    NUMBER,"
            sql += "    COST_CURRENCY_CODE      VARCHAR2(30),"
            sql += "    UPDATE_DATE             DATE,"
            sql += "    AGENT_VERSION           VARCHAR2(30),"
            sql += "    CONSTRAINT OCI_COST_STATS_PK PRIMARY KEY (TENANT_NAME,FILE_ID,USAGE_INTERVAL_START)"
            sql += ")"
            cursor.execute(sql)
            print("   Table OCI_COST_STATS created")

            update_cost_stats(connection)
        else:
            print("   Table OCI_COST_STATS exist")

        # check if COST_MY_COST_OVERAGE columns exist in OCI_COST_STATS table, if not create
        sql = "select count(*) from user_tab_columns where table_name = 'OCI_COST_STATS' and column_name='COST_MY_COST_OVERAGE'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if columns not exist, create them
        if val == 0:
            print("   Column COST_MY_COST_OVERAGE does not exist in the table OCI_COST_STATS, adding...")
            sql = "alter table OCI_COST_STATS add (COST_MY_COST_OVERAGE NUMBER, COST_CURRENCY_CODE VARCHAR2(10))"
            cursor.execute(sql)
            update_cost_stats(connection)

        # check if OCI_COST_REFERENCE table exist, if not create
        sql = "select count(*) from user_tables where table_name = 'OCI_COST_REFERENCE'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if table not exist, create it
        if val == 0:
            print("   Table OCI_COST_REFERENCE was not exist, creating")
            sql = "CREATE TABLE OCI_COST_REFERENCE ("
            sql += "    TENANT_NAME             VARCHAR2(100),"
            sql += "    REF_TYPE                VARCHAR2(100),"
            sql += "    REF_NAME                VARCHAR2(1000),"
            sql += "    CONSTRAINT OCI_REFERENCE_PK PRIMARY KEY (TENANT_NAME,REF_TYPE,REF_NAME) "
            sql += ") "
            cursor.execute(sql)
            print("   Table OCI_COST_REFERENCE created")

            update_cost_reference(connection)
        else:
            print("   Table OCI_COST_REFERENCE exist")

        # close cursor
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at check_database_table_structure_cost() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at check_database_table_structure_cost() - " + str(e))


##########################################################################
# Check Table Structure Price List
##########################################################################
def check_database_table_structure_price_list(connection, tenant_name):
    try:
        # open cursor
        cursor = connection.cursor()

        # check if OCI_PRICE_LIST table exist, if not create
        sql = "select count(*) from user_tables where table_name = 'OCI_PRICE_LIST'"
        cursor.execute(sql)
        val, = cursor.fetchone()

        # if table not exist, create it
        if val == 0:
            print("   Table OCI_PRICE_LIST was not exist, creating")
            sql = "create table OCI_PRICE_LIST ("
            sql += "    TENANT_NAME             VARCHAR2(100),"
            sql += "    COST_PRODUCT_SKU        VARCHAR2(10),"
            sql += "    PRD_DESCRIPTION         VARCHAR2(1000),"
            sql += "    COST_CURRENCY_CODE      VARCHAR2(10),"
            sql += "    COST_UNIT_PRICE         NUMBER,"
            sql += "    COST_LAST_UPDATE        DATE,"
            sql += "    RATE_DESCRIPTION        VARCHAR2(1000),"
            sql += "    RATE_PAYGO_PRICE        NUMBER,"
            sql += "    RATE_MONTHLY_FLEX_PRICE NUMBER,"
            sql += "    RATE_UPDATE_DATE        DATE,"
            sql += "    CONSTRAINT OCI_PRICE_LIST_PK PRIMARY KEY (TENANT_NAME,COST_PRODUCT_SKU) "
            sql += ") "
            cursor.execute(sql)
            print("   Table OCI_PRICE_LIST created")
            update_price_list(connection)
            update_public_rates(connection, tenant_name)
        else:
            print("   Table OCI_PRICE_LIST exist")

        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database at check_database_table_price_list() - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database at check_database_table_price_list() - " + str(e))


#########################################################################
# Load Cost File
##########################################################################
def load_cost_file(connection, object_storage, object_file, max_file_id, cmd, tenancy, compartments):
    num_files = 0
    num_rows = 0

    try:
        o = object_file

        # keep tag keys per file
        tags_keys = []

        # get file name
        filename = o.name.rsplit('/', 1)[-1]
        file_id = filename[:-7]
        file_time = str(o.time_created)[0:16]

        # if file already loaded, skip (check if < max_file_id
        if str(max_file_id) != "None":
            if file_id <= str(max_file_id):
                return num_files

        # if file id enabled, check
        if cmd.fileid:
            if file_id != cmd.fileid:
                return num_files

        # check file date
        if cmd.filedate:
            if file_time <= cmd.filedate:
                return num_files

        path_filename = work_report_dir + '/' + filename
        print("   Processing file " + o.name + " - " + str(o.size) + " bytes, " + file_time)

        # download file
        object_details = object_storage.get_object(usage_report_namespace, str(tenancy.id), o.name)
        with open(path_filename, 'wb') as f:
            for chunk in object_details.data.raw.stream(1024 * 1024, decode_content=False):
                f.write(chunk)

        # Read file to variable
        with gzip.open(path_filename, 'rt') as file_in:
            csv_reader = csv.DictReader(file_in)

            # Adjust the batch size to meet memory and performance requirements for cx_oracle
            batch_size = 5000
            array_size = 1000

            sql = "INSERT INTO OCI_COST ("
            sql += "TENANT_NAME,"
            sql += "FILE_ID,"
            sql += "USAGE_INTERVAL_START, "
            sql += "USAGE_INTERVAL_END, "
            sql += "PRD_SERVICE, "
            # 6
            sql += "PRD_COMPARTMENT_ID, "
            sql += "PRD_COMPARTMENT_NAME, "
            sql += "PRD_COMPARTMENT_PATH, "
            sql += "PRD_REGION, "
            sql += "PRD_AVAILABILITY_DOMAIN, "
            # 11
            sql += "USG_RESOURCE_ID, "
            sql += "USG_BILLED_QUANTITY, "
            sql += "USG_BILLED_QUANTITY_OVERAGE, "
            sql += "COST_SUBSCRIPTION_ID, "
            sql += "COST_PRODUCT_SKU, "
            # 16
            sql += "PRD_DESCRIPTION, "
            sql += "COST_UNIT_PRICE, "
            sql += "COST_UNIT_PRICE_OVERAGE, "
            sql += "COST_MY_COST, "
            sql += "COST_MY_COST_OVERAGE, "
            # 21
            sql += "COST_CURRENCY_CODE, "
            sql += "COST_BILLING_UNIT, "
            sql += "COST_OVERAGE_FLAG,"
            sql += "IS_CORRECTION, "
            sql += "TAGS_DATA "
            sql += ") VALUES ("
            sql += ":1, :2, to_date(:3,'YYYY-MM-DD HH24:MI'), to_date(:4,'YYYY-MM-DD HH24:MI'), :5,  "
            sql += ":6, :7, :8, :9, :10, "
            sql += ":11, to_number(:12), to_number(:13) ,:14, :15, "
            sql += ":16, to_number(:17), to_number(:18), to_number(:19), to_number(:20), "
            sql += ":21, :22, :23, :24, :25"
            sql += ") "

            # insert bulk to database
            cursor = cx_Oracle.Cursor(connection)

            # Predefine the memory areas to match the table definition
            cursor.setinputsizes(None, array_size)

            data = []
            for row in csv_reader:

                # find compartment path
                compartment_path = ""
                for c in compartments:
                    if c['id'] == row['product/compartmentId']:
                        compartment_path = c['path']

                # Handle Tags up to 4000 chars with # seperator
                tags_data = ""
                for (key, value) in row.items():
                    if 'tags' in key and len(value) > 0:

                        # remove # and = from the tags keys and value
                        keyadj = str(key).replace("tags/", "").replace("#", "").replace("=", "")
                        valueadj = str(value).replace("#", "").replace("=", "")

                        # check if length < 4000 to avoid overflow database column
                        if len(tags_data) + len(keyadj) + len(valueadj) + 2 < 4000:
                            tags_data += ("#" if tags_data == "" else "") + keyadj + "=" + valueadj + "#"

                        # add tag key to tag_keys array
                            if keyadj not in tags_keys:
                                tags_keys.append(keyadj)

                # Assign each column to variable to avoid error if column missing from the file
                lineItem_intervalUsageStart = get_column_value_from_array('lineItem/intervalUsageStart', row)
                lineItem_intervalUsageEnd = get_column_value_from_array('lineItem/intervalUsageEnd', row)
                product_service = get_column_value_from_array('product/service', row)
                product_compartmentId = get_column_value_from_array('product/compartmentId', row)
                product_compartmentName = get_column_value_from_array('product/compartmentName', row)
                product_region = get_column_value_from_array('product/region', row)
                product_availabilityDomain = get_column_value_from_array('product/availabilityDomain', row)
                product_resourceId = get_column_value_from_array('product/resourceId', row)
                usage_billedQuantity = get_column_value_from_array('usage/billedQuantity', row)
                usage_billedQuantityOverage = get_column_value_from_array('usage/billedQuantityOverage', row)
                cost_subscriptionId = get_column_value_from_array('cost/subscriptionId', row)
                cost_productSku = get_column_value_from_array('cost/productSku', row)
                product_Description = get_column_value_from_array('product/Description', row)
                cost_unitPrice = get_column_value_from_array('cost/unitPrice', row)
                cost_unitPriceOverage = get_column_value_from_array('cost/unitPriceOverage', row)
                cost_myCost = get_column_value_from_array('cost/myCost', row)
                cost_myCostOverage = get_column_value_from_array('cost/myCostOverage', row)
                cost_currencyCode = get_column_value_from_array('cost/currencyCode', row)
                cost_overageFlag = get_column_value_from_array('cost/overageFlag', row)
                lineItem_isCorrection = get_column_value_from_array('lineItem/isCorrection', row)

                # OCI changed the column billingUnitReadable to skuUnitDescription
                if 'cost/skuUnitDescription' in row:
                    cost_billingUnitReadable = get_column_value_from_array('cost/skuUnitDescription', row)
                else:
                    cost_billingUnitReadable = get_column_value_from_array('cost/billingUnitReadable', row)

                # Fix OCI Data for missing product description
                if cost_productSku == "B88285" and product_Description == "":
                    product_Description = "Object Storage Classic"
                    cost_billingUnitReadable = "Gigabyte Storage Capacity per Month"

                elif cost_productSku == "B88272" and product_Description == "":
                    product_Description = "Compute Classic - Unassociated Static IP"
                    cost_billingUnitReadable = "IPs"

                elif cost_productSku == "B88166" and product_Description == "":
                    product_Description = "Oracle Identity Cloud - Standard"
                    cost_billingUnitReadable = "Active User per Hour"

                elif cost_productSku == "B88167" and product_Description == "":
                    product_Description = "Oracle Identity Cloud - Basic"
                    cost_billingUnitReadable = "Active User per Hour"

                elif cost_productSku == "B88168" and product_Description == "":
                    product_Description = "Oracle Identity Cloud - Basic - Consumer User"
                    cost_billingUnitReadable = "Active User per Hour"

                elif cost_productSku == "B88274" and product_Description == "":
                    product_Description = "Block Storage Classic"
                    cost_billingUnitReadable = "Gigabyte Storage Capacity per Month"

                elif cost_productSku == "B89164" and product_Description == "":
                    product_Description = "Oracle Security Monitoring and Compliance Edition"
                    cost_billingUnitReadable = "100 Entities Per Hour"

                elif cost_productSku == "B88269" and product_Description == "":
                    product_Description = "Compute Classic"
                    cost_billingUnitReadable = "OCPU Per Hour "

                elif cost_productSku == "B88269" and product_Description == "":
                    product_Description = "Compute Classic"
                    cost_billingUnitReadable = "OCPU Per Hour"

                elif cost_productSku == "B88275" and product_Description == "":
                    product_Description = "Block Storage Classic - High I/O"
                    cost_billingUnitReadable = "Gigabyte Storage Per Month"

                elif cost_productSku == "B88283" and product_Description == "":
                    product_Description = "Object Storage Classic - GET and all other Requests"
                    cost_billingUnitReadable = "10,000 Requests Per Month"

                elif cost_productSku == "B88284" and product_Description == "":
                    product_Description = "Object Storage Classic - PUT, COPY, POST or LIST Requests"
                    cost_billingUnitReadable = "10,000 Requests Per Month"

                # create array
                row_data = (
                    str(tenancy.name),
                    file_id,
                    lineItem_intervalUsageStart[0:10] + " " + lineItem_intervalUsageStart[11:16],
                    lineItem_intervalUsageEnd[0:10] + " " + lineItem_intervalUsageEnd[11:16],
                    product_service,
                    product_compartmentId,
                    product_compartmentName,
                    compartment_path,
                    product_region,
                    product_availabilityDomain,
                    product_resourceId,
                    usage_billedQuantity,
                    usage_billedQuantityOverage,
                    cost_subscriptionId,
                    cost_productSku,
                    product_Description,
                    cost_unitPrice,
                    cost_unitPriceOverage,
                    cost_myCost,
                    cost_myCostOverage,
                    cost_currencyCode,
                    cost_billingUnitReadable,
                    cost_overageFlag,
                    lineItem_isCorrection,
                    tags_data
                )
                data.append(row_data)
                num_rows += 1

                # executemany every batch size
                if len(data) % batch_size == 0:
                    cursor.executemany(sql, data)
                    data = []

            # if data exist final execute
            if data:
                cursor.executemany(sql, data)

            connection.commit()
            cursor.close()
            print("   Completed  file " + o.name + " - " + str(num_rows) + " Rows Inserted")

        num_files += 1

        # remove file
        os.remove(path_filename)

        #######################################
        # insert bulk tags to the database
        #######################################
        data = []
        for tag in tags_keys:
            row_data = (str(tenancy.name), tag, str(tenancy.name), tag)
            data.append(row_data)

        if data:
            cursor = cx_Oracle.Cursor(connection)
            sql = "INSERT INTO OCI_COST_TAG_KEYS (TENANT_NAME , TAG_KEY) "
            sql += "SELECT :1, :2 FROM DUAL "
            sql += "WHERE NOT EXISTS (SELECT 1 FROM OCI_COST_TAG_KEYS B WHERE B.TENANT_NAME = :3 AND B.TAG_KEY = :4)"

            cursor.prepare(sql)
            cursor.executemany(None, data)
            connection.commit()
            cursor.close()
            print("   Total " + str(len(data)) + " Tags Merged.")

        return num_files

    except cx_Oracle.DatabaseError as e:
        print("\nload_cost_file() - Error manipulating database - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        print("\nload_cost_file() - Error Download Usage and insert to database - " + str(e))
        raise SystemExit


#########################################################################
# Load Usage File
##########################################################################
def load_usage_file(connection, object_storage, object_file, max_file_id, cmd, tenancy, compartments):
    num_files = 0
    num_rows = 0
    try:
        o = object_file

        # keep tag keys per file
        tags_keys = []

        # get file name
        filename = o.name.rsplit('/', 1)[-1]
        file_id = filename[:-7]
        file_time = str(o.time_created)[0:16]

        # if file already loaded, skip (check if < max_usage_file_id)
        if str(max_file_id) != "None":
            if file_id <= str(max_file_id):
                return num_files

        # if file id enabled, check
        if cmd.fileid:
            if file_id != cmd.file_id:
                return num_files

        # check file date
        if cmd.filedate:
            if file_time <= cmd.filedate:
                return num_files

        path_filename = work_report_dir + '/' + filename
        print("   Processing file " + o.name + " - " + str(o.size) + " bytes, " + file_time)

        # download file
        object_details = object_storage.get_object(usage_report_namespace, str(tenancy.id), o.name)
        with open(path_filename, 'wb') as f:
            for chunk in object_details.data.raw.stream(1024 * 1024, decode_content=False):
                f.write(chunk)

        # Read file to variable
        with gzip.open(path_filename, 'rt') as file_in:
            csv_reader = csv.DictReader(file_in)

            # sql statement
            sql = "INSERT INTO OCI_USAGE (TENANT_NAME , FILE_ID, USAGE_INTERVAL_START, USAGE_INTERVAL_END, PRD_SERVICE, PRD_RESOURCE, "
            sql += "PRD_COMPARTMENT_ID, PRD_COMPARTMENT_NAME, PRD_COMPARTMENT_PATH, PRD_REGION, PRD_AVAILABILITY_DOMAIN, USG_RESOURCE_ID, "
            sql += "USG_BILLED_QUANTITY, USG_CONSUMED_QUANTITY, USG_CONSUMED_UNITS, USG_CONSUMED_MEASURE, IS_CORRECTION, TAGS_DATA "
            sql += ") VALUES ("
            sql += ":1, :2, to_date(:3,'YYYY-MM-DD HH24:MI'), to_date(:4,'YYYY-MM-DD HH24:MI'), :5, :6, "
            sql += ":7, :8, :9, :10, :11, :12, "
            sql += "to_number(:13), to_number(:14), :15, :16, :17 ,:18 "
            sql += ") "

            # Adjust the batch size to meet memory and performance requirements
            batch_size = 5000
            array_size = 1000

            # insert bulk to database
            cursor = cx_Oracle.Cursor(connection)

            # Predefine the memory areas to match the table definition
            cursor.setinputsizes(None, array_size)

            data = []
            for row in csv_reader:

                # find compartment path
                compartment_path = ""
                for c in compartments:
                    if c['id'] == row['product/compartmentId']:
                        compartment_path = c['path']

                # Handle Tags up to 3500 chars with # seperator
                tags_data = ""
                for (key, value) in row.items():
                    if 'tags' in key and len(value) > 0:

                        # remove # and = from the tags keys and value
                        keyadj = str(key).replace("tags/", "").replace("#", "").replace("=", "")
                        valueadj = str(value).replace("#", "").replace("=", "")

                        # check if length < 3500 to avoid overflow database column
                        if len(tags_data) + len(keyadj) + len(valueadj) + 2 < 3500:
                            tags_data += ("#" if tags_data == "" else "") + keyadj + "=" + valueadj + "#"

                        # add tag key to tag_keys array
                            if keyadj not in tags_keys:
                                tags_keys.append(keyadj)

                # Assign each column to variable to avoid error if column missing from the file
                lineItem_intervalUsageStart = get_column_value_from_array('lineItem/intervalUsageStart', row)
                lineItem_intervalUsageEnd = get_column_value_from_array('lineItem/intervalUsageEnd', row)
                product_service = get_column_value_from_array('product/service', row)
                product_resource = get_column_value_from_array('product/resource', row)
                product_compartmentId = get_column_value_from_array('product/compartmentId', row)
                product_compartmentName = get_column_value_from_array('product/compartmentName', row)
                product_region = get_column_value_from_array('product/region', row)
                product_availabilityDomain = get_column_value_from_array('product/availabilityDomain', row)
                product_resourceId = get_column_value_from_array('product/resourceId', row)
                usage_billedQuantity = get_column_value_from_array('usage/billedQuantity', row)
                usage_consumedQuantity = get_column_value_from_array('usage/consumedQuantity', row)
                usage_consumedQuantityUnits = get_column_value_from_array('usage/consumedQuantityUnits', row)
                usage_consumedQuantityMeasure = get_column_value_from_array('usage/consumedQuantityMeasure', row)
                lineItem_isCorrection = get_column_value_from_array('lineItem/isCorrection', row)

                # create array for bulk insert
                row_data = (
                    str(tenancy.name),
                    file_id,
                    lineItem_intervalUsageStart[0:10] + " " + lineItem_intervalUsageStart[11:16],
                    lineItem_intervalUsageEnd[0:10] + " " + lineItem_intervalUsageEnd[11:16],
                    product_service,
                    product_resource,
                    product_compartmentId,
                    product_compartmentName,
                    compartment_path,
                    product_region,
                    product_availabilityDomain,
                    product_resourceId,
                    usage_billedQuantity,
                    usage_consumedQuantity,
                    usage_consumedQuantityUnits,
                    usage_consumedQuantityMeasure,
                    lineItem_isCorrection,
                    tags_data
                )
                data.append(row_data)
                num_rows += 1

                # insert every buffer size
                if len(data) % batch_size == 0:
                    cursor.executemany(sql, data)
                    data = []

            # final insert
            if data:
                cursor.executemany(sql, data)

            # commit
            connection.commit()
            cursor.close()
            print("   Completed  file " + o.name + " - " + str(num_rows) + " Rows Inserted")

        num_files += 1

        # remove file
        os.remove(path_filename)

        #######################################
        # insert bulk tags to the database
        #######################################
        data = []
        for tag in tags_keys:
            row_data = (str(tenancy.name), tag, str(tenancy.name), tag)
            data.append(row_data)

        if data:
            cursor = cx_Oracle.Cursor(connection)
            sql = "INSERT INTO OCI_USAGE_TAG_KEYS (TENANT_NAME , TAG_KEY) "
            sql += "SELECT :1, :2 FROM DUAL "
            sql += "WHERE NOT EXISTS (SELECT 1 FROM OCI_USAGE_TAG_KEYS B WHERE B.TENANT_NAME = :3 AND B.TAG_KEY = :4)"

            cursor.prepare(sql)
            cursor.executemany(None, data)
            connection.commit()
            cursor.close()
            print("   Total " + str(len(data)) + " Tags Merged.")

        return num_files

    except cx_Oracle.DatabaseError as e:
        print("\nload_usage_file() - Error manipulating database - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        print("\nload_usage_file() - Error Download Usage and insert to database - " + str(e))
        raise SystemExit


##########################################################################
# Main
##########################################################################
def main_process():
    cmd = set_parser_arguments()
    if cmd is None:
        exit()
    config, signer = create_signer(cmd)

    ############################################
    # Start
    ############################################
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
        tenancy_home_region = ""

        # find home region full name
        subscribed_regions = identity.list_region_subscriptions(tenancy.id).data
        for reg in subscribed_regions:
            if reg.is_home_region:
                tenancy_home_region = str(reg.region_name)

        print("   Tenant Name : " + str(tenancy.name))
        print("   Tenant Id   : " + tenancy.id)
        print("   App Version : " + version)
        print("   Home Region : " + tenancy_home_region)
        print("")

        # set signer home region
        signer.region = tenancy_home_region
        config['region'] = tenancy_home_region

        # Extract compartments
        compartments = identity_read_compartments(identity, tenancy)

    except Exception as e:
        print("\nError extracting compartments section - " + str(e) + "\n")
        raise SystemExit

    ############################################
    # connect to database
    ############################################
    max_usage_file_id = ""
    max_cost_file_id = ""
    connection = None
    try:
        print("\nConnecting to database " + cmd.dname)
        connection = cx_Oracle.connect(user=cmd.duser, password=cmd.dpass, dsn=cmd.dname, encoding="UTF-8", nencoding="UTF-8")
        cursor = connection.cursor()
        print("   Connected")

        # Check tables structure
        print("\nChecking Database Structure...")
        check_database_table_structure_usage(connection)
        check_database_table_structure_cost(connection)
        check_database_table_structure_price_list(connection, tenancy.name)

        ###############################
        # fetch max file id processed
        # for usage and cost
        ###############################
        print("\nChecking Last Loaded File...")
        sql = "select nvl(max(file_id),'0') as file_id from OCI_USAGE where to_char(TENANT_NAME)=:tenant_name"
        cursor.execute(sql, {"tenant_name": str(tenancy.name)})
        max_usage_file_id, = cursor.fetchone()

        sql = "select nvl(max(file_id),'0') as file_id from OCI_COST where to_char(TENANT_NAME)=:tenant_name"
        cursor.execute(sql, {"tenant_name": str(tenancy.name)})
        max_cost_file_id, = cursor.fetchone()

        print("   Max Usage File Id Processed = " + str(max_usage_file_id))
        print("   Max Cost  File Id Processed = " + str(max_cost_file_id))
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database - " + str(e) + "\n")
        raise SystemExit

    except Exception as e:
        raise Exception("\nError manipulating database - " + str(e))

    ############################################
    # Download Usage, cost and insert to database
    ############################################
    try:
        print("\nConnecting to Object Storage Service...")

        object_storage = oci.object_storage.ObjectStorageClient(config, signer=signer)
        if cmd.proxy:
            object_storage.base_client.session.proxies = {'https': cmd.proxy}
        print("   Connected")

        #############################
        # Handle Report Usage
        #############################
        usage_num = 0
        if not cmd.skip_usage:
            print("\nHandling Usage Report...")
            objects = object_storage.list_objects(usage_report_namespace, str(tenancy.id), fields="timeCreated,size", limit=999, prefix="reports/usage-csv/", start="reports/usage-csv/" + max_usage_file_id).data
            for object_file in objects.objects:
                usage_num += load_usage_file(connection, object_storage, object_file, max_usage_file_id, cmd, tenancy, compartments)
            print("\n   Total " + str(usage_num) + " Usage Files Loaded")

        #############################
        # Handle Cost Usage
        #############################
        cost_num = 0
        if not cmd.skip_cost:
            print("\nHandling Cost Report...")
            objects = object_storage.list_objects(usage_report_namespace, str(tenancy.id), fields="timeCreated,size", limit=999, prefix="reports/cost-csv/", start="reports/cost-csv/" + max_cost_file_id).data
            for object_file in objects.objects:
                cost_num += load_cost_file(connection, object_storage, object_file, max_cost_file_id, cmd, tenancy, compartments)
            print("\n   Total " + str(cost_num) + " Cost Files Loaded")

        # Handle Index structure if not exist
        check_database_index_structure_usage(connection)
        check_database_index_structure_cost(connection)

        # Update oci_usage_stats and oci_cost_stats if there were files
        if usage_num > 0:
            update_usage_stats(connection)
        if cost_num > 0:
            update_cost_stats(connection)
            update_cost_reference(connection)
            update_price_list(connection)
            update_public_rates(connection, tenancy.name)

        # Close Connection
        connection.close()

    except cx_Oracle.DatabaseError as e:
        print("\nError manipulating database - " + str(e) + "\n")

    except Exception as e:
        print("\nError Download Usage and insert to database - " + str(e))

    ############################################
    # print completed
    ############################################
    print("\nCompleted at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


##########################################################################
# Execute Main Process
##########################################################################
main_process()
