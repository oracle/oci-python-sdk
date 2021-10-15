# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# showusage.py
#
# @author: Adi Zohar, Oct 07 2021
#
# Supports Python 3
##########################################################################
# Application Command line parameters
#
#   -c config    - OCI CLI Config
#   -t profile   - profile inside the config file
#   -p proxy     - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip          - Use Instance Principals for Authentication
#   -dt          - Use Instance Principals with delegation token for cloud shell
#   -ds date     - Start Date in YYYY-MM-DD format
#   -de date     - End Date in YYYY-MM-DD format (Not Inclusive)
#   -ld days     - Add Days Combined with Start Date (de is ignored if specified)
#   -report type - Report Type = PRODUCT, DAILY
#
#
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

version = "2021.10.07"


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
# Usage Daily by Product
##########################################################################
def usage_daily_product(usageClient, tenant_id, time_usage_started, time_usage_ended):

    try:
        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity='DAILY',
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
        for item in request_summarized_usages.data.items:
            data.append({
                'sku': item.sku_part_number,
                'sku_name': item.sku_name if item.sku_part_number in item.sku_name else item.sku_part_number + " - " + item.sku_name,
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'currency': item.currency,
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if item.currency:
                currency = item.currency
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        ################################
        # Grouped Dict
        ################################
        gdata = {}
        for item in data:
            sku = item['sku']
            if sku not in gdata:
                gdata[sku] = {'cost': item['cost'], 'quantity': item['quantity'], 'sku_name': item['sku_name'], 'currency': item['currency']}
            else:
                gdata[sku]['cost'] += item['cost']
                gdata[sku]['quantity'] += item['quantity']

        ################################
        # Compact based on SKUs
        ################################
        col = {
            'product': 65,
            'quantity': 14,
            'days': 10,
            'cost': 13,
            'month': 13,
            'year': 13
        }

        days = (max_date - min_date).days + 1

        product_header = "Product Summary for " + min_date.strftime('%m/%d/%Y') + " - " + max_date.strftime('%m/%d/%Y') + " in " + currency
        print_header(product_header, 3)
        print("")
        print(
            "Product".ljust(col['product']) +
            " Days".rjust(col['days']) +
            " Quantity".rjust(col['quantity']) +
            " Cost".rjust(col['cost']) +
            " Month-31".rjust(col['month']) +
            " Year".rjust(col['year'])
        )

        print(
            "".ljust(col['product'], '=') +
            " ".ljust(col['days'], '=') +
            " ".ljust(col['quantity'], '=') +
            " ".ljust(col['cost'], '=') +
            " ".ljust(col['month'], '=') +
            " ".ljust(col['year'], '=')
        )

        total = 0
        for item_key in sorted(gdata, key=lambda x: gdata[x]['cost']):
            item = gdata[item_key]
            if item['cost'] == 0:
                continue
            total += item['cost']
            line = item['sku_name'].ljust(col['product'])[0:col['product']]
            line += "{:8,.0f}".format(days).rjust(col['days'])
            line += "{:8,.1f}".format(item['quantity']).rjust(col['quantity'])
            line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
            line += "{:9,.0f}".format(item['cost'] / days * 31).rjust(col['month'])
            line += "{:9,.0f}".format(item['cost'] / days * 365).rjust(col['year'])
            print(line)

        # Total
        print(
            "".ljust(col['product'], '=') +
            " ".ljust(col['days'], '=') +
            " ".ljust(col['quantity'], '=') +
            " ".ljust(col['cost'], '=') +
            " ".ljust(col['month'], '=') +
            " ".ljust(col['year'], '=')
        )
        print(
            "Total ".ljust(col['product'] + col['days'] + col['quantity']) +
            " {:8,.1f}".format(total).rjust(col['cost']) +
            " {:9,.0f}".format(total / days * 31).rjust(col['month']) +
            " {:9,.0f}".format(total / days * 365).rjust(col['year'])
        )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_daily_product' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_daily_product' - " + str(e))


##########################################################################
# Usage Daily Summary
##########################################################################
def usage_daily_summary(usageClient, tenant_id, time_usage_started, time_usage_ended):

    try:

        # oci.usage_api.models.RequestSummarizedUsagesDetails
        requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=tenant_id,
            granularity='DAILY',
            query_type='COST',
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
        for item in request_summarized_usages.data.items:
            data.append({
                'day': item.time_usage_started.strftime('%Y-%m-%d'),
                'cost': item.computed_amount if item.computed_amount else 0,
                'quantity': item.computed_quantity if item.computed_quantity else 0,
                'currency': item.currency,
                'time_usage_started': item.time_usage_started,
                'time_usage_ended': item.time_usage_ended
            })
            if not min_date or item.time_usage_started < min_date:
                min_date = item.time_usage_started
            if not max_date or item.time_usage_started > max_date:
                max_date = item.time_usage_started

        ################################
        # Grouped Dict
        ################################
        gdata = {}
        for item in data:
            day = item['day']
            if day not in gdata:
                gdata[day] = {'cost': item['cost'], 'quantity': item['quantity'], 'currency': item['currency']}
            else:
                gdata[day]['cost'] += item['cost']
                gdata[day]['quantity'] += item['quantity']

        ################################
        # Compact based on SKUs
        ################################
        col = {
            'day': 15,
            'cost': 15,
            'month': 15,
            'year': 15
        }

        product_header = "Daily Summary for " + min_date.strftime('%m/%d/%Y') + " - " + max_date.strftime('%m/%d/%Y')
        print_header(product_header, 3)
        print("")
        print(
            "Day".ljust(col['day']) +
            " Cost".rjust(col['cost']) +
            " Month-31".rjust(col['month']) +
            " Year".rjust(col['year'])
        )

        print(
            "".ljust(col['day'], '=') +
            " ".ljust(col['cost'], '=') +
            " ".ljust(col['month'], '=') +
            " ".ljust(col['year'], '=')
        )

        total = 0
        for item_key in sorted(gdata, key=lambda x: x):
            item = gdata[item_key]
            if item['cost'] == 0:
                continue
            total += item['cost']
            line = item_key.ljust(col['day'])[0:col['day']]
            line += "{:8,.1f}".format(item['cost']).rjust(col['cost'])
            line += "{:9,.0f}".format(item['cost'] * 31).rjust(col['month'])
            line += "{:9,.0f}".format(item['cost'] * 365).rjust(col['year'])
            print(line)

        # Total
        print(
            "".ljust(col['day'], '=') +
            " ".ljust(col['cost'], '=') +
            " ".ljust(col['month'], '=') +
            " ".ljust(col['year'], '=')
        )
        print(
            "Total ".ljust(col['day']) +
            " {:8,.1f}".format(total).rjust(col['cost'])
        )

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'usage_daily_summary' - " + str(e))

    except Exception as e:
        print("\nException Error at 'usage_daily_summary' - " + str(e))


##########################################################################
# Main Process
##########################################################################
def main():

    # Get Command Line Parser
    # parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(usage=argparse.SUPPRESS, formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=130))
    parser.add_argument('-c', default="", dest='config_file', help='OCI CLI Config file')
    parser.add_argument('-t', default="", dest='config_profile', help='Config Profile inside the config file')
    parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
    parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
    parser.add_argument('-dt', action='store_true', default=False, dest='is_delegation_token', help='Use Delegation Token for Authentication')
    parser.add_argument("-ds", default=None, dest='date_start', help="Start Date - format YYYY-MM-DD", type=valid_date_type)
    parser.add_argument("-de", default=None, dest='date_end', help="End Date - format YYYY-MM-DD, (Not Inclusive)", type=valid_date_type)
    parser.add_argument("-days", default=None, dest='days', help="Add Days Combined with Start Date (de is ignored if specified)", type=int)
    parser.add_argument("-report", default="ALL", dest='report', help="Report Type = PRODUCT / DAILY / ALL ( Default = ALL )")
    cmd = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return

    if not cmd.report or not (cmd.report == "DAILY" or cmd.report == "PRODUCT" or cmd.report == "ALL"):

        parser.print_help()
        print("")
        print("**********************************************************")
        print("***          You must specify report type !            ***")
        print("***   DAILY   = Daily cost                             ***")
        print("***   PRODUCT = Product Summary Cost                   ***")
        print("***   ALL     = All Reports                            ***")
        print("**********************************************************")
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
    print("Disclaimer      : This is not an official Oracle application,  It does not supported by Oracle, It should NOT be used for utilization calculation purposes !")
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

    if days > 93:
        print("\n!!! Error, Max 93 days period allowed, input is " + str(days) + " days, !!!")
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
        print("\nConnecting to UsageAPI Service...")
        usage_client = oci.usage_api.UsageapiClient(config, signer=signer)
        if cmd.proxy:
            usage_client.base_client.session.proxies = {'https': cmd.proxy}

        if report_type == 'DAILY' or report_type == 'ALL':
            usage_daily_summary(usage_client, tenant_id, time_usage_started, time_usage_ended)

        if report_type == 'PRODUCT' or report_type == 'ALL':
            usage_daily_product(usage_client, tenant_id, time_usage_started, time_usage_ended)

    except Exception as e:
        raise RuntimeError("\nError at main function - " + str(e))


##########################################################################
# Main Process
##########################################################################
main()
