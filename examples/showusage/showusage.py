# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# showusage.py
#
# @author: Adi Zohar, Oct 07 2021, Updated July 19th, 2024
# Added OSR Eligible for tenant grouping and CSV files
# Added new reports - Special and Compartment
# Added Monthly Reports - use -g MONTH
#
# Supports Python 3
##########################################################################
# Application Command line parameters
#
#   -c config    - OCI CLI Config
#   -t profile   - profile inside the config file
#   -p proxy     - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip          - Use Instance Principals for Authentication
#   -g  grn      - Granularity DAILY / MONTHLY (Default DAILY)
#   -dt          - Use Instance Principals with delegation token for cloud shell
#   -ds date     - Start Date in YYYY-MM-DD format
#   -de date     - End Date in YYYY-MM-DD format (Not Inclusive)
#   -ld days     - Add Days Combined with Start Date (de is ignored if specified)
#   -ld days     - Add Days Combined with Start Date (de is ignored if specified)
#   -report type - Report Type = PRODUCT, DATE, REGION, SERVICE, RESOURCE, TENANT, SPECIAL, COMPARTMENT
#                  SPECIAL is group by Service, Region, Product Description
#   -csv         - Write to CSV files - usage_products.csv, usage_by_date.csv, usage_region.csvs,
#                                       usage_resources.csv, usage_tenants.csv, usage_special.csv, usage_compartments.csv
#
##########################################################################
# Those are the valid options for GroupBy:
#    "tagNamespace", "tagKey", "tagValue", "service", "skuName", "skuPartNumber", "unit", "compartmentName",
#    "compartmentPath", "compartmentId", "platform", "region", "logicalAd", "resourceId", "tenantId", "tenantName"
##########################################################################
# Info:
#    List Tenancy Usage
#
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of ShowUsageGroup group with below Policy rules:
#          Allow group ShowUsageGroup to inspect tenancies in tenancy
#          Allow group ShowUsageGroup to read usage-report in tenancy
#
#    Option 2 - Instance Principle
#       Compute instance part of DynShowUsageGroup dynamic group with policy rules:
#          Allow dynamic group DynShowUsageGroup to inspect tenancies in tenancy
#          Allow dynamic group DynShowUsageGroup to read usage-report in tenancy
#
##########################################################################
# Modules Included:
# - oci.identity.IdentityClient
# - oci.usage_api.UsageapiClient
#
# APIs Used:
# - IdentityClient.get_tenancy               - Policy TENANCY_INSPECT
# - IdentityClient.list_region_subscriptions - Policy TENANCY_INSPECT
# - UsageapiClient.request_summarized_usages - read usage-report
#
##########################################################################
import sys
import argparse
import datetime
import oci
import os
import platform
import csv

version = "2024.07.19"

csv_file_products = "usage_products.csv"
csv_file_by_date = "usage_by_date.csv"
csv_file_regions = "usage_regions.csv"
csv_file_resources = "usage_resources.csv"
csv_file_tenants = "usage_tenants.csv"
csv_file_service = "usage_service.csv"
csv_file_special = "usage_special.csv"
csv_file_compartment = "usage_compartments.csv"


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
# custom argparse *date* type for user dates
##########################################################################
def valid_date_type(arg_date_str):
    try:
        return datetime.datetime.strptime(arg_date_str, "%Y-%m-%d")
    except ValueError:
        msg = "Given Date ({0}) not valid! Expected format, YYYY-MM-DD!".format(arg_date_str)
        raise argparse.ArgumentTypeError(msg)


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
# Duration / days or months
##########################################################################
def duration(min_date, max_date, granularity):

    if granularity == 'DAILY':
        days = (max_date - min_date).days + 1
        # print("Duration = " + str(days) + " days")
        return days
    else:
        months = max_date.month - min_date.month + 12 * (max_date.year - min_date.year) + 1
        # print("Duration = " + str(months) + " Months")
        return months


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

        print("CSV: " + file_name + " created")

    except Exception as e:
        raise Exception("Error in export_to_csv_file: " + str(e.args))


##########################################################################
# Group Dictionaries by PK
##########################################################################
def group_dictionaries(data):

    try:
        gdata = {}
        for item in data:
            pk = item['pk']
            if pk not in gdata:
                gdata[pk] = item
            else:
                gdata[pk]['cost'] += item['cost']
                gdata[pk]['quantity'] += item['quantity']
                if item['currency'] and not gdata[pk]['currency']:
                    gdata[pk]['currency'] = item['currency']
                if 'sku_part_number' in item and 'sku_name' in item and 'osr_eligible' in gdata[pk]:
                    gdata[pk]['osr_eligible'] += osr_eligible_cost(item['sku_part_number'], item['sku_name'], item['cost'])

        return gdata
    except Exception as e:
        print("\nException Error at 'group_dictionaries' - " + str(e))


##########################################################################
# Usage Daily by Tenant
##########################################################################
def osr_eligible_cost(sku_part_number, sku_name, cost):

    # IF Windows or VMWare
    if 'windows' in sku_name.lower() or 'vmware' in sku_name.lower():
        return 0

    # if Market Image with MP
    if str(sku_part_number).lower()[0:1] == 'mp':
        return 0
    return cost


##########################################################################
# Usage Product by Date
##########################################################################
def usage_product(usageClient, tenant_id, time_usage_started, time_usage_ended, is_csv, granularity):

    try:
        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity=granularity,
            query_type='COST',
            group_by=['skuPartNumber', 'skuName'],
            time_usage_started=time_usage_started.strftime('%Y-%m-%dT%H:%M:%SZ'),
            time_usage_ended=time_usage_ended.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

        # usageClient.request_summarized_usages
        request_summarized_usages = usageClient.request_summarized_usages(
            requestSummarizedUsagesDetails,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )

        ################################
        # Add all data to array data
        ################################
        data = []
        min_date = None
        max_date = None
        date_format = '%Y-%m-%d' if granularity == 'DAILY' else '%Y-%m'
        currency = ""
        for item in request_summarized_usages.data.items:
            data.append({
                'pk': item.sku_part_number,
                'sku': item.sku_part_number,
                'sku_name': item.sku_name if item.sku_part_number in item.sku_name else item.sku_part_number + " - " + item.sku_name,
                'sku_part_number': item.sku_part_number,
                'osr_eligible': osr_eligible_cost(item.sku_part_number, item.sku_name, item.computed_amount if item.computed_amount else 0),
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'currency': item.currency.lstrip(),
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if item.currency.lstrip():
                currency = item.currency
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        days = duration(min_date, max_date, granularity)

        ################################
        # Group Dictionaries by PK
        ################################
        gdata = group_dictionaries(data)

        ################################
        # if to generate to csv
        ################################
        if is_csv:

            csv_output = []
            for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue

                if granularity == 'DAILY':
                    csv_output.append({
                        'Product SKU': item['sku_part_number'],
                        'Product Name': item['sku_name'],
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Days': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.1f}".format(item['quantity']),
                        'Osr Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost']),
                        'Month-31': "{:9.0f}".format(item['cost'] / days * 31),
                        'Year': "{:9.0f}".format(item['cost'] / days * 365),
                    })
                else:
                    csv_output.append({
                        'Product SKU': item['sku_part_number'],
                        'Product Name': item['sku_name'],
                        'Granularity': 'Monthly',
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Months': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.1f}".format(item['quantity']),
                        'Osr Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost'])
                    })

            export_to_csv_file(csv_file_products, csv_output)

        else:

            ################################
            # Print to screen
            ################################
            col = {
                'product': 65,
                'quantity': 14,
                'days': 10,
                'osr_eligible': 13,
                'cost': 13,
                'month': 13,
                'year': 13
            }

            currency_print = (" in " + currency) if currency else ""
            product_header = granularity + " Product Summary for " + min_date.strftime(date_format) + " - " + max_date.strftime(date_format) + currency_print
            print_header(product_header, 3)
            print("")

            print(
                "Product".ljust(col['product']) +
                " Quantity".rjust(col['quantity']) +
                " Duration".rjust(col['days']) +
                " OSR Eligible".rjust(col['osr_eligible']) +
                " Cost".rjust(col['cost']) +
                (" Month-31".rjust(col['month']) if granularity == 'DAILY' else "") +
                (" Year".rjust(col['year']) if granularity == 'DAILY' else "")
            )

            print(
                "".ljust(col['product'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )

            total = 0
            osr_total = 0
            for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue
                total += item['cost']
                osr_total += item['osr_eligible']
                line = item['sku_name'].ljust(col['product'])[0:col['product']]
                line += "{:8,.1f}".format(item['quantity']).rjust(col['quantity'])
                line += "{:8,.0f}".format(days).rjust(col['days'])
                line += "{:8,.1f}".format(item['osr_eligible']).rjust(col['osr_eligible'])
                line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
                if granularity == 'DAILY':
                    line += "{:9,.0f}".format(item['cost'] / days * 31).rjust(col['month'])
                    line += "{:9,.0f}".format(item['cost'] / days * 365).rjust(col['year'])
                print(line)

            # Total
            print(
                "".ljust(col['product'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")

            )
            print(
                "Total ".ljust(col['product'] + col['quantity'] + col['days']) +
                " {:8,.1f}".format(osr_total).rjust(col['osr_eligible']) +
                " {:8,.1f}".format(total).rjust(col['cost']) +
                (" {:9,.0f}".format(total / days * 31).rjust(col['month']) if granularity == 'DAILY' else "") +
                (" {:9,.0f}".format(total / days * 31 * 12).rjust(col['year']) if granularity == 'DAILY' else "")
            )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_product' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_product' - " + str(e))


##########################################################################
# Usage Daily by Region
##########################################################################
def usage_region(usageClient, tenant_id, time_usage_started, time_usage_ended, is_csv, granularity):

    try:
        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity=granularity,
            query_type='COST',
            group_by=['region'],
            time_usage_started=time_usage_started.strftime('%Y-%m-%dT%H:%M:%SZ'),
            time_usage_ended=time_usage_ended.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

        # usageClient.request_summarized_usages
        request_summarized_usages = usageClient.request_summarized_usages(
            requestSummarizedUsagesDetails,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )

        ################################
        # Add all data to array data
        ################################
        data = []
        min_date = None
        max_date = None
        date_format = '%Y-%m-%d' if granularity == 'DAILY' else '%Y-%m'
        currency = ""
        for item in request_summarized_usages.data.items:
            data.append({
                'pk': item.region,
                'region': item.region,
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'currency': item.currency.lstrip(),
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if item.currency.lstrip():
                currency = item.currency
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        days = duration(min_date, max_date, granularity)

        ################################
        # Group Dictionaries by PK
        ################################
        gdata = group_dictionaries(data)

        ################################
        # if to generate to csv
        ################################
        if is_csv:

            csv_output = []
            for item_key in sorted(gdata, key=lambda x: gdata[x]['pk']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue

                if granularity == 'DAILY':
                    csv_output.append({
                        'Region': item_key,
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Days': days,
                        'Currency': item['currency'],
                        'Cost': "{:8.1f}".format(item['cost']),
                        'Month-31': "{:9.0f}".format(item['cost'] / days * 31),
                        'Year': "{:9.0f}".format(item['cost'] / days * 365)
                    })
                else:
                    csv_output.append({
                        'Region': item_key,
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Months': days,
                        'Currency': item['currency'],
                        'Cost': "{:8.1f}".format(item['cost'])
                    })

            export_to_csv_file(csv_file_regions, csv_output)

        else:
            ################################
            # Compact based on SKUs
            ################################
            col = {
                'region': 25,
                'days': 10,
                'cost': 13,
                'month': 13,
                'year': 13
            }

            currency_print = (" in " + currency) if currency else ""
            product_header = granularity + " Region Summary for " + min_date.strftime(date_format) + " - " + max_date.strftime(date_format) + currency_print
            print_header(product_header, 3)
            print("")
            print(
                "Region".ljust(col['region']) +
                " Duration".rjust(col['days']) +
                " Cost".rjust(col['cost']) +
                (" Month-31".rjust(col['month']) if granularity == 'DAILY' else "") +
                (" Year".rjust(col['year']) if granularity == 'DAILY' else "")
            )

            print(
                "".ljust(col['region'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )

            total = 0
            for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue
                total += item['cost']
                line = item_key.ljust(col['region'])
                line += "{:8,.0f}".format(days).rjust(col['days'])
                line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
                if granularity == 'DAILY':
                    line += "{:9,.0f}".format(item['cost'] / days * 31).rjust(col['month'])
                    line += "{:9,.0f}".format(item['cost'] / days * 365).rjust(col['year'])
                print(line)

            # Total
            print(
                "".ljust(col['region'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )
            print(
                "Total ".ljust(col['region'] + col['days']) +
                " {:8,.1f}".format(total).rjust(col['cost']) +
                (" {:9,.0f}".format(total / days * 31).rjust(col['month']) if granularity == 'DAILY' else "") +
                (" {:9,.0f}".format(total / days * 31 * 12).rjust(col['year']) if granularity == 'DAILY' else "")
            )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_region' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_region' - " + str(e))


##########################################################################
# Usage Daily by Tenant
##########################################################################
def usage_tenant(usageClient, tenant_id, time_usage_started, time_usage_ended, is_csv, granularity):

    try:
        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity=granularity,
            query_type='COST',
            group_by=['tenantName', 'skuPartNumber', 'skuName'],
            time_usage_started=time_usage_started.strftime('%Y-%m-%dT%H:%M:%SZ'),
            time_usage_ended=time_usage_ended.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

        # usageClient.request_summarized_usages
        request_summarized_usages = usageClient.request_summarized_usages(
            requestSummarizedUsagesDetails,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )

        ################################
        # Add all data to array data
        ################################
        data = []
        min_date = None
        max_date = None
        date_format = '%Y-%m-%d' if granularity == 'DAILY' else '%Y-%m'
        currency = ""
        for item in request_summarized_usages.data.items:
            data.append({
                'pk': item.tenant_name,
                'tenant': item.tenant_name,
                'sku_part_number': item.sku_part_number,
                'sku_name': item.sku_name,
                'osr_eligible': osr_eligible_cost(item.sku_part_number, item.sku_name, item.computed_amount if item.computed_amount else 0),
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'currency': item.currency.lstrip(),
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if item.currency.lstrip():
                currency = item.currency
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        days = duration(min_date, max_date, granularity)

        ################################
        # Group Dictionaries by PK
        ################################
        gdata = group_dictionaries(data)

        ################################
        # if to generate to csv
        ################################
        if is_csv:

            csv_output = []
            for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue

                if granularity == 'DAILY':
                    csv_output.append({
                        'Tenant': item_key,
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Days': days,
                        'Currency': item['currency'],
                        'Osr Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost']),
                        'Month-31': "{:9.0f}".format(item['cost'] / days * 31),
                        'Year': "{:9.0f}".format(item['cost'] / days * 365),
                    })
                else:
                    csv_output.append({
                        'Tenant': item_key,
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Months': days,
                        'Currency': item['currency'],
                        'Osr Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost'])
                    })

            export_to_csv_file(csv_file_tenants, csv_output)

        else:

            ################################
            # Print to screen
            ################################
            col = {
                'tenant': 30,
                'days': 10,
                'osr_eligible': 15,
                'cost': 15,
                'month': 13,
                'year': 13
            }

            currency_print = (" in " + currency) if currency else ""
            product_header = granularity + " Tenant Summary for " + min_date.strftime(date_format) + " - " + max_date.strftime(date_format) + currency_print
            print_header(product_header, 3)
            print("")
            print(
                "Tenant".ljust(col['tenant']) +
                " Duration".rjust(col['days']) +
                " OSR Eligible".rjust(col['osr_eligible']) +
                " Cost".rjust(col['cost']) +
                (" Month-31".rjust(col['month']) if granularity == 'DAILY' else "") +
                (" Year".rjust(col['year']) if granularity == 'DAILY' else "")
            )

            print(
                "".ljust(col['tenant'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['cost'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )

            total = 0
            osr_total = 0
            for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue
                total += item['cost']
                osr_total += item['osr_eligible']
                line = item_key.ljust(col['tenant'])
                line += "{:8,.0f}".format(days).rjust(col['days'])
                line += "{:8,.1f}".format(item['osr_eligible']).rjust(col['osr_eligible'])
                line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
                if granularity == 'DAILY':
                    line += "{:9,.0f}".format(item['cost'] / days * 31).rjust(col['month'])
                    line += "{:9,.0f}".format(item['cost'] / days * 365).rjust(col['year'])
                print(line)

            # Total
            print(
                "".ljust(col['tenant'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )
            print(
                "Total ".ljust(col['tenant'] + col['days']) +
                " {:8,.1f}".format(osr_total).rjust(col['osr_eligible']) +
                " {:8,.1f}".format(total).rjust(col['cost']) +
                (" {:9,.0f}".format(total / days * 31).rjust(col['month']) if granularity == 'DAILY' else "") +
                (" {:9,.0f}".format(total / days * 31 * 12).rjust(col['year']) if granularity == 'DAILY' else "")
            )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_tenant' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_tenant' - " + str(e))


##########################################################################
# Usage Daily by Service
##########################################################################
def usage_service(usageClient, tenant_id, time_usage_started, time_usage_ended, is_csv, granularity):

    try:
        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity=granularity,
            query_type='COST',
            group_by=['service', 'skuPartNumber', 'skuName'],
            time_usage_started=time_usage_started.strftime('%Y-%m-%dT%H:%M:%SZ'),
            time_usage_ended=time_usage_ended.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

        # usageClient.request_summarized_usages
        request_summarized_usages = usageClient.request_summarized_usages(
            requestSummarizedUsagesDetails,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )

        ################################
        # Add all data to array data
        ################################
        data = []
        min_date = None
        max_date = None
        date_format = '%Y-%m-%d' if granularity == 'DAILY' else '%Y-%m'
        currency = ""
        for item in request_summarized_usages.data.items:
            data.append({
                'pk': item.service,
                'service': item.service,
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'sku_part_number': item.sku_part_number,
                'sku_name': item.sku_name,
                'osr_eligible': osr_eligible_cost(item.sku_part_number, item.sku_name, item.computed_amount if item.computed_amount else 0),
                'currency': item.currency.lstrip(),
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if item.currency.lstrip():
                currency = item.currency
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        days = duration(min_date, max_date, granularity)

        ################################
        # Group Dictionaries by PK
        ################################
        gdata = group_dictionaries(data)

        ################################
        # if to generate to csv
        ################################
        if is_csv:

            csv_output = []
            for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue

                if granularity == 'DAILY':
                    csv_output.append({
                        'Service': item_key,
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Days': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.1f}".format(item['quantity']),
                        'Osr Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost']),
                        'Month-31': "{:9.0f}".format(item['cost'] / days * 31),
                        'Year': "{:9.0f}".format(item['cost'] / days * 365),
                    })
                else:
                    csv_output.append({
                        'Service': item_key,
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Months': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.1f}".format(item['quantity']),
                        'Osr Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost'])
                    })

            export_to_csv_file(csv_file_service, csv_output)

        else:

            ################################
            # Print to screen
            ################################
            col = {
                'service': 45,
                'quantity': 14,
                'days': 10,
                'osr_eligible': 15,
                'cost': 13,
                'month': 13,
                'year': 13
            }

            currency_print = (" in " + currency) if currency else ""
            product_header = granularity + " Service Summary for " + min_date.strftime(date_format) + " - " + max_date.strftime(date_format) + currency_print
            print_header(product_header, 3)
            print("")
            print(
                "Service".ljust(col['service']) +
                " Duration".rjust(col['days']) +
                " Quantity".rjust(col['quantity']) +
                " OSR Eligible".rjust(col['osr_eligible']) +
                " Cost".rjust(col['cost']) +
                (" Month-31".rjust(col['month']) if granularity == 'DAILY' else "") +
                (" Year".rjust(col['year']) if granularity == 'DAILY' else "")
            )

            print(
                "".ljust(col['service'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )

            total = 0
            osr_total = 0
            for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue
                total += item['cost']
                osr_total += item['osr_eligible']
                line = item_key.ljust(col['service'])
                line += "{:8,.0f}".format(days).rjust(col['days'])
                line += "{:8,.1f}".format(item['quantity']).rjust(col['quantity'])
                line += "{:8,.1f}".format(item['osr_eligible']).rjust(col['osr_eligible'])
                line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
                if granularity == 'DAILY':
                    line += "{:9,.0f}".format(item['cost'] / days * 31).rjust(col['month'])
                    line += "{:9,.0f}".format(item['cost'] / days * 365).rjust(col['year'])
                print(line)

            # Total
            print(
                "".ljust(col['service'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )
            print(
                "Total ".ljust(col['service'] + col['quantity'] + col['days']) +
                " {:8,.1f}".format(osr_total).rjust(col['osr_eligible']) +
                " {:8,.1f}".format(total).rjust(col['cost']) +
                (" {:9,.0f}".format(total / days * 31).rjust(col['month']) if granularity == 'DAILY' else "") +
                (" {:9,.0f}".format(total / days * 31 * 12).rjust(col['year']) if granularity == 'DAILY' else "")
            )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_service' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_service' - " + str(e))


##########################################################################
# Usage Daily by Compartment and Service
##########################################################################
def usage_compartment(usageClient, tenant_id, time_usage_started, time_usage_ended, is_csv, granularity):

    try:
        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity=granularity,
            query_type='COST',
            compartment_depth=5,
            group_by=['compartmentPath', 'service', 'skuPartNumber', 'skuName'],
            time_usage_started=time_usage_started.strftime('%Y-%m-%dT%H:%M:%SZ'),
            time_usage_ended=time_usage_ended.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

        # usageClient.request_summarized_usages
        request_summarized_usages = usageClient.request_summarized_usages(
            requestSummarizedUsagesDetails,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )

        ################################
        # Add all data to array data
        ################################
        data = []
        min_date = None
        max_date = None
        date_format = '%Y-%m-%d' if granularity == 'DAILY' else '%Y-%m'
        currency = ""
        for item in request_summarized_usages.data.items:
            data.append({
                'pk': item.compartment_path + ":" + item.service,
                'compartment': item.compartment_path,
                'service': item.service,
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'sku_part_number': item.sku_part_number,
                'sku_name': item.sku_name,
                'osr_eligible': osr_eligible_cost(item.sku_part_number, item.sku_name, item.computed_amount if item.computed_amount else 0),
                'currency': item.currency.lstrip(),
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if item.currency.lstrip():
                currency = item.currency
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        days = duration(min_date, max_date, granularity)

        ################################
        # Group Dictionaries by PK
        ################################
        gdata = group_dictionaries(data)

        ################################
        # if to generate to csv
        ################################
        if is_csv:

            csv_output = []
            for item_key in sorted(gdata, key=lambda x: gdata[x]['pk']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue

                if granularity == 'DAILY':
                    csv_output.append({
                        'Compartment Path': item['compartment'],
                        'Service': item['service'],
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Days': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.1f}".format(item['quantity']),
                        'Osr Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost']),
                        'Month-31': "{:9.0f}".format(item['cost'] / days * 31),
                        'Year': "{:9.0f}".format(item['cost'] / days * 365),
                    })
                else:
                    csv_output.append({
                        'Compartment Path': item['compartment'],
                        'Service': item['service'],
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Months': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.1f}".format(item['quantity']),
                        'Osr Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost'])
                    })

            export_to_csv_file(csv_file_compartment, csv_output)

        else:

            ################################
            # Print to screen
            ################################
            col = {
                'compartment': 70,
                'service': 40,
                'quantity': 14,
                'days': 10,
                'osr_eligible': 15,
                'cost': 13,
                'month': 13,
                'year': 13
            }

            currency_print = (" in " + currency) if currency else ""
            product_header = granularity + " Compartment Summary for " + min_date.strftime(date_format) + " - " + max_date.strftime(date_format) + currency_print
            print_header(product_header, 3)
            print("")
            print(
                "Compartment".ljust(col['compartment']) +
                " Service".ljust(col['service']) +
                " Duration".rjust(col['days']) +
                " Quantity".rjust(col['quantity']) +
                " OSR Eligible".rjust(col['osr_eligible']) +
                " Cost".rjust(col['cost']) +
                (" Month-31".rjust(col['month']) if granularity == 'DAILY' else "") +
                (" Year".rjust(col['year']) if granularity == 'DAILY' else "")
            )

            print(
                "".ljust(col['compartment'], '=') +
                " ".ljust(col['service'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )

            total = 0
            osr_total = 0
            for item_key in sorted(gdata, key=lambda x: gdata[x]['pk']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue
                total += item['cost']
                osr_total += item['osr_eligible']

                line = item['compartment'].ljust(col['compartment'])
                line += " " + item['service'].ljust(col['service'] - 1)
                line += "{:8,.0f}".format(days).rjust(col['days'])
                line += "{:8,.1f}".format(item['quantity']).rjust(col['quantity'])
                line += "{:8,.1f}".format(item['osr_eligible']).rjust(col['osr_eligible'])
                line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
                if granularity == 'DAILY':
                    line += "{:9,.0f}".format(item['cost'] / days * 31).rjust(col['month'])
                    line += "{:9,.0f}".format(item['cost'] / days * 365).rjust(col['year'])
                print(line)

            # Total
            print(
                "".ljust(col['compartment'], '=') +
                " ".ljust(col['service'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )
            print(
                "Total ".ljust(col['compartment'] + col['service'] + + col['days'] + col['quantity']) +
                " {:8,.1f}".format(osr_total).rjust(col['osr_eligible']) +
                " {:8,.1f}".format(total).rjust(col['cost']) +
                (" {:9,.0f}".format(total / days * 31).rjust(col['month']) if granularity == 'DAILY' else "") +
                (" {:9,.0f}".format(total / days * 31 * 12).rjust(col['year']) if granularity == 'DAILY' else "")
            )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_compartment' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_compartment' - " + str(e))


##########################################################################
# Usage Daily by Speical Grouping = Service, Region, Product Description
##########################################################################
def usage_special(usageClient, tenant_id, time_usage_started, time_usage_ended, is_csv, granularity):

    try:
        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity=granularity,
            query_type='COST',
            group_by=['service', 'region', 'skuPartNumber', 'skuName'],
            time_usage_started=time_usage_started.strftime('%Y-%m-%dT%H:%M:%SZ'),
            time_usage_ended=time_usage_ended.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

        # usageClient.request_summarized_usages
        request_summarized_usages = usageClient.request_summarized_usages(
            requestSummarizedUsagesDetails,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )

        ################################
        # Add all data to array data
        ################################
        data = []
        min_date = None
        max_date = None
        date_format = '%Y-%m-%d' if granularity == 'DAILY' else '%Y-%m'
        currency = ""
        for item in request_summarized_usages.data.items:
            data.append({
                'pk': item.service + ":" + item.region + ":" + item.sku_name,
                'service': item.service,
                'region': item.region,
                'sku_part_number': item.sku_part_number,
                'sku_name': item.sku_name,
                'osr_eligible': osr_eligible_cost(item.sku_part_number, item.sku_name, item.computed_amount if item.computed_amount else 0),
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'currency': item.currency.lstrip(),
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if item.currency.lstrip():
                currency = item.currency
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        days = duration(min_date, max_date, granularity)

        ################################
        # Group Dictionaries by PK
        ################################
        gdata = group_dictionaries(data)

        ################################
        # if to generate to csv
        ################################
        if is_csv:

            csv_output = []
            for item_key in sorted(gdata, key=lambda x: gdata[x]['pk']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue
                if granularity == 'DAILY':
                    csv_output.append({
                        'Service': item['service'],
                        'Region': item['region'],
                        'Product SKU': item['sku_part_number'],
                        'Product Name': item['sku_name'],
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Days': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.1f}".format(item['quantity']),
                        'OSR Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost']),
                        'Month-31': "{:9.0f}".format(item['cost'] / days * 31),
                        'Year': "{:9.0f}".format(item['cost'] / days * 365),
                    })
                else:
                    csv_output.append({
                        'Service': item['service'],
                        'Region': item['region'],
                        'Product SKU': item['sku_part_number'],
                        'Product Name': item['sku_name'],
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Months': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.1f}".format(item['quantity']),
                        'OSR Eligible Cost': "{:8.1f}".format(item['osr_eligible']),
                        'Cost': "{:8.1f}".format(item['cost'])
                    })

            export_to_csv_file(csv_file_special, csv_output)

        else:

            ################################
            # Print to screen
            ################################
            col = {
                'pk': 120,
                'days': 10,
                'osr_eligible': 15,
                'quantity': 14,
                'cost': 13
            }

            currency_print = (" in " + currency) if currency else ""
            product_header = granularity + " Service, Region and Product for " + min_date.strftime(date_format) + " - " + max_date.strftime(date_format) + currency_print
            print_header(product_header, 3)
            print("")
            print(
                "Service,Region and Product".ljust(col['pk']) +
                " Duration".rjust(col['days']) +
                " Quantity".rjust(col['quantity']) +
                " OSR Eligible".rjust(col['osr_eligible']) +
                " Cost".rjust(col['cost'])
            )

            print(
                "".ljust(col['pk'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=')
            )

            total = 0
            osr_total = 0
            for item_key in sorted(gdata, key=lambda x: gdata[x]['pk']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue
                total += item['cost']
                osr_total += item['osr_eligible']
                line = item_key.ljust(col['pk'])
                line += "{:8,.0f}".format(days).rjust(col['days'])
                line += "{:8,.1f}".format(item['quantity']).rjust(col['quantity'])
                line += "{:8,.1f}".format(item['osr_eligible']).rjust(col['osr_eligible'])
                line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
                print(line)

            # Total
            print(
                "".ljust(col['pk'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=')
            )
            print(
                "Total ".ljust(col['pk'] + col['days'] + col['quantity']) +
                " {:8,.1f}".format(osr_total).rjust(col['osr_eligible']) +
                " {:8,.1f}".format(total).rjust(col['cost'])
            )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_special' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_special' - " + str(e))


##########################################################################
# Usage Daily by Resource
##########################################################################
def usage_resource(usageClient, tenant_id, time_usage_started, time_usage_ended, is_csv, granularity):

    try:
        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity=granularity,
            query_type='COST',
            group_by=['resourceId', 'region', 'skuPartNumber', 'skuName'],
            time_usage_started=time_usage_started.strftime('%Y-%m-%dT%H:%M:%SZ'),
            time_usage_ended=time_usage_ended.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

        # usageClient.request_summarized_usages
        request_summarized_usages = usageClient.request_summarized_usages(
            requestSummarizedUsagesDetails,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )

        ################################
        # Add all data to array data
        ################################
        data = []
        min_date = None
        max_date = None
        date_format = '%Y-%m-%d' if granularity == 'DAILY' else '%Y-%m'
        currency = ""
        for item in request_summarized_usages.data.items:
            data.append({
                'pk': item.resource_id,
                'resourceid': item.resource_id,
                'region': item.region,
                'sku_part_number': item.sku_part_number,
                'sku_name': item.sku_name,
                'osr_eligible': osr_eligible_cost(item.sku_part_number, item.sku_name, item.computed_amount if item.computed_amount else 0),
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'currency': item.currency.lstrip(),
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if item.currency.lstrip():
                currency = item.currency
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        days = duration(min_date, max_date, granularity)

        ################################
        # Group Dictionaries by PK
        ################################
        gdata = group_dictionaries(data)

        ################################
        # if to generate to csv
        ################################
        if is_csv:

            csv_output = []
            for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue

                if granularity == 'DAILY':
                    csv_output.append({
                        'Resource': item_key,
                        'Region': item['region'],
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Days': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.4f}".format(item['quantity']),
                        'Osr Eligible Cost': "{:8.4f}".format(item['osr_eligible']),
                        'Cost': "{:8.4f}".format(item['cost']),
                        'Month-31': "{:9.0f}".format(item['cost'] / days * 31),
                        'Year': "{:9.0f}".format(item['cost'] / days * 365),
                    })
                else:
                    csv_output.append({
                        'Resource': item_key,
                        'Region': item['region'],
                        'Start Date': min_date.strftime('%m/%d/%Y'),
                        'End Date': max_date.strftime('%m/%d/%Y'),
                        'Months': days,
                        'Currency': item['currency'],
                        'Quantity': "{:8.4f}".format(item['quantity']),
                        'Osr Eligible Cost': "{:8.4f}".format(item['osr_eligible']),
                        'Cost': "{:8.4f}".format(item['cost'])
                    })

            export_to_csv_file(csv_file_resources, csv_output)

        else:

            ################################
            # Print to screen
            ################################
            col = {
                'resourceid': 100,
                'quantity': 14,
                'days': 10,
                'osr_eligible': 15,
                'cost': 13,
                'month': 13,
                'year': 13
            }

            currency_print = (" in " + currency) if currency else ""
            product_header = granularity + " ResourceId Summary for " + min_date.strftime(date_format) + " - " + max_date.strftime(date_format) + currency_print
            print_header(product_header, 3)
            print("")
            print(
                "Resource".ljust(col['resourceid']) +
                " Duration".rjust(col['days']) +
                " Quantity".rjust(col['quantity']) +
                " OSR Eligible".rjust(col['osr_eligible']) +
                " Cost".rjust(col['cost']) +
                (" Month-31".rjust(col['month']) if granularity == 'DAILY' else "") +
                (" Year".rjust(col['year']) if granularity == 'DAILY' else "")
            )

            print(
                "".ljust(col['resourceid'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )

            total = 0
            osr_total = 0
            for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue
                total += item['cost']
                osr_total += item['osr_eligible']
                line = str(item_key[0:col['resourceid']]).ljust(col['resourceid'])
                line += "{:8,.0f}".format(days).rjust(col['days'])
                line += "{:8,.1f}".format(item['quantity']).rjust(col['quantity'])
                line += "{:8,.1f}".format(item['osr_eligible']).rjust(col['osr_eligible'])
                line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
                if granularity == 'DAILY':
                    line += "{:9,.0f}".format(item['cost'] / days * 31).rjust(col['month'])
                    line += "{:9,.0f}".format(item['cost'] / days * 365).rjust(col['year'])
                print(line)

            # Total
            print(
                "".ljust(col['resourceid'], '=') +
                " ".ljust(col['days'], '=') +
                " ".ljust(col['quantity'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )
            print(
                "Total ".ljust(col['resourceid'] + col['days'] + col['quantity']) +
                " {:8,.1f}".format(osr_total).rjust(col['osr_eligible']) +
                " {:8,.1f}".format(total).rjust(col['cost']) +
                (" {:9,.0f}".format(total / days * 31).rjust(col['month']) if granularity == 'DAILY' else "") +
                (" {:9,.0f}".format(total / days * 31 * 12).rjust(col['year']) if granularity == 'DAILY' else "")
            )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_resource' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_resource' - " + str(e))


##########################################################################
# Usage Daily Summary
##########################################################################
def usage_summary(usageClient, tenant_id, time_usage_started, time_usage_ended, is_csv, granularity):

    try:

        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity=granularity,
            query_type='COST',
            group_by=['skuPartNumber', 'skuName'],
            time_usage_started=time_usage_started.strftime('%Y-%m-%dT%H:%M:%SZ'),
            time_usage_ended=time_usage_ended.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

        # usageClient.request_summarized_usages
        request_summarized_usages = usageClient.request_summarized_usages(
            requestSummarizedUsagesDetails,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )

        ################################
        # Add all data to array data
        ################################
        data = []
        min_date = None
        max_date = None
        currency = ""
        date_format = '%Y-%m-%d' if granularity == 'DAILY' else '%Y-%m'
        for item in request_summarized_usages.data.items:
            data.append({
                'pk': item.time_usage_started.strftime(date_format),
                'day': item.time_usage_started.strftime(date_format),
                'sku_part_number': item.sku_part_number,
                'sku_name': item.sku_name,
                'osr_eligible': osr_eligible_cost(item.sku_part_number, item.sku_name, item.computed_amount if item.computed_amount else 0),
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'currency': item.currency.lstrip(),
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if item.currency.lstrip():
                currency = item.currency
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        ################################
        # Group Dictionaries by PK
        ################################
        gdata = group_dictionaries(data)

        ################################
        # if to generate to csv
        ################################
        if is_csv:

            csv_output = []
            for item_key in sorted(gdata, key=lambda x: gdata[x]['day']):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue

                if granularity == 'DAILY':
                    csv_output.append({
                        'Day': item['day'],
                        'Currency': item['currency'],
                        'Osr Eligible Cost': "{:8.4f}".format(item['osr_eligible']),
                        'Cost': "{:8.3f}".format(item['cost']),
                        'Month-31': "{:9.0f}".format(item['cost'] * 31),
                        'Year': "{:9.0f}".format(item['cost'] * 365),
                    })
                else:
                    csv_output.append({
                        'Day': item['day'],
                        'Currency': item['currency'],
                        'Osr Eligible Cost': "{:8.4f}".format(item['osr_eligible']),
                        'Cost': "{:8.3f}".format(item['cost'])
                    })

            export_to_csv_file(csv_file_by_date, csv_output)

        else:

            ################################
            # Print to screen
            ################################
            col = {
                'day': 15,
                'osr_eligible': 15,
                'cost': 15,
                'month': 15,
                'year': 15
            }

            currency_print = (" in " + currency) if currency else ""
            product_header = granularity + " Summary for " + min_date.strftime(date_format) + " - " + max_date.strftime(date_format) + currency_print
            print_header(product_header, 3)
            print("")
            print(
                "Date".ljust(col['day']) +
                " OSR Eligible".rjust(col['osr_eligible']) +
                " Cost".rjust(col['cost']) +
                (" Month-31".rjust(col['month']) if granularity == 'DAILY' else "") +
                (" Year".rjust(col['year']) if granularity == 'DAILY' else "")
            )

            print(
                "".ljust(col['day'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )

            total = 0
            osr_total = 0
            for item_key in sorted(gdata, key=lambda x: x):
                item = gdata[item_key]
                if item['cost'] == 0:
                    continue
                total += item['cost']
                osr_total += item['osr_eligible']
                line = item_key.ljust(col['day'])[0:col['day']]
                line += "{:8,.1f}".format(item['osr_eligible']).rjust(col['osr_eligible'])
                line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
                if granularity == 'DAILY':
                    line += "{:9,.0f}".format(item['cost'] * 31).rjust(col['month'])
                    line += "{:9,.0f}".format(item['cost'] * 365).rjust(col['year'])
                print(line)

            # Total
            print(
                "".ljust(col['day'], '=') +
                " ".ljust(col['osr_eligible'], '=') +
                " ".ljust(col['cost'], '=') +
                (" ".ljust(col['month'], '=') if granularity == 'DAILY' else "") +
                (" ".ljust(col['year'], '=') if granularity == 'DAILY' else "")
            )
            print(
                "Total ".ljust(col['day']) +
                " {:8,.1f}".format(osr_total).rjust(col['osr_eligible']) +
                " {:8,.1f}".format(total).rjust(col['cost'])
            )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_summary' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_summary' - " + str(e))


##########################################################################
# Main Process
##########################################################################
def main():

    report_type_array = ['ALL', 'DATE', 'SERVICE', 'PRODUCT', 'REGION', 'RESOURCE', 'SPECIAL', 'TENANT', 'COMPARTMENT']

    # Get Command Line Parser
    # parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(usage=argparse.SUPPRESS, formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=150))
    parser.add_argument('-c', default="", dest='config_file', help='OCI CLI Config file')
    parser.add_argument('-t', default="", dest='config_profile', help='Config Profile inside the config file')
    parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
    parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
    parser.add_argument('-dt', action='store_true', default=False, dest='is_delegation_token', help='Use Delegation Token for Authentication')
    parser.add_argument("-ds", default=None, dest='date_start', help="Start Date - format YYYY-MM-DD", type=valid_date_type)
    parser.add_argument("-de", default=None, dest='date_end', help="End Date - format YYYY-MM-DD, (Not Inclusive)", type=valid_date_type)
    parser.add_argument("-days", default=None, dest='days', help="Add Days Combined with Start Date (de is ignored if specified)", type=int)
    parser.add_argument("-g", default="DAILY", dest='granularity', help="Granularity DAILY or MONTHLY (Default DAILY)")
    parser.add_argument("-report", default="ALL", dest='report', help="Report Type = " + ' / '.join(x for x in report_type_array) + " ( Default = ALL )")
    parser.add_argument('-csv', action='store_true', default=False, dest='csv', help='Write to CSV files instead of output to the screen - usage_*.csv')
    cmd = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return

    if not cmd.report or cmd.report not in report_type_array:

        parser.print_help()
        print("")
        print("***************************************************************")
        print("***          You must specify report type !                 ***")
        print("***   DATE        = Date cost                               ***")
        print("***   PRODUCT     = Product Summary Cost                    ***")
        print("***   SERVICE     = Service Summary Cost                    ***")
        print("***   REGION      = Region Summary Cost                     ***")
        print("***   RESOURCE    = Resource Summary Cost                   ***")
        print("***   SPECIAL     = Service, Region and Product             ***")
        print("***   COMPARTMENT = Compartment Path, Service               ***")
        print("***                                                         ***")
        print("***   ALL     = All Reports                                 ***")
        print("***************************************************************")
        return None

    if not (cmd.date_start):

        parser.print_help()
        print("")
        print("**********************************************************")
        print("***          You must specify date range!!             ***")
        print("***   Either DATE_START+DAYS or DATE_START+DATE_END    ***")
        print("**********************************************************")
        return None

    # Start print time info
    print_header("Running Show Usage", 0)

    print("Author          : Adi Zohar")
    print("Disclaimer      : This is not an official Oracle application,")
    print("                : It does not supported by Oracle, It should NOT be used for utilization calculation purposes !")
    print("                : Last 2 days may not be filled and should not be used")
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
    print("Command Line    : " + ' '.join(x for x in sys.argv[1:]))

    ############################################
    # Date Validation
    ############################################
    time_usage_started = None
    time_usage_ended = None
    report_type = cmd.report

    if cmd.date_start and cmd.date_start > datetime.datetime.now():
        print("\n!!! Error, Start date cannot be in the future !!!")
        sys.exit()

    if cmd.date_start and cmd.date_end and cmd.date_start > cmd.date_end:
        print("\n!!! Error, Start date cannot be greater than End date !!!")
        sys.exit()

    if cmd.date_start:
        time_usage_started = cmd.date_start

    if cmd.days:
        time_usage_ended = time_usage_started + datetime.timedelta(days=cmd.days)
    elif cmd.date_end:
        time_usage_ended = cmd.date_end
    else:
        time_usage_ended = time_usage_started + datetime.timedelta(days=1)

    print("Start Date      : " + time_usage_started.strftime('%m/%d/%Y'))
    print("End Date        : " + time_usage_ended.strftime('%m/%d/%Y') + " Not Included")

    ############################################
    # Days check
    ############################################
    days = (time_usage_ended - time_usage_started).days

    if days > 93 and cmd.granularity == 'DAILY':
        print("\n!!! Error, Max 93 days period allowed for DAILY, input is " + str(days) + " days, !!!")
        sys.exit()

    if days > 366 and cmd.granularity == 'MONTHLY':
        print("\n!!! Error, Max 366 days period allowed for MONTHLY, input is " + str(days) + " days, !!!")
        sys.exit()

    ############################################
    # create signer
    ############################################
    config, signer = create_signer(cmd.config_file, cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)
    tenant_id = ""

    print_header("Fetching data", 0)
    try:
        print("\nConnecting to Identity Service...\n")
        identity = oci.identity.IdentityClient(config, signer=signer)
        if cmd.proxy:
            identity.base_client.session.proxies = {'https': cmd.proxy}

        tenancy = identity.get_tenancy(config["tenancy"]).data
        regions = identity.list_region_subscriptions(tenancy.id).data
        tenant_id = tenancy.id

        # Set home region for connection
        for reg in regions:
            if reg.is_home_region:
                tenancy_home_region = str(reg.region_name)

        config['region'] = tenancy_home_region
        signer.region = tenancy_home_region

        print("Tenant Name  : " + str(tenancy.name))
        print("Tenant Id    : " + tenancy.id)
        print("Home Region  : " + tenancy_home_region)

    except Exception as e:
        raise RuntimeError("\nError fetching tenant information - " + str(e))

    ############################################
    # Connection to UsageAPI
    ############################################
    try:
        print("\nConnecting to UsageAPI Service...\n")
        usage_client = oci.usage_api.UsageapiClient(config, signer=signer)
        if cmd.proxy:
            usage_client.base_client.session.proxies = {'https': cmd.proxy}

        if report_type == 'DATE' or report_type == 'ALL':
            usage_summary(usage_client, tenant_id, time_usage_started, time_usage_ended, cmd.csv, cmd.granularity)

        if report_type == 'PRODUCT' or report_type == 'ALL':
            usage_product(usage_client, tenant_id, time_usage_started, time_usage_ended, cmd.csv, cmd.granularity)

        if report_type == 'REGION' or report_type == 'ALL':
            usage_region(usage_client, tenant_id, time_usage_started, time_usage_ended, cmd.csv, cmd.granularity)

        if report_type == 'SERVICE' or report_type == 'ALL':
            usage_service(usage_client, tenant_id, time_usage_started, time_usage_ended, cmd.csv, cmd.granularity)

        if report_type == 'RESOURCE' or report_type == 'ALL':
            usage_resource(usage_client, tenant_id, time_usage_started, time_usage_ended, cmd.csv, cmd.granularity)

        if report_type == 'TENANT' or report_type == 'ALL':
            usage_tenant(usage_client, tenant_id, time_usage_started, time_usage_ended, cmd.csv, cmd.granularity)

        if report_type == 'SPECIAL' or report_type == 'ALL':
            usage_special(usage_client, tenant_id, time_usage_started, time_usage_ended, cmd.csv, cmd.granularity)

        if report_type == 'COMPARTMENT' or report_type == 'ALL':
            usage_compartment(usage_client, tenant_id, time_usage_started, time_usage_ended, cmd.csv, cmd.granularity)

    except Exception as e:
        raise RuntimeError("\nError at main function - " + str(e))


##########################################################################
# Main Process
##########################################################################
main()
